# Target    

## Properties  
 
## Methods  
### Target.AttackTargetFromList
```
AttackTargetFromList(String targetid) -> Void
```
- __String__ **targetid**
### Target.Cancel
```
Cancel() -> Void
```
### Target.ClearLast
```
ClearLast() -> Void
```
### Target.ClearLastandQueue
```
ClearLastandQueue() -> Void
```
### Target.ClearQueue
```
ClearQueue() -> Void
```
### Target.Equals
```
Equals(Object obj) -> Boolean
```
- __Object__ **obj**
### Target.GetHashCode
```
GetHashCode() -> Int32
```
### Target.GetLast
```
GetLast() -> Int32
```
### Target.GetLastAttack
```
GetLastAttack() -> Int32
```
### Target.GetTargetFromList
```
GetTargetFromList(String targetid) -> Mobile
```
- __String__ **targetid**
### Target.GetType
```
GetType() -> Type
```
### Target.HasTarget
```
HasTarget() -> Boolean
```
### Target.Last
```
Last() -> Void
```
### Target.LastQueued
```
LastQueued() -> Void
```
### Target.PerformTargetFromList
```
PerformTargetFromList(String targetid) -> Void
```
- __String__ **targetid**
### Target.PromptGroundTarget
```
PromptGroundTarget(String message) -> Point3D
```
- __String__ **message** Select Ground Position
### Target.PromptTarget
```
PromptTarget(String message) -> Int32
```
- __String__ **message** Select Item or Mobile
### Target.Self
```
Self() -> Void
```
### Target.SelfQueued
```
SelfQueued() -> Void
```
### Target.SetLast
```
SetLast(Int32 serial, Boolean wait) -> Void
```
- __Int32__ **serial** 
- __Boolean__ **wait** True
### Target.SetLast
```
SetLast(Mobile mob) -> Void
```
- __Mobile__ **mob**
### Target.SetLastTargetFromList
```
SetLastTargetFromList(String targetid) -> Void
```
- __String__ **targetid**
### Target.TargetExecute
```
TargetExecute(Int32 x, Int32 y, Int32 z) -> Void
```
- __Int32__ **x** 
- __Int32__ **y** 
- __Int32__ **z**
### Target.TargetExecute
```
TargetExecute(Int32 x, Int32 y, Int32 z, Int32 gfx) -> Void
```
- __Int32__ **x** 
- __Int32__ **y** 
- __Int32__ **z** 
- __Int32__ **gfx**
### Target.TargetExecute
```
TargetExecute(Mobile mobile) -> Void
```
- __Mobile__ **mobile**
### Target.TargetExecute
```
TargetExecute(Item item) -> Void
```
- __Item__ **item**
### Target.TargetExecute
```
TargetExecute(Int32 serial) -> Void
```
- __Int32__ **serial**
### Target.TargetExecuteRelative
```
TargetExecuteRelative(Mobile m, Int32 offset) -> Void
```
- __Mobile__ **m** 
- __Int32__ **offset**
### Target.TargetExecuteRelative
```
TargetExecuteRelative(Int32 serial, Int32 offset) -> Void
```
- __Int32__ **serial** 
- __Int32__ **offset**
### Target.ToString
```
ToString() -> String
```
### Target.WaitForTarget
```
WaitForTarget(Int32 delay, Boolean noshow) -> Void
```
- __Int32__ **delay** 
- __Boolean__ **noshow** False