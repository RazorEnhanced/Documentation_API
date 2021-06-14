:mod:`Mobile`
========================================
.. py:module:: Mobile
   :synopsis: 
            <summary>
            The Mobile class represents an single alive entity. 
            While the Mobile.Serial is unique for each Mobile, Mobile.MobileID is the unique for the Mobile apparence, or image. Sometimes is also called Body or Body ID.
            Mobiles which dies and leave a corpse behind, they stop existing as Mobiles and instead leave a corpse as a Item object appears.
            </summary>
        


Properties
----------------
* Mobile.Backpack :mod:`Item`
  Get the Item representing the backpack of a Mobile. Return null if it doesn't have one.

* Mobile.Body :mod:`Int32`
  Represents the type of Mobile, usually unique for the Mobile image. ( Alias: Mobile.MobileID )

* Mobile.Color :mod:`Int32`
  Color of the mobile.

* Mobile.Contains :mod:`List[Item]`
  Returns the list of items present in the Paperdoll (or equivalent) of the Mobile.
Might not match the items found using via Layer.

* Mobile.Deleted :mod:`Boolean`

* Mobile.Direction :mod:`String`
  Returns the direction of the Mobile.

* Mobile.Female :mod:`Boolean`
  The Mobile is a female.

* Mobile.Flying :mod:`Boolean`
  The mobile is Flying ( Gragoyle )

* Mobile.Hits :mod:`Int32`
  The current hit point of a Mobile. To be read as propotion over Mobile.HitsMax.

* Mobile.HitsMax :mod:`Int32`
  Maximum hitpoint of a Mobile.

* Mobile.Hue :mod:`Int32`

* Mobile.InParty :mod:`Boolean`
  True: if the Mobile is in your party. - False: otherwise.

* Mobile.IsGhost :mod:`Boolean`
  If is a Ghost
Match any MobileID  in the list:
    402, 403, 607, 608, 694, 695, 970

* Mobile.IsHuman :mod:`Boolean`
  Check is the Mobile has a human body.
Match any MobileID in the list:
    183, 184, 185, 186, 400, 
    401, 402, 403, 605, 606,
    607, 608, 666, 667, 694, 
    744, 745, 747, 748, 750,  
    751, 970, 695

* Mobile.Mana :mod:`Int32`
  The current mana of a Mobile. To be read as propotion over Mobile.ManaMax.

* Mobile.ManaMax :mod:`Int32`
  Maximum mana of a Mobile.

* Mobile.Map :mod:`Int32`
  Current map or facet.

* Mobile.MobileID :mod:`Int32`
  Represents the type of Mobile, usually unique for the Mobile image. ( Alias: Mobile.Body )

* Mobile.Mount :mod:`Item`
  Returns the Item assigned to the "Mount" Layer.

* Mobile.Name :mod:`String`
  Name of the Mobile.

* Mobile.Notoriety :mod:`Int32`
  Get the notoriety of the Mobile.

Notorieties:
    1: blue, innocent
    2: green, friend
    3: gray, neutral
    4: gray, criminal
    5: orange, enemy
    6: red, hostile 
    6: yellow, invulnerable

* Mobile.Paralized :mod:`Boolean`
  The mobile is Paralized.

* Mobile.Poisoned :mod:`Boolean`
  The mobile is Poisoned.

* Mobile.Position :mod:`Point3D`

* Mobile.Properties :mod:`List[Property]`
  Get all properties of a Mobile as list of lines of the tooltip.

* Mobile.PropsUpdated :mod:`Boolean`
  True: Mobile.Propertires are updated - False: otherwise.

* Mobile.Quiver :mod:`Item`
  Get the Item representing the quiver of a Mobile. Return null if it doesn't have one.

* Mobile.Serial :mod:`Int32`

* Mobile.Stam :mod:`Int32`
  The current stamina of a Mobile. To be read as propotion over Mobile.StamMax.

* Mobile.StamMax :mod:`Int32`
  Maximum stamina of a Mobile.

* Mobile.Visible :mod:`Boolean`
  True: The Mobile is visible - Flase: The mobile is hidden.

* Mobile.WarMode :mod:`Boolean`
  Mobile is in War mode.

* Mobile.YellowHits :mod:`Boolean`
  The mobile healthbar is not blue, but yellow.


Methods
--------------

.. py:function:: Mobile.DistanceTo(other_mobile) -> Int32


* other_mobile: :mod:`Mobile` The other mobile.


Returns the distance between the current Mobile and another one.

.. py:function:: Mobile.GetItemOnLayer(layer) -> Item


* layer: :mod:`String` Layers:
   Layername
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


Returns the Item associated with a Mobile Layer.
