:mod:`Misc`
========================================
.. py:module:: Misc
   :synopsis: 
            <summary>
            The Misc class contains general purpose functions of common use.
            </summary>
        



Methods
--------------

.. py:function:: Misc.Beep() -> Void





Play Beep system sound.

.. py:function:: Misc.CancelPrompt() -> Void





Cancel a prompt request.

.. py:function:: Misc.CaptureNow() -> Void





Creates a snapshot of the current UO window.

.. py:function:: Misc.CheckIgnoreObject(serial) -> Boolean


* serial: :mod:`Int32` Serial to check.


Check object from ignore list, return true if present. Can check Serial, Items or Mobiles

.. py:function:: Misc.CheckIgnoreObject(itm) -> Boolean


* itm: :mod:`Item` Item to check




.. py:function:: Misc.CheckIgnoreObject(mob) -> Boolean


* mob: :mod:`Mobile` Mobile to check




.. py:function:: Misc.CheckSharedValue(name) -> Boolean


* name: :mod:`String` Name of the value.


Check if a shared value exixts.

.. py:function:: Misc.ClearDragQueue() -> Void





Clear the Drag-n-Drop queue.

.. py:function:: Misc.ClearIgnore() -> Void





Clear ignore list from all object

.. py:function:: Misc.CloseBackpack() -> Void





Close the backpack. 
(OSI client only, no ClassicUO)

.. py:function:: Misc.CloseMenu() -> Void





Close opened Old Menu.

.. py:function:: Misc.ContextReply(serial, menu_name) -> Void


* serial: :mod:`Int32` 
* menu_name: :mod:`String` Name of the Entry as wirtten in-game.




.. py:function:: Misc.ContextReply(serial, respone_num) -> Void


* serial: :mod:`Int32` Serial of the Entity
* respone_num: :mod:`Int32` Poition of the option in the menu. Starts from 0.


Respond to a context menu on mobile or item. Menu ID is base zero, or can use string of menu text.

.. py:function:: Misc.ContextReply(mob, menu_num) -> Void


* mob: :mod:`Mobile` 
* menu_num: :mod:`Int32` 




.. py:function:: Misc.ContextReply(mob, menu_name) -> Void


* mob: :mod:`Mobile` 
* menu_name: :mod:`String` 




.. py:function:: Misc.ContextReply(itm, menu_name) -> Void


* itm: :mod:`Item` 
* menu_name: :mod:`String` 




.. py:function:: Misc.ContextReply(itm, menu_num) -> Void


* itm: :mod:`Item` 
* menu_num: :mod:`Int32` 




.. py:function:: Misc.CurrentScriptDirectory() -> String





Get the path to the Scripts directory.

.. py:function:: Misc.Disconnect() -> Void





Force client to disconnect.

.. py:function:: Misc.DistanceSqrt(point_a, point_b) -> Double


* point_a: :mod:`Point3D` First coordinates.
* point_b: :mod:`Point3D` Second coordinates.


Compute the distance between 2 Point3D using pitagora's.

.. py:function:: Misc.ExportPythonAPI(path, pretty) -> Void


* path: :mod:`String` Name of the output file. (default: Config/AutoComplete.json )
* pretty: :mod:`Boolean` Print a readable JSON. (default: True )


Return a string containing list RE Python API list in JSON format.

.. py:function:: Misc.FilterSeason(enable, seasonFlag) -> Void


* enable: :mod:`Boolean` True: enable seasons filter
* seasonFlag: :mod:`UInt32` 0: Spring (default fallback)
1: Summer
2: Fall
3: Winter
4: Desolation


Enable or disable the Seasons filter forcing a specific season
Season filter state will be saved on logout but not the season flag that will be recovered.

.. py:function:: Misc.FocusUOWindow() -> Void





Set UoClient window in focus or restore if minimized.

.. py:function:: Misc.GetContPosition() -> Point





Get the position of the currently active Gump/Container.
(OSI client only, no ClassicUO)

.. py:function:: Misc.GetMapInfo(serial) -> Misc.MapInfo


* serial: :mod:`UInt32` Serial of the object.


Get MapInfo about a Mobile or Item using the serial

.. py:function:: Misc.GetMenuTitle() -> String





