# Sistema de Cultivo Hidropónico Automatizado — Cannabis (2 plantas / 150 g)

> ⚠️ **Aviso legal (leer antes de comprar nada):** el cultivo de cannabis está regulado de forma muy distinta según el país, provincia o estado. Antes de adquirir cualquier componente verificá tu legislación local (cantidad de plantas permitidas, autocultivo registrado, uso medicinal vs. recreativo, cultivo en espacio cerrado, etc.). Ejemplos de 2026: Uruguay y Canadá permiten autocultivo registrado (hasta 4-6 plantas/hogar); varios estados de EE.UU. lo permiten con límites propios; en España existe un vacío legal para consumo/cultivo estrictamente privado y no visible (jurisprudencia de "consumo compartido", no una ley clara); México permite autocultivo con permiso de autoconsumo tras fallos de la Corte; en la mayoría de Europa, Asia y buena parte de Latinoamérica **es ilegal**. Este documento es una guía técnica de ingeniería (hidroponía + IoT) y asume que quien lo use cultiva en un contexto legal. Ante la duda, consultá con un abogado local.

---

## 🏗️ ARQUITECTURA DEL SISTEMA

### Método elegido: **RDWC (Recirculating Deep Water Culture)**

| Método | Pros | Contras | ¿Para este proyecto? |
|---|---|---|---|
| **DWC/RDWC** | Simple mecánicamente (sin goteros que se tapan), muy tolerante a fallos, raíces con máxima oxigenación → crecimiento rápido, un solo punto de control de pH/EC si es recirculante | Requiere control estricto de temp. del agua (riesgo *Pythium*/pudrición de raíz si el agua supera ~22 °C) | ✅ **Recomendado** — es el método hidropónico más popular y mejor documentado específicamente para cannabis casero |
| **NFT** | Bajo consumo de agua, buena para raíces pequeñas | Con cannabis las raíces crecen densas y gruesas, tienden a tapar el canal; una falla de bomba de pocos minutos puede matar la planta (sin buffer de agua) | ❌ Más frágil para 2 plantas de floración larga |
| **Ebb & Flow** | Buen balance agua/aire, funciona con sustrato (coco/perlita) | Más partes móviles (bandeja de inundación, temporizador de drenaje), mayor riesgo mecánico (fuga, bomba pegada) | ⚠️ Válido pero más complejo de automatizar que DWC sin beneficio extra para solo 2 plantas |

**Por qué RDWC y no 2 baldes DWC independientes:** con 2 baldes conectados a un **reservorio central**, necesitás **un solo set de sensores y bombas dosificadoras** para ambas plantas en vez de duplicarlo. Esto reduce el costo de automatización a la mitad y simplifica la lógica de control.

### Diagrama conceptual

```
┌───────────────────────────────────────────────────────────────────┐
│                     CARPA DE CULTIVO (80×80×180 cm)                │
│                                                                     │
│   [LED grow light — regulable, colgado con poleas ajustables]      │
│         │                                                          │
│   ┌───────────────┐            ┌───────────────┐                   │
│   │  Balde DWC #1 │            │  Balde DWC #2 │                   │
│   │  19-20 L      │            │  19-20 L      │                   │
│   │  net pot+arlita│           │  net pot+arlita│                  │
│   │  piedra difusora│          │  piedra difusora│                 │
│   └───────┬───────┘            └───────┬───────┘                   │
│           │   tubería PVC 1/2" + uniseal│                          │
│           └──────────────┬──────────────┘                          │
│                           │                                        │
│                  ┌────────▼─────────┐                              │
│                  │   RESERVORIO      │  ← sonda pH                 │
│                  │   central 40-60 L │  ← sonda EC/TDS             │
│                  │                   │  ← sonda temp. agua (DS18B20)│
│                  │                   │  ← bomba de aire (24/7)     │
│                  │                   │  ← bomba de recirculación   │
│                  │                   │  ← 4 bombas peristálticas   │
│                  │                   │    (pH+/pH-/Nutr.A/Nutr.B)  │
│                  └────────┬──────────┘                             │
│                           │ sensor de nivel (flotador+ultrasónico) │
│                           │ ← electroválvula de rellenado (agua)   │
│                                                                     │
│   [Extractor + filtro de carbón] ──────────────► al exterior       │
│   [Ventilador de circulación interna — siempre encendido]           │
│   [Sensor temp/humedad aire] [Sensor de luz/lux]                    │
└───────────────────────────────────────────────────────────────────┘
```

