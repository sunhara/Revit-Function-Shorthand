import clr 
#This is .NET's Common Language Runtime. It's an execution environment
#that is able to execute code from several different languages.

import sys 
#sys is a fundamental Python library - here, we're using it to load in
#the standard IronPython libraries
import System #The System namespace at the root of .NET
from System import Array #.NET class for handling array information
from System.Collections.Generic import * #Lets you handle generics. Revit's API
#sometimes wants hard-typed 'generic' lists, called ILists. If you don't need
#these you can delete this line.

clr.AddReference("RevitNodes") #Dynamo's nodes for Revit

import Revit #Loads in the Revit namespace in RevitNodes
clr.ImportExtensions(Revit.Elements) #More loading of Dynamo's Revit libraries
clr.ImportExtensions(Revit.GeometryConversion) #More loading of Dynamo's
#Revit libraries. You'll only need this if you're interacting with geometry.
clr.AddReference("RevitServices") #Dynamo's classes for handling Revit documents

import RevitServices 
from RevitServices.Persistence import DocumentManager #An internal Dynamo class
#that keeps track of the document that Dynamo is currently attached to
from RevitServices.Transactions import TransactionManager #A Dynamo class for
#opening and closing transactions to change the Revit document's database

clr.AddReference("RevitAPI") #Adding reference to Revit's API DLLs
clr.AddReference("RevitAPIUI") #Adding reference to Revit's API DLLs

import Autodesk #Loads the Autodesk namespace
from Autodesk.Revit.DB import * #Loading Revit's API classes
from Autodesk.Revit.UI import * #Loading Revit's API UI classes  




app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc,"Start a new Transaction")


def createList(r1, r2):
    return list(range(r1, r2+1))
     


# Place your code below this line
all_Sheets = FilteredElementCollector(doc)
all_Sheets.OfCategory(BuiltInCategory.OST_Sheets)
all_Sheets.WhereElementIsNotElementType()
all_Sheets_Ele = all_Sheets.ToElements()

indicat = all_Sheets_Ele[0].LookupParameter("Sheet Number").AsString()
indicator = indicat.startswith("FB")

sheetsNum = []

for i in all_Sheets_Ele:
    num = i.LookupParameter("Sheet Number")
       
    numValue = num.AsString()
    
    if  indicator:
        numValue1 = numValue.strip("FB") 
        
        sheetsNum.append(float(numValue1))
    else:
        sheetsNum.append(float(numValue))


# Get the sheets number as index
indices = sorted(range(len(sheetsNum)), key = lambda index: sheetsNum[index])
renumber = createList(1,len(indices))  #rename with the renumber


t.Start()

for i,j in zip(indices,renumber):
     num2 = all_Sheets_Ele[i].LookupParameter("Sheet Number")
     numstr = str(j)
     
     if indicator:
        num2.Set(numstr)
     else:
        num2.Set("FB"+numstr)
     

t.Commit()
# Assign your output to the OUT variable.
print( indicator,indicat,sheetsNum)
