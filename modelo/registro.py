#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode

class registroClass:

        nombres = None
        apellidos = None
        contraseña = None
        correo = None
        celular = None

        def __init__(self,correo,nombres,apellidos,contraseña,celular):
                self.apellidos = apellidos
                self.nombres = nombres
                self.contraseña = contraseña
                self.correo = correo
                self.celular = celular

        def consultarUsuario(email):
                try:
                        cnx = mysql.connector.connect(user='michael',password='Camaleon_176',database='proyecto',host='127.0.0.1')
                        cursor = cnx.cursor()
                        cursor.execute("select * from usuario where correo_electronico='{}';".format(email))
                        data = cursor.fetchone()
                        if data == None:
                                return None
                        else:
                                u = usuarioClass(correo = data[0], nombres = data[2], apellidos = data[1], celular = data[3] ,contraseña = data[4])
                                return u
                        cursor.close()
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                print("Something is wrong with you user name or password")
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                print("Database does not exist")
                        else:
                                print(err)
                else:
                                cnx.close()


        def registrarUsuario(correo,nombres,apellidos,contraseña,celular):
                try:
                        cnx = mysql.connector.connect(user='michael',password='Camaleon_176',database='proyecto',host='127.0.0.1')
                        cursor = cnx.cursor()
                        cursor.execute("INSERT INTO usuario (correo_electronico,apellido,nombre,celular,contraseña) VALUES ('{}','{}','{}','{}','{}');".format(correo,apellidos,nombres,celular,contraseña))    
                        cnx.commit()
                        cursor.close()
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                print("Something is wrong with you user name or password")
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                print("Database does not exist")
                        else:
                                print(err)
                else:
                                cnx.close()