**Tamaño de carpa recomendado:** 80×80×180 cm (da espacio a los 2 baldes + reservorio + zona de mangueras). Con entrenamiento LST/SCROG y objetivo modesto de 150 g totales, hasta una 60×60×160 cm alcanzaría, pero 80×80 deja margen de maniobra para la parte de automatización (mucho más importante en este proyecto que el tamaño del dosel).

**Recomendación de genética:** para el primer ciclo, usar semillas **autoflorecientes** (fotoperiodo fijo 18/6 todo el ciclo, sin necesidad de cambiar el ciclo de luz, cosecha en 10-12 semanas desde germinación). Simplifica una variable entera del sistema. Fotoperiódicas también funcionan (el cambio 18/6→12/12 es trivial de automatizar con un enchufe inteligente), pero alargan el proyecto y agregan una decisión manual de "cuándo cambiar".

---

## 📋 COMPONENTES CRÍTICOS A AUTOMATIZAR

| Parámetro | Sensor | Actuador | Rango objetivo (cannabis) |
|---|---|---|---|
| Riego/recirculación | Nivel de agua | Bomba de recirculación | Circular 10-15 min cada 4 h (no hace falta "riego" como en sustrato — las raíces están sumergidas) |
| pH | Sonda de pH | Bombas peristálticas pH Up/Down | 5.5 – 6.2 (hidro) |
| EC/TDS | Sonda EC/TDS | Bombas peristálticas de nutrientes | Plántula 0.4-0.8 mS/cm · Vegetativo 1.2-1.8 · Floración 1.6-2.2 |
| Temp. del agua | DS18B20 sumergible | Alarma / chiller (fase 4) | 18-22 °C (>22 °C = riesgo de hongo de raíz) |
| Humedad/temp. aire | SHT31 o DHT22 | Extractor (velocidad variable) | Veg: 22-28 °C / 55-70% HR · Floración: 20-26 °C / 40-50% HR |
| Luz | Sensor lux (BH1750) | Enchufe inteligente + dimmer del driver LED | 18/6 (auto o veg) → 12/12 (floración fotoperiódica) |
| Ventilación | Temp/humedad | Extractor + filtro de carbón | 1 renovación de aire completa cada 1-3 min |
| CO2 | — | (opcional, fase 4) | No necesario para el objetivo de 150 g en carpa pequeña |

---

## 📋 LISTA COMPLETA DE COMPONENTES

> Precios aproximados en USD, 2026. AliExpress suele ser 30-50% más barato pero con 3-6 semanas de envío y sin garantía real; Amazon/tiendas de hidroponía (GrowGeneration, Hydrobuilder) son más caras pero con soporte y envío rápido. Para electrónica (ESP32, sensores DFRobot/Atlas) AliExpress es perfectamente confiable si comprás vendedores con buena reputación (DFRobot Official, Atlas Scientific no vende ahí — solo en su web/Amazon).

### Estructura y cultivo

| Componente | Modelo / rango | Especificación | Precio | Dónde | Económico vs. premium |
|---|---|---|---|---|---|
| Carpa de cultivo | AC Infinity Cloudlab 743 (80×80×180) | Mylar 98% reflectancia, tela gruesa, cierres reforzados | $140-160 | Amazon / AC Infinity store | Económico: VIVOSUN 80×80×180 ($75-90, Amazon/AliExpress) |
| Baldes DWC | Cubo 19-20 L + tapa con net pot 15-20 cm | Opaco (evita algas), con orificio para uniseal | $12-18 c/u ($25-35 el par) | Ferretería local + net pots en AliExpress/Amazon | Kit premium: "Current Culture Under Current" ($250+, no justifica para 2 plantas) |
| Reservorio central | Contenedor opaco 40-60 L con tapa | Con salida para bulkhead/uniseal | $20-25 | Ferretería / Amazon | — |
| Uniseals + tubería | Uniseal 1/2"-3/4" + manguera PVC/silicona | Conexión baldes↔reservorio | $15-20 total | AliExpress / ferretería hidroponía | — |
| Sustrato inerte | Arlita (bolitas de arcilla) o hydroton | Para net pots, no retiene nutrientes en exceso | $10-15 (bolsa 10L) | Vivero / Amazon | — |

