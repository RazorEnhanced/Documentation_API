:mod:`Gumps`
========================================
.. py:module:: Gumps



Methods
--------------

.. py:function:: Gumps.CloseGump(gumpid) -> Void


* gumpid: :mod:`UInt32` 




.. py:function:: Gumps.CurrentGump() -> UInt32







.. py:function:: Gumps.HasGump() -> Boolean







.. py:function:: Gumps.LastGumpGetLine(line) -> String


* line: :mod:`Int32` 




.. py:function:: Gumps.LastGumpGetLineList() -> List[String]







.. py:function:: Gumps.LastGumpRawData() -> String







.. py:function:: Gumps.LastGumpTextExist(text) -> Boolean


* text: :mod:`String` 




.. py:function:: Gumps.LastGumpTextExistByLine(line, text) -> Boolean


* line: :mod:`Int32` 
* text: :mod:`String` 




.. py:function:: Gumps.LastGumpTile() -> List[Int32]







.. py:function:: Gumps.ResetGump() -> Void







.. py:function:: Gumps.SendAction(gumpid, buttonid) -> Void


* gumpid: :mod:`UInt32` 
* buttonid: :mod:`Int32` 




.. py:function:: Gumps.SendAdvancedAction(gumpid, buttonid, switchs) -> Void


* gumpid: :mod:`UInt32` 
* buttonid: :mod:`Int32` 
* switchs: :mod:`List[Int32]` 




.. py:function:: Gumps.SendAdvancedAction(gumpid, buttonid, entryID, entryS) -> Void


* gumpid: :mod:`UInt32` 
* buttonid: :mod:`Int32` 
* entryID: :mod:`List[Int32]` 
* entryS: :mod:`List[String]` 




.. py:function:: Gumps.SendAdvancedAction(gumpid, buttonid, switchs, entryID, entryS) -> Void


* gumpid: :mod:`UInt32` 
* buttonid: :mod:`Int32` 
* switchs: :mod:`List[Int32]` 
* entryID: :mod:`List[Int32]` 
* entryS: :mod:`List[String]` 




.. py:function:: Gumps.WaitForGump(gumpid, delay) -> Void


* gumpid: :mod:`UInt32` 
* delay: :mod:`Int32` 



