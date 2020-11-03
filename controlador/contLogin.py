#!/usr/bin/python3

from modelo.login import loginClass as mod
import json
import cgi

data = cgi.FieldStorage()

correo = data.getvalue('correo')
contraseña = data.getvalue('password')

usuario = mod.consultarUsuario(correo,contraseña)

print('Content-Type: text/json')
print('')
print('[')
if usuario == None:
    print("None")
else:
    print("exist")
print(']')