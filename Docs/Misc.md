# Misc    

## Properties  
### Misc.SharedScriptData __ConcurrentDictionary`2__ 
## Methods  
### Misc.Beep
```
Misc.Beep() -> Void
```
### Misc.CancelPrompt
```
Misc.CancelPrompt() -> Void
```
### Misc.CaptureNow
```
Misc.CaptureNow() -> Void
```
### Misc.CheckIgnoreObject
```
Misc.CheckIgnoreObject(s) -> Boolean
```
- **s**: Int32
### Misc.CheckIgnoreObject
```
Misc.CheckIgnoreObject(m) -> Boolean
```
- **m**: Mobile
### Misc.CheckIgnoreObject
```
Misc.CheckIgnoreObject(i) -> Boolean
```
- **i**: Item
### Misc.CheckSharedValue
```
Misc.CheckSharedValue(name) -> Boolean
```
- **name**: String
### Misc.ClearIgnore
```
Misc.ClearIgnore() -> Void
```
### Misc.CloseBackpack
```
Misc.CloseBackpack() -> Void
```
### Misc.CloseMenu
```
Misc.CloseMenu() -> Void
```
### Misc.ContextReply
```
Misc.ContextReply(serial, menuname) -> Void
```
- **serial**: Int32 
- **menuname**: String
### Misc.ContextReply
```
Misc.ContextReply(item, menuname) -> Void
```
- **item**: Item 
- **menuname**: String
### Misc.ContextReply
```
Misc.ContextReply(mob, menuname) -> Void
```
- **mob**: Mobile 
- **menuname**: String
### Misc.ContextReply
```
Misc.ContextReply(item, idx) -> Void
```
- **item**: Item 
- **idx**: Int32
### Misc.ContextReply
```
Misc.ContextReply(mob, idx) -> Void
```
- **mob**: Mobile 
- **idx**: Int32
### Misc.ContextReply
```
Misc.ContextReply(serial, idx) -> Void
```
- **serial**: Int32 
- **idx**: Int32
### Misc.CurrentScriptDirectory
```
Misc.CurrentScriptDirectory() -> String
```
### Misc.Disconnect
```
Misc.Disconnect() -> Void
```
### Misc.DistanceSqrt
```
Misc.DistanceSqrt(a, b) -> Double
```
- **a**: Point3D 
- **b**: Point3D
### Misc.Equals
```
Misc.Equals(obj) -> Boolean
```
- **obj**: Object
### Misc.ExportPythonAPI
```
Misc.ExportPythonAPI(path, pretty) -> Void
```
- **path**: String 
- **pretty**: Boolean True
Return a string containing list RE Python API list in JSON format.
### Misc.FocusUOWindow
```
Misc.FocusUOWindow() -> Void
```
### Misc.GetContPosition
```
Misc.GetContPosition() -> Point
```
### Misc.GetHashCode
```
Misc.GetHashCode() -> Int32
```
### Misc.GetMapInfo
```
Misc.GetMapInfo(serial) -> MapInfo
```
- **serial**: UInt32
### Misc.GetMenuTitle
```
Misc.GetMenuTitle() -> String
```
### Misc.GetType
```
Misc.GetType() -> Type
```
### Misc.HasMenu
```
Misc.HasMenu() -> Boolean
```
### Misc.HasPrompt
```
Misc.HasPrompt() -> Boolean
```
### Misc.HasQueryString
```
Misc.HasQueryString() -> Boolean
```
### Misc.IgnoreObject
```
Misc.IgnoreObject(i) -> Void
```
- **i**: Item
### Misc.IgnoreObject
```
Misc.IgnoreObject(m) -> Void
```
- **m**: Mobile
### Misc.IgnoreObject
```
Misc.IgnoreObject(s) -> Void
```
- **s**: Int32
### Misc.LastHotKey
```
Misc.LastHotKey() -> HotKeyEvent
```
Returns the latest HotKeyEvent recorded by razor.
The HotKeyEvent has 2 properties:
hke.Key: enum System.Windows.Forms.Keys
hke.Timestamp: double repesenting the UnixTimestamp, compatible with python's time.time()
### Misc.MenuContain
```
Misc.MenuContain(submenu) -> Boolean
```
- **submenu**: String
### Misc.MenuResponse
```
Misc.MenuResponse(submenu) -> Void
```
- **submenu**: String
### Misc.MouseLocation
```
Misc.MouseLocation() -> Point
```
### Misc.MouseMove
```
Misc.MouseMove(posX, posY) -> Void
```
- **posX**: Int32 
- **posY**: Int32
### Misc.NextContPosition
```
Misc.NextContPosition(x, y) -> Void
```
- **x**: Int32 
- **y**: Int32
### Misc.NoOperation
```
Misc.NoOperation() -> Void
```
### Misc.NoRunStealthStatus
```
Misc.NoRunStealthStatus() -> Boolean
```
### Misc.NoRunStealthToggle
```
Misc.NoRunStealthToggle(enable) -> Void
```
- **enable**: Boolean
### Misc.Pause
```
Misc.Pause(mseconds) -> Void
```
- **mseconds**: Int32
### Misc.PetRename
```
Misc.PetRename(serial, name) -> Void
```
- **serial**: Int32 
- **name**: String
### Misc.PetRename
```
Misc.PetRename(mob, name) -> Void
```
- **mob**: Mobile 
- **name**: String
### Misc.QueryStringResponse
```
Misc.QueryStringResponse(okcancel, response) -> Void
```
- **okcancel**: Boolean 
- **response**: String
### Misc.ReadSharedValue
```
Misc.ReadSharedValue(name) -> Object
```
- **name**: String
### Misc.RemoveSharedValue
```
Misc.RemoveSharedValue(name) -> Void
```
- **name**: String
### Misc.ResetPrompt
```
Misc.ResetPrompt() -> Void
```
### Misc.ResponsePrompt
```
Misc.ResponsePrompt(text) -> Void
```
- **text**: String
### Misc.Resync
```
Misc.Resync() -> Void
```
### Misc.ScriptRun
```
Misc.ScriptRun(scriptfile) -> Void
```
- **scriptfile**: String
### Misc.ScriptStatus
```
Misc.ScriptStatus(scriptfile) -> Boolean
```
- **scriptfile**: String
### Misc.ScriptStop
```
Misc.ScriptStop(scriptfile) -> Void
```
- **scriptfile**: String
### Misc.ScriptStopAll
```
Misc.ScriptStopAll() -> Void
```
### Misc.SendMessage
```
Misc.SendMessage(msg) -> Void
```
- **msg**: Double
### Misc.SendMessage
```
Misc.SendMessage(num, color) -> Void
```
- **num**: Int32 
- **color**: Int32
### Misc.SendMessage
```
Misc.SendMessage(msg, wait) -> Void
```
- **msg**: String 
- **wait**: Boolean True
### Misc.SendMessage
```
Misc.SendMessage(msg, color) -> Void
```
- **msg**: Boolean 
- **color**: Int32
### Misc.SendMessage
```
Misc.SendMessage(num, color) -> Void
```
- **num**: UInt32 
- **color**: Int32
### Misc.SendMessage
```
Misc.SendMessage(msg) -> Void
```
- **msg**: Boolean
### Misc.SendMessage
```
Misc.SendMessage(num) -> Void
```
- **num**: UInt32
### Misc.SendMessage
```
Misc.SendMessage(obj) -> Void
```
- **obj**: Object
### Misc.SendMessage
```
Misc.SendMessage(num) -> Void
```
- **num**: Int32
### Misc.SendMessage
```
Misc.SendMessage(msg, color) -> Void
```
- **msg**: Double 
- **color**: Int32
### Misc.SendMessage
```
Misc.SendMessage(num) -> Void
```
- **num**: Single
### Misc.SendMessage
```
Misc.SendMessage(obj, color) -> Void
```
- **obj**: Object 
- **color**: Int32
### Misc.SendToClient
```
Misc.SendToClient(keys) -> Void
```
- **keys**: String
### Misc.SetSharedValue
```
Misc.SetSharedValue(name, value) -> Void
```
- **name**: String 
- **value**: Object
### Misc.ShardName
```
Misc.ShardName() -> String
```
### Misc.ToString
```
Misc.ToString() -> String
```
### Misc.UnIgnoreObject
```
Misc.UnIgnoreObject(i) -> Void
```
- **i**: Item
### Misc.UnIgnoreObject
```
Misc.UnIgnoreObject(s) -> Void
```
- **s**: Int32
### Misc.UnIgnoreObject
```
Misc.UnIgnoreObject(m) -> Void
```
- **m**: Mobile
### Misc.WaitForContext
```
Misc.WaitForContext(i, delay) -> List`1
```
- **i**: Item 
- **delay**: Int32
### Misc.WaitForContext
```
Misc.WaitForContext(mob, delay) -> List`1
```
- **mob**: Mobile 
- **delay**: Int32
### Misc.WaitForContext
```
Misc.WaitForContext(ser, delay) -> List`1
```
- **ser**: Int32 
- **delay**: Int32
### Misc.WaitForMenu
```
Misc.WaitForMenu(delay) -> Void
```
- **delay**: Int32
### Misc.WaitForPrompt
```
Misc.WaitForPrompt(delay) -> Void
```
- **delay**: Int32
### Misc.WaitForQueryString
```
Misc.WaitForQueryString(delay) -> Void
```
- **delay**: Int32