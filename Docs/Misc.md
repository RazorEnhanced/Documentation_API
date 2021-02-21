# Misc    

## Properties  
## Misc.SharedScriptData 
## Methods  
### Misc.Beep
``` python
Misc.Beep()

```
### Misc.CancelPrompt
``` python
Misc.CancelPrompt()

```
### Misc.CaptureNow
``` python
Misc.CaptureNow()

```
### Misc.CheckIgnoreObject
``` python
Misc.CheckIgnoreObject(Int32 s)
  Int32 s #
```
### Misc.CheckIgnoreObject
``` python
Misc.CheckIgnoreObject(Mobile m)
  Mobile m #
```
### Misc.CheckIgnoreObject
``` python
Misc.CheckIgnoreObject(Item i)
  Item i #
```
### Misc.CheckSharedValue
``` python
Misc.CheckSharedValue(String name)
  String name #
```
### Misc.ClearIgnore
``` python
Misc.ClearIgnore()

```
### Misc.CloseBackpack
``` python
Misc.CloseBackpack()

```
### Misc.CloseMenu
``` python
Misc.CloseMenu()

```
### Misc.ContextReply
``` python
Misc.ContextReply(Int32 serial, String menuname)
  Int32 serial #
  String menuname #
```
### Misc.ContextReply
``` python
Misc.ContextReply(Item item, String menuname)
  Item item #
  String menuname #
```
### Misc.ContextReply
``` python
Misc.ContextReply(Mobile mob, String menuname)
  Mobile mob #
  String menuname #
```
### Misc.ContextReply
``` python
Misc.ContextReply(Item item, Int32 idx)
  Item item #
  Int32 idx #
```
### Misc.ContextReply
``` python
Misc.ContextReply(Mobile mob, Int32 idx)
  Mobile mob #
  Int32 idx #
```
### Misc.ContextReply
``` python
Misc.ContextReply(Int32 serial, Int32 idx)
  Int32 serial #
  Int32 idx #
```
### Misc.CurrentScriptDirectory
``` python
Misc.CurrentScriptDirectory()

```
### Misc.Disconnect
``` python
Misc.Disconnect()

```
### Misc.DistanceSqrt
``` python
Misc.DistanceSqrt(Point3D a, Point3D b)
  Point3D a #
  Point3D b #
```
### Misc.Equals
``` python
Misc.Equals(Object obj)
  Object obj #
```
### Misc.ExportPythonAPI
``` python
Misc.ExportPythonAPI(String path, Boolean pretty)
  String path #
  Boolean pretty #True
```
Return a string containing list RE Python API list in JSON format.
### Misc.FocusUOWindow
``` python
Misc.FocusUOWindow()

```
### Misc.GetContPosition
``` python
Misc.GetContPosition()

```
### Misc.GetHashCode
``` python
Misc.GetHashCode()

```
### Misc.GetMapInfo
``` python
Misc.GetMapInfo(UInt32 serial)
  UInt32 serial #
```
### Misc.GetMenuTitle
``` python
Misc.GetMenuTitle()

```
### Misc.GetType
``` python
Misc.GetType()

```
### Misc.HasMenu
``` python
Misc.HasMenu()

```
### Misc.HasPrompt
``` python
Misc.HasPrompt()

```
### Misc.HasQueryString
``` python
Misc.HasQueryString()

```
### Misc.IgnoreObject
``` python
Misc.IgnoreObject(Item i)
  Item i #
```
### Misc.IgnoreObject
``` python
Misc.IgnoreObject(Mobile m)
  Mobile m #
```
### Misc.IgnoreObject
``` python
Misc.IgnoreObject(Int32 s)
  Int32 s #
```
### Misc.LastHotKey
``` python
Misc.LastHotKey()

```
Returns the latest HotKeyEvent recorded by razor.
The HotKeyEvent has 2 properties:
hke.Key: enum System.Windows.Forms.Keys
hke.Timestamp: double repesenting the UnixTimestamp, compatible with python's time.time()
### Misc.MenuContain
``` python
Misc.MenuContain(String submenu)
  String submenu #
```
### Misc.MenuResponse
``` python
Misc.MenuResponse(String submenu)
  String submenu #
```
### Misc.MouseLocation
``` python
Misc.MouseLocation()

```
### Misc.MouseMove
``` python
Misc.MouseMove(Int32 posX, Int32 posY)
  Int32 posX #
  Int32 posY #
```
### Misc.NextContPosition
``` python
Misc.NextContPosition(Int32 x, Int32 y)
  Int32 x #
  Int32 y #
```
### Misc.NoOperation
``` python
Misc.NoOperation()

```
### Misc.NoRunStealthStatus
``` python
Misc.NoRunStealthStatus()

```
### Misc.NoRunStealthToggle
``` python
Misc.NoRunStealthToggle(Boolean enable)
  Boolean enable #
```
### Misc.Pause
``` python
Misc.Pause(Int32 mseconds)
  Int32 mseconds #
```
### Misc.PetRename
``` python
Misc.PetRename(Int32 serial, String name)
  Int32 serial #
  String name #
```
### Misc.PetRename
``` python
Misc.PetRename(Mobile mob, String name)
  Mobile mob #
  String name #
```
### Misc.QueryStringResponse
``` python
Misc.QueryStringResponse(Boolean okcancel, String response)
  Boolean okcancel #
  String response #
```
### Misc.ReadSharedValue
``` python
Misc.ReadSharedValue(String name)
  String name #
```
### Misc.RemoveSharedValue
``` python
Misc.RemoveSharedValue(String name)
  String name #
```
### Misc.ResetPrompt
``` python
Misc.ResetPrompt()

```
### Misc.ResponsePrompt
``` python
Misc.ResponsePrompt(String text)
  String text #
```
### Misc.Resync
``` python
Misc.Resync()

```
### Misc.ScriptRun
``` python
Misc.ScriptRun(String scriptfile)
  String scriptfile #
```
### Misc.ScriptStatus
``` python
Misc.ScriptStatus(String scriptfile)
  String scriptfile #
```
### Misc.ScriptStop
``` python
Misc.ScriptStop(String scriptfile)
  String scriptfile #
```
### Misc.ScriptStopAll
``` python
Misc.ScriptStopAll()

```
### Misc.SendMessage
``` python
Misc.SendMessage(Double msg)
  Double msg #
```
### Misc.SendMessage
``` python
Misc.SendMessage(Int32 num, Int32 color)
  Int32 num #
  Int32 color #
```
### Misc.SendMessage
``` python
Misc.SendMessage(String msg, Boolean wait)
  String msg #
  Boolean wait #True
```
### Misc.SendMessage
``` python
Misc.SendMessage(Boolean msg, Int32 color)
  Boolean msg #
  Int32 color #
```
### Misc.SendMessage
``` python
Misc.SendMessage(UInt32 num, Int32 color)
  UInt32 num #
  Int32 color #
```
### Misc.SendMessage
``` python
Misc.SendMessage(Boolean msg)
  Boolean msg #
```
### Misc.SendMessage
``` python
Misc.SendMessage(UInt32 num)
  UInt32 num #
```
### Misc.SendMessage
``` python
Misc.SendMessage(Object obj)
  Object obj #
```
### Misc.SendMessage
``` python
Misc.SendMessage(Int32 num)
  Int32 num #
```
### Misc.SendMessage
``` python
Misc.SendMessage(Double msg, Int32 color)
  Double msg #
  Int32 color #
```
### Misc.SendMessage
``` python
Misc.SendMessage(Single num)
  Single num #
```
### Misc.SendMessage
``` python
Misc.SendMessage(Object obj, Int32 color)
  Object obj #
  Int32 color #
```
### Misc.SendToClient
``` python
Misc.SendToClient(String keys)
  String keys #
```
### Misc.SetSharedValue
``` python
Misc.SetSharedValue(String name, Object value)
  String name #
  Object value #
```
### Misc.ShardName
``` python
Misc.ShardName()

```
### Misc.ToString
``` python
Misc.ToString()

```
### Misc.UnIgnoreObject
``` python
Misc.UnIgnoreObject(Item i)
  Item i #
```
### Misc.UnIgnoreObject
``` python
Misc.UnIgnoreObject(Int32 s)
  Int32 s #
```
### Misc.UnIgnoreObject
``` python
Misc.UnIgnoreObject(Mobile m)
  Mobile m #
```
### Misc.WaitForContext
``` python
Misc.WaitForContext(Item i, Int32 delay)
  Item i #
  Int32 delay #
```
### Misc.WaitForContext
``` python
Misc.WaitForContext(Mobile mob, Int32 delay)
  Mobile mob #
  Int32 delay #
```
### Misc.WaitForContext
``` python
Misc.WaitForContext(Int32 ser, Int32 delay)
  Int32 ser #
  Int32 delay #
```
### Misc.WaitForMenu
``` python
Misc.WaitForMenu(Int32 delay)
  Int32 delay #
```
### Misc.WaitForPrompt
``` python
Misc.WaitForPrompt(Int32 delay)
  Int32 delay #
```
### Misc.WaitForQueryString
``` python
Misc.WaitForQueryString(Int32 delay)
  Int32 delay #
```