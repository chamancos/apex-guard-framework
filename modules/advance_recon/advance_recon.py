#!/usr/bin/env python3
# ==============================================================================
# Script: advance_recon.py
# Proyecto: Apex-Guard & Disruptive Protection Framework
# Autor: Alexis Isaac Solís Pinedo
# Descripción: Módulo táctico de evaluación de rutas, riesgos y nivel de blindaje
# ==============================================================================

import json
from datetime import datetime

def evaluar_ruta(nombre_ruta, distancia_km, puntos_ciegos, indice_criminalidad, trafico_actual):
    """Calcula el factor de riesgo táctico y determina el nivel de blindaje/disrupción."""
    
    puntaje_riesgo = (puntos_ciegos * 2.5) + (indice_criminalidad * 3.0) + (1.5 if trafico_actual == "Congestionado" else 0.5)
    
    nivel_alerta = "VERDE (Ruta Segura)"
    protocolo_disruptivo = "Desplazamiento estándar a velocidad constante."
    blindaje_sugerido = "Nivel III (Estándar)"

    if puntaje_riesgo > 15:
        nivel_alerta = "ROJO (Alto Riesgo - Requiere Disrupción)"
        protocolo_disruptivo = "ACTIVAR CONTRAMEDIDA: Cambio dinámico de ruta a 2 km del checkpoint, uso de vehículo señuelo y formación en cuña."
        blindaje_sugerido = "Nivel V / VI (Alto Blindaje Balístico)"
    elif puntaje_riesgo > 8:
        nivel_alerta = "AMARILLO (Precaución Moderada)"
        protocolo_disruptivo = "Monitoreo constante de retaguardia, evitar detenciones prolongadas en semáforos."
        blindaje_sugerido = "Nivel IV (Reforzado)"

    reporte_ruta = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ruta": nombre_ruta,
        "distancia_km": distancia_km,
        "puntaje_riesgo_tactico": round(puntaje_riesgo, 2),
        "estado_alerta": nivel_alerta,
        "blindaje_requerido": blindaje_sugerido,
        "protocolo_disruptivo_recomendado": protocolo_disruptivo
    }
    return reporte_ruta

def main():
    print("====================================================")
    print("   APEX-GUARD: Módulo de Reconocimiento y Rutas     ")
    print("====================================================")
    
    rutas_prueba = [
        {"nombre": "Ruta Centro - Zona Hotelera", "distancia": 12.5, "ciegos": 2, "crim": 1, "trafico": "Fluido"},
        {"nombre": "Ruta Periférico Norte (Punto Crítico)", "distancia": 18.0, "ciegos": 5, "crim": 4, "trafico": "Congestionado"},
        {"nombre": "Ruta Alterna Aeropuerto", "distancia": 24.1, "ciegos": 1, "crim": 2, "trafico": "Moderado"}
    ]
    
    evaluaciones = []
    print("\n[+] Analizando vectores de desplazamiento...\n")
    
    for r in rutas_prueba:
        res = evaluar_ruta(r["nombre"], r["distancia"], r["ciegos"], r["crim"], r["trafico"])
        evaluaciones.append(res)
        
        print(f"[Ruta] {res['ruta']}")
        print(f"  ├── Nivel de Alerta: {res['estado_alerta']}")
        print(f"  ├── Blindaje: {res['blindaje_requerido']}")
        print(f"  └── Táctica: {res['protocolo_disruptivo_recomendado']}\n")

    with open("../../docs/logs/recon_rutas_log.json", "w", encoding="utf-8") as f:
        json.dump(evaluaciones, f, indent=4, ensure_ascii=False)
        
    print("[✔] Reporte de reconocimiento táctico guardado en docs/logs/recon_rutas_log.json")

if __name__ == "__main__":
    main()
