#Copyright: NamDang
#Gmail: namkeepfire@gmail.com
#Date: 29-10-2018

import clr 
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence  import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("System")
import System
from System.Collections.Generic import *
dataEnteringNode = IN
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
#function def.

def unElement(element):
    if isinstance(element,List):
        return [UnwrapElement(i) for i in element]
    else:
        return UnwrapELement(element)
def paraElement(element):
    return [i.Definition.Name for i in element.Parameters]
def getType(_e_):
    try:
        ht = doc.GetElement(_e_.GetTypeId())
    except Exception:
        pass
        return "Error!"
def warning(status):
    return '\n'.Join('{:^35}'.format(i) for i in status.split('\n'))
def ToRevits(geo):
    if isinstance(geo,List):
        return [i.ToRevitType(True) for i in geo]
    else:
        return geo.ToRevitType(True)
def ToRevit(geo):
    return geo.ToRevitType(True)
def ProcessList(fun,listElement):
    return map(lambda x: ProcessList(fun,x) if type(x)==list else fun(x),listElement)
def ToGeodyry(dsObject):
	 #convert DS Line to Revit Line
	 startPt = XYZ(dsObject.StartPoint.X, dsObject.StartPoint.Y, dsObject.StartPoint.Z)
	 endPt = XYZ(dsObject.EndPoint.X, dsObject.EndPoint.Y, dsObject.EndPoint.Z)
	 return Line.CreateBound(startPt, endPt)

curve = UnwrapElement(IN[0])
curves = ToGeodyry(curve)
level = UnwrapElement(IN[1])
boolean = IN[2]
# Comamnd:
TransactionManager.Instance.EnsureInTransaction(doc)
ht = Wall.Create(doc,curves,level.Id,boolean)
TransactionManager.Instance.TransactionTaskDone()
OUT = ht



