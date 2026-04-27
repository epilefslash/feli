#!/usr/bin/env python3
"""
Conecta a Windsor.ai y analiza campañas de Facebook Ads.

Uso:
    python3 scripts/windsor_facebook_analysis.py
    python3 scripts/windsor_facebook_analysis.py --date-preset last_7d
    python3 scripts/windsor_facebook_analysis.py --date-from 2026-01-01 --date-to 2026-01-31
    WINDSOR_API_KEY=xxx python3 scripts/windsor_facebook_analysis.py

Sin dependencias externas: usa solo la stdlib de Python 3.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

WINDSOR_ENDPOINT = "https://connectors.windsor.ai/all"

DEFAULT_API_KEY = "fb7b9e885b3576154de891c8adf5e9bc3d1b"

DEFAULT_FACEBOOK_ACCOUNTS = [
    "facebook__2583844138546343",
    "facebook__273087505",
    "facebook__382322122763045",
]

FIELDS = [
    "account_name",
    "campaign",
    "datasource",
    "date",
    "source",
    "spend",
    "impressions",
    "clicks",
    "ctr",
    "cpc",
]


def fetch_windsor(api_key: str, accounts: Iterable[str], date_preset: str | None,
                  date_from: str | None, date_to: str | None) -> list[dict[str, Any]]:
    params = {
        "api_key": api_key,
        "fields": ",".join(FIELDS),
        "select_accounts": ",".join(accounts),
    }
    if date_from and date_to:
        params["date_from"] = date_from
        params["date_to"] = date_to
    else:
        params["date_preset"] = date_preset or "last_28d"

    url = f"{WINDSOR_ENDPOINT}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": "windsor-fb-analysis/1.0"})

    try:
        with urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if hasattr(e, "read") else ""
        sys.exit(f"[error] Windsor respondió {e.code}: {body[:300]}")
    except URLError as e:
        sys.exit(f"[error] No se pudo conectar a Windsor: {e}")

    if isinstance(payload, dict) and "data" in payload:
        return payload["data"]
    if isinstance(payload, list):
        return payload
    sys.exit(f"[error] Formato inesperado de Windsor: {type(payload).__name__}")


def to_float(v: Any) -> float:
    if v is None or v == "":
        return 0.0
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def keep_facebook(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for r in rows:
        ds = (r.get("datasource") or r.get("source") or "").lower()
        if "facebook" in ds:
            out.append(r)
    return out


def fmt_money(x: float) -> str:
    return f"${x:,.2f}"


def fmt_int(x: float) -> str:
    return f"{int(round(x)):,}"


def fmt_pct(x: float) -> str:
    return f"{x:.2f}%"


def hr(char: str = "─", width: int = 72) -> str:
    return char * width


def section(title: str) -> None:
    print()
    print(hr("═"))
    print(f"  {title}")
    print(hr("═"))


def aggregate(rows: list[dict[str, Any]], key: str | None = None
              ) -> dict[str, dict[str, float]]:
    buckets: dict[str, dict[str, float]] = defaultdict(
        lambda: {"spend": 0.0, "impressions": 0.0, "clicks": 0.0, "rows": 0.0}
    )
    for r in rows:
        k = r.get(key) if key else "TOTAL"
        if not k:
            k = "(sin valor)"
        b = buckets[k]
        b["spend"] += to_float(r.get("spend"))
        b["impressions"] += to_float(r.get("impressions"))
        b["clicks"] += to_float(r.get("clicks"))
        b["rows"] += 1
    for b in buckets.values():
        b["ctr"] = (b["clicks"] / b["impressions"] * 100) if b["impressions"] else 0.0
        b["cpc"] = (b["spend"] / b["clicks"]) if b["clicks"] else 0.0
        b["cpm"] = (b["spend"] / b["impressions"] * 1000) if b["impressions"] else 0.0
    return buckets


def print_general(rows: list[dict[str, Any]]) -> None:
    section("MÉTRICAS GENERALES")
    if not rows:
        print("  (sin datos)")
        return
    totals = aggregate(rows)["TOTAL"]
    accounts = sorted({r.get("account_name") or "(sin nombre)" for r in rows})
    dates = sorted({r.get("date") for r in rows if r.get("date")})

    print(f"  Cuentas analizadas : {len(accounts)} → {', '.join(accounts)}")
    if dates:
        print(f"  Rango de fechas    : {dates[0]} → {dates[-1]} ({len(dates)} días)")
    print(f"  Filas en respuesta : {int(totals['rows'])}")
    print()
    print(f"  Inversión total    : {fmt_money(totals['spend'])}")
    print(f"  Impresiones        : {fmt_int(totals['impressions'])}")
    print(f"  Clics              : {fmt_int(totals['clicks'])}")
    print(f"  CTR promedio       : {fmt_pct(totals['ctr'])}")
    print(f"  CPC promedio       : {fmt_money(totals['cpc'])}")
    print(f"  CPM promedio       : {fmt_money(totals['cpm'])}")


def print_by_campaign(rows: list[dict[str, Any]]) -> None:
    section("RENDIMIENTO POR CAMPAÑA")
    if not rows:
        print("  (sin datos)")
        return
    by_camp = aggregate(rows, key="campaign")
    ordered = sorted(by_camp.items(), key=lambda kv: kv[1]["spend"], reverse=True)

    name_w = max(20, min(40, max(len(k) for k, _ in ordered)))
    header = f"  {'Campaña':<{name_w}}  {'Gasto':>10}  {'Impr.':>10}  {'Clics':>8}  {'CTR':>7}  {'CPC':>8}"
    print(header)
    print("  " + hr("─", len(header) - 2))
    for name, m in ordered:
        label = (name[: name_w - 1] + "…") if len(name) > name_w else name
        print(
            f"  {label:<{name_w}}  {fmt_money(m['spend']):>10}  "
            f"{fmt_int(m['impressions']):>10}  {fmt_int(m['clicks']):>8}  "
            f"{fmt_pct(m['ctr']):>7}  {fmt_money(m['cpc']):>8}"
        )

    if len(ordered) >= 2:
        print()
        top = ordered[0]
        bottom = ordered[-1]
        print(f"  → Top spend     : {top[0]} ({fmt_money(top[1]['spend'])})")
        print(f"  → Menor spend   : {bottom[0]} ({fmt_money(bottom[1]['spend'])})")
        best_ctr = max(ordered, key=lambda kv: kv[1]["ctr"])
        worst_ctr = min(
            (kv for kv in ordered if kv[1]["impressions"] > 0),
            key=lambda kv: kv[1]["ctr"],
            default=None,
        )
        print(f"  → Mejor CTR     : {best_ctr[0]} ({fmt_pct(best_ctr[1]['ctr'])})")
        if worst_ctr:
            print(f"  → Peor CTR      : {worst_ctr[0]} ({fmt_pct(worst_ctr[1]['ctr'])})")


def print_temporal(rows: list[dict[str, Any]]) -> None:
    section("TENDENCIA TEMPORAL (POR DÍA)")
    if not rows:
        print("  (sin datos)")
        return
    by_date = aggregate(rows, key="date")
    ordered = sorted(by_date.items(), key=lambda kv: kv[0] or "")
    if not ordered:
        print("  (sin fechas en los datos)")
        return

    max_spend = max((m["spend"] for _, m in ordered), default=0.0) or 1.0
    bar_w = 30

    print(f"  {'Fecha':<12}  {'Gasto':>10}  {'Impr.':>10}  {'Clics':>7}  {'CTR':>7}  Gráfico")
    print("  " + hr("─", 70))
    total_spend = 0.0
    for date, m in ordered:
        bar_len = int(round((m["spend"] / max_spend) * bar_w)) if m["spend"] > 0 else 0
        bar = "█" * bar_len
        date_str = date or "(sin fecha)"
        print(
            f"  {date_str:<12}  {fmt_money(m['spend']):>10}  "
            f"{fmt_int(m['impressions']):>10}  {fmt_int(m['clicks']):>7}  "
            f"{fmt_pct(m['ctr']):>7}  {bar}"
        )
        total_spend += m["spend"]

    print()
    avg_daily = total_spend / len(ordered) if ordered else 0.0
    peak_date, peak_metrics = max(ordered, key=lambda kv: kv[1]["spend"])
    print(f"  → Días con datos    : {len(ordered)}")
    print(f"  → Gasto diario prom.: {fmt_money(avg_daily)}")
    print(f"  → Día pico          : {peak_date} ({fmt_money(peak_metrics['spend'])})")

    if len(ordered) >= 4:
        half = len(ordered) // 2
        first_half_spend = sum(m["spend"] for _, m in ordered[:half])
        second_half_spend = sum(m["spend"] for _, m in ordered[half:])
        delta = second_half_spend - first_half_spend
        pct = (delta / first_half_spend * 100) if first_half_spend else 0.0
        trend = "↑" if delta > 0 else ("↓" if delta < 0 else "→")
        print(
            f"  → Tendencia         : {trend} 2da mitad vs 1ra: "
            f"{fmt_money(delta)} ({pct:+.1f}%)"
        )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Análisis de Facebook Ads vía Windsor.ai")
    p.add_argument("--api-key", default=os.environ.get("WINDSOR_API_KEY", DEFAULT_API_KEY),
                   help="API key de Windsor (o env WINDSOR_API_KEY)")
    p.add_argument("--accounts", default=",".join(DEFAULT_FACEBOOK_ACCOUNTS),
                   help="IDs de cuenta separados por coma (formato facebook__XXXX)")
    p.add_argument("--date-preset", default="last_28d",
                   help="Preset de Windsor: last_7d, last_14d, last_28d, last_30d, ...")
    p.add_argument("--date-from", help="Fecha inicio YYYY-MM-DD (anula --date-preset)")
    p.add_argument("--date-to", help="Fecha fin YYYY-MM-DD (anula --date-preset)")
    p.add_argument("--raw", action="store_true",
                   help="Imprime el JSON crudo de Windsor y termina")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    accounts = [a.strip() for a in args.accounts.split(",") if a.strip()]

    print(hr("═"))
    print("  Windsor.ai → Facebook Ads · Análisis")
    print(hr("═"))
    print(f"  Generado : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if args.date_from and args.date_to:
        print(f"  Rango    : {args.date_from} → {args.date_to}")
    else:
        print(f"  Preset   : {args.date_preset}")
    print(f"  Cuentas  : {len(accounts)}")

    rows = fetch_windsor(
        api_key=args.api_key,
        accounts=accounts,
        date_preset=args.date_preset,
        date_from=args.date_from,
        date_to=args.date_to,
    )

    if args.raw:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return

    fb_rows = keep_facebook(rows)
    if not fb_rows:
        print()
        print("  [aviso] La respuesta no contiene filas de Facebook.")
        print(f"  Filas totales recibidas: {len(rows)}")
        if rows:
            sources = sorted({(r.get('datasource') or r.get('source') or '?') for r in rows})
            print(f"  Datasources presentes : {', '.join(sources)}")
        return

    print_general(fb_rows)
    print_by_campaign(fb_rows)
    print_temporal(fb_rows)
    print()


if __name__ == "__main__":
    main()
