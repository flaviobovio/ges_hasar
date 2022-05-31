import gui
import wx
from entidades import *


class BuscarArticuloDialog (gui.BuscarDialog):
       
    def __init__( self, parent):
        gui.BuscarDialog.__init__( self, parent)
        self.m_comboBoxCampos.AppendItems(["Descripcion", "Codigo"])
        self.m_comboBoxCampos.SetSelection(0)
        self.m_textCtrlCadena.SetFocus()
        self.SetTitle("Buscar Articulo")
        self.m_staticTextEncabezado.SetLabel(
        "             Codigo          Descripcion                                                           ")

    def m_OnButtonClickBuscar( self, event ):
        self.buscar()
        
    def m_OnKeyDownResultados( self, event ):
        key = event.GetKeyCode()
        if key == 13 or key == 370:
            self.Parent.m_Articulo = self.m_listBoxResultados.GetClientData(self.m_listBoxResultados.GetSelection())
            self.Destroy()
        elif key == 27:
            self.Destroy()            
        else:
            event.Skip()
            
    def m_OnKeyDownCadena( self, event ):
        key = event.GetKeyCode()
        if key == 13 or key == 370:
            self.buscar()
        elif key == 27:
            self.Destroy()            
        else:
            event.Skip()
                
               
    def m_OnLeftClickResultados( self, event ):
        self.Parent.m_Articulo = self.m_listBoxResultados.GetClientData(self.m_listBoxResultados.GetSelection())
        self.Destroy()
        

    def buscar(self):
        self.m_listBoxResultados.Clear()
        fil = "Articulo." + self.m_comboBoxCampos.GetValue().lower()+ ".like('%" + self.m_textCtrlCadena.GetValue().strip() + "%')"
        for art in SESSION.query(Articulo).filter(eval(fil)).all(): 
            #self.m_listBoxResultados.Append(art.codigo.rjust(13) + "  " + 
            #    art.descripcion.ljust(35) + " " + str("%.2f"%art.stock).rjust(8) + " " + str("%.2f"%art.p_venta).rjust(10), art) 
            self.m_listBoxResultados.Append(art.codigo.rjust(13) + "  " + art.descripcion.ljust(35) , art) 
            
        self.m_listBoxResultados.SetSelection(0)     
        self.m_listBoxResultados.SetFocus()
        
    




