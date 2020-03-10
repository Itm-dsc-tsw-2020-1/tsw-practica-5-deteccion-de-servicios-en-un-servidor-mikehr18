import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


# Inicio del cÃ³digo
print ("Python conectandose a MySQL")

# ConectÃ¡ndose a MySQL




class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], height=10, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self, text=title, background="#ECCCCE", font=("Helvetica", 26))
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers, 
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")

        # Agregamos dos scrollbars 
        vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="left")

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=tkFont.Font().measure(header.title()))

    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width)



def ventana_reporte(parent=None):
    t3 = tk.Toplevel(parent, bg="#3333ff")
    t3.title("Reporte")
    t3.geometry('500x500')
    t3.configure(bg="#3333ff")
    t3.focus_set()
    t3.grab_set()

    puertos_headers = ( u"puerto", u"status",
                        u"service"
                        )


    clientes_tab = Table(t3, title="200.33.171.20", headers=puertos_headers)
    clientes_tab.pack()

    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='nmap' )
    operacion = conexion.cursor()

    operacion.execute( "SELECT * FROM puertos" )


    

    for row in operacion:
        clientes_tab.add_row(row)





ventana  = tk.Tk()
ventana_reporte(parent=ventana)
ventana.mainloop()









