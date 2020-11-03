#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode

class actividadClass:

        nombre_act = None
        nombre_mat = None
        descripcion = None
        fecha = None
        rango = None

        def __init__(self,nombre_act,nombre_mat,descripcion,fecha,rango):
                self.nombre_act = nombre_act
                self.nombre_mat = nombre_mat
                self.descripcion = descripcion
                self.fecha = fecha
                self.rango = rango

        def obtenerActividades():
                try:
                        cnx = mysql.connector.connect(user='michael',password='Camaleon_176',database='proyecto',host='127.0.0.1')
                        cursor = cnx.cursor()
                        cursor.execute("select * from actividad;")
                        data = cursor.fetchall()
                        if data == None:
                                return None
                        else:
                                actividades = []
                                for row in data:
                                    actividad = actividadClass(nombre_act = row[0], nombre_mat = row[1], descripcion = row[2], fecha = row[3] ,rango = row[4])
                                    actividades.append(actividad)
                                return actividades
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
