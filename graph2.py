import matplotlib.pyplot as mpl
import numpy as np
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo

# Create a canvas
w, h = 900,900
window = tk.Tk()
window.title("Proyecto final, Analisis con 2 senales")
canvas = tk.Canvas(window, width=w, height=h)
canvas.pack()

# Generate some example data
X = np.linspace(0, 2 * np.pi, 50)       #graficas a poner
Y = np.sin(X)

# Create the figure we desire to add to an existing canvas
fig = mpl.figure(figsize=(3, 2))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(X, Y)

# Keep this handle alive, or else figure will disappear
fig_x, fig_y = 75, 75
fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
fig_w, fig_h = fig_photo.width(), fig_photo.height()

# Add more elements to the canvas, potentially on top of the figure
canvas.create_text(150, 50, text="Grafica Audio 1 en Dominio de tiempo", anchor="s")


# Create the figure we desire to add to an existing canvas
fig2 = mpl.figure(figsize=(3, 2))
ax2 = fig2.add_axes([0, 0, 1, 1])
ax2.plot(X, Y)

# Keep this handle alive, or else figure will disappear
fig2_x, fig2_y = 75,350
fig2_photo = draw_figure(canvas, fig2, loc=(fig2_x, fig2_y))
fig2_w, fig2_h = fig2_photo.width(), fig2_photo.height()

# Add more elements to the canvas, potentially on top of the figure
canvas.create_text(170,320, text="Grafica Audio 1 en Dominio de Frecuencia", anchor="s")

# Create the figure we desire to add to an existing canvas
fig3 = mpl.figure(figsize=(3, 2))
ax3= fig3.add_axes([0,0, 1, 1])
ax3.plot(X, Y)

# Keep this handle alive, or else figure will disappear
fig3_x, fig3_y = 450, 75
fig3_photo = draw_figure(canvas, fig3, loc=(fig3_x, fig3_y))
fig3_w, fig3_h = fig3_photo.width(), fig3_photo.height()

# Add more elements to the canvas, potentially on top of the figure
canvas.create_text(550, 50, text="Grafica Audio 2 en Dominio de tiempo", anchor="s")


# Create the figure we desire to add to an existing canvas
fig4 = mpl.figure(figsize=(3, 2))
ax4 = fig4.add_axes([0,0, 1, 1])
ax4.plot(X, Y)

# Keep this handle alive, or else figure will disappear
fig4_x, fig4_y = 450,350
fig4_photo = draw_figure(canvas, fig4, loc=(fig4_x, fig4_y))
fig4_w, fig4_h = fig4_photo.width(), fig4_photo.height()

# Add more elements to the canvas, potentially on top of the figure
canvas.create_text(570,320, text="Grafica Audio 2 en Dominio de Frecuencia", anchor="s")


# Create the figure we desire to add to an existing canvas
fig_resul = mpl.figure(figsize=(3, 2))
ax_r = fig_resul.add_axes([0,0, 1, 1])
ax_r.plot(X, Y)

# Keep this handle alive, or else figure will disappear
fig_x_r, fig_y_r = 300,620
fig_photo_r = draw_figure(canvas, fig_resul, loc=(fig_x_r, fig_y_r))
fig_w_r, fig_h_r = fig_photo_r.width(), fig_photo_r.height()

# Add more elements to the canvas,   potentially on top of the figure
canvas.create_text(450,600, text="Grafica Resultado de Operaciones", anchor="s")
#menu de audios
var=tk.StringVar(window)
opciones=['audio1','audio2']
op=tk.OptionMenu(window,var,*opciones)
op.config(width=30)
op.pack(side='right',padx=1,pady=1)
	
btn =tk.Button(window, text="Reproducir")
btn.pack(side='right',padx=5,pady=5)

bton =tk.Button(window, text="Graficar")
bton.pack(side='right',padx=5,pady=5)

#boton menu
v=tk.StringVar(window)
opcioness=['Suma','Resta','Multiplicacion']
opo=tk.OptionMenu(window,v,*opcioness)
opo.config(width=30)
opo.pack(side='right',padx=1,pady=1)
    
# Let Tk take over
tk.mainloop()