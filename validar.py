# -*- coding: utf-8 -*-
import os, random
from datetime import date
from Crypto.Cipher import AES
from licencia import *


clave = raw_input("Ingrese Clave a validar (sin guiones):\n\n").upper()

#f = fecha_clave(clave) 


try:
    if fecha_clave(clave) == date.today():
        print "\nEl Codigo es:\n"
        print codigo (clave)
    else:
        print "\nClave no valida!!!"                
except:      
    print "\nClave no valida, probable error en formato !!!"        
