#Copyright: NamDang
#Gmail : namkeepfire@gmail.com
#Date: 27-10-2018

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
dataEnteringNode = IN
a = IN[0]
level = UnwrapElement(IN[1])
boolean = IN[2]
p1 = XYZ(0,0,0)
p2 = XYZ(a,0,0)
curve = Line.CreateBound(p1,p2)
def parameter(element):
	return [i.Definition.Name for i in element.Parameters]
def typeElement(_e_):
	try:
		gettype = doc.GetElement(_e_.GetTypeId())
		return gettype
	except Exception:
		pass
		return "Không lấy ra được type của Element"
def warning(status):
	return '\n'.Join('{:^35}'.format(i) for i in status.split('\n'))
TransactionManager.Instance.EnsureInTransaction(doc)
ht = Wall.Create(doc,curve,level.Id,boolean)
ht1 = parameter(ht)
ht2 = typeElement(ht)
TransactionManager.Instance.TransactionTaskDone()
OUT = [ht,ht1,ht2]
