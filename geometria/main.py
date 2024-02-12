import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in range(10):
            self.grid_rowconfigure(x, weight=1)
            self.grid_columnconfigure(x, weight=1)

        menubar = tk.Menu(self)
        opt_menu = tk.Menu(menubar)

        opt_menu.add_command(label="Equação da reta", command=self.mostra_equacao)

        menubar.add_cascade(label="Opções", menu=opt_menu)
        self.config(menu=menubar)

        self.ent = None  # Para armazenar a entrada

        self.figs, self.ax = plt.subplots()
        self.cnv= FigureCanvasTkAgg(self.figs, master=self)
        self.cnv.get_tk_widget().grid(row=1, column=0, columnspan=10, sticky='nsew')

    def mostra_equacao(self):
        if self.ent is None:
            self.ent = tk.Entry(self, width=20, font="arial 14")
            self.ent.grid(row=0, column=1, pady=10)

            self.ent.bind('<Return>', self.line_graphic)
            lb_eq = tk.Label(self, text="Equação da reta:", font="arial 14", anchor='center')
            lb_eq.grid(row=0, column=0, pady=10)

    def line_graphic(self, event):
        
        x = np.linspace(-10, 10, 100)
        y = eval(self.ent.get())

        self.ax.clear()

        self.ax.plot(x, y)
        self.ax.set_xlabel('Eixo X')
        self.ax.set_ylabel('Eixo Y')
        self.ax.set_title('Gráfico da Reta')
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)
        self.ax.grid(color='gray', linestyle='--', linewidth=0.5)
        self.ax.legend()
        
        self.cnv.draw()

if __name__ == '__main__':
    win = Window()
    win.mainloop()