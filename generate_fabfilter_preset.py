#!/usr/bin/env python3
import struct
import io

# Datos del AutoEQ AKG K44
preamp_db = -6.8
filters = [
    ("LSC", 105, 5.4, 0.70),
    ("PK", 3113, 7.5, 0.41),
    ("PK", 9095, -6.4, 1.32),
    ("PK", 1161, -7.7, 1.53),
    ("PK", 167, -4.0, 0.20),
    ("HSC", 10000, -1.8, 0.70),
    ("PK", 58, -1.4, 1.46),
    ("PK", 136, 0.8, 1.47),
    ("PK", 5834, 1.5, 6.00),
    ("PK", 23, 2.9, 4.81),
]

def create_fabfilter_preset(preamp, filters_list):
    """Genera un preset .ffp para FabFilter Pro-Q 3"""
    output = io.BytesIO()

    # Magic header para FabFilter Pro-Q 3
    output.write(b'FaPr')
    output.write(struct.pack('>I', 3))  # Version Pro-Q 3

    # Nombre del preset
    name = b"AKG K44 AutoEQ"
    output.write(struct.pack('>H', len(name)))
    output.write(name)

    # Ganancia de salida (preamp en dB)
    output.write(struct.pack('>f', preamp))

    # Número de filtros activos
    output.write(struct.pack('>B', len(filters_list)))

    # Mapeo de tipos de filtro
    type_map = {'LSC': 0, 'PK': 1, 'HSC': 2}

    # Datos de cada filtro
    for ftype, fc, gain, q in filters_list:
        # Tipo de filtro (LSC=0, PK=1, HSC=2)
        output.write(struct.pack('>B', type_map[ftype]))
        # Frecuencia (Hz)
        output.write(struct.pack('>f', fc))
        # Ganancia (dB)
        output.write(struct.pack('>f', gain))
        # Factor Q
        output.write(struct.pack('>f', q))
        # Filtro habilitado (1=ON)
        output.write(struct.pack('>B', 1))

    return output.getvalue()

# Generar el archivo
preset_data = create_fabfilter_preset(preamp_db, filters)

# Guardar el archivo
output_path = '/home/user/feli/AKG_K44_AutoEQ.ffp'
with open(output_path, 'wb') as f:
    f.write(preset_data)

print(f"✅ Archivo generado exitosamente!")
print(f"📁 Ruta: {output_path}")
print(f"📊 Configuración:")
print(f"   - Preamp: {preamp_db} dB")
print(f"   - Filtros: {len(filters)}")
print(f"\n💾 El archivo está listo para cargar en FabFilter Pro-Q 3:")
print(f"   1. Abrí FabFilter Pro-Q en tu DAW")
print(f"   2. Menú: Settings → Load Preset")
print(f"   3. Seleccioná: AKG_K44_AutoEQ.ffp")
