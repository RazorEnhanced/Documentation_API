:mod:`Items`
========================================
.. py:module:: Items
   :synopsis: 
            <summary>
            The Items class provides a wide range of functions to search and interact with Items.
            </summary>
        



Methods
--------------

.. py:function:: Items.ApplyFilter(filter) -> List[Item]


* filter: :mod:`Items.Filter` A filter object.


Filter the global list of Items according to the options specified by the filter ( see: Items.Filter ).

.. py:function:: Items.BackpackCount(itemid, color) -> Int32


* itemid: :mod:`Int32` ItemID to search.
* color: :mod:`Int32` Color to search. (default -1: any color)


Count items in Player Backpack.

.. py:function:: Items.ContainerCount(serial, itemid, color, recursive) -> Int32


* serial: :mod:`Int32` 
* itemid: :mod:`Int32` 
* color: :mod:`Int32` 
* recursive: :mod:`Boolean` 




.. py:function:: Items.ContainerCount(container, itemid, color, recursive) -> Int32


* container: :mod:`Item` Serial or Item to search into.
* itemid: :mod:`Int32` ItemID of the item to search.
* color: :mod:`Int32` Color to match. (default: -1, any color)
* recursive: :mod:`Boolean` Search also in already open subcontainers.


Count items inside a container, summing also the amount in stacks.

.. py:function:: Items.ContextExist(i, name) -> Int32


* i: :mod:`Item` 
* name: :mod:`String` 




.. py:function:: Items.ContextExist(serial, name) -> Int32


* serial: :mod:`Int32` Serial or Item to check.
* name: :mod:`String` Name of the Context Manu entry


Check if Context Menu entry exists for an Item.

.. py:function:: Items.DropFromHand(item, container) -> Void


* item: :mod:`Item` Item object to drop.
* container: :mod:`Item` Target container.


Drop into a bag an Item currently held in-hand. ( see: Items.Lift )

.. py:function:: Items.DropItemGroundSelf(serialitem, amount) -> Void


* serialitem: :mod:`Int32` 
* amount: :mod:`Int32` 




.. py:function:: Items.DropItemGroundSelf(item, amount) -> Void


* item: :mod:`Item` Item object to drop.
* amount: :mod:`Int32` Amount to move. (default: 0, the whole stack)


Drop an Item on the ground, at the current Player position.
NOTE: On some server is not allowed to drop Items on tiles occupied by Mobiles and the Player.

.. py:function:: Items.FindByID(itemid, color, container, range, considerIgnoreList) -> Item


* itemid: :mod:`Int32` 
* color: :mod:`Int32` 
* container: :mod:`Int32` 
* range: :mod:`Int32` 
* considerIgnoreList: :mod:`Boolean` 




.. py:function:: Items.FindByID(itemid, color, container, recursive, considerIgnoreList) -> Item


* itemid: :mod:`Int32` ItemID filter.
* color: :mod:`Int32` Color filter. (-1: any, 0: natural )
* container: :mod:`Int32` Serial of the container to search. (-1: any Item)
* recursive: :mod:`Boolean` Search subcontainers. 
    True: all subcontainers
    False: only main
    1,2,n: Maximum subcontainer depth
* considerIgnoreList: :mod:`Boolean` True: Ignore Items are excluded - False: any Item.


Find a single Item matching specific ItemID, Color and Container. 
Optionally can search in all subcontaners or to a maximum depth in subcontainers.
Can use -1 on color for no chose color, can use -1 on container for search in all item in memory. The depth defaults to only the top but can search for # of sub containers.

.. py:function:: Items.FindBySerial(serial) -> Item


* serial: :mod:`Int32` Serial of the Item.


Search for a specific Item by using it Serial

.. py:function:: Items.GetImage(itemID, hue) -> Bitmap


* itemID: :mod:`Int32` ItemID to use.
* hue: :mod:`Int32` Optional: Color to apply. (Default 0, natural)


Get the Image on an Item by specifing the ItemID. Optinally is possible to apply a color.

.. py:function:: Items.GetPropStringByIndex(serial, index) -> String


* serial: :mod:`Int32` Serial or Item to read.
* index: :mod:`Int32` Number of the Property line.


Get a Property line, by index. if not found returns and empty string.

.. py:function:: Items.GetPropStringByIndex(item, index) -> String


* item: :mod:`Item` 
* index: :mod:`Int32` 




.. py:function:: Items.GetPropStringList(serial) -> List[String]


* serial: :mod:`Int32` Serial or Item to read.


Get string list of all Properties of an item, if item no props list is empty.

.. py:function:: Items.GetPropStringList(item) -> List[String]


* item: :mod:`Item` 




.. py:function:: Items.GetPropValue(serial, name) -> Single


* serial: :mod:`Int32` Serial or Item to read.
* name: :mod:`String` Name of the Propery.


Read the value of a Property.

.. py:function:: Items.GetPropValue(item, name) -> Single


* item: :mod:`Item` 
* name: :mod:`String` 




.. py:function:: Items.Hide(item) -> Void


* item: :mod:`Item` 




.. py:function:: Items.Hide(serial) -> Void


* serial: :mod:`Int32` Serial or Item to hide.


Hied an Item, affects only the player.

.. py:function:: Items.Lift(item, amount) -> Void


