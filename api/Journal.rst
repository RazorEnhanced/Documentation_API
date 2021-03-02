:mod:`Journal`
========================================
.. py:module:: Journal



Methods
--------------

.. py:function:: Journal.Clear() -> Void







.. py:function:: Journal.GetLineText(text, addname) -> String


* text: :mod:`String` 
* addname: :mod:`Boolean` 




.. py:function:: Journal.GetSpeechName() -> List[String]







.. py:function:: Journal.GetTextByColor(color, addname) -> List[String]


* color: :mod:`Int32` 
* addname: :mod:`Boolean` 




.. py:function:: Journal.GetTextByName(name) -> List[String]


* name: :mod:`String` 




.. py:function:: Journal.GetTextBySerial(serial) -> List[String]


* serial: :mod:`Int32` 




.. py:function:: Journal.GetTextByType(type, addname) -> List[String]


* type: :mod:`String` 
* addname: :mod:`Boolean` 




.. py:function:: Journal.Search(text) -> Boolean


* text: :mod:`String` 




.. py:function:: Journal.SearchByColor(text, color) -> Boolean


* text: :mod:`String` 
* color: :mod:`Int32` 




.. py:function:: Journal.SearchByName(text, name) -> Boolean


* text: :mod:`String` 
* name: :mod:`String` 




.. py:function:: Journal.SearchByType(text, type) -> Boolean


* text: :mod:`String` 
* type: :mod:`String` 




.. py:function:: Journal.WaitByName(name, delay) -> Boolean


* name: :mod:`String` 
* delay: :mod:`Int32` 




.. py:function:: Journal.WaitJournal(text, delay) -> Void


* text: :mod:`String` 
* delay: :mod:`Int32` 




.. py:function:: Journal.WaitJournal(msgs, delay) -> String


* msgs: :mod:`List[String]` 
* delay: :mod:`Int32` 



