# BudgetVisualizer 📊
## By: Jaren Pazmino

Un optimizador y visualizador de presupuesto mensual desarrollado en Python como proyecto final para el curso **Code in Place de la Universidad de Stanford**. 

El programa permite a los usuarios ingresar sus finanzas a través de la consola y genera instantáneamente un gráfico interactivo utilizando programación gráfica (`tkinter`). Su principal innovación es la implementación de la **Regla de Alerta del 30%**: si una categoría de consumo iguala o supera este umbral, la barra cambia automáticamente de color verde a rojo, advirtiendo al usuario visualmente sobre posibles riesgos financieros.

## 🚀 Características
- **Modularización Estricta:** Diseñado bajo los principios de *Top-Down Design* de Stanford.
- **Validación Robusta de Datos:** El programa es inmune a ingresos accidentales de texto o números negativos.
- **Diseño Gráfico Proporcional:** Las dimensiones y espacios de las barras se calculan de manera dinámica según el tamaño del lienzo (*Canvas*).

## 🛠️ Instalación y Uso
1. Asegúrate de tener Python 3 instalado en tu máquina.
2. Clona este repositorio o descarga los archivos en una carpeta local.
3. Ejecuta el archivo principal desde tu terminal:
   ```bash
   python budget_visualizer.py