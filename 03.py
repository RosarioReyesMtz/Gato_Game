from tkinter import *
from tkinter import ttk

class Juego:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x200')
        self.root.title("Juego de Tic-Tac-Toe")
        
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.mensaje = StringVar()
        self.mensaje.set("Turno de X")
        ttk.Label(self.mainframe, textvariable=self.mensaje).grid(column=1, row=4, sticky=(W, E))
        
        self.buttons = {}
        self.turn = 1
        self.crear_botones()
        
        self.restart_btn = ttk.Button(self.mainframe, text="Reiniciar", command=self.reiniciar)
        self.restart_btn.grid(column=1, row=5, sticky=(W, E))
        
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
    
    def crear_botones(self):
        positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        for pos in positions:
            button = ttk.Button(self.mainframe, text=" ", width=5, command=lambda p=pos: self.on_button_click(p))
            button.grid(column=pos[0], row=pos[1], sticky=W)
            self.buttons[pos] = button
    
    def reiniciar(self):
        self.turn = 1
        self.mensaje.set("Turno de X")
        for button in self.buttons.values():
            button["text"] = " "
    
    def on_button_click(self, pos):
        button = self.buttons[pos]
        if button["text"] == " ":
            button["text"] = "X" if self.turn % 2 == 1 else "O"
            self.turn += 1
            winner = self.check_winner()
            if winner:
                if winner == "Empate":
                    self.mensaje.set("¡Es un empate!")
                else:
                    self.mensaje.set(f"¡Ganó {winner}!")
            elif self.turn > 9:
                self.mensaje.set("¡Es un empate!")
            else:
                self.mensaje.set(f"Turno de {'X' if self.turn % 2 == 1 else 'O'}")
    
    def check_winner(self):
        for i in range(1, 4):
            if self.buttons[(i, 1)]["text"] == self.buttons[(i, 2)]["text"] == self.buttons[(i, 3)]["text"] != " ":
                return self.buttons[(i, 1)]["text"]
        
        for i in range(1, 4):
            if self.buttons[(1, i)]["text"] == self.buttons[(2, i)]["text"] == self.buttons[(3, i)]["text"] != " ":
                return self.buttons[(1, i)]["text"]
        
        if self.buttons[(1, 1)]["text"] == self.buttons[(2, 2)]["text"] == self.buttons[(3, 3)]["text"] != " ":
            return self.buttons[(1, 1)]["text"]
        if self.buttons[(1, 3)]["text"] == self.buttons[(2, 2)]["text"] == self.buttons[(3, 1)]["text"] != " ":
            return self.buttons[(1, 3)]["text"]
        
        if all(button["text"] != " " for button in self.buttons.values()):
            return "Empate"
        
        return None


root = Tk()
juego = Juego(root)
root.mainloop()