Get the title of title for open Old Menu.

.. py:function:: Misc.HasMenu() -> Boolean





Check if an Old Menu is open.

.. py:function:: Misc.HasPrompt() -> Boolean





Check if have a prompt request.

.. py:function:: Misc.HasQueryString() -> Boolean





Check if a have a query string menu opened, return true or false.

.. py:function:: Misc.IgnoreObject(serial) -> Void


* serial: :mod:`Int32` Serial to ignore.


Add an entiry to the ignore list. Can ignore Serial, Items or Mobiles.

.. py:function:: Misc.IgnoreObject(mob) -> Void


* mob: :mod:`Mobile` Mobile to ignore




.. py:function:: Misc.IgnoreObject(itm) -> Void


* itm: :mod:`Item` Item to ignore




.. py:function:: Misc.Inspect() -> Void





Prompt the user with a Target. Open the inspector for the selected target.

.. py:function:: Misc.LastHotKey() -> HotKeyEvent





Returns the latest HotKey recorded by razor as HotKeyEvent object.

.. py:function:: Misc.MenuContain(text) -> Boolean


* text: :mod:`String` Text to search.


Search in open Old Menu if contains a specific text.

.. py:function:: Misc.MenuResponse(text) -> Void


* text: :mod:`String` Name of subitem to respond.


Perform a menu response by subitem name. If item not exist close menu.

.. py:function:: Misc.MouseLocation() -> Point





Returns a point with the X and Y coordinates of the mouse relative to the UO Window

.. py:function:: Misc.MouseMove(posX, posY) -> Void


* posX: :mod:`Int32` X screen coordinate.
* posY: :mod:`Int32` Y screen coordinate.


Moves the mouse pointer to the position X,Y relative to the UO window

.. py:function:: Misc.NextContPosition(x, y) -> Void


* x: :mod:`Int32` X coordinate.
* y: :mod:`Int32` Y coordinate.


Return the X,Y of the next container, relative to the game window.
(OSI client only, no ClassicUO)

.. py:function:: Misc.NoOperation() -> Void





Just do nothing and enjot the present moment.

.. py:function:: Misc.NoRunStealthStatus() -> Boolean





Get the status of "No Run When Stealth" via scripting.

.. py:function:: Misc.NoRunStealthToggle(enable) -> Void


* enable: :mod:`Boolean` True: enable the option.


Set "No Run When Stealth" via scripting. Changes via scripting are not persistents.

.. py:function:: Misc.OpenPaperdoll() -> Void





Open the backpack. 
(OSI client only, no ClassicUO)

.. py:function:: Misc.Pause(millisec) -> Void


* millisec: :mod:`Int32` Pause duration, in milliseconds.


Pause the script for a given amount of time.

.. py:function:: Misc.PetRename(mob, name) -> Void


* mob: :mod:`Mobile` Mobile object representing the pet.
* name: :mod:`String` 




.. py:function:: Misc.PetRename(serial, name) -> Void


* serial: :mod:`Int32` Serial of the pet.
* name: :mod:`String` New name to set.


Rename a specific pet.

.. py:function:: Misc.QueryStringResponse(okcancel, response) -> Void


* okcancel: :mod:`Boolean` OK Button
* response: :mod:`String` Cancel Button


Perform a query string response by ok or cancel button and specific response string.

.. py:function:: Misc.ReadSharedValue(name) -> Object


* name: :mod:`String` Name of the value.


Get a Shared Value, if value not exist return null.
Shared values are accessible by every script.

.. py:function:: Misc.RemoveSharedValue(name) -> Void


* name: :mod:`String` Name of the value.


Remove a Shared Value.

.. py:function:: Misc.ResetPrompt() -> Void





Reset a prompt response.

.. py:function:: Misc.ResponsePrompt(text) -> Void


* text: :mod:`String` Text of the response.


Response a prompt request. Often used to rename runes and similar.

.. py:function:: Misc.Resync() -> Void





Trigger a client ReSync.

.. py:function:: Misc.ScriptRun(scriptfile) -> Void


* scriptfile: :mod:`String` Name of the script.


Run a script by file name, Script must be present in script grid.

