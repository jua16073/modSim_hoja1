# Tasukete Kudasai
from tkinter import * 



def canvas():
  master = Tk()

  canvas_width = 80
  canvas_height = 80
  w = Canvas(master, 
            width=canvas_width,
            height=canvas_height)
  w.pack()

  y = int(canvas_height / 2)
  w.create_line(0, y, canvas_width, y, fill="#476042")

  mainloop()

