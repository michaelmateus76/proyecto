#!/usr/bin/python3

from modelo.registro import registroClass as mod
import json
import cgi

data = cgi.FieldStorage()

correo = data.getvalue('correo')
contraseña = data.getvalue('password')
nombres = data.getvalue('nombres')
apellidos = data.getvalue('apellidos')
celular = data.getvalue('cel')

usuario = mod.consultarUsuario(correo)

if usuario == None:
    mod.registrarUsuario(correo,nombres,apellidos,contraseña,celular)

print('Content-Type: text/json')
print('')
print('[')
if usuario == None:
    print("None")
else:
    print("exist")
print(']')