import tkinter as tk
import random
from tkinter import messagebox

class CarRacingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Carreras de Autos")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, bg="gray", width=800, height=600)
        self.canvas.pack()

        # Variables del juego
        self.car_width = 40
        self.car_height = 80
        self.car_speed_x = 10 # Velocidad de movimiento lateral
        self.car_speed_y = 5  # Velocidad de avance (aceleración)
        self.finish_line_y = 50 # Posición de la línea de meta

        self.game_running = False

        # Línea de meta
        self.canvas.create_line(0, self.finish_line_y, 800, self.finish_line_y, fill="white", width=5, tags="finish_line")
        self.canvas.create_text(400, self.finish_line_y - 20, text="META", fill="white", font=("Arial", 20, "bold"))


        # Auto del Jugador 1 (Azul)
        self.car1_x = 200
        self.car1_y = 500
        self.car1 = self.canvas.create_rectangle(
            self.car1_x - self.car_width / 2, self.car1_y - self.car_height / 2,
            self.car1_x + self.car_width / 2, self.car1_y + self.car_height / 2,
            fill="blue", tags="car1"
        )
        # Etiqueta de texto para el Jugador 1, ahora almacenada como atributo
        self.car1_text = self.canvas.create_text(self.car1_x, self.car1_y + self.car_height / 2 + 15, text="Jugador 1", fill="blue", font=("Arial", 10), tags="car1_text")


        # Auto del Jugador 2 (Rojo)
        self.car2_x = 600
        self.car2_y = 500
        self.car2 = self.canvas.create_rectangle(
            self.car2_x - self.car_width / 2, self.car2_y - self.car_height / 2,
            self.car2_x + self.car_width / 2, self.car2_y + self.car_height / 2,
            fill="red", tags="car2"
        )
        # Etiqueta de texto para el Jugador 2, ahora almacenada como atributo
        self.car2_text = self.canvas.create_text(self.car2_x, self.car2_y + self.car_height / 2 + 15, text="Jugador 2", fill="red", font=("Arial", 10), tags="car2_text")

        # Texto de estado del juego
        self.game_status_text = self.canvas.create_text(
            400, 300, text="Presiona 'Iniciar Juego'", font=("Arial", 30, "bold"), fill="white"
        )

        # Botón de inicio/reinicio
        self.start_button = tk.Button(root, text="Iniciar Juego", command=self.start_game)
        self.start_button.pack(side=tk.BOTTOM, pady=10)

        # Controles del teclado
        # Jugador 1: A (izquierda), D (derecha), W (acelerar)
        self.root.bind("<a>", lambda event: self.move_car(self.car1, -self.car_speed_x, 0))
        self.root.bind("<d>", lambda event: self.move_car(self.car1, self.car_speed_x, 0))
        self.root.bind("<w>", lambda event: self.move_car(self.car1, 0, -self.car_speed_y))

        # Jugador 2: Flecha izquierda, Flecha derecha, Flecha arriba (acelerar)
        self.root.bind("<Left>", lambda event: self.move_car(self.car2, -self.car_speed_x, 0))
        self.root.bind("<Right>", lambda event: self.move_car(self.car2, self.car_speed_x, 0))
        self.root.bind("<Up>", lambda event: self.move_car(self.car2, 0, -self.car_speed_y))

    def start_game(self):
        if not self.game_running:
            self.game_running = True
            self.reset_cars_position()
            self.canvas.itemconfig(self.game_status_text, text="") # Borra el texto de estado
            self.start_button.config(text="Reiniciar Juego", command=self.reset_game)
            self.game_loop()

    def reset_game(self):
        self.game_running = False
        self.start_button.config(text="Iniciar Juego", command=self.start_game)
        self.reset_cars_position()
        self.canvas.itemconfig(self.game_status_text, text="Presiona 'Iniciar Juego'") # Muestra el texto de estado inicial

    def reset_cars_position(self):
        # Reinicia la posición de los autos
        self.car1_x, self.car1_y = 200, 500
        self.car2_x, self.car2_y = 600, 500
        self.canvas.coords(
            self.car1,
            self.car1_x - self.car_width / 2, self.car1_y - self.car_height / 2,
            self.car1_x + self.car_width / 2, self.car1_y + self.car_height / 2
        )
        self.canvas.coords(
            self.car2,
            self.car2_x - self.car_width / 2, self.car2_y - self.car_height / 2,
            self.car2_x + self.car_width / 2, self.car2_y + self.car_height / 2
        )
        # Mueve las etiquetas de texto a sus posiciones iniciales
        self.canvas.coords(self.car1_text, self.car1_x, self.car1_y + self.car_height / 2 + 15)
        self.canvas.coords(self.car2_text, self.car2_x, self.car2_y + self.car_height / 2 + 15)


    def move_car(self, car_id, dx, dy):
        if self.game_running:
            # Obtener las coordenadas actuales del auto desde el canvas
            x1, y1, x2, y2 = self.canvas.coords(car_id)

            # Calcular la nueva posición propuesta
            proposed_dx = dx
            proposed_dy = dy

            # Limitar el movimiento horizontal dentro del canvas
            if x1 + proposed_dx < 0:
                proposed_dx = -x1
            elif x2 + proposed_dx > 800:
                proposed_dx = 800 - x2

            # Limitar el movimiento vertical (para que no retrocedan más allá del inicio)
            if y2 + proposed_dy > 600: # No permitir ir más allá del borde inferior
                proposed_dy = 600 - y2
            elif y1 + proposed_dy < self.finish_line_y - self.car_height / 2: # No permitir ir mucho más allá de la meta
                 proposed_dy = 0 # Detener el movimiento vertical si ya cruzó la meta

            # Mover el auto en el canvas
            self.canvas.move(car_id, proposed_dx, proposed_dy)

            # Actualizar las coordenadas de referencia del auto y mover la etiqueta de texto
            new_x1, new_y1, new_x2, new_y2 = self.canvas.coords(car_id)
            new_center_x = (new_x1 + new_x2) / 2
            new_center_y = (new_y1 + new_y2) / 2

            if car_id == self.car1:
                self.car1_x = new_center_x
                self.car1_y = new_center_y
                self.canvas.coords(self.car1_text, self.car1_x, self.car1_y + self.car_height / 2 + 15)
            else:
                self.car2_x = new_center_x
                self.car2_y = new_center_y
                self.canvas.coords(self.car2_text, self.car2_x, self.car2_y + self.car_height / 2 + 15)


    def check_win_condition(self):
        # Obtener la posición Y de la parte superior de cada auto
        car1_coords = self.canvas.coords(self.car1)
        car2_coords = self.canvas.coords(self.car2)

        car1_top_y = car1_coords[1]
        car2_top_y = car2_coords[1]

        winner = None
        if car1_top_y <= self.finish_line_y:
            winner = "Jugador 1"
        if car2_top_y <= self.finish_line_y:
            if winner: # Si ambos cruzan al mismo tiempo, el primero en ser detectado gana
                pass
            else:
                winner = "Jugador 2"

        if winner:
            self.game_running = False
            self.canvas.itemconfig(self.game_status_text, text=f"¡{winner} ha ganado!")
            messagebox.showinfo("Fin del Juego", f"¡{winner} ha ganado la carrera!")
            self.start_button.config(text="Reiniciar Juego", command=self.reset_game)
            return True
        return False

    def game_loop(self):
        if not self.game_running:
            return

        # Comprobar la condición de victoria
        if self.check_win_condition():
            return

        # Continuar el bucle del juego
        self.root.after(10, self.game_loop) # Actualiza cada 10 milisegundos

if __name__ == "__main__":
    root = tk.Tk()
    game = CarRacingGame(root)
    root.mainloop()
