# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb  9 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.richtext
import wx.grid

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Gestion", pos = wx.DefaultPosition, size = wx.Size( 800,570 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auinotebook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		
		bSizer2.Add( self.m_auinotebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar = wx.MenuBar( 0 )
		self.m_mnArchivo = wx.Menu()
		self.m_mniClientes = wx.MenuItem( self.m_mnArchivo, wx.ID_ANY, u"&Clientes", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnArchivo.AppendItem( self.m_mniClientes )
		
		self.m_mni_proveedores = wx.MenuItem( self.m_mnArchivo, wx.ID_ANY, u"&Proveedores", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnArchivo.AppendItem( self.m_mni_proveedores )
		
		self.m_mniArticulos = wx.MenuItem( self.m_mnArchivo, wx.ID_ANY, u"&Articulos", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnArchivo.AppendItem( self.m_mniArticulos )
		
		self.m_mnArchivo.AppendSeparator()
		
		self.m_mniSalir = wx.MenuItem( self.m_mnArchivo, wx.ID_ANY, u"&Salir", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnArchivo.AppendItem( self.m_mniSalir )
		
		self.m_menubar.Append( self.m_mnArchivo, u"&Archivo" ) 
		
		self.m_mnComprobantes = wx.Menu()
		self.m_mniFactura = wx.MenuItem( self.m_mnComprobantes, wx.ID_ANY, u"&Factura", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnComprobantes.AppendItem( self.m_mniFactura )
		
		self.m_mniNCredito = wx.MenuItem( self.m_mnComprobantes, wx.ID_ANY, u"Nota de &Crédito", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnComprobantes.AppendItem( self.m_mniNCredito )
		
		self.m_mnComprobantes.AppendSeparator()
		
		self.m_mniCierreZ = wx.MenuItem( self.m_mnComprobantes, wx.ID_ANY, u"Cierre &Z", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnComprobantes.AppendItem( self.m_mniCierreZ )
		
		self.m_menubar.Append( self.m_mnComprobantes, u"&Comprobantes" ) 
		
		self.m_mnAyuda = wx.Menu()
		self.m_mniAcercade = wx.MenuItem( self.m_mnAyuda, wx.ID_ANY, u"&Acerca de", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnAyuda.AppendItem( self.m_mniAcercade )
		
		self.m_menubar.Append( self.m_mnAyuda, u"&?" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_mniClientesClick, id = self.m_mniClientes.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniProveedores, id = self.m_mni_proveedores.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniArticulosClick, id = self.m_mniArticulos.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniSalirClick, id = self.m_mniSalir.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniFacturaClick, id = self.m_mniFactura.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniN_CreditoClick, id = self.m_mniNCredito.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniCierreZClick, id = self.m_mniCierreZ.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniAcercadeClick, id = self.m_mniAcercade.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_mniClientesClick( self, event ):
		event.Skip()
	
	def m_mniProveedores( self, event ):
		event.Skip()
	
	def m_mniArticulosClick( self, event ):
		event.Skip()
	
	def m_mniSalirClick( self, event ):
		event.Skip()
	
	def m_mniFacturaClick( self, event ):
		event.Skip()
	
	def m_mniN_CreditoClick( self, event ):
		event.Skip()
	
	def m_mniCierreZClick( self, event ):
		event.Skip()
	
	def m_mniAcercadeClick( self, event ):
		event.Skip()
	

###########################################################################
## Class ClientePanelBase
###########################################################################

class ClientePanelBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.TAB_TRAVERSAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 2, 5, 5, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Cuenta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetMinSize( wx.Size( 75,-1 ) )
		self.m_staticText7.SetMaxSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText7, 1, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_textCtrlCuenta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CAPITALIZE )
		self.m_textCtrlCuenta.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlCuenta, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )
		
		
		fgSizer2.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetMinSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrlRazon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlRazon.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlRazon, 1, wx.TOP, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"IVA               ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetMinSize( wx.Size( 75,-1 ) )
		self.m_staticText9.SetMaxSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxIvaChoices = []
		self.m_comboBoxIva = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxIvaChoices, wx.CB_READONLY )
		self.m_comboBoxIva.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_comboBoxIva, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 5, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"CUIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer2.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlCuit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
		self.m_textCtrlCuit.SetMaxLength( 11 ) 
		self.m_textCtrlCuit.SetMinSize( wx.Size( 110,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlCuit, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Dirección  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetMinSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlDireccion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlDireccion.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlDireccion, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Localidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrlLocalidad = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlLocalidad.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlLocalidad, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"C.Postal    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer2.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlCp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlCp.SetMinSize( wx.Size( 100,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlCp, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Provincia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer2.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlProvincia = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlProvincia.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlProvincia, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		fgSizer2.Add( self.m_staticText53, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlTelefono = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlTelefono, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Fax", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer2.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlFax = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlFax.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlFax, 0, 0, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"E-Mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer2.Add( self.m_staticText22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlEmail, 0, 0, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Web", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer2.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlWeb = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlWeb, 0, 0, 5 )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Vendedor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer2.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxVendedorChoices = []
		self.m_comboBoxVendedor = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxVendedorChoices, wx.CB_READONLY )
		fgSizer2.Add( self.m_comboBoxVendedor, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Cond.Vta.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer2.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxTipo_VentaChoices = []
		self.m_comboBoxTipo_Venta = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxTipo_VentaChoices, wx.CB_READONLY )
		fgSizer2.Add( self.m_comboBoxTipo_Venta, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Crédito", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		fgSizer2.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.m_textCtrlCredito = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.m_textCtrlCredito.SetMinSize( wx.Size( 100,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlCredito, 0, 0, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		fgSizer2.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_checkBoxActivo = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxActivo.SetValue(True) 
		self.m_checkBoxActivo.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_checkBoxActivo, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer7.Add( fgSizer2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Notas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetMinSize( wx.Size( 75,-1 ) )
		
		bSizer8.Add( self.m_staticText29, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_richTextObservaciones = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		self.m_richTextObservaciones.Enable( False )
		self.m_richTextObservaciones.SetMinSize( wx.Size( -1,50 ) )
		self.m_richTextObservaciones.SetMaxSize( wx.Size( 700,50 ) )
		
		bSizer8.Add( self.m_richTextObservaciones, 1, wx.EXPAND|wx.BOTTOM, 5 )
		
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButtonPrimero = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_2leftarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonPrimero.SetToolTipString( u"Primero" )
		
		bSizer9.Add( self.m_bpButtonPrimero, 0, wx.ALL, 5 )
		
		self.m_bpButtonAnterior = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_1leftarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonAnterior.SetToolTipString( u"Anterior" )
		
		bSizer9.Add( self.m_bpButtonAnterior, 0, wx.ALL, 5 )
		
		self.m_bpButtonSiguiente = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_player_play_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonSiguiente.SetToolTipString( u"Siguiente" )
		
		bSizer9.Add( self.m_bpButtonSiguiente, 0, wx.ALL, 5 )
		
		self.m_bpButtonUltimo = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_2rightarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonUltimo.SetToolTipString( u"Ultimo" )
		
		bSizer9.Add( self.m_bpButtonUltimo, 0, wx.ALL, 5 )
		
		self.m_bpButtonBuscar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_find_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonBuscar, 0, wx.ALL, 5 )
		
		self.m_bpButtonAgregar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_add_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonAgregar, 0, wx.ALL, 5 )
		
		self.m_bpButtonEditar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonEditar, 0, wx.ALL, 5 )
		
		self.m_bpButtonBorrar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_remove_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonBorrar, 0, wx.ALL, 5 )
		
		self.m_bpButtonGuardar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_apply_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonGuardar, 0, wx.ALL, 5 )
		
		self.m_bpButtonDeshacer = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_reload_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonDeshacer.SetToolTipString( u"Deshacer" )
		
		bSizer9.Add( self.m_bpButtonDeshacer, 0, wx.ALL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer9, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		# Connect Events
		self.m_textCtrlCuenta.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusCuenta )
		self.m_textCtrlRazon.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusRazon )
		self.m_textCtrlCuit.Bind( wx.EVT_CHAR, self.m_OnCharCuit )
		self.m_textCtrlCuit.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusCuit )
		self.m_textCtrlDireccion.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusDireccion )
		self.m_textCtrlCredito.Bind( wx.EVT_CHAR, self.m_OnCharCredito )
		self.m_textCtrlCredito.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusCredito )
		self.m_bpButtonPrimero.Bind( wx.EVT_BUTTON, self.m_OnButtonClickPrimero )
		self.m_bpButtonAnterior.Bind( wx.EVT_BUTTON, self.m_OnButtonClickAnterior )
		self.m_bpButtonSiguiente.Bind( wx.EVT_BUTTON, self.m_OnButtonClickSiguiente )
		self.m_bpButtonUltimo.Bind( wx.EVT_BUTTON, self.m_OnButtonClickUltimo )
		self.m_bpButtonBuscar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBuscar )
		self.m_bpButtonAgregar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickAgregar )
		self.m_bpButtonEditar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickEditar )
		self.m_bpButtonBorrar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBorrar )
		self.m_bpButtonGuardar.Bind( wx.EVT_BUTTON, self.m_OnButtonGuardar )
		self.m_bpButtonDeshacer.Bind( wx.EVT_BUTTON, self.m_OnButtonDeshacer )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnKillFocusCuenta( self, event ):
		event.Skip()
	
	def m_OnKillFocusRazon( self, event ):
		event.Skip()
	
	def m_OnCharCuit( self, event ):
		event.Skip()
	
	def m_OnKillFocusCuit( self, event ):
		event.Skip()
	
	def m_OnKillFocusDireccion( self, event ):
		event.Skip()
	
	def m_OnCharCredito( self, event ):
		event.Skip()
	
	def m_OnKillFocusCredito( self, event ):
		event.Skip()
	
	def m_OnButtonClickPrimero( self, event ):
		event.Skip()
	
	def m_OnButtonClickAnterior( self, event ):
		event.Skip()
	
	def m_OnButtonClickSiguiente( self, event ):
		event.Skip()
	
	def m_OnButtonClickUltimo( self, event ):
		event.Skip()
	
	def m_OnButtonClickBuscar( self, event ):
		event.Skip()
	
	def m_OnButtonClickAgregar( self, event ):
		event.Skip()
	
	def m_OnButtonClickEditar( self, event ):
		event.Skip()
	
	def m_OnButtonClickBorrar( self, event ):
		event.Skip()
	
	def m_OnButtonGuardar( self, event ):
		event.Skip()
	
	def m_OnButtonDeshacer( self, event ):
		event.Skip()
	

