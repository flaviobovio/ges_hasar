import gui
import wx
import BuscarClienteDialog
import BuscarArticuloDialog
import CerrarN_CreditoDialog
from datetime import *
from entidades import *
from wx import calendar

m_Cpbte = None

class N_CreditoPanel ( gui.CpbtePanelBase):
    
    m_Cliente = None
    m_Articulo = None
   
    def __init__( self, parent ):
        gui.CpbtePanelBase.__init__( self, parent )
        
       
        self.m_textCtrlNumero.Disable()
        self.m_staticTextRemito.SetLabel("Cpbte Origen")
        #self.m_textCtrlRemito.Disable()        
        
        for r in range(self.m_gridDetalle.GetNumberRows()):
            self.m_gridDetalle.SetReadOnly(r, 1, True)       
        self.m_gridDetalle.SetColFormatFloat(2, 6, 2) 
        self.m_gridDetalle.SetColFormatFloat(3, 6, 2)         
        self.m_gridDetalle.SetColFormatFloat(4, 6, 2)   
        self.m_textCtrlCuenta.SetFocus()

    def m_OnGridCellChange( self, event ):
        row = event.GetRow()
        col = event.GetCol()
        cel = self.m_gridDetalle.GetCellValue(row,col)

        if col == 0:
            self.m_Articulo = SESSION.query(Articulo).filter(Articulo.codigo==cel).first()
            if self.m_Articulo != None:
                self.llenarLinea()
            else:
                busDialog = BuscarArticuloDialog.BuscarArticuloDialog(self) 
                busDialog.ShowModal()
                self.llenarLinea()

        elif col == 2:
            if eval(cel) > 0:
                pre = self.m_gridDetalle.GetCellValue(row,col+1)
                tot = str(eval(cel)*eval(pre))
                self.m_gridDetalle.SetCellValue(row, 4, tot)                 
        elif col == 3:
            if eval(cel) > 0:
                can = self.m_gridDetalle.GetCellValue(row,col-1)
                tot = str(eval(cel)*eval(can))
                self.m_gridDetalle.SetCellValue(row, 4, tot)                 
                
            
            
    def m_OnKeyDownDetalle( self, event ):       
        key = event.GetKeyCode() 
        if key == 13 or key == 370:  #Enter
            self.m_gridDetalle.DisableCellEditControl()
            row = self.m_gridDetalle.GetGridCursorRow()
            col = self.m_gridDetalle.GetGridCursorCol()
            if col == 0 and self.m_gridDetalle.GetCellValue(row, col) == "":
                busDialog = BuscarArticuloDialog.BuscarArticuloDialog(self) 
                busDialog.ShowModal()
                self.llenarLinea()
            if col < 3:
                self.m_gridDetalle.MoveCursorRight(False)
            else:
                self.m_gridDetalle.SetGridCursor( min(row+1, 9), 0) 
        elif key == 9:  #Tab
            self.m_bpButtonOk.SetFocus()        
        elif key == 127:  #Del
            row = self.m_gridDetalle.GetGridCursorRow()        
            self.m_gridDetalle.DeleteRows(row, 1)            
            self.m_gridDetalle.AppendRows(1)                        
        else:
            event.Skip()

    def m_OnKeyDownCuenta( self, event ):       
        key = event.GetKeyCode() 
        if key == 13 or key == 370:  #Enter
            if self.m_textCtrlCuenta.GetValue() == "":
                busDialog = BuscarClienteDialog.BuscarClienteDialog(self) 
                busDialog.ShowModal()
            else:
                self.m_Cliente = SESSION.query(Cliente).filter(Cliente.cuenta==self.m_textCtrlCuenta.GetValue()).first()
        
            if self.m_Cliente != None:
                self.m_textCtrlCuenta.SetValue(self.m_Cliente.cuenta)
                self.m_textCtrlRazon.SetValue(self.m_Cliente.razon)
                self.m_staticTextCpbte.SetLabel("NOTA DE CREDITO " + self.m_Cliente.iva.comprobante)
                self.m_textCtrlRazon.SetFocus()         
        else:
            event.Skip()

    def m_OnSetFocusRazon( self, event ):
        if self.m_textCtrlRazon.GetValue() != "":
            self.m_gridDetalle.SetFocus()
        else:
            event.Skip()            


    def m_OnButtonClickCliente( self, event ):
        busDialog = BuscarClienteDialog.BuscarClienteDialog(self) 
        busDialog.ShowModal()
        self.m_textCtrlCuenta.SetValue(self.m_Cliente.cuenta)
        self.m_textCtrlRazon.SetValue(self.m_Cliente.razon)
        self.m_staticTextCpbte.SetLabel("NOTA DE CREDITO " + self.m_Cliente.iva.comprobante)        
        self.m_textCtrlRazon.SetFocus()                                    
        
    def m_OnButtonClickOk( self, event ):
        self.m_Cpbte = Notacr()
        self.m_Cpbte.cliente = self.m_Cliente
        self.m_Cpbte.f_cpbte = calendar._wxdate2pydate(self.m_datePickerFecha.GetValue())
        
        
        self.m_Cpbte.razon = self.m_textCtrlRazon.GetValue()
        self.m_Cpbte.n_remito = self.m_textCtrlRemito.GetValue()        
        self.m_Cpbte.t_cpbte = self.m_Cliente.iva.comprobante
        self.m_Cpbte.i_bruto = 0
        self.m_Cpbte.i_descuento = 0
        self.m_Cpbte.i_iva1 = 0
        self.m_Cpbte.i_iva2 = 0
        self.m_Cpbte.i_iva3 = 0        
        self.m_Cpbte.i_neto = 0
        
        
        for row in range(self.m_gridDetalle.GetNumberRows()):
            if len(self.m_gridDetalle.GetCellValue(row, 0)) > 0:
                cod = self.m_gridDetalle.GetCellValue(row, 0)
                self.m_Articulo = SESSION.query(Articulo).filter(Articulo.codigo==cod).first()
                d_cpbt = d_Notacr (self.m_Cpbte.id,\
                    self.m_Articulo.id,\
                    eval(self.m_gridDetalle.GetCellValue(row, 2)),\
                    self.m_Articulo.t_iva,\
                    eval(self.m_gridDetalle.GetCellValue(row, 3)) )
                d_cpbt.articulo = self.m_Articulo    
                self.m_Cpbte.d_notacr.append(d_cpbt)                       
                imp = eval(self.m_gridDetalle.GetCellValue(row, 4))
                self.m_Cpbte.i_bruto += round(imp / (1 + self.m_Articulo.t_iva / 100), 2)
                if self.m_Articulo.t_iva == 10.5:
                    self.m_Cpbte.i_iva1 += round (imp - (imp / 1.105), 2)
                elif self.m_Articulo.t_iva == 21:
                    self.m_Cpbte.i_iva2 += round(imp - (imp / 1.21), 2)
                
                self.m_Cpbte.i_neto += imp
                
                                    
        cerrarDialog = CerrarN_CreditoDialog.CerrarN_CreditoDialog(self)
        cerrarDialog.ShowModal()
        if self.m_Cpbte.estado != None:
            self.vaciarDatos()
        

    
    
    def m_OnButtonClickGuardar( self, event ):
        #event.Skip()

        a = self.m_datePickerFecha.GetValue().Format('%Y/%m/%d')
        print a

                       
    def llenarLinea(self):
        if self.m_Articulo != None:
            row = self.m_gridDetalle.GetGridCursorRow()
            self.m_gridDetalle.SetCellValue(row, 0, self.m_Articulo.codigo)                    
            self.m_gridDetalle.SetCellValue(row, 1, self.m_Articulo.descripcion)        
            self.m_gridDetalle.SetCellValue(row, 2, "1")                    
            self.m_gridDetalle.SetCellValue(row, 3, str(self.m_Articulo.p_venta))        
            self.m_gridDetalle.SetCellValue(row, 4, str(self.m_Articulo.p_venta))   
            
    def vaciarDatos(self):
        self.m_Cpbte = None
        self.m_Cliente = None
        self.m_Articulo = None

        self.m_textCtrlCuenta.SetValue("")
        self.m_textCtrlRazon.SetValue("")
        #self.m_datePickerFecha.SetValue()
        self.m_textCtrlRemito.SetValue("")        
              
        self.m_gridDetalle.DeleteRows(0,10)            
        self.m_gridDetalle.AppendRows(10)                        
        

        