.. py:function:: Misc.ScriptStatus(scriptfile) -> Boolean


* scriptfile: :mod:`String` 


Get status of script if running or not, Script must be present in script grid.

.. py:function:: Misc.ScriptStop(scriptfile) -> Void


* scriptfile: :mod:`String` Name of the script.


Stop a script by file name, Script must be present in script grid.

.. py:function:: Misc.ScriptStopAll() -> Void





Stop all script running.

.. py:function:: Misc.SendMessage(msg, wait) -> Void


* msg: :mod:`String` 
* wait: :mod:`Boolean` 




.. py:function:: Misc.SendMessage(msg, color, wait) -> Void


* msg: :mod:`String` The object to print.
* color: :mod:`Int32` Color of the message.
* wait: :mod:`Boolean` True: Wait for confimation. - False: Returns instatnly.


Send a message to the client.

.. py:function:: Misc.SendMessage(obj, color) -> Void


* obj: :mod:`Object` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendMessage(num) -> Void


* num: :mod:`Int32` 




.. py:function:: Misc.SendMessage(obj) -> Void


* obj: :mod:`Object` 




.. py:function:: Misc.SendMessage(num) -> Void


* num: :mod:`UInt32` 




.. py:function:: Misc.SendMessage(msg) -> Void


* msg: :mod:`Double` 




.. py:function:: Misc.SendMessage(msg, color) -> Void


* msg: :mod:`Double` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendMessage(msg) -> Void


* msg: :mod:`Boolean` 




.. py:function:: Misc.SendMessage(num) -> Void


* num: :mod:`Single` 




.. py:function:: Misc.SendMessage(num, color) -> Void


* num: :mod:`Int32` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendMessage(num, color) -> Void


* num: :mod:`UInt32` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendMessage(msg, color) -> Void


* msg: :mod:`Boolean` 
* color: :mod:`Int32` 




.. py:function:: Misc.SendToClient(keys) -> Void


* keys: :mod:`String` List of keys.


Send to the client a list of keystrokes. Can contain control characters: 
- Send Control+Key: ctrl+u: ^u
- Send ENTER: {Enter}
Note: some keys don't work with ClassicUO (es: {Enter} )

.. py:function:: Misc.SetSharedValue(name, value) -> Void


* name: :mod:`String` Name of the value.
* value: :mod:`Object` Value to set.


Set a Shared Value by specific name, if value exist he repalce value.
Shared values are accessible by every script.

.. py:function:: Misc.ShardName() -> String





Get the name of the shard.

.. py:function:: Misc.UnIgnoreObject(mob) -> Void


* mob: :mod:`Mobile` Item to unignore




.. py:function:: Misc.UnIgnoreObject(itm) -> Void


* itm: :mod:`Item` Item to unignore.




.. py:function:: Misc.UnIgnoreObject(serial) -> Void


* serial: :mod:`Int32` Serial to unignore.


Remove object from ignore list. Can remove serial, items or mobiles

.. py:function:: Misc.WaitForContext(serial, delay) -> List[Misc.Context]


* serial: :mod:`Int32` Serial of the entity.
* delay: :mod:`Int32` Maximum wait.


Wait for Context Menu to appear, for a maximum amount of time. Usable on an Item or Mobile.

.. py:function:: Misc.WaitForContext(itm, delay) -> List[Misc.Context]


* itm: :mod:`Item` Entity as Item object.
* delay: :mod:`Int32` 




.. py:function:: Misc.WaitForContext(mob, delay) -> List[Misc.Context]


* mob: :mod:`Mobile` Entity as Item object.
* delay: :mod:`Int32` 




.. py:function:: Misc.WaitForMenu(delay) -> Boolean


* delay: :mod:`Int32` Maximum wait, in milliseconds.


Pause script until server send an Old Menu, for a maximum amount of time.

.. py:function:: Misc.WaitForPrompt(delay) -> Boolean


* delay: :mod:`Int32` Maximum wait time.


Wait for a prompt for a maximum amount of time.

.. py:function:: Misc.WaitForQueryString(delay) -> Boolean


* delay: :mod:`Int32` Maximum wait, in milliseconds.


Pause script until server send query string request, for a maximum amount of time.
