# Find the coordinates of the Mouse
import tkinter

def mouse_click(event):

    # retrieve XY cords as a tuple
    coords = root.winfo_pointerxy()
    print('coords: {}' .format(coords))
    print('X: {}' .format(coords[0]))
    print('Y: {}' .format(coords[1]))

root = tkinter.Tk()
root.bind('<Button>', mouse_click)
root.mainloop()