###########################################################################
## Class ProveedorPanelBase
###########################################################################

class ProveedorPanelBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.TAB_TRAVERSAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 2, 5, 5, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Cuenta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetMinSize( wx.Size( 75,-1 ) )
		self.m_staticText7.SetMaxSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText7, 1, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_textCtrlCuenta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CAPITALIZE )
		self.m_textCtrlCuenta.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlCuenta, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )
		
		
		fgSizer2.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetMinSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrlRazon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlRazon.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlRazon, 1, wx.TOP, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"IVA               ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetMinSize( wx.Size( 75,-1 ) )
		self.m_staticText9.SetMaxSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxIvaChoices = []
		self.m_comboBoxIva = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxIvaChoices, wx.CB_READONLY )
		self.m_comboBoxIva.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_comboBoxIva, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 5, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"CUIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer2.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlCuit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
		self.m_textCtrlCuit.SetMaxLength( 11 ) 
		self.m_textCtrlCuit.SetMinSize( wx.Size( 110,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlCuit, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Dirección  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetMinSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlDireccion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlDireccion.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlDireccion, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Localidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrlLocalidad = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlLocalidad.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlLocalidad, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"C.Postal    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer2.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlCp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlCp.SetMinSize( wx.Size( 100,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlCp, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Provincia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer2.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlProvincia = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlProvincia.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlProvincia, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		fgSizer2.Add( self.m_staticText53, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlTelefono = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlTelefono, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Fax", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer2.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlFax = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlFax.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlFax, 0, 0, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"E-Mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer2.Add( self.m_staticText22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlEmail, 0, 0, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Web", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer2.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlWeb = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlWeb, 0, 0, 5 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		fgSizer2.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_checkBoxActivo = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxActivo.SetValue(True) 
		self.m_checkBoxActivo.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_checkBoxActivo, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer7.Add( fgSizer2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Notas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetMinSize( wx.Size( 75,-1 ) )
		
		bSizer8.Add( self.m_staticText29, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_richTextObservaciones = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.HSCROLL|wx.VSCROLL|wx.WANTS_CHARS )
		self.m_richTextObservaciones.Enable( False )
		self.m_richTextObservaciones.SetMinSize( wx.Size( -1,50 ) )
		self.m_richTextObservaciones.SetMaxSize( wx.Size( 700,50 ) )
		
		bSizer8.Add( self.m_richTextObservaciones, 1, wx.EXPAND|wx.BOTTOM, 5 )
		
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButtonPrimero = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_2leftarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonPrimero.SetToolTipString( u"Primero" )
		
		bSizer9.Add( self.m_bpButtonPrimero, 0, wx.ALL, 5 )
		
		self.m_bpButtonAnterior = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_1leftarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonAnterior.SetToolTipString( u"Anterior" )
		
		bSizer9.Add( self.m_bpButtonAnterior, 0, wx.ALL, 5 )
		
		self.m_bpButtonSiguiente = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_player_play_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonSiguiente.SetToolTipString( u"Siguiente" )
		
		bSizer9.Add( self.m_bpButtonSiguiente, 0, wx.ALL, 5 )
		
		self.m_bpButtonUltimo = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_2rightarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonUltimo.SetToolTipString( u"Ultimo" )
		
		bSizer9.Add( self.m_bpButtonUltimo, 0, wx.ALL, 5 )
		
		self.m_bpButtonBuscar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_find_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonBuscar, 0, wx.ALL, 5 )
		
		self.m_bpButtonAgregar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_add_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonAgregar, 0, wx.ALL, 5 )
		
		self.m_bpButtonEditar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonEditar, 0, wx.ALL, 5 )
		
		self.m_bpButtonBorrar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_remove_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonBorrar, 0, wx.ALL, 5 )
		
		self.m_bpButtonGuardar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_apply_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonGuardar, 0, wx.ALL, 5 )
		
		self.m_bpButtonDeshacer = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_reload_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonDeshacer.SetToolTipString( u"Deshacer" )
		
		bSizer9.Add( self.m_bpButtonDeshacer, 0, wx.ALL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer9, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		# Connect Events
		self.m_textCtrlCuenta.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusCuenta )
		self.m_textCtrlRazon.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusRazon )
		self.m_textCtrlCuit.Bind( wx.EVT_CHAR, self.m_OnCharCuit )
		self.m_textCtrlCuit.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusCuit )
		self.m_textCtrlDireccion.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusDireccion )
		self.m_bpButtonPrimero.Bind( wx.EVT_BUTTON, self.m_OnButtonClickPrimero )
		self.m_bpButtonAnterior.Bind( wx.EVT_BUTTON, self.m_OnButtonClickAnterior )
		self.m_bpButtonSiguiente.Bind( wx.EVT_BUTTON, self.m_OnButtonClickSiguiente )
		self.m_bpButtonUltimo.Bind( wx.EVT_BUTTON, self.m_OnButtonClickUltimo )
		self.m_bpButtonBuscar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBuscar )
		self.m_bpButtonAgregar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickAgregar )
		self.m_bpButtonEditar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickEditar )
		self.m_bpButtonBorrar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBorrar )
		self.m_bpButtonGuardar.Bind( wx.EVT_BUTTON, self.m_OnButtonGuardar )
		self.m_bpButtonDeshacer.Bind( wx.EVT_BUTTON, self.m_OnButtonDeshacer )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnKillFocusCuenta( self, event ):
		event.Skip()
	
	def m_OnKillFocusRazon( self, event ):
		event.Skip()
	
	def m_OnCharCuit( self, event ):
		event.Skip()
	
	def m_OnKillFocusCuit( self, event ):
		event.Skip()
	
	def m_OnKillFocusDireccion( self, event ):
		event.Skip()
	
	def m_OnButtonClickPrimero( self, event ):
		event.Skip()
	
	def m_OnButtonClickAnterior( self, event ):
		event.Skip()
	
	def m_OnButtonClickSiguiente( self, event ):
		event.Skip()
	
	def m_OnButtonClickUltimo( self, event ):
		event.Skip()
	
	def m_OnButtonClickBuscar( self, event ):
		event.Skip()
	
	def m_OnButtonClickAgregar( self, event ):
		event.Skip()
	
	def m_OnButtonClickEditar( self, event ):
		event.Skip()
	
	def m_OnButtonClickBorrar( self, event ):
		event.Skip()
	
	def m_OnButtonGuardar( self, event ):
		event.Skip()
	
	def m_OnButtonDeshacer( self, event ):
		event.Skip()
	

