#
# 2222222222222222222222222222222222222222222222222222222222222222222222222222222
#
from sqlalchemy import *
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


BASE = declarative_base()
DATABASE = create_engine('mysql+mysqldb://weberp:weberp@192.168.9.11/gestion')
DATABASE.echo = False
METADATA = MetaData(DATABASE)
SESSIONCLASS = sessionmaker(bind=DATABASE)
SESSION = SESSIONCLASS()


#
#       COMUNES 2
#

class Vendedor(BASE):
    __tablename__ = 'vendedores'
    id = Column(Integer, primary_key=True)
    nombre = Column(VARCHAR(15))
    comision = Column(Float)
    activo = Column(Boolean)
    def __init__(self, nombre, comision, activo):
        self.nombre = nombre
        self.comision = comision
        self.activo = activo
    def __repr__(self):
            return "<Vendedor('%s','%s','%s')>" % (self.nombre, self.comision, self.activo)


class Tipo_Venta(BASE):
    __tablename__ = 'tipos_venta'
    id = Column(Integer, primary_key=True)
    tipo = Column(VARCHAR(15))
    cta_cte = Column(Boolean)
    plazo = Column(Integer)
    def __init__(self, tipo, cta_cte, plazo):
        self.tipo = tipo
        self.cta_cte = cta_cte
        self.plazo = plazo
    def __repr__(self):
            return "<Tipo_Venta('%s','%s','%s')>" % (self.tipo, self.cta_cte, self.plazo)





class Iva(BASE):
    __tablename__ = 'iva'
    id = Column(Integer, primary_key=True)
    situacion = Column(VARCHAR(15))
    abreviacion = Column(VARCHAR(1))
    cuit = Column(Boolean)
    discrimina = Column(Boolean)
    comprobante = Column(VARCHAR(1))
    def __init__(self, situacion, abreviacion, cuit, discrimina, comprobante):
        self.situacion = situacion
        self.abreviacion = abreviacion
        self.cuit = cuit
        self.discrimina = discrimina        
        self.comprobante = comprobante
    def __repr__(self):
            return "<Iva('%s','%s','%s','%s','%s')>" % (self.situacion, self.abreviacion, self.cuit, self.discrimina, self.comprobante)




class Cliente(BASE):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    cuenta = Column(VARCHAR(10))
    razon = Column(VARCHAR(50))
    cuit = Column(VARCHAR(11))
    direccion = Column(VARCHAR(50))
    localidad = Column(VARCHAR(50))
    cp = Column(VARCHAR(8))
    provincia = Column(VARCHAR(20))
    id_iva = Column(Integer, ForeignKey('iva.id'))
    telefono = Column(VARCHAR(50))
    fax = Column(VARCHAR(50))
    web = Column(VARCHAR(50))
    email = Column(VARCHAR(50))
    id_vendedor = Column(Integer, ForeignKey('vendedores.id'))
    credito = Column(Float)
    id_tipo_venta = Column(Integer,  ForeignKey('tipos_venta.id'))
    observaciones = Column(VARCHAR(150))
    fecha_alta = Column(Date)
    activo = Column(Boolean)

    iva = relationship("Iva")
    vendedor = relationship("Vendedor")
    tipo_venta = relationship("Tipo_Venta")
    

    def __init__(self, cuenta, razon, cuit, direccion, localidad, cp, provincia, id_iva, telefono, fax, web, email, id_vendedor, credito, id_tipo_venta, observaciones, fecha_alta, activo):
        self.cuenta = cuenta
        self.razon = razon
        self.cuit = cuit
        self.direccion = direccion
        self.localidad = localidad
        self.cp = cp
        self.provincia = provincia
        self.id_iva = id_iva
        self.telefono = telefono
        self.fax = fax
        self.web = web
        self.email = email
        self.id_vendedor = id_vendedor
        self.credito = credito
        self.id_tipo_venta = id_tipo_venta
        self.observaciones = observaciones
        self.fecha_alta = fecha_alta
        self.activo = activo
    def __repr__(self):
            return "<Cliente('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.cuenta, self.razon, self.cuit, self.direccion, self.localidad, self.cp, self.provincia, self.id_iva, self.telefono, self.fax, self.web, self.email, self.id_vendedor, self.credito, self.id_tipo_venta, self.observaciones, self.fecha_alta, self.activo)

