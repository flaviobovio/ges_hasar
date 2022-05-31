import wx
import gui
from entidades import *
from Validadores import *
from Funciones import *
import datetime
from time import time
from BuscarProveedorDialog import BuscarProveedorDialog




class ProveedorPanel ( gui.ProveedorPanelBase ):
    
    m_Proveedor = None
 
    def __init__( self, parent ):
        gui.ProveedorPanelBase.__init__( self, parent )
        self.m_textCtrlCuenta.SetValidator(ValidarTexto())
        self.m_textCtrlRazon.SetValidator(ValidarTexto())
        self.m_textCtrlCuit.SetValidator(ValidarCuit())
        self.m_textCtrlDireccion.SetValidator(ValidarTexto())

        for row in SESSION.query(Iva):           
            self.m_comboBoxIva.Append(row.situacion, row)           

        self.HabilitarControles(False)        

    
    def LlenarControles (self):       
        self.m_textCtrlCuenta.SetValue(self.m_Proveedor.cuenta)
        self.m_textCtrlRazon.SetValue(self.m_Proveedor.razon)
        self.m_textCtrlCuit.SetValue(self.m_Proveedor.cuit)
        self.m_textCtrlDireccion.SetValue(self.m_Proveedor.direccion)
        self.m_textCtrlLocalidad.SetValue(self.m_Proveedor.localidad)
        self.m_textCtrlCp.SetValue(self.m_Proveedor.cp)
        self.m_textCtrlProvincia.SetValue(self.m_Proveedor.provincia)
        #self.m_comboBoxIva.SetStringSelection(self.m_Proveedor.iva.situacion)
        self.m_textCtrlTelefono.SetValue(self.m_Proveedor.telefono)
        self.m_textCtrlFax.SetValue(self.m_Proveedor.fax)
        self.m_textCtrlWeb.SetValue(self.m_Proveedor.web)
        self.m_textCtrlEmail.SetValue(self.m_Proveedor.email)
        self.m_richTextObservaciones.SetValue(self.m_Proveedor.observaciones)
        self.m_checkBoxActivo.SetValue(self.m_Proveedor.activo)
        self.m_checkBoxActivo.SetLabel(str(self.m_Proveedor.fecha_alta))
        
    def VaciarDatos (self):
        self.m_Proveedor = Proveedor ("","","","","","","",0,"","","","","",datetime.date.today(), True)
        self.m_Proveedor.iva = SESSION.query(Iva).first()
        self.LlenarControles()

    def HabilitarControles(self, acti): # True Activar, False Desactivar
        for ctrl in self.GetChildren():
            if ctrl.GetName() != "button":
                ctrl.Enable(acti)
            else:
                ctrl.Enable(not acti)
        self.m_bpButtonDeshacer.Enable(acti)
        self.m_bpButtonGuardar.Enable(acti)       
        self.m_textCtrlCuenta.SetFocus()
       
       
        
    def m_OnCharCuit( self, event ):
        if CaracterNatural (event.GetKeyCode()):
            event.Skip()

    def m_OnKillFocusCuit( self, event ):
        return self.m_textCtrlCuit.GetValidator().Validate(self.m_textCtrlCuit)

    def m_OnKillFocusCuenta( self, event ):
        return self.m_textCtrlCuenta.GetValidator().Validate(self.m_textCtrlCuenta)

    def m_OnKillFocusRazon( self, event ):
        return self.m_textCtrlRazon.GetValidator().Validate(self.m_textCtrlRazon)
    
    def m_OnKillFocusDireccion( self, event ):
        return self.m_textCtrlDireccion.GetValidator().Validate(self.m_textCtrlDireccion)

    
    def m_OnButtonClickPrimero( self, event ):  
        self.m_Proveedor = SESSION.query(Proveedor).order_by(Proveedor.cuenta).first()
        self.LlenarControles()
    def m_OnButtonClickAnterior( self, event ):
        cuen = self.m_textCtrlCuenta.GetValue()
        self.m_Proveedor = SESSION.query(Proveedor).order_by(desc(Proveedor.cuenta)).filter(Proveedor.cuenta < cuen).first()
        if self.m_Proveedor != None:
            self.LlenarControles()
    
    def m_OnButtonClickSiguiente( self, event ):
        cuen = self.m_textCtrlCuenta.GetValue()
        self.m_Proveedor = SESSION.query(Proveedor).order_by(Proveedor.cuenta).filter(Proveedor.cuenta > cuen).first()
       
        if self.m_Proveedor != None:
            self.LlenarControles()
    
    def m_OnButtonClickUltimo( self, event ):
        self.m_Proveedor = SESSION.query(Proveedor).order_by(desc(Proveedor.cuenta)).first()
        self.LlenarControles()

    def m_OnButtonClickAgregar( self, event ):
        self.VaciarDatos()
        self.m_comboBoxIva.SetSelection(0)
        self.HabilitarControles(True)
    
    def m_OnButtonClickEditar( self, event ):
        if self.m_Proveedor != None:
            self.HabilitarControles(True)
    
    def m_OnButtonClickBorrar( self, event ):
        DATABASE.echo = True
        if self.m_Proveedor != None:
            acep = wx.MessageBox("Borrar Proveedor ?", "Confirma", wx.YES_NO)
            if (acep == wx.YES):
                SESSION.delete(self.m_Proveedor)
                SESSION.commit()
                self.VaciarDatos()

            
    def m_OnButtonGuardar( self, event ):
        if self.Validate():
            self.m_Proveedor.cuenta = self.m_textCtrlCuenta.GetValue()
            self.m_Proveedor.razon = self.m_textCtrlRazon.GetValue()
            self.m_Proveedor.cuit = self.m_textCtrlCuit.GetValue()
            self.m_Proveedor.direccion = self.m_textCtrlDireccion.GetValue()
            self.m_Proveedor.localidad = self.m_textCtrlLocalidad.GetValue()
            self.m_Proveedor.cp = self.m_textCtrlCp.GetValue()
            self.m_Proveedor.provincia = self.m_textCtrlProvincia.GetValue()
            self.m_Proveedor.iva = self.m_comboBoxIva.GetClientData(self.m_comboBoxIva.GetSelection())
            self.m_Proveedor.telefono = self.m_textCtrlTelefono.GetValue()
            self.m_Proveedor.fax = self.m_textCtrlFax.GetValue()
            self.m_Proveedor.web = self.m_textCtrlWeb.GetValue()
            self.m_Proveedor.email = self.m_textCtrlEmail.GetValue()
            self.m_Proveedor.observaciones = self.m_richTextObservaciones.GetValue()
            #OZZY -> datetime.date.today()
            self.m_Proveedor.activo = self.m_checkBoxActivo.GetValue()
                       
            SESSION.merge(self.m_Proveedor)
            SESSION.commit()
            self.HabilitarControles(False)            
        else:
            wx.MessageBox("Ingrese correctamenta los campos requeridos", "Error")
        

    
    def m_OnButtonDeshacer( self, event ):
        self.m_Proveedor = None
        self.VaciarDatos()
        self.HabilitarControles(False)
        
    def m_OnButtonClickBuscar( self, event ):
        busDialog = BuscarProveedorDialog(self) 
        busDialog.ShowModal()
        self.LlenarControles()

        