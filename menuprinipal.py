#crear ventana para biblioteca
#3 pantallas
#ingreso informacion libros
#ingreso informacion prestamo
#ingreaso informacion alumno
import sys
import pymysql
from datetime import *
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import menuprinipal_support

def vp_start_gui():
    global val, w, root
    root = Tk()
    top = menuprincipal (root)
    menuprinipal_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = menuprincipal (w)
    menuprinipal_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None
class algoritmo(object):
    fechaactual=datetime.date(datetime.today())
    fechaactual=str(fechaactual)
    fechaactual2=fechaactual.split("-")
    dia=int(fechaactual2[2])
    dia=dia+7
    dia=str(dia)
    fechafinal=fechaactual2[0]+"-"+fechaactual2[1]+"-"+dia
    def __init__(self):
        self.nomre="tt"
    def consultasql2(sql,*args,**kwords):
        sql1="CREATE TABLE IF NOT EXISTS alumnos(ID_ALUMNOS INT(11) AUTO_INCREMENT,RUT INT(11) NOT NULL, NOMBRE VARCHAR(40) NOT NULL, APELLIDO VARCHAR(40) NOT NULL, CARRERA VARCHAR(20) NOT NULL, SEMESTRE INT(2) NOT NULL, CELULAR INT(11) NOT NULL, DIRECCION_PARTICULAR VARCHAR(40), CIUDAD VARCHAR(20) NOT NULL, ATRAZOS INT(11) NOT NULL, PRIMARY KEY(ID_ALUMNOS))"
        sql2="CREATE TABLE IF NOT EXISTS libros(ID INT(11) AUTO_INCREMENT, AUTOR VARCHAR(60) NOT NULL, TITULO VARCHAR(50) NOT NULL, EDITORIALES VARCHAR(30) NOT NULL, ISBM VARCHAR(30) NOT NULL, GENERO VARCHAR(20), AÑO DATETIME NOT NULL, id_libros VARCHAR(20) NOT NULL, PRIMARY KEY(ID))"
        sql3="CREATE TABLE IF NOT EXISTS prestamo( ID_LIBRO1 INT(11) NOT NULL, ID_LIBRO2 INT(11) NOT NULL, ID_ALUMNOS INT(11) NOT NULL,RUT VARCHAR(80) NOT NULL,FECHA_PRESTAMO DATETIME NOT NULL,FECHA_DEVUELTA DATETIME NOT NULL,PRIMARY KEY(ID_LIBRO2))"
        sql4="CREATE TABLE IF NOT EXISTS inventario(TITULOS VARCHAR(40) NOT NULL, AUTOR VARCHAR(40) NOT NULL, EDITORIAL VARCHAR(20) NOT NULL, CANTIDAD INT(5) NOT NULL)"
        claves=kwords.keys()
        valores=kwords.values()
        valores=list(valores)
        #valores=tuple(valores)
        print(valores)
        try:
            conexion=pymysql.connect("127.0.0.1","root","","administradorbibloteca")
            if conexion!="null":
                try:
                    try:
                        with conexion.cursor() as cursor:
                            cursor.execute(sql1)
                            conexion.commit()
                        with conexion.cursor() as cursor:
                            cursor.execute(sql2)
                            conexion.commit()
                        with conexion.cursor() as cursor:
                            cursor.execute(sql3)
                            conexion.commit()
                        with conexion.cursor() as cursor:
                            cursor.execute(sql4)
                            conexion.commit()
                    except:
                        pass
                    with conexion.cursor() as cursor:
                        cursor.execute(sql,valores[:])
                        conexion.commit()
                finally:
                    conexion.close()
        except Exception as e:
            print(e)
    def consultasql(sql,*args,**kwords):
        
        sql1="CREATE TABLE IF NOT EXISTS alumnos(ID_ALUMNOS INT(11) AUTO_INCREMENT,RUT INT(11) NOT NULL, NOMBRE VARCHAR(40) NOT NULL, APELLIDO VARCHAR(40) NOT NULL, CARRERA VARCHAR(20) NOT NULL, SEMESTRE INT(2) NOT NULL, CELULAR INT(11) NOT NULL, DIRECCION_PARTICULAR VARCHAR(40), CIUDAD VARCHAR(20) NOT NULL, ATRAZOS INT(11) NOT NULL, PRIMARY KEY(ID_ALUMNOS))"
        sql2="CREATE TABLE IF NOT EXISTS libros(ID INT(11) AUTO_INCREMENT, AUTOR VARCHAR(60) NOT NULL, TITULO VARCHAR(50) NOT NULL, EDITORIALES VARCHAR(30) NOT NULL, ISBM VARCHAR(30) NOT NULL, GENERO VARCHAR(20), AÑO DATETIME NOT NULL, id_libros VARCHAR(20) NOT NULL, PRIMARY KEY(ID))"
        sql3="CREATE TABLE IF NOT EXISTS prestamo( ID_LIBRO1 INT(11) NOT NULL, ID_LIBRO2 INT(11) NOT NULL, ID_ALUMNOS INT(11) NOT NULL,RUT VARCHAR(80) NOT NULL,FECHA_PRESTAMO DATETIME NOT NULL,FECHA_DEVUELTA DATETIME NOT NULL,PRIMARY KEY(ID_LIBRO2))"
        sql4="CREATE TABLE IF NOT EXISTS inventario(TITULOS VARCHAR(40) NOT NULL, AUTOR VARCHAR(40) NOT NULL, EDITORIAL VARCHAR(20) NOT NULL, CANTIDAD INT(5) NOT NULL)"
        claves=kwords.keys()
        valores=kwords.values()
        valores=list(valores)
        #valores=tuple(valores)
        print(valores)
        try:
            conexion=pymysql.connect("127.0.0.1","root","","administradorbibloteca")
            if conexion!="null":
                try:
                    try:
                        with conexion.cursor() as cursor:
                            cursor.execute(sql1)
                            conexion.commit()
                        with conexion.cursor() as cursor:
                            cursor.execute(sql2)
                            conexion.commit()
                        with conexion.cursor() as cursor:
                            cursor.execute(sql3)
                            conexion.commit()
                        with conexion.cursor() as cursor:
                            cursor.execute(sql4)
                            conexion.commit()
                    except:
                        pass
                    try:                  
                        with conexion.cursor() as cursor:
                            cursor.execute(sql,valores[:])
                            resultado=cursor.fetchone()
                    except:
                        with conexion.cursor() as cursor:
                            cursor.execute(sql)
                            resultado=cursor.fetchone()                        
                finally:
                    conexion.close()
        except Exception as e:
            print(e)
        return resultado

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
class diseño(algoritmo):
    def regreso():
        app=Toplevel(root)
        app.title("devolucion")
        app.geometry("300x150")
        app.iconbitmap("recurso\dibujosdetiendasparaimprimir1_1_.ico")
        label1=Label(app,text="ID LIBRO1: ").place(x=10,y=40)
        var1=StringVar()
        EN=Entry(app,textvariable=var1).place(x=80,y=43)
        
        bn=Button(app,text="entregar").place(x=50,y=70)
        app.mainloop()
        
    def prestamo():
        def prestamos():
            import datetime
            
            idlib1=var8.get()
            idlib2=var9.get()
            idalum=var10.get()
            ruts=var_rut.get()
            fechaactual=datetime.date(datetime.today())
            fechaactual=str(fechaactual)
            fechaactual2=fechaactual.split("-")
            dia=int(fechaactual2[2])
            dia=dia+7
            dia=str(dia)
            fechafinal=fechaactual2[0]+"-"+fechaactual2[1]+"-"+dia
            sql="INSERT INTO prestamo(ID_LIBRO1,ID_LIBRO2,ID_ALUMNOS,RUT,FECHA_PRESTAMO,FECHA_DEVUELTA) VALUES(%s,%s,%s,%s,%s,%s)"
            sql2="SELECT NOMBRE FORM libros WHERE id_libro=%s"
            nombre=algoritmo.consultasql(sql2,ID_LIBRO1=idlib1)
            sql3="SELECT CANTIDAD FORM inventario WHERE TITULOS=%s"
            cantidad=algoritmo.consultasql(sql3,TITULOS=nombre)
            if cantidad!=0:
                cantidad=int(cantidad)
                cantidad=cantidad-1
                sq4="UPDATE inventario set CANTIDAD=%s WHERE TITULOS=%s"
                algoritmo.consultasql2(sql4,CANTIDAD=cantidad,TITULOS=nombre)
                algoritmo.consultasql2(sql,ID_LIBRO1=idlib1,ID_LIBRO2=idlib2,ID_ALUMNOS=idalum,RUT=ruts,FECHA_PRESTAMO=fechaactual,FECHA_DEVUELTA=fechafinal)
            else:
                showwarning(title="inventario vacio",message="todos los libros estan prestados",**options)
            
            
        ventana2=Toplevel(root)
        ventana2.title("Prestamo libro")
        ventana2.geometry("500x300")
        ventana2.iconbitmap("recurso\dibujosdetiendasparaimprimir1_1_.ico")
        
        
        prestamo=Label(ventana2,text="INGRESAR INFORMACION DEL PRESTAMO").place(x=130,y=10)
        
        ID = Label(ventana2,text="ID libro1 : ").place(x=80,y=40)
        var8 = StringVar()
        texto1 = Entry(ventana2,textvariable=var8).place(x=110,y=43)
    
        idli = Label(ventana2,text="ID Libro2 : ").place(x=250,y=40)
        var9 = StringVar()
        texto2 = Entry(ventana2,textvariable=var9).place(x=310,y=43)
        
        IDalu= Label(ventana2,text="ID Alumno : ").place(x=30,y=80)
        var10 = StringVar()
        texto3 = Entry(ventana2,textvariable=var10).place(x=110,y=83)
        
        labrut=Label(ventana2,text="rut: ").place(x=270,y=80)
        var_rut=StringVar()
        rut=Entry(ventana2,textvariable=var_rut).place(x=310,y=83)
        
        
        aceptar = Button(ventana2,text="Aceptar",command=prestamos).place(x=400,y=250)   
        ventana2.mainloop()
    def infodealumno():
        def enviaralumno():
            sql="INSERT INTO alumnos(RUT,NOMBRE,APELLIDO,CARRERA,SEMENSTRE,CELULAR,DIRECCION_PARTICULAR,CIUDAD,ATRAZOS) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rt=var14.get()
            nom=var13.get()
            apll=valorapellido.get()
            carr=var15.get()
            sem=valorsemestre.get()
            celur=var16.get()
            dirrec=var18.get()
            CIU=var17.get()

            algoritmo.consultasql2(sql,RUT=rt,NOMBRE=nom,APELLIDO=apll,CARRERA=carr,SEMESTRE=sem,CELULAR=celur,DIRRECION=dirrec,CIUDAD=CIU,ATRAZO=0)
            
        ventana3=Toplevel(root)
        ventana3.title("Información alumno")
        ventana3.geometry("500x300")
        ventana3.iconbitmap("recurso\dibujosdetiendasparaimprimir1_1_.ico")
        
        alumno=Label(ventana3,text="INGRESAR INFORMACION DEL ALUMNO").place(x=130,y=10)
        
        nombre = Label(ventana3,text="Nombre alumno: ").place(x=10,y=40)
        var13 = StringVar()
        texto1 = Entry(ventana3,textvariable=var13).place(x=110,y=43)
        
        apellido=Label(ventana3,text="apellido: ").place(x=10,y=80)
        valorapellido=StringVar()
        enapellido=Entry(ventana3,textvariable=valorapellido).place(x=110,y=83)
        
        semestre=Label(ventana3,text="semestre: ").place(x=250,y=120)
        valorsemestre=IntVar()
        sensemestre=Entry(ventana3,textvariable=valorsemestre).place(x=310,y=123)
        
        
        rut = Label(ventana3,text="Rut: ").place(x=250,y=40)
        var14 = IntVar()
        texto2 = Entry(ventana3,textvariable=var14).place(x=310,y=43)
        
        carrera= Label(ventana3,text="Carrera: ").place(x=10,y=120)
        var15 = StringVar()
        texto3 = Entry(ventana3,textvariable=var15).place(x=110,y=123)
        
        numero = Label(ventana3,text="Número de contacto: ").place(x=250,y=80)
        var16 = IntVar()
        texto4 = Entry(ventana3,textvariable=var16).place(x=370,y=83)
        
        ciudad = Label(ventana3,text="Ciudad: ").place(x=10,y=160)
        var17 = StringVar()
        texto5 = Entry(ventana3,textvariable=var17).place(x=110,y=163)
        
        Dirección= Label(ventana3,text="Dirección: ").place(x=10,y=200)
        var18 = StringVar()
        texto6 = Entry(ventana3,textvariable=var18).place(x=110,y=203)
        
        
        aceptar = Button(ventana3,text="Registrar",command=enviaralumno).place(x=410,y=250)
        
        ventana3.mainloop()


    def librobiloteca():
        def enviodeinformacion():
            def cantinv():
                try:
                    sql="SELECT CANTIDAD FROM inventario WHERE TITULOS=%s"
                    CANTI=algoritmo.consultasql(sql,TITULOS=TIT)
                    print(CANTI)
                    CANTI=int(CANTI[0])
                    NUEVA_CAN=CANTI+1
                except:
                    NUEVA_CAN=1
                return NUEVA_CAN
                
                
            sql1="INSERT INTO libros(AUTOR,TITULO,EDITORIALES,ISBM,GENERO,AÑO,id_libro) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            sql2="INSERT INTO inventario(TITULOS,AUTOR,EDITORIAL,CANTIDAD) VALUES(%s,%s,%s,%s)"
            TIT=var7.get()
            autors=var1.get()
            editorials=var2.get()
            años=var3.get()
            tipos=var4.get()
            id_lib=var5.get()
            isbns=var6.get()
            Cantidad=cantinv()
            algoritmo.consultasql2(sql1,AUTOR=autors,TITULO=TIT,EDITORIALES=editorials,ISBM=isbns,GENERO=tipos,AÑO=años,id_libro=id_lib)
            Cantidad=cantinv()
            algoritmo.consultasql2(sql2,TITULOS=TIT,AUTOR=autors,EDITORIAL=editorials,CANTIDAD=Cantidad)
            
            
        ventana = Toplevel(root)
        ventana.title("Libros Bilblioteca")
        ventana.geometry("500x300")
        ventana.iconbitmap("recurso\dibujosdetiendasparaimprimir1_1_.ico")
        
        
        #Ingreso de libros
        #En combobox agregar la lista de libros parte values
        libro = Label(ventana,text="INGRESAR INFORMACION DEL LIBRO").place(x=130,y=10)
        
        TITULO = Label(ventana,text="Nombre: ").place(x=10,y=40)
        var7 = StringVar()
        texto12 = Entry(ventana,textvariable=var7).place(x=100,y=43)
        
        autor = Label(ventana,text="Autor: ").place(x=250,y=120)
        var1 = StringVar()
        texto1 = Entry(ventana,textvariable=var1).place(x=310,y=123)
        
        editorial= Label(ventana,text="Editorial: ").place(x=10,y=80)
        var2 = StringVar()
        texto2 = Entry(ventana,textvariable=var2).place(x=100,y=83)
        
        año = Label(ventana,text="Fecha: ").place(x=250,y=40)
        var3 = StringVar()
        texto = Entry(ventana,textvariable=var3).place(x=310,y=43)
        
        tipo = Label(ventana,text="Tipo: ").place(x=10,y=120)
        var4 = StringVar()
        texto3 = Entry(ventana,textvariable=var4).place(x=100,y=123)
        
        id_libro = Label(ventana,text="ID Libro: ").place(x=250,y=80)
        var5 = StringVar()
        texto6 = Entry(ventana,textvariable=var5).place(x=310,y=83)
        
        isbn= Label(ventana,text="ISBN: ").place(x=10,y=160)
        var6 = StringVar()
        texto4 = Entry(ventana,textvariable=var6).place(x=100,y=163)
        
        
        
        aceptar = Button(ventana,text="Registrar",command=enviodeinformacion).place(x=10,y=250)
        
        ventana.mainloop()
    def solicitudinfo():
        def tablas():
            def solicitud():
                
                sql="SELECT * FORM "+nombre+" WHERE "+VARIABLE+"=%S"
                sql=str(sql)
                datos=algoritmo.consultasql(sql,variable=var1)
                claves=datos.keys()
                valores=datos.values()
                for i in range(len(claves)):
                    Text1.insert(i,0,claves[i]+": "+valores[i])
            nombre=combox.get()
            if nombre=="alumnos":
                lab2=Label(app2,text="rut: ").place(x=10,y=120)
                var1=StringVar()
                text=Entry(app,textvariable=var1).place(x=100,y=123)
                btn2=Button(app2,text="buscar",commnad=solicitud).place(x=90,y=160)
                VALIABLE="RUT"
            elif nombre=="prestamo":
                lab2=Label(app2,text="rut: ").place(x=10,y=120)
                var1=StringVar()
                text=Entry(app,textvariable=var1).place(x=100,y=123)
                btn2=Button(app2,text="buscar",commnad=solicitud).place(x=90,y=160)
            elif nombre=="libros":
                lab2=Label(app2,text="id_libro: ").place(x=10,y=120)
                var1=StringVar()
                text=Entry(app,textvariable=var1).place(x=100,y=123)
                btn2=Button(app2,text="buscar",commnad=solicitud).place(x=90,y=160)
                
            
        app2=Toplevel(root)
        app2.title("que informacion quiere solicitar")
        app2.geometry("800x500")
        app2.iconbitmap("recurso\dibujosdetiendasparaimprimir1_1_.ico")
        labw=Label(app2,text="clasificacion : ").place(x=10,y=40)
        Text1 = Text(app2)
        Text1.place(relx=0.3, rely=0.04, relheight=0.85, relwidth=0.67)
        Text1.configure(background="white")
        Text1.configure(font="TkTextFont")
        Text1.configure(foreground="black")
        Text1.configure(highlightbackground="#d9d9d9")
        Text1.configure(highlightcolor="black")
        Text1.configure(insertbackground="black")
        Text1.configure(selectbackground="#c4c4c4")
        Text1.configure(selectforeground="black")
        Text1.configure(undo="1")
        Text1.configure(width=404)
        Text1.configure(wrap=WORD)
        labela=Label(app2,text="elija una opcion").place(x=90,y=20)
        intems=algoritmo.consultasql("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE table_schema='administradorbibloteca'")
        print(intems)
        intems=list(intems)
        combox=ttk.Combobox(app2)
        combox.place(x=90,y=40)
        combox["values"]=intems
        botn1=Button(app2,text="aceptar",command=tablas).place(x=90,y=120)
        app2.mainloop()
        

