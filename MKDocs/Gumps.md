# Gumps    

## Properties  
 
## Methods  
### Gumps.CloseGump
```
Gumps.CloseGump(gumpid) -> Void
```
- **gumpid**: UInt32
### Gumps.CurrentGump
```
Gumps.CurrentGump() -> UInt32
```
### Gumps.Equals
```
Gumps.Equals(obj) -> Boolean
```
- **obj**: Object
### Gumps.GetHashCode
```
Gumps.GetHashCode() -> Int32
```
### Gumps.GetType
```
Gumps.GetType() -> Type
```
### Gumps.HasGump
```
Gumps.HasGump() -> Boolean
```
### Gumps.LastGumpGetLine
```
Gumps.LastGumpGetLine(line) -> String
```
- **line**: Int32
### Gumps.LastGumpGetLineList
```
Gumps.LastGumpGetLineList() -> List`1
```
### Gumps.LastGumpRawData
```
Gumps.LastGumpRawData() -> String
```
### Gumps.LastGumpTextExist
```
Gumps.LastGumpTextExist(text) -> Boolean
```
- **text**: String
### Gumps.LastGumpTextExistByLine
```
Gumps.LastGumpTextExistByLine(line, text) -> Boolean
```
- **line**: Int32 
- **text**: String
### Gumps.LastGumpTile
```
Gumps.LastGumpTile() -> List`1
```
### Gumps.ResetGump
```
Gumps.ResetGump() -> Void
```
### Gumps.SendAction
```
Gumps.SendAction(gumpid, buttonid) -> Void
```
- **gumpid**: UInt32 
- **buttonid**: Int32
### Gumps.SendAdvancedAction
```
Gumps.SendAdvancedAction(gumpid, buttonid, entryID, entryS) -> Void
```
- **gumpid**: UInt32 
- **buttonid**: Int32 
- **entryID**: List`1 
- **entryS**: List`1
### Gumps.SendAdvancedAction
```
Gumps.SendAdvancedAction(gumpid, buttonid, switchs, entryID, entryS) -> Void
```
- **gumpid**: UInt32 
- **buttonid**: Int32 
- **switchs**: List`1 
- **entryID**: List`1 
- **entryS**: List`1
### Gumps.SendAdvancedAction
```
Gumps.SendAdvancedAction(gumpid, buttonid, switchs) -> Void
```
- **gumpid**: UInt32 
- **buttonid**: Int32 
- **switchs**: List`1
### Gumps.ToString
```
Gumps.ToString() -> String
```
### Gumps.WaitForGump
```
Gumps.WaitForGump(gumpid, delay) -> Void
```
- **gumpid**: UInt32 
- **delay**: Int32