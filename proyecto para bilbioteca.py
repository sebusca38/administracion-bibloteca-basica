#crear ventana para biblioteca
#3 pantallas
#ingreso informacion libros
#ingreso informacion prestamo
#ingreaso informacion alumno
from tkinter import *
from tkinter import ttk
import pymysql
import datetime

class algoritmo(object):
    
    def __init__(self):
        self.iniciarconexion()
        
    def iniciarconexion():
        try:
            conexion=pymysql.connect("127.0.0.1","root","","administradorbibloteca")
            if conexion!="null":
                estado="conexion exitosa"
        except Exception as e:
            estado=e
        finally:
            conexion.close()
        return estado
    def consultasql(sql,datos):
        claves=kwords.keys()
        valores=[]
        for i in range(len(claves)):
            valores.append(kwords[claves[i]])
        try:
            conexion=pymysql.connect("127.0.0.1","root","","administradorbibloteca")
            if conexion!="null":
                try:
                    with conexion.cursor() as cursor:
                        cursor.execute(sql,valores)
                        conexion.commit()
                finally:
                    conexion.close()
        except Exception as e:
            print(e)
        finally:
            conexion.close()            
    def inviodeinformacion(nombretabla,opciones,*args,**kwords):
        if opciones==1:
            datos=kwords
            claves=kwords.keys()
            sql="INSERT INTO "+nombretabla+"(RUT, NOMBRE, APELLIDO, CARRERA, SEMENSTRE, CELULAR, DIRECCION_PARTICULAR, CIUDAD, ATRAZOS) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            consultasql(sql,datos)
        elif opciones==2:
            sql="DELETE FROM"+nombretabla+"WHERE rut=%s"
        elif opciones==3:
            sql="SELECT * FROM"+nombretabla+"WHERE "+args[0]+"=%s"                   
