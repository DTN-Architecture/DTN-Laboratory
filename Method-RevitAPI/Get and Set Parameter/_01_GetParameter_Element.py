import clr
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB  import *
clr.AddReference("RevitServices")
import  RevitServices
from RevitServices.Persistence  import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('ProToGeometry')
from Autodesk.DesignScript.Geometry  import *
clr.AddReference("System")
import System
from System.Collections.Generic     import *
clr.AddReference("RevitNodes")
import Revit 
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

dataEnteringNode = IN

#Function:
def listMap(fun,_e):
    return map(lambda x: listMap(fun,x) if type(x)==list else fun(x),_e)
def une(_e):
    return UnwrapElement(_e)
def paraName(_e):
    return [i.Definition.Name for i in _e.Parameters]
def valuepara(_e):
    return [i.AsValueString() for i in _e.Parameters]
#Input 
element = IN[0]
parameter = IN[1]
outlist = []
familytype = []
#Programming
TransactionManager.Instance.EnsureInTransaction(doc)
for i in UnwrapElement(element):
    for j in i.Parameters:
        if j.IsShared and j.Definition.Name == parameter:
            parameterValue = i.get_Parameter(j.GUID)
            outlist.append(ParameterValue.AsString())
TransactionManager.Instance.TransactionTaskDone()
OUT = outlist

#Luu y:
#+ Phai UnwrapElement doi tuong trong Revit vao python dynamo