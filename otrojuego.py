import tkinter as tk
import time
import random
from tkinter import messagebox # Asegúrate de que messagebox está importado

class TennisGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Tenis")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, bg="lightgreen", width=600, height=400)
        self.canvas.pack()

        # Game variables
        self.paddle_width = 80
        self.paddle_height = 10
        self.ball_radius = 7
        self.score_player = 0
        self.score_opponent = 0
        self.game_running = False

        # Player paddle
        self.player_paddle = self.canvas.create_rectangle(
            (600 - self.paddle_width) / 2, 380,
            (600 + self.paddle_width) / 2, 390,
            fill="blue"
        )

        # Opponent paddle (simple AI)
        self.opponent_paddle = self.canvas.create_rectangle(
            (600 - self.paddle_width) / 2, 10,
            (600 + self.paddle_width) / 2, 20,
            fill="red"
        )

        # Ball
        self.ball = self.canvas.create_oval(
            (600 - self.ball_radius) / 2, (400 - self.ball_radius) / 2,
            (600 + self.ball_radius) / 2, (400 + self.ball_radius) / 2,
            fill="white"
        )
        self.ball_dx = 3 # Ball horizontal speed
        self.ball_dy = 3 # Ball vertical speed

        # Score display
        self.score_text = self.canvas.create_text(
            300, 30, text="Jugador: 0 - Oponente: 0", font=("Arial", 18), fill="black"
        )

        # Game status display
        self.game_status_text = self.canvas.create_text(
            300, 200, text="Presiona 'Iniciar Juego'", font=("Arial", 24), fill="darkblue"
        )

        # Start/Stop button
        self.start_button = tk.Button(root, text="Iniciar Juego", command=self.start_game)
        self.start_button.pack(side=tk.BOTTOM, pady=5)

        # Bind keyboard events for player paddle movement
        # Asegúrate de que la ventana del juego esté enfocada para que los controles funcionen.
        self.root.bind("<Left>", self.move_player_left)
        self.root.bind("<Right>", self.move_player_right)

    def start_game(self):
        # Inicia el juego si no está corriendo
        if not self.game_running:
            self.game_running = True
            self.score_player = 0
            self.score_opponent = 0
            self.update_score_display()
            self.reset_ball()
            self.canvas.itemconfig(self.game_status_text, text="") # Borra el texto de estado
            self.game_loop()
            self.start_button.config(text="Reiniciar Juego", command=self.reset_game)

    def reset_game(self):
        # Reinicia el estado del juego
        self.game_running = False
        self.start_button.config(text="Iniciar Juego", command=self.start_game)
        self.reset_ball()
        self.score_player = 0
        self.score_opponent = 0
        self.update_score_display()
        self.canvas.itemconfig(self.game_status_text, text="Presiona 'Iniciar Juego'") # Muestra el texto de estado inicial

    def reset_ball(self):
        # Reinicia la posición de la pelota al centro
        self.canvas.coords(
            self.ball,
            (600 - self.ball_radius) / 2, (400 - self.ball_radius) / 2,
            (600 + self.ball_radius) / 2, (400 + self.ball_radius) / 2
        )
        # Aleatoriza la dirección inicial de la pelota
        self.ball_dx = random.choice([-3, 3])
        self.ball_dy = random.choice([-3, 3])

    def update_score_display(self):
        # Actualiza el texto del marcador en el canvas
        self.canvas.itemconfig(self.score_text, text=f"Jugador: {self.score_player} - Oponente: {self.score_opponent}")

    def move_player_left(self, event):
        # Mueve la raqueta del jugador a la izquierda
        if self.game_running:
            x1, y1, x2, y2 = self.canvas.coords(self.player_paddle)
            if x1 > 0: # Evita que la raqueta se salga del borde izquierdo
                self.canvas.move(self.player_paddle, -15, 0)

    def move_player_right(self, event):
        # Mueve la raqueta del jugador a la derecha
        if self.game_running:
            x1, y1, x2, y2 = self.canvas.coords(self.player_paddle)
            if x2 < 600: # Evita que la raqueta se salga del borde derecho
                self.canvas.move(self.player_paddle, 15, 0)

    def move_opponent_paddle(self):
        # IA simple: la raqueta del oponente sigue la posición x de la pelota
        ball_x, ball_y, _, _ = self.canvas.coords(self.ball)
        paddle_x1, _, paddle_x2, _ = self.canvas.coords(self.opponent_paddle)
        paddle_center = (paddle_x1 + paddle_x2) / 2

        # Mueve la raqueta del oponente hacia la pelota
        if ball_x < paddle_center - 10:
            self.canvas.move(self.opponent_paddle, -2, 0)
        elif ball_x > paddle_center + 10:
            self.canvas.move(self.opponent_paddle, 2, 0)

    def game_loop(self):
        # Bucle principal del juego
        if not self.game_running:
            return

        # Mueve la pelota
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_x1, ball_y1, ball_x2, ball_y2 = self.canvas.coords(self.ball)

        # Colisión de la pelota con las paredes laterales
        if ball_x1 <= 0 or ball_x2 >= 600:
            self.ball_dx *= -1 # Invierte la dirección horizontal

        # Colisión de la pelota con la raqueta del jugador
        player_paddle_coords = self.canvas.coords(self.player_paddle)
        if ball_y2 >= player_paddle_coords[1] and ball_y1 <= player_paddle_coords[3] and \
           ball_x2 >= player_paddle_coords[0] and ball_x1 <= player_paddle_coords[2]:
            self.ball_dy *= -1 # Invierte la dirección vertical
            # Añade un pequeño cambio aleatorio a dx para un juego más dinámico
            self.ball_dx += random.uniform(-0.5, 0.5)

        # Colisión de la pelota con la raqueta del oponente
        opponent_paddle_coords = self.canvas.coords(self.opponent_paddle)
        if ball_y1 <= opponent_paddle_coords[3] and ball_y2 >= opponent_paddle_coords[1] and \
           ball_x2 >= opponent_paddle_coords[0] and ball_x1 <= opponent_paddle_coords[2]:
            self.ball_dy *= -1 # Invierte la dirección vertical
            # Añade un pequeño cambio aleatorio a dx para un juego más dinámico
            self.ball_dx += random.uniform(-0.5, 0.5)

        # Comprueba si hay puntuación
        if ball_y1 < 0: # El oponente falló
            self.score_player += 1
            self.update_score_display()
            self.reset_ball()
            if self.score_player >= 5: # Condición de victoria
                self.game_running = False
                self.canvas.itemconfig(self.game_status_text, text="¡Has ganado!") # Muestra el mensaje de victoria
                messagebox.showinfo("Fin del Juego", "¡Has ganado!")
                self.start_button.config(text="Reiniciar Juego", command=self.reset_game)
                return
        elif ball_y2 > 400: # El jugador falló
            self.score_opponent += 1
            self.update_score_display()
            self.reset_ball()
            if self.score_opponent >= 5: # Condición de derrota
                self.game_running = False
                self.canvas.itemconfig(self.game_status_text, text="¡Has perdido!") # Muestra el mensaje de derrota
                messagebox.showinfo("Fin del Juego", "¡Has perdido!")
                self.start_button.config(text="Reiniciar Juego", command=self.reset_game)
                return

        self.move_opponent_paddle() # Mueve la raqueta del oponente

        # Continúa el bucle del juego
        self.root.after(10, self.game_loop) # Actualiza cada 10 milisegundos

if __name__ == "__main__":
    root = tk.Tk()
    game = TennisGame(root)
    root.mainloop()
# Asegúrate de que el código se ejecuta correctamente
# y que la ventana del juego se cierra adecuadamente al finalizar.  
# Puedes probar el juego ejecutando este script en tu entorno local.
# Asegúrate de que tienes tkinter instalado y configurado correctamente.
# Puedes instalar tkinter si no lo tienes con: pip install tk
# Asegúrate de que el código se ejecuta correctamente
# y que la ventana del juego se cierra adecuadamente al finalizar. 