### Riego, oxigenación y bombeo

| Componente | Modelo | Especificación | Precio | Dónde |
|---|---|---|---|---|
| Bomba de aire | EcoPlus 1 Air 1 (7W) o VIVOSUN dual outlet 6W | 2 salidas, silenciosa | $20-25 | Amazon/AliExpress |
| Piedras difusoras | 4" air stone x2-4 | Micro-burbuja | $6-10 (pack) | AliExpress |
| Bomba de recirculación | Bomba sumergible 400-800 L/h, 12-24V DC (para poder controlarla con relé de bajo voltaje) | Cabezal ~1-1.5 m | $15-25 | Amazon/AliExpress |
| Electroválvula rellenado | Solenoide 12V NC 1/2" | Para top-off automático desde tanque de agua osmotizada/reposada | $10-15 | AliExpress |

### Sensores

| Sensor | Modelo económico | Modelo premium | Precio |
|---|---|---|---|
| pH | DFRobot Gravity Analog pH Sensor Kit V2 | Atlas Scientific pH EZO Kit | $45-60 / $110-130 |
| EC/TDS | DFRobot Gravity Analog EC Sensor Kit | Atlas Scientific EC EZO Kit | $50-65 / $150-170 |
| Temp. agua | DS18B20 sumergible (impermeable) | — (es el estándar) | $4-6 |
| Temp/humedad aire | DHT22/AM2302 | SHT31 (más preciso, ±2%) | $8-10 / $12-15 |
| Nivel de agua | Flotador (float switch) x2 (redundancia) | + sensor ultrasónico JSN-SR04T (sin contacto, no se ensucia) | $5 c/u / +$8 |
| Luz (lux) | BH1750 (I2C) | Sensor PAR/PPFD (Apogee o clon chino ~$60-80) | $3-5 / $60-300 |

**Nota sobre sensores baratos de AliExpress (ej. PH-4502C a $10):** funcionan, pero derivan rápido y necesitan recalibración semanal. Para un sistema que se supone "automatizado" (sin supervisión constante), vale la pena el salto a DFRobot Gravity (mejor relación precisión/precio) en vez de los clones ultra baratos.

### Controlador y electrónica de control

| Componente | Modelo | Uso | Precio |
|---|---|---|---|
| Controlador central | Raspberry Pi 4B (4GB) + fuente + case + microSD 32GB | Corre Home Assistant OS (dashboard + automatizaciones + notificaciones) | $70-90 |
| Nodo de sensores/actuadores | ESP32 DevKitC x1-2 | Corre ESPHome, se conecta a HA por WiFi/MQTT, lee sensores y controla relés de bajo voltaje | $8-10 c/u |
| Módulo de relés | Relé 4 u 8 canales, 5V, optoaislado | Control de bombas dosificadoras y electroválvula (circuitos 12V DC) | $8-12 |
| Bombas dosificadoras | Bomba peristáltica 12V (genérica, tipo Kamoer/DIY) x4 (pH+, pH−, Nutriente A, Nutriente B) | Dosificación de precisión en mL | $12-15 c/u ($50-60 el set) |
| Fuente 12V | Fuente conmutada 12V 5A (Mean Well o genérica) | Alimenta bombas dosificadoras + electroválvula | $12-18 |
| Enchufes inteligentes (cargas AC) | Shelly Plug S o Sonoff S31 x4 (luz, extractor, bomba de aire, bomba de recirculación) | **Controlan las cargas de 220/110V — evita cablear alto voltaje a mano**, se integran nativamente a Home Assistant | $10-15 c/u ($45-60 el set) |

