# Mobiles    

## Properties  
 
## Methods  
### Mobiles.ApplyFilter
```
ApplyFilter(Filter filter) -> List`1
```
- __Filter__ **filter**
### Mobiles.ContextExist
```
ContextExist(Int32 serial, String name) -> Int32
```
- __Int32__ **serial** 
- __String__ **name**
### Mobiles.ContextExist
```
ContextExist(Mobile mob, String name) -> Int32
```
- __Mobile__ **mob** 
- __String__ **name**
### Mobiles.Equals
```
Equals(Object obj) -> Boolean
```
- __Object__ **obj**
### Mobiles.FindBySerial
```
FindBySerial(Int32 serial) -> Mobile
```
- __Int32__ **serial**
### Mobiles.GetHashCode
```
GetHashCode() -> Int32
```
### Mobiles.GetPropStringByIndex
```
GetPropStringByIndex(Int32 serial, Int32 index) -> String
```
- __Int32__ **serial** 
- __Int32__ **index**
### Mobiles.GetPropStringByIndex
```
GetPropStringByIndex(Mobile mob, Int32 index) -> String
```
- __Mobile__ **mob** 
- __Int32__ **index**
### Mobiles.GetPropStringList
```
GetPropStringList(Mobile mob) -> List`1
```
- __Mobile__ **mob**
### Mobiles.GetPropStringList
```
GetPropStringList(Int32 serial) -> List`1
```
- __Int32__ **serial**
### Mobiles.GetPropValue
```
GetPropValue(Int32 serial, String name) -> Single
```
- __Int32__ **serial** 
- __String__ **name**
### Mobiles.GetPropValue
```
GetPropValue(Mobile mob, String name) -> Single
```
- __Mobile__ **mob** 
- __String__ **name**
### Mobiles.GetTrackingInfo
```
GetTrackingInfo() -> LastTrackingInfo
```
### Mobiles.GetType
```
GetType() -> Type
```
### Mobiles.Message
```
Message(Mobile mobile, Int32 hue, String message, Boolean wait) -> Void
```
- __Mobile__ **mobile** 
- __Int32__ **hue** 
- __String__ **message** 
- __Boolean__ **wait** True
### Mobiles.Message
```
Message(Int32 serial, Int32 hue, String message, Boolean wait) -> Void
```
- __Int32__ **serial** 
- __Int32__ **hue** 
- __String__ **message** 
- __Boolean__ **wait** True
### Mobiles.Select
```
Select(List`1 mobiles, String selector) -> Mobile
```
- __List`1__ **mobiles** 
- __String__ **selector**
### Mobiles.SingleClick
```
SingleClick(Int32 mobileserial) -> Void
```
- __Int32__ **mobileserial**
### Mobiles.SingleClick
```
SingleClick(Mobile mobile) -> Void
```
- __Mobile__ **mobile**
### Mobiles.ToString
```
ToString() -> String
```
### Mobiles.UseMobile
```
UseMobile(Int32 mobileserial) -> Void
```
- __Int32__ **mobileserial**
### Mobiles.UseMobile
```
UseMobile(Mobile mobile) -> Void
```
- __Mobile__ **mobile**
### Mobiles.WaitForProps
```
WaitForProps(Int32 mobileserial, Int32 delay) -> Void
```
- __Int32__ **mobileserial** 
- __Int32__ **delay**
### Mobiles.WaitForProps
```
WaitForProps(Mobile m, Int32 delay) -> Void
```
- __Mobile__ **m** 
- __Int32__ **delay**
### Mobiles.WaitForStats
```
WaitForStats(Int32 mobileserial, Int32 delay) -> Void
```
- __Int32__ **mobileserial** 
- __Int32__ **delay**
### Mobiles.WaitForStats
```
WaitForStats(Mobile m, Int32 delay) -> Void
```
- __Mobile__ **m** 
- __Int32__ **delay**