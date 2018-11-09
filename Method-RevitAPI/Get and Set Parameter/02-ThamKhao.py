#Copyright (c) 2014, Nathan Miller
#The Proving Ground http://theprovingground.org

# Default imports
import clr

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

#The input to this node will be stored in the IN[0] variable.

doc =  DocumentManager.Instance.CurrentDBDocument
app =  DocumentManager.Instance.CurrentUIApplication.Application

elements = UnwrapElement(IN[0])
parameter = IN[1]

values = []
if hasattr(elements, "__iter__"):
	output = []
	for elem in elements:
		if hasattr(elem, "__iter__"):
			vals = []
			for e in elem:
				for p in elem.Parameters:
					if p.Definition.Name == parameter:		
						parm = p.AsValueString()
						if (parm is None):
							parm = p.AsString()
				vals.append(parm)
			values.append(vals)
		else:
			for p in elem.Parameters:
				if p.Definition.Name == parameter:		
					parm = p.AsValueString()
					if (parm is None):
							parm = p.AsString()
			values.append(parm)
	output.append(values)
else:
	parm = 	elements.Parameter[parameter].AsValueString()
	output = parm



#Assign your output to the OUT variable
OUT = output


# SCRIPT2: KONRAD K SONBON
# Copyright(c) 2015, Konrad K Sobon
# @arch_laboratory, http://archi-lab.net

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN

paramNames = IN[1]

if isinstance(IN[0], list):
	elements = []
	for i in IN[0]:
		elements.append(UnwrapElement(i))
else:
	elements = UnwrapElement(IN[0])

def ProcessList(_func, _list):
	return map( lambda x: ProcessList(_func, x) if type(x)==list else _func(x), _list )

def ProcessListArg(_func, _list, _arg):
    return map( lambda x: ProcessListArg(_func, x, _arg) if type(x)==list else _func(x, _arg), _list )

def GetElemType(e):
	doc = DocumentManager.Instance.CurrentDBDocument
	try:
		elemType = doc.GetElement(e.GetTypeId())
		return elemType
	except:
		pass
		return None

def GetParamValue(eType, pName):
	paramValue = None
	for i in eType.Parameters:
		if i.Definition.Name == pName:
			paramValue = i.AsString()
			break
		else:
			continue
	return paramValue

try:
	errorReport = None
	paramValues = []
	if isinstance(elements, list):
		elemTypes = ProcessList(GetElemType, elements)
		if isinstance(paramNames, list):
			for i in paramNames:
				paramValues.append(ProcessListArg(GetParamValue, elemTypes, i))
			paramValues = map(list, zip(*paramValues))
		else:
			paramValues = ProcessListArg(GetParamValue, elemTypes, paramNames)
	else:
		elemTypes = [GetElemType(elements)]
		if isinstance(paramNames, list):
			for i in paramNames:
				paramValues.append(ProcessListArg(GetParamValue, elemTypes, i))
			paramValues = map(list, zip(*paramValues))
		else:
			paramValues = ProcessListArg(GetParamValue, elemTypes, paramNames)
except:
	# if error accurs anywhere in the process catch it
	import traceback
	errorReport = traceback.format_exc()	

#Assign your output to the OUT variable
if errorReport == None:
	OUT = paramValues
else:
	OUT = errorReport