
#copyRight:NamDang
#gmail:Namkeepfire@gmail.com
#Date:30-10-2018
 
import clr
clr.AddReference("RevitAPI")
import  Autodesk
from Autodesk.Revit.DB  import *
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
clr.AddReference('ProToGeometry')
from Autodesk.DesignScript.Geometry import *

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

dataEnteringNode = IN
#-----------------------------------------------------------
element = IN[0] 
para = IN[1]
Error =  []
#-----------------------------------------------------------
def unw(e):
    return UnwrapElement(e)
def paraElement(e):
    return [i.Definition.Name for i in e.Parameters]
def searchPara(e,_para):
    value11 = None
    for i in e.Parameters:
        if i.Definition.Name == _para:
            value11 = i.AsString()
            break
        else:
            continue
    return value11        
def getType(e):
    doc = DocumentManager.Instance.CurrentDBDocument
    try:
        a1 = doc.GetElement(e.GetTypeId())
        return a1
    except Exception:
        pass
        return "Error!"
def listmap1(fun,e):
    return map(lambda x: listmap1(fun,x) if isinstance(x,list) else fun(x),e)
def listmap2(fun,e,value):
    return map(lambda x: listmap2(fun,x,value) if isinstance(x,list) else fun(x,value), e)
def warning(status):
    return '\n'.join('{:^35'.format(i) for i in status.split('\n'))
try:
    Error = None
    ht = []
    if isinstance(element,list):
        element1 = listmap1(unw,element)
        if isinstance(para,list):
            for i in para:
                ht.append(listmap2(searchPara,element1,i)
            ht = map(list,zip(*ht))                 
        else:
            ht = listmap2(searchPara,element1,para)
    else:
        element1 = unw(element)
        if isinstance(para,list):
            for i in para:
                ht.append(listmap2(searchPara,element1,i))
            ht = map(list,zip(*ht0))
        else:
            ht = searchPara(element,para)
except Exception:
    Error = warning("Kiểm tra type biến para \n Kiểm tra danh sách element")
if Error == None:
    OUT = ht
else:
    OUT = Error