> 🔒 **Decisión de seguridad clave:** todo lo que sea corriente alterna (luz, extractor, bombas de 110/220V) se controla con **enchufes inteligentes certificados** (Shelly/Sonoff), no con relés armados a mano. El cableado DIY con Arduino/ESP32 se reserva **solo** para circuitos de 12V DC (bombas dosificadoras, electroválvula). Esto es más caro que un relé de $2, pero elimina el riesgo de electrocución/incendio de cablear 220V sin experiencia.

### Iluminación

| Componente | Modelo económico | Modelo premium | Precio |
|---|---|---|---|
| LED grow light | Mars Hydro TS 600 (~100W real) | Spider Farmer SF1000D (100W real, diodos Samsung LM301B, dimmer) | $65-75 / $110-130 |
| Timer/control | (reemplazado por enchufe inteligente, ver arriba) | — | — |

Con 100W reales sobre 2 plantas en 0.64 m² de dosel, la densidad de potencia es más que suficiente para el objetivo modesto de 150 g totales.

### Ventilación y ambiente

| Componente | Modelo económico | Modelo premium | Precio |
|---|---|---|---|
| Extractor | VIVOSUN 4" inline fan | AC Infinity CLOUDLINE T4 (con control propio de temp/humedad) | $30-38 / $65-75 |
| Filtro de carbón | Genérico 4" | VIVOSUN/AC Infinity 4" | $25-35 |
| Ventilador circulación | Clip fan USB/12V oscilante | — | $12-18 |

⚠️ El filtro de carbón **no es opcional**: el olor del cannabis en floración es intenso y es lo primero que genera problemas de vecindad o legales, incluso donde el cultivo es legal.

### Medidores manuales de respaldo

| Componente | Uso | Precio |
|---|---|---|
| pH-metro de bolsillo (pen) | Verificar/calibrar la sonda digital | $12-18 |
| TDS/EC metro de bolsillo | Idem para EC | $10-15 |
| Soluciones de calibración pH 4.0/7.0/10.0 | Calibración periódica | $10-12 (set) |
| Solución de calibración EC 1413 µS | Calibración periódica | $8-10 |
| Termohigrómetro analógico | Verificación cruzada del sensor digital | $8-10 |

### Nutrientes

| Componente | Modelo | Precio |
|---|---|---|
| Kit nutrientes hidro (Grow/Micro/Bloom) | General Hydroponics Flora Trio (económico) o Advanced Nutrients pH Perfect (premium) | $25-35 / $45-55 |
| pH Up / pH Down | Cualquier marca hidropónica | $10-12 c/u |

---

## 📋 PLAN DE COMPRA MODULAR

### Fase 1 — MVP (cultivo funcional, 100% manual) — **≈ $480-620**
Objetivo: tener la planta viva y creciendo con control manual mientras llega el resto.
- Carpa 80×80×180: $75-160
- LED grow light: $65-130
- 2 baldes DWC + net pots + arlita + uniseals: $60-80
- Bomba de aire + piedras difusoras: $25-30
- Extractor + filtro de carbón + ventilador circulación: $70-120
- Nutrientes + pH Up/Down: $40-50
- Medidores manuales (pH pen + TDS pen + calibración): $35-40
- Enchufe con temporizador mecánico (fallback antes de tener smart plugs): $8-10

### Fase 2 — Automatización básica (control remoto + monitoreo) — **≈ $210-250**
Objetivo: sacar el control de las cargas AC de tus manos y empezar a monitorear.
- Raspberry Pi 4B + accesorios (Home Assistant OS): $70-90
- 2× ESP32 DevKitC: $18-20
- Sensor temp/humedad aire (DHT22/SHT31): $8-15
- Sensor temp. agua (DS18B20): $5
- 2× flotador de nivel: $10
- 4× enchufe inteligente (Shelly/Sonoff): $45-60
- Misceláneos de cableado/gabinete: $25-30

### Fase 3 — Automatización completa (pH, EC, dosificación) — **≈ $230-370**
Objetivo: cerrar el loop de control químico del agua.
- Sonda de pH (kit): $45-130
- Sonda de EC/TDS (kit): $50-170
- 4× bomba peristáltica + relé 4ch + fuente 12V: $80-95
- Electroválvula de rellenado: $10-15
- Sensor de luz BH1750: $3-5
- Tubería/fittings adicionales: $20-30