class Articulo(BASE):
    __tablename__ = 'articulos'
    id = Column(Integer, primary_key=True)
    codigo = Column(VARCHAR(18))
    codigoaux = Column(VARCHAR(18))
    id_rubro = Column(Integer, ForeignKey('rubros.id'))    
    descripcion = Column(VARCHAR(50))
    stock = Column(Float)
    stockminimo = Column(Float)
    redondeo = Column(Float)
    p_costo = Column(Float)
    margen = Column(Float)
    t_iva = Column(Float)
    p_venta = Column(Float)
    descuento1 = Column(Float)
    descuento2 = Column(Float)
    descuento3 = Column(Float)
    modificado = Column(Date)
    activo = Column(Boolean)

    def __init__(self, codigo, codigoaux, id_rubro, descripcion, stock, stockminimo, redondeo, p_costo, margen, \
        t_iva, p_venta, descuento1, descuento2, descuento3, modificado, activo):
        self.codigo = codigo
        self.codigoaux = codigoaux
        self.id_rubro = id_rubro
        self.descripcion = descripcion
        self.stock = stock
        self.stockminimo = stockminimo
        self.redondeo = redondeo
        self.p_costo = p_costo
        self.margen = margen
        self.t_iva = t_iva
        self.p_venta = p_venta
        self.descuento1 = descuento1
        self.descuento2 = descuento2
        self.descuento3 = descuento3
        self.modificado = modificado
        self.activo = activo
    def __repr__(self):
            return "<articulo('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" \
            % (self.codigo, self.codigoaux, self.id_rubro, self.descripcion, self.stock, self.stockminimo, self.redondeo, \
                self.p_costo, self.margen, self.t_iva, self.p_venta, self.descuento1, self.descuento2, self.descuento3, \
                self.modificado, self.activo)

class Rubro(BASE):
    __tablename__ = 'rubros'
    id = Column(Integer, primary_key=True)
    rubro = Column(VARCHAR(20))
    def __init__(self, rubro):
        self.rubro = rubro
    def __repr__(self):
            return "<Rubro('%s')>" % (self.rubro)
        
        
        
        
#
#       COMPROBANTES
#

class Factura(BASE):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    t_cpbte = Column(VARCHAR(1))
    n_cpbte = Column(VARCHAR(12))
    f_cpbte = Column(Date)
    n_remito = Column(VARCHAR(12))
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    razon = Column(VARCHAR(50))
    i_bruto = Column(Float)
    i_descuento = Column(Float)
    i_iva1 = Column(Float)    
    i_iva2 = Column(Float)    
    i_iva3 = Column(Float)        
    i_neto = Column(Float)        
    id_vendedor = Column(Integer, ForeignKey('vendedores.id'))
    f_vencimiento = Column(Date)
    estado = Column(VARCHAR(1))           
    id_tipo_venta = Column(Integer,  ForeignKey('tipos_venta.id'))
    d_factura = relationship("d_Factura", backref="Factura")    
    cliente = relationship("Cliente") 
    vendedor = relationship("Vendedor")
    tipo_venta = relationship("Tipo_Venta")    

    def __init__(self):
        pass

    def __repr__(self):
            return "<Factura('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" \
            % (self.t_cpbte, self.n_cpbte, self.f_cpbte, self.n_remito, self.id_cliente, self.razon, \
            self.i_bruto, self.i_descuento, self.i_iva1, self.i_iva2, self.i_iva3, self.i_neto, \
            self.id_vendedor, self.f_vencimiento, self.estado, self.id_tipo_venta)
            
            
class d_Factura(BASE):
    __tablename__ = 'd_facturas'
    id = Column(Integer, primary_key=True)
    id_factura = Column(Integer, ForeignKey('facturas.id'))      
    id_articulo = Column(Integer, ForeignKey('articulos.id'))
    cantidad = Column(Float)
    t_iva = Column(Float)    
    precio = Column(Float)   
    articulo = relationship("Articulo")        


    def __init__(self, id_factura, id_articulo, cantidad, t_iva, precio):
        self.id_factura = id_factura
        self.id_articulo = id_articulo
        self.cantidad = cantidad
        self.t_iva = t_iva 
        self.precio = precio
    def __repr__(self):
            return "<d_Factura('%s','%s','%s','%s','%s')>" \
            % (self.id_factura, self.id_articulo, self.cantidad, self.t_iva, self.precio )            
        


