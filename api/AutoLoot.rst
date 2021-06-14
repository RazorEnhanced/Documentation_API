:mod:`AutoLoot`
========================================
.. py:module:: AutoLoot
   :synopsis: 
            <summary>
            The Autoloot class allow to interact with the Autoloot Agent, via scripting.
            </summary>
        



Methods
--------------

.. py:function:: AutoLoot.ChangeList(listName) -> Void


* listName: :mod:`String` Name of an existing organizer list.


Change the Autoloot's active list.

.. py:function:: AutoLoot.GetList(lootListName) -> List[AutoLoot.AutoLootItem]


* lootListName: :mod:`String` Name of the AutoLoot list.


Given an AutoLoot list name, return a list of AutoLootItem associated.

.. py:function:: AutoLoot.GetLootBag() -> UInt32





Get current Autoloot destination container.

.. py:function:: AutoLoot.ResetIgnore() -> Void





Reset the Autoloot ignore list.

.. py:function:: AutoLoot.RunOnce(lootListName, millisec, filter) -> Void


* lootListName: :mod:`String` Name of the Autoloot listfilter for search on ground.
* millisec: :mod:`Int32` Delay in milliseconds. (unused)
* filter: :mod:`Items.Filter` Item filter


Start Autoloot with custom parameters.

.. py:function:: AutoLoot.SetNoOpenCorpse(noOpen) -> Boolean


* noOpen: :mod:`Boolean` True: "No Open Corpse" is active - False: otherwise


Toggle "No Open Corpse" on/off. The change doesn't persist if you reopen razor.

.. py:function:: AutoLoot.Start() -> Void





Start the Autoloot Agent on the currently active list.

.. py:function:: AutoLoot.Status() -> Boolean





Check Autoloot Agent status

.. py:function:: AutoLoot.Stop() -> Void





Stop the Autoloot Agent.
