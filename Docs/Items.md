# Items    

## Properties  
 
## Methods  
### Items.ApplyFilter
``` python
Items.ApplyFilter(Filter filter)
  Filter filter #
```
### Items.BackpackCount
``` python
Items.BackpackCount(Int32 itemid, Int32 color)
  Int32 itemid #
  Int32 color #-1
```
### Items.ContainerCount
``` python
Items.ContainerCount(Item container, Int32 itemid, Int32 color)
  Item container #
  Int32 itemid #
  Int32 color #-1
```
### Items.ContainerCount
``` python
Items.ContainerCount(Int32 serial, Int32 itemid, Int32 color)
  Int32 serial #
  Int32 itemid #
  Int32 color #-1
```
### Items.ContextExist
``` python
Items.ContextExist(Int32 serial, String name)
  Int32 serial #
  String name #
```
### Items.ContextExist
``` python
Items.ContextExist(Item i, String name)
  Item i #
  String name #
```
### Items.DropFromHand
``` python
Items.DropFromHand(Item item, Item bag)
  Item item #
  Item bag #
```
### Items.DropItemGroundSelf
``` python
Items.DropItemGroundSelf(Int32 serialitem, Int32 amount)
  Int32 serialitem #
  Int32 amount #0
```
### Items.DropItemGroundSelf
``` python
Items.DropItemGroundSelf(Item item, Int32 amount)
  Item item #
  Int32 amount #0
```
### Items.Equals
``` python
Items.Equals(Object obj)
  Object obj #
```
### Items.FindByID
``` python
Items.FindByID(Int32 itemid, Int32 color, Int32 container)
  Int32 itemid #
  Int32 color #
  Int32 container #
```
### Items.FindBySerial
``` python
Items.FindBySerial(Int32 serial)
  Int32 serial #
```
### Items.GetHashCode
``` python
Items.GetHashCode()

```
### Items.GetPropStringByIndex
``` python
Items.GetPropStringByIndex(Int32 serial, Int32 index)
  Int32 serial #
  Int32 index #
```
### Items.GetPropStringByIndex
``` python
Items.GetPropStringByIndex(Item item, Int32 index)
  Item item #
  Int32 index #
```
### Items.GetPropStringList
``` python
Items.GetPropStringList(Item item)
  Item item #
```
### Items.GetPropStringList
``` python
Items.GetPropStringList(Int32 serial)
  Int32 serial #
```
### Items.GetPropValue
``` python
Items.GetPropValue(Int32 serial, String name)
  Int32 serial #
  String name #
```
### Items.GetPropValue
``` python
Items.GetPropValue(Item item, String name)
  Item item #
  String name #
```
### Items.GetTotalResistProp
``` python
Items.GetTotalResistProp(Int32 serial)
  Int32 serial #
```
### Items.GetType
``` python
Items.GetType()

```
### Items.Hide
``` python
Items.Hide(Item item)
  Item item #
```
### Items.Hide
``` python
Items.Hide(Int32 serial)
  Int32 serial #
```
### Items.Lift
``` python
Items.Lift(Item item, Int32 amount)
  Item item #
  Int32 amount #
```
### Items.Message
``` python
Items.Message(Int32 serial, Int32 hue, String message)
  Int32 serial #
  Int32 hue #
  String message #
```
### Items.Message
``` python
Items.Message(Item item, Int32 hue, String message)
  Item item #
  Int32 hue #
  String message #
```
### Items.Move
``` python
Items.Move(Item source, Mobile destination, Int32 amount, Int32 x, Int32 y)
  Item source #
  Mobile destination #
  Int32 amount #
  Int32 x #
  Int32 y #
```
### Items.Move
``` python
Items.Move(Int32 source, Int32 destination, Int32 amount, Int32 x, Int32 y)
  Int32 source #
  Int32 destination #
  Int32 amount #
  Int32 x #
  Int32 y #
```
### Items.Move
``` python
Items.Move(Item source, Item destination, Int32 amount, Int32 x, Int32 y)
  Item source #
  Item destination #
  Int32 amount #
  Int32 x #
  Int32 y #
```
### Items.Move
``` python
Items.Move(Int32 source, Item destination, Int32 amount, Int32 x, Int32 y)
  Int32 source #
  Item destination #
  Int32 amount #
  Int32 x #
  Int32 y #
```
### Items.Move
``` python
Items.Move(Item source, Int32 destination, Int32 amount, Int32 x, Int32 y)
  Item source #
  Int32 destination #
  Int32 amount #
  Int32 x #
  Int32 y #
```
### Items.Move
``` python
Items.Move(Int32 source, Mobile destination, Int32 amount, Int32 x, Int32 y)
  Int32 source #
  Mobile destination #
  Int32 amount #
  Int32 x #
  Int32 y #
```
### Items.Move
``` python
Items.Move(Item source, Mobile destination, Int32 amount)
  Item source #
  Mobile destination #
  Int32 amount #
```
### Items.Move
``` python
Items.Move(Int32 source, Mobile destination, Int32 amount)
  Int32 source #
  Mobile destination #
  Int32 amount #
```
### Items.Move
``` python
Items.Move(Item source, Int32 destination, Int32 amount)
  Item source #
  Int32 destination #
  Int32 amount #
```
### Items.Move
``` python
Items.Move(Int32 source, Int32 destination, Int32 amount)
  Int32 source #
  Int32 destination #
  Int32 amount #
```
### Items.Move
``` python
Items.Move(Item source, Item destination, Int32 amount)
  Item source #
  Item destination #
  Int32 amount #
```
### Items.Move
``` python
Items.Move(Int32 source, Item destination, Int32 amount)
  Int32 source #
  Item destination #
  Int32 amount #
```
### Items.MoveOnGround
``` python
Items.MoveOnGround(Item source, Int32 amount, Int32 x, Int32 y, Int32 z)
  Item source #
  Int32 amount #
  Int32 x #
  Int32 y #
  Int32 z #
```
### Items.MoveOnGround
``` python
Items.MoveOnGround(Int32 source, Int32 amount, Int32 x, Int32 y, Int32 z)
  Int32 source #
  Int32 amount #
  Int32 x #
  Int32 y #
  Int32 z #
```
### Items.Select
``` python
Items.Select(List`1 items, String selector)
  List`1 items #
  String selector #
```
### Items.SingleClick
``` python
Items.SingleClick(Int32 itemserial)
  Int32 itemserial #
```
### Items.SingleClick
``` python
Items.SingleClick(Item item)
  Item item #
```
### Items.ToString
``` python
Items.ToString()

```
### Items.UseItem
``` python
Items.UseItem(Int32 itemSerial, Int32 targetSerial)
  Int32 itemSerial #
  Int32 targetSerial #
```
### Items.UseItem
``` python
Items.UseItem(Int32 itemserial)
  Int32 itemserial #
```
### Items.UseItem
``` python
Items.UseItem(Int32 itemSerial, Int32 targetSerial, Boolean wait)
  Int32 itemSerial #
  Int32 targetSerial #
  Boolean wait #
```
### Items.UseItem
``` python
Items.UseItem(Item item, Int32 target)
  Item item #
  Int32 target #
```
### Items.UseItem
``` python
Items.UseItem(Int32 item, EnhancedEntity target)
  Int32 item #
  EnhancedEntity target #
```
### Items.UseItem
``` python
Items.UseItem(Item item, EnhancedEntity target)
  Item item #
  EnhancedEntity target #
```
### Items.UseItem
``` python
Items.UseItem(Item item)
  Item item #
```
### Items.UseItemByID
``` python
Items.UseItemByID(Int32 itemid, Int32 color)
  Int32 itemid #
  Int32 color #-1
```
### Items.WaitForContents
``` python
Items.WaitForContents(Item bag, Int32 delay)
  Item bag #
  Int32 delay #
```
### Items.WaitForContents
``` python
Items.WaitForContents(Int32 serialbag, Int32 delay)
  Int32 serialbag #
  Int32 delay #
```
### Items.WaitForProps
``` python
Items.WaitForProps(Item i, Int32 delay)
  Item i #
  Int32 delay #
```
### Items.WaitForProps
``` python
Items.WaitForProps(Int32 itemserial, Int32 delay)
  Int32 itemserial #
  Int32 delay #
```