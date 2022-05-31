from entidades import * 
a = Vendedor("Gatop2", 2, True)
from entidades2 import * 
b = copiarSqlAlchemy (a, Vendedor)
SESSION.add(b)
#SESSION.commit()

