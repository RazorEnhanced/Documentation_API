:mod:`Journal`
========================================
.. py:module:: Journal
   :synopsis: 
            <summary>
            The Journal class provides access to the message Journal.
            </summary>
        



Methods
--------------

.. py:function:: Journal.Clear() -> Void





Removes all entry from the Jorunal. This operation is Global for all Razor.

.. py:function:: Journal.GetJournalEntry(afterTimestap) -> List[Journal.JournalEntry]


* afterTimestap: :mod:`Double` Timestap as UnixTime, the number of seconds elapsed since 01-Jan-1970. (default: -1, no filter)


Get a copy of all Journal lines as JournalEntry. The list can be filtered to include *only* most recent events.

.. py:function:: Journal.GetJournalEntry(afterJournalEntry) -> List[Journal.JournalEntry]


* afterJournalEntry: :mod:`Journal.JournalEntry` A JournalEntry object (default: null, no filter)


Get a copy of all Journal lines as JournalEntry. The list can be filtered to include *only* most recent events.

.. py:function:: Journal.GetLineText(text, addname) -> String


* text: :mod:`String` Text to search.
* addname: :mod:`Boolean` Prepend source name. (default: False)


Search and return the most recent line Journal containing the given text. (case sensitive)

.. py:function:: Journal.GetSpeechName() -> List[String]





Get list of speakers.

.. py:function:: Journal.GetTextByColor(color, addname) -> List[String]


* color: :mod:`Int32` Color of the soruce.
* addname: :mod:`Boolean` Prepend source name. (default: False)


Returns all the lines present in the Journal for a given color.

.. py:function:: Journal.GetTextByName(name, addname) -> List[String]


* name: :mod:`String` Name of the soruce.
* addname: :mod:`Boolean` Prepend source name. (default: False)


Returns all the lines present in the Journal for a given source name. (case sensitive)

.. py:function:: Journal.GetTextBySerial(serial, addname) -> List[String]


* serial: :mod:`Int32` Serial of the soruce.
* addname: :mod:`Boolean` Prepend source name. (default: False)


Returns all the lines present in the Journal for a given serial.

.. py:function:: Journal.GetTextByType(type, addname) -> List[String]


* type: :mod:`String` Regular
System
Emote
Label
Focus
Whisper
Yell
Spell
Guild
Alliance
Party
Encoded
Special
* addname: :mod:`Boolean` Prepend source name. (default: False)


Returns all the lines present in the Journal for a given type. (case sensitive)

.. py:function:: Journal.Search(text) -> Boolean


* text: :mod:`String` Text to search.


Search in the Journal for the occurrence of text. (case sensitive)

.. py:function:: Journal.SearchByColor(text, color) -> Boolean


* text: :mod:`String` Text to search.
* color: :mod:`Int32` Color of the message.


Search in the Journal for the occurrence of text, for a given color. (case sensitive)

.. py:function:: Journal.SearchByName(text, name) -> Boolean


* text: :mod:`String` Text to search.
* name: :mod:`String` Name of the source.


Search in the Journal for the occurrence of text, for a given soruce. (case sensitive)

.. py:function:: Journal.SearchByType(text, type) -> Boolean


* text: :mod:`String` Text to search.
* type: :mod:`String` Regular
System
Emote
Label
Focus
Whisper
Yell
Spell
Guild
Alliance
Party
Encoded
Special


Search in the Journal for the occurrence of text, for a given type. (case sensitive)

.. py:function:: Journal.WaitByName(name, delay) -> Boolean


* name: :mod:`String` Name of the soruce.
* delay: :mod:`Int32` Maximum pause in milliseconds.


Pause script and wait for maximum amount of time, for a specific soruce to appear in Jorunal. (case sensitive)

.. py:function:: Journal.WaitJournal(msgs, delay) -> String


* msgs: :mod:`List[String]` 
* delay: :mod:`Int32` 




.. py:function:: Journal.WaitJournal(text, delay) -> Boolean


* text: :mod:`String` Text to search.
* delay: :mod:`Int32` Maximum pause in milliseconds.


Pause script and wait for maximum amount of time, for a specific text to appear in Journal. (case sensitive)
