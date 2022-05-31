import gui
import wx
from entidades import *


class BuscarClienteDialog (gui.BuscarDialog):
    

    
    def __init__( self, parent):
        gui.BuscarDialog.__init__( self, parent)
        self.m_comboBoxCampos.AppendItems(["Razon", "Cuenta", "CUIT", "Direccion", "Localidad"])
        self.m_comboBoxCampos.SetSelection(0)
        self.m_textCtrlCadena.SetFocus()
        self.SetTitle("Buscar Cliente")

    def m_OnButtonClickBuscar( self, event ):
        self.buscar()
        
    def m_OnKeyDownResultados( self, event ):
        key = event.GetKeyCode()
        if key == 13 or key == 370:
            self.Parent.m_Cliente = self.m_listBoxResultados.GetClientData(self.m_listBoxResultados.GetSelection())
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
        self.Parent.m_Cliente = self.m_listBoxResultados.GetClientData(self.m_listBoxResultados.GetSelection())
        self.Destroy()
        
        
    def buscar(self):
        self.m_gridResultados.ClearGrid()
        fil = "Cliente." + self.m_comboBoxCampos.GetValue().lower()+ ".like('%" + self.m_textCtrlCadena.GetValue().strip() + "%')"
        data = []
        for cli in SESSION.query(Cliente).filter(eval(fil)).all(): 
            data.append([cli.cuenta, cli.razon, cli.cuit, cli.direccion])
        print data
        
        self.m_gridResultados.AutoSizeColumns(True)
        tb = GenericTable(data)
        self.m_gridResultados.SetTable(tb, True)
        return


        
        
        for cli in SESSION.query(Cliente).filter(eval(fil)).all(): 
        
            self.m_GridResultados.Append(cli.cuenta.ljust(10)+" "+cli.razon.ljust(50)+" "+\
            str(cli.cuit).ljust(11)+" "+cli.direccion+" "+cli.localidad, cli)
        #self.m_listBoxResultados.SetSelection(0)     
        self.m_gridResultados.SetFocus()
        
        
        
class GenericTable(wx.grid.PyGridTableBase):
    def __init__(self, data, rowLabels=None, colLabels=None):
        wx.grid.PyGridTableBase.__init__(self)
        self.data = data
        self.rowLabels = rowLabels
        self.colLabels = colLabels
        
    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def GetColLabelValue(self, col):
        if self.colLabels:
            return self.colLabels[col]
        
    def GetRowLabelValue(self, row):
        if self.rowLabels:
            return self.rowLabels[row]
        
    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        pass         

        
        
        
        
        
        
    

