# Misc

- `Misc.SharedScriptData``Misc.Beep()`



`Misc.CancelPrompt()`



`Misc.CaptureNow()`



`Misc.CheckIgnoreObject(Int32 s)`

- `Int32 s` 

`Misc.CheckIgnoreObject(Mobile m)`

- `Mobile m` 

`Misc.CheckIgnoreObject(Item i)`

- `Item i` 

`Misc.CheckSharedValue(String name)`

- `String name` 

`Misc.ClearIgnore()`



`Misc.CloseBackpack()`



`Misc.CloseMenu()`



`Misc.ContextReply(Int32 serial, Int32 idx)`

- `Int32 serial` 
- `Int32 idx` 

`Misc.ContextReply(Item item, Int32 idx)`

- `Item item` 
- `Int32 idx` 

`Misc.ContextReply(Mobile mob, String menuname)`

- `Mobile mob` 
- `String menuname` 

`Misc.ContextReply(Item item, String menuname)`

- `Item item` 
- `String menuname` 

`Misc.ContextReply(Int32 serial, String menuname)`

- `Int32 serial` 
- `String menuname` 

`Misc.ContextReply(Mobile mob, Int32 idx)`

- `Mobile mob` 
- `Int32 idx` 

`Misc.CurrentScriptDirectory()`



`Misc.Disconnect()`



`Misc.DistanceSqrt(Point3D a, Point3D b)`

- `Point3D a` 
- `Point3D b` 

`Misc.ExportPythonAPI(String path, Boolean pretty)`

- `String path` 
- `Boolean pretty` True
Return a string containing list RE Python API list in JSON format.
`Misc.FocusUOWindow()`



`Misc.get_SharedScriptData()`



`Misc.GetContPosition()`



`Misc.GetMapInfo(UInt32 serial)`

- `UInt32 serial` 

`Misc.GetMenuTitle()`



`Misc.HasMenu()`



`Misc.HasPrompt()`



`Misc.HasQueryString()`



`Misc.IgnoreObject(Mobile m)`

- `Mobile m` 

`Misc.IgnoreObject(Int32 s)`

- `Int32 s` 

`Misc.IgnoreObject(Item i)`

- `Item i` 

`Misc.LastHotKey()`


Returns the latest HotKeyEvent recorded by razor.
The HotKeyEvent has 2 properties:
hke.Key: enum System.Windows.Forms.Keys
hke.Timestamp: double repesenting the UnixTimestamp, compatible with python's time.time()
`Misc.MenuContain(String submenu)`

- `String submenu` 

`Misc.MenuResponse(String submenu)`

- `String submenu` 

`Misc.MouseLocation()`



`Misc.MouseMove(Int32 posX, Int32 posY)`

- `Int32 posX` 
- `Int32 posY` 

`Misc.NextContPosition(Int32 x, Int32 y)`

- `Int32 x` 
- `Int32 y` 

`Misc.NoOperation()`



`Misc.NoRunStealthStatus()`



`Misc.NoRunStealthToggle(Boolean enable)`

- `Boolean enable` 

`Misc.Pause(Int32 mseconds)`

- `Int32 mseconds` 

`Misc.PetRename(Mobile mob, String name)`

- `Mobile mob` 
- `String name` 

`Misc.PetRename(Int32 serial, String name)`

- `Int32 serial` 
- `String name` 

`Misc.QueryStringResponse(Boolean okcancel, String response)`

- `Boolean okcancel` 
- `String response` 

`Misc.ReadSharedValue(String name)`

- `String name` 

`Misc.RemoveSharedValue(String name)`

- `String name` 

`Misc.ResetPrompt()`



`Misc.ResponsePrompt(String text)`

- `String text` 

`Misc.Resync()`



`Misc.ScriptRun(String scriptfile)`

- `String scriptfile` 

`Misc.ScriptStatus(String scriptfile)`

- `String scriptfile` 

`Misc.ScriptStop(String scriptfile)`

- `String scriptfile` 

`Misc.ScriptStopAll()`



`Misc.SendMessage(String msg, Boolean wait)`

- `String msg` 
- `Boolean wait` True

`Misc.SendMessage(Double msg, Int32 color)`

- `Double msg` 
- `Int32 color` 

`Misc.SendMessage(Int32 num)`

- `Int32 num` 

`Misc.SendMessage(Object obj)`

- `Object obj` 

`Misc.SendMessage(Boolean msg, Int32 color)`

- `Boolean msg` 
- `Int32 color` 

`Misc.SendMessage(UInt32 num)`

- `UInt32 num` 

`Misc.SendMessage(Boolean msg)`

- `Boolean msg` 

`Misc.SendMessage(Double msg)`

- `Double msg` 

`Misc.SendMessage(Single num)`

- `Single num` 

`Misc.SendMessage(Int32 num, Int32 color)`

- `Int32 num` 
- `Int32 color` 

`Misc.SendMessage(Object obj, Int32 color)`

- `Object obj` 
- `Int32 color` 

`Misc.SendMessage(UInt32 num, Int32 color)`

- `UInt32 num` 
- `Int32 color` 

`Misc.SendToClient(String keys)`

- `String keys` 

`Misc.set_SharedScriptData(ConcurrentDictionary`2 value)`

- `ConcurrentDictionary`2 value` 

`Misc.SetSharedValue(String name, Object value)`

- `String name` 
- `Object value` 

`Misc.ShardName()`



`Misc.UnIgnoreObject(Int32 s)`

- `Int32 s` 

`Misc.UnIgnoreObject(Item i)`

- `Item i` 

`Misc.UnIgnoreObject(Mobile m)`

- `Mobile m` 

`Misc.WaitForContext(Item i, Int32 delay)`

- `Item i` 
- `Int32 delay` 

`Misc.WaitForContext(Int32 ser, Int32 delay)`

- `Int32 ser` 
- `Int32 delay` 

`Misc.WaitForContext(Mobile mob, Int32 delay)`

- `Mobile mob` 
- `Int32 delay` 

`Misc.WaitForMenu(Int32 delay)`

- `Int32 delay` 

`Misc.WaitForPrompt(Int32 delay)`

- `Int32 delay` 

`Misc.WaitForQueryString(Int32 delay)`

- `Int32 delay` 
