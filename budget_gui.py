import tkinter as tk
from tkinter import messagebox
from translations import TEXTS

# --- CONSTANTES DE DISEÑO (DARK MODE FINTECH) ---
WIDTH, HEIGHT = 800, 700
ALERT_THRESHOLD = 0.30

# Paleta de Colores
BG_MAIN = "#0f172a"       # Fondo oscuro azulado
CARD_BG = "#1e293b"       # Fondo de tarjetas/formularios
TEXT_MAIN = "#f8fafc"     # Texto blanco
TEXT_MUTED = "#94a3b8"    # Texto grisáceo
ACCENT = "#3b82f6"        # Azul brillante (Botones)
ACCENT_HOVER = "#2563eb"  # Azul oscuro (Hover)
CHART_SAFE = "#2ecc71"    # Verde brillante
CHART_ALERT = "#e74c3c"   # Rojo coral

FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_SUB = ("Segoe UI", 16)
FONT_TEXT = ("Segoe UI", 12)
FONT_BTN = ("Segoe UI", 12, "bold")

class BudgetApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BudgetVisualizer 2.0 - Premium Edition")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.configure(bg=BG_MAIN)
        
        # Centrar la ventana en la pantalla
        self.root.eval('tk::PlaceWindow . center')
        
        self.lang = 'es' # Default
        self.show_language_screen()
        self.root.mainloop()

    def clear_screen(self):
        """Elimina todos los widgets actuales de la ventana con un efecto limpio."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_modern_button(self, parent, text, command, width=20, bg=ACCENT, hover=ACCENT_HOVER):
        """Genera botones planos sin bordes horribles 3D y con efecto hover."""
        btn = tk.Button(parent, text=text, command=command, font=FONT_BTN, 
                        bg=bg, fg=TEXT_MAIN, relief="flat", width=width,
                        activebackground=hover, activeforeground=TEXT_MAIN,
                        cursor="hand2", pady=8)
        
        # Efectos de Hover
        btn.bind("<Enter>", lambda e: btn.config(bg=hover))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))
        return btn

    def create_modern_entry(self, parent):
        """Genera campos de texto oscuros con un borde sutil."""
        ent = tk.Entry(parent, font=FONT_TEXT, bg="#334155", fg=TEXT_MAIN, 
                       insertbackground=TEXT_MAIN, relief="flat", 
                       highlightthickness=2, highlightbackground=CARD_BG, highlightcolor=ACCENT)
        return ent

    # --- PANTALLA 1: SELECCIÓN DE IDIOMA ---
    def show_language_screen(self):
        self.clear_screen()
        
        # Contenedor central
        frame = tk.Frame(self.root, bg=BG_MAIN)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(frame, text="BudgetVisualizer 2.0", font=("Segoe UI", 32, "bold"), 
                 bg=BG_MAIN, fg=ACCENT).pack(pady=(0, 10))
                 
        tk.Label(frame, text="Select Language / Selecciona Idioma", font=FONT_SUB, 
                 bg=BG_MAIN, fg=TEXT_MUTED).pack(pady=(0, 40))
        
        self.create_modern_button(frame, "🇪🇸  Español", lambda: self.set_language('es')).pack(pady=10)
        self.create_modern_button(frame, "🇬🇧  English", lambda: self.set_language('en')).pack(pady=10)

    def set_language(self, lang_code):
        self.lang = lang_code
        self.show_input_screen()

    # --- PANTALLA 2: ENTRADA DE DATOS ---
    def show_input_screen(self):
        self.clear_screen()
        t = TEXTS[self.lang]
        
        # Encabezado
        tk.Label(self.root, text=t['app_title'], font=FONT_TITLE, bg=BG_MAIN, fg=TEXT_MAIN).pack(pady=(30, 10))
        tk.Label(self.root, text=t['expenses_title'], font=FONT_SUB, bg=BG_MAIN, fg=TEXT_MUTED).pack(pady=(0, 20))
        
        # Tarjeta (Card) que contiene el formulario
        card = tk.Frame(self.root, bg=CARD_BG, padx=40, pady=40, bd=0)
        card.pack(pady=10)

        # Campo Ingreso Total (Destacado)
        tk.Label(card, text=t['income_label'], font=FONT_BTN, bg=CARD_BG, fg=ACCENT).grid(row=0, column=0, sticky="w", pady=(0, 20))
        self.income_ent = self.create_modern_entry(card)
        self.income_ent.grid(row=0, column=1, padx=20, pady=(0, 20), ipady=5)

        # Separador visual
        tk.Frame(card, bg="#334155", height=1).grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 20))

        # Campos Gastos
        self.expense_entries = {}
        categories = ['vivienda', 'comida', 'transporte', 'entretenimiento']
        
        for i, cat in enumerate(categories):
            tk.Label(card, text=f"{t[cat]} ($):", font=FONT_TEXT, bg=CARD_BG, fg=TEXT_MAIN).grid(row=i+2, column=0, sticky="w", pady=10)
            ent = self.create_modern_entry(card)
            ent.grid(row=i+2, column=1, padx=20, pady=10, ipady=4)
            self.expense_entries[t[cat]] = ent

        # Botón de Generar
        self.create_modern_button(self.root, t['btn_generate'], self.process_data, width=25, bg="#10b981", hover="#059669").pack(pady=30)

    def process_data(self):
        """Valida datos numéricos y lanza la gráfica."""
        try:
            income_str = self.income_ent.get().strip()
            if not income_str: raise ValueError
            income = float(income_str)
            if income <= 0: raise ValueError
            
            percentages = {}
            for cat_name, entry in self.expense_entries.items():
                val_str = entry.get().strip()
                if not val_str: val_str = "0" # Si lo dejan en blanco, asume 0
                val = float(val_str)
                if val < 0: raise ValueError
                percentages[cat_name] = val / income
            
            self.show_chart_screen(percentages)
        except ValueError:
            messagebox.showerror("Error", TEXTS[self.lang]['input_error'])

    # --- PANTALLA 3: GRÁFICO FINAL ESTILIZADO ---
    def show_chart_screen(self, data):
        self.clear_screen()
        
        # Botón de retorno (Arriba a la izquierda)
        top_bar = tk.Frame(self.root, bg=BG_MAIN)
        top_bar.pack(fill="x", padx=20, pady=15)
        btn_back = tk.Button(top_bar, text="← Volver / Back", command=self.show_input_screen, 
                             bg=BG_MAIN, fg=TEXT_MUTED, font=FONT_TEXT, relief="flat", cursor="hand2", activebackground=BG_MAIN, activeforeground=TEXT_MAIN)
        btn_back.pack(side="left")

        # Lienzo Gráfico
        canvas_width, canvas_height = WIDTH - 100, HEIGHT - 150
        canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, bg=CARD_BG, highlightthickness=0)
        canvas.pack(pady=10)

        # Configuración matemática de dibujo
        bottom_y = canvas_height - 60
        max_h = canvas_height - 150
        slot_w = canvas_width / len(data)
        bar_w = 70

        # Dibujar Cuadrícula de fondo (Grid lines) para escala visual
        for pct in range(10, 110, 10):
            y_line = bottom_y - ((pct / 100) * max_h)
            if y_line > 30: # Evitar dibujar fuera del canvas
                canvas.create_line(40, y_line, canvas_width - 40, y_line, fill="#334155", dash=(2, 4))
                canvas.create_text(20, y_line, text=f"{pct}%", fill=TEXT_MUTED, font=("Segoe UI", 8))

        # Línea de Alerta (30%)
        alert_y = bottom_y - (ALERT_THRESHOLD * max_h)
        canvas.create_line(40, alert_y, canvas_width - 40, alert_y, fill=CHART_ALERT, dash=(6, 2), width=2)
        canvas.create_text(canvas_width - 120, alert_y - 12, text=TEXTS[self.lang]['limit_label'], fill=CHART_ALERT, font=("Segoe UI", 10, "bold"))

        # Renderizado de Barras
        for i, (cat, pct) in enumerate(data.items()):
            x_center = (i * slot_w) + (slot_w / 2)
            lx = x_center - (bar_w / 2)
            rx = x_center + (bar_w / 2)
            
            # Limitar la barra a un máximo visual para no salirse de la pantalla si el gasto > 100%
            visual_pct = pct if pct <= 1.0 else 1.0
            h = visual_pct * max_h
            ty = bottom_y - h
            
            color = CHART_ALERT if pct >= ALERT_THRESHOLD else CHART_SAFE

            # Dibujar Sombra de Barra (Efecto de profundidad)
            canvas.create_rectangle(lx + 4, ty + 4, rx + 4, bottom_y, fill="#0f172a", outline="")
            
            # Dibujar Barra Principal
            canvas.create_rectangle(lx, ty, rx, bottom_y, fill=color, outline=color)
            
            # Etiquetas (Abajo categoría, Arriba porcentaje)
            canvas.create_text(x_center, bottom_y + 25, text=cat, font=("Segoe UI", 11, "bold"), fill=TEXT_MAIN)
            
            # Si supera el 100%, advertir en el texto
            display_pct = f"{round(pct*100, 1)}%"
            if pct > 1.0: display_pct += " (!)"
            canvas.create_text(x_center, ty - 15, text=display_pct, font=("Segoe UI", 12, "bold"), fill=TEXT_MAIN)

        # Línea base sólida
        canvas.create_line(40, bottom_y, canvas_width - 40, bottom_y, fill=TEXT_MUTED, width=2)

if __name__ == "__main__":
    BudgetApp()