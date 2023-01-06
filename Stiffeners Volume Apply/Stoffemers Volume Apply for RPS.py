import clr 
#This is .NET's Common Language Runtime. It's an execution environment
#that is able to execute code from several different languages.

import sys 
#sys is a fundamental Python library - here, we're using it to load in
#the standard IronPython libraries

sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib') #Imports the
#standard IronPython libraries, which cover everything from servers and
#encryption through to regular expressions.

import System #The System namespace at the root of .NET
from System import Array #.NET class for handling array information
from System.Collections.Generic import * #Lets you handle generics. Revit's API
#sometimes wants hard-typed 'generic' lists, called ILists. If you don't need
#these you can delete this line.


clr.AddReference("RevitAPI") #Adding reference to Revit's API DLLs
clr.AddReference("RevitAPIUI") #Adding reference to Revit's API DLLs

import Autodesk #Loads the Autodesk namespace
from Autodesk.Revit.DB import * #Loading Revit's API classes
from Autodesk.Revit.UI import * #Loading Revit's API UI classes  

doc = __revit__.ActiveUIDocument.Document
#__revit__ is a predefined variable 
#A reference to the Autodesk.Revit.Application instance, obtained from the ExternalCommandData aurgument passed to plugins.
#Finally, setting up handles to the active Revit document

app = __revit__.Application
#Setting a handle to the currently-open instance of the Revit application


t = Transaction(doc,"This is a new transaction")

# Place your code below this line
all_stiffeners = FilteredElementCollector(doc)
all_stiffeners.OfCategory(BuiltInCategory.OST_StructuralStiffener)
all_stiffeners.WhereElementIsNotElementType()
allStiffeners = all_stiffeners.ToElements()

Para = []


t.Start()


for i in allStiffeners:
    targetVolume = i.LookupParameter("Stiffener_Volume")
    volume = i.LookupParameter("Volume")
    value = round(volume.AsDouble(),5)
    Para.append(value)
    
    targetVolume.Set(value)




t.Commit()

print(Para)
