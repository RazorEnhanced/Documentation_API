:mod:`Timer`
========================================
.. py:module:: Timer
   :synopsis: 
            <summary>
            Timer are normally used to display messages after a certain period of time. 
            They are also often used to keep track of the maximum amount of time for an action to complete.
            </summary>
        



Methods
--------------

.. py:function:: Timer.Check(name) -> Boolean


* name: :mod:`String` 


Check if a timer object is expired or not.

.. py:function:: Timer.Create(name, delay, message) -> Void


* name: :mod:`String` Timer name.
* delay: :mod:`Int32` Delay in milliseconds.
* message: :mod:`String` Message displayed at timeouit.


Create a timer with the provided name that will expire in ms_timer time (in milliseconds)

.. py:function:: Timer.Create(name, delay) -> Void


* name: :mod:`String` 
* delay: :mod:`Int32` 




.. py:function:: Timer.Remaining(name) -> Int32


* name: :mod:`String` Timer name


Get remaining time for a named timer