class menuprincipal:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#d9d9d9' 

        top.geometry("713x450+650+150")
        top.title("menu principal")
        top.configure(background="#d9d9d9")
        top.iconbitmap("recurso\dibujosdetiendasparaimprimir1_1_.ico")

        

        self.Button1 = Button(top,command=diseño.regreso)
        self.Button1.place(relx=0.04, rely=0.07, height=33, width=126)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''entregar libro''')
        self.Button1.configure(width=126)

        self.Button2 = Button(top,command=diseño.infodealumno)
        self.Button2.place(relx=0.04, rely=0.18, height=33, width=126)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''registrar alumnos''')
        self.Button2.configure(width=126)

        self.Button3 = Button(top,command=diseño.librobiloteca)
        self.Button3.place(relx=0.04, rely=0.29, height=33, width=126)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''registrar libros''')
        self.Button3.configure(width=126)

        self.Button4 = Button(top,command=diseño.prestamo)
        self.Button4.place(relx=0.04, rely=0.4, height=33, width=126)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''prestamo''')
        self.Button4.configure(width=126)

        self.Button5 = Button(top,command=diseño.solicitudinfo)
        self.Button5.place(relx=0.04, rely=0.51, height=33, width=126)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''solicitar informacion''')
        self.Button5.configure(width=126)

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.29, rely=0.09, relheight=0.75, relwidth=0.67)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=473)

if __name__ == '__main__':
    vp_start_gui()