# -*- coding: utf-8 -*-
import gui, wx
from licencia import *

class LicenciaDialog ( gui.LicenciaDialogBase):
  
           
    clave = clave()
    contador = 1

    def __init__( self, parent):
        gui.LicenciaDialogBase.__init__( self, parent )
        self.m_textCtrlClave.Disable()
        self.m_textCtrlClave.SetValue(self.clave[0:4] + "-" + self.clave[4:8] + "-" + self.clave[8:12])


    def m_OnButtonValidar( self, event ):
        if codigo(self.clave) == self.m_textCtrlCodigo.GetValue():
            generar()
            wx.MessageBox(u"Código de validación correcto\n\n\n\n".encode("latin-1"), "Error",wx.ICON_OK)                        
            self.Destroy()            
        else:      
            wx.MessageBox(u"Código de validación incorrecto\n\n\n\n".encode("latin-1"), "Error",wx.ICON_ERROR)            
            if self.contador > 2:
                self.Destroy()
                
            self.contador += 1

    def m_OnButtonCancelar( self, event ):
        self.Destroy()

