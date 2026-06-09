# budget_visualizer.py
from graphics import Canvas

# --- CONSTANTES DE CONFIGURACIÓN ---
CANVAS_WIDTH = 650
CANVAS_HEIGHT = 450
ALERT_THRESHOLD = 0.30  # Límite de alerta (30%)

# Constantes de diseño del gráfico
BAR_WIDTH = 80           
BOTTOM_Y = CANVAS_HEIGHT - 60  
MAX_BAR_HEIGHT = 300     

def main():
    """ Orquesta la lógica del programa con manejo de errores y validación. """
    print("=== BIENVENIDO A TU OPTIMIZADOR DE PRESUPUESTO ===")
    
    # 1. Entrada de datos validada por consola
    total_income = get_total_income()
    expenses = get_expenses()
    
    # 2. Procesamiento matemático
    percentages = calculate_percentages(total_income, expenses)
    
    # 3. Inicialización del Canvas Local
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # 4. Renderizado del gráfico completo
    draw_budget_chart(canvas, percentages)
    
    # 5. Mantener ventana activa
    print("\n[Éxito] Gráfico generado de forma segura.")
    print("Cierra la ventana gráfica para terminar la ejecución.")
    canvas.mainloop()

def get_positive_float(prompt):
    """
    Función modular que solicita un número flotante, atrapa errores de texto
    y asegura que el valor sea estrictamente mayor a cero.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Error: El valor debe ser un número positivo mayor a cero. Intenta de nuevo.")
        except ValueError:
            print("Error: Entrada inválida. Por favor, introduce solo números enteros o decimales.")

def get_total_income():
    """Solicita el ingreso mensual total usando la función de validación."""
    return get_positive_float("Ingresa tu ingreso mensual total disponible ($): ")

def get_expenses():
    """Solicita los gastos usando la función de validación para reutilizar código."""
    print("\nIntroduce tus gastos mensuales por categoría:")
    expenses = {
        'Vivienda': get_positive_float("- Vivienda (Alquiler/Servicios): $"),
        'Comida': get_positive_float("- Comida (Super/Restaurantes): $"),
        'Transporte': get_positive_float("- Transporte (Gasolina/Pasajes): $"),
        'Entretenimiento': get_positive_float("- Entretenimiento (Salidas/Streaming): $")
    }
    return expenses

def calculate_percentages(income, expenses):
    """Calcula la proporción de cada gasto frente al ingreso total."""
    percentages = {}
    for category in expenses:
        percentages[category] = expenses[category] / income
    return percentages

# --- CAPA DE RENDERIZADO GRÁFICO ---

def draw_budget_chart(canvas, percentages):
    """Coordina el dibujo de todos los componentes visuales."""
    draw_threshold_line(canvas)
    
    slot_width = CANVAS_WIDTH / len(percentages)
    index = 0
    
    for category in percentages:
        percentage = percentages[category]
        
        # Calcular coordenadas X
        slot_left_x = index * slot_width
        margin = (slot_width - BAR_WIDTH) / 2
        left_x = slot_left_x + margin
        right_x = left_x + BAR_WIDTH
        
        # Calcular coordenadas Y
        bar_height = percentage * MAX_BAR_HEIGHT
        top_y = BOTTOM_Y - bar_height
        
        # Definición de alertas por color (Verde vs Rojo)
        color = '#2ecc71'  
        if percentage >= ALERT_THRESHOLD:
            color = '#e74c3c'  
            
        draw_single_bar(canvas, left_x, top_y, right_x, color)
        draw_labels(canvas, left_x, category, percentage)
        
        index += 1

def draw_threshold_line(canvas):
    """Dibuja la línea guía horizontal del 30%."""
    threshold_y = BOTTOM_Y - (ALERT_THRESHOLD * MAX_BAR_HEIGHT)
    canvas.create_line(0, threshold_y, CANVAS_WIDTH, threshold_y, color='#95a5a6')
    canvas.create_text(110, threshold_y - 12, "LÍMITE RECOMENDADO (30%)", color='#7f8c8d')

def draw_single_bar(canvas, left_x, top_y, right_x, color):
    """Dibuja el cuerpo rectangular de la barra."""
    canvas.create_rectangle(left_x, top_y, right_x, BOTTOM_Y, fill_color=color, outline_color='#2c3e50')

def draw_labels(canvas, left_x, category, percentage):
    """Escribe los nombres de las categorías abajo y sus porcentajes arriba."""
    center_x = left_x + (BAR_WIDTH / 2)
    canvas.create_text(center_x, BOTTOM_Y + 25, category, color='#2c3e50')
    
    readable_percent = f"{round(percentage * 100, 1)}%"
    bar_height = percentage * MAX_BAR_HEIGHT
    top_y = BOTTOM_Y - bar_height
    canvas.create_text(center_x, top_y - 15, readable_percent, color='#34495e')

if __name__ == '__main__':
    main()