#
#       COMPROBANTES 2
#

class Factura2(BASE):
    __tablename__ = 'facturas2'
    id = Column(Integer, primary_key=True)
    t_cpbte = Column(VARCHAR(1))
    n_cpbte = Column(VARCHAR(12))
    f_cpbte = Column(Date)
    n_remito = Column(VARCHAR(12))
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    razon = Column(VARCHAR(50))
    i_bruto = Column(Float)
    i_descuento = Column(Float)
    i_iva1 = Column(Float)    
    i_iva2 = Column(Float)    
    i_iva3 = Column(Float)        
    i_neto = Column(Float)        
    id_vendedor = Column(Integer, ForeignKey('vendedores.id'))
    f_vencimiento = Column(Date)
    estado = Column(VARCHAR(1))           
    id_tipo_venta = Column(Integer,  ForeignKey('tipos_venta.id'))
    d_factura = relationship("d_Factura2", backref="Factura2")    
    cliente = relationship("Cliente") 
    vendedor = relationship("Vendedor")
    tipo_venta = relationship("Tipo_Venta")    

    def __init__(self, t_cpbte, n_cpbte, f_cpbte, n_remito, id_cliente, razon, i_bruto, i_descuento, i_iva1,\
                    i_iva2, i_iva3, i_neto, id_vendedor, f_vencimiento, estado, id_tipo_venta):
        self.t_cpbte = t_cpbte 
        self.n_cpbte = n_cpbte 
        self.f_cpbte = f_cpbte 
        self.n_remito = n_remito 
        self.id_cliente = id_cliente
        self.razon = razon 
        self.i_bruto = i_bruto
        self.i_descuento = i_descuento 
        self.i_iva1 = i_iva1 
        self.i_iva2 = i_iva2 
        self.i_iva3 = i_iva3 
        self.i_neto = i_neto 
        self.id_vendedor = id_vendedor 
        self.f_vencimiento = f_vencimiento 
        self.estado = estado
        self.id_tipo_venta = id_tipo_venta

    def __repr__(self):
            return "<Factura2('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" \
            % (self.t_cpbte, self.n_cpbte, self.f_cpbte, self.n_remito, self.id_cliente, self.razon, \
            self.i_bruto, self.i_descuento, self.i_iva1, self.i_iva2, self.i_iva3, self.i_neto, \
            self.id_vendedor, self.f_vencimiento, self.estado, self.id_tipo_venta)
            
            
class d_Factura2(BASE):
    __tablename__ = 'd_facturas2'
    id = Column(Integer, primary_key=True)
    id_factura = Column(Integer, ForeignKey('facturas2.id'))      
    id_articulo = Column(Integer, ForeignKey('articulos.id'))
    cantidad = Column(Float)
    t_iva = Column(Float)    
    precio = Column(Float)   
    articulo = relationship("Articulo")        


    def __init__(self, id_factura, id_articulo, cantidad, t_iva, precio):
        self.id_factura = id_factura
        self.id_articulo = id_articulo
        self.cantidad = cantidad
        self.t_iva = t_iva 
        self.precio = precio
    def __repr__(self):
            return "<d_Factura2('%s','%s','%s','%s','%s')>" \
            % (self.id_factura, self.id_articulo, self.cantidad, self.t_iva, self.precio )            













#       Crear Tablas
#BASE2.metadata.create_all(DATABASE2) 



def copiarSqlAlchemy(obj, clase): # copia un objeto de SQLAlchemy - Parametros (SqlAlchemyObj, SqlAlchemyClass)
    n = 0
    obj2 = ""
    for i in obj.__table__.columns:
        if n >= 1:
            if n >=2:
                obj2 += ","           
            array = str(i).split(".")
            valor = eval("obj."+array[1])
            valor = '"' + str(valor) + '"'
            obj2 +=  valor
        n += 1
        
    ret = None
    try:
        ret = eval(clase.__name__+"("+obj2+")")
    except:
        print "Error, no se puede copiar objecto ",
        print obj, 
        print ", Clase ",
        print clase
   
    return ret

def copiarFactura12(obj):
    obj2 = copiarSqlAlchemy(obj, Factura2)
    for det in obj.d_factura:
        det2 = copiarSqlAlchemy(det, d_Factura2)
        obj2.d_factura.append(det2)

    return obj2