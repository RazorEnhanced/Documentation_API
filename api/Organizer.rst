:mod:`Organizer`
========================================
.. py:module:: Organizer
   :synopsis: 
            <summary>
            The Organizer class allow you to interect with the Scavenger Agent, via scripting.
            </summary>
        



Methods
--------------

.. py:function:: Organizer.ChangeList(listName) -> Void


* listName: :mod:`String` Name of an existing organizer list.


Change the Organizer's active list.

.. py:function:: Organizer.FStart() -> Void





Start the Organizer Agent on the currently active list.

.. py:function:: Organizer.FStop() -> Void





Stop the Organizer Agent.

.. py:function:: Organizer.RunOnce(organizerName, sourceBag, destBag, dragDelay) -> Void


* organizerName: :mod:`String` 
* sourceBag: :mod:`Int32` 
* destBag: :mod:`Int32` 
* dragDelay: :mod:`Int32` 




.. py:function:: Organizer.Status() -> Boolean





Check Organizer Agent status
