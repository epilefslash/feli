"""
AI Consultant Agent - Guitar Lessons Business Consultation
Run: python run_guitar_consultation.py
Requires: GOOGLE_API_KEY and optionally PERPLEXITY_API_KEY
"""
import asyncio
import os
import sys

# Add awesome-llm-apps to path
sys.path.insert(0, '/home/user/awesome-llm-apps/advanced_ai_agents/single_agent_apps')

from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

CONSULTATION_PROMPT = """
Soy instructor de guitarra independiente (negocio unipersonal).

Industria: Clases de guitarra (educacion musical)
Tamano del negocio: Solo yo, trabajo independiente
Problema principal: Quiero concentrar en UN encuentro de 4 horas (taller intensivo de guitarra)
lo que normalmente se da en 4 clases separadas.

Mi situacion actual:
- Doy clases individuales y en grupo
- Quiero crear un formato de taller de 1 dia (4 horas) para principiantes o intermedios
- Precio actual de mis clases: $70,000 (pesos colombianos) por clase
- No tengo equipo, todo lo hago yo

Necesito recomendaciones concretas que pueda implementar ESTA SEMANA para:
1. Estructurar el taller de 4 horas (que cubrir, como dividir el tiempo)
2. Como promocionar y vender este taller
3. Que precio ponerle al taller
4. Como encontrar los primeros participantes

Dame un plan de accion especifico para los proximos 7 dias.
"""

async def run_consultation():
    try:
        from ai_consultant_agent.ai_consultant_agent import root_agent, APP_NAME
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
        session_id="guitar-consultation"
    )

    print("Consultoria de negocio - Clases de Guitarra")
    print("=" * 50)
    print()

    message = types.Content(
        role="user",
        parts=[types.Part(text=CONSULTATION_PROMPT)]
    )

    async for event in runner.run_async(
        user_id="guitar-teacher",
        session_id="guitar-consultation",
        new_message=message
    ):
        if event.is_final_response():
            print(event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(run_consultation())
