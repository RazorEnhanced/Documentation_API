:mod:`Friend`
========================================
.. py:module:: Friend



Methods
--------------

.. py:function:: Friend.AddFriendTarget() -> Void







.. py:function:: Friend.AddPlayer(friendlist, name, serial) -> Void


* friendlist: :mod:`String` Name of the the Friend List. (See Agent tab)
* name: :mod:`String` Name of the Friend want to add.
* serial: :mod:`Int32` Serial of the Friend you want to add.


Add the player specified to the Friend list named in FriendListName parameter

.. py:function:: Friend.ChangeList(friendlist) -> Void


* friendlist: :mod:`String` Name of the list of friend.


Change friend list, List must be exist in friend list GUI configuration

.. py:function:: Friend.GetList(friendlist) -> List[Int32]


* friendlist: :mod:`String` Name of the list of friend.


Retrive list of serial in list, List must be exist in friend Agent tab.

.. py:function:: Friend.IsFriend(serial) -> Boolean


* serial: :mod:`Int32` Serial you want to check


Check if Player is in FriendList, returns a bool value.