### Fase 4 — Optimización (opcional, mejoras de robustez) — **≈ $150-350**
- UPS/batería pequeña para el Raspberry Pi (evita perder el control si hay corte de luz): $50-80
- Sensor ultrasónico de nivel (sin partes móviles, complementa al flotador): $8-12
- Cámara (ESP32-CAM o webcam USB) para monitoreo visual remoto vía Home Assistant: $15-40
- Bandeja de contención secundaria (anti-fuga bajo el reservorio): $20-30
- Mini chiller de agua o simplemente botellas de hielo rotativas, si la sala supera 24 °C ambiente: $0-150
- CO2 (opcional, solo si la carpa queda bien sellada — no es necesario para el objetivo de 150 g): $150+

**Total sistema completo (Fases 1-3):** ≈ **$920 – $1,240** según elecciones económicas/premium.
**Con Fase 4 completa:** ≈ **$1,100 – $1,600**.

---

## 🛠️ SISTEMA DE CONTROL

**Software recomendado:**
- **Home Assistant (HAOS)** en el Raspberry Pi → cerebro central: dashboard, automatizaciones (reglas if/then), historial de gráficos, notificaciones push (app móvil oficial) y alertas por Telegram.
- **ESPHome** en cada ESP32 → firmware simple en YAML, se integra automático a Home Assistant, no requiere programar en C++ a mano.
- **Mosquitto (MQTT)** como broker de mensajería entre ESP32 y HA (add-on oficial de HA, un clic).
- **Node-RED** (opcional, add-on de HA) solo si la lógica de dosificación se vuelve más compleja que reglas simples (ej. dosificación proporcional con PID).

### Diagrama de conexiones

```
SENSORES                    CONTROLADOR                    ACTUADORES
--------                    -----------                    ----------
Sonda pH          ─┐                                    ┌─ Bomba peristáltica pH+
Sonda EC/TDS       ─┤                                    ├─ Bomba peristáltica pH−
Temp. agua(DS18B20)─┼──► ESP32 (ESPHome) ──MQTT──►       ├─ Bombas peristálticas Nutr. A/B
Temp/Hum aire(SHT31)─┤        (relés 12V DC)              ├─ Relé bomba de recirculación
Nivel agua(flotador)─┤                                    └─ Relé electroválvula rellenado
Luz (BH1750)        ─┘
                              │
                              ▼
                     Raspberry Pi + Home Assistant
                     (dashboard, reglas, histórico)
                              │
                ┌─────────────┼──────────────┐
                ▼             ▼              ▼
          Automatizaciones  Notificaciones  Enchufes inteligentes
           (umbrales)       (Telegram/App)   Shelly/Sonoff (220V):
                                              · LED grow light
                                              · Extractor
                                              · Bomba de aire (24/7)
                                              · Ventilador circulación
```

### Lógica de automatización (pseudocódigo)

