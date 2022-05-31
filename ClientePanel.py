import wx
import gui
from entidades import *
from Validadores import *
from Funciones import *
import datetime
from time import time
from BuscarClienteDialog import BuscarClienteDialog




class ClientePanel ( gui.ClientePanelBase ):
    
    m_Cliente = None
 
    def __init__( self, parent ):
        gui.ClientePanelBase.__init__( self, parent )
        self.m_textCtrlCuenta.SetValidator(ValidarTexto())
        self.m_textCtrlRazon.SetValidator(ValidarTexto())
        self.m_textCtrlCuit.SetValidator(ValidarCuit())
        self.m_textCtrlDireccion.SetValidator(ValidarTexto())
        self.m_textCtrlCredito.SetValidator(ValidarNatural())

        for row in SESSION.query(Iva):           
            self.m_comboBoxIva.Append(row.situacion, row)           
        for row in SESSION.query(Vendedor):
            self.m_comboBoxVendedor.Append(row.nombre, row)
        for row in SESSION.query(Tipo_Venta):
            self.m_comboBoxTipo_Venta.Append(row.tipo, row)

        self.HabilitarControles(False)        

    
    def LlenarControles (self):       
        self.m_textCtrlCuenta.SetValue(self.m_Cliente.cuenta)
        self.m_textCtrlRazon.SetValue(self.m_Cliente.razon)
        self.m_textCtrlCuit.SetValue(self.m_Cliente.cuit)
        self.m_textCtrlDireccion.SetValue(self.m_Cliente.direccion)
        self.m_textCtrlLocalidad.SetValue(self.m_Cliente.localidad)
        self.m_textCtrlCp.SetValue(self.m_Cliente.cp)
        self.m_textCtrlProvincia.SetValue(self.m_Cliente.provincia)
        self.m_comboBoxIva.SetStringSelection(self.m_Cliente.iva.situacion)
        self.m_textCtrlTelefono.SetValue(self.m_Cliente.telefono)
        self.m_textCtrlFax.SetValue(self.m_Cliente.fax)
        self.m_textCtrlWeb.SetValue(self.m_Cliente.web)
        self.m_textCtrlEmail.SetValue(self.m_Cliente.email)
        self.m_comboBoxVendedor.SetStringSelection(self.m_Cliente.vendedor.nombre)
        self.m_textCtrlCredito.SetValue(str(self.m_Cliente.credito))
        self.m_comboBoxTipo_Venta.SetStringSelection(self.m_Cliente.tipo_venta.tipo)
        self.m_richTextObservaciones.SetValue(self.m_Cliente.observaciones)
        self.m_checkBoxActivo.SetValue(self.m_Cliente.activo)
        self.m_checkBoxActivo.SetLabel(str(self.m_Cliente.fecha_alta))
        
    def VaciarDatos (self):
        self.m_Cliente = Cliente ("","","","","","","",0,"","","","",0,0,0,"",datetime.date.today(), True)
        self.m_Cliente.iva = SESSION.query(Iva).first()
        self.m_Cliente.vendedor = SESSION.query(Vendedor).first()
        self.m_Cliente.tipo_venta = SESSION.query(Tipo_Venta).first()
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

    def m_OnCharCredito( self, event ):
        if CaracterNatural (event.GetKeyCode()):
            event.Skip()
    def m_OnKillFocusCredito( self, event ):
        return self.m_textCtrlCredito.GetValidator().Validate(self.m_textCtrlCredito)
    
    def m_OnButtonClickPrimero( self, event ):  
        self.m_Cliente = SESSION.query(Cliente).order_by(Cliente.cuenta).first()
        self.LlenarControles()
    def m_OnButtonClickAnterior( self, event ):
        cuen = self.m_textCtrlCuenta.GetValue()
        self.m_Cliente = SESSION.query(Cliente).order_by(desc(Cliente.cuenta)).filter(Cliente.cuenta < cuen).first()
        if self.m_Cliente != None:
            self.LlenarControles()
    
    def m_OnButtonClickSiguiente( self, event ):
        cuen = self.m_textCtrlCuenta.GetValue()
        self.m_Cliente = SESSION.query(Cliente).order_by(Cliente.cuenta).filter(Cliente.cuenta > cuen).first()
       
        if self.m_Cliente != None:
            self.LlenarControles()
    
    def m_OnButtonClickUltimo( self, event ):
        self.m_Cliente = SESSION.query(Cliente).order_by(desc(Cliente.cuenta)).first()
        self.LlenarControles()

    def m_OnButtonClickAgregar( self, event ):
        self.VaciarDatos()
        self.m_comboBoxIva.SetSelection(0)
        self.m_comboBoxVendedor.SetSelection(0)
        self.m_comboBoxTipo_Venta.SetSelection(0)        
        self.HabilitarControles(True)
    
    def m_OnButtonClickEditar( self, event ):
        if self.m_Cliente != None:
            self.HabilitarControles(True)
    
    def m_OnButtonClickBorrar( self, event ):
        DATABASE.echo = True
        if self.m_Cliente != None:
            acep = wx.MessageBox("Borrar Cliente ?", "Confirma", wx.YES_NO)
            if (acep == wx.YES):
                SESSION.delete(self.m_Cliente)
                SESSION.commit()
                self.VaciarDatos()

            
    def m_OnButtonGuardar( self, event ):
        if self.Validate():
            self.m_Cliente.cuenta = self.m_textCtrlCuenta.GetValue()
            self.m_Cliente.razon = self.m_textCtrlRazon.GetValue()
            self.m_Cliente.cuit = self.m_textCtrlCuit.GetValue()
            self.m_Cliente.direccion = self.m_textCtrlDireccion.GetValue()
            self.m_Cliente.localidad = self.m_textCtrlLocalidad.GetValue()
            self.m_Cliente.cp = self.m_textCtrlCp.GetValue()
            self.m_Cliente.provincia = self.m_textCtrlProvincia.GetValue()
            self.m_Cliente.iva = self.m_comboBoxIva.GetClientData(self.m_comboBoxIva.GetSelection())
            self.m_Cliente.telefono = self.m_textCtrlTelefono.GetValue()
            self.m_Cliente.fax = self.m_textCtrlFax.GetValue()
            self.m_Cliente.web = self.m_textCtrlWeb.GetValue()
            self.m_Cliente.email = self.m_textCtrlEmail.GetValue()
            self.m_Cliente.vendedor = self.m_comboBoxVendedor.GetClientData(self.m_comboBoxVendedor.GetSelection())
            self.m_Cliente.credito = float(self.m_textCtrlCredito.GetValue())
            self.m_Cliente.tipo_venta = self.m_comboBoxTipo_Venta.GetClientData(self.m_comboBoxTipo_Venta.GetSelection())
            self.m_Cliente.observaciones = self.m_richTextObservaciones.GetValue()
            #OZZY -> datetime.date.today()
            self.m_Cliente.activo = self.m_checkBoxActivo.GetValue()
                       
            SESSION.merge(self.m_Cliente)
            SESSION.commit()
            self.HabilitarControles(False)            
        else:
            wx.MessageBox("Ingrese correctamenta los campos requeridos", "Error")
        

    
    def m_OnButtonDeshacer( self, event ):
        self.m_Cliente = None
        self.VaciarDatos()
        self.HabilitarControles(False)
        
    def m_OnButtonClickBuscar( self, event ):
        busDialog = BuscarClienteDialog(self) 
        busDialog.ShowModal()
        self.LlenarControles()

        