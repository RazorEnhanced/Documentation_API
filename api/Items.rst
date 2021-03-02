:mod:`Items`
========================================
.. py:module:: Items



Methods
--------------

.. py:function:: Items.ApplyFilter(filter) -> List[Item]


* filter: :mod:`Items.Filter` 




.. py:function:: Items.BackpackCount(itemid, color) -> Int32


* itemid: :mod:`Int32` 
* color: :mod:`Int32` 




.. py:function:: Items.ContainerCount(serial, itemid, color) -> Int32


* serial: :mod:`Int32` 
* itemid: :mod:`Int32` 
* color: :mod:`Int32` 




.. py:function:: Items.ContainerCount(container, itemid, color) -> Int32


* container: :mod:`Item` 
* itemid: :mod:`Int32` 
* color: :mod:`Int32` 




.. py:function:: Items.ContextExist(serial, name) -> Int32


* serial: :mod:`Int32` 
* name: :mod:`String` 




.. py:function:: Items.ContextExist(i, name) -> Int32


* i: :mod:`Item` 
* name: :mod:`String` 




.. py:function:: Items.DropFromHand(item, bag) -> Void


* item: :mod:`Item` 
* bag: :mod:`Item` 




.. py:function:: Items.DropItemGroundSelf(serialitem, amount) -> Void


* serialitem: :mod:`Int32` 
* amount: :mod:`Int32` 




.. py:function:: Items.DropItemGroundSelf(item, amount) -> Void


* item: :mod:`Item` 
* amount: :mod:`Int32` 




.. py:function:: Items.FindByID(itemid, color, container) -> Item


* itemid: :mod:`Int32` 
* color: :mod:`Int32` 
* container: :mod:`Int32` 




.. py:function:: Items.FindBySerial(serial) -> Item


* serial: :mod:`Int32` 




.. py:function:: Items.GetPropStringByIndex(serial, index) -> String


* serial: :mod:`Int32` 
* index: :mod:`Int32` 




.. py:function:: Items.GetPropStringByIndex(item, index) -> String


* item: :mod:`Item` 
* index: :mod:`Int32` 




.. py:function:: Items.GetPropStringList(item) -> List[String]


* item: :mod:`Item` 




.. py:function:: Items.GetPropStringList(serial) -> List[String]


* serial: :mod:`Int32` 




.. py:function:: Items.GetPropValue(serial, name) -> Single


* serial: :mod:`Int32` 
* name: :mod:`String` 




.. py:function:: Items.GetPropValue(item, name) -> Single


* item: :mod:`Item` 
* name: :mod:`String` 




.. py:function:: Items.GetTotalResistProp(serial) -> Single


* serial: :mod:`Int32` 




.. py:function:: Items.Hide(serial) -> Void


* serial: :mod:`Int32` 




.. py:function:: Items.Hide(item) -> Void


* item: :mod:`Item` 




.. py:function:: Items.Lift(item, amount) -> Void


* item: :mod:`Item` 
* amount: :mod:`Int32` 




.. py:function:: Items.Message(item, hue, message) -> Void


* item: :mod:`Item` 
* hue: :mod:`Int32` 
* message: :mod:`String` 




.. py:function:: Items.Message(serial, hue, message) -> Void


* serial: :mod:`Int32` 
* hue: :mod:`Int32` 
* message: :mod:`String` 




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
* destination: :mod:`Mobile` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Item` 
* destination: :mod:`Int32` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Int32` 
* destination: :mod:`Item` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Item` 
* destination: :mod:`Item` 
* amount: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Int32` 
* destination: :mod:`Int32` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Item` 
* destination: :mod:`Item` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Int32` 
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




.. py:function:: Items.Move(source, destination, amount, x, y) -> Void


* source: :mod:`Int32` 
* destination: :mod:`Mobile` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 




.. py:function:: Items.Move(source, destination, amount) -> Void


* source: :mod:`Int32` 
* destination: :mod:`Mobile` 
* amount: :mod:`Int32` 




.. py:function:: Items.MoveOnGround(source, amount, x, y, z) -> Void


* source: :mod:`Int32` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 
* z: :mod:`Int32` 




.. py:function:: Items.MoveOnGround(source, amount, x, y, z) -> Void


* source: :mod:`Item` 
* amount: :mod:`Int32` 
* x: :mod:`Int32` 
* y: :mod:`Int32` 
* z: :mod:`Int32` 




.. py:function:: Items.Select(items, selector) -> Item


* items: :mod:`List[Item]` 
* selector: :mod:`String` 




.. py:function:: Items.SingleClick(item) -> Void


* item: :mod:`Item` 




.. py:function:: Items.SingleClick(itemserial) -> Void


* itemserial: :mod:`Int32` 




.. py:function:: Items.UseItem(item, target) -> Void


* item: :mod:`Int32` 
* target: :mod:`EnhancedEntity` 




.. py:function:: Items.UseItem(itemserial) -> Void


* itemserial: :mod:`Int32` 




.. py:function:: Items.UseItem(itemSerial, targetSerial, wait) -> Void


* itemSerial: :mod:`Int32` 
* targetSerial: :mod:`Int32` 
* wait: :mod:`Boolean` 




.. py:function:: Items.UseItem(itemSerial, targetSerial) -> Void


* itemSerial: :mod:`Int32` 
* targetSerial: :mod:`Int32` 




.. py:function:: Items.UseItem(item, target) -> Void


* item: :mod:`Item` 
* target: :mod:`Int32` 




.. py:function:: Items.UseItem(item, target) -> Void


* item: :mod:`Item` 
* target: :mod:`EnhancedEntity` 




.. py:function:: Items.UseItem(item) -> Void


* item: :mod:`Item` 




.. py:function:: Items.UseItemByID(itemid, color) -> Boolean


* itemid: :mod:`Int32` 
* color: :mod:`Int32` 




.. py:function:: Items.WaitForContents(bag, delay) -> Void


* bag: :mod:`Item` 
* delay: :mod:`Int32` 




.. py:function:: Items.WaitForContents(serialbag, delay) -> Void


* serialbag: :mod:`Int32` 
* delay: :mod:`Int32` 




.. py:function:: Items.WaitForProps(i, delay) -> Void


* i: :mod:`Item` 
* delay: :mod:`Int32` 




.. py:function:: Items.WaitForProps(itemserial, delay) -> Void


* itemserial: :mod:`Int32` 
* delay: :mod:`Int32` 