```python
# --- RECIRCULACIÓN (no hay "riego" en DWC, las raíces están sumergidas) ---
cada 4 horas:
    activar bomba_recirculacion durante 15 min   # mezcla y oxigena

bomba_aire: SIEMPRE ENCENDIDA 24/7               # nunca apagar: hipoxia mata raíces en <2h

si nivel_agua < nivel_minimo:
    abrir electrovalvula_rellenado
    hasta nivel_agua >= nivel_objetivo OR tiempo > 5 min   # timeout de seguridad
    si tiempo > 5 min sin alcanzar nivel: ALARMA "revisar rellenado manual"

# --- pH ---
leer ph cada 10 min
si ph > 6.2:
    dosificar pH_Down 2 mL
    esperar 30 min (tiempo de mezcla) antes de volver a dosificar
si ph < 5.5:
    dosificar pH_Up 2 mL
    esperar 30 min
si dosis_acumulada(ultimas_2h) > 20 mL:
    DETENER dosificación
    ALARMA CRÍTICA "posible sonda de pH defectuosa o fuga de químico"

# --- EC/TDS ---
leer ec cada 30 min
si ec < ec_objetivo_etapa - 0.2:
    dosificar Nutriente_A 5 mL + Nutriente_B 5 mL
si ec > ec_objetivo_etapa + 0.3:
    ALARMA "EC alta — diluir con agua limpia (acción manual o electroválvula de agua sola)"

# --- TEMPERATURA DEL AGUA ---
si temp_agua > 22°C:
    ALARMA "riesgo de Pythium (pudrición de raíz) — agregar hielo / activar chiller"
si temp_agua < 18°C:
    ALARMA "raíces frías, absorción de nutrientes más lenta"

# --- TEMPERATURA/HUMEDAD DEL AIRE ---
si temp_aire > 28°C:
    extractor -> velocidad alta
si temp_aire < 20°C:
    extractor -> velocidad minima
si humedad > 65% (etapa floración):
    extractor -> velocidad alta
    ALARMA "riesgo de moho/botritis"

# --- LUZ ---
si etapa == "autofloreciente":
    ciclo fijo 18h ON / 6h OFF durante todo el cultivo
si etapa == "fotoperiodica_vegetativo":
    ciclo 18h ON / 6h OFF
si etapa == "fotoperiodica_floracion":
    ciclo 12h ON / 12h OFF   # cambio disparado manualmente desde el dashboard
intensidad: rampa 50% -> 100% durante las primeras 2 semanas (evitar estrés lumínico)

# --- ALARMAS ---
niveles: INFO (log) / WARNING (notificación push) / CRITICAL (push + Telegram + repetir cada 15 min hasta ack)
casos CRITICAL: nivel de agua crítico, sonda de pH sin datos > 1h, temp_aire > 32°C, corte de energía detectado
```

---

## 💰 RESUMEN FINANCIERO

| Concepto | Costo |
|---|---|
| Fase 1 — MVP | $480 – $620 |
| Fase 2 — Automatización básica | $210 – $250 |
| Fase 3 — Automatización completa | $230 – $370 |
| **Subtotal sistema funcional completo** | **$920 – $1,240** |
| Fase 4 — Optimización (opcional) | $150 – $350 |
| **Total con optimización** | **$1,100 – $1,600** |

| Concepto operativo mensual | Estimado |
|---|---|
| Electricidad (LED ~100W × 12-18h, extractor, bombas, controlador ≈ 2.2-2.5 kWh/día ≈ 70 kWh/mes) | $8 – $15/mes (varía mucho según tarifa local, usé ~$0.15/kWh de referencia) |
| Nutrientes y químicos de pH | $10 – $15/mes |
| Consumibles (soluciones de calibración, filtros) amortizado | $3 – $5/mes |
| **Total operativo mensual** | **≈ $25 – $35/mes** |

**Tiempo de setup:**
- Fase 1 (armado físico: carpa, baldes, luz, ventilación): ~1 día
- Fase 2 (cableado bajo voltaje, instalación Home Assistant, enchufes inteligentes): ~1 fin de semana
- Fase 3 (plomería de dosificación, calibración de sondas, integración a HA): ~1 fin de semana
- Total activo de armado: ~4-5 días, repartidos en el primer mes mientras llegan los componentes

**Mantenimiento requerido:**
- Diario: chequeo visual 2 min (dashboard + planta)
- Semanal: completar/cambiar reservorio (20-30 min), poda/entrenamiento LST (10-15 min)
- Cada 2-4 semanas: calibración de sondas pH/EC (15 min)
- Mensual: limpieza de piedras difusoras y bombas

---

## ⚠️ CONSIDERACIONES CRÍTICAS

**Legales:** ver aviso al inicio del documento. Es el punto de mayor riesgo real del proyecto — mucho más que cualquier falla técnica. Verificá tu jurisdicción específica antes de comprar semillas.

**Seguridad eléctrica:**
- Tomacorriente con protección diferencial (GFCI/RCD) obligatorio — hay agua y electricidad en el mismo espacio.
- "Drip loops" en todos los cables que bajen hacia el reservorio (que el cable haga un lazo hacia abajo antes de llegar al enchufe, para que el agua gotee y caiga, no que corra hacia el enchufe).
- Electrónica de bajo voltaje (ESP32, relés) en gabinete cerrado, fuera del área húmeda directa.
- Circuito dedicado, no sobrecargar una sola zapatilla con luz + extractor + bombas.

