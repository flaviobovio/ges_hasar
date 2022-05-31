import gui
import MySQLdb
from entidades import Cliente
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker



# To change this template, choose Tools | Templates
# and open the template in the editor.

class Factura ( gui.FacturaPanel ):
    def __init__( self, parent ):
        gui.FacturaPanel.__init__( self, parent )




	db = create_engine('mysql+mysqldb://root:aaaaaa@192.168.9.13/gestion')
	db.echo = False  # Try changing this to True and see what happens

	metadata = MetaData(db)
	Base = declarative_base()
	Session = sessionmaker(bind=db)
	session = Session()


        self.m_comboBoxCliente.Clear()
        for row in session.query(Cliente):
            print row.nombre
            self.m_comboBoxCliente.Append(row.nombre)


