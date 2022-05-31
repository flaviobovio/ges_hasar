#!/usr/bin/env python  
#-*- coding: latin-1 -*-

import os
import gui
import wx
from xlrd import open_workbook
from BuscarProveedorDialog import BuscarProveedorDialog
from entidades import *
from datetime import date

class ImportarPanel ( gui.ImportarPanelBase):
    
    m_Libro = None
    m_Hoja = None
   
    def __init__( self, parent ):
        gui.ImportarPanelBase.__init__( self, parent )
        
        
    def m_OnButtonClickProveedor( self, event ):
        busDialog = BuscarProveedorDialog(self)         
        busDialog.ShowModal()
        self.m_textCtrlCuenta.SetValue(self.m_Proveedor.cuenta)
        self.m_textCtrlRazon.SetValue(self.m_Proveedor.razon)
        self.m_comboBoxCodigo.SetFocus()                                    
        
       
    def m_OnFileChangedLista( self, event ):
        self.m_Libro = open_workbook(self.m_filePickerLista.GetPath())
        self.m_comboBoxHoja.Clear()
        for h in self.m_Libro.sheets():
            self.m_comboBoxHoja.Append(h.name, h)


        if self.m_comboBoxHoja.GetCount() == 1:
            self.m_comboBoxHoja.Enable(False)
        else:
            self.m_comboBoxHoja.Enable(True)
            
        self.m_comboBoxHoja.SetSelection(0)        
        #self.m_Hoja =self.m_comboBoxHoja.GetClientData(self.m_comboBoxHoja.GetSelection())        
        self.LlenarVista()


    def m_OnComboBoxHoja( self, event ):
        self.LlenarVista()

    def m_OnButtonClickImportar( self, event ):
        
        c_codigo = ord(self.m_comboBoxCodigo.GetValue()) - 65
        c_descripcion = ord(self.m_comboBoxDescripcion.GetValue()) - 65
        c_precio = ord(self.m_comboBoxPrecio.GetValue()) - 65


        for row in range(self.m_Hoja.nrows):
            values = []
            for col in range(self.m_Hoja.ncols):
                values.append(self.m_Hoja.cell(row,col).value)           
        
            art = None
            #print values[c_descripcion].encode('latin-1'), values[c_precio], type(values[c_precio]).__name__ 
            
            if type(values[c_precio]).__name__ == 'float':  
                if self.m_comboBoxTipoPrecio.GetValue() == "Costo":
                    art = Articulo(values[c_codigo], "", 1, 1, values[c_descripcion], self.m_textCtrlCuenta.GetValue(), \
                        0, 0, 0, values[c_precio], 0, 21, 0, 0, 0, 0, date.today(), True)
                else:
                    art = Articulo(values[c_codigo], "", 1, 1, values[c_descripcion], self.m_textCtrlCuenta.GetValue(), \
                        0, 0, 0, 0, 0, 21, values[c_precio], 0, 0, 0, date.today(), True)
                    
                SESSION.add(art)
                SESSION.commit()
        
        
        
        


    def m_OnButtonClickCancelar( self, event ):
        res = wx.MessageBox("Elimina todos los artículos del proveedor", "Confirma ?", wx.YES_NO | wx.ICON_QUESTION)
        if res == wx.YES:
            arts = SESSION.query(Articulo).filter(Articulo.id_proveedor==self.m_textCtrlCuenta.GetValue()) 
            for art in arts: 
                SESSION.delete(art)
            SESSION.commit()


        
    def LlenarVista(self):
        self.m_Hoja = self.m_comboBoxHoja.GetClientData(self.m_comboBoxHoja.GetSelection())        
        lin = self.m_gridPreliminar.GetNumberRows()
        if lin > 0:
            self.m_gridPreliminar.DeleteRows(0, lin)

        for row in range(self.m_Hoja.nrows):
            self.m_gridPreliminar.AppendRows(1)                        
            for col in range(self.m_Hoja.ncols):
                if col < self.m_gridPreliminar.GetNumberCols():
                    val = self.m_Hoja.cell(row,col).value
                    if type(val).__name__ == 'float':
                        val = str(val)
                    else:
                        val = val.encode('latin-1')
                    self.m_gridPreliminar.SetCellValue(row, col, val) 

        self.m_gridPreliminar.AutoSizeColumns()