class diseño(algoritmo):
    def __init__(self):
            self.principal=Tk()
            self.principal.title("menu de inicio")
            self.principal.geometry("500x200")
            self.cerrar = Button(self.principal,text="cerrar",command=self.principal.destroy()).place(x=100,y=80)
            self.prestamo=Button(self.principal,text="prestar",command=diseño.prestamo(self.principal)).place(x=100,y=40)
            self.informacion_de_al=Button(self.principal,text="informacion del alumno",command=diseño.infodealumno(self.principal)).place(x=150,y=40)
            self.libros_de_bibloteca=Button(self.principal,text="libros de la bibloteca",command=diseño.librobiloteca(self.principal)).place(x=300,y=40)
            self.principal.mainloop()
    def nuevainstancia(actual):
        app=Toplevel(actual)
        app.title("datos de conexion")
        app.geometry("500x200")
        
    def prestamo(actual):
        ventana2=Toplevel(actual)
        ventana2.title("Prestamo libro")
        ventana2.geometry("500x300")
        
        prestamo=Label(ventana2,text="INGRESAR INFORMACION DEL PRESTAMO").place(x=130,y=10)
        
        ID = Label(ventana2,text="ID: ").place(x=10,y=40)
        var8 = StringVar()
        texto1 = Entry(ventana2,textvariable=var8).place(x=110,y=43)
    
        idli = Label(ventana2,text="ID Libro: ").place(x=250,y=40)
        var9 = StringVar()
        texto2 = Entry(ventana2,textvariable=var9).place(x=310,y=43)
        
        IDalu= Label(ventana2,text="ID Alumno: ").place(x=10,y=80)
        var10 = StringVar()
        texto3 = Entry(ventana2,textvariable=var10).place(x=110,y=83)
        
        
        aceptar = Button(ventana2,text="Aceptar").place(x=10,y=250)
        cancelar = Button(ventana2,text="Cancelar",command=ventana2.destroy).place(x=300,y=250)
        
        ventana2.mainloop()
    def infodealumno(actual):
        self.ventana3=Toplevel(actual)
        self.ventana3.title("Información alumno")
        self.ventana3.geometry("500x300")
        
        self.alumno=Label(ventana3,text="INGRESAR INFORMACION DEL ALUMNO").place(x=130,y=10)
        
        self.nombre = Label(ventana3,text="Nombre alumno: ").place(x=10,y=40)
        self.var13 = StringVar()
        self.texto1 = Entry(ventana3,textvariable=var13).place(x=110,y=43)
        
        self.apellido=Label(self.ventana3,text="apellido: ")
        self.valorapellido=StringVar()
        self.enapellido=Entry(self.ventana3,textvariable=valorapellido)
        
        self.semestre=Label(ventana3,text="semestre: ")
        self.valorsemestre=IntVar()
        self.ensemestre=Entry(ventana3,textvariable=valorsemestre)
        
        
        self.rut = Label(ventana3,text="Rut: ").place(x=250,y=40)
        self.var14 = StringVar()
        self.texto2 = Entry(ventana3,textvariable=var14).place(x=310,y=43)
        
        self.carrera= Label(ventana3,text="Carrera: ").place(x=10,y=80)
        self.var15 = StringVar()
        self.texto3 = Entry(ventana3,textvariable=var15).place(x=110,y=83)
        
        self.numero = Label(ventana3,text="Número de contacto: ").place(x=250,y=80)
        self.var16 = StringVar()
        self.texto4 = Entry(ventana3,textvariable=var16).place(x=370,y=83)
        
        self.ciudad = Label(ventana3,text="Ciudad: ").place(x=10,y=120)
        self.var17 = StringVar()
        self.texto5 = Entry(ventana3,textvariable=var17).place(x=110,y=123)
        
        self.Dirección= Label(ventana3,text="Dirección: ").place(x=10,y=80)
        self.var18 = StringVar()
        self.texto6 = Entry(ventana3,textvariable=var18).place(x=110,y=83)
        
        self.aceptar = Button(ventana3,text="Aceptar").place(x=10,y=250)
        self.cancelar = Button(ventana3,text="Cancelar").place(x=300,y=250)
        
        self.ventana3.mainloop()


    def librobiloteca(actual):
        self.ventana = Toplevel(actual)
        self.ventana.title("Libros Bilblioteca")
        self.ventana.geometry("500x300")
        
        #Ingreso de libros
        #En combobox agregar la lista de libros parte values
        self.libro = Label(ventana,text="INGRESAR INFORMACION DEL LIBRO").place(x=130,y=10)
            
        self.autor = Label(ventana,text="Autor: ").place(x=250,y=40)
        self.var1 = StringVar()
        self.texto1 = Entry(ventana,textvariable=var1).place(x=310,y=43)
        
        self.editorial= Label(ventana,text="Editorial: ").place(x=10,y=80)
        self.var2 = StringVar()
        self.texto2 = Entry(ventana,textvariable=var2).place(x=100,y=83)
        
        self.año = Label(ventana,text="Año: ").place(x=250,y=80)
        self.var3 = StringVar()
        self.texto = Entry(ventana,textvariable=var3).place(x=310,y=83)
        
        self.tipo = Label(ventana,text="Tipo: ").place(x=10,y=120)
        self.var4 = StringVar()
        self.texto3 = Entry(ventana,textvariable=var4).place(x=100,y=123)
        
        self.id_libro = Label(ventana,text="ID Libro: ").place(x=250,y=120)
        self.var5 = StringVar()
        self.texto6 = Entry(ventana,textvariable=var5).place(x=310,y=123)
        
        self.isbn= Label(ventana,text="ISBN: ").place(x=10,y=160)
        self.var6 = StringVar()
        self.texto4 = Entry(ventana,textvariable=var6).place(x=100,y=163)
        
        self.cantidad  = Label(ventana,text="Cantidad: ").place(x=250,y=160)
        self.var7 = StringVar()
        self.texto5 = Entry(ventana,textvariable=var7).place(x=310,y=163)
        
        
        self.aceptar = Button(ventana,text="Aceptar").place(x=10,y=250)
        self.cancelar = Button(ventana,text="Cancelar").place(x=300,y=250)
        
        self.ventana.mainloop()

    