# Misc    

## Properties  
### Misc.SharedScriptData __ConcurrentDictionary`2__ 
## Methods  
### Misc.Beep
```
Beep() -> Void
```
### Misc.CancelPrompt
```
CancelPrompt() -> Void
```
### Misc.CaptureNow
```
CaptureNow() -> Void
```
### Misc.CheckIgnoreObject
```
CheckIgnoreObject(Int32 s) -> Boolean
```
- __Int32__ **s**
### Misc.CheckIgnoreObject
```
CheckIgnoreObject(Mobile m) -> Boolean
```
- __Mobile__ **m**
### Misc.CheckIgnoreObject
```
CheckIgnoreObject(Item i) -> Boolean
```
- __Item__ **i**
### Misc.CheckSharedValue
```
CheckSharedValue(String name) -> Boolean
```
- __String__ **name**
### Misc.ClearIgnore
```
ClearIgnore() -> Void
```
### Misc.CloseBackpack
```
CloseBackpack() -> Void
```
### Misc.CloseMenu
```
CloseMenu() -> Void
```
### Misc.ContextReply
```
ContextReply(Int32 serial, String menuname) -> Void
```
- __Int32__ **serial** 
- __String__ **menuname**
### Misc.ContextReply
```
ContextReply(Item item, String menuname) -> Void
```
- __Item__ **item** 
- __String__ **menuname**
### Misc.ContextReply
```
ContextReply(Mobile mob, String menuname) -> Void
```
- __Mobile__ **mob** 
- __String__ **menuname**
### Misc.ContextReply
```
ContextReply(Item item, Int32 idx) -> Void
```
- __Item__ **item** 
- __Int32__ **idx**
### Misc.ContextReply
```
ContextReply(Mobile mob, Int32 idx) -> Void
```
- __Mobile__ **mob** 
- __Int32__ **idx**
### Misc.ContextReply
```
ContextReply(Int32 serial, Int32 idx) -> Void
```
- __Int32__ **serial** 
- __Int32__ **idx**
### Misc.CurrentScriptDirectory
```
CurrentScriptDirectory() -> String
```
### Misc.Disconnect
```
Disconnect() -> Void
```
### Misc.DistanceSqrt
```
DistanceSqrt(Point3D a, Point3D b) -> Double
```
- __Point3D__ **a** 
- __Point3D__ **b**
### Misc.Equals
```
Equals(Object obj) -> Boolean
```
- __Object__ **obj**
### Misc.ExportPythonAPI
```
ExportPythonAPI(String path, Boolean pretty) -> Void
```
- __String__ **path** 
- __Boolean__ **pretty** True
Return a string containing list RE Python API list in JSON format.
### Misc.FocusUOWindow
```
FocusUOWindow() -> Void
```
### Misc.GetContPosition
```
GetContPosition() -> Point
```
### Misc.GetHashCode
```
GetHashCode() -> Int32
```
### Misc.GetMapInfo
```
GetMapInfo(UInt32 serial) -> MapInfo
```
- __UInt32__ **serial**
### Misc.GetMenuTitle
```
GetMenuTitle() -> String
```
### Misc.GetType
```
GetType() -> Type
```
### Misc.HasMenu
```
HasMenu() -> Boolean
```
### Misc.HasPrompt
```
HasPrompt() -> Boolean
```
### Misc.HasQueryString
```
HasQueryString() -> Boolean
```
### Misc.IgnoreObject
```
IgnoreObject(Item i) -> Void
```
- __Item__ **i**
### Misc.IgnoreObject
```
IgnoreObject(Mobile m) -> Void
```
- __Mobile__ **m**
### Misc.IgnoreObject
```
IgnoreObject(Int32 s) -> Void
```
- __Int32__ **s**
### Misc.LastHotKey
```
LastHotKey() -> HotKeyEvent
```
Returns the latest HotKeyEvent recorded by razor.
The HotKeyEvent has 2 properties:
hke.Key: enum System.Windows.Forms.Keys
hke.Timestamp: double repesenting the UnixTimestamp, compatible with python's time.time()
### Misc.MenuContain
```
MenuContain(String submenu) -> Boolean
```
- __String__ **submenu**
### Misc.MenuResponse
```
MenuResponse(String submenu) -> Void
```
- __String__ **submenu**
### Misc.MouseLocation
```
MouseLocation() -> Point
```
### Misc.MouseMove
```
MouseMove(Int32 posX, Int32 posY) -> Void
```
- __Int32__ **posX** 
- __Int32__ **posY**
### Misc.NextContPosition
```
NextContPosition(Int32 x, Int32 y) -> Void
```
- __Int32__ **x** 
- __Int32__ **y**
### Misc.NoOperation
```
NoOperation() -> Void
```
### Misc.NoRunStealthStatus
```
NoRunStealthStatus() -> Boolean
```
### Misc.NoRunStealthToggle
```
NoRunStealthToggle(Boolean enable) -> Void
```
- __Boolean__ **enable**
### Misc.Pause
```
Pause(Int32 mseconds) -> Void
```
- __Int32__ **mseconds**
### Misc.PetRename
```
PetRename(Int32 serial, String name) -> Void
```
- __Int32__ **serial** 
- __String__ **name**
### Misc.PetRename
```
PetRename(Mobile mob, String name) -> Void
```
- __Mobile__ **mob** 
- __String__ **name**
### Misc.QueryStringResponse
```
QueryStringResponse(Boolean okcancel, String response) -> Void
```
- __Boolean__ **okcancel** 
- __String__ **response**
### Misc.ReadSharedValue
```
ReadSharedValue(String name) -> Object
```
- __String__ **name**
### Misc.RemoveSharedValue
```
RemoveSharedValue(String name) -> Void
```
- __String__ **name**
### Misc.ResetPrompt
```
ResetPrompt() -> Void
```
### Misc.ResponsePrompt
```
ResponsePrompt(String text) -> Void
```
- __String__ **text**
### Misc.Resync
```
Resync() -> Void
```
### Misc.ScriptRun
```
ScriptRun(String scriptfile) -> Void
```
- __String__ **scriptfile**
### Misc.ScriptStatus
```
ScriptStatus(String scriptfile) -> Boolean
```
- __String__ **scriptfile**
### Misc.ScriptStop
```
ScriptStop(String scriptfile) -> Void
```
- __String__ **scriptfile**
### Misc.ScriptStopAll
```
ScriptStopAll() -> Void
```
### Misc.SendMessage
```
SendMessage(Double msg) -> Void
```
- __Double__ **msg**
### Misc.SendMessage
```
SendMessage(Int32 num, Int32 color) -> Void
```
- __Int32__ **num** 
- __Int32__ **color**
### Misc.SendMessage
```
SendMessage(String msg, Boolean wait) -> Void
```
- __String__ **msg** 
- __Boolean__ **wait** True
### Misc.SendMessage
```
SendMessage(Boolean msg, Int32 color) -> Void
```
- __Boolean__ **msg** 
- __Int32__ **color**
### Misc.SendMessage
```
SendMessage(UInt32 num, Int32 color) -> Void
```
- __UInt32__ **num** 
- __Int32__ **color**
### Misc.SendMessage
```
SendMessage(Boolean msg) -> Void
```
- __Boolean__ **msg**
### Misc.SendMessage
```
SendMessage(UInt32 num) -> Void
```
- __UInt32__ **num**
### Misc.SendMessage
```
SendMessage(Object obj) -> Void
```
- __Object__ **obj**
### Misc.SendMessage
```
SendMessage(Int32 num) -> Void
```
- __Int32__ **num**
### Misc.SendMessage
```
SendMessage(Double msg, Int32 color) -> Void
```
- __Double__ **msg** 
- __Int32__ **color**
### Misc.SendMessage
```
SendMessage(Single num) -> Void
```
- __Single__ **num**
### Misc.SendMessage
```
SendMessage(Object obj, Int32 color) -> Void
```
- __Object__ **obj** 
- __Int32__ **color**
### Misc.SendToClient
```
SendToClient(String keys) -> Void
```
- __String__ **keys**
### Misc.SetSharedValue
```
SetSharedValue(String name, Object value) -> Void
```
- __String__ **name** 
- __Object__ **value**
### Misc.ShardName
```
ShardName() -> String
```
### Misc.ToString
```
ToString() -> String
```
### Misc.UnIgnoreObject
```
UnIgnoreObject(Item i) -> Void
```
- __Item__ **i**
### Misc.UnIgnoreObject
```
UnIgnoreObject(Int32 s) -> Void
```
- __Int32__ **s**
### Misc.UnIgnoreObject
```
UnIgnoreObject(Mobile m) -> Void
```
- __Mobile__ **m**
### Misc.WaitForContext
```
WaitForContext(Item i, Int32 delay) -> List`1
```
- __Item__ **i** 
- __Int32__ **delay**
### Misc.WaitForContext
```
WaitForContext(Mobile mob, Int32 delay) -> List`1
```
- __Mobile__ **mob** 
- __Int32__ **delay**
### Misc.WaitForContext
```
WaitForContext(Int32 ser, Int32 delay) -> List`1
```
- __Int32__ **ser** 
- __Int32__ **delay**
### Misc.WaitForMenu
```
WaitForMenu(Int32 delay) -> Void
```
- __Int32__ **delay**
### Misc.WaitForPrompt
```
WaitForPrompt(Int32 delay) -> Void
```
- __Int32__ **delay**
### Misc.WaitForQueryString
```
WaitForQueryString(Int32 delay) -> Void
```
- __Int32__ **delay**