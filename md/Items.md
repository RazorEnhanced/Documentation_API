# Items    

## Properties  
 
## Methods  
### Items.ApplyFilter
```
ApplyFilter(Filter filter) -> List`1
```
- __Filter__ **filter**
### Items.BackpackCount
```
BackpackCount(Int32 itemid, Int32 color) -> Int32
```
- __Int32__ **itemid** 
- __Int32__ **color** -1
### Items.ContainerCount
```
ContainerCount(Item container, Int32 itemid, Int32 color) -> Int32
```
- __Item__ **container** 
- __Int32__ **itemid** 
- __Int32__ **color** -1
### Items.ContainerCount
```
ContainerCount(Int32 serial, Int32 itemid, Int32 color) -> Int32
```
- __Int32__ **serial** 
- __Int32__ **itemid** 
- __Int32__ **color** -1
### Items.ContextExist
```
ContextExist(Int32 serial, String name) -> Int32
```
- __Int32__ **serial** 
- __String__ **name**
### Items.ContextExist
```
ContextExist(Item i, String name) -> Int32
```
- __Item__ **i** 
- __String__ **name**
### Items.DropFromHand
```
DropFromHand(Item item, Item bag) -> Void
```
- __Item__ **item** 
- __Item__ **bag**
### Items.DropItemGroundSelf
```
DropItemGroundSelf(Int32 serialitem, Int32 amount) -> Void
```
- __Int32__ **serialitem** 
- __Int32__ **amount** 0
### Items.DropItemGroundSelf
```
DropItemGroundSelf(Item item, Int32 amount) -> Void
```
- __Item__ **item** 
- __Int32__ **amount** 0
### Items.Equals
```
Equals(Object obj) -> Boolean
```
- __Object__ **obj**
### Items.FindByID
```
FindByID(Int32 itemid, Int32 color, Int32 container) -> Item
```
- __Int32__ **itemid** 
- __Int32__ **color** 
- __Int32__ **container**
### Items.FindBySerial
```
FindBySerial(Int32 serial) -> Item
```
- __Int32__ **serial**
### Items.GetHashCode
```
GetHashCode() -> Int32
```
### Items.GetPropStringByIndex
```
GetPropStringByIndex(Int32 serial, Int32 index) -> String
```
- __Int32__ **serial** 
- __Int32__ **index**
### Items.GetPropStringByIndex
```
GetPropStringByIndex(Item item, Int32 index) -> String
```
- __Item__ **item** 
- __Int32__ **index**
### Items.GetPropStringList
```
GetPropStringList(Item item) -> List`1
```
- __Item__ **item**
### Items.GetPropStringList
```
GetPropStringList(Int32 serial) -> List`1
```
- __Int32__ **serial**
### Items.GetPropValue
```
GetPropValue(Int32 serial, String name) -> Single
```
- __Int32__ **serial** 
- __String__ **name**
### Items.GetPropValue
```
GetPropValue(Item item, String name) -> Single
```
- __Item__ **item** 
- __String__ **name**
### Items.GetTotalResistProp
```
GetTotalResistProp(Int32 serial) -> Single
```
- __Int32__ **serial**
### Items.GetType
```
GetType() -> Type
```
### Items.Hide
```
Hide(Item item) -> Void
```
- __Item__ **item**
### Items.Hide
```
Hide(Int32 serial) -> Void
```
- __Int32__ **serial**
### Items.Lift
```
Lift(Item item, Int32 amount) -> Void
```
- __Item__ **item** 
- __Int32__ **amount**
### Items.Message
```
Message(Int32 serial, Int32 hue, String message) -> Void
```
- __Int32__ **serial** 
- __Int32__ **hue** 
- __String__ **message**
### Items.Message
```
Message(Item item, Int32 hue, String message) -> Void
```
- __Item__ **item** 
- __Int32__ **hue** 
- __String__ **message**
### Items.Move
```
Move(Item source, Mobile destination, Int32 amount, Int32 x, Int32 y) -> Void
```
- __Item__ **source** 
- __Mobile__ **destination** 
- __Int32__ **amount** 
- __Int32__ **x** 
- __Int32__ **y**
### Items.Move
```
Move(Int32 source, Int32 destination, Int32 amount, Int32 x, Int32 y) -> Void
```
- __Int32__ **source** 
- __Int32__ **destination** 
- __Int32__ **amount** 
- __Int32__ **x** 
- __Int32__ **y**
### Items.Move
```
Move(Item source, Item destination, Int32 amount, Int32 x, Int32 y) -> Void
```
- __Item__ **source** 
- __Item__ **destination** 
- __Int32__ **amount** 
- __Int32__ **x** 
- __Int32__ **y**
### Items.Move
```
Move(Int32 source, Item destination, Int32 amount, Int32 x, Int32 y) -> Void
```
- __Int32__ **source** 
- __Item__ **destination** 
- __Int32__ **amount** 
- __Int32__ **x** 
- __Int32__ **y**
### Items.Move
```
Move(Item source, Int32 destination, Int32 amount, Int32 x, Int32 y) -> Void
```
- __Item__ **source** 
- __Int32__ **destination** 
- __Int32__ **amount** 
- __Int32__ **x** 
- __Int32__ **y**
### Items.Move
```
Move(Int32 source, Mobile destination, Int32 amount, Int32 x, Int32 y) -> Void
```
- __Int32__ **source** 
- __Mobile__ **destination** 
- __Int32__ **amount** 
- __Int32__ **x** 
- __Int32__ **y**
### Items.Move
```
Move(Item source, Mobile destination, Int32 amount) -> Void
```
- __Item__ **source** 
- __Mobile__ **destination** 
- __Int32__ **amount**
### Items.Move
```
Move(Int32 source, Mobile destination, Int32 amount) -> Void
```
- __Int32__ **source** 
- __Mobile__ **destination** 
- __Int32__ **amount**
### Items.Move
```
Move(Item source, Int32 destination, Int32 amount) -> Void
```
- __Item__ **source** 
- __Int32__ **destination** 
- __Int32__ **amount**
### Items.Move
```
Move(Int32 source, Int32 destination, Int32 amount) -> Void
```
- __Int32__ **source** 
- __Int32__ **destination** 
- __Int32__ **amount**
### Items.Move
```
Move(Item source, Item destination, Int32 amount) -> Void
```
- __Item__ **source** 
- __Item__ **destination** 
- __Int32__ **amount**
### Items.Move
```
Move(Int32 source, Item destination, Int32 amount) -> Void
```
- __Int32__ **source** 
- __Item__ **destination** 
- __Int32__ **amount**
### Items.MoveOnGround
```
MoveOnGround(Item source, Int32 amount, Int32 x, Int32 y, Int32 z) -> Void
```
- __Item__ **source** 
- __Int32__ **amount** 
- __Int32__ **x** 
- __Int32__ **y** 
- __Int32__ **z**
### Items.MoveOnGround
```
MoveOnGround(Int32 source, Int32 amount, Int32 x, Int32 y, Int32 z) -> Void
```
- __Int32__ **source** 
- __Int32__ **amount** 
- __Int32__ **x** 
- __Int32__ **y** 
- __Int32__ **z**
### Items.Select
```
Select(List`1 items, String selector) -> Item
```
- __List`1__ **items** 
- __String__ **selector**
### Items.SingleClick
```
SingleClick(Int32 itemserial) -> Void
```
- __Int32__ **itemserial**
### Items.SingleClick
```
SingleClick(Item item) -> Void
```
- __Item__ **item**
### Items.ToString
```
ToString() -> String
```
### Items.UseItem
```
UseItem(Int32 itemSerial, Int32 targetSerial) -> Void
```
- __Int32__ **itemSerial** 
- __Int32__ **targetSerial**
### Items.UseItem
```
UseItem(Int32 itemserial) -> Void
```
- __Int32__ **itemserial**
### Items.UseItem
```
UseItem(Int32 itemSerial, Int32 targetSerial, Boolean wait) -> Void
```
- __Int32__ **itemSerial** 
- __Int32__ **targetSerial** 
- __Boolean__ **wait**
### Items.UseItem
```
UseItem(Item item, Int32 target) -> Void
```
- __Item__ **item** 
- __Int32__ **target**
### Items.UseItem
```
UseItem(Int32 item, EnhancedEntity target) -> Void
```
- __Int32__ **item** 
- __EnhancedEntity__ **target**
### Items.UseItem
```
UseItem(Item item, EnhancedEntity target) -> Void
```
- __Item__ **item** 
- __EnhancedEntity__ **target**
### Items.UseItem
```
UseItem(Item item) -> Void
```
- __Item__ **item**
### Items.UseItemByID
```
UseItemByID(Int32 itemid, Int32 color) -> Boolean
```
- __Int32__ **itemid** 
- __Int32__ **color** -1
### Items.WaitForContents
```
WaitForContents(Item bag, Int32 delay) -> Void
```
- __Item__ **bag** 
- __Int32__ **delay**
### Items.WaitForContents
```
WaitForContents(Int32 serialbag, Int32 delay) -> Void
```
- __Int32__ **serialbag** 
- __Int32__ **delay**
### Items.WaitForProps
```
WaitForProps(Item i, Int32 delay) -> Void
```
- __Item__ **i** 
- __Int32__ **delay**
### Items.WaitForProps
```
WaitForProps(Int32 itemserial, Int32 delay) -> Void
```
- __Int32__ **itemserial** 
- __Int32__ **delay**