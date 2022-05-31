import gui
import wx
from BuscarClienteDialog import BuscarClienteDialog
from entidades import *
from datetime import datetime
from Validadores import *

import  wx.grid as gridlib

class ReciboPanel ( gui.ReciboPanelBase):
    
    m_Cliente = None
   
    def __init__( self, parent ):
        gui.ReciboPanelBase.__init__( self, parent )
        self.m_textCtrlNumero.Disable()
        
        
        

        
        for r in range(self.m_gridDetalle.GetNumberRows()):
            self.m_gridDetalle.SetReadOnly(r, 0, True)       
            
            
            
            
        self.m_gridDetalle.SetColFormatFloat(3, 6, 0) 
        self.m_gridDetalle.SetColFormatFloat(5, 6, 2)   
        self.m_textCtrlCuenta.SetFocus()
        
        
    
           
            

    def m_OnGridCellChange( self, event ):
        row = event.GetRow()
        col = event.GetCol()
        cel = self.m_gridDetalle.GetCellValue(row,col)

        if col == 0:
            pass
        elif col == 1:
            #if cel != "":
            #    try:
            #        print datetime.strptime(cel, "%d/%m/%y")
            #    except ValueError:
            #        wx.MessageBox("Ingrese una fecha en formato dd/mm/aa",style=wx.ICON_ERROR)
            #        self.m_gridDetalle.EnableCellEditControl()
                    #self.m_gridDetalle.SetGridCursor( row, col) 
            pass

        elif col == 3:
            pass            
        elif col == 5:
            if self.m_gridDetalle.GetCellValue(row, 1) != "":
                self.m_gridDetalle.SetCellValue(row, 0, "Cheque/Tarjeta")
            else: 
                if eval(cel) > 0:
                    self.m_gridDetalle.SetCellValue(row, 0, "Efectivo")
                elif eval(cel) < 0:
                    self.m_gridDetalle.SetCellValue(row, 0, "Vuelto")
                
                
                
            
            
    def m_OnKeyDownDetalle( self, event ):       
        key = event.GetKeyCode() 
        if key == 13 or key == 370:  #Enter
            self.m_gridDetalle.DisableCellEditControl()
            row = self.m_gridDetalle.GetGridCursorRow()
            col = self.m_gridDetalle.GetGridCursorCol()
            cel = self.m_gridDetalle.GetCellValue(row, col)
            if col == 1:
                if cel == "":
                    self.m_gridDetalle.SetGridCursor(row, 5)
                else:
                    try:
                        datetime.strptime(cel, "%d/%m/%y")
                    except ValueError:
                        wx.MessageBox("Ingrese una fecha en formato dd/mm/aa",style=wx.ICON_ERROR)
                        self.m_gridDetalle.SetGridCursor( row, 0)                         
                        #self.m_gridDetalle.EnableCellEditControl()
                
            if col < 5:
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
                busDialog = BuscarClienteDialog(self) 
                busDialog.ShowModal()
            else:
                self.m_Cliente = SESSION.query(Cliente).filter(Cliente.cuenta==self.m_textCtrlCuenta.GetValue()).first()
        
            if self.m_Cliente != None:
                self.m_textCtrlCuenta.SetValue(self.m_Cliente.cuenta)
                self.m_textCtrlRazon.SetValue(self.m_Cliente.razon)
                self.m_textCtrlRazon.SetFocus()         
        else:
            event.Skip()

    def m_OnSetFocusRazon( self, event ):
        if self.m_textCtrlRazon.GetValue() != "":
            self.m_gridDetalle.SetFocus()
        else:
            event.Skip()            


    def m_OnButtonClickCliente( self, event ):
        busDialog = BuscarClienteDialog(self) 
        busDialog.ShowModal()
        self.m_textCtrlCuenta.SetValue(self.m_Cliente.cuenta)
        self.m_textCtrlRazon.SetValue(self.m_Cliente.razon)
        self.m_textCtrlRazon.SetFocus()                                    
        
    def m_OnButtonClickImprimir( self, event ):
        rec = Recibo()
        rec.id = 0
        rec.cliente = self.m_Cliente
        rec.razon = self.m_textCtrlRazon.GetValue()
        rec.i_neto = 0
        
        print rec
        print rec.cliente

        

        
        for row in range(self.m_gridDetalle.GetNumberRows()):
            if len(self.m_gridDetalle.GetCellValue(row, 0)) > 0:
                cod = self.m_gridDetalle.GetCellValue(row, 0)
                self.m_Articulo = SESSION.query(Articulo).filter(Articulo.codigo==cod).first()
                d_fac = d_Factura (fac.id,\
                    self.m_Articulo.id,\
                    eval(self.m_gridDetalle.GetCellValue(row, 2)),\
                    self.m_Articulo.t_iva,\
                    eval(self.m_gridDetalle.GetCellValue(row, 3)) )
                d_fac.articulo = self.m_Articulo    
                fac.d_factura.append(d_fac)                       
                imp = eval(self.m_gridDetalle.GetCellValue(row, 4))
                fac.i_bruto += round(imp / (1 + self.m_Articulo.t_iva / 100), 2)
                if self.m_Articulo.t_iva == 10.5:
                    fac.i_iva1 += round (imp - (imp / 1.105), 2)
                elif self.m_Articulo.t_iva == 21:
                    fac.i_iva2 += round(imp - (imp / 1.21), 2)
                
                fac.i_neto += imp
                    
        cerrarDialog = CerrarFacturaDialog.CerrarFacturaDialog(self, fac)
        cerrarDialog.ShowModal()

    def m_OnButtonClickGuardar( self, event ):
        event.Skip()
    
    def m_OnButtonClickCancelar( self, event ):
        event.Skip()

                       
    def llenarLinea(self):
        if self.m_Articulo != None:
            row = self.m_gridDetalle.GetGridCursorRow()
            self.m_gridDetalle.SetCellValue(row, 0, self.m_Articulo.codigo)                    
            self.m_gridDetalle.SetCellValue(row, 1, self.m_Articulo.descripcion)        
            self.m_gridDetalle.SetCellValue(row, 2, "1")                    
            self.m_gridDetalle.SetCellValue(row, 3, str(self.m_Articulo.p_venta))        
            self.m_gridDetalle.SetCellValue(row, 4, str(self.m_Articulo.p_venta))   


