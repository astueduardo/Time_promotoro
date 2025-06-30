
-----

# ⌛ Pomodoro Timer

## Descripción

El **Pomodoro Timer** es una aplicación de escritorio simple y efectiva construida con Python y Tkinter, diseñada para ayudarte a gestionar tu tiempo y mejorar tu productividad siguiendo la popular técnica Pomodoro. Esta técnica divide tu tiempo de trabajo en intervalos, tradicionalmente de 25 minutos, seguidos de breves descansos. Los descansos más largos se toman después de cada cuatro "pomodoros".

Esta herramienta te proporciona un temporizador visual y funcional para:

  * Mantener un seguimiento claro de tus sesiones de trabajo.
  * Recordarte cuándo tomar un descanso.
  * Ayudarte a mantener la concentración y evitar el agotamiento.

## Características

  * **Temporizador de Pomodoro:** Sesiones de trabajo de 25 minutos.
  * **Descansos Cortos:** Descansos de 5 minutos después de cada sesión de trabajo.
  * **Descansos Largos:** Descansos de 15 minutos después de cada 4 pomodoros completados.
  * **Interfaz de Usuario Intuitiva:** Interfaz gráfica sencilla y limpia.
  * **Contador de Pomodoros:** Rastrea cuántas sesiones de trabajo has completado.
  * **Notificaciones:** Alertas visuales y sonoras (un simple "bell" de Tkinter) cuando una sesión termina.
  * **Controles Básicos:** Botones para Iniciar, Pausar, Reiniciar y Saltar sesiones.

## Requisitos

  * Python 3.x
  * `tkinter` (generalmente viene incluido con las instalaciones estándar de Python)

## Instalación

1.  **Clonar el Repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/pomodoro-timer.git
    cd pomodoro-timer
    ```

2.  **Ejecutar la Aplicación:**

    ```bash
    python pomodoro_timer.py
    ```

    (Asegúrate de reemplazar `pomodoro_timer.py` con el nombre de tu archivo si es diferente).

## Uso

Una vez que inicies la aplicación, verás la ventana del Pomodoro Timer:

  * **Iniciar:** Haz clic en el botón **"Iniciar"** para comenzar la sesión de trabajo.
  * **Pausar:** Si necesitas un descanso o una interrupción, haz clic en **"Pausar"**.
  * **Reiniciar:** El botón **"Reiniciar"** restablece el temporizador a una nueva sesión de trabajo de 25 minutos y borra el contador de pomodoros.
  * **Saltar:** Usa el botón **"Saltar"** para terminar la sesión actual y pasar a la siguiente fase (descanso si estabas trabajando, o trabajo si estabas en un descanso).
  * **Contador de Pomodoros:** La aplicación llevará un registro de los "Pomodoros" completados, que se incrementará cada vez que finalices una sesión de trabajo completa.

### Ciclo del Pomodoro

El temporizador sigue el ciclo estándar de la técnica Pomodoro:

1.  **Trabajo:** 25 minutos
2.  **Descanso Corto:** 5 minutos (después de 1, 2, 3 y 5to pomodoro, etc.)
3.  **Descanso Largo:** 15 minutos (después de cada 4 pomodoros completados)

## Personalización (Opcional)

Puedes modificar las constantes al principio del script `pomodoro_timer.py` para ajustar los tiempos o los colores de la interfaz:

```python
# --- Constantes ---
TIEMPO_TRABAJO = 25 * 60  # 25 minutos en segundos
TIEMPO_DESCANSO_CORTO = 5 * 60
TIEMPO_DESCANSO_LARGO = 15 * 60
COLOR_FONDO = "#2E2E2E"
COLOR_TEXTO = "#FFFFFF"
COLOR_TIMER = "#00FF00"
```

## Contribuciones

¡Las contribuciones son bienvenidas\! Si tienes ideas para mejorar, nuevas características o encuentras algún error, no dudes en:

1.  Hacer un "fork" del repositorio.
2.  Crear una nueva rama (`git checkout -b feature/AmazingFeature`).
3.  Realizar tus cambios y hacer "commit" (`git commit -m 'Add some AmazingFeature'`).
4.  Subir tus cambios (`git push origin feature/AmazingFeature`).
5.  Abrir un "Pull Request".

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

-----

