from tkinter import Tk

from gui import UI

if __name__ == "__main__":
    window = Tk()
    window.title("Gomoku")
    window.geometry("1000x800")


    ui = UI(window)
    ui.start()

    window.mainloop()