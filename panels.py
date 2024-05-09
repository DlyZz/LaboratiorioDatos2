import customtkinter as ctk

class Panel(ctk.CTkFrame):
  def __init__(self, parent):
    super().__init__(parent, fg_color='#EEEEEE')
    self.pack(fill='x', pady=4, ipady=8)

class SimplePanel(Panel):
  def __init__(self, parent, text, text_button, button_command):
    super().__init__(parent)

    #layout
    self.rowconfigure((0,1), weight=1)
    self.columnconfigure((0,1), weight=1)

    ctk.CTkLabel(self, text=text, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=0, padx=4, sticky='w')
    entry = ctk.CTkEntry(self, font=ctk.CTkFont(family="Roboto", size=14))
    entry.grid(row=1, column=0, columnspan=2, sticky='ew', padx=4, pady=4)
    ctk.CTkButton(self, text=text_button, font=ctk.CTkFont(family="Roboto", size=14), corner_radius=5, command=button_command(entry)).grid(row=2, column=1, sticky='e', padx=4, pady=4)

class InfoPanel(Panel):
  def __init__(self, parent, name, city, country, latitude, longitude):
    super().__init__(parent)

    #layout
    self.rowconfigure((0,1,2,3,4), weight=1)
    self.columnconfigure((0,1), weight=1)

    ctk.CTkLabel(self, text="Nombre:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=0, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=name, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=0, column=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text="Ciudad:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=1, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=city, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=1, column=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text="País:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=2, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=country, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=2, column=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text="Latitud:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=3, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=latitude, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=3, column=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text="Longitud:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=4, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=longitude, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=4, column=1, padx=4, sticky='w')

class LongestPathPanel(Panel):
  def __init__(self, parent, minPaths, distance):
    super().__init__(parent)

    #layout
    self.rowconfigure(0, weight=1)
    self.columnconfigure(0, weight=1)

    ctk.CTkLabel(self, text="Camino:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=minPaths, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=0, column=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text="Distancia:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text=distance, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=1, column=1, padx=4, sticky='w')
    