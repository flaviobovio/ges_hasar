def CaracterNatural(key):
	acceptable_characters = "1234567890"	
	# 13 = enter, 314 & 316 = arrows, 8 = backspace, 127 = del, 9 = tab, incio 313, fin 312
	otras = [13, 314, 316, 8, 127, 9, 313, 312] 
	tecla_valida = key in otras or (key < 256 and chr(key) in acceptable_characters)
	return tecla_valida

def CaracterEntero(key):
	acceptable_characters = "1234567890-"	
	# 13 = enter, 314 & 316 = arrows, 8 = backspace, 127 = del, 9 = tab, incio 313, fin 312
	otras = [13, 314, 316, 8, 127, 9, 313, 312] 
	tecla_valida = key in otras or (key < 256 and chr(key) in acceptable_characters)
	return tecla_valida

def CaracterDecimal(key):
	acceptable_characters = "1234567890.-"	
	# 13 = enter, 314 & 316 = arrows, 8 = backspace, 127 = del, 9 = tab, incio 313, fin 312
	otras = [13, 314, 316, 8, 127, 9, 313, 312] 
	tecla_valida = key in otras or (key < 256 and chr(key) in acceptable_characters)
	return tecla_valida

def FechaDatePicker (fecha):
	import wx
	#Devuelve una fecha tipo Date como wx.DateTime 
	ano,mes,dia = str(fecha).split('-')
	return wx.DateTimeFromDMY (int(dia),int(mes)-1,int(ano))

def DatePickerFecha (fecha):
	import datetime.date
	#Devuelve una fecha tipo wx.DateTime como Date 
	ano,mes,dia = str(fecha).split('-')
	return date(int(ano),int(mes),int(dia))

	
