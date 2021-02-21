# Misc    

## Properties  
### Misc.SharedScriptData 
## Methods  
### Misc.Beep
```py
Misc.Beep()```
### Misc.CancelPrompt
```py
Misc.CancelPrompt()```
### Misc.CaptureNow
```py
Misc.CaptureNow()```
### Misc.CheckIgnoreObject
```py
Misc.CheckIgnoreObject(Int32 s)
- Int32 **s** ____```
### Misc.CheckIgnoreObject
```py
Misc.CheckIgnoreObject(Mobile m)
- Mobile **m** ____```
### Misc.CheckIgnoreObject
```py
Misc.CheckIgnoreObject(Item i)
- Item **i** ____```
### Misc.CheckSharedValue
```py
Misc.CheckSharedValue(String name)
- String **name** ____```
### Misc.ClearIgnore
```py
Misc.ClearIgnore()```
### Misc.CloseBackpack
```py
Misc.CloseBackpack()```
### Misc.CloseMenu
```py
Misc.CloseMenu()```
### Misc.ContextReply
```py
Misc.ContextReply(Int32 serial, String menuname)
- Int32 **serial** ____
- String **menuname** ____```
### Misc.ContextReply
```py
Misc.ContextReply(Item item, String menuname)
- Item **item** ____
- String **menuname** ____```
### Misc.ContextReply
```py
Misc.ContextReply(Mobile mob, String menuname)
- Mobile **mob** ____
- String **menuname** ____```
### Misc.ContextReply
```py
Misc.ContextReply(Item item, Int32 idx)
- Item **item** ____
- Int32 **idx** ____```
### Misc.ContextReply
```py
Misc.ContextReply(Mobile mob, Int32 idx)
- Mobile **mob** ____
- Int32 **idx** ____```
### Misc.ContextReply
```py
Misc.ContextReply(Int32 serial, Int32 idx)
- Int32 **serial** ____
- Int32 **idx** ____```
### Misc.CurrentScriptDirectory
```py
Misc.CurrentScriptDirectory()```
### Misc.Disconnect
```py
Misc.Disconnect()```
### Misc.DistanceSqrt
```py
Misc.DistanceSqrt(Point3D a, Point3D b)
- Point3D **a** ____
- Point3D **b** ____```
### Misc.Equals
```py
Misc.Equals(Object obj)
- Object **obj** ____```
### Misc.ExportPythonAPI
```py
Misc.ExportPythonAPI(String path, Boolean pretty)
- String **path** ____
- Boolean **pretty** __True__```
Return a string containing list RE Python API list in JSON format.
### Misc.FocusUOWindow
```py
Misc.FocusUOWindow()```
### Misc.GetContPosition
```py
Misc.GetContPosition()```
### Misc.GetHashCode
```py
Misc.GetHashCode()```
### Misc.GetMapInfo
```py
Misc.GetMapInfo(UInt32 serial)
- UInt32 **serial** ____```
### Misc.GetMenuTitle
```py
Misc.GetMenuTitle()```
### Misc.GetType
```py
Misc.GetType()```
### Misc.HasMenu
```py
Misc.HasMenu()```
### Misc.HasPrompt
```py
Misc.HasPrompt()```
### Misc.HasQueryString
```py
Misc.HasQueryString()```
### Misc.IgnoreObject
```py
Misc.IgnoreObject(Item i)
- Item **i** ____```
### Misc.IgnoreObject
```py
Misc.IgnoreObject(Mobile m)
- Mobile **m** ____```
### Misc.IgnoreObject
```py
Misc.IgnoreObject(Int32 s)
- Int32 **s** ____```
### Misc.LastHotKey
```py
Misc.LastHotKey()```
Returns the latest HotKeyEvent recorded by razor.
The HotKeyEvent has 2 properties:
hke.Key: enum System.Windows.Forms.Keys
hke.Timestamp: double repesenting the UnixTimestamp, compatible with python's time.time()
### Misc.MenuContain
```py
Misc.MenuContain(String submenu)
- String **submenu** ____```
### Misc.MenuResponse
```py
Misc.MenuResponse(String submenu)
- String **submenu** ____```
### Misc.MouseLocation
```py
Misc.MouseLocation()```
### Misc.MouseMove
```py
Misc.MouseMove(Int32 posX, Int32 posY)
- Int32 **posX** ____
- Int32 **posY** ____```
### Misc.NextContPosition
```py
Misc.NextContPosition(Int32 x, Int32 y)
- Int32 **x** ____
- Int32 **y** ____```
### Misc.NoOperation
```py
Misc.NoOperation()```
### Misc.NoRunStealthStatus
```py
Misc.NoRunStealthStatus()```
### Misc.NoRunStealthToggle
```py
Misc.NoRunStealthToggle(Boolean enable)
- Boolean **enable** ____```
### Misc.Pause
```py
Misc.Pause(Int32 mseconds)
- Int32 **mseconds** ____```
### Misc.PetRename
```py
Misc.PetRename(Int32 serial, String name)
- Int32 **serial** ____
- String **name** ____```
### Misc.PetRename
```py
Misc.PetRename(Mobile mob, String name)
- Mobile **mob** ____
- String **name** ____```
### Misc.QueryStringResponse
```py
Misc.QueryStringResponse(Boolean okcancel, String response)
- Boolean **okcancel** ____
- String **response** ____```
### Misc.ReadSharedValue
```py
Misc.ReadSharedValue(String name)
- String **name** ____```
### Misc.RemoveSharedValue
```py
Misc.RemoveSharedValue(String name)
- String **name** ____```
### Misc.ResetPrompt
```py
Misc.ResetPrompt()```
### Misc.ResponsePrompt
```py
Misc.ResponsePrompt(String text)
- String **text** ____```
### Misc.Resync
```py
Misc.Resync()```
### Misc.ScriptRun
```py
Misc.ScriptRun(String scriptfile)
- String **scriptfile** ____```
### Misc.ScriptStatus
```py
Misc.ScriptStatus(String scriptfile)
- String **scriptfile** ____```
### Misc.ScriptStop
```py
Misc.ScriptStop(String scriptfile)
- String **scriptfile** ____```
### Misc.ScriptStopAll
```py
Misc.ScriptStopAll()```
### Misc.SendMessage
```py
Misc.SendMessage(Double msg)
- Double **msg** ____```
### Misc.SendMessage
```py
Misc.SendMessage(Int32 num, Int32 color)
- Int32 **num** ____
- Int32 **color** ____```
### Misc.SendMessage
```py
Misc.SendMessage(String msg, Boolean wait)
- String **msg** ____
- Boolean **wait** __True__```
### Misc.SendMessage
```py
Misc.SendMessage(Boolean msg, Int32 color)
- Boolean **msg** ____
- Int32 **color** ____```
### Misc.SendMessage
```py
Misc.SendMessage(UInt32 num, Int32 color)
- UInt32 **num** ____
- Int32 **color** ____```
### Misc.SendMessage
```py
Misc.SendMessage(Boolean msg)
- Boolean **msg** ____```
### Misc.SendMessage
```py
Misc.SendMessage(UInt32 num)
- UInt32 **num** ____```
### Misc.SendMessage
```py
Misc.SendMessage(Object obj)
- Object **obj** ____```
### Misc.SendMessage
```py
Misc.SendMessage(Int32 num)
- Int32 **num** ____```
### Misc.SendMessage
```py
Misc.SendMessage(Double msg, Int32 color)
- Double **msg** ____
- Int32 **color** ____```
### Misc.SendMessage
```py
Misc.SendMessage(Single num)
- Single **num** ____```
### Misc.SendMessage
```py
Misc.SendMessage(Object obj, Int32 color)
- Object **obj** ____
- Int32 **color** ____```
### Misc.SendToClient
```py
Misc.SendToClient(String keys)
- String **keys** ____```
### Misc.SetSharedValue
```py
Misc.SetSharedValue(String name, Object value)
- String **name** ____
- Object **value** ____```
### Misc.ShardName
```py
Misc.ShardName()```
### Misc.ToString
```py
Misc.ToString()```
### Misc.UnIgnoreObject
```py
Misc.UnIgnoreObject(Item i)
- Item **i** ____```
### Misc.UnIgnoreObject
```py
Misc.UnIgnoreObject(Int32 s)
- Int32 **s** ____```
### Misc.UnIgnoreObject
```py
Misc.UnIgnoreObject(Mobile m)
- Mobile **m** ____```
### Misc.WaitForContext
```py
Misc.WaitForContext(Item i, Int32 delay)
- Item **i** ____
- Int32 **delay** ____```
### Misc.WaitForContext
```py
Misc.WaitForContext(Mobile mob, Int32 delay)
- Mobile **mob** ____
- Int32 **delay** ____```
### Misc.WaitForContext
```py
Misc.WaitForContext(Int32 ser, Int32 delay)
- Int32 **ser** ____
- Int32 **delay** ____```
### Misc.WaitForMenu
```py
Misc.WaitForMenu(Int32 delay)
- Int32 **delay** ____```
### Misc.WaitForPrompt
```py
Misc.WaitForPrompt(Int32 delay)
- Int32 **delay** ____```
### Misc.WaitForQueryString
```py
Misc.WaitForQueryString(Int32 delay)
- Int32 **delay** ____```