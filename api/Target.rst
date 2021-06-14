:mod:`Target`
========================================
.. py:module:: Target
   :synopsis: 
            <summary>
            The Target class provides various method for targeting Land, Items and Mobiles in game.
            </summary>
        



Methods
--------------

.. py:function:: Target.AttackTargetFromList(target_name) -> Void


* target_name: :mod:`String` 


Attack Target from gui filter selector, in Targetting tab.

.. py:function:: Target.Cancel() -> Void





Cancel the current target.

.. py:function:: Target.ClearLast() -> Void





Clear the last target.

.. py:function:: Target.ClearLastandQueue() -> Void





Clear last target and target queue.

.. py:function:: Target.ClearQueue() -> Void





Clear Queue Target.

.. py:function:: Target.GetLast() -> Int32





Get serial number of last target

.. py:function:: Target.GetLastAttack() -> Int32





Get serial number of last attack target

.. py:function:: Target.GetTargetFromList(target_name) -> Mobile


* target_name: :mod:`String` Name of the target filter.


Get Mobile object from GUI filter selector, in Targetting tab.

.. py:function:: Target.HasTarget() -> Boolean





Get status if have in-game cursor has target shape.

.. py:function:: Target.Last() -> Void





Execute the target on the last Item or Mobile targeted.

.. py:function:: Target.LastQueued() -> Void





Enqueue the next target on the last Item or Mobile targeted.

.. py:function:: Target.PerformTargetFromList(target_name) -> Void


* target_name: :mod:`String` Name of the target filter.


Execute Target from GUI filter selector, in Targetting tab.

.. py:function:: Target.PromptGroundTarget(message, color) -> Point3D


* message: :mod:`String` Hint on what to select.
* color: :mod:`Int32` Color of the message. (default: 945, gray)


Prompt a target in-game, wait for the Player to select the ground. Can also specific a text message for prompt.

.. py:function:: Target.PromptTarget(message, color) -> Int32


* message: :mod:`String` Hint on what to select.
* color: :mod:`Int32` Color of the message. (default: 945, gray)


Prompt a target in-game, wait for the Player to select an Item or a Mobile. Can also specific a text message for prompt.

.. py:function:: Target.Self() -> Void





Execute the target on the Player.

.. py:function:: Target.SelfQueued() -> Void





Enqueue the next target on the Player.

.. py:function:: Target.SetLast(serial, wait) -> Void


* serial: :mod:`Int32` Serial of the Mobile.
* wait: :mod:`Boolean` Wait confirmation from the server.


Set the last target to specific mobile, using the serial.

.. py:function:: Target.SetLast(mob) -> Void


* mob: :mod:`Mobile` 




.. py:function:: Target.SetLastTargetFromList(target_name) -> Void


* target_name: :mod:`String` Name of the target filter.


Set Last Target from GUI filter selector, in Targetting tab.

.. py:function:: Target.TargetExecute(item) -> Void


* item: :mod:`Item` Item object to Target.




.. py:function:: Target.TargetExecute(serial) -> Void


* serial: :mod:`Int32` Serial of the Target




.. py:function:: Target.TargetExecute(x, y, z) -> Void


* x: :mod:`Int32` 
* y: :mod:`Int32` 
* z: :mod:`Int32` 




.. py:function:: Target.TargetExecute(mobile) -> Void


* mobile: :mod:`Mobile` Mobile object to Target.




.. py:function:: Target.TargetExecute(x, y, z, StaticID) -> Void


* x: :mod:`Int32` X coordinate.
* y: :mod:`Int32` Y coordinate.
* z: :mod:`Int32` Z coordinate.
* StaticID: :mod:`Int32` ID of Land/Tile


Execute target on specific serial, item, mobile, X Y Z point.

.. py:function:: Target.TargetExecuteRelative(serial, offset) -> Void


* serial: :mod:`Int32` Serial of the mobile
* offset: :mod:`Int32` 




.. py:function:: Target.TargetExecuteRelative(mobile, offset) -> Void


* mobile: :mod:`Mobile` Mobile object to target.
* offset: :mod:`Int32` Distance from the target.


Execute target on specific land point with offset distance from Mobile. Distance is calculated by target Mobile.Direction.

.. py:function:: Target.TargetResource(item_serial, resource_number) -> Void


* item_serial: :mod:`Int32` Item object to use.
* resource_number: :mod:`Int32` Resource as standard name or custom number
               0: ore
               1: sand
               2: wood
               3: graves
               4: red_mushrooms
               n: custom


Find and target a resource using the specified item.

.. py:function:: Target.TargetResource(item, resouce_name) -> Void


* item: :mod:`Item` Item object to use.
* resouce_name: :mod:`String` 




.. py:function:: Target.TargetResource(item, resoruce_number) -> Void


* item: :mod:`Item` 
* resoruce_number: :mod:`Int32` 




.. py:function:: Target.TargetResource(item_serial, resource_name) -> Void


* item_serial: :mod:`Int32` 
* resource_name: :mod:`String` 




.. py:function:: Target.WaitForTarget(delay, noshow) -> Boolean


* delay: :mod:`Int32` Maximum amount to wait, in milliseconds
* noshow: :mod:`Boolean` Pevent the cursor to display the target.


Wait for the cursor to show the target, pause the script for a maximum amount of time. and optional flag True or False. True Not show cursor, false show it
