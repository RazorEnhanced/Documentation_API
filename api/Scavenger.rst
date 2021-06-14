:mod:`Scavenger`
========================================
.. py:module:: Scavenger
   :synopsis: 
            <summary>
            The Scavenger class allow you to interect with the Scavenger Agent, via scripting.
            </summary>
        



Methods
--------------

.. py:function:: Scavenger.ChangeList(listName) -> Void


* listName: :mod:`String` Name of an existing organizer list.


Change the Scavenger's active list.

.. py:function:: Scavenger.GetScavengerBag() -> UInt32





Get current Scravenger destination container.

.. py:function:: Scavenger.ResetIgnore() -> Void







.. py:function:: Scavenger.RunOnce(scavengerList, millisec, filter) -> Void


* scavengerList: :mod:`List[Scavenger.ScavengerItem]` 
* millisec: :mod:`Int32` 
* filter: :mod:`Items.Filter` 




.. py:function:: Scavenger.Start() -> Void





Start the Scavenger Agent on the currently active list.

.. py:function:: Scavenger.Status() -> Boolean





Check Scavenger Agent status

.. py:function:: Scavenger.Stop() -> Void





Stop the Scavenger Agent.
