#!/usr/bin/env python3
"""
Bot de DMs automáticos para Instagram.
Escucha webhooks de Meta y responde con info de clases cuando alguien comenta.
"""

from __future__ import annotations

import hmac
import hashlib
import json
import logging
import os
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import PlainTextResponse

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

app = FastAPI()

# ── Config desde env ──────────────────────────────────────────────────────────
VERIFY_TOKEN   = os.environ["VERIFY_TOKEN"]          # cualquier string secreto tuyo
APP_SECRET     = os.environ["APP_SECRET"]            # App Secret de Meta Developer Console
PAGE_TOKEN     = os.environ["PAGE_TOKEN"]            # Page Access Token (largo plazo)
TRIGGER_WORDS  = [w.strip().lower() for w in os.environ.get("TRIGGER_WORDS", "mas info,más info,info,más información").split(",")]
GRAPH_VERSION  = os.environ.get("GRAPH_VERSION", "v21.0")
GRAPH_API      = f"https://graph.facebook.com/{GRAPH_VERSION}"

# ── Mensaje de respuesta ──────────────────────────────────────────────────────
DM_TEXT = """Hola ¿cómo te va? Ahí te paso la info sobre las clases :)

🎯 ¿Qué vas a lograr?
Desde la primera clase tocás algo real: una canción que te guste, no ejercicios al pepe. Para eso, antes de arrancar me contás 3 bandas que te vuelen la cabeza. Ahí diseño todo en función de tu estilo. Las clases son 100% tuyas: tu nivel, tu ritmo, lo que vos querés tocar.

🧠 ¿Cómo funciona?
Trabajamos en ciclos de 4 clases — una por semana, 1 hora cada una. 4 clases es el tiempo perfecto para que aprendas una canción completa, resuelvas lo que te traba y sientas que progresaste de verdad. Después de las 4, decidís: ¿seguís con otro ciclo? ¿cambiás de nivel? ¿tomás un respiro? Sin ataduras.

🚀 Arrancás cuando quieras. La próxima semana, el próximo mes — como te acomode.

📍 Ubicación: Echesortu, Rioja al 4000. Zona tranquila, fácil de llegar 🏡

🎒 ¿Qué traés?
Solo un anotador. Guitarra, espacio y amplificador — todo acá.

🔞 Edad mínima: las clases están orientadas a personas a partir de los 10 años.

💸 Inversión: $73.000 el ciclo de 4 clases (salen $18.250 por clase). Menos que una pizza con amigos 🍕
y te llevás algo que te queda para siempre

📅 Clases disponibles: lunes, martes, miércoles, jueves y viernes.
Para confirmar un horario puntual, escribime directo al WhatsApp 👇
3412100466"""


# ── Helpers ───────────────────────────────────────────────────────────────────

def _verify_signature(payload: bytes, signature_header: str | None) -> bool:
    """Verifica que el webhook realmente viene de Meta."""
    if not signature_header or not signature_header.startswith("sha256="):
        return False
    expected = hmac.new(APP_SECRET.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature_header[7:])


def _send_dm(recipient_igsid: str, text: str) -> dict[str, Any]:
    """Envía un DM vía Instagram Graph API."""
    url = f"{GRAPH_API}/me/messages"
    body = json.dumps({
        "recipient": {"id": recipient_igsid},
        "message":   {"text": text},
        "messaging_type": "RESPONSE",
    }).encode()
    req = Request(
        f"{url}?access_token={PAGE_TOKEN}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except HTTPError as e:
        body_err = e.read().decode("utf-8", errors="replace")
        log.error("Graph API error %s: %s", e.code, body_err[:300])
        raise
    except URLError as e:
        log.error("Network error sending DM: %s", e)
        raise


def _is_triggered(text: str) -> bool:
    t = text.lower()
    return any(w in t for w in TRIGGER_WORDS)


# ── Rutas ─────────────────────────────────────────────────────────────────────

@app.get("/webhook")
def verify_webhook(request: Request):
    """Meta llama este endpoint para verificar el webhook al configurarlo."""
    params = dict(request.query_params)
    mode      = params.get("hub.mode")
    token     = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        log.info("Webhook verificado correctamente.")
        return PlainTextResponse(challenge)

    log.warning("Verificación fallida: mode=%s token=%s", mode, token)
    raise HTTPException(status_code=403, detail="Verificación fallida")


@app.post("/webhook")
async def receive_webhook(request: Request):
    """Recibe eventos de Meta (comentarios, mensajes)."""
    raw_body = await request.body()

    # Verificar firma (seguridad — evita requests falsos)
    sig = request.headers.get("X-Hub-Signature-256")
    if APP_SECRET and not _verify_signature(raw_body, sig):
        log.warning("Firma inválida — request ignorado")
        raise HTTPException(status_code=403, detail="Firma inválida")

    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="JSON inválido")

    log.debug("Webhook recibido: %s", json.dumps(payload)[:500])

    if payload.get("object") != "instagram":
        return Response(status_code=200)

    for entry in payload.get("entry", []):
        for change in entry.get("changes", []):
            _handle_change(change)

        # Mensajes directos (messaging_optins, messages)
        for messaging in entry.get("messaging", []):
            _handle_messaging(messaging)

    return Response(status_code=200)


def _handle_change(change: dict) -> None:
    """Procesa eventos de tipo 'changes' (comentarios en posts/ads)."""
    field = change.get("field")
    value = change.get("value", {})

    if field == "comments":
        comment_text = value.get("text", "")
        commenter_id = value.get("from", {}).get("id")

        if not commenter_id:
            return

        if _is_triggered(comment_text):
            log.info("Comentario trigger detectado de %s: %r", commenter_id, comment_text[:60])
            try:
                result = _send_dm(commenter_id, DM_TEXT)
                log.info("DM enviado: %s", result)
            except Exception as e:
                log.error("Error enviando DM a %s: %s", commenter_id, e)
        else:
            log.debug("Comentario ignorado (sin trigger): %r", comment_text[:60])


def _handle_messaging(messaging: dict) -> None:
    """Procesa eventos de messaging (story replies, opt-ins)."""
    sender_id = messaging.get("sender", {}).get("id")
    if not sender_id:
        return

    # Story reply
    if "message" in messaging:
        reply_to = messaging["message"].get("reply_to", {})
        if reply_to.get("story"):
            text = messaging["message"].get("text", "")
            if _is_triggered(text) or not text:
                log.info("Story reply de %s — enviando info", sender_id)
                try:
                    _send_dm(sender_id, DM_TEXT)
                except Exception as e:
                    log.error("Error enviando DM a %s: %s", sender_id, e)

    # Optin de historia (botón "más info" en story ad)
    if "optin" in messaging:
        log.info("Story optin de %s — enviando info", sender_id)
        try:
            _send_dm(sender_id, DM_TEXT)
        except Exception as e:
            log.error("Error enviando DM a %s: %s", sender_id, e)


@app.get("/health")
def health():
    return {"status": "ok", "trigger_words": TRIGGER_WORDS}
