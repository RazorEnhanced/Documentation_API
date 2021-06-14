:mod:`Items.Filter`
========================================
.. py:module:: Items.Filter
   :synopsis: 
            <summary>
            The Items.Filter class is used to store options to filter the global Item list.
            Often used in combination with Items.ApplyFilter.
            </summary>
        


Properties
----------------
* Items.Filter.CheckIgnoreObject :mod:`Boolean`
  Exclude from the search Items which are currently on the global Ignore List. ( default: False, any Item )

* Items.Filter.Enabled :mod:`Boolean`
  True: The filter is used - False: Return all Item. ( default: True, active )

* Items.Filter.Graphics :mod:`List[Int32]`
  Limit the search to a list of Grapichs ID (see: Item.ItemID ) 
Supports .Add() and .AddRange()

* Items.Filter.Hues :mod:`List[Int32]`
  Limit the search to a list of Colors.
Supports .Add() and .AddRange()

* Items.Filter.IsContainer :mod:`Int32`
  Limit the search to the Items which are also containers. (default: -1: any Item)

* Items.Filter.IsCorpse :mod:`Int32`
  Limit the search to the corpses on the ground. (default: -1, any Item)

* Items.Filter.IsDoor :mod:`Int32`
  Limit the search to the doors. (default: -1: any Item)

* Items.Filter.Layers :mod:`List[String]`
  Limit the search to the wearable Items by Layer.
Supports .Add() and .AddRange()

Layers:
    RightHand
    LeftHand
    Shoes
    Pants
    Shirt
    Head
    Gloves
    Ring
    Neck
    Waist
    InnerTorso
    Bracelet
    MiddleTorso
    Earrings
    Arms
    Cloak
    OuterTorso
    OuterLegs
    InnerLegs
    Talisman

* Items.Filter.Movable :mod:`Int32`
  Limit the search to only Movable Items. ( default: -1, any Item )

* Items.Filter.Name :mod:`String`
  Limit the search by name of the Item.

* Items.Filter.OnGround :mod:`Int32`
  Limit the search to the Items on the ground. (default: -1, any Item)

* Items.Filter.RangeMax :mod:`Double`
  Limit the search by distance, to Items on the ground which are at most RangeMax tiles away from the Player. ( default: -1, any Item )

* Items.Filter.RangeMin :mod:`Double`
  Limit the search by distance, to Items on the ground which are at least RangeMin tiles away from the Player. ( default: -1, any Item )

* Items.Filter.Serials :mod:`List[Int32]`
  Limit the search to a list of Serials of Item to find. (ex: 0x0406EFCA )
Supports .Add() and .AddRange()


