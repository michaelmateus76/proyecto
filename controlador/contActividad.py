#!/usr/bin/python3

from modelo.actividad import actividadClass as mod
import json
import cgi

data=cgi.FieldStorage()

actividades = mod.obtenerActividades()
print('Content-Type: text/json')
print('')
print('[')
i=1
for actividad in actividades:
    print(json.dumps(actividad.__dict__))
    if i<len(actividades):
        i=i+1
        print(',')
print(']')