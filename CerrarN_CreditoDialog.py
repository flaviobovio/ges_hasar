# -*- coding: utf-8 -*-
import gui
import wx
import sys, os, codecs
from datetime import date, timedelta
from entidades import *
from Funciones import FechaDatePicker
from wx import calendar




class CerrarN_CreditoDialog ( gui.CerrarCpbteDialogBase):
    
    
    m_Cpbte = None
       
   
    def __init__( self, parent):
        gui.CerrarCpbteDialogBase.__init__( self, parent )
        
        self.m_Cpbte = parent.m_Cpbte
        
        for row in SESSION.query(Vendedor):
            self.m_comboBoxVendedor.Append(row.nombre, row)
        for row in SESSION.query(Tipo_Venta):
            self.m_comboBoxTipo_Venta.Append(row.tipo, row)


        self.m_comboBoxTipo_Venta.SetStringSelection(self.m_Cpbte.cliente.tipo_venta.tipo)
        self.m_comboBoxVendedor.SetStringSelection(self.m_Cpbte.cliente.vendedor.nombre)      
        self.m_textCtrlPlazo.SetValue(str(self.m_Cpbte.cliente.tipo_venta.plazo))

        self.m_datePickerF_Vencimiento.SetValue(FechaDatePicker(date.today() + timedelta(days=self.m_Cpbte.cliente.tipo_venta.plazo)))
        self.m_staticTextI_Bruto.SetLabel(str("%.2f" % self.m_Cpbte.i_bruto).rjust(10))       
        self.m_staticTextIva1.SetLabel("IVA 10.5%")
        self.m_staticTextI_Iva1.SetLabel(str("%.2f" % self.m_Cpbte.i_iva1).rjust(10))
        self.m_staticTextIva2.SetLabel("IVA 21.0%")        
        self.m_staticTextI_Iva2.SetLabel(str("%.2f" % self.m_Cpbte.i_iva2).rjust(10))
        self.m_staticTextI_Neto.SetLabel(str("%.2f" % self.m_Cpbte.i_neto).rjust(10))
        self.m_bpButtonEmitir.SetFocus()
        
        
        
    def m_OnButtonEmitir( self, event ):
        self.m_Cpbte.f_vencimiento = calendar._wxdate2pydate(self.m_datePickerF_Vencimiento.GetValue())
        self.m_Cpbte.vendedor = self.m_comboBoxVendedor.GetClientData(self.m_comboBoxVendedor.GetSelection())
        self.m_Cpbte.tipo_venta = self.m_comboBoxTipo_Venta.GetClientData(self.m_comboBoxTipo_Venta.GetSelection())  
        self.m_Cpbte.observaciones = self.m_textCtrlObservaciones.GetValue()      
        
        saveout = sys.stdout  


        fsock = open('pfisin.txt', 'w')  
        #fsock = codecs.open('pfisin.txt', encoding=None, mode='w+', errors='ignore')
                    
        sys.stdout = fsock    
        sep = chr(28)
        #Encabezado
        sys.stdout.write("b" + sep + self.m_Cpbte.razon + sep + self.m_Cpbte.cliente.cuit + sep + self.m_Cpbte.cliente.iva.abreviacion + sep)
        if self.m_Cpbte.cliente.iva.abreviacion == "C":  # Cons. Final
            fsock.write("2") #DNI
        else:
            fsock.write("C") #CUIT               
        fsock.write(sep + self.m_Cpbte.cliente.direccion + "\n")
        fsock.write(chr(147))
        fsock.write(sep + "1" + sep + self.m_Cpbte.n_remito.zfill(8) + "\n")  
        fsock.write(chr(128))     
        fsock.write(sep)     
       
        if self.m_Cpbte.cliente.iva.comprobante == "A": #Tipo Compbte
            sys.stdout.write("R") 
        else:
            sys.stdout.write("S")             

        sys.stdout.write(sep + "T" + "\n")

        #Detalle 
        for item in self.m_Cpbte.d_notacr:  
            sys.stdout.write("B" + sep)
            sys.stdout.write(item.articulo.descripcion.encode('cp850', 'ignore') + sep)
            sys.stdout.write(str(round(item.cantidad, 1)) + sep)
            sys.stdout.write(str(round(item.precio, 2)) + sep)            
            sys.stdout.write(str(round(item.t_iva, 1)) + sep)
            sys.stdout.write("M" + sep + "0.0" + sep + "0" + sep + "T\n")
        #Pie
        sys.stdout.write("A" + sep + " " + sep + "0\n") # Linea an blanco        
        sys.stdout.write("A" + sep)
        sys.stdout.write(self.m_Cpbte.observaciones[0:30].encode('cp850', 'ignore'))
        sys.stdout.write(sep + "0\n")
                         
 
        print chr(129)

        sys.stdout = saveout                    
        fsock.close()

        os.system("del PFISIN.ANS")
        os.system("wspooler -p1 -f PFISIN.TXT")


        file = open("PFISIN.ANS")
        lineas = file.readlines()
        numero = "0002" + lineas[1][34:42]
        file.close()
        self.m_Cpbte.n_cpbte = numero
        self.m_Cpbte.estado = "F"


        
        SESSION.add(self.m_Cpbte)
        SESSION.commit()        
        
        self.Destroy()        




        
        

    
    def m_OnButtonClickCancelar( self, event ):
        import sys
        f = open('t.txt', 'w')  

        f.write(chr(147) + "new")
        f.close()    
    
        self.Destroy()
        
        



