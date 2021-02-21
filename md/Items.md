# Items    

## Properties  
 
## Methods  
### Items.ApplyFilter
```
Items.ApplyFilter(filter) -> List`1
```
- **filter**: Filter
### Items.BackpackCount
```
Items.BackpackCount(itemid, color) -> Int32
```
- **itemid**: Int32 
- **color**: Int32 -1
### Items.ContainerCount
```
Items.ContainerCount(container, itemid, color) -> Int32
```
- **container**: Item 
- **itemid**: Int32 
- **color**: Int32 -1
### Items.ContainerCount
```
Items.ContainerCount(serial, itemid, color) -> Int32
```
- **serial**: Int32 
- **itemid**: Int32 
- **color**: Int32 -1
### Items.ContextExist
```
Items.ContextExist(serial, name) -> Int32
```
- **serial**: Int32 
- **name**: String
### Items.ContextExist
```
Items.ContextExist(i, name) -> Int32
```
- **i**: Item 
- **name**: String
### Items.DropFromHand
```
Items.DropFromHand(item, bag) -> Void
```
- **item**: Item 
- **bag**: Item
### Items.DropItemGroundSelf
```
Items.DropItemGroundSelf(serialitem, amount) -> Void
```
- **serialitem**: Int32 
- **amount**: Int32 0
### Items.DropItemGroundSelf
```
Items.DropItemGroundSelf(item, amount) -> Void
```
- **item**: Item 
- **amount**: Int32 0
### Items.Equals
```
Items.Equals(obj) -> Boolean
```
- **obj**: Object
### Items.FindByID
```
Items.FindByID(itemid, color, container) -> Item
```
- **itemid**: Int32 
- **color**: Int32 
- **container**: Int32
### Items.FindBySerial
```
Items.FindBySerial(serial) -> Item
```
- **serial**: Int32
### Items.GetHashCode
```
Items.GetHashCode() -> Int32
```
### Items.GetPropStringByIndex
```
Items.GetPropStringByIndex(serial, index) -> String
```
- **serial**: Int32 
- **index**: Int32
### Items.GetPropStringByIndex
```
Items.GetPropStringByIndex(item, index) -> String
```
- **item**: Item 
- **index**: Int32
### Items.GetPropStringList
```
Items.GetPropStringList(item) -> List`1
```
- **item**: Item
### Items.GetPropStringList
```
Items.GetPropStringList(serial) -> List`1
```
- **serial**: Int32
### Items.GetPropValue
```
Items.GetPropValue(serial, name) -> Single
```
- **serial**: Int32 
- **name**: String
### Items.GetPropValue
```
Items.GetPropValue(item, name) -> Single
```
- **item**: Item 
- **name**: String
### Items.GetTotalResistProp
```
Items.GetTotalResistProp(serial) -> Single
```
- **serial**: Int32
### Items.GetType
```
Items.GetType() -> Type
```
### Items.Hide
```
Items.Hide(item) -> Void
```
- **item**: Item
### Items.Hide
```
Items.Hide(serial) -> Void
```
- **serial**: Int32
### Items.Lift
```
Items.Lift(item, amount) -> Void
```
- **item**: Item 
- **amount**: Int32
### Items.Message
```
Items.Message(serial, hue, message) -> Void
```
- **serial**: Int32 
- **hue**: Int32 
- **message**: String
### Items.Message
```
Items.Message(item, hue, message) -> Void
```
- **item**: Item 
- **hue**: Int32 
- **message**: String
### Items.Move
```
Items.Move(source, destination, amount, x, y) -> Void
```
- **source**: Item 
- **destination**: Mobile 
- **amount**: Int32 
- **x**: Int32 
- **y**: Int32
### Items.Move
```
Items.Move(source, destination, amount, x, y) -> Void
```
- **source**: Int32 
- **destination**: Int32 
- **amount**: Int32 
- **x**: Int32 
- **y**: Int32
### Items.Move
```
Items.Move(source, destination, amount, x, y) -> Void
```
- **source**: Item 
- **destination**: Item 
- **amount**: Int32 
- **x**: Int32 
- **y**: Int32
### Items.Move
```
Items.Move(source, destination, amount, x, y) -> Void
```
- **source**: Int32 
- **destination**: Item 
- **amount**: Int32 
- **x**: Int32 
- **y**: Int32
### Items.Move
```
Items.Move(source, destination, amount, x, y) -> Void
```
- **source**: Item 
- **destination**: Int32 
- **amount**: Int32 
- **x**: Int32 
- **y**: Int32
### Items.Move
```
Items.Move(source, destination, amount, x, y) -> Void
```
- **source**: Int32 
- **destination**: Mobile 
- **amount**: Int32 
- **x**: Int32 
- **y**: Int32
### Items.Move
```
Items.Move(source, destination, amount) -> Void
```
- **source**: Item 
- **destination**: Mobile 
- **amount**: Int32
### Items.Move
```
Items.Move(source, destination, amount) -> Void
```
- **source**: Int32 
- **destination**: Mobile 
- **amount**: Int32
### Items.Move
```
Items.Move(source, destination, amount) -> Void
```
- **source**: Item 
- **destination**: Int32 
- **amount**: Int32
### Items.Move
```
Items.Move(source, destination, amount) -> Void
```
- **source**: Int32 
- **destination**: Int32 
- **amount**: Int32
### Items.Move
```
Items.Move(source, destination, amount) -> Void
```
- **source**: Item 
- **destination**: Item 
- **amount**: Int32
### Items.Move
```
Items.Move(source, destination, amount) -> Void
```
- **source**: Int32 
- **destination**: Item 
- **amount**: Int32
### Items.MoveOnGround
```
Items.MoveOnGround(source, amount, x, y, z) -> Void
```
- **source**: Item 
- **amount**: Int32 
- **x**: Int32 
- **y**: Int32 
- **z**: Int32
### Items.MoveOnGround
```
Items.MoveOnGround(source, amount, x, y, z) -> Void
```
- **source**: Int32 
- **amount**: Int32 
- **x**: Int32 
- **y**: Int32 
- **z**: Int32
### Items.Select
```
Items.Select(items, selector) -> Item
```
- **items**: List`1 
- **selector**: String
### Items.SingleClick
```
Items.SingleClick(itemserial) -> Void
```
- **itemserial**: Int32
### Items.SingleClick
```
Items.SingleClick(item) -> Void
```
- **item**: Item
### Items.ToString
```
Items.ToString() -> String
```
### Items.UseItem
```
Items.UseItem(itemSerial, targetSerial) -> Void
```
- **itemSerial**: Int32 
- **targetSerial**: Int32
### Items.UseItem
```
Items.UseItem(itemserial) -> Void
```
- **itemserial**: Int32
### Items.UseItem
```
Items.UseItem(itemSerial, targetSerial, wait) -> Void
```
- **itemSerial**: Int32 
- **targetSerial**: Int32 
- **wait**: Boolean
### Items.UseItem
```
Items.UseItem(item, target) -> Void
```
- **item**: Item 
- **target**: Int32
### Items.UseItem
```
Items.UseItem(item, target) -> Void
```
- **item**: Int32 
- **target**: EnhancedEntity
### Items.UseItem
```
Items.UseItem(item, target) -> Void
```
- **item**: Item 
- **target**: EnhancedEntity
### Items.UseItem
```
Items.UseItem(item) -> Void
```
- **item**: Item
### Items.UseItemByID
```
Items.UseItemByID(itemid, color) -> Boolean
```
- **itemid**: Int32 
- **color**: Int32 -1
### Items.WaitForContents
```
Items.WaitForContents(bag, delay) -> Void
```
- **bag**: Item 
- **delay**: Int32
### Items.WaitForContents
```
Items.WaitForContents(serialbag, delay) -> Void
```
- **serialbag**: Int32 
- **delay**: Int32
### Items.WaitForProps
```
Items.WaitForProps(i, delay) -> Void
```
- **i**: Item 
- **delay**: Int32
### Items.WaitForProps
```
Items.WaitForProps(itemserial, delay) -> Void
```
- **itemserial**: Int32 
- **delay**: Int32