#!/usr/bin/env python  
#-*- coding: latin-1 -*-

import os
from entidades import *
from xlrd import open_workbook
from datetime import date




wb = open_workbook('../Oriental/castelli.xls')
print wb.sheets().
for s in wb.sheets():

    print 'Sheet:',s.name
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)           
        
        art = None
        print values[1].encode('latin-1')
        if type(values[3]).__name__ == 'float':  
            art =  Articulo(values[0], 0, 0, values[1], 0, 0, 0, values[3], 25, \
                21, 0, 0, 0, 0, date.today(), True)
            #SESSION.add(art)
            #SESSION.commit()