**Redundancia (qué pasa si falla un sensor):**
- Límite de dosis máxima por ventana de tiempo en pH/EC (evita sobredosificar si la sonda da una lectura fija/errónea).
- Doble sensor de nivel (flotador mecánico + ultrasónico) — si uno falla, el otro cubre.
- Detección de "dato viejo": si un sensor no reporta en X minutos, Home Assistant dispara alarma en vez de asumir que todo está bien.
- Los enchufes inteligentes (Shelly/Sonoff) permiten configurar un estado de "recuperación" ante corte de luz (ej. la bomba de aire vuelve a encender sola).
- Bomba de aire nunca depende de automatización condicional — va siempre encendida, en un circuito simple sin lógica que la pueda apagar por error.

**Calibración de sondas (procedimiento):**
1. Enjuagar la sonda con agua destilada.
2. Sumergir en solución buffer pH 7.0, esperar estabilización, calibrar punto medio.
3. Repetir con pH 4.0 y pH 10.0 (calibración de 3 puntos) cada 2-4 semanas.
4. Para EC: calibrar con solución 1413 µS/cm, ajustando temperatura de referencia (25 °C).
5. Verificar con el pH-metro/TDS-metro manual como cruce de control mensual.

---

## 🌱 PLAN DE EXPERIMENTACIÓN (primeras 2-4 semanas)

**Semana 1 (germinación + trasplante):**
- Germinar semillas en toalla húmeda o taco de lana de roca.
- Trasplantar a net pot con arlita cuando aparezca la raíz pivotante (~1-2 cm).
- EC muy baja (0.4-0.6 mS/cm), pH 5.8-6.0.
- Luz al 30-50% de intensidad, 18/6.
- Monitorear: que la raíz llegue al agua/reservorio sin ahogarse (nivel justo debajo del net pot al inicio).

**Semana 2 (vegetativo temprano):**
- Subir EC a 0.8-1.2 mS/cm.
- Confirmar que bomba de aire funciona 24/7 sin cortes (raíz visible, blanca, sin olor).
- Empezar a registrar en el dashboard: pH, EC, temp. agua, temp/humedad aire — construir el "baseline" de la planta.
- Ajustar altura de luz según estrés (hojas hacia arriba = bien; hojas "de paraguas" hacia abajo = muy cerca).

**Semana 3-4 (vegetativo pleno):**
- EC 1.2-1.8 mS/cm.
- Empezar LST (doblado de ramas) para aplanar el dosel y aprovechar mejor la luz — clave para maximizar los 150 g con solo 2 plantas.
- Verificar que las alarmas disparan correctamente: forzar a propósito un pH fuera de rango un día y confirmar que la notificación llega.
- Cambiar a floración (12/12) si es fotoperiódica, cuando la planta tenga el tamaño deseado (usualmente cuando ocupa ~50% del espacio final).

**Diagnóstico de problemas comunes:**
- *Hojas amarillas generalizadas + raíz marrón/olor:* pudrición de raíz → revisar temp. del agua, oxigenación, y hacer cambio total de reservorio.
- *Puntas quemadas:* EC demasiado alta → diluir con agua.
- *Hojas muy oscuras/rígidas + crecimiento lento a pesar de EC correcta:* "pH lockout" (bloqueo de nutrientes) → verificar calibración de la sonda de pH, puede estar leyendo mal.
- *Estrés lumínico (hojas en forma de garra hacia arriba):* exceso de luz/muy cerca → subir la lámpara o bajar intensidad.

**Ajustes esperados tras el primer ciclo:** casi seguro vas a recalibrar los umbrales de EC por etapa (cada genética responde distinto), afinar el tiempo de dosificación de las bombas peristálticas (mL reales vs. mL teóricos varía por bomba), y probablemente subir la Fase 4 (chiller o UPS) si detectás que la temperatura del agua o los cortes de luz fueron el cuello de botella real.
