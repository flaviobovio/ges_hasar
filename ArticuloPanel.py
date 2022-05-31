import wx
import gui
from entidades import *
from Validadores import *
from Funciones import *
from datetime import date
from BuscarArticuloDialog import BuscarArticuloDialog

class ArticuloPanel (gui.ArticuloPanelBase ):
    
    m_Articulo = None
    
    def __init__( self, parent ):
        gui.ArticuloPanelBase.__init__( self, parent )        
        
        
        for row in SESSION.query(Rubro):           
            self.m_comboBoxRubro.Append(row.rubro, row)           
        for row in SESSION.query(Unidad):
            self.m_comboBoxUnidad.Append(row.unidad, row)   
            
        self.HabilitarControles(False) 


    def LlenarControles (self):       
        self.m_textCtrlCodigo.SetValue(self.m_Articulo.codigo)
        self.m_textCtrlCodigoaux.SetValue(self.m_Articulo.codigoaux)        
        self.m_textCtrlDescripcion.SetValue(self.m_Articulo.descripcion)         
        self.m_textCtrlCuenta.SetValue(str(self.m_Articulo.id_proveedor))
        self.m_comboBoxRubro.SetStringSelection(self.m_Articulo.rubro.rubro)        
        self.m_comboBoxUnidad.SetStringSelection(self.m_Articulo.unidad.unidad)                
        self.m_textCtrlStock.SetValue(str(self.m_Articulo.stock))
        self.m_textCtrlStockMinimo.SetValue(str(self.m_Articulo.stockminimo))
        self.m_textCtrlRedondeo.SetValue(str(self.m_Articulo.redondeo))
        self.m_textCtrlP_Costo.SetValue(str(self.m_Articulo.p_costo))
        self.m_textCtrlMargen.SetValue(str(self.m_Articulo.margen))
        self.m_textCtrlT_Iva.SetValue(str(self.m_Articulo.t_iva))
        self.m_textCtrlP_Venta.SetValue(str(self.m_Articulo.p_venta))
        self.m_textCtrlReca_Desc1.SetValue(str(self.m_Articulo.reca_desc1))
        self.m_textCtrlReca_Desc2.SetValue(str(self.m_Articulo.reca_desc2))
        self.m_textCtrlReca_Desc3.SetValue(str(self.m_Articulo.reca_desc3))           
        self.m_textCtrlModificado.SetValue(str(self.m_Articulo.modificado))
        self.m_checkBoxActivo.SetValue(self.m_Articulo.activo)         

    def VaciarDatos (self):      
        self.m_Articulo = Articulo ("","",0,0,"",0,0,0,0,0,0,0,0,0,0,0,date.today(), True)
        self.m_Articulo.rubro = SESSION.query(Rubro).first()
        self.m_Articulo.unidad = SESSION.query(Unidad).first()
        self.LlenarControles()
        
    def HabilitarControles(self, acti): # True Activar, False Desactivar
        for ctrl in self.GetChildren():
            if ctrl.GetName() != "button":
                ctrl.Enable(acti)
            else:
                ctrl.Enable(not acti)
        self.m_bpButtonDeshacer.Enable(acti)
        self.m_bpButtonGuardar.Enable(acti)       
        self.m_textCtrlCodigo.SetFocus()
        
        
 

    def m_OnButtonClickPrimero( self, event ):  
        self.m_Articulo = SESSION.query(Articulo).order_by(Articulo.codigo).first()
        self.LlenarControles()
    def m_OnButtonClickAnterior( self, event ):
        cod = self.m_textCtrlCodigo.GetValue()
        self.m_Articulo = SESSION.query(Articulo).order_by(desc(Articulo.codigo)).filter(Articulo.codigo < cod).first()

        if self.m_Articulo != None:
            self.LlenarControles()
    
    def m_OnButtonClickSiguiente( self, event ):
        cod = self.m_textCtrlCodigo.GetValue()
        self.m_Articulo = SESSION.query(Articulo).order_by(Articulo.codigo).filter(Articulo.codigo > cod).first()
       
        if self.m_Articulo != None:
            self.LlenarControles()
    
    def m_OnButtonClickUltimo( self, event ):
        self.m_Articulo = SESSION.query(Articulo).order_by(desc(Articulo.codigo)).first()
        self.LlenarControles()

    def m_OnButtonClickAgregar( self, event ):
        self.VaciarDatos()
        self.m_comboBoxRubro.SetSelection(0)
        self.m_comboBoxUnidad.SetSelection(0)
        self.HabilitarControles(True)
    
    def m_OnButtonClickEditar( self, event ):
        if self.m_Articulo != None:
            self.HabilitarControles(True)
    
    def m_OnButtonClickBorrar( self, event ):
        DATABASE.echo = True
        if self.m_Articulo != None:
            acep = wx.MessageBox("Borrar Articulo ?", "Confirma", wx.YES_NO)
            if (acep == wx.YES):
                SESSION.delete(self.m_Articulo)
                SESSION.commit()
                self.VaciarDatos()

            
    def m_OnButtonGuardar( self, event ):
        if self.Validate():
            self.m_Articulo.codigo = self.m_textCtrlCodigo.GetValue()
            self.m_Articulo.codigoaux = self.m_textCtrlCodigoaux.GetValue()        
            self.m_Articulo.descripcion = self.m_textCtrlDescripcion.GetValue()         
            self.m_Articulo.id_proveedor = self.m_textCtrlCuenta.GetValue()
            self.m_Articulo.rubro = self.m_comboBoxRubro.GetClientData(self.m_comboBoxRubro.GetSelection())
            self.m_Articulo.unidad = self.m_comboBoxUnidad.GetClientData(self.m_comboBoxUnidad.GetSelection())
            self.m_Articulo.stock = float(self.m_textCtrlStock.GetValue())
            self.m_Articulo.stockminimo = float(self.m_textCtrlStockMinimo.GetValue())
            self.m_Articulo.redondeo = float(self.m_textCtrlRedondeo.GetValue())
            self.m_Articulo.p_costo = float(self.m_textCtrlP_Costo.GetValue())
            self.m_Articulo.margen = float(self.m_textCtrlMargen.GetValue())
            self.m_Articulo.t_iva = float(self.m_textCtrlT_Iva.GetValue())
            self.m_Articulo.p_venta = float(self.m_textCtrlStock.GetValue())        
            self.m_Articulo.reca_desc1 = float(self.m_textCtrlReca_Desc1.GetValue())
            self.m_Articulo.reca_desc2 = float(self.m_textCtrlReca_Desc2.GetValue())
            self.m_Articulo.reca_desc3 = float(self.m_textCtrlReca_Desc3.GetValue())                       
            #self.m_textCtrlModificado.SetValue(str(self.m_Articulo.modificado))
            self.m_Articulo.activo = self.m_checkBoxActivo.GetValue()        

                      
            SESSION.merge(self.m_Articulo)
            SESSION.commit()
            self.HabilitarControles(False)            
        else:
            wx.MessageBox("Ingrese correctamenta los campos requeridos", "Error")
        

    
    def m_OnButtonDeshacer( self, event ):
        self.m_Articulo = None
        self.VaciarDatos()
        self.HabilitarControles(False)
        
    def m_OnButtonClickBuscar( self, event ):
        busDialog = BuscarArticuloDialog(self) 
        busDialog.ShowModal()
        self.LlenarControles()

            
        