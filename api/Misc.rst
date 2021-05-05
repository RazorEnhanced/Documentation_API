:mod:`Misc`
========================================
.. py:module:: Misc


Properties
----------------
* Misc.SharedScriptData :mod:`Dictionary[String, Object]`


Methods
--------------

.. py:function:: Misc.Beep() -> Void







.. py:function:: Misc.CancelPrompt() -> Void







.. py:function:: Misc.CaptureNow() -> Void







.. py:function:: Misc.CheckIgnoreObject(m) -> Boolean


* m: :mod:`Mobile` 




.. py:function:: Misc.CheckIgnoreObject(s) -> Boolean


* s: :mod:`Int32` 




.. py:function:: Misc.CheckIgnoreObject(i) -> Boolean


* i: :mod:`Item` 




.. py:function:: Misc.CheckSharedValue(name) -> Boolean


* name: :mod:`String` 




.. py:function:: Misc.ClearDragQueue() -> Void







.. py:function:: Misc.ClearIgnore() -> Void







.. py:function:: Misc.CloseBackpack() -> Void







.. py:function:: Misc.CloseMenu() -> Void







.. py:function:: Misc.ContextReply(mob, idx) -> Void


* mob: :mod:`Mobile` 
* idx: :mod:`Int32` 




.. py:function:: Misc.ContextReply(item, idx) -> Void


* item: :mod:`Item` 
* idx: :mod:`Int32` 




.. py:function:: Misc.ContextReply(mob, menuname) -> Void


* mob: :mod:`Mobile` 
* menuname: :mod:`String` 




.. py:function:: Misc.ContextReply(item, menuname) -> Void


* item: :mod:`Item` 
* menuname: :mod:`String` 




.. py:function:: Misc.ContextReply(serial, menuname) -> Void


* serial: :mod:`Int32` 
* menuname: :mod:`String` 




.. py:function:: Misc.ContextReply(serial, idx) -> Void


* serial: :mod:`Int32` 
* idx: :mod:`Int32` 




.. py:function:: Misc.CurrentScriptDirectory() -> String







.. py:function:: Misc.Disconnect() -> Void







.. py:function:: Misc.DistanceSqrt(a, b) -> Double


* a: :mod:`Point3D` 
* b: :mod:`Point3D` 




.. py:function:: Misc.ExportPythonAPI(path, pretty) -> Void


* path: :mod:`String` Default: RazorEnhanced.json
* pretty: :mod:`Boolean` Default: True - Export a more readble version | False - Export a more compact version


Return a string containing list RE Python API list in JSON format.

.. py:function:: Misc.FocusUOWindow() -> Void







.. py:function:: Misc.GetContPosition() -> Point







.. py:function:: Misc.GetMapInfo(serial) -> Misc.MapInfo


* serial: :mod:`UInt32` 




.. py:function:: Misc.GetMenuTitle() -> String







.. py:function:: Misc.HasMenu() -> Boolean







.. py:function:: Misc.HasPrompt() -> Boolean







.. py:function:: Misc.HasQueryString() -> Boolean







.. py:function:: Misc.IgnoreObject(s) -> Void


* s: :mod:`Int32` 




.. py:function:: Misc.IgnoreObject(m) -> Void


* m: :mod:`Mobile` 




.. py:function:: Misc.IgnoreObject(i) -> Void


* i: :mod:`Item` 




.. py:function:: Misc.Inspect() -> Void







.. py:function:: Misc.LastHotKey() -> HotKeyEvent





Returns the latest HotKeyEvent recorded by razor.
The HotKeyEvent has 2 properties:
hke.Key: enum System.Windows.Forms.Keys
hke.Timestamp: double repesenting the UnixTimestamp, compatible with python's time.time()

.. py:function:: Misc.MenuContain(submenu) -> Boolean


* submenu: :mod:`String` 




.. py:function:: Misc.MenuResponse(submenu) -> Void


* submenu: :mod:`String` 




.. py:function:: Misc.MouseLocation() -> Point







.. py:function:: Misc.MouseMove(posX, posY) -> Void


* posX: :mod:`Int32` 
* posY: :mod:`Int32` 




.. py:function:: Misc.NextContPosition(x, y) -> Void


