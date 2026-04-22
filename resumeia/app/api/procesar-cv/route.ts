import { NextRequest, NextResponse } from "next/server";
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

async function mejorarCV(cv: string, puesto: string, idioma: string, estilo: string) {
  const msg = await client.messages.create({
    model: "claude-haiku-4-5-20251001",
    max_tokens: 2000,
    messages: [{
      role: "user",
      content: `Sos un experto en recursos humanos y redacción de CVs profesionales.

Mejorar el siguiente CV en estilo "${estilo}" para el puesto de "${puesto}".
El resultado debe estar en ${idioma}.

Reglas:
- Mejorá la redacción para que suene más profesional e impactante
- Usá verbos de acción fuertes (logré, desarrollé, lideré, implementé)
- Agregá métricas si es posible (ej: "aumenté ventas un 30%")
- Adaptá el tono al estilo pedido: formal=conservador, creativo=dinámico, ejecutivo=liderazgo
- Mantené la información verídica del CV original
- Formato limpio y legible

CV ORIGINAL:
${cv}

Respondé SOLO con el CV mejorado, sin explicaciones adicionales.`
    }]
  });
  return (msg.content[0] as { text: string }).text;
}

async function generarCoverLetter(cv: string, puesto: string, idioma: string) {
  const msg = await client.messages.create({
    model: "claude-haiku-4-5-20251001",
    max_tokens: 1000,
    messages: [{
      role: "user",
      content: `Basándote en este CV, escribí una cover letter profesional para el puesto de "${puesto}" en ${idioma}.

CV:
${cv}

La carta debe:
- Tener apertura impactante (no "Me dirijo a usted...")
- Destacar 2-3 logros clave del CV
- Mostrar conocimiento del rol
- Cierre con call-to-action
- Máximo 3 párrafos

Respondé SOLO con la cover letter.`
    }]
  });
  return (msg.content[0] as { text: string }).text;
}

async function generarTips(cv: string, puesto: string, idioma: string) {
  const msg = await client.messages.create({
    model: "claude-haiku-4-5-20251001",
    max_tokens: 800,
    messages: [{
      role: "user",
      content: `Basándote en este CV y el puesto de "${puesto}", dá 5 tips específicos para la entrevista en ${idioma}.

CV:
${cv}

Los tips deben ser:
- Específicos al perfil de esta persona
- Prácticos y accionables
- Incluir posibles preguntas difíciles y cómo responderlas

Formato: lista numerada. Solo los 5 tips, sin introducción.`
    }]
  });
  return (msg.content[0] as { text: string }).text;
}

export async function POST(req: NextRequest) {
  try {
    const { cv, puesto, idioma } = await req.json();

    if (!cv || !puesto || !idioma) {
      return NextResponse.json({ error: "Faltan datos" }, { status: 400 });
    }

    const [cvFormal, cvCreativo, cvEjecutivo, coverLetter, tips] = await Promise.all([
      mejorarCV(cv, puesto, idioma, "formal"),
      mejorarCV(cv, puesto, idioma, "creativo"),
      mejorarCV(cv, puesto, idioma, "ejecutivo"),
      generarCoverLetter(cv, puesto, idioma),
      generarTips(cv, puesto, idioma),
    ]);

    return NextResponse.json({ cvFormal, cvCreativo, cvEjecutivo, coverLetter, tips });
  } catch (error) {
    console.error("Error procesando CV:", error);
    return NextResponse.json({ error: "Error procesando el CV" }, { status: 500 });
  }
}
