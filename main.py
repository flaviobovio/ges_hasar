import wx
import locale
from MainFrame import MainFrame
from licencia import *
import LicenciaDialog



class Gestion(wx.App):
   
    def OnInit(self):
        if chequear():  
            self.m_frame = MainFrame(None)
            self.m_frame.Show()
            self.SetTopWindow(self.m_frame)
        else:
            self.licDialog = LicenciaDialog.LicenciaDialog (None)
            self.licDialog.ShowModal()        


        return True

app = Gestion(0)
app.MainLoop()
