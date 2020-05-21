#!/usr/bin/env python
import tkinter as tk
import webbrowser


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.shared_data = {
            "Send to Web": tk.StringVar()
        }

        self.frames = {
            'MainApp': MainApp(self, self)
        }

        self.current_frame = None
        self.show_frame('MainApp')

    def show_frame(self, name):
        if self.current_frame:
            self.current_frame.forget()
        self.current_frame = self.frames[name]
        self.current_frame.pack()

        self.current_frame.update_widgets()  # <-- update data in widgets


class MainApp(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="WhatsApp Chat Ver 1.1 Created by Nati").pack(side="top", fill="x", pady=10)

        self.entry1 = tk.Entry(self, textvariable=self.controller.shared_data["Send to Web"])
        self.entry1.pack()

        call_button = tk.Button(self, text="Whatsapp Desktop Client", command=self._desktopclient)
        call_button.pack()

        web_client = tk.Button(self, text="WhatsApp Web", command=self._webchrome)
        web_client.pack()

        tk.Label(self, text="Chat without saving the contacts enjoy ;)").pack(side="top", fill="x", pady=10)

    def _desktopclient(self):

        phonenumber = self.controller.shared_data["Send to Web"].get()

        caller_web_link = ("https://wa.me/972" + phonenumber)
        webbrowser.open(caller_web_link)

    def _webchrome(self):

        phonenumber = self.controller.shared_data["Send to Web"].get()

        caller_web_link = ("https://web.whatsapp.com/send?phone=972" + phonenumber)
        webbrowser.open(caller_web_link)

    def update_widgets(self):
        pass


if __name__ == "__main__":
    App = App()

    w = 350  # width for the Tk root
    h = 150  # height for the Tk root

    # get screen width and height
    ws = App.winfo_screenwidth()  # width of the screen
    hs = App.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    App.geometry('%dx%d+%d+%d' % (w, h, x, y))
    App.title("Whatsapp")
    App.mainloop()
