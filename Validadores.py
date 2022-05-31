import wx
class ValidarTexto(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)
    def Clone(self): # Required method for validator
        return ValidarTexto()
    def TransferToWindow(self):
        return True # Prevent wxDialog from complaining.
    def TransferFromWindow(self):
        return True # Prevent wxDialog from complaining.
     
    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
     
        if len(text) == 0:
            #self.parent.m_statusBar.SetStatusText("Se requiere ingresar texto")    
            #wx.MessageBox("Se requiere ingresar texto", "Error")
            textCtrl.SetBackgroundColour("grey")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(
            wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

class ValidarCuit(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)
    def Clone(self): # Required method for validator
        return ValidarCuit()
    def TransferToWindow(self):
        return True # Prevent wxDialog from complaining.
    def TransferFromWindow(self):
        return True # Prevent wxDialog from complaining.
     
    def Validate(self, win):
        textCtrl = self.GetWindow()
        cuit = textCtrl.GetValue()
        es_valido = False
        if len(cuit) in  [0,11]:
            if len(cuit) == 11:     
                base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
                # calculo el digito verificador:
                aux = 0
                for i in xrange(10):
                    aux += int(cuit[i]) * base[i]
                aux = 11 - (aux - (int(aux / 11) * 11))
                if aux == 11:
                    aux = 0
                if aux == 10:
                    aux = 9
                es_valido = (aux == int(cuit[10]))
            else:
                es_valido = True
        if es_valido:
            textCtrl.SetBackgroundColour(
            wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True
        else:
            #wx.MessageBox("El CUIT no es valido", "Error")
            textCtrl.SetBackgroundColour("grey")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False

class ValidarNatural(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)
    def Clone(self): # Required method for validator
        return ValidarNatural()
    def TransferToWindow(self):
        return True # Prevent wxDialog from complaining.
    def TransferFromWindow(self):
        return True # Prevent wxDialog from complaining.
     
    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()

        try:
            if eval(text) >= 0 :
                textCtrl.SetBackgroundColour(
                wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True
        except:
            pass
     
        #wx.MessageBox("Se requiere un valor mayor o igual a 0", "Error")
        textCtrl.SetBackgroundColour("grey")
        textCtrl.SetFocus()
        textCtrl.Refresh()
        return False

