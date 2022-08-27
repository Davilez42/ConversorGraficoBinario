



from msilib.schema import Icon
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from xmlrpc.client import FastMarshaller
from controlador import *
class conversorBinarios(tk.Frame):
    def __init__(self,master) -> None:
       super().__init__(master )
       self.cajatexto1 = tk.Entry(master)
       self.cajatexto1.place(relx=0.50,rely=0.30,relheight=0.20,relwidth=0.40)
       
       self.cajaResultado = tk.Label(master)
       self.cajaResultado.config(bg="#DBFFFF")
       self.cajaResultado.place(relx=0.50,rely=0.70,relheight=0.20,relwidth=0.40)
       
       self.etiqueta = tk.Label(master,text="a")
       self.etiqueta.place(relx=0.65,rely=0.55,relheight=0.1,relwidth=0.1)
     
      #Botno 
       self.botonConvertir = tk.Button(master,text="Convertir",command=lambda:self.logica())
       self.botonConvertir.place(relx=0.10,rely=0.70,relheight=0.20,relwidth=0.30)
       
       valor_defecto = "Binario a Decimal"
       self.modos= ttk.Combobox(master)
       self.modos.set("Binario a Decimal")
       self.modos['values'] = ["Binario a Decimal","Decimal a Binario"]
       self.modos.place(relx=0.10,rely=0.30,relheight=0.20,relwidth=0.30)
       
       self.etiqueta2 = tk.Label(master,text="Modos")
       self.etiqueta2.place(relx=0.10,rely=0.20,relheight=0.10,relwidth=0.30)

       self.barramenu = tk.Menu(master)
       self.mnu_Informacion =tk.Menu(self.barramenu,tearoff=0)#creo un menu
       self.mnu_Informacion.add_command(label="Version",command=lambda:self.Version())
       self.mnu_Informacion.add_command(label="Info",command=lambda:self.Info())

       self.mnu_opciones = tk.Menu(self.barramenu,tearoff=0)
       self.mnu_opciones.add_command(label="Salir",command=lambda:self.salir())
  
       self.barramenu.add_cascade(label="Informacion",menu=self.mnu_Informacion)
       self.barramenu.add_cascade(label="opciones",menu=self.mnu_opciones)

       self.master.config(menu=self.barramenu)
      
        
        
    def logica(self):
        modo = self.modos.get()
        if "Binario a Decimal"==modo :
            resultado = convertiraDecimal(int(self.cajatexto1.get()))
            self.cajaResultado["text"] = resultado
        if "Decimal a Binario"==modo :
            resultado = convertiraBinario(int(self.cajatexto1.get()))
            self.cajaResultado["text"] = resultado    
            
    def salir(self):
        desicion = messagebox.askquestion("Salir","Desea salir de la aplicacion?")
        if desicion == "yes":
            ventana.destroy()

    def Info(self):
         messagebox.showinfo("Info","Autor: Jose David Suarez Cardona")

    def Version(self):
        messagebox.showinfo("Version","Version: 1.1")
    
ventana = tk.Tk()
ventana.geometry("400x200")
ventana.grid()
ventana.config(bg="#CCFFCC")
App = conversorBinarios(ventana)
App.mainloop()    