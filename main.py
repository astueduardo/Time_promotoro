import tkinter as tk
from tkinter import messagebox
# Para un sonido multiplataforma, instala 'playsound': pip install playsound
# from playsound import playsound

# --- Constantes ---
TIEMPO_TRABAJO = 25 * 60  # 25 minutos en segundos
TIEMPO_DESCANSO_CORTO = 5 * 60
TIEMPO_DESCANSO_LARGO = 15 * 60
COLOR_FONDO = "#2E2E2E"
COLOR_TEXTO = "#FFFFFF"
COLOR_TIMER = "#00FF00"

class PomodoroTimer:
    def __init__(self, root):
        self.ventana = root
        self.ventana.title("Pomodoro Timer")
        self.ventana.geometry("350x250")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg=COLOR_FONDO)

        # --- Variables de estado ---
        self.tiempo_restante_seg = TIEMPO_TRABAJO
        self.en_ejecucion = False
        self.es_trabajo = True
        self.pomodoros_completados = 0
        self.temporizador_id = None

        # --- Variables de la interfaz ---
        self.tiempo_display = tk.StringVar()
        self.estado_sesion = tk.StringVar()

        self._crear_widgets()
        self.reiniciar_temporizador()

    def _crear_widgets(self):
        # Etiquetas
        etiqueta_tiempo = tk.Label(self.ventana, textvariable=self.tiempo_display, font=("Roboto", 50), bg=COLOR_FONDO, fg=COLOR_TIMER)
        etiqueta_tiempo.pack(pady=10)

        etiqueta_estado = tk.Label(self.ventana, textvariable=self.estado_sesion, font=("Roboto", 16), bg=COLOR_FONDO, fg=COLOR_TEXTO)
        etiqueta_estado.pack()

        self.etiqueta_contador = tk.Label(self.ventana, text="Pomodoros: 0", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Roboto", 10))
        self.etiqueta_contador.pack(pady=5)

        # Botones
        frame_botones = tk.Frame(self.ventana, bg=COLOR_FONDO)
        frame_botones.pack(pady=10)

        btn_iniciar = tk.Button(frame_botones, text="Iniciar", command=self.iniciar_temporizador, bg="#4CAF50", fg="white", font=("Roboto", 12), borderwidth=0, padx=10, pady=5)
        btn_iniciar.grid(row=0, column=0, padx=5)

        btn_pausar = tk.Button(frame_botones, text="Pausar", command=self.pausar_temporizador, bg="#F44336", fg="white", font=("Roboto", 12), borderwidth=0, padx=10, pady=5)
        btn_pausar.grid(row=0, column=1, padx=5)

        btn_reiniciar = tk.Button(frame_botones, text="Reiniciar", command=self.reiniciar_temporizador, bg="#2196F3", fg="white", font=("Roboto", 12), borderwidth=0, padx=10, pady=5)
        btn_reiniciar.grid(row=0, column=2, padx=5)

        btn_saltar = tk.Button(frame_botones, text="Saltar", command=self.saltar_sesion, bg="#FF9800", fg="white", font=("Roboto", 12), borderwidth=0, padx=10, pady=5)
        btn_saltar.grid(row=0, column=3, padx=5)


    def _actualizar_display(self):
        minutos = self.tiempo_restante_seg // 60
        segundos = self.tiempo_restante_seg % 60
        self.tiempo_display.set(f"{minutos:02d}:{segundos:02d}")

    def _contar(self):
        if self.en_ejecucion and self.tiempo_restante_seg > 0:
            self.tiempo_restante_seg -= 1
            self._actualizar_display()
            self.temporizador_id = self.ventana.after(1000, self._contar)
        elif self.en_ejecucion and self.tiempo_restante_seg <= 0:
            self.en_ejecucion = False
            # Aquí podrías usar una librería multiplataforma
            # playsound("alert.wav")
            self.ventana.bell() # Sonido simple y nativo de tkinter
            messagebox.showinfo("Tiempo terminado", "¡Sesión finalizada!")
            self.saltar_sesion(fue_completado=True)

    def iniciar_temporizador(self):
        if not self.en_ejecucion:
            self.en_ejecucion = True
            self._contar()

    def pausar_temporizador(self):
        self.en_ejecucion = False
        if self.temporizador_id:
            self.ventana.after_cancel(self.temporizador_id)

    def reiniciar_temporizador(self):
        self.pausar_temporizador()
        self.es_trabajo = True
        self.tiempo_restante_seg = TIEMPO_TRABAJO
        self.estado_sesion.set("Sesión: Trabajo")
        self._actualizar_display()

    def saltar_sesion(self, fue_completado=False):
        self.pausar_temporizador()
        if self.es_trabajo and fue_completado:
            self.pomodoros_completados += 1
            self.etiqueta_contador.config(text=f"Pomodoros: {self.pomodoros_completados}")

        self.es_trabajo = not self.es_trabajo

        if self.es_trabajo:
            self.tiempo_restante_seg = TIEMPO_TRABAJO
            self.estado_sesion.set("Sesión: Trabajo")
        else: # Es descanso
            if self.pomodoros_completados > 0 and self.pomodoros_completados % 4 == 0:
                self.tiempo_restante_seg = TIEMPO_DESCANSO_LARGO
                self.estado_sesion.set("Sesión: Descanso Largo")
            else:
                self.tiempo_restante_seg = TIEMPO_DESCANSO_CORTO
                self.estado_sesion.set("Sesión: Descanso")
        
        self._actualizar_display()


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = PomodoroTimer(ventana_principal)
    ventana_principal.mainloop()