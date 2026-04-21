"""
AI Sales Intelligence Agent - Guitar Lessons Battle Card
Run: python run_guitar_sales.py
Requires: GOOGLE_API_KEY
"""
import asyncio
import os
import sys

sys.path.insert(0, '/home/user/awesome-llm-apps/advanced_ai_agents/multi_agent_apps/agent_teams')

from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

SALES_PROMPT = """
Necesito un analisis de ventas e inteligencia competitiva para mi negocio:

Mi producto/servicio: Clases de guitarra (individuales y talleres grupales)
Mi cliente ideal: Personas que arrancan desde 0 o que ya tienen algo de experiencia y quieren mejorar
Mi precio actual: $70,000 pesos colombianos por clase individual

Analiza la competencia de clases de guitarra online y presencial en Colombia.
Genera un battle card contra las plataformas online tipo Fender Play, JustinGuitar, o instructores locales.

Quiero saber:
1. Oportunidades de venta que no estoy aprovechando
2. Estrategia de prospeccion (donde encontrar mis clientes ideales)
3. Los primeros 5 pasos concretos para vender mas esta semana
4. Como posicionarme vs la competencia online y presencial
5. Que objeciones me van a poner y como responderlas

Hazlo especifico para un instructor independiente en Colombia.
"""

async def run_sales_analysis():
    try:
        from ai_sales_intelligence_agent_team.agent import root_agent
        APP_NAME = "ai_sales_intelligence"
    except ImportError as e:
        print(f"Error importing agent: {e}")
        print("Make sure GOOGLE_API_KEY is set and google-adk is installed")
        return

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: GOOGLE_API_KEY not set")
        print("Set it with: export GOOGLE_API_KEY=your-key-here")
        return

    session_service = InMemorySessionService()
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

    await session_service.create_session(
        app_name=APP_NAME,
        user_id="guitar-teacher",
        session_id="guitar-sales"
    )

    print("Sales Intelligence - Clases de Guitarra")
    print("=" * 50)
    print()

    message = types.Content(
        role="user",
        parts=[types.Part(text=SALES_PROMPT)]
    )

    async for event in runner.run_async(
        user_id="guitar-teacher",
        session_id="guitar-sales",
        new_message=message
    ):
        if event.is_final_response():
            print(event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(run_sales_analysis())
