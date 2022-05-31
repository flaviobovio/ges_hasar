import gui
import wx
from entidades import *


class BuscarProveedorDialog (gui.BuscarDialog):
    

    
    def __init__( self, parent):
        gui.BuscarDialog.__init__( self, parent)
        self.m_comboBoxCampos.AppendItems(["Razon", "Cuenta", "CUIT", "Direccion", "Localidad"])
        self.m_comboBoxCampos.SetSelection(0)
        self.m_textCtrlCadena.SetFocus()
        self.SetTitle("Buscar Proveedor")
        self.m_staticTextEncabezado.SetLabel(
        "Cuenta          Nombre o Razon Social                    Cuit              Direccion                       Localidad")
        

    def m_OnButtonClickBuscar( self, event ):
        self.buscar()
        
    def m_OnKeyDownResultados( self, event ):
        key = event.GetKeyCode()
        if key == 13 or key == 370:
            self.Parent.m_Proveedor = self.m_listBoxResultados.GetClientData(self.m_listBoxResultados.GetSelection())
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
        self.Parent.m_Proveedor = self.m_listBoxResultados.GetClientData(self.m_listBoxResultados.GetSelection())
        self.Destroy()
        
        
    def buscar(self):
        self.m_listBoxResultados.Clear()
        fil = "Proveedor." + self.m_comboBoxCampos.GetValue().lower()+ ".like('%" + self.m_textCtrlCadena.GetValue().strip() + "%')"
        for cli in SESSION.query(Proveedor).filter(eval(fil)).all(): 
            self.m_listBoxResultados.Append(cli.cuenta.ljust(10)+" "+cli.razon.ljust(30)+" "+\
            str(cli.cuit).ljust(11)+" "+cli.direccion.ljust(20)+" "+cli.localidad.ljust(20), cli)
        self.m_listBoxResultados.SetSelection(0)     
        self.m_listBoxResultados.SetFocus()
        
    




