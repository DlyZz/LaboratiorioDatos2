from numpy import infty
from panels import *
import customtkinter as ctk
from tkinter import messagebox


class Menu(ctk.CTkTabview):
  def __init__(self, parent, graph, app):
    super().__init__(parent)
    self.grid(row=0, column=0, sticky='nsew')

    #tabs
    self.add('Información')
    self.add('Caminos Mínimos Más Largos')
    self.add('Caminos Mínimo')

    #frames
    InfoFrame(self.tab('Información'),graph, app)
    self.longestPathFrame = LongestPathFrame(self.tab('Caminos Mínimos Más Largos'), graph, app)

  
class InfoFrame(ctk.CTkFrame):
  def __init__(self, parent, graph, app):
    super().__init__(parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

    def searchCommand(entry):
      return lambda: self.searchAirport(entry, graph) 
    
    self.infoPanel = None
    SimplePanel(self, 'Ingrese el código del aeropuerto a buscar: ', 'Buscar Aeropuerto', searchCommand)
  
  def searchAirport(self, entry, graph):
    code = entry.get().upper()
    if self.infoPanel: self.infoPanel.destroy()
    vertex = graph.getVertex(code)
    if vertex:
      self.infoPanel = InfoPanel(self, vertex.data['Name'], vertex.data['City'], vertex.data['Country'], vertex.data['Latitude'], vertex.data['Longitude']  )
    else:
      messagebox.showerror('Error', 'El aeropuerto no existe en la base de datos.')
      entry.delete(0, 'end')

class LongestPathFrame(ctk.CTkFrame):
  def __init__(self, parent, graph, app):
    super().__init__(parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

     # Layout
    self.rowconfigure(0, weight=1)
    self.columnconfigure(0, weight=1)

    # Scrollable Frame
    self.scroll_frame = ctk.CTkScrollableFrame(self)
    self.scroll_frame.pack(fill='both', expand=True)


    def searchCommand(entry):
      return lambda: self.searchLongestPath(entry, graph) 
    
    self.infoPanel = None
    SimplePanel(self.scroll_frame, 'Ingrese el código del aeropuerto de origen: ', 'Ver Rutas', searchCommand)

  def searchLongestPath(self, entry, graph):
    code = entry.get().upper()
    vertex = graph.getVertex(code)
    if self.infoPanel: self.infoPanel.destroy()
    minPaths = graph.dijkstra(vertex)
    minPaths = {
      key: minPaths[key]
      for key in sorted( minPaths, key=lambda x: minPaths[x][0], reverse = True)
      if not minPaths[key][0] == infty
    }
  
    i = 0
    for airport in minPaths:
      pathAux = graph.getPath(minPaths, vertex, airport)
      path = pathAux[pathAux.index('(') + 1:pathAux.index(')')].split('->')
      LongestPathPanel(self.scroll_frame, graph.getPath(minPaths, vertex, airport), float(path[0]))
      InfoPanel(self.scroll_frame, airport.data['Name'], airport.data['City'], airport.data['Country'], airport.data['Latitude'], airport.data['Longitude'])
      i += 1
      if i>=10:
        break


  