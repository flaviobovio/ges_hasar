from wxPython.wx import *
from wxPython.grid import *

class CustomCellChoiceEditor(wxPyGridCellEditor):
    def __init__(self, varDefDict, editable):
        wxPyGridCellEditor.__init__(self)
        self._varDefDict = varDefDict
        self._editable = editable

    def Create(self, parent, id, evtHandler):
        """
        Called to create the control, which must derive from wxControl.
        """
        self._tc = wxChoice(parent, id, choices = self._varDefDict.values())
        if len(self._varDefDict):
            self._tc.SetSelection(0)
        self.SetControl(self._tc)
        if evtHandler:
            self._tc.PushEventHandler(evtHandler)


    def SetSize(self, rect):
        """
        Called to position/size the edit control within the cell rectangle.
        If you don't fill the cell (the rect) then be sure to override
        PaintBackground and do something meaningful there.
        """
        self._tc.SetDimensions(rect.x, rect.y, rect.width+4, rect.height+4,
                               wxSIZE_ALLOW_MINUS_ONE)


    def BeginEdit(self, row, col, grid):
        """
        Fetch the value from the table and prepare the edit control
        to begin editing.  Set the focus to the edit control.
        """
        self.startValue = grid.GetTable().GetValue(row, col)
        self._tc.SetStringSelection(self._varDefDict[self.startValue])
        self._tc.SetFocus()


    def EndEdit(self, row, col, grid):
        """
        Complete the editing of the current cell. Returns true if the value
        has changed.  If necessary, the control may be destroyed.
        """
        changed = false

        pclDescr = self._tc.GetStringSelection()
        # extract pcl
        pcl = pclDescr.split('    ')[0]
        if pcl != self.startValue :
            changed = true
            grid.GetTable().SetValue(row, col, pcl) # update the table

        self.startValue = ''
        return changed


    def Reset(self):
        """
        Reset the value in the control back to its starting value.
        """
        self._tc.SetStringSelection(self._varDefDict[self.startValue])


    def Clone(self):
        """
        Create a new object which is the copy of this one
        """
        return CustomCellChoiceEditor(self._varDefDict, self._editable)

#---------------------------------------------------------------------------

class TestFrame(wxFrame):
    def __init__(self, parent):
        wxFrame.__init__(self, parent, -1, "Custom Grid Cell Editor Test",
                         size=(400,120))
        grid = wxGrid(self, 2001, size = wxSize(360, 80))
        grid.CreateGrid(2, 2)
        grid.SetColLabelValue(0, 'Col 1')
        grid.SetColLabelValue(1, 'Col 2')
        grid.SetColLabelAlignment(wxALIGN_CENTRE, wxALIGN_CENTRE)
        grid.SetColSize(1, 280)
        grid.SetRowLabelSize(0)
        grid.SetCellValue(1, 1, 'A')
        dict = {'A':'A    Description_of_A', 'B':'B    Description_of_B'}
        grid.SetCellEditor(1, 1, CustomCellChoiceEditor(dict, true))


#---------------------------------------------------------------------------

if __name__ == '__main__':
    import sys
    app = wxPySimpleApp()
    frame = TestFrame(None)
    frame.Show(true)
    app.MainLoop()