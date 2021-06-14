:mod:`Statics`
========================================
.. py:module:: Statics
   :synopsis: 
            <summary>
            The Statics class provides access to informations about the Map, down to the individual tile.
            When using this function it's important to remember the distinction between Land and Tile:
            Land
            ----
            For a given (X,Y,map) there can be only 1 (0 zero) Land item, and has 1 specific Z coordinate.
            
            Tile
            ----
            For a given (X,Y,map) there can be any number of Tile items.
            </summary>
        



Methods
--------------

.. py:function:: Statics.CheckDeedHouse(x, y) -> Boolean


* x: :mod:`Int32` X coordinate.
* y: :mod:`Int32` Y coordinate.


Check if the given Tile is occupied by a private house.
Need to be in-sight, on most servers the maximum distance is 18 tiles.

.. py:function:: Statics.GetLandFlag(itemid, flagname) -> Boolean


* itemid: :mod:`Int32` 
* flagname: :mod:`String` None
Translucent
Wall
Damaging
Impassable
Surface
Bridge
Window
NoShoot
Foliage
HoverOver
Roof
Door
Wet


Land: Check Flag value of a given Land item.

.. py:function:: Statics.GetLandID(x, y, map) -> Int32


* x: :mod:`Int32` X coordinate.
* y: :mod:`Int32` Y coordinate.
* map: :mod:`Int32` 0 = Felucca
            	1 = Trammel
2 = Ilshenar
3 = Malas
            	4 = Tokuno
            	5 = TerMur


Land: Return the StaticID of the Land item, give the coordinates and map.

.. py:function:: Statics.GetLandName(StaticID) -> String


* StaticID: :mod:`Int32` Land item StaticID.


Land: Get the name of a Land item given the StaticID.

.. py:function:: Statics.GetLandZ(x, y, map) -> Int32


* x: :mod:`Int32` X coordinate.
* y: :mod:`Int32` Y coordinate.
* map: :mod:`Int32` 0 = Felucca
            	1 = Trammel
2 = Ilshenar
3 = Malas
            	4 = Tokuno
            	5 = TerMur


Land: Return the Z coordinate (height) of the Land item, give the coordinates and map.

.. py:function:: Statics.GetStaticsLandInfo(x, y, map) -> Statics.TileInfo


* x: :mod:`Int32` X coordinate.
* y: :mod:`Int32` Y coordinate.
* map: :mod:`Int32` 0 = Felucca
            	1 = Trammel
2 = Ilshenar
3 = Malas
            	4 = Tokuno
            	5 = TerMur


Land: Return a TileInfo representing the Land item for a given X,Y, map.

.. py:function:: Statics.GetStaticsTileInfo(x, y, map) -> List[Statics.TileInfo]


* x: :mod:`Int32` X coordinate.
* y: :mod:`Int32` Y coordinate.
* map: :mod:`Int32` 0 = Felucca
            	1 = Trammel
2 = Ilshenar
3 = Malas
            	4 = Tokuno
            	5 = TerMur


Tile: Return a list of TileInfo representing the Tile items for a given X,Y, map.

.. py:function:: Statics.GetTileFlag(StaticID, flagname) -> Boolean


* StaticID: :mod:`Int32` StaticID of a Tile item.
* flagname: :mod:`String` None
Translucent
Wall
Damaging
Impassable
Surface
Bridge
Window
NoShoot
Foliage
HoverOver
Roof
Door
Wet


Tile: Check Flag value of a given Tile item.

.. py:function:: Statics.GetTileHeight(StaticID) -> Int32


* StaticID: :mod:`Int32` Tile item StaticID.


Tile: Get hight of a Tile item, in Z coordinate reference.

.. py:function:: Statics.GetTileName(StaticID) -> String


* StaticID: :mod:`Int32` Tile item StaticID.


Tile: Get the name of a Tile item given the StaticID.