###########################################################################
## Class CpbtePanelBase
###########################################################################

class CpbtePanelBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.TAB_TRAVERSAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 5, 5, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Cliente", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		self.m_staticText32.SetMinSize( wx.Size( 110,-1 ) )
		
		fgSizer3.Add( self.m_staticText32, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlCuenta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.m_textCtrlCuenta.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer3.Add( self.m_textCtrlCuenta, 0, wx.TOP|wx.RIGHT, 5 )
		
		self.m_bpButtonCliente = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_find_16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_bpButtonCliente, 0, wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		self.m_staticText33.SetMinSize( wx.Size( 75,-1 ) )
		
		fgSizer3.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlRazon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlRazon.SetMinSize( wx.Size( 320,-1 ) )
		
		fgSizer3.Add( self.m_textCtrlRazon, 0, wx.TOP, 5 )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Comprobante", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetMinSize( wx.Size( 100,-1 ) )
		
		fgSizer3.Add( self.m_staticText29, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticTextCpbte = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCpbte.Wrap( -1 )
		self.m_staticTextCpbte.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 94, 92, False, wx.EmptyString ) )
		
		fgSizer3.Add( self.m_staticTextCpbte, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 110, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Número", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		fgSizer3.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlNumero = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlNumero.SetMinSize( wx.Size( 100,-1 ) )
		
		fgSizer3.Add( self.m_textCtrlNumero, 0, 0, 5 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		fgSizer3.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_datePickerFecha = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer3.Add( self.m_datePickerFecha, 0, 0, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticTextRemito = wx.StaticText( self, wx.ID_ANY, u"Remito", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextRemito.Wrap( -1 )
		fgSizer3.Add( self.m_staticTextRemito, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlRemito = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.m_textCtrlRemito.SetMinSize( wx.Size( 100,-1 ) )
		
		fgSizer3.Add( self.m_textCtrlRemito, 0, 0, 5 )
		
		
		fgSizer3.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( fgSizer3, 0, wx.EXPAND, 5 )
		
		self.m_gridDetalle = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridDetalle.CreateGrid( 10, 5 )
		self.m_gridDetalle.EnableEditing( True )
		self.m_gridDetalle.EnableGridLines( True )
		self.m_gridDetalle.EnableDragGridSize( False )
		self.m_gridDetalle.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridDetalle.SetColSize( 0, 107 )
		self.m_gridDetalle.SetColSize( 1, 400 )
		self.m_gridDetalle.SetColSize( 2, 59 )
		self.m_gridDetalle.SetColSize( 3, 80 )
		self.m_gridDetalle.SetColSize( 4, 87 )
		self.m_gridDetalle.EnableDragColMove( False )
		self.m_gridDetalle.EnableDragColSize( True )
		self.m_gridDetalle.SetColLabelSize( 30 )
		self.m_gridDetalle.SetColLabelValue( 0, u"Código" )
		self.m_gridDetalle.SetColLabelValue( 1, u"Artículo" )
		self.m_gridDetalle.SetColLabelValue( 2, u"Can" )
		self.m_gridDetalle.SetColLabelValue( 3, u"Precio" )
		self.m_gridDetalle.SetColLabelValue( 4, u"SubTotal" )
		self.m_gridDetalle.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridDetalle.EnableDragRowSize( True )
		self.m_gridDetalle.SetRowLabelSize( 20 )
		self.m_gridDetalle.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridDetalle.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer7.Add( self.m_gridDetalle, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10.SetMinSize( wx.Size( 5,1 ) ) 
		self.m_bpButtonOk = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_apply_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer10.Add( self.m_bpButtonOk, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		# Connect Events
		self.m_textCtrlCuenta.Bind( wx.EVT_KEY_DOWN, self.m_OnKeyDownCuenta )
		self.m_bpButtonCliente.Bind( wx.EVT_BUTTON, self.m_OnButtonClickCliente )
		self.m_textCtrlRazon.Bind( wx.EVT_SET_FOCUS, self.m_OnSetFocusRazon )
		self.m_gridDetalle.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.m_OnGridCellChange )
		self.m_gridDetalle.Bind( wx.EVT_KEY_DOWN, self.m_OnKeyDownDetalle )
		self.m_bpButtonOk.Bind( wx.EVT_BUTTON, self.m_OnButtonClickOk )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnKeyDownCuenta( self, event ):
		event.Skip()
	
	def m_OnButtonClickCliente( self, event ):
		event.Skip()
	
	def m_OnSetFocusRazon( self, event ):
		event.Skip()
	
	def m_OnGridCellChange( self, event ):
		event.Skip()
	
	def m_OnKeyDownDetalle( self, event ):
		event.Skip()
	
	def m_OnButtonClickOk( self, event ):
		event.Skip()
	

###########################################################################
## Class ReciboPanelBase
###########################################################################

class ReciboPanelBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.TAB_TRAVERSAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 5, 5, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Cliente", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		self.m_staticText32.SetMinSize( wx.Size( 110,-1 ) )
		
		fgSizer3.Add( self.m_staticText32, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlCuenta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.m_textCtrlCuenta.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer3.Add( self.m_textCtrlCuenta, 0, wx.TOP|wx.RIGHT, 5 )
		
		self.m_bpButtonCliente = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_find_16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_bpButtonCliente, 0, wx.TOP|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		self.m_staticText33.SetMinSize( wx.Size( 60,-1 ) )
		
		fgSizer3.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlRazon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlRazon.SetMinSize( wx.Size( 360,-1 ) )
		
		fgSizer3.Add( self.m_textCtrlRazon, 0, wx.TOP, 5 )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Comprobante", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetMinSize( wx.Size( 100,-1 ) )
		
		fgSizer3.Add( self.m_staticText29, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Recibo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		self.m_staticText35.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 94, 92, False, wx.EmptyString ) )
		
		fgSizer3.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 80, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Número", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		fgSizer3.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlNumero = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlNumero.SetMinSize( wx.Size( 100,-1 ) )
		
		fgSizer3.Add( self.m_textCtrlNumero, 0, 0, 5 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		fgSizer3.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_datePicker2 = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer3.Add( self.m_datePicker2, 0, 0, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"Concepto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		fgSizer3.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl26.SetMinSize( wx.Size( 360,-1 ) )
		
		fgSizer3.Add( self.m_textCtrl26, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer7.Add( fgSizer3, 0, wx.EXPAND, 5 )
		
		self.m_gridDetalle = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridDetalle.CreateGrid( 10, 6 )
		self.m_gridDetalle.EnableEditing( True )
		self.m_gridDetalle.EnableGridLines( True )
		self.m_gridDetalle.EnableDragGridSize( False )
		self.m_gridDetalle.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridDetalle.SetColSize( 0, 90 )
		self.m_gridDetalle.SetColSize( 1, 100 )
		self.m_gridDetalle.SetColSize( 2, 182 )
		self.m_gridDetalle.SetColSize( 3, 90 )
		self.m_gridDetalle.SetColSize( 4, 186 )
		self.m_gridDetalle.SetColSize( 5, 100 )
		self.m_gridDetalle.EnableDragColMove( False )
		self.m_gridDetalle.EnableDragColSize( True )
		self.m_gridDetalle.SetColLabelSize( 30 )
		self.m_gridDetalle.SetColLabelValue( 0, wx.EmptyString )
		self.m_gridDetalle.SetColLabelValue( 1, u"Fecha" )
		self.m_gridDetalle.SetColLabelValue( 2, u"Banco/Tarjeta" )
		self.m_gridDetalle.SetColLabelValue( 3, u"Número" )
		self.m_gridDetalle.SetColLabelValue( 4, u"Plaza" )
		self.m_gridDetalle.SetColLabelValue( 5, u"Importe" )
		self.m_gridDetalle.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridDetalle.EnableDragRowSize( True )
		self.m_gridDetalle.SetRowLabelSize( 20 )
		self.m_gridDetalle.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridDetalle.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer7.Add( self.m_gridDetalle, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10.SetMinSize( wx.Size( 5,1 ) ) 
		self.m_bpButtonOk = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_fileprint_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer10.Add( self.m_bpButtonOk, 0, wx.ALL, 5 )
		
		self.m_bpButton18 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_app_kfloppy_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer10.Add( self.m_bpButton18, 0, wx.ALL, 5 )
		
		self.m_bpButton19 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_button_cancel_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer10.Add( self.m_bpButton19, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		# Connect Events
		self.m_textCtrlCuenta.Bind( wx.EVT_KEY_DOWN, self.m_OnKeyDownCuenta )
		self.m_bpButtonCliente.Bind( wx.EVT_BUTTON, self.m_OnButtonClickCliente )
		self.m_textCtrlRazon.Bind( wx.EVT_SET_FOCUS, self.m_OnSetFocusRazon )
		self.m_gridDetalle.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.m_OnGridCellChange )
		self.m_gridDetalle.Bind( wx.EVT_KEY_DOWN, self.m_OnKeyDownDetalle )
		self.m_bpButtonOk.Bind( wx.EVT_BUTTON, self.m_OnButtonClickImprimir )
		self.m_bpButton18.Bind( wx.EVT_BUTTON, self.m_OnButtonClickGuardar )
		self.m_bpButton19.Bind( wx.EVT_BUTTON, self.m_OnButtonClickCancelar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnKeyDownCuenta( self, event ):
		event.Skip()
	
	def m_OnButtonClickCliente( self, event ):
		event.Skip()
	
	def m_OnSetFocusRazon( self, event ):
		event.Skip()
	
	def m_OnGridCellChange( self, event ):
		event.Skip()
	
	def m_OnKeyDownDetalle( self, event ):
		event.Skip()
	
	def m_OnButtonClickImprimir( self, event ):
		event.Skip()
	
	def m_OnButtonClickGuardar( self, event ):
		event.Skip()
	
	def m_OnButtonClickCancelar( self, event ):
		event.Skip()
	

###########################################################################
## Class CerrarCpbteDialogBase
###########################################################################

class CerrarCpbteDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Condiciones de Venta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		self.m_staticText26.SetMinSize( wx.Size( 145,-1 ) )
		
		fgSizer4.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		m_comboBoxTipo_VentaChoices = []
		self.m_comboBoxTipo_Venta = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxTipo_VentaChoices, 0 )
		fgSizer4.Add( self.m_comboBoxTipo_Venta, 0, wx.ALL, 5 )
		
		
		fgSizer4.AddSpacer( ( 25, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"I.Bruto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		fgSizer4.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.m_staticTextI_Bruto = wx.StaticText( self, wx.ID_ANY, u"9999999.99", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextI_Bruto.Wrap( -1 )
		fgSizer4.Add( self.m_staticTextI_Bruto, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Vendedor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		fgSizer4.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		m_comboBoxVendedorChoices = []
		self.m_comboBoxVendedor = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxVendedorChoices, 0 )
		fgSizer4.Add( self.m_comboBoxVendedor, 0, wx.ALL, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticTextIva1 = wx.StaticText( self, wx.ID_ANY, u"IVA 00.0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextIva1.Wrap( -1 )
		fgSizer4.Add( self.m_staticTextIva1, 0, wx.ALL, 5 )
		
		self.m_staticTextI_Iva1 = wx.StaticText( self, wx.ID_ANY, u"9999999.99", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextI_Iva1.Wrap( -1 )
		fgSizer4.Add( self.m_staticTextI_Iva1, 1, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Plazo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		fgSizer4.Add( self.m_staticText33, 0, wx.ALL, 5 )
		
		self.m_textCtrlPlazo = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.m_textCtrlPlazo.SetMinSize( wx.Size( 50,-1 ) )
		
		fgSizer4.Add( self.m_textCtrlPlazo, 0, wx.ALL, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticTextIva2 = wx.StaticText( self, wx.ID_ANY, u"IVA2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextIva2.Wrap( -1 )
		fgSizer4.Add( self.m_staticTextIva2, 0, wx.ALL, 5 )
		
		self.m_staticTextI_Iva2 = wx.StaticText( self, wx.ID_ANY, u"9999999.99", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextI_Iva2.Wrap( -1 )
		fgSizer4.Add( self.m_staticTextI_Iva2, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"Fecha Vencimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer4.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_datePickerF_Vencimiento = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer4.Add( self.m_datePickerF_Vencimiento, 0, wx.ALL, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"I.Neto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		fgSizer4.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.m_staticTextI_Neto = wx.StaticText( self, wx.ID_ANY, u"9999999.99", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextI_Neto.Wrap( -1 )
		fgSizer4.Add( self.m_staticTextI_Neto, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( fgSizer4, 0, 0, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Observaciones", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		self.m_staticText40.SetMinSize( wx.Size( 145,-1 ) )
		
		bSizer14.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlObservaciones = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_textCtrlObservaciones, 1, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bpButtonEmitir = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_fileprint_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer12.Add( self.m_bpButtonEmitir, 0, wx.ALL, 5 )
		
		self.m_bpButtonCancelar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_button_cancel_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer12.Add( self.m_bpButtonCancelar, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		bSizer11.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_bpButtonEmitir.Bind( wx.EVT_BUTTON, self.m_OnButtonEmitir )
		self.m_bpButtonCancelar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickCancelar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnButtonEmitir( self, event ):
		event.Skip()
	
	def m_OnButtonClickCancelar( self, event ):
		event.Skip()
	

###########################################################################
## Class BuscarDialog
###########################################################################

class BuscarDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Buscar por", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer3.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxCamposChoices = []
		self.m_comboBoxCampos = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxCamposChoices, wx.CB_READONLY|wx.CB_SIMPLE )
		self.m_comboBoxCampos.SetMinSize( wx.Size( 250,-1 ) )
		
		fgSizer3.Add( self.m_comboBoxCampos, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlCadena = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlCadena.SetMinSize( wx.Size( 330,-1 ) )
		
		fgSizer3.Add( self.m_textCtrlCadena, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bpButtonBuscar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_find_16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_bpButtonBuscar, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( fgSizer3, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextEncabezado = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextEncabezado.Wrap( -1 )
		self.m_staticTextEncabezado.SetFont( wx.Font( 8, 74, 90, 92, False, "Sans" ) )
		
		bSizer8.Add( self.m_staticTextEncabezado, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		m_listBoxResultadosChoices = []
		self.m_listBoxResultados = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxResultadosChoices, 0 )
		self.m_listBoxResultados.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Droid Sans Mono" ) )
		self.m_listBoxResultados.SetMinSize( wx.Size( 700,400 ) )
		
		bSizer8.Add( self.m_listBoxResultados, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer7.Add( bSizer9, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrlCadena.Bind( wx.EVT_KEY_DOWN, self.m_OnKeyDownCadena )
		self.m_bpButtonBuscar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBuscar )
		self.m_listBoxResultados.Bind( wx.EVT_KEY_DOWN, self.m_OnKeyDownResultados )
		self.m_listBoxResultados.Bind( wx.EVT_LEFT_DCLICK, self.m_OnLeftClickResultados )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnKeyDownCadena( self, event ):
		event.Skip()
	
	def m_OnButtonClickBuscar( self, event ):
		event.Skip()
	
	def m_OnKeyDownResultados( self, event ):
		event.Skip()
	
	def m_OnLeftClickResultados( self, event ):
		event.Skip()
	

###########################################################################
## Class ArticuloPanelBase
###########################################################################

class ArticuloPanelBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.TAB_TRAVERSAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer6 = wx.FlexGridSizer( 0, 5, 5, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"Codigo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		fgSizer6.Add( self.m_staticText47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlCodigo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlCodigo, 0, wx.TOP, 5 )
		
		
		fgSizer6.AddSpacer( ( 100, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Cod.Auxiliar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		fgSizer6.Add( self.m_staticText48, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlCodigoaux = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlCodigoaux, 1, wx.TOP|wx.EXPAND, 5 )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Descripción", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer6.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlDescripcion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlDescripcion.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer6.Add( self.m_textCtrlDescripcion, 0, 0, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Rubro", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		fgSizer6.Add( self.m_staticText49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxRubroChoices = []
		self.m_comboBoxRubro = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxRubroChoices, wx.CB_READONLY )
		fgSizer6.Add( self.m_comboBoxRubro, 0, 0, 5 )
		
		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Proveedor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		fgSizer6.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlCuenta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlCuenta, 0, 0, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Unidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		fgSizer6.Add( self.m_staticText53, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxUnidadChoices = []
		self.m_comboBoxUnidad = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxUnidadChoices, wx.CB_READONLY )
		fgSizer6.Add( self.m_comboBoxUnidad, 0, 0, 5 )
		
		self.m_staticText531 = wx.StaticText( self, wx.ID_ANY, u"Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText531.Wrap( -1 )
		fgSizer6.Add( self.m_staticText531, 0, wx.ALL, 5 )
		
		self.m_textCtrlStock = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlStock, 0, 0, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"Stock Min", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		fgSizer6.Add( self.m_staticText54, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlStockMinimo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlStockMinimo, 0, 0, 5 )
		
		self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"Redondeo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )
		fgSizer6.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlRedondeo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlRedondeo, 0, 0, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"P.Costo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		fgSizer6.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlP_Costo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlP_Costo, 0, 0, 5 )
		
		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Margen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		fgSizer6.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlMargen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlMargen, 0, 0, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Iva", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		fgSizer6.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlT_Iva = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlT_Iva, 0, 0, 5 )
		
		self.m_staticText60 = wx.StaticText( self, wx.ID_ANY, u"P.Venta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		fgSizer6.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlP_Venta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlP_Venta, 0, 0, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"% Rec/Desc 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		fgSizer6.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlReca_Desc1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlReca_Desc1, 0, 0, 5 )
		
		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"% Rec/Desc 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		fgSizer6.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlReca_Desc2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlReca_Desc2, 0, 0, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"% Rec/Desc 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		fgSizer6.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlReca_Desc3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlReca_Desc3, 0, 0, 5 )
		
		self.m_staticText64 = wx.StaticText( self, wx.ID_ANY, u"Modificado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )
		fgSizer6.Add( self.m_staticText64, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlModificado = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrlModificado, 0, 0, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Estado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )
		fgSizer6.Add( self.m_staticText65, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxActivo = wx.CheckBox( self, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_checkBoxActivo, 0, 0, 5 )
		
		
		bSizer16.Add( fgSizer6, 1, 0, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer9.AddSpacer( ( 0, 0), 0, wx.EXPAND, 5 )
		
		self.m_bpButtonPrimero = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_2leftarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonPrimero.SetToolTipString( u"Primero" )
		
		bSizer9.Add( self.m_bpButtonPrimero, 0, wx.ALL, 5 )
		
		self.m_bpButtonAnterior = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_1leftarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonAnterior.SetToolTipString( u"Anterior" )
		
		bSizer9.Add( self.m_bpButtonAnterior, 0, wx.ALL, 5 )
		
		self.m_bpButtonSiguiente = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_player_play_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonSiguiente.SetToolTipString( u"Siguiente" )
		
		bSizer9.Add( self.m_bpButtonSiguiente, 0, wx.ALL, 5 )
		
		self.m_bpButtonUltimo = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_2rightarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonUltimo.SetToolTipString( u"Ultimo" )
		
		bSizer9.Add( self.m_bpButtonUltimo, 0, wx.ALL, 5 )
		
		self.m_bpButtonBuscar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_find_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonBuscar, 0, wx.ALL, 5 )
		
		self.m_bpButtonAgregar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_add_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonAgregar, 0, wx.ALL, 5 )
		
		self.m_bpButtonEditar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonEditar, 0, wx.ALL, 5 )
		
		self.m_bpButtonBorrar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_remove_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonBorrar, 0, wx.ALL, 5 )
		
		self.m_bpButtonGuardar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_apply_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer9.Add( self.m_bpButtonGuardar, 0, wx.ALL, 5 )
		
		self.m_bpButtonDeshacer = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_reload_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonDeshacer.SetToolTipString( u"Deshacer" )
		
		bSizer9.Add( self.m_bpButtonDeshacer, 0, wx.ALL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer16.Add( bSizer9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer16 )
		self.Layout()
		
		# Connect Events
		self.m_bpButtonPrimero.Bind( wx.EVT_BUTTON, self.m_OnButtonClickPrimero )
		self.m_bpButtonAnterior.Bind( wx.EVT_BUTTON, self.m_OnButtonClickAnterior )
		self.m_bpButtonSiguiente.Bind( wx.EVT_BUTTON, self.m_OnButtonClickSiguiente )
		self.m_bpButtonUltimo.Bind( wx.EVT_BUTTON, self.m_OnButtonClickUltimo )
		self.m_bpButtonBuscar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBuscar )
		self.m_bpButtonAgregar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickAgregar )
		self.m_bpButtonEditar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickEditar )
		self.m_bpButtonBorrar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBorrar )
		self.m_bpButtonGuardar.Bind( wx.EVT_BUTTON, self.m_OnButtonGuardar )
		self.m_bpButtonDeshacer.Bind( wx.EVT_BUTTON, self.m_OnButtonDeshacer )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnButtonClickPrimero( self, event ):
		event.Skip()
	
	def m_OnButtonClickAnterior( self, event ):
		event.Skip()
	
	def m_OnButtonClickSiguiente( self, event ):
		event.Skip()
	
	def m_OnButtonClickUltimo( self, event ):
		event.Skip()
	
	def m_OnButtonClickBuscar( self, event ):
		event.Skip()
	
	def m_OnButtonClickAgregar( self, event ):
		event.Skip()
	
	def m_OnButtonClickEditar( self, event ):
		event.Skip()
	
	def m_OnButtonClickBorrar( self, event ):
		event.Skip()
	
	def m_OnButtonGuardar( self, event ):
		event.Skip()
	
	def m_OnButtonDeshacer( self, event ):
		event.Skip()
	

###########################################################################
## Class ImportarPanelBase
###########################################################################

class ImportarPanelBase ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.TAB_TRAVERSAL )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, u"Archivo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )
		fgSizer7.Add( self.m_staticText69, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_filePickerLista = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Seleccione un archivo", u"*.xls", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		self.m_filePickerLista.SetMinSize( wx.Size( 500,21 ) )
		
		fgSizer7.Add( self.m_filePickerLista, 0, wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Hoja", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		fgSizer7.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxHojaChoices = []
		self.m_comboBoxHoja = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxHojaChoices, wx.CB_READONLY )
		self.m_comboBoxHoja.SetSelection( 0 )
		fgSizer7.Add( self.m_comboBoxHoja, 0, wx.ALL, 5 )
		
		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Proveedor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )
		fgSizer7.Add( self.m_staticText65, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlCuenta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_READONLY )
		self.m_textCtrlCuenta.SetMinSize( wx.Size( 150,-1 ) )
		
		bSizer24.Add( self.m_textCtrlCuenta, 0, wx.ALL, 0 )
		
		self.m_bpButtonProveedor = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_find_16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer24.Add( self.m_bpButtonProveedor, 0, wx.RIGHT|wx.LEFT, 5 )
		
		self.m_textCtrlRazon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrlRazon.SetMinSize( wx.Size( 320,-1 ) )
		
		bSizer24.Add( self.m_textCtrlRazon, 0, 0, 5 )
		
		self.m_bpButtonCancelar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_button_cancel_16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer24.Add( self.m_bpButtonCancelar, 0, wx.LEFT, 5 )
		
		
		fgSizer7.Add( bSizer24, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_staticText70 = wx.StaticText( self, wx.ID_ANY, u"Código", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )
		fgSizer7.Add( self.m_staticText70, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxCodigoChoices = [ u"Seleccione Columna...", u"A", u"B", u"C", u"D", u"E", u"F" ]
		self.m_comboBoxCodigo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxCodigoChoices, wx.CB_READONLY )
		self.m_comboBoxCodigo.SetSelection( 0 )
		fgSizer7.Add( self.m_comboBoxCodigo, 0, wx.ALL, 5 )
		
		self.m_staticText66 = wx.StaticText( self, wx.ID_ANY, u"Descripción", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )
		fgSizer7.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxDescripcionChoices = [ u"Seleccione Columna...", u"A", u"B", u"C", u"D", u"E", u"F" ]
		self.m_comboBoxDescripcion = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxDescripcionChoices, wx.CB_READONLY )
		self.m_comboBoxDescripcion.SetSelection( 0 )
		fgSizer7.Add( self.m_comboBoxDescripcion, 0, wx.ALL, 5 )
		
		self.m_staticText84 = wx.StaticText( self, wx.ID_ANY, u"Precio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )
		fgSizer7.Add( self.m_staticText84, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_comboBoxPrecioChoices = [ u"Selecciona Columna...", u"A", u"B", u"C", u"D", u"E", u"F" ]
		self.m_comboBoxPrecio = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxPrecioChoices, wx.CB_READONLY )
		self.m_comboBoxPrecio.SetSelection( 0 )
		bSizer23.Add( self.m_comboBoxPrecio, 0, wx.ALL, 5 )
		
		m_comboBoxTipoPrecioChoices = [ u"Costo", u"Venta" ]
		self.m_comboBoxTipoPrecio = wx.ComboBox( self, wx.ID_ANY, u"Costo", wx.DefaultPosition, wx.Size( 80,-1 ), m_comboBoxTipoPrecioChoices, wx.CB_READONLY )
		self.m_comboBoxTipoPrecio.SetSelection( 0 )
		bSizer23.Add( self.m_comboBoxTipoPrecio, 0, wx.ALL, 5 )
		
		self.m_checkBoxIva = wx.CheckBox( self, wx.ID_ANY, u"Iva Incluído", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxIva.SetValue(True) 
		bSizer23.Add( self.m_checkBoxIva, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer7.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		self.m_bpButtonImportar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_reload_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer7.Add( self.m_bpButtonImportar, 0, wx.ALL, 5 )
		
		
		bSizer18.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_gridPreliminar = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridPreliminar.CreateGrid( 0, 6 )
		self.m_gridPreliminar.EnableEditing( True )
		self.m_gridPreliminar.EnableGridLines( True )
		self.m_gridPreliminar.EnableDragGridSize( False )
		self.m_gridPreliminar.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridPreliminar.EnableDragColMove( False )
		self.m_gridPreliminar.EnableDragColSize( True )
		self.m_gridPreliminar.SetColLabelSize( 20 )
		self.m_gridPreliminar.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridPreliminar.EnableDragRowSize( True )
		self.m_gridPreliminar.SetRowLabelSize( 0 )
		self.m_gridPreliminar.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridPreliminar.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer19.Add( self.m_gridPreliminar, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer18.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer18 )
		self.Layout()
		
		# Connect Events
		self.m_filePickerLista.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_OnFileChangedLista )
		self.m_comboBoxHoja.Bind( wx.EVT_COMBOBOX, self.m_OnComboBoxHoja )
		self.m_textCtrlCuenta.Bind( wx.EVT_KEY_DOWN, self.m_OnKeyDownCuenta )
		self.m_bpButtonProveedor.Bind( wx.EVT_BUTTON, self.m_OnButtonClickProveedor )
		self.m_textCtrlRazon.Bind( wx.EVT_SET_FOCUS, self.m_OnSetFocusRazon )
		self.m_bpButtonCancelar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickCancelar )
		self.m_bpButtonImportar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickImportar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnFileChangedLista( self, event ):
		event.Skip()
	
	def m_OnComboBoxHoja( self, event ):
		event.Skip()
	
	def m_OnKeyDownCuenta( self, event ):
		event.Skip()
	
	def m_OnButtonClickProveedor( self, event ):
		event.Skip()
	
	def m_OnSetFocusRazon( self, event ):
		event.Skip()
	
	def m_OnButtonClickCancelar( self, event ):
		event.Skip()
	
	def m_OnButtonClickImportar( self, event ):
		event.Skip()
	

###########################################################################
## Class LicenciaDialogBase
###########################################################################

class LicenciaDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Licencia", pos = wx.DefaultPosition, size = wx.Size( 357,173 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer9 = wx.FlexGridSizer( 3, 3, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, u"Clave", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )
		self.m_staticText85.SetFont( wx.Font( 12, 74, 90, 90, False, "MS Shell Dlg 2" ) )
		
		fgSizer9.Add( self.m_staticText85, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_textCtrlClave = wx.TextCtrl( self, wx.ID_ANY, u"ABCD-EFHO-OKLM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlClave.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		self.m_textCtrlClave.SetMinSize( wx.Size( 180,-1 ) )
		self.m_textCtrlClave.SetMaxSize( wx.Size( 180,-1 ) )
		
		fgSizer9.Add( self.m_textCtrlClave, 0, wx.ALL, 5 )
		
		self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, u"Código de Validación", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		self.m_staticText86.SetFont( wx.Font( 12, 74, 90, 90, False, "MS Shell Dlg 2" ) )
		
		fgSizer9.Add( self.m_staticText86, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_textCtrlCodigo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlCodigo.SetFont( wx.Font( 12, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		self.m_textCtrlCodigo.SetMinSize( wx.Size( 180,-1 ) )
		self.m_textCtrlCodigo.SetMaxSize( wx.Size( 180,-1 ) )
		
		fgSizer9.Add( self.m_textCtrlCodigo, 0, wx.ALL, 5 )
		
		
		fgSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer24.Add( fgSizer9, 1, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButtonValidar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_apply_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer25.Add( self.m_bpButtonValidar, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButtonCancelar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_button_cancel_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer25.Add( self.m_bpButtonCancelar, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer24.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer24 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_bpButtonValidar.Bind( wx.EVT_BUTTON, self.m_OnButtonValidar )
		self.m_bpButtonCancelar.Bind( wx.EVT_BUTTON, self.m_OnButtonCancelar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnButtonValidar( self, event ):
		event.Skip()
	
	def m_OnButtonCancelar( self, event ):
		event.Skip()
	

