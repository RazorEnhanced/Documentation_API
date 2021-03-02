:mod:`Target`
========================================
.. py:module:: Target



Methods
--------------

.. py:function:: Target.AttackTargetFromList(targetid) -> Void


* targetid: :mod:`String` 




.. py:function:: Target.Cancel() -> Void







.. py:function:: Target.ClearLast() -> Void







.. py:function:: Target.ClearLastandQueue() -> Void







.. py:function:: Target.ClearQueue() -> Void







.. py:function:: Target.GetLast() -> Int32







.. py:function:: Target.GetLastAttack() -> Int32







.. py:function:: Target.GetTargetFromList(targetid) -> Mobile


* targetid: :mod:`String` 




.. py:function:: Target.HasTarget() -> Boolean







.. py:function:: Target.Last() -> Void







.. py:function:: Target.LastQueued() -> Void







.. py:function:: Target.PerformTargetFromList(targetid) -> Void


* targetid: :mod:`String` 




.. py:function:: Target.PromptGroundTarget(message) -> Point3D


* message: :mod:`String` 




.. py:function:: Target.PromptTarget(message) -> Int32


* message: :mod:`String` 




.. py:function:: Target.Self() -> Void







.. py:function:: Target.SelfQueued() -> Void







.. py:function:: Target.SetLast(serial, wait) -> Void


* serial: :mod:`Int32` 
* wait: :mod:`Boolean` 




.. py:function:: Target.SetLast(mob) -> Void


* mob: :mod:`Mobile` 




.. py:function:: Target.SetLastTargetFromList(targetid) -> Void


* targetid: :mod:`String` 




.. py:function:: Target.TargetExecute(x, y, z, gfx) -> Void


* x: :mod:`Int32` 
* y: :mod:`Int32` 
* z: :mod:`Int32` 
* gfx: :mod:`Int32` 




.. py:function:: Target.TargetExecute(mobile) -> Void


* mobile: :mod:`Mobile` 




.. py:function:: Target.TargetExecute(item) -> Void


* item: :mod:`Item` 




.. py:function:: Target.TargetExecute(serial) -> Void


* serial: :mod:`Int32` 




.. py:function:: Target.TargetExecute(x, y, z) -> Void


* x: :mod:`Int32` 
* y: :mod:`Int32` 
* z: :mod:`Int32` 




.. py:function:: Target.TargetExecuteRelative(serial, offset) -> Void


* serial: :mod:`Int32` 
* offset: :mod:`Int32` 




.. py:function:: Target.TargetExecuteRelative(m, offset) -> Void


* m: :mod:`Mobile` 
* offset: :mod:`Int32` 




.. py:function:: Target.WaitForTarget(delay, noshow) -> Void


* delay: :mod:`Int32` 
* noshow: :mod:`Boolean` 