* item: :mod:`Item` Item object to Lift.
* amount: :mod:`Int32` Amount to lift. (0: the whole stack)


Lift an Item and hold it in-hand. ( see: Items.DropFromHand )

.. py:function:: Items.Message(serial, hue, message) -> Void


* serial: :mod:`Int32` 
* hue: :mod:`Int32` 
* message: :mod:`String` 




.. py:function:: Items.Message(item, hue, message) -> Void


* item: :mod:`Item` Serial or Item to display text on.
* hue: :mod:`Int32` Color of the message.
* message: :mod:`String` Message as


Display an in-game message on top of an Item, visibile only for the Player.

.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Int32` 
* destination: :mod:`Item` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Item` 
* destination: :mod:`Mobile` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Int32` 
* destination: :mod:`Int32` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Item` 
* destination: :mod:`Item` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Int32` 
* destination: :mod:`Mobile` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Item` 
* destination: :mod:`Int32` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Int32` 
* destination: :mod:`Mobile` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Int32` Serial or Item of the Item to move.
* destination: :mod:`Int32` Serial, Mobile or Item as destination.
* amount: :mod:`Int32` Amount to move (-1: the whole stack)
* x: :mod:`Int32` Optional: X coordinate inside the container.
* y: :mod:`Int32` Optional: Y coordinate inside the container.


Move an Item to a destination, which can be an Item or a Mobile.

.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Int32` 
* destination: :mod:`Item` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Item` 
* destination: :mod:`Mobile` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Item` 
* destination: :mod:`Item` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Item` 
* destination: :mod:`Int32` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 




.. py:function:: Items.MoveOnGround(source, amount, x, y, z) -> Void


* source: :mod:`Int32` Serial or Item to move.
* amount: :mod:`Int32` Amount of Items to move (0: the whole stack )
* x: :mod:`Int32` X world coordinates.
* y: :mod:`Int32` Y world coordinates.
* z: :mod:`Int32` Z world coordinates.


Move an Item on the ground to a specific location.

.. py:function:: Items.MoveOnGround(source, amount, x, y, z) -> Void


* source: :mod:`Item` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 
* z: :mod:`Int32` 




.. py:function:: Items.Select(items, selector) -> Item


* items: :mod:`List[Item]` 
* selector: :mod:`String` 




.. py:function:: Items.SetColor(serial, color) -> Void


* serial: :mod:`Int32` Serial of the Item.
* color: :mod:`Int32` Color as number. (default: -1, reset original color)


Change/override the Color of an Item, the change affects only Player client. The change is not persistent.
If the color is -1 or unspecified, the color of the item is restored.

.. py:function:: Items.SingleClick(itemserial) -> Void


* itemserial: :mod:`Int32` 




.. py:function:: Items.SingleClick(item) -> Void


* item: :mod:`Item` Serial or Item to click


Send a single click network event to the server.

.. py:function:: Items.UseItem(item, target) -> Void


* item: :mod:`Item` 
* target: :mod:`Int32` 




.. py:function:: Items.UseItem(item, target) -> Void


* item: :mod:`Item` 
* target: :mod:`EnhancedEntity` 




.. py:function:: Items.UseItem(item) -> Void


* item: :mod:`Item` 




.. py:function:: Items.UseItem(itemSerial, targetSerial) -> Void


* itemSerial: :mod:`Int32` 
* targetSerial: :mod:`Int32` 




.. py:function:: Items.UseItem(item, target) -> Void


* item: :mod:`Int32` 
* target: :mod:`EnhancedEntity` 




.. py:function:: Items.UseItem(itemSerial, targetSerial, wait) -> Void


* itemSerial: :mod:`Int32` Serial or Item to use.
* targetSerial: :mod:`Int32` Optional: Serial of the Item or Mobile target.
* wait: :mod:`Boolean` Optional: Wait for confirmation by the server. (default: True)


Use an Item, optionally is possible to specify a Item or Mobile target.
NOTE: The optional target may not work on some free shards. Use Target.Execute instead.

.. py:function:: Items.UseItem(itemserial) -> Void


* itemserial: :mod:`Int32` 




.. py:function:: Items.UseItemByID(itemid, color) -> Boolean


* itemid: :mod:`Int32` ItemID to be used.
* color: :mod:`Int32` Color to be used. (default: -1, any)


Use any item of a specific type, matching Item.ItemID. Optionally also of a specific color, matching Item.Hue.

.. py:function:: Items.WaitForContents(bag, delay) -> Void


* bag: :mod:`Item` Container as Item object.
* delay: :mod:`Int32` Maximum wait, in milliseconds.


Open a container an wait for the Items to load, for a maximum amount of time.

.. py:function:: Items.WaitForContents(bag_serial, delay) -> Void


* bag_serial: :mod:`Int32` Container as Item serial.
* delay: :mod:`Int32` 




.. py:function:: Items.WaitForProps(i, delay) -> Void


* i: :mod:`Item` 
* delay: :mod:`Int32` 




.. py:function:: Items.WaitForProps(itemserial, delay) -> Void


* itemserial: :mod:`Int32` Serial or Item read.
* delay: :mod:`Int32` Maximum waiting time, in milliseconds.


If not updated, request to the Properties of an Item, and wait for a maximum amount of time.
