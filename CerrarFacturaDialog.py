# -*- coding: utf-8 -*-
import gui
import wx
import sys
import os
from datetime import date, timedelta
from entidades import *
from Funciones import FechaDatePicker
from wx import calendar


class CerrarFacturaDialog ( gui.CerrarCpbteDialogBase):
    
    
    m_Factura = None
       
   
    def __init__( self, parent):
        gui.CerrarCpbteDialogBase.__init__( self, parent )
        
        self.m_Factura = parent.m_Factura
        
        for row in SESSION.query(Vendedor):
            self.m_comboBoxVendedor.Append(row.nombre, row)
        for row in SESSION.query(Tipo_Venta):
            self.m_comboBoxTipo_Venta.Append(row.tipo, row)


        self.m_comboBoxTipo_Venta.SetStringSelection(self.m_Factura.cliente.tipo_venta.tipo)
        self.m_comboBoxVendedor.SetStringSelection(self.m_Factura.cliente.vendedor.nombre)      
        self.m_textCtrlPlazo.SetValue(str(self.m_Factura.cliente.tipo_venta.plazo))

        self.m_datePickerF_Vencimiento.SetValue(FechaDatePicker(date.today() + timedelta(days=self.m_Factura.cliente.tipo_venta.plazo)))
        self.m_staticTextI_Bruto.SetLabel(str("%.2f" % self.m_Factura.i_bruto).rjust(10))       
        self.m_staticTextIva1.SetLabel("IVA 10.5%")
        self.m_staticTextI_Iva1.SetLabel(str("%.2f" % self.m_Factura.i_iva1).rjust(10))
        self.m_staticTextIva2.SetLabel("IVA 21.0%")        
        self.m_staticTextI_Iva2.SetLabel(str("%.2f" % self.m_Factura.i_iva2).rjust(10))
        self.m_staticTextI_Neto.SetLabel(str("%.2f" % self.m_Factura.i_neto).rjust(10))
        self.m_bpButtonEmitir.SetFocus()
        
        
        
    def m_OnButtonEmitir( self, event ):
        

        self.m_Factura.f_vencimiento = calendar._wxdate2pydate(self.m_datePickerF_Vencimiento.GetValue())
        self.m_Factura.vendedor = self.m_comboBoxVendedor.GetClientData(self.m_comboBoxVendedor.GetSelection())
        self.m_Factura.tipo_venta = self.m_comboBoxTipo_Venta.GetClientData(self.m_comboBoxTipo_Venta.GetSelection())        
        self.m_Factura.observaciones = self.m_textCtrlObservaciones.GetValue()
        
        saveout = sys.stdout                  
        fsock = open('pfisin.txt', 'w')                             
        sys.stdout = fsock                                       

        sep = chr(28)
        #Encabezado
        sys.stdout.write("b" + sep + self.m_Factura.razon + sep + self.m_Factura.cliente.cuit + sep + self.m_Factura.cliente.iva.abreviacion + sep)
        if self.m_Factura.cliente.iva.abreviacion == "C": # Cons. Final
            fsock.write("2") #DNI
        else:
            fsock.write("C") #CUIT               
        fsock.write(sep + self.m_Factura.cliente.direccion + "\n")






        sys.stdout.write("@" + sep)
        sys.stdout.write(self.m_Factura.cliente.iva.comprobante) #Tipo Compbte
        sys.stdout.write(sep + "T\n")

        #Detalle 
        for item in self.m_Factura.d_factura:  
            sys.stdout.write("B" + sep)
            sys.stdout.write(item.articulo.descripcion.encode('cp850', 'ignore') + sep)
            sys.stdout.write(str(round(item.cantidad, 1)) + sep)
            sys.stdout.write(str(round(item.precio, 2)) + sep)            
            sys.stdout.write(str(round(item.t_iva, 1)) + sep)
            sys.stdout.write("M" + sep + "0.0" + sep + "0" + sep + "T\n")



        #Pie
        sys.stdout.write("A" + sep + " " + sep + "0\n") # Linea an blanco
        sys.stdout.write("A" + sep)
        sys.stdout.write(self.m_Factura.observaciones[0:30].encode('cp850', 'ignore'))
        sys.stdout.write(sep + "0\n")
        print "C" + sep + "P" + sep + "Subtotal" + sep +  "0"
        print "D" + sep + "Efectivo" + sep + str(round(self.m_Factura.i_neto, 2)) + sep + "T" + sep + "0"
        print "E"

        sys.stdout = saveout                    
        fsock.close()

        os.system("del PFISIN.ANS")
        os.system("wspooler -p1 -f PFISIN.TXT")


        file = open("PFISIN.ANS")
        lineas = file.readlines()
        numero = "0002" + lineas[1][34:42]
        file.close()
        self.m_Factura.n_cpbte = numero
        self.m_Factura.estado = "F"


        
        SESSION.add(self.m_Factura)
        SESSION.commit()        
        
        self.Destroy()



        
        

    
    def m_OnButtonClickCancelar( self, event ):
        self.Destroy()
        
        



