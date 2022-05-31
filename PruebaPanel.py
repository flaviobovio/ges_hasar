import gui
import wx
import  wx.grid as gridlib
from datetime import datetime


class PruebaPanel ( gui.PruebaPanelBase):
   
    def __init__( self, parent ):
        gui.PruebaPanelBase.__init__( self, parent )


        table = CustomDataTable()

        # The second parameter means that the grid is to take ownership of the
        # table and will destroy it when done.  Otherwise you would need to keep
        # a reference to it and call it's Destroy method later.
        self.m_grid.SetTable(table, True)        
        self.m_grid.SetRowLabelSize(20)
        self.m_grid.SetMargins(0,0)
        self.m_grid.AutoSizeColumns(False)
        self.m_grid.SetColSize( 0, 90 )
        self.m_grid.SetColSize( 1, 100 )
        self.m_grid.SetColSize( 2, 182 )
        self.m_grid.SetColSize( 3, 90 )
        self.m_grid.SetColSize( 4, 186 )
        self.m_grid.SetColSize( 5, 100 )
        
    def m_OnKeyDownDetalle( self, event ):       
        key = event.GetKeyCode() 
        if key == 13 or key == 370:  #Enter
            self.m_grid.DisableCellEditControl()
            row = self.m_grid.GetGridCursorRow()
            col = self.m_grid.GetGridCursorCol()
            cel = self.m_grid.GetCellValue(row, col)
            if col == 1:
                if cel == "":
                    self.m_grid.SetGridCursor(row, 5)
                else:
                    try:
                        datetime.strptime(cel, "%d/%m/%y")
                    except ValueError:
                        wx.MessageBox("Ingrese una fecha en formato dd/mm/aa",style=wx.ICON_ERROR)
                        self.m_grid.SetGridCursor( row, 0)                         
                        #self.m_grid.EnableCellEditControl()
                
            if col < 5:
                self.m_grid.MoveCursorRight(False)
            else:              
                self.m_grid.SetGridCursor( min(row+1, 9), 0) 
        elif key == 9:  #Tab
            self.m_bpButtonOk.SetFocus()        
        elif key == 127:  #Del
            row = self.m_grid.GetGridCursorRow()        
            self.m_grid.DeleteRows(row, 1)            
            self.m_grid.AppendRows(1)                        
        else:
            event.Skip()
        
        
        







class CustomDataTable(gridlib.PyGridTableBase):

    def __init__(self):
        gridlib.PyGridTableBase.__init__(self)


        self.colLabels = ['', 'Fecha', 'Banco', 'Numero', 'Plaza', 'Importe']


        self.dataTypes = [gridlib.GRID_VALUE_STRING,
                          gridlib.GRID_VALUE_STRING,
                          gridlib.GRID_VALUE_STRING,
                          gridlib.GRID_VALUE_STRING,                        
                          gridlib.GRID_VALUE_STRING,
                          gridlib.GRID_VALUE_FLOAT + ':6,2',
                          ]
        self.data = [ 
            ["Cheque/Tarjeta", "01/07/2011", "Bnaco de cek adasd major", "       ", 'Venado Tuerto SF', 0], 
            ["","","", "","", 0],
            ["","","", "","", 0],
            ["","","", "","", 0]          
            ]
        


    #--------------------------------------------------
    # required methods for the wxPyGridTableBase interface

    def GetNumberRows(self):
        return len(self.data) + 1

    def GetNumberCols(self):
        return len(self.data[0])

    def IsEmptyCell(self, row, col):
        try:
            return not self.data[row][col]
        except IndexError:
            return True

    # Get/Set values in the table.  The Python version of these
    # methods can handle any data-type, (as long as the Editor and
    # Renderer understands the type too,) not just strings as in the
    # C++ version.
    def GetValue(self, row, col):
        try:
            return self.data[row][col]
        except IndexError:
            return ''

    def SetValue(self, row, col, value):
        #def innerSetValue(row, col, value):
        #    try:
        #        print value
        #        self.data[row][col] = value
        #        print "despus"
        #    except IndexError:
        #        if self.GetNumberRows() < 4:
        #            print "agrega"
        #            # add a new row
        #            self.data.append([''] * self.GetNumberCols())
        #            innerSetValue(row, col, value)

        #            # tell the grid we've added a row
        #            msg = gridlib.GridTableMessage(self,        # The table
        #                gridlib.GRIDTABLE_NOTIFY_ROWS_APPENDED, # what we did to it
        #                1                                       # how many
        #                )

        #            self.GetView().ProcessTableMessage(msg)
        #innerSetValue(row, col, value) 
        try:
            self.data[row][col] = value
            print self.data
        except:
            print "Error"

    #--------------------------------------------------
    # Some optional methods

    # Called when the grid needs to display labels
    def GetColLabelValue(self, col):
        return self.colLabels[col]

    # Called to determine the kind of editor/renderer to use by
    # default, doesn't necessarily have to be the same type used
    # natively by the editor/renderer if they know how to convert.
    def GetTypeName(self, row, col):
        return self.dataTypes[col]

    # Called to determine how the data can be fetched and stored by the
    # editor and renderer.  This allows you to enforce some type-safety
    # in the grid.
    def CanGetValueAs(self, row, col, typeName):
        colType = self.dataTypes[col].split(':')[0]
        if typeName == colType:
            return True
        else:
            return False

    def CanSetValueAs(self, row, col, typeName):
        return self.CanGetValueAs(row, col, typeName)
