:mod:`Item`
========================================
.. py:module:: Item
   :synopsis: 
            <summary>
            The Item class represent a single in-game Item object. Examples of Item are: Swords, bags, bandages, reagents, clothing.
            While the Item.Serial is unique for each Item, Item.ItemID is the unique for the Item apparence, or image. Sometimes is also called ID or Graphics ID.
            Item can also be house foriture as well as decorative items on the ground, like lamp post and banches.
            However, for Item on the ground that cannot be picked up, they might be part of the world map, see Statics class.
            </summary>
        


Properties
----------------
* Item.Amount :mod:`Int32`
  Read amount from item type object.

* Item.Container :mod:`Int32`
  Serial of the container which contains the object.

* Item.Contains :mod:`List[Item]`
  Contains the list of Item inside a container.

* Item.Deleted :mod:`Boolean`

* Item.Direction :mod:`String`
  Item direction.

* Item.Durability :mod:`Int32`
  Get the current durability of an Item. (0: no durability)

* Item.GridNum :mod:`Byte`
  Returns the GridNum of the item. (need better documentation)

* Item.Hue :mod:`Int32`

* Item.Image :mod:`Bitmap`
  Get the in-game image on an Item as Bitmap object.
See MSDN: https://docs.microsoft.com/dotnet/api/system.drawing.bitmap

* Item.IsBagOfSending :mod:`Boolean`
  True: if the item is a bag of sending - False: otherwise.

* Item.IsContainer :mod:`Boolean`
  True: if the item is a container - False: otherwise.

* Item.IsCorpse :mod:`Boolean`
  True: if the item is a corpse - False: otherwise.

* Item.IsDoor :mod:`Boolean`
  True: if the item is a door - False: otherwise.

* Item.IsInBank :mod:`Boolean`
  True: if the item is in the Player's bank - False: otherwise.

* Item.IsLootable :mod:`Boolean`
  True: For regualar items - False: for hair, beards, etc.

* Item.IsPotion :mod:`Boolean`
  True: if the item is a potion - False: otherwise.

* Item.IsPouch :mod:`Boolean`
  True: if the item is a pouch - False: otherwise.

* Item.IsResource :mod:`Boolean`
  True: if the item is a resource (ore, sand, wood, stone, fish) - False: otherwise

* Item.IsTwoHanded :mod:`Boolean`
  True: if the item is a 2-handed weapon - False: otherwise.

* Item.IsVirtueShield :mod:`Boolean`
  True: if the item is a virtue shield - False: otherwise.

* Item.ItemID :mod:`Int32`
  Represents the type of Item, usually unique for the Item image.  Sometime called ID or Graphics ID.

* Item.Layer :mod:`String`
  Gets the Layer, for werable items only. (need better documentation)

* Item.MaxDurability :mod:`Int32`
  Get the maximum durability of an Item. (0: no durability)

* Item.Movable :mod:`Boolean`
  Item is movable

* Item.Name :mod:`String`
  Item name

* Item.OnGround :mod:`Boolean`
  True: if the item is on the ground - False: otherwise.

* Item.Position :mod:`Point3D`

* Item.Properties :mod:`List[Property]`
  Get the list of Properties of an Item.

* Item.PropsUpdated :mod:`Boolean`
  True: if Properties are updated - False: otherwise.

* Item.RootContainer :mod:`Int32`
  Get serial of root container of item.

* Item.Serial :mod:`Int32`

* Item.Updated :mod:`Boolean`
  Check if the Item already have been updated with all the properties. (need better documentation)

* Item.Visible :mod:`Boolean`
  Item is Visible

* Item.Weight :mod:`Int32`
  Get the weight of a item. (0: no weight)


Methods
--------------

.. py:function:: Item.DistanceTo(itm) -> Int32


* itm: :mod:`Item` Target as Item




.. py:function:: Item.DistanceTo(mob) -> Int32


* mob: :mod:`Mobile` Target as Mobile


Return the distance in number of tiles, from Item to Mobile.

.. py:function:: Item.GetWorldPosition() -> Point3D







.. py:function:: Item.IsChildOf(container) -> Boolean


* container: :mod:`Item` Item as container.


Check if an Item is contained in a container. Can be a Item or a Mobile (wear by).

.. py:function:: Item.IsChildOf(container) -> Boolean


* container: :mod:`Mobile` Mobile as container.




.. py:function:: Item.ToString() -> String






