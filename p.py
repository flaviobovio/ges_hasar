# -*- coding: utf-8 -*-
import os, time, random
from Crypto.Cipher import AES
from licencia import *



generar()
print "11111"

f = open("licencia.lic", "r")
t = f.read()
#ljust(32)
f.close()
print t
print "----"



IV = 16 * '\x00'           # Initialization vector: discussed later
mode = AES.MODE_CBC
key = '@#!C30711494592f'
encryptor = AES.new(key, mode, IV=IV)
ciphertext = encryptor.decrypt(t) 
print ciphertext[11:17] 
print ciphertext[0:11] 

exit()






cuit = "23242984919"
fecha = "130814"
key = '@#!C30711494592f'
text = (cuit + fecha).ljust(32)
ciphertext = encryptor.encrypt(text)    
f = open("licencia.lic", "w")
f.write(ciphertext)
f.close()

exit()





exit()



cc = clave()
kk = fecha_clave(cc)
print cc
print kk

f = open("respuesta.ans")
respuesta = f.readlines()
f.close()


fecha = (time.strftime("%d%m%y"))
ale = str(random.choice(range(99999, 999999)))


codigo = ""
for i in range(0,6):
    codigo = codigo + chr(ord(fecha[i]) + int(ale[i])+17) +  chr(ord(ale[i])+ 33)


print codigo




key = '@#!C30711494592f'

print hash(codigo+key)


IV = 16 * '\x00'           # Initialization vector: discussed later
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)
text = '2324298491904042011 ' + "flavio bovio"
ciphertext = encryptor.encrypt(text)


print ciphertext



