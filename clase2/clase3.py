from tkinter import Frame, Tk
from tkinter.messagebox import askyesno

ventanaPrincipal = Tk()
ventanaPrincipal.title('Prueba de eventos')

def actionc_click(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)
    
def precionar_tecla(event):
    print("pressed", repr(event.char))
    
def el_usuario_quiere_salir():
    if askyesno('salir de la aplicacion', '¿seguro que quieres cerra la aplicacion'):
        ventanaPrincipal.destroy()
        
frame = Frame(ventanaPrincipal, width=500, height=500)
frame.bind("<Key>", precionar_tecla)
frame.bind("<Button-1>", actionc_click)
frame.pack()

ventanaPrincipal.protocol('WM_DELETE_WINDOW', el_usuario_quiere_salir)
ventanaPrincipal.mainloop()