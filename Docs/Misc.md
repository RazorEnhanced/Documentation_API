# Misc    

### Properties  
## Misc.SharedScriptData 
### Methods  
## Misc.Beep
```python
Misc.Beep()```
## Misc.CancelPrompt
```python
Misc.CancelPrompt()```
## Misc.CaptureNow
```python
Misc.CaptureNow()```
## Misc.CheckIgnoreObject
```python
Misc.CheckIgnoreObject(Int32 s)
- Int32 **s** ____```
## Misc.CheckIgnoreObject
```python
Misc.CheckIgnoreObject(Mobile m)
- Mobile **m** ____```
## Misc.CheckIgnoreObject
```python
Misc.CheckIgnoreObject(Item i)
- Item **i** ____```
## Misc.CheckSharedValue
```python
Misc.CheckSharedValue(String name)
- String **name** ____```
## Misc.ClearIgnore
```python
Misc.ClearIgnore()```
## Misc.CloseBackpack
```python
Misc.CloseBackpack()```
## Misc.CloseMenu
```python
Misc.CloseMenu()```
## Misc.ContextReply
```python
Misc.ContextReply(Int32 serial, String menuname)
- Int32 **serial** ____
- String **menuname** ____```
## Misc.ContextReply
```python
Misc.ContextReply(Item item, String menuname)
- Item **item** ____
- String **menuname** ____```
## Misc.ContextReply
```python
Misc.ContextReply(Mobile mob, String menuname)
- Mobile **mob** ____
- String **menuname** ____```
## Misc.ContextReply
```python
Misc.ContextReply(Item item, Int32 idx)
- Item **item** ____
- Int32 **idx** ____```
## Misc.ContextReply
```python
Misc.ContextReply(Mobile mob, Int32 idx)
- Mobile **mob** ____
- Int32 **idx** ____```
## Misc.ContextReply
```python
Misc.ContextReply(Int32 serial, Int32 idx)
- Int32 **serial** ____
- Int32 **idx** ____```
## Misc.CurrentScriptDirectory
```python
Misc.CurrentScriptDirectory()```
## Misc.Disconnect
```python
Misc.Disconnect()```
## Misc.DistanceSqrt
```python
Misc.DistanceSqrt(Point3D a, Point3D b)
- Point3D **a** ____
- Point3D **b** ____```
## Misc.Equals
```python
Misc.Equals(Object obj)
- Object **obj** ____```
## Misc.ExportPythonAPI
```python
Misc.ExportPythonAPI(String path, Boolean pretty)
- String **path** ____
- Boolean **pretty** __True__```
Return a string containing list RE Python API list in JSON format.
## Misc.FocusUOWindow
```python
Misc.FocusUOWindow()```
## Misc.GetContPosition
```python
Misc.GetContPosition()```
## Misc.GetHashCode
```python
Misc.GetHashCode()```
## Misc.GetMapInfo
```python
Misc.GetMapInfo(UInt32 serial)
- UInt32 **serial** ____```
## Misc.GetMenuTitle
```python
Misc.GetMenuTitle()```
## Misc.GetType
```python
Misc.GetType()```
## Misc.HasMenu
```python
Misc.HasMenu()```
## Misc.HasPrompt
```python
Misc.HasPrompt()```
## Misc.HasQueryString
```python
Misc.HasQueryString()```
## Misc.IgnoreObject
```python
Misc.IgnoreObject(Item i)
- Item **i** ____```
## Misc.IgnoreObject
```python
Misc.IgnoreObject(Mobile m)
- Mobile **m** ____```
## Misc.IgnoreObject
```python
Misc.IgnoreObject(Int32 s)
- Int32 **s** ____```
## Misc.LastHotKey
```python
Misc.LastHotKey()```
Returns the latest HotKeyEvent recorded by razor.
The HotKeyEvent has 2 properties:
hke.Key: enum System.Windows.Forms.Keys
hke.Timestamp: double repesenting the UnixTimestamp, compatible with python's time.time()
## Misc.MenuContain
```python
Misc.MenuContain(String submenu)
- String **submenu** ____```
## Misc.MenuResponse
```python
Misc.MenuResponse(String submenu)
- String **submenu** ____```
## Misc.MouseLocation
```python
Misc.MouseLocation()```
## Misc.MouseMove
```python
Misc.MouseMove(Int32 posX, Int32 posY)
- Int32 **posX** ____
- Int32 **posY** ____```
## Misc.NextContPosition
```python
Misc.NextContPosition(Int32 x, Int32 y)
- Int32 **x** ____
- Int32 **y** ____```
## Misc.NoOperation
```python
Misc.NoOperation()```
## Misc.NoRunStealthStatus
```python
Misc.NoRunStealthStatus()```
## Misc.NoRunStealthToggle
```python
Misc.NoRunStealthToggle(Boolean enable)
- Boolean **enable** ____```
## Misc.Pause
```python
Misc.Pause(Int32 mseconds)
- Int32 **mseconds** ____```
## Misc.PetRename
```python
Misc.PetRename(Int32 serial, String name)
- Int32 **serial** ____
- String **name** ____```
## Misc.PetRename
```python
Misc.PetRename(Mobile mob, String name)
- Mobile **mob** ____
- String **name** ____```
## Misc.QueryStringResponse
```python
Misc.QueryStringResponse(Boolean okcancel, String response)
- Boolean **okcancel** ____
- String **response** ____```
## Misc.ReadSharedValue
```python
Misc.ReadSharedValue(String name)
- String **name** ____```
## Misc.RemoveSharedValue
```python
Misc.RemoveSharedValue(String name)
- String **name** ____```
## Misc.ResetPrompt
```python
Misc.ResetPrompt()```
## Misc.ResponsePrompt
```python
Misc.ResponsePrompt(String text)
- String **text** ____```
## Misc.Resync
```python
Misc.Resync()```
## Misc.ScriptRun
```python
Misc.ScriptRun(String scriptfile)
- String **scriptfile** ____```
## Misc.ScriptStatus
```python
Misc.ScriptStatus(String scriptfile)
- String **scriptfile** ____```
## Misc.ScriptStop
```python
Misc.ScriptStop(String scriptfile)
- String **scriptfile** ____```
## Misc.ScriptStopAll
```python
Misc.ScriptStopAll()```
## Misc.SendMessage
```python
Misc.SendMessage(Double msg)
- Double **msg** ____```
## Misc.SendMessage
```python
Misc.SendMessage(Int32 num, Int32 color)
- Int32 **num** ____
- Int32 **color** ____```
## Misc.SendMessage
```python
Misc.SendMessage(String msg, Boolean wait)
- String **msg** ____
- Boolean **wait** __True__```
## Misc.SendMessage
```python
Misc.SendMessage(Boolean msg, Int32 color)
- Boolean **msg** ____
- Int32 **color** ____```
## Misc.SendMessage
```python
Misc.SendMessage(UInt32 num, Int32 color)
- UInt32 **num** ____
- Int32 **color** ____```
## Misc.SendMessage
```python
Misc.SendMessage(Boolean msg)
- Boolean **msg** ____```
## Misc.SendMessage
```python
Misc.SendMessage(UInt32 num)
- UInt32 **num** ____```
## Misc.SendMessage
```python
Misc.SendMessage(Object obj)
- Object **obj** ____```
## Misc.SendMessage
```python
Misc.SendMessage(Int32 num)
- Int32 **num** ____```
## Misc.SendMessage
```python
Misc.SendMessage(Double msg, Int32 color)
- Double **msg** ____
- Int32 **color** ____```
## Misc.SendMessage
```python
Misc.SendMessage(Single num)
- Single **num** ____```
## Misc.SendMessage
```python
Misc.SendMessage(Object obj, Int32 color)
- Object **obj** ____
- Int32 **color** ____```
## Misc.SendToClient
```python
Misc.SendToClient(String keys)
- String **keys** ____```
## Misc.SetSharedValue
```python
Misc.SetSharedValue(String name, Object value)
- String **name** ____
- Object **value** ____```
## Misc.ShardName
```python
Misc.ShardName()```
## Misc.ToString
```python
Misc.ToString()```
## Misc.UnIgnoreObject
```python
Misc.UnIgnoreObject(Item i)
- Item **i** ____```
## Misc.UnIgnoreObject
```python
Misc.UnIgnoreObject(Int32 s)
- Int32 **s** ____```
## Misc.UnIgnoreObject
```python
Misc.UnIgnoreObject(Mobile m)
- Mobile **m** ____```
## Misc.WaitForContext
```python
Misc.WaitForContext(Item i, Int32 delay)
- Item **i** ____
- Int32 **delay** ____```
## Misc.WaitForContext
```python
Misc.WaitForContext(Mobile mob, Int32 delay)
- Mobile **mob** ____
- Int32 **delay** ____```
## Misc.WaitForContext
```python
Misc.WaitForContext(Int32 ser, Int32 delay)
- Int32 **ser** ____
- Int32 **delay** ____```
## Misc.WaitForMenu
```python
Misc.WaitForMenu(Int32 delay)
- Int32 **delay** ____```
## Misc.WaitForPrompt
```python
Misc.WaitForPrompt(Int32 delay)
- Int32 **delay** ____```
## Misc.WaitForQueryString
```python
Misc.WaitForQueryString(Int32 delay)
- Int32 **delay** ____```