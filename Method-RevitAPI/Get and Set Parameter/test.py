import clr
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB  import *
clr.AddReference("Revitservices")
import Revitservices
from Revitservices.Persistence import DocumentManager
from Revitservices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference('ProToGeometry')
from Autodesk.DesignScript.Geometry import *
import System
from System.Collections.Generic import *
import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
#Nhap khau:-----------------------------------------------
dataEnteringNode = IN
e = IN[0]
paraname = IN[1]

#Function: ------------------------------------------------
def listmap1(fun,e):
    return map(lambda x: listmap1(fun,x) if type(x)==list else fun(x),e)
def listmap2(fun,e,value):
    return map(lambda x: listmap2(fun,x,value) if type(x)==list else fun(e,value),e)
def unw(e):
    return UnwrapElement(e)
def GetBipName(e,paraname = IN[1]):
    e1 = UnwrapElement(e)
    ht = next(i for i in e1.Parameters if i.Definiton.Name == paraname)
    return ht.Definition.BuiltInParameter.ToString()
def GetBipValue(e,bip):
    doc = DocumentManager.Instance.CurrentDBDocument
    valu = e.get_Parameter(bip)
    if e.get_Parameter(bip).StorageType == StorageType.String:
        value = valu.AsString()
    elif valu.StoregeType == StorageType.Integer:
        value = valu.AsInteger
    elif valu.StorageType == StorageType.Double:
        value = valu.AsDouble()
    return value
def GetBuiltInParameter(paraName):
    builtInParameter = System.Enum.GetValues(builtInParameter)
    a = []
    for i in builtInParameter:
        if i.ToString() == paraName:
            a.append(i)
            break
        else:
            continue
    return a[0]
#--------------------------------------------------------------
if isinstance(e,list):
    elements = listmap1(unw,e)
else:
    elements = unw(e)
try:
    errorReport = None 
    ht = []
    if isinstance(elements,list):
        for i in e:
            bips = GetBipName(i,paranaem = IN[1])
            values = GetBipValue(i,bips)
            ht.append(GetBuiltInParameter(values))
    else:
        bips = GetBipName(elements,paraname = IN[1])
        values = GetBipValue(elements,bips)
        ht.append(GetBuiltInParameter(values))
except:
    import traceback
    errorReport = trackback.format_exc()
if errorReport = None:
    OUT = ht 
else: 
    OUT = errorReport 