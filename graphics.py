import tkinter as tk

class Canvas:
    def __init__(self, width, height, title="Visualizador de Presupuesto"):
        """Inicializa la ventana nativa del sistema operativo."""
        self.root = tk.Tk()
        self.root.title(title)
        self.root.resizable(False, False)
        
        # Creamos el lienzo blanco
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()

    def create_rectangle(self, x1, y1, x2, y2, fill_color, outline_color="black"):
        """Dibuja un rectángulo."""
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline=outline_color)

    def create_line(self, x1, y1, x2, y2, color="black"):
        """Dibuja una línea recta."""
        return self.canvas.create_line(x1, y1, x2, y2, fill=color, width=1.5)

    def create_text(self, x, y, text_content, color="black"):
        """Dibuja texto en pantalla con tipografía limpia."""
        return self.canvas.create_text(x, y, text=text_content, fill=color, font=("Arial", 10, "bold"))

    def mainloop(self):
        """Mantiene la ventana abierta hasta que el usuario la cierre."""
        self.root.mainloop()