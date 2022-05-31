# -*- coding: utf-8 -*-
import wx, os, time, random
from datetime import datetime, timedelta
from Crypto.Cipher import AES
key = '@#!C30711494592f'
cuit = "23242984919"
IV = 16 * '\x00'           # Initialization vector: discussed later
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

def chequear():
    os.system("del respuesta.ans")
    os.system("wspooler -p1 -c Y") #fec
    try:
        f = open("respuesta.ans")
        respuesta = f.readlines()
        f.close()
        ffis = datetime.strptime(respuesta[0][34:40], '%y%m%d')
    except IOError:
        wx.MessageBox((u"Error de comunicación con la impresora").encode("latin-1"), "Impresora Fiscal", wx.OK | wx.ICON_WARNING)        
        exit()


    os.system("del respuesta.ans")
    os.system("wspooler -p1 -c s") #datos 
    try:
        f = open("respuesta.ans")
        respuesta = f.readlines()
        f.close()
        cfis = respuesta[0][34:45] 
    except IOError:
        wx.MessageBox((u"Error de comunicación con la impresora").encode("latin-1"), "Impresora Fiscal", wx.OK | wx.ICON_WARNING)        
        exit()        

    
    try:
        f = open("licencia.lic", "r")
        t = f.read()
        f.close()
        ciphertext = encryptor.decrypt(t) 
        carc  = ciphertext[0:11] 
        farc = datetime.strptime(ciphertext[11:17], '%d%m%y')


        if cfis == carc:
            if ffis <= farc:
                restan = farc - ffis
                if restan < timedelta(days=5):
                    wx.MessageBox((u"Restan " + str(restan.days) + u" días para renovar la licencia").encode("latin-1"), "Licencia", wx.OK | wx.ICON_WARNING)
                return True
            
    except IOError:       
        wx.MessageBox((u"Error al leer archivo de licencia").encode("latin-1"), "Licencia", wx.OK | wx.ICON_WARNING)        

    return False

            

    
            
        

def clave():
    fecha = (time.strftime("%d%m%y"))
    ale = str(random.choice(range(99999, 999999))).zfill(6)
    clave = ""
    
    for i in range(0,6):
        clave = clave + chr(ord(fecha[i]) + int(ale[i])+17) +  chr(ord(ale[i])+ 33)
    return clave

def codigo(clave):
    codigo = int(hash(clave+key))
    return str(abs(codigo))
    
def fecha_clave(clave):
    fecha = ""
    for i in range(0,6):
        a = chr(ord(clave[(i*2)+1])-33)
        b = ord(clave[(i*2)])
        fecha += chr(b-int(a)-17)
    fecha  = datetime.strptime(fecha, "%d%m%y").date()
    return fecha
    

def generar():  
    fecha = (datetime.now()+timedelta(days=61)).strftime("%d%m%y")
    text = (cuit + fecha).ljust(32)
    print text
    ciphertext = encryptor.encrypt(text)    
    f = open("licencia.lic", "w")
    f.write(ciphertext)
    f.close()

    




