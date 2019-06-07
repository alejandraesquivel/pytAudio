import matplotlib.pyplot as mpl
import numpy as np
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg

class Window(Frame):
    
    def __init__ (self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        
    def init_window(self):
        self.master.title('Proyecto final senales')
        self.pack(fill=BOTH, expand=1)
        self.draw_figure()
        self.create_menu()
        
        
    def create_menu(self):
        menu_audios=Menu(self.master)
        self.master.config(menu=menu_audios)
        audios=Menu(menu_audios)
        
    def salir(self):
        self.exit
    
    def boton_graficar_df(self):
        
    def boton_graficar_dt(self):
        
    def ab
        
    def draw_figure(self,canvas, figure, loc=(0, 0)):
        """ Draw a matplotlib figure onto a Tk canvas
        loc: location of top-left corner of figure on canvas in pixels.
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
window = tk.Tk()
window.geometry('900x600')
# Let Tk take over
app=Window(window)
tk.mainloop()
