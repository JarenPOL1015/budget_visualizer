# budget_visualizer.py
from graphics import Canvas
from translations import TEXTS 

# --- CONSTANTES DE CONFIGURACIÓN GRÁFICA ---
CANVAS_WIDTH = 650
CANVAS_HEIGHT = 450
ALERT_THRESHOLD = 0.30  

BAR_WIDTH = 80           
BOTTOM_Y = CANVAS_HEIGHT - 60  
MAX_BAR_HEIGHT = 300     

def main():
    """ Orquesta la lógica permitiendo elegir el idioma al inicio. """
    lang = choose_language()
    
    print("\n" + TEXTS[lang]['welcome'])
    
    total_income = get_total_income(lang)
    expenses = get_expenses(lang)
    percentages = calculate_percentages(total_income, expenses)
    
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_budget_chart(canvas, percentages, lang)
    
    print(TEXTS[lang]['success'])
    print(TEXTS[lang]['close_window'])
    canvas.mainloop()

def choose_language():
    """Pregunta al usuario el idioma de interfaz antes de arrancar."""
    while True:
        print("Select Language / Selecciona el Idioma:")
        print("1. Español")
        print("2. English")
        choice = input("Choice / Opción (1/2): ").strip()
        if choice == '1':
            return 'es'
        elif choice == '2':
            return 'en'
        print("Opción inválida / Invalid option.\n")

def get_positive_float(prompt, lang):
    """Solicita un número flotante y muestra errores en el idioma elegido."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print(TEXTS[lang]['input_error'])
        except ValueError:
            print(TEXTS[lang]['type_error'])

def get_total_income(lang):
    """Solicita el ingreso total usando los textos del idioma activo."""
    return get_positive_float(TEXTS[lang]['income_prompt'], lang)

def get_expenses(lang):
    """Genera el diccionario mapeando directamente los nombres traducidos."""
    print(TEXTS[lang]['expense_intro'])
    expenses = {
        TEXTS[lang]['vivienda']: get_positive_float(TEXTS[lang]['vivienda_prompt'], lang),
        TEXTS[lang]['comida']: get_positive_float(TEXTS[lang]['comida_prompt'], lang),
        TEXTS[lang]['transporte']: get_positive_float(TEXTS[lang]['transporte_prompt'], lang),
        TEXTS[lang]['entretenimiento']: get_positive_float(TEXTS[lang]['entretenimiento_prompt'], lang)
    }
    return expenses

def calculate_percentages(income, expenses):
    """Calcula las proporciones de los gastos."""
    percentages = {}
    for category in expenses:
        percentages[category] = expenses[category] / income
    return percentages

# --- CAPA DE RENDERIZADO GRÁFICO ---

def draw_budget_chart(canvas, percentages, lang):
    """Dibuja el gráfico y adapta las etiquetas dinámicamente."""
    draw_threshold_line(canvas, lang)
    
    slot_width = CANVAS_WIDTH / len(percentages)
    index = 0
    
    for category in percentages:
        percentage = percentages[category]
        
        slot_left_x = index * slot_width
        margin = (slot_width - BAR_WIDTH) / 2
        left_x = slot_left_x + margin
        right_x = left_x + BAR_WIDTH
        top_y = BOTTOM_Y - (percentage * MAX_BAR_HEIGHT)
        
        color = '#2ecc71'  
        if percentage >= ALERT_THRESHOLD:
            color = '#e74c3c'  
            
        draw_single_bar(canvas, left_x, top_y, right_x, color)
        draw_labels(canvas, left_x, category, percentage)
        
        index += 1

def draw_threshold_line(canvas, lang):
    """Dibuja la línea del 30% con el texto en el idioma correcto."""
    threshold_y = BOTTOM_Y - (ALERT_THRESHOLD * MAX_BAR_HEIGHT)
    canvas.create_line(0, threshold_y, CANVAS_WIDTH, threshold_y, color='#95a5a6')
    
    text_x = 110 if lang == 'es' else 125
    canvas.create_text(text_x, threshold_y - 12, TEXTS[lang]['limit_label'], color='#7f8c8d')

def draw_single_bar(canvas, left_x, top_y, right_x, color):
    """Dibuja el cuerpo rectangular de la barra."""
    canvas.create_rectangle(left_x, top_y, right_x, BOTTOM_Y, fill_color=color, outline_color='#2c3e50')

def draw_labels(canvas, left_x, category, percentage):
    """Escribe los nombres de las categorías abajo y sus porcentajes arriba."""
    center_x = left_x + (BAR_WIDTH / 2)
    canvas.create_text(center_x, BOTTOM_Y + 25, category, color='#2c3e50')
    
    readable_percent = f"{round(percentage * 100, 1)}%"
    top_y = BOTTOM_Y - (percentage * MAX_BAR_HEIGHT)
    canvas.create_text(center_x, top_y - 15, readable_percent, color='#34495e')

if __name__ == '__main__':
    main()