:mod:`Gumps`
========================================
.. py:module:: Gumps
   :synopsis: 
            <summary>
            The Gumps class is used to read and interact with in-game gumps, via scripting.
            
            NOTE
            ----
            During development of scripts that involves interecting with Gumps, is often needed to know gumpids and buttonids.
            For this purpose, can be particularly usefull to use *Inspect Gumps* and *Record*, top right, in the internal RE script editor.
            </summary>
        



Methods
--------------

.. py:function:: Gumps.CloseGump(gumpid) -> Void


* gumpid: :mod:`UInt32` ID of the gump


Close a specific Gump.

.. py:function:: Gumps.CurrentGump() -> UInt32





Return the ID of most recent, still open Gump.

.. py:function:: Gumps.HasGump() -> Boolean





Get status if have a gump open or not.

.. py:function:: Gumps.LastGumpGetLine(line_num) -> String


* line_num: :mod:`Int32` Number of the line.


Get a specific line from the most recent and still open Gump. Filter by line number.

.. py:function:: Gumps.LastGumpGetLineList() -> List[String]





Get all text from the most recent and still open Gump.

.. py:function:: Gumps.LastGumpRawData() -> String





Get the Raw Data of the most recent and still open Gump.

.. py:function:: Gumps.LastGumpRawText() -> List[String]





Get the Raw Text of the most recent and still open Gump.

.. py:function:: Gumps.LastGumpTextExist(text) -> Boolean


* text: :mod:`String` Text to search.


Search for text inside the most recent and still open Gump.

.. py:function:: Gumps.LastGumpTextExistByLine(line_num, text) -> Boolean


* line_num: :mod:`Int32` Number of the line.
* text: :mod:`String` Text to search.


Search for text, in a spacific line of the most recent and still open Gump.

.. py:function:: Gumps.LastGumpTile() -> List[Int32]





Get the list of Gump Tile (! this documentation is a stub !)

.. py:function:: Gumps.ResetGump() -> Void





Clean current status of Gumps.

.. py:function:: Gumps.SendAction(gumpid, buttonid) -> Void


* gumpid: :mod:`UInt32` ID of the gump.
* buttonid: :mod:`Int32` ID of the Button to press.


Send a Gump response by gumpid and buttonid.

.. py:function:: Gumps.SendAdvancedAction(gumpid, buttonid, switchlist_id, textlist_id, textlist_str) -> Void


* gumpid: :mod:`UInt32` 
* buttonid: :mod:`Int32` 
* switchlist_id: :mod:`List[Int32]` 
* textlist_id: :mod:`List[Int32]` 
* textlist_str: :mod:`List[String]` 




.. py:function:: Gumps.SendAdvancedAction(gumpid, buttonid, textlist_id, textlist_str) -> Void


* gumpid: :mod:`UInt32` 
* buttonid: :mod:`Int32` 
* textlist_id: :mod:`List[Int32]` 
* textlist_str: :mod:`List[String]` 




.. py:function:: Gumps.SendAdvancedAction(gumpid, buttonid, switchs) -> Void


* gumpid: :mod:`UInt32` 
* buttonid: :mod:`Int32` 
* switchs: :mod:`List[Int32]` 




.. py:function:: Gumps.WaitForGump(gumpid, delay) -> Void


* gumpid: :mod:`UInt32` ID of the gump. (0: any)
* delay: :mod:`Int32` Maximum wait, in milliseconds.


Waits for a specific Gump to appear, for a maximum amount of time. If gumpid is 0 it will match any Gump.
