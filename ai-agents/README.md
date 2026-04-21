# Equipo de Agentes IA - Negocio de Clases de Guitarra

## Agentes instalados

### 1. AI Consultant Agent (Consultoria de negocio)
- **Fuente**: `awesome-llm-apps/advanced_ai_agents/single_agent_apps/ai_consultant_agent`
- **Script**: `consultant/run_guitar_consultation.py`
- **Uso**: Consultoria estrategica sobre el taller de 4 horas

### 2. AI Sales Intelligence Agent Team (Ventas)
- **Fuente**: `awesome-llm-apps/advanced_ai_agents/multi_agent_apps/agent_teams/ai_sales_intelligence_agent_team`
- **Script**: `sales-intelligence/run_guitar_sales.py`
- **Uso**: Battle cards, prospeccion y estrategia de ventas

### 3. AI Competitor Intelligence (Analisis de competencia)
- **Fuente**: `awesome-llm-apps/advanced_ai_agents/multi_agent_apps/agent_teams/ai_competitor_intelligence_agent_team`
- **Requiere**: OpenAI + Firecrawl + Exa API keys

## Configuracion rapida

```bash
# 1. Copiar y llenar las API keys
cp .env.example .env
# Editar .env con tu GOOGLE_API_KEY

# 2. Cargar las variables
source .env  # o: export GOOGLE_API_KEY=tu-key

# 3. Correr la consultoria
python consultant/run_guitar_consultation.py

# 4. Correr el analisis de ventas
python sales-intelligence/run_guitar_sales.py

# 5. O usar la interfaz web de ADK
cd /home/user/awesome-llm-apps/advanced_ai_agents/single_agent_apps
adk web ai_consultant_agent
# Abrir: http://localhost:8000
```

## Obtener API Keys (gratis)

- **Google API Key** (Gemini): https://aistudio.google.com/app/apikey
  - Plan gratuito: 1,500 requests/dia con Gemini 1.5 Flash
- **Perplexity** (opcional): https://www.perplexity.ai/settings/api
