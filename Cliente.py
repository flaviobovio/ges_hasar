import gui
import MySQLdb
from entidades import *
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker



# To change this template, choose Tools | Templates
# and open the template in the editor.

class Cliente ( gui.ClientePanel ):
	def __init__( self, parent ):
		gui.ClientePanel.__init__( self, parent )


		db = create_engine('mysql+mysqldb://root:aaaaaa@192.168.9.13/gestion')
		db.echo = False  # Try changing this to True and see what happens

		metadata = MetaData(db)
		Base = declarative_base()
		Session = sessionmaker(bind=db)
		session = Session()

	        for row in session.query(Iva):
			self.m_comboBoxIva.Append(row.situacion, row)
	        for row in session.query(Vendedor):
			self.m_comboBoxVendedor.Append(row.nombre, row)
	        for row in session.query(Tipo_Venta):
			self.m_comboBoxTipo_Venta.Append(row.tipo, row)

	def m_OnSaveButtonClick( self, event ):

		print "Activo ---------"
		print self.m_checkBoxActivo.GetValue()

		cli = Cliente (self.m_textCtrlCuenta.GetValue(),\
		self.m_textCtrlRazon.GetValue(),\
		self.m_textCtrlCuit.GetValue(),\
		self.m_textCtrlDireccion.GetValue(),\
		self.m_textCtrlLocalidad.GetValue(),\
		self.m_textCtrlCp.GetValue(),\
		self.m_textCtrlProvincia.GetValue(),\
		self.m_comboBoxIva.GetClientData(self.m_comboBoxIva.GetSelection()).id,\
		self.m_textCtrlTelefono.GetValue(),\
		self.m_textCtrlFax.GetValue(),\
		self.m_textCtrlWeb.GetValue(),\
		self.m_textCtrlEmail.GetValue(),\
		self.m_comboBoxVendedor.GetClientData(self.m_comboBoxVendedor.GetSelection()).id,\
		self.m_spinCtrlCredito.GetValue(),\
		self.m_comboBoxTipo_Venta.GetClientData(self.m_comboBoxTipo_Venta.GetSelection()).id,\
		self.m_richTextObservaciones.GetValue(),\
		datetime.date.today(),\
		self.m_checkBoxActivo.GetValue())