class CustomDataTable(gridlib.PyGridTableBase):
    def __init__(self, log):
        gridlib.PyGridTableBase.__init__(self)
        self.log = log

        self.colLabels = ['', 'Fecha', 'Banco', 'Priority', 'Platform',
                          'Opened?', 'Fixed?', 'Tested?', 'TestFloat']

        self.dataTypes = [gridlib.GRID_VALUE_STRING,
                          gridlib.GRID_VALUE_STRING,
                          gridlib.GRID_VALUE_CHOICE,
                          gridlib.GRID_VALUE_NUMBER,
                          gridlib.GRID_VALUE_CHOICE + ':all,MSW,GTK,other',
                          gridlib.GRID_VALUE_FLOAT + ':6,2',
                          ]





    #--------------------------------------------------
    # required methods for the wxPyGridTableBase interface

    def GetNumberRows(self):
        return len(self.data) + 1

    def GetNumberCols(self):
        return len(self.data[0])

    def IsEmptyCell(self, row, col):
        try:
            return not self.data[row][col]
        except IndexError:
            return True

    # Get/Set values in the table.  The Python version of these
    # methods can handle any data-type, (as long as the Editor and
    # Renderer understands the type too,) not just strings as in the
    # C++ version.
    def GetValue(self, row, col):
        try:
            return self.data[row][col]
        except IndexError:
            return ''

    def SetValue(self, row, col, value):
        def innerSetValue(row, col, value):
            try:
                self.data[row][col] = value
            except IndexError:
                # add a new row
                self.data.append([''] * self.GetNumberCols())
                innerSetValue(row, col, value)

                # tell the grid we've added a row
                msg = gridlib.GridTableMessage(self,            # The table
                        gridlib.GRIDTABLE_NOTIFY_ROWS_APPENDED, # what we did to it
                        1                                       # how many
                        )

                self.GetView().ProcessTableMessage(msg)
        innerSetValue(row, col, value) 

    #--------------------------------------------------
    # Some optional methods

    # Called when the grid needs to display labels
    def GetColLabelValue(self, col):
        return self.colLabels[col]

    # Called to determine the kind of editor/renderer to use by
    # default, doesn't necessarily have to be the same type used
    # natively by the editor/renderer if they know how to convert.
    def GetTypeName(self, row, col):
        return self.dataTypes[col]

    # Called to determine how the data can be fetched and stored by the
    # editor and renderer.  This allows you to enforce some type-safety
    # in the grid.
    def CanGetValueAs(self, row, col, typeName):
        colType = self.dataTypes[col].split(':')[0]
        if typeName == colType:
            return True
        else:
            return False

    def CanSetValueAs(self, row, col, typeName):
        return self.CanGetValueAs(row, col, typeName)




    