* x: :mod:`Int32` 
* y: :mod:`Int32` 




.. py:function:: Misc.NoOperation() -> Void







.. py:function:: Misc.NoRunStealthStatus() -> Boolean







.. py:function:: Misc.NoRunStealthToggle(enable) -> Void


* enable: :mod:`Boolean` 




.. py:function:: Misc.OpenPaperdoll() -> Void







.. py:function:: Misc.Pause(mseconds) -> Void


* mseconds: :mod:`Int32` 




.. py:function:: Misc.PetRename(serial, name) -> Void


* serial: :mod:`Int32` 
* name: :mod:`String` 




.. py:function:: Misc.PetRename(mob, name) -> Void


* mob: :mod:`Mobile` 
* name: :mod:`String` 




.. py:function:: Misc.QueryStringResponse(okcancel, response) -> Void


* okcancel: :mod:`Boolean` 
* response: :mod:`String` 




.. py:function:: Misc.ReadSharedValue(name) -> Object


* name: :mod:`String` 




.. py:function:: Misc.RemoveSharedValue(name) -> Void


* name: :mod:`String` 




.. py:function:: Misc.ResetPrompt() -> Void







.. py:function:: Misc.ResponsePrompt(text) -> Void


* text: :mod:`String` 




.. py:function:: Misc.Resync() -> Void







.. py:function:: Misc.ScriptRun(scriptfile) -> Void


* scriptfile: :mod:`String` 




.. py:function:: Misc.ScriptStatus(scriptfile) -> Boolean


* scriptfile: :mod:`String` 




.. py:function:: Misc.ScriptStop(scriptfile) -> Void


* scriptfile: :mod:`String` 




.. py:function:: Misc.ScriptStopAll() -> Void







.. py:function:: Misc.SendMessage(msg, wait) -> Void


* msg: :mod:`String` 
* wait: :mod:`Boolean` 




.. py:function:: Misc.SendMessage(msg) -> Void


* msg: :mod:`Boolean` 




.. py:function:: Misc.SendMessage(num) -> Void


* num: :mod:`Int32` 




.. py:function:: Misc.SendMessage(obj) -> Void


* obj: :mod:`Object` 




.. py:function:: Misc.SendMessage(num) -> Void


* num: :mod:`UInt32` 




.. py:function:: Misc.SendMessage(msg) -> Void


* msg: :mod:`Double` 




.. py:function:: Misc.SendMessage(num) -> Void


* num: :mod:`Single` 




.. py:function:: Misc.SendMessage(obj, color) -> Void


* obj: :mod:`Object` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendMessage(num, color) -> Void


* num: :mod:`Int32` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendMessage(msg, color) -> Void


* msg: :mod:`Boolean` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendMessage(msg, color) -> Void


* msg: :mod:`Double` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendMessage(num, color) -> Void


* num: :mod:`UInt32` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendToClient(keys) -> Void


* keys: :mod:`String` 




.. py:function:: Misc.SetSharedValue(name, value) -> Void


* name: :mod:`String` 
* value: :mod:`Object` 




.. py:function:: Misc.ShardName() -> String







.. py:function:: Misc.UnIgnoreObject(s) -> Void


* s: :mod:`Int32` 




.. py:function:: Misc.UnIgnoreObject(m) -> Void


* m: :mod:`Mobile` 




.. py:function:: Misc.UnIgnoreObject(i) -> Void


* i: :mod:`Item` 




.. py:function:: Misc.WaitForContext(ser, delay) -> List[Misc.Context]


* ser: :mod:`Int32` 
* delay: :mod:`Int32` 




.. py:function:: Misc.WaitForContext(mob, delay) -> List[Misc.Context]


* mob: :mod:`Mobile` 
* delay: :mod:`Int32` 




.. py:function:: Misc.WaitForContext(i, delay) -> List[Misc.Context]


* i: :mod:`Item` 
* delay: :mod:`Int32` 




.. py:function:: Misc.WaitForMenu(delay) -> Void


* delay: :mod:`Int32` 




.. py:function:: Misc.WaitForPrompt(delay) -> Void


* delay: :mod:`Int32` 




.. py:function:: Misc.WaitForQueryString(delay) -> Void


* delay: :mod:`Int32` 



