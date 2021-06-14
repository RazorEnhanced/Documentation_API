:mod:`Mobiles.Filter`
========================================
.. py:module:: Mobiles.Filter
   :synopsis: 
            <summary>
            The Mobiles.Filter class is used to store options to filter the global Mobile list.
            Often used in combination with Mobiles.ApplyFilter.
            </summary>
        


Properties
----------------
* Mobiles.Filter.Blessed :mod:`Int32`
  Limit the search to only Blessed Mobiles.  (default: -1, any Mobile)

* Mobiles.Filter.Bodies :mod:`List[Int32]`
  Limit the search to a list of MobileID (see: Mobile.ItemID or Mobile.Body ) 
Supports .Add() and .AddRange()

* Mobiles.Filter.CheckIgnoreObject :mod:`Boolean`
  Exclude from the search Mobiles which are currently on the global Ignore List. ( default: False, any Item )

* Mobiles.Filter.CheckLineOfSight :mod:`Boolean`
  Limit the search only to the Mobiles which are in line of sight. (default: false, any Mobile)

* Mobiles.Filter.Enabled :mod:`Boolean`
  True: The filter is used - False: Return all Mobile. ( default: True, active )

* Mobiles.Filter.Female :mod:`Int32`
  Limit the search to female Mobile.  (default: -1, any)

* Mobiles.Filter.Friend :mod:`Int32`
  Limit the search to friend Mobile. (default: -1, any)

* Mobiles.Filter.Hues :mod:`List[Int32]`
  Limit the search to a list of Colors.
Supports .Add() and .AddRange()

* Mobiles.Filter.IsGhost :mod:`Int32`
  Limit the search to Ghost only. (default: -1, any Mobile )
Match any MobileID in the list:
    402, 403, 607, 608, 694, 695, 970

* Mobiles.Filter.IsHuman :mod:`Int32`
  Limit the search to Humans only. (default: -1, any Mobile )
Match any MobileID in the list:
    183, 184, 185, 186, 400, 
    401, 402, 403, 605, 606,
    607, 608, 666, 667, 694, 
    744, 745, 747, 748, 750,  
    751, 970, 695

* Mobiles.Filter.Name :mod:`String`
  Limit the search by name of the Mobile.

* Mobiles.Filter.Notorieties :mod:`List[Byte]`
  Limit the search to the Mobile by notoriety.
Supports .Add() and .AddRange()

Notorieties:
    1: blue, innocent
    2: green, friend
    3: gray, neutral
    4: gray, criminal
    5: orange, enemy
    6: red, hostile 
    6: yellow, invulnerable

* Mobiles.Filter.Paralized :mod:`Int32`
  Limit the search to paralized Mobile. (default: -1, any)

* Mobiles.Filter.Poisoned :mod:`Int32`
  Limit the search to only Poisoned Mobiles.  (default: -1, any Mobile)

* Mobiles.Filter.RangeMax :mod:`Double`
  Limit the search by distance, to Mobiles which are at most RangeMax tiles away from the Player. ( default: -1, any Mobile )

* Mobiles.Filter.RangeMin :mod:`Double`
  Limit the search by distance, to Mobiles which are at least RangeMin tiles away from the Player. ( default: -1, any Mobile )

* Mobiles.Filter.Serials :mod:`List[Int32]`
  Limit the search to a list of Serials of Mobile to find. (ex: 0x0406EFCA )
Supports .Add() and .AddRange()

* Mobiles.Filter.Warmode :mod:`Int32`
  Limit the search to Mobile War mode. (default: -1, any Mobile)
    -1: any
     0: peace
     1: war


