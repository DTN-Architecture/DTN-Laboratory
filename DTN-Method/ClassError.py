import clr 
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DesignScript.Geometry import *
import sys

dataEnteringNode = IN
class ErrorReport(Exception):
	def __init__(self, status):
		self.s = '\n'.join('{:^40'.format(i) for i in status.split('\n'))
	def print(self):
		return self.s
	def __iter__(self):
		return self
#output
OUT = 0