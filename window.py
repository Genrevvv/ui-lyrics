from tkinter import *

class Window:
    open_windows = 0

    def __init__(self, parent, title, width, height, x_offset, y_offset):
        self.parent = parent
        self.window = Toplevel(parent)
        self.window.title(title)

        Window.open_windows += 1
        x = ((parent.winfo_screenwidth() - width) // 2 ) + x_offset
        y = ((parent.winfo_screenheight() - height) // 2) + y_offset

        self.window.geometry(f'{width}x{height}+{x}+{y}')
        self.window.protocol('WM_DELETE_WINDOW', self.close)

        self.content = Frame(self.window)
        self.content.pack(padx=20, pady=20)

    def show_lyrics(self, lyrics, i=0):
        if i >= len(lyrics):
            return
        
        text, delay = lyrics[i]
        self.add_text(text)

        self.parent.after(delay, lambda: self.show_lyrics(lyrics, i+1))


    def add_text(self, text, fs=25, fg='black'):
        Label(self.content, text=text, font=('Arial', fs), fg=fg).pack(expand=True)
        
    def close(self):
        # Window.open_windows -= 1
        # self.window.destroy()

        # if Window.open_windows == 0:
        #     self.parent.destroy()
        
        self.parent.destroy()
