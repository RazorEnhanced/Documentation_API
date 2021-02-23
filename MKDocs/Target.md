# Target    

## Properties  
 
## Methods  
### Target.AttackTargetFromList
```
Target.AttackTargetFromList(targetid) -> Void
```
- **targetid**: String
### Target.Cancel
```
Target.Cancel() -> Void
```
### Target.ClearLast
```
Target.ClearLast() -> Void
```
### Target.ClearLastandQueue
```
Target.ClearLastandQueue() -> Void
```
### Target.ClearQueue
```
Target.ClearQueue() -> Void
```
### Target.Equals
```
Target.Equals(obj) -> Boolean
```
- **obj**: Object
### Target.GetHashCode
```
Target.GetHashCode() -> Int32
```
### Target.GetLast
```
Target.GetLast() -> Int32
```
### Target.GetLastAttack
```
Target.GetLastAttack() -> Int32
```
### Target.GetTargetFromList
```
Target.GetTargetFromList(targetid) -> Mobile
```
- **targetid**: String
### Target.GetType
```
Target.GetType() -> Type
```
### Target.HasTarget
```
Target.HasTarget() -> Boolean
```
### Target.Last
```
Target.Last() -> Void
```
### Target.LastQueued
```
Target.LastQueued() -> Void
```
### Target.PerformTargetFromList
```
Target.PerformTargetFromList(targetid) -> Void
```
- **targetid**: String
### Target.PromptGroundTarget
```
Target.PromptGroundTarget(message) -> Point3D
```
- **message**: String Select Ground Position
### Target.PromptTarget
```
Target.PromptTarget(message) -> Int32
```
- **message**: String Select Item or Mobile
### Target.Self
```
Target.Self() -> Void
```
### Target.SelfQueued
```
Target.SelfQueued() -> Void
```
### Target.SetLast
```
Target.SetLast(serial, wait) -> Void
```
- **serial**: Int32 
- **wait**: Boolean True
### Target.SetLast
```
Target.SetLast(mob) -> Void
```
- **mob**: Mobile
### Target.SetLastTargetFromList
```
Target.SetLastTargetFromList(targetid) -> Void
```
- **targetid**: String
### Target.TargetExecute
```
Target.TargetExecute(x, y, z) -> Void
```
- **x**: Int32 
- **y**: Int32 
- **z**: Int32
### Target.TargetExecute
```
Target.TargetExecute(x, y, z, gfx) -> Void
```
- **x**: Int32 
- **y**: Int32 
- **z**: Int32 
- **gfx**: Int32
### Target.TargetExecute
```
Target.TargetExecute(mobile) -> Void
```
- **mobile**: Mobile
### Target.TargetExecute
```
Target.TargetExecute(item) -> Void
```
- **item**: Item
### Target.TargetExecute
```
Target.TargetExecute(serial) -> Void
```
- **serial**: Int32
### Target.TargetExecuteRelative
```
Target.TargetExecuteRelative(m, offset) -> Void
```
- **m**: Mobile 
- **offset**: Int32
### Target.TargetExecuteRelative
```
Target.TargetExecuteRelative(serial, offset) -> Void
```
- **serial**: Int32 
- **offset**: Int32
### Target.ToString
```
Target.ToString() -> String
```
### Target.WaitForTarget
```
Target.WaitForTarget(delay, noshow) -> Void
```
- **delay**: Int32 
- **noshow**: Boolean False