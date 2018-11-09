#Copyright: NamDang
#Gmail : namkeepfire@gmail.com
#Date: 28-10-2018

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("System")
import System
from System.Collections.Generic import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
dataEnteringNode = IN
#Function for list handling
def ProcessList(fun,listElement):
    return map(lambda x: ProcessList(fun,x) if type(x)==list else fun(x),listElement)
#input from dynamo to revit
def unElement(element):
	return UnwrapElement(element)
def torevit(geo):
    return geo.ToRevitType(True)
#function - Parameter and type element
def paraElement(element):
    return [i.Definition.Name for i in element.Parameters]
def getType(_e_):
    try:
        ht = doc.GetElement(_e_.GetTypeId())
    except Exception:
        pass
        return "Error!"
# warning exception
def warning(status):
    return '\n'.Join('{:^35}'.format(i) for i in status.split('\n'))

#Value input 
if isinstance(IN[0],list):
    curve = ProcessList(torevit,IN[0])
else:
    curve = torevit(IN[0])
#curveArray = List[Curve](curve)
level = UnwrapElement(IN[1])
boolean = IN[2]
# Comamnd:
TransactionManager.Instance.EnsureInTransaction(doc)
ht = Wall.Create(doc,curve,level.Id,boolean)
TransactionManager.Instance.TransactionTaskDone()
OUT = ht

