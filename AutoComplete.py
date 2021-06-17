""" Version: 0.8.0
This module represents the scripting PythonAPI available in RazorEnhanced.
This class is NOT intended to be used as code, but to provice autocomplete in external editors and generation documentation.
"""
from typing import *
class String(str): pass
class Object: pass
class Boolean: pass
class Byte(int): pass
class Int(int): pass 
class Int32(int): pass 
class UInt32(int): pass
class Float(float): pass
class Single(float): pass
class Double(float): pass

class AutoLoot:
	"""	
	<summary>
	The Autoloot class allow to interact with the Autoloot Agent, via scripting.
	</summary>
		
	"""

	@staticmethod
	def ChangeList(listName: str):
		"""Change the Autoloot's active list.
		
		Parameters
		----------
		listName: str
			Name of an existing organizer list.
		
		"""

	@staticmethod
	def GetList(lootListName: str) -> "List[AutoLoot.AutoLootItem]":
		"""Given an AutoLoot list name, return a list of AutoLootItem associated.
		
		Parameters
		----------
		lootListName: str
			Name of the AutoLoot list.
		
		Returns
		-------
		List[AutoLoot.AutoLootItem]
		
		"""

	@staticmethod
	def GetLootBag() -> "UInt32":
		"""Get current Autoloot destination container.
		
		Returns
		-------
		UInt32
			Serial of the container.
		
		"""

	@staticmethod
	def ResetIgnore():
		"""Reset the Autoloot ignore list.
		
		"""

	@staticmethod
	def RunOnce(lootListName: str, millisec: int, filter: "Items.Filter"):
		"""Start Autoloot with custom parameters.
		
		Parameters
		----------
		lootListName: str
			Name of the Autoloot listfilter for search on ground.
		millisec: int
			Delay in milliseconds. (unused)
		filter: Items.Filter
			Item filter
		
		"""

	@staticmethod
	def SetNoOpenCorpse(noOpen: bool) -> bool:
		"""Toggle "No Open Corpse" on/off. The change doesn't persist if you reopen razor.
		
		Parameters
		----------
		noOpen: bool
			True: "No Open Corpse" is active - False: otherwise
		
		Returns
		-------
		bool
			Previous value of "No Open Corpse"
		
		"""

	@staticmethod
	def Start():
		"""Start the Autoloot Agent on the currently active list.
		
		"""

	@staticmethod
	def Status() -> bool:
		"""Check Autoloot Agent status
		
		Returns
		-------
		bool
			True: if the Autoloot is running - False: otherwise
		
		"""

	@staticmethod
	def Stop():
		"""Stop the Autoloot Agent.
		
		"""


	class AutoLootItem:
		"""				
		"""
		@property
		def Color(self) -> int: return int() 
		
		@Color.setter
		def Color(self, Color: int): pass

		@property
		def Graphics(self) -> int: return int() 
		
		@Graphics.setter
		def Graphics(self, Graphics: int): pass

		@property
		def List(self) -> str: return str() 
		
		@List.setter
		def List(self, List: str): pass

		@property
		def LootBagOverride(self) -> int: return int() 
		
		@LootBagOverride.setter
		def LootBagOverride(self, LootBagOverride: int): pass

		@property
		def Name(self) -> str: return str() 
		
		@Name.setter
		def Name(self, Name: str): pass

		@property
		def Properties(self) -> "List[AutoLoot.AutoLootItem.Property]": return List[AutoLoot.AutoLootItem.Property]() 
		
		@Properties.setter
		def Properties(self, Properties: "List[AutoLoot.AutoLootItem.Property]"): pass

		@property
		def Selected(self) -> bool: return bool() 
		
		@Selected.setter
		def Selected(self, Selected: bool): pass



class BandageHeal:
	"""		
	"""

	@staticmethod
	def Start():
		"""Start BandageHeal Agent.
		
		"""

	@staticmethod
	def Status() -> bool:
		"""Check BandageHeal Agent status, returns a bool value.
		
		Returns
		-------
		bool
			True: is running - False: otherwise
		
		"""

	@staticmethod
	def Stop():
		"""Stop BandageHeal Agent.
		
		"""


class BuyAgent:
	"""	
	<summary>
	The BuyAgent class allow you to interect with the BuyAgent, via scripting.
	</summary>
		
	"""

	@staticmethod
	def ChangeList(listName: str):
		"""Change the BuyAgent's active list.
		
		Parameters
		----------
		listName: str
			Name of an existing buy list.
		
		"""

	@staticmethod
	def Disable():
		"""Disable BuyAgent Agent.
		
		"""

	@staticmethod
	def Enable():
		"""Enable BuyAgent on the currently active list.
		
		"""

	@staticmethod
	def Status() -> bool:
		"""Check BuyAgent Agent status
		
		Returns
		-------
		bool
			True: if the BuyAgent is active - False: otherwise
		
		"""


class DPSMeter:
	"""	
	<summary>
	The DPSMeter class implements a Damage Per Second meter which can be useful to tune meta-builds.(???)
	</summary>
		
	"""

	@staticmethod
	def GetDamage(serial: int) -> int:
		"""Get total damage per Mobile.
		
		Parameters
		----------
		serial: int
			Serial of the Mobile.
		
		Returns
		-------
		int
			Total damage.
		
		"""

	@staticmethod
	def Pause():
		"""Pause DPSMeter data recording.
		
		"""

	@staticmethod
	def Start():
		"""Start DPSMeter engine.
		
		"""

	@staticmethod
	def Status() -> bool:
		"""Check DPSMeter Agent status, returns a bool value.
		
		Returns
		-------
		bool
			True: is running - False: otherwise
		
		"""

	@staticmethod
	def Stop():
		"""Stop DPSMeter engine.
		
		"""


class Dress:
	"""		
	"""

	@staticmethod
	def ChangeList(dresslist: str):
		"""Change dress list, List must be exist in dress/undress Agent tab.
		
		Parameters
		----------
		dresslist: str
			Name of the list of friend.
		
		"""

	@staticmethod
	def DressFStart():
		"""Start Dress engine.
		
		"""

	@staticmethod
	def DressFStop():
		"""Stop Dress engine.
		
		"""

	@staticmethod
	def DressStatus() -> bool:
		"""Check Dress Agent status, returns a bool value.
		
		Returns
		-------
		bool
			True: is running - False: otherwise
		
		"""

	@staticmethod
	def UnDressFStart():
		"""Start UnDress engine.
		
		"""

	@staticmethod
	def UnDressFStop():
		"""Stop UnDress engine.
		
		"""

	@staticmethod
	def UnDressStatus() -> bool:
		"""Check UnDress Agent status, returns a bool value.
		
		Returns
		-------
		bool
			True: is running - False: otherwise
		
		"""


class Friend:
	"""		
	"""

	@staticmethod
	def AddFriendTarget():
		"""
		
		"""

	@staticmethod
	def AddPlayer(friendlist: str, name: str, serial: int):
		"""Add the player specified to the Friend list named in FriendListName parameter
		
		Parameters
		----------
		friendlist: str
			Name of the the Friend List. (See Agent tab)
		name: str
			Name of the Friend want to add.
		serial: int
			Serial of the Friend you want to add.
		
		"""

	@staticmethod
	def ChangeList(friendlist: str):
		"""Change friend list, List must be exist in friend list GUI configuration
		
		Parameters
		----------
		friendlist: str
			Name of the list of friend.
		
		"""

	@staticmethod
	def GetList(friendlist: str) -> "List[Int32]":
		"""Retrive list of serial in list, List must be exist in friend Agent tab.
		
		Parameters
		----------
		friendlist: str
			Name of the list of friend.
		
		Returns
		-------
		List[Int32]
		
		"""

	@staticmethod
	def IsFriend(serial: int) -> bool:
		"""Check if Player is in FriendList, returns a bool value.
		
		Parameters
		----------
		serial: int
			Serial you want to check
		
		Returns
		-------
		bool
			True: if is a friend - False: otherwise
		
		"""


class Gumps:
	"""	
	<summary>
	The Gumps class is used to read and interact with in-game gumps, via scripting.
	
	NOTE
	----
	During development of scripts that involves interecting with Gumps, is often needed to know gumpids and buttonids.
	For this purpose, can be particularly usefull to use *Inspect Gumps* and *Record*, top right, in the internal RE script editor.
	</summary>
		
	"""

	@staticmethod
	def CloseGump(gumpid: "UInt32"):
		"""Close a specific Gump.
		
		Parameters
		----------
		gumpid: UInt32
			ID of the gump
		
		"""

	@staticmethod
	def CurrentGump() -> "UInt32":
		"""Return the ID of most recent, still open Gump.
		
		Returns
		-------
		UInt32
			ID of gump.
		
		"""

	@staticmethod
	def HasGump() -> bool:
		"""Get status if have a gump open or not.
		
		Returns
		-------
		bool
			True: There is a Gump open - False: otherwise.
		
		"""

	@staticmethod
	def LastGumpGetLine(line_num: int) -> str:
		"""Get a specific line from the most recent and still open Gump. Filter by line number.
		
		Parameters
		----------
		line_num: int
			Number of the line.
		
		Returns
		-------
		str
			Text content of the line. (empty: line not found)
		
		"""

	@staticmethod
	def LastGumpGetLineList() -> "List[String]":
		"""Get all text from the most recent and still open Gump.
		
		Returns
		-------
		List[String]
			Text of the gump.
		
		"""

	@staticmethod
	def LastGumpRawData() -> str:
		"""Get the Raw Data of the most recent and still open Gump.
		
		Returns
		-------
		str
			Raw Data of the gump.
		
		"""

	@staticmethod
	def LastGumpRawText() -> "List[String]":
		"""Get the Raw Text of the most recent and still open Gump.
		
		Returns
		-------
		List[String]
			List of Raw Text.
		
		"""

	@staticmethod
	def LastGumpTextExist(text: str) -> bool:
		"""Search for text inside the most recent and still open Gump.
		
		Parameters
		----------
		text: str
			Text to search.
		
		Returns
		-------
		bool
			True: Text found in active Gump - False: otherwise
		
		"""

	@staticmethod
	def LastGumpTextExistByLine(line_num: int, text: str) -> bool:
		"""Search for text, in a spacific line of the most recent and still open Gump.
		
		Parameters
		----------
		line_num: int
			Number of the line.
		text: str
			Text to search.
		
		Returns
		-------
		bool
		
		"""

	@staticmethod
	def LastGumpTile() -> "List[Int32]":
		"""Get the list of Gump Tile (! this documentation is a stub !)
		
		Returns
		-------
		List[Int32]
			List of Gump Tile.
		
		"""

	@staticmethod
	def ResetGump():
		"""Clean current status of Gumps.
		
		"""

	@staticmethod
	def SendAction(gumpid: "UInt32", buttonid: int):
		"""Send a Gump response by gumpid and buttonid.
		
		Parameters
		----------
		gumpid: UInt32
			ID of the gump.
		buttonid: int
			ID of the Button to press.
		
		"""

	@staticmethod
	def SendAdvancedAction(gumpid: "UInt32", buttonid: int, switchlist_id: "List[Int32]", textlist_id: Union["List[Int32]", "List[String]", None], textlist_str: Union["List[String]", None]):
		"""
		
		Parameters
		----------
		gumpid: UInt32
		buttonid: int
		switchlist_id: List[Int32]
		textlist_id: List[Int32] or List[String] or None
		textlist_str: List[String] or None
		
		"""

	@staticmethod
	def WaitForGump(gumpid: "UInt32", delay: int):
		"""Waits for a specific Gump to appear, for a maximum amount of time. If gumpid is 0 it will match any Gump.
		
		Parameters
		----------
		gumpid: UInt32
			ID of the gump. (0: any)
		delay: int
			Maximum wait, in milliseconds.
		
		"""


class HotKeyEvent:
	"""		
	"""
	@property
	def HotKey(self) -> "Keys": return Keys() 
	
	@HotKey.setter
	def HotKey(self, HotKey: "Keys"): pass

	@property
	def LastEvent(self) -> "HotKeyEvent": return HotKeyEvent() 
	
	@LastEvent.setter
	def LastEvent(self, LastEvent: "HotKeyEvent"): pass

	@property
	def Timestamp(self) -> float: return float() 
	
	@Timestamp.setter
	def Timestamp(self, Timestamp: float): pass

	@staticmethod
	def AddEvent(k: "Keys") -> "HotKeyEvent":
		"""
		
		Parameters
		----------
		k: Keys
		
		Returns
		-------
		HotKeyEvent
		
		"""


class Item:
	"""	
	<summary>
	The Item class represent a single in-game Item object. Examples of Item are: Swords, bags, bandages, reagents, clothing.
	While the Item.Serial is unique for each Item, Item.ItemID is the unique for the Item apparence, or image. Sometimes is also called ID or Graphics ID.
	Item can also be house foriture as well as decorative items on the ground, like lamp post and banches.
	However, for Item on the ground that cannot be picked up, they might be part of the world map, see Statics class.
	</summary>
		
	"""
	@property
	def Amount(self) -> int: 
		"""Read amount from item type object."""
		return int() 
	
	@Amount.setter
	def Amount(self, Amount: int): pass

	@property
	def Container(self) -> int: 
		"""Serial of the container which contains the object."""
		return int() 
	
	@Container.setter
	def Container(self, Container: int): pass

	@property
	def Contains(self) -> "List[Item]": 
		"""Contains the list of Item inside a container."""
		return List[Item]() 
	
	@Contains.setter
	def Contains(self, Contains: "List[Item]"): pass

	@property
	def Deleted(self) -> bool: return bool() 
	
	@Deleted.setter
	def Deleted(self, Deleted: bool): pass

	@property
	def Direction(self) -> str: 
		"""Item direction."""
		return str() 
	
	@Direction.setter
	def Direction(self, Direction: str): pass

	@property
	def Durability(self) -> int: 
		"""Get the current durability of an Item. (0: no durability)"""
		return int() 
	
	@Durability.setter
	def Durability(self, Durability: int): pass

	@property
	def GridNum(self) -> int: 
		"""Returns the GridNum of the item. (need better documentation)"""
		return int() 
	
	@GridNum.setter
	def GridNum(self, GridNum: int): pass

	@property
	def Hue(self) -> int: return int() 
	
	@Hue.setter
	def Hue(self, Hue: int): pass

	@property
	def Image(self) -> "Bitmap": 
		"""Get the in-game image on an Item as Bitmap object.
		See MSDN: https://docs.microsoft.com/dotnet/api/system.drawing.bitmap"""
		return Bitmap() 
	
	@Image.setter
	def Image(self, Image: "Bitmap"): pass

	@property
	def IsBagOfSending(self) -> bool: 
		"""True: if the item is a bag of sending - False: otherwise."""
		return bool() 
	
	@IsBagOfSending.setter
	def IsBagOfSending(self, IsBagOfSending: bool): pass

	@property
	def IsContainer(self) -> bool: 
		"""True: if the item is a container - False: otherwise."""
		return bool() 
	
	@IsContainer.setter
	def IsContainer(self, IsContainer: bool): pass

	@property
	def IsCorpse(self) -> bool: 
		"""True: if the item is a corpse - False: otherwise."""
		return bool() 
	
	@IsCorpse.setter
	def IsCorpse(self, IsCorpse: bool): pass

	@property
	def IsDoor(self) -> bool: 
		"""True: if the item is a door - False: otherwise."""
		return bool() 
	
	@IsDoor.setter
	def IsDoor(self, IsDoor: bool): pass

	@property
	def IsInBank(self) -> bool: 
		"""True: if the item is in the Player's bank - False: otherwise."""
		return bool() 
	
	@IsInBank.setter
	def IsInBank(self, IsInBank: bool): pass

	@property
	def IsLootable(self) -> bool: 
		"""True: For regualar items - False: for hair, beards, etc."""
		return bool() 
	
	@IsLootable.setter
	def IsLootable(self, IsLootable: bool): pass

	@property
	def IsPotion(self) -> bool: 
		"""True: if the item is a potion - False: otherwise."""
		return bool() 
	
	@IsPotion.setter
	def IsPotion(self, IsPotion: bool): pass

	@property
	def IsPouch(self) -> bool: 
		"""True: if the item is a pouch - False: otherwise."""
		return bool() 
	
	@IsPouch.setter
	def IsPouch(self, IsPouch: bool): pass

	@property
	def IsResource(self) -> bool: 
		"""True: if the item is a resource (ore, sand, wood, stone, fish) - False: otherwise"""
		return bool() 
	
	@IsResource.setter
	def IsResource(self, IsResource: bool): pass

	@property
	def IsTwoHanded(self) -> bool: 
		"""True: if the item is a 2-handed weapon - False: otherwise."""
		return bool() 
	
	@IsTwoHanded.setter
	def IsTwoHanded(self, IsTwoHanded: bool): pass

	@property
	def IsVirtueShield(self) -> bool: 
		"""True: if the item is a virtue shield - False: otherwise."""
		return bool() 
	
	@IsVirtueShield.setter
	def IsVirtueShield(self, IsVirtueShield: bool): pass

	@property
	def ItemID(self) -> int: 
		"""Represents the type of Item, usually unique for the Item image.  Sometime called ID or Graphics ID."""
		return int() 
	
	@ItemID.setter
	def ItemID(self, ItemID: int): pass

	@property
	def Layer(self) -> str: 
		"""Gets the Layer, for werable items only. (need better documentation)"""
		return str() 
	
	@Layer.setter
	def Layer(self, Layer: str): pass

	@property
	def MaxDurability(self) -> int: 
		"""Get the maximum durability of an Item. (0: no durability)"""
		return int() 
	
	@MaxDurability.setter
	def MaxDurability(self, MaxDurability: int): pass

	@property
	def Movable(self) -> bool: 
		"""Item is movable"""
		return bool() 
	
	@Movable.setter
	def Movable(self, Movable: bool): pass

	@property
	def Name(self) -> str: 
		"""Item name"""
		return str() 
	
	@Name.setter
	def Name(self, Name: str): pass

	@property
	def OnGround(self) -> bool: 
		"""True: if the item is on the ground - False: otherwise."""
		return bool() 
	
	@OnGround.setter
	def OnGround(self, OnGround: bool): pass

	@property
	def Position(self) -> "Point3D": return Point3D() 
	
	@Position.setter
	def Position(self, Position: "Point3D"): pass

	@property
	def Properties(self) -> "List[Property]": 
		"""Get the list of Properties of an Item."""
		return List[Property]() 
	
	@Properties.setter
	def Properties(self, Properties: "List[Property]"): pass

	@property
	def PropsUpdated(self) -> bool: 
		"""True: if Properties are updated - False: otherwise."""
		return bool() 
	
	@PropsUpdated.setter
	def PropsUpdated(self, PropsUpdated: bool): pass

	@property
	def RootContainer(self) -> int: 
		"""Get serial of root container of item."""
		return int() 
	
	@RootContainer.setter
	def RootContainer(self, RootContainer: int): pass

	@property
	def Serial(self) -> int: return int() 
	
	@Serial.setter
	def Serial(self, Serial: int): pass

	@property
	def Updated(self) -> bool: 
		"""Check if the Item already have been updated with all the properties. (need better documentation)"""
		return bool() 
	
	@Updated.setter
	def Updated(self, Updated: bool): pass

	@property
	def Visible(self) -> bool: 
		"""Item is Visible"""
		return bool() 
	
	@Visible.setter
	def Visible(self, Visible: bool): pass

	@property
	def Weight(self) -> int: 
		"""Get the weight of a item. (0: no weight)"""
		return int() 
	
	@Weight.setter
	def Weight(self, Weight: int): pass

	def DistanceTo(self, itm: Union["Item", "Mobile"]) -> int:
		"""
		Return the distance in number of tiles, from Item to Mobile.
		
		Parameters
		----------
		itm: Item or Mobile
			Target as Item
			Target as Mobile
		
		Returns
		-------
		int
			Distance in number of tiles.
		
		"""

	def GetWorldPosition(self) -> "Point3D":
		"""
		
		Returns
		-------
		Point3D
		
		"""

	def IsChildOf(self, container: Union["Item", "Mobile"]) -> bool:
		"""Check if an Item is contained in a container. Can be a Item or a Mobile (wear by).
		
		
		Parameters
		----------
		container: Item or Mobile
			Item as container.
			Mobile as container.
		
		Returns
		-------
		bool
			True: if is contained - False: otherwise.
		
		"""

	def ToString(self) -> str:
		"""
		
		Returns
		-------
		str
		
		"""


class Items:
	"""	
	<summary>
	The Items class provides a wide range of functions to search and interact with Items.
	</summary>
		
	"""

	@staticmethod
	def ApplyFilter(filter: "Items.Filter") -> "List[Item]":
		"""Filter the global list of Items according to the options specified by the filter ( see: Items.Filter ).
		
		Parameters
		----------
		filter: Items.Filter
			A filter object.
		
		Returns
		-------
		List[Item]
			the list of Items respectinf the filter criteria.
		
		"""

	@staticmethod
	def BackpackCount(itemid: int, color: int) -> int:
		"""Count items in Player Backpack.
		
		Parameters
		----------
		itemid: int
			ItemID to search.
		color: int
			Color to search. (default -1: any color)
		
		Returns
		-------
		int
		
		"""

	@staticmethod
	def ContainerCount(serial: Union[int, "Item"], itemid: int, color: int, recursive: bool) -> int:
		"""
		Count items inside a container, summing also the amount in stacks.
		
		Parameters
		----------
		serial: int or Item
			Serial or Item to search into.
		itemid: int
			ItemID of the item to search.
		color: int
			Color to match. (default: -1, any color)
		recursive: bool
			Search also in already open subcontainers.
		
		Returns
		-------
		int
		
		"""

	@staticmethod
	def ContextExist(i: Union["Item", int], name: str) -> int:
		"""
		Check if Context Menu entry exists for an Item.
		
		Parameters
		----------
		i: Item or int
			Serial or Item to check.
		name: str
			Name of the Context Manu entry
		
		Returns
		-------
		int
		
		"""

	@staticmethod
	def DropFromHand(item: "Item", container: "Item"):
		"""Drop into a bag an Item currently held in-hand. ( see: Items.Lift )
		
		Parameters
		----------
		item: Item
			Item object to drop.
		container: Item
			Target container.
		
		"""

	@staticmethod
	def DropItemGroundSelf(serialitem: Union[int, "Item"], amount: int):
		"""
		Drop an Item on the ground, at the current Player position.
		NOTE: On some server is not allowed to drop Items on tiles occupied by Mobiles and the Player.
		
		Parameters
		----------
		serialitem: int or Item
			Item object to drop.
		amount: int
			Amount to move. (default: 0, the whole stack)
		
		"""

	@staticmethod
	def FindByID(itemid: int, color: int, container: int, range: Union[int, bool], considerIgnoreList: bool) -> "Item":
		"""
		Find a single Item matching specific ItemID, Color and Container. 
		Optionally can search in all subcontaners or to a maximum depth in subcontainers.
		Can use -1 on color for no chose color, can use -1 on container for search in all item in memory. The depth defaults to only the top but can search for # of sub containers.
		
		Parameters
		----------
		itemid: int
			ItemID filter.
		color: int
			Color filter. (-1: any, 0: natural )
		container: int
			Serial of the container to search. (-1: any Item)
		range: int or bool
			Search subcontainers. 
			True: all subcontainers
			False: only main
			1,2,n: Maximum subcontainer depth
		considerIgnoreList: bool
			True: Ignore Items are excluded - False: any Item.
		
		Returns
		-------
		Item
			The Item matching the criteria.
		
		"""

	@staticmethod
	def FindBySerial(serial: int) -> "Item":
		"""Search for a specific Item by using it Serial
		
		Parameters
		----------
		serial: int
			Serial of the Item.
		
		Returns
		-------
		Item
			Item object if found, or null if not found.
		
		"""

	@staticmethod
	def GetImage(itemID: int, hue: int) -> "Bitmap":
		"""Get the Image on an Item by specifing the ItemID. Optinally is possible to apply a color.
		
		Parameters
		----------
		itemID: int
			ItemID to use.
		hue: int
			Optional: Color to apply. (Default 0, natural)
		
		Returns
		-------
		Bitmap
		
		"""

	@staticmethod
	def GetPropStringByIndex(item: Union["Item", int], index: int) -> str:
		"""Get a Property line, by index. if not found returns and empty string.
		
		
		Parameters
		----------
		item: Item or int
			Serial or Item to read.
		index: int
			Number of the Property line.
		
		Returns
		-------
		str
			A property line as a string.
		
		"""

	@staticmethod
	def GetPropStringList(serial: Union[int, "Item"]) -> "List[String]":
		"""Get string list of all Properties of an item, if item no props list is empty.
		
		
		Parameters
		----------
		serial: int or Item
			Serial or Item to read.
		
		Returns
		-------
		List[String]
			List of strings.
		
		"""

	@staticmethod
	def GetPropValue(serial: Union[int, "Item"], name: str) -> float:
		"""Read the value of a Property.
		
		
		Parameters
		----------
		serial: int or Item
			Serial or Item to read.
		name: str
			Name of the Propery.
		
		Returns
		-------
		float
		
		"""

	@staticmethod
	def Hide(item: Union["Item", int]):
		"""
		Hied an Item, affects only the player.
		
		Parameters
		----------
		item: Item or int
			Serial or Item to hide.
		
		"""

	@staticmethod
	def Lift(item: "Item", amount: int):
		"""Lift an Item and hold it in-hand. ( see: Items.DropFromHand )
		
		Parameters
		----------
		item: Item
			Item object to Lift.
		amount: int
			Amount to lift. (0: the whole stack)
		
		"""

	@staticmethod
	def Message(serial: Union[int, "Item"], hue: int, message: str):
		"""
		Display an in-game message on top of an Item, visibile only for the Player.
		
		Parameters
		----------
		serial: int or Item
			Serial or Item to display text on.
		hue: int
			Color of the message.
		message: str
			Message as
		
		"""

	@staticmethod
	def Move(source: Union["Item", int], destination: Union["Item", int, "Mobile"], amount: int, x: Union[int, None], y: Union[int, None]):
		"""
		Move an Item to a destination, which can be an Item or a Mobile.
		
		Parameters
		----------
		source: Item or int
			Serial or Item of the Item to move.
		destination: Item or int or Mobile
			Serial, Mobile or Item as destination.
		amount: int
			Amount to move (-1: the whole stack)
		x: int or None
			Optional: X coordinate inside the container.
		y: int or None
			Optional: Y coordinate inside the container.
		
		"""

	@staticmethod
	def MoveOnGround(source: Union[int, "Item"], amount: int, x: int, y: int, z: int):
		"""Move an Item on the ground to a specific location.
		
		
		Parameters
		----------
		source: int or Item
			Serial or Item to move.
		amount: int
			Amount of Items to move (0: the whole stack )
		x: int
			X world coordinates.
		y: int
			Y world coordinates.
		z: int
			Z world coordinates.
		
		"""

	@staticmethod
	def Select(items: "List[Item]", selector: str) -> "Item":
		"""
		
		Parameters
		----------
		items: List[Item]
		selector: str
		
		Returns
		-------
		Item
		
		"""

	@staticmethod
	def SetColor(serial: int, color: int):
		"""Change/override the Color of an Item, the change affects only Player client. The change is not persistent.
		If the color is -1 or unspecified, the color of the item is restored.
		
		Parameters
		----------
		serial: int
			Serial of the Item.
		color: int
			Color as number. (default: -1, reset original color)
		
		"""

	@staticmethod
	def SingleClick(itemserial: Union[int, "Item"]):
		"""
		Send a single click network event to the server.
		
		Parameters
		----------
		itemserial: int or Item
			Serial or Item to click
		
		"""

	@staticmethod
	def UseItem(itemSerial: Union[int, "Item"], targetSerial: Union[int, "EnhancedEntity", None], wait: Union[bool, None]):
		"""Use an Item, optionally is possible to specify a Item or Mobile target.
		NOTE: The optional target may not work on some free shards. Use Target.Execute instead.
		
		
		Parameters
		----------
		itemSerial: int or Item
			Serial or Item to use.
		targetSerial: int or EnhancedEntity or None
			Optional: Serial of the Item or Mobile target.
		wait: bool or None
			Optional: Wait for confirmation by the server. (default: True)
		
		"""

	@staticmethod
	def UseItemByID(itemid: int, color: int) -> bool:
		"""Use any item of a specific type, matching Item.ItemID. Optionally also of a specific color, matching Item.Hue.
		
		Parameters
		----------
		itemid: int
			ItemID to be used.
		color: int
			Color to be used. (default: -1, any)
		
		Returns
		-------
		bool
		
		"""

	@staticmethod
	def WaitForContents(bag: Union["Item", int], delay: int):
		"""Open a container an wait for the Items to load, for a maximum amount of time.
		
		
		Parameters
		----------
		bag: Item or int
			Container as Item object.
			Container as Item serial.
		delay: int
			Maximum wait, in milliseconds.
		
		"""

	@staticmethod
	def WaitForProps(i: Union["Item", int], delay: int):
		"""
		If not updated, request to the Properties of an Item, and wait for a maximum amount of time.
		
		Parameters
		----------
		i: Item or int
			Serial or Item read.
		delay: int
			Maximum waiting time, in milliseconds.
		
		"""


	class Filter:
		"""		
		<summary>
		The Items.Filter class is used to store options to filter the global Item list.
		Often used in combination with Items.ApplyFilter.
		</summary>
				
		"""
		@property
		def CheckIgnoreObject(self) -> bool: 
			"""Exclude from the search Items which are currently on the global Ignore List. ( default: False, any Item )"""
			return bool() 
		
		@CheckIgnoreObject.setter
		def CheckIgnoreObject(self, CheckIgnoreObject: bool): pass

		@property
		def Enabled(self) -> bool: 
			"""True: The filter is used - False: Return all Item. ( default: True, active )"""
			return bool() 
		
		@Enabled.setter
		def Enabled(self, Enabled: bool): pass

		@property
		def Graphics(self) -> "List[Int32]": 
			"""Limit the search to a list of Grapichs ID (see: Item.ItemID ) 
			Supports .Add() and .AddRange()"""
			return List[Int32]() 
		
		@Graphics.setter
		def Graphics(self, Graphics: "List[Int32]"): pass

		@property
		def Hues(self) -> "List[Int32]": 
			"""Limit the search to a list of Colors.
			Supports .Add() and .AddRange()"""
			return List[Int32]() 
		
		@Hues.setter
		def Hues(self, Hues: "List[Int32]"): pass

		@property
		def IsContainer(self) -> int: 
			"""Limit the search to the Items which are also containers. (default: -1: any Item)"""
			return int() 
		
		@IsContainer.setter
		def IsContainer(self, IsContainer: int): pass

		@property
		def IsCorpse(self) -> int: 
			"""Limit the search to the corpses on the ground. (default: -1, any Item)"""
			return int() 
		
		@IsCorpse.setter
		def IsCorpse(self, IsCorpse: int): pass

		@property
		def IsDoor(self) -> int: 
			"""Limit the search to the doors. (default: -1: any Item)"""
			return int() 
		
		@IsDoor.setter
		def IsDoor(self, IsDoor: int): pass

		@property
		def Layers(self) -> "List[String]": 
			"""Limit the search to the wearable Items by Layer.
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
			Talisman"""
			return List[String]() 
		
		@Layers.setter
		def Layers(self, Layers: "List[String]"): pass

		@property
		def Movable(self) -> int: 
			"""Limit the search to only Movable Items. ( default: -1, any Item )"""
			return int() 
		
		@Movable.setter
		def Movable(self, Movable: int): pass

		@property
		def Name(self) -> str: 
			"""Limit the search by name of the Item."""
			return str() 
		
		@Name.setter
		def Name(self, Name: str): pass

		@property
		def OnGround(self) -> int: 
			"""Limit the search to the Items on the ground. (default: -1, any Item)"""
			return int() 
		
		@OnGround.setter
		def OnGround(self, OnGround: int): pass

		@property
		def RangeMax(self) -> float: 
			"""Limit the search by distance, to Items on the ground which are at most RangeMax tiles away from the Player. ( default: -1, any Item )"""
			return float() 
		
		@RangeMax.setter
		def RangeMax(self, RangeMax: float): pass

		@property
		def RangeMin(self) -> float: 
			"""Limit the search by distance, to Items on the ground which are at least RangeMin tiles away from the Player. ( default: -1, any Item )"""
			return float() 
		
		@RangeMin.setter
		def RangeMin(self, RangeMin: float): pass

		@property
		def Serials(self) -> "List[Int32]": 
			"""Limit the search to a list of Serials of Item to find. (ex: 0x0406EFCA )
			Supports .Add() and .AddRange()"""
			return List[Int32]() 
		
		@Serials.setter
		def Serials(self, Serials: "List[Int32]"): pass



class Journal:
	"""	
	<summary>
	The Journal class provides access to the message Journal.
	</summary>
		
	"""

	@staticmethod
	def Clear():
		"""Removes all entry from the Jorunal. This operation is Global for all Razor.
		
		"""

	@staticmethod
	def GetJournalEntry(afterTimestap: Union[float, "Journal.JournalEntry"]) -> "List[Journal.JournalEntry]":
		"""Get a copy of all Journal lines as JournalEntry. The list can be filtered to include *only* most recent events.
		
		Parameters
		----------
		afterTimestap: float or Journal.JournalEntry
			Timestap as UnixTime, the number of seconds elapsed since 01-Jan-1970. (default: -1, no filter)
			A JournalEntry object (default: null, no filter)
		
		Returns
		-------
		List[Journal.JournalEntry]
			List of JournalEntry
		
		"""

	@staticmethod
	def GetLineText(text: str, addname: bool) -> str:
		"""Search and return the most recent line Journal containing the given text. (case sensitive)
		
		Parameters
		----------
		text: str
			Text to search.
		addname: bool
			Prepend source name. (default: False)
		
		Returns
		-------
		str
			Return the full line - Empty string if not found.
		
		"""

	@staticmethod
	def GetSpeechName() -> "List[String]":
		"""Get list of speakers.
		
		Returns
		-------
		List[String]
			List of speakers as text.
		
		"""

	@staticmethod
	def GetTextByColor(color: int, addname: bool) -> "List[String]":
		"""Returns all the lines present in the Journal for a given color.
		
		Parameters
		----------
		color: int
			Color of the soruce.
		addname: bool
			Prepend source name. (default: False)
		
		Returns
		-------
		List[String]
			A list of Journal as lines of text.
		
		"""

	@staticmethod
	def GetTextByName(name: str, addname: bool) -> "List[String]":
		"""Returns all the lines present in the Journal for a given source name. (case sensitive)
		
		Parameters
		----------
		name: str
			Name of the soruce.
		addname: bool
			Prepend source name. (default: False)
		
		Returns
		-------
		List[String]
			A list of Journal as lines of text.
		
		"""

	@staticmethod
	def GetTextBySerial(serial: int, addname: bool) -> "List[String]":
		"""Returns all the lines present in the Journal for a given serial.
		
		Parameters
		----------
		serial: int
			Serial of the soruce.
		addname: bool
			Prepend source name. (default: False)
		
		Returns
		-------
		List[String]
			A list of Journal as lines of text.
		
		"""

	@staticmethod
	def GetTextByType(type: str, addname: bool) -> "List[String]":
		"""Returns all the lines present in the Journal for a given type. (case sensitive)
		
		Parameters
		----------
		type: str
			Regular
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
		addname: bool
			Prepend source name. (default: False)
		
		Returns
		-------
		List[String]
			A list of Journal as lines of text.
		
		"""

	@staticmethod
	def Search(text: str) -> bool:
		"""Search in the Journal for the occurrence of text. (case sensitive)
		
		Parameters
		----------
		text: str
			Text to search.
		
		Returns
		-------
		bool
			True: Text is found - False: otherwise
		
		"""

	@staticmethod
	def SearchByColor(text: str, color: int) -> bool:
		"""Search in the Journal for the occurrence of text, for a given color. (case sensitive)
		
		Parameters
		----------
		text: str
			Text to search.
		color: int
			Color of the message.
		
		Returns
		-------
		bool
			True: Text is found - False: otherwise
		
		"""

	@staticmethod
	def SearchByName(text: str, name: str) -> bool:
		"""Search in the Journal for the occurrence of text, for a given soruce. (case sensitive)
		
		Parameters
		----------
		text: str
			Text to search.
		name: str
			Name of the source.
		
		Returns
		-------
		bool
			True: Text is found - False: otherwise
		
		"""

	@staticmethod
	def SearchByType(text: str, type: str) -> bool:
		"""Search in the Journal for the occurrence of text, for a given type. (case sensitive)
		
		Parameters
		----------
		text: str
			Text to search.
		type: str
			Regular
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
		
		Returns
		-------
		bool
			True: Text is found - False: otherwise
		
		"""

	@staticmethod
	def WaitByName(name: str, delay: int) -> bool:
		"""Pause script and wait for maximum amount of time, for a specific soruce to appear in Jorunal. (case sensitive)
		
		Parameters
		----------
		name: str
			Name of the soruce.
		delay: int
			Maximum pause in milliseconds.
		
		Returns
		-------
		bool
		
		"""

	@staticmethod
	def WaitJournal(msgs: Union["List[String]", str], delay: int) -> Union[str, bool]:
		"""
		Pause script and wait for maximum amount of time, for a specific text to appear in Journal. (case sensitive)
		
		Parameters
		----------
		msgs: List[String] or str
			Text to search.
		delay: int
			Maximum pause in milliseconds.
		
		Returns
		-------
		str, bool
			True: Text is found - False: otherwise
		
		"""


	class JournalEntry:
		"""		
		<summary>
		The JournalEntry class rapresents a line in the Journal.
		</summary>
				
		"""
		@property
		def Color(self) -> int: 
			"""Color of the text."""
			return int() 
		
		@Color.setter
		def Color(self, Color: int): pass

		@property
		def Name(self) -> str: 
			"""Name of the source, can be a Mobile or an Item."""
			return str() 
		
		@Name.setter
		def Name(self, Name: str): pass

		@property
		def Serial(self) -> int: 
			"""Name of the source, can be a Mobile or an Item."""
			return int() 
		
		@Serial.setter
		def Serial(self, Serial: int): pass

		@property
		def Text(self) -> str: 
			"""Actual content of the Journal Line."""
			return str() 
		
		@Text.setter
		def Text(self, Text: str): pass

		@property
		def Timestamp(self) -> float: 
			"""Timestamp as UnixTime, the number of seconds elapsed since 01-Jan-1970."""
			return float() 
		
		@Timestamp.setter
		def Timestamp(self, Timestamp: float): pass

		@property
		def Type(self) -> str: 
			"""Regular
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
			Special"""
			return str() 
		
		@Type.setter
		def Type(self, Type: str): pass

		def Copy(self) -> "Journal.JournalEntry":
			"""
			
			Returns
			-------
			Journal.JournalEntry
			
			"""


class Misc:
	"""	
	<summary>
	The Misc class contains general purpose functions of common use.
	</summary>
		
	"""

	@staticmethod
	def Beep():
		"""Play Beep system sound.
		
		"""

	@staticmethod
	def CancelPrompt():
		"""Cancel a prompt request.
		
		"""

	@staticmethod
	def CaptureNow():
		"""Creates a snapshot of the current UO window.
		
		"""

	@staticmethod
	def CheckIgnoreObject(serial: Union[int, "Item", "Mobile"]) -> bool:
		"""Check object from ignore list, return true if present. Can check Serial, Items or Mobiles
		
		
		Parameters
		----------
		serial: int or Item or Mobile
			Serial to check.
			Item to check
			Mobile to check
		
		Returns
		-------
		bool
			True: Object is ignored - False: otherwise.
		
		"""

	@staticmethod
	def CheckSharedValue(name: str) -> bool:
		"""Check if a shared value exixts.
		
		Parameters
		----------
		name: str
			Name of the value.
		
		Returns
		-------
		bool
			True: Shared value exists - False: otherwise.
		
		"""

	@staticmethod
	def ClearDragQueue():
		"""Clear the Drag-n-Drop queue.
		
		"""

	@staticmethod
	def ClearIgnore():
		"""Clear ignore list from all object
		
		"""

	@staticmethod
	def CloseBackpack():
		"""Close the backpack. 
		(OSI client only, no ClassicUO)
		
		"""

	@staticmethod
	def CloseMenu():
		"""Close opened Old Menu.
		
		"""

	@staticmethod
	def ContextReply(serial: Union[int, "Mobile", "Item"], menu_name: Union[str, int]):
		"""
		Respond to a context menu on mobile or item. Menu ID is base zero, or can use string of menu text.
		
		Parameters
		----------
		serial: int or Mobile or Item
			Serial of the Entity
		menu_name: str or int
			Name of the Entry as wirtten in-game.
			Poition of the option in the menu. Starts from 0.
		
		"""

	@staticmethod
	def CurrentScriptDirectory() -> str:
		"""Get the path to the Scripts directory.
		
		Returns
		-------
		str
			Path as text
		
		"""

	@staticmethod
	def Disconnect():
		"""Force client to disconnect.
		
		"""

	@staticmethod
	def DistanceSqrt(point_a: "Point3D", point_b: "Point3D") -> float:
		"""Compute the distance between 2 Point3D using pitagora's.
		
		Parameters
		----------
		point_a: Point3D
			First coordinates.
		point_b: Point3D
			Second coordinates.
		
		Returns
		-------
		float
		
		"""

	@staticmethod
	def ExportPythonAPI(path: str, pretty: bool):
		"""Return a string containing list RE Python API list in JSON format.
		
		Parameters
		----------
		path: str
			Name of the output file. (default: Config/AutoComplete.json )
		pretty: bool
			Print a readable JSON. (default: True )
		
		"""

	@staticmethod
	def FilterSeason(enable: bool, seasonFlag: "UInt32"):
		"""Enable or disable the Seasons filter forcing a specific season
		Season filter state will be saved on logout but not the season flag that will be recovered.
		
		Parameters
		----------
		enable: bool
			True: enable seasons filter
		seasonFlag: UInt32
			0: Spring (default fallback)
			1: Summer
			2: Fall
			3: Winter
			4: Desolation
		
		"""

	@staticmethod
	def FocusUOWindow():
		"""Set UoClient window in focus or restore if minimized.
		
		"""

	@staticmethod
	def GetContPosition() -> "Point":
		"""Get the position of the currently active Gump/Container.
		(OSI client only, no ClassicUO)
		
		Returns
		-------
		Point
			Return X,Y coordinates as a Point2D
		
		"""

	@staticmethod
	def GetMapInfo(serial: "UInt32") -> "Misc.MapInfo":
		"""Get MapInfo about a Mobile or Item using the serial
		
		Parameters
		----------
		serial: UInt32
			Serial of the object.
		
		Returns
		-------
		Misc.MapInfo
			A MapInfo object.
		
		"""

	@staticmethod
	def GetMenuTitle() -> str:
		"""Get the title of title for open Old Menu.
		
		Returns
		-------
		str
			Text of the title.
		
		"""

	@staticmethod
	def HasMenu() -> bool:
		"""Check if an Old Menu is open.
		
		Returns
		-------
		bool
			True: is open - False: otherwise
		
		"""

	@staticmethod
	def HasPrompt() -> bool:
		"""Check if have a prompt request.
		
		Returns
		-------
		bool
			True: there is a prompt - False: otherwise
		
		"""

	@staticmethod
	def HasQueryString() -> bool:
		"""Check if a have a query string menu opened, return true or false.
		
		Returns
		-------
		bool
			True: Has quesy - False: otherwise.
		
		"""

	@staticmethod
	def IgnoreObject(mob: Union["Mobile", "Item", int]):
		"""Add an entiry to the ignore list. Can ignore Serial, Items or Mobiles.
		
		
		Parameters
		----------
		mob: Mobile or Item or int
			Mobile to ignore
			Item to ignore
			Serial to ignore.
		
		"""

	@staticmethod
	def Inspect():
		"""Prompt the user with a Target. Open the inspector for the selected target.
		
		"""

	@staticmethod
	def LastHotKey() -> "HotKeyEvent":
		"""Returns the latest HotKey recorded by razor as HotKeyEvent object.
		
		Returns
		-------
		HotKeyEvent
		
		"""

	@staticmethod
	def MenuContain(text: str) -> bool:
		"""Search in open Old Menu if contains a specific text.
		
		Parameters
		----------
		text: str
			Text to search.
		
		Returns
		-------
		bool
			True: Text found - False: otherwise.
		
		"""

	@staticmethod
	def MenuResponse(text: str):
		"""Perform a menu response by subitem name. If item not exist close menu.
		
		Parameters
		----------
		text: str
			Name of subitem to respond.
		
		"""

	@staticmethod
	def MouseLocation() -> "Point":
		"""Returns a point with the X and Y coordinates of the mouse relative to the UO Window
		
		Returns
		-------
		Point
			Return X,Y coords as Point object.
		
		"""

	@staticmethod
	def MouseMove(posX: int, posY: int):
		"""Moves the mouse pointer to the position X,Y relative to the UO window
		
		Parameters
		----------
		posX: int
			X screen coordinate.
		posY: int
			Y screen coordinate.
		
		"""

	@staticmethod
	def NextContPosition(x: int, y: int):
		"""Return the X,Y of the next container, relative to the game window.
		(OSI client only, no ClassicUO)
		
		Parameters
		----------
		x: int
			X coordinate.
		y: int
			Y coordinate.
		
		"""

	@staticmethod
	def NoOperation():
		"""Just do nothing and enjot the present moment.
		
		"""

	@staticmethod
	def NoRunStealthStatus() -> bool:
		"""Get the status of "No Run When Stealth" via scripting.
		
		Returns
		-------
		bool
			True: Open is active - False: otherwise.
		
		"""

	@staticmethod
	def NoRunStealthToggle(enable: bool):
		"""Set "No Run When Stealth" via scripting. Changes via scripting are not persistents.
		
		Parameters
		----------
		enable: bool
			True: enable the option.
		
		"""

	@staticmethod
	def OpenPaperdoll():
		"""Open the backpack. 
		(OSI client only, no ClassicUO)
		
		"""

	@staticmethod
	def Pause(millisec: int):
		"""Pause the script for a given amount of time.
		
		Parameters
		----------
		millisec: int
			Pause duration, in milliseconds.
		
		"""

	@staticmethod
	def PetRename(mob: Union["Mobile", int], name: str):
		"""
		Rename a specific pet.
		
		Parameters
		----------
		mob: Mobile or int
			Mobile object representing the pet.
			Serial of the pet.
		name: str
			New name to set.
		
		"""

	@staticmethod
	def QueryStringResponse(okcancel: bool, response: str):
		"""Perform a query string response by ok or cancel button and specific response string.
		
		Parameters
		----------
		okcancel: bool
			OK Button
		response: str
			Cancel Button
		
		"""

	@staticmethod
	def ReadSharedValue(name: str) -> object:
		"""Get a Shared Value, if value not exist return null.
		Shared values are accessible by every script.
		
		Parameters
		----------
		name: str
			Name of the value.
		
		Returns
		-------
		object
			The stored object.
		
		"""

	@staticmethod
	def RemoveSharedValue(name: str):
		"""Remove a Shared Value.
		
		Parameters
		----------
		name: str
			Name of the value.
		
		"""

	@staticmethod
	def ResetPrompt():
		"""Reset a prompt response.
		
		"""

	@staticmethod
	def ResponsePrompt(text: str):
		"""Response a prompt request. Often used to rename runes and similar.
		
		Parameters
		----------
		text: str
			Text of the response.
		
		"""

	@staticmethod
	def Resync():
		"""Trigger a client ReSync.
		
		"""

	@staticmethod
	def ScriptRun(scriptfile: str):
		"""Run a script by file name, Script must be present in script grid.
		
		Parameters
		----------
		scriptfile: str
			Name of the script.
		
		"""

	@staticmethod
	def ScriptStatus(scriptfile: str) -> bool:
		"""Get status of script if running or not, Script must be present in script grid.
		
		Parameters
		----------
		scriptfile: str
		
		Returns
		-------
		bool
			True: Script is running - False: otherwise.
		
		"""

	@staticmethod
	def ScriptStop(scriptfile: str):
		"""Stop a script by file name, Script must be present in script grid.
		
		Parameters
		----------
		scriptfile: str
			Name of the script.
		
		"""

	@staticmethod
	def ScriptStopAll():
		"""Stop all script running.
		
		"""

	@staticmethod
	def SendMessage(msg: Union[str, bool, "UInt32", int, float, object, float], color: Union[int, bool, None], wait: Union[bool, None]):
		"""Send a message to the client.
		
		
		Parameters
		----------
		msg: str or bool or UInt32 or int or float or object or float
			The object to print.
		color: int or bool or None
			Color of the message.
		wait: bool or None
			True: Wait for confimation. - False: Returns instatnly.
		
		"""

	@staticmethod
	def SendToClient(keys: str):
		"""Send to the client a list of keystrokes. Can contain control characters: 
		- Send Control+Key: ctrl+u: ^u
		- Send ENTER: {Enter}
		Note: some keys don't work with ClassicUO (es: {Enter} )
		
		Parameters
		----------
		keys: str
			List of keys.
		
		"""

	@staticmethod
	def SetSharedValue(name: str, value: object):
		"""Set a Shared Value by specific name, if value exist he repalce value.
		Shared values are accessible by every script.
		
		Parameters
		----------
		name: str
			Name of the value.
		value: object
			Value to set.
		
		"""

	@staticmethod
	def ShardName() -> str:
		"""Get the name of the shard.
		
		Returns
		-------
		str
			Name of the shard
		
		"""

	@staticmethod
	def UnIgnoreObject(mob: Union["Mobile", "Item", int]):
		"""
		Remove object from ignore list. Can remove serial, items or mobiles
		
		Parameters
		----------
		mob: Mobile or Item or int
			Item to unignore
			Item to unignore.
			Serial to unignore.
		
		"""

	@staticmethod
	def WaitForContext(serial: Union[int, "Item", "Mobile"], delay: int) -> "List[Misc.Context]":
		"""Wait for Context Menu to appear, for a maximum amount of time. Usable on an Item or Mobile.
		
		
		Parameters
		----------
		serial: int or Item or Mobile
			Serial of the entity.
			Entity as Item object.
		delay: int
			Maximum wait.
		
		Returns
		-------
		List[Misc.Context]
		
		"""

	@staticmethod
	def WaitForMenu(delay: int) -> bool:
		"""Pause script until server send an Old Menu, for a maximum amount of time.
		
		Parameters
		----------
		delay: int
			Maximum wait, in milliseconds.
		
		Returns
		-------
		bool
			True: if the Old Menu is open - False: otherwise.
		
		"""

	@staticmethod
	def WaitForPrompt(delay: int) -> bool:
		"""Wait for a prompt for a maximum amount of time.
		
		Parameters
		----------
		delay: int
			Maximum wait time.
		
		Returns
		-------
		bool
			True: Prompt is present - False: otherwise
		
		"""

	@staticmethod
	def WaitForQueryString(delay: int) -> bool:
		"""Pause script until server send query string request, for a maximum amount of time.
		
		Parameters
		----------
		delay: int
			Maximum wait, in milliseconds.
		
		Returns
		-------
		bool
			True: if player has a query - False: otherwise.
		
		"""


	class Context:
		"""		
		<summary>
		The Context class holds information about a single entry in the Context Menu.
		</summary>
				
		"""
		@property
		def Entry(self) -> str: return str() 
		
		@Entry.setter
		def Entry(self, Entry: str): pass

		@property
		def Response(self) -> int: return int() 
		
		@Response.setter
		def Response(self, Response: int): pass



	class MapInfo:
		"""		
		<summary>
		The MapInfo class is used to store information about the Map location.
		</summary>
				
		"""
		@property
		def Facet(self) -> "UInt16": return UInt16() 
		
		@Facet.setter
		def Facet(self, Facet: "UInt16"): pass

		@property
		def MapEnd(self) -> "Point2D": return Point2D() 
		
		@MapEnd.setter
		def MapEnd(self, MapEnd: "Point2D"): pass

		@property
		def MapOrigin(self) -> "Point2D": return Point2D() 
		
		@MapOrigin.setter
		def MapOrigin(self, MapOrigin: "Point2D"): pass

		@property
		def PinPosition(self) -> "Point2D": return Point2D() 
		
		@PinPosition.setter
		def PinPosition(self, PinPosition: "Point2D"): pass

		@property
		def Serial(self) -> "UInt32": return UInt32() 
		
		@Serial.setter
		def Serial(self, Serial: "UInt32"): pass



class Mobile:
	"""	
	<summary>
	The Mobile class represents an single alive entity. 
	While the Mobile.Serial is unique for each Mobile, Mobile.MobileID is the unique for the Mobile apparence, or image. Sometimes is also called Body or Body ID.
	Mobiles which dies and leave a corpse behind, they stop existing as Mobiles and instead leave a corpse as a Item object appears.
	</summary>
		
	"""
	@property
	def Backpack(self) -> "Item": 
		"""Get the Item representing the backpack of a Mobile. Return null if it doesn't have one."""
		return Item() 
	
	@Backpack.setter
	def Backpack(self, Backpack: "Item"): pass

	@property
	def Body(self) -> int: 
		"""Represents the type of Mobile, usually unique for the Mobile image. ( Alias: Mobile.MobileID )"""
		return int() 
	
	@Body.setter
	def Body(self, Body: int): pass

	@property
	def Color(self) -> int: 
		"""Color of the mobile."""
		return int() 
	
	@Color.setter
	def Color(self, Color: int): pass

	@property
	def Contains(self) -> "List[Item]": 
		"""Returns the list of items present in the Paperdoll (or equivalent) of the Mobile.
		Might not match the items found using via Layer."""
		return List[Item]() 
	
	@Contains.setter
	def Contains(self, Contains: "List[Item]"): pass

	@property
	def Deleted(self) -> bool: return bool() 
	
	@Deleted.setter
	def Deleted(self, Deleted: bool): pass

	@property
	def Direction(self) -> str: 
		"""Returns the direction of the Mobile."""
		return str() 
	
	@Direction.setter
	def Direction(self, Direction: str): pass

	@property
	def Female(self) -> bool: 
		"""The Mobile is a female."""
		return bool() 
	
	@Female.setter
	def Female(self, Female: bool): pass

	@property
	def Flying(self) -> bool: 
		"""The mobile is Flying ( Gragoyle )"""
		return bool() 
	
	@Flying.setter
	def Flying(self, Flying: bool): pass

	@property
	def Hits(self) -> int: 
		"""The current hit point of a Mobile. To be read as propotion over Mobile.HitsMax."""
		return int() 
	
	@Hits.setter
	def Hits(self, Hits: int): pass

	@property
	def HitsMax(self) -> int: 
		"""Maximum hitpoint of a Mobile."""
		return int() 
	
	@HitsMax.setter
	def HitsMax(self, HitsMax: int): pass

	@property
	def Hue(self) -> int: return int() 
	
	@Hue.setter
	def Hue(self, Hue: int): pass

	@property
	def InParty(self) -> bool: 
		"""True: if the Mobile is in your party. - False: otherwise."""
		return bool() 
	
	@InParty.setter
	def InParty(self, InParty: bool): pass

	@property
	def IsGhost(self) -> bool: 
		"""If is a Ghost
		Match any MobileID  in the list:
		402, 403, 607, 608, 694, 695, 970"""
		return bool() 
	
	@IsGhost.setter
	def IsGhost(self, IsGhost: bool): pass

	@property
	def IsHuman(self) -> bool: 
		"""Check is the Mobile has a human body.
		Match any MobileID in the list:
		183, 184, 185, 186, 400, 
		401, 402, 403, 605, 606,
		607, 608, 666, 667, 694, 
		744, 745, 747, 748, 750,  
		751, 970, 695"""
		return bool() 
	
	@IsHuman.setter
	def IsHuman(self, IsHuman: bool): pass

	@property
	def Mana(self) -> int: 
		"""The current mana of a Mobile. To be read as propotion over Mobile.ManaMax."""
		return int() 
	
	@Mana.setter
	def Mana(self, Mana: int): pass

	@property
	def ManaMax(self) -> int: 
		"""Maximum mana of a Mobile."""
		return int() 
	
	@ManaMax.setter
	def ManaMax(self, ManaMax: int): pass

	@property
	def Map(self) -> int: 
		"""Current map or facet."""
		return int() 
	
	@Map.setter
	def Map(self, Map: int): pass

	@property
	def MobileID(self) -> int: 
		"""Represents the type of Mobile, usually unique for the Mobile image. ( Alias: Mobile.Body )"""
		return int() 
	
	@MobileID.setter
	def MobileID(self, MobileID: int): pass

	@property
	def Mount(self) -> "Item": 
		"""Returns the Item assigned to the "Mount" Layer."""
		return Item() 
	
	@Mount.setter
	def Mount(self, Mount: "Item"): pass

	@property
	def Name(self) -> str: 
		"""Name of the Mobile."""
		return str() 
	
	@Name.setter
	def Name(self, Name: str): pass

	@property
	def Notoriety(self) -> int: 
		"""Get the notoriety of the Mobile.
		
		Notorieties:
		1: blue, innocent
		2: green, friend
		3: gray, neutral
		4: gray, criminal
		5: orange, enemy
		6: red, hostile 
		6: yellow, invulnerable"""
		return int() 
	
	@Notoriety.setter
	def Notoriety(self, Notoriety: int): pass

	@property
	def Paralized(self) -> bool: 
		"""The mobile is Paralized."""
		return bool() 
	
	@Paralized.setter
	def Paralized(self, Paralized: bool): pass

	@property
	def Poisoned(self) -> bool: 
		"""The mobile is Poisoned."""
		return bool() 
	
	@Poisoned.setter
	def Poisoned(self, Poisoned: bool): pass

	@property
	def Position(self) -> "Point3D": return Point3D() 
	
	@Position.setter
	def Position(self, Position: "Point3D"): pass

	@property
	def Properties(self) -> "List[Property]": 
		"""Get all properties of a Mobile as list of lines of the tooltip."""
		return List[Property]() 
	
	@Properties.setter
	def Properties(self, Properties: "List[Property]"): pass

	@property
	def PropsUpdated(self) -> bool: 
		"""True: Mobile.Propertires are updated - False: otherwise."""
		return bool() 
	
	@PropsUpdated.setter
	def PropsUpdated(self, PropsUpdated: bool): pass

	@property
	def Quiver(self) -> "Item": 
		"""Get the Item representing the quiver of a Mobile. Return null if it doesn't have one."""
		return Item() 
	
	@Quiver.setter
	def Quiver(self, Quiver: "Item"): pass

	@property
	def Serial(self) -> int: return int() 
	
	@Serial.setter
	def Serial(self, Serial: int): pass

	@property
	def Stam(self) -> int: 
		"""The current stamina of a Mobile. To be read as propotion over Mobile.StamMax."""
		return int() 
	
	@Stam.setter
	def Stam(self, Stam: int): pass

	@property
	def StamMax(self) -> int: 
		"""Maximum stamina of a Mobile."""
		return int() 
	
	@StamMax.setter
	def StamMax(self, StamMax: int): pass

	@property
	def Visible(self) -> bool: 
		"""True: The Mobile is visible - Flase: The mobile is hidden."""
		return bool() 
	
	@Visible.setter
	def Visible(self, Visible: bool): pass

	@property
	def WarMode(self) -> bool: 
		"""Mobile is in War mode."""
		return bool() 
	
	@WarMode.setter
	def WarMode(self, WarMode: bool): pass

	@property
	def YellowHits(self) -> bool: 
		"""The mobile healthbar is not blue, but yellow."""
		return bool() 
	
	@YellowHits.setter
	def YellowHits(self, YellowHits: bool): pass

	def DistanceTo(self, other_mobile: "Mobile") -> int:
		"""Returns the distance between the current Mobile and another one.
		
		Parameters
		----------
		other_mobile: Mobile
			The other mobile.
		
		Returns
		-------
		int
			Distance in tiles
		
		"""

	def GetItemOnLayer(self, layer: str) -> "Item":
		"""Returns the Item associated with a Mobile Layer.
		
		Parameters
		----------
		layer: str
			Layers:
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
		
		Returns
		-------
		Item
			Item for the layer. Return null if not found or Layer invalid.
		
		"""


class Mobiles:
	"""	
	<summary>
	The Mobiles class provides a wide range of functions to search and interact with Mobile.
	</summary>
		
	"""

	@staticmethod
	def ApplyFilter(filter: "Mobiles.Filter") -> "List[Mobile]":
		"""
		
		Parameters
		----------
		filter: Mobiles.Filter
		
		Returns
		-------
		List[Mobile]
		
		"""

	@staticmethod
	def ContextExist(serial: Union[int, "Mobile"], name: str) -> int:
		"""
		
		Parameters
		----------
		serial: int or Mobile
		name: str
		
		Returns
		-------
		int
		
		"""

	@staticmethod
	def FindBySerial(serial: int) -> "Mobile":
		"""Find the Mobile with a specific Serial.
		
		Parameters
		----------
		serial: int
			Serial of the Mobile.
		
		Returns
		-------
		Mobile
		
		"""

	@staticmethod
	def GetPropStringByIndex(serial: Union[int, "Mobile"], index: int) -> str:
		"""
		
		Parameters
		----------
		serial: int or Mobile
		index: int
		
		Returns
		-------
		str
		
		"""

	@staticmethod
	def GetPropStringList(mob: Union["Mobile", int]) -> "List[String]":
		"""
		
		Parameters
		----------
		mob: Mobile or int
		
		Returns
		-------
		List[String]
		
		"""

	@staticmethod
	def GetPropValue(mob: Union["Mobile", int], name: str) -> float:
		"""
		
		Parameters
		----------
		mob: Mobile or int
		name: str
		
		Returns
		-------
		float
		
		"""

	@staticmethod
	def GetTrackingInfo() -> "Mobiles.TrackingInfo":
		"""Get the most updated information about tracking.
		
		Returns
		-------
		Mobiles.TrackingInfo
		
		"""

	@staticmethod
	def Message(mobile: Union["Mobile", int], hue: int, message: str, wait: bool):
		"""
		
		Parameters
		----------
		mobile: Mobile or int
		hue: int
		message: str
		wait: bool
		
		"""

	@staticmethod
	def Select(mobiles: "List[Mobile]", selector: str) -> "Mobile":
		"""
		
		Parameters
		----------
		mobiles: List[Mobile]
		selector: str
		
		Returns
		-------
		Mobile
		
		"""

	@staticmethod
	def SingleClick(mobileserial: Union[int, "Mobile"]):
		"""
		
		Parameters
		----------
		mobileserial: int or Mobile
		
		"""

	@staticmethod
	def UseMobile(mobileserial: Union[int, "Mobile"]):
		"""
		
		Parameters
		----------
		mobileserial: int or Mobile
		
		"""

	@staticmethod
	def WaitForProps(m: Union["Mobile", int], delay: int):
		"""
		
		Parameters
		----------
		m: Mobile or int
		delay: int
		
		"""

	@staticmethod
	def WaitForStats(mobileserial: Union[int, "Mobile"], delay: int):
		"""
		
		Parameters
		----------
		mobileserial: int or Mobile
		delay: int
		
		"""


	class Filter:
		"""		
		<summary>
		The Mobiles.Filter class is used to store options to filter the global Mobile list.
		Often used in combination with Mobiles.ApplyFilter.
		</summary>
				
		"""
		@property
		def Blessed(self) -> int: 
			"""Limit the search to only Blessed Mobiles.  (default: -1, any Mobile)"""
			return int() 
		
		@Blessed.setter
		def Blessed(self, Blessed: int): pass

		@property
		def Bodies(self) -> "List[Int32]": 
			"""Limit the search to a list of MobileID (see: Mobile.ItemID or Mobile.Body ) 
			Supports .Add() and .AddRange()"""
			return List[Int32]() 
		
		@Bodies.setter
		def Bodies(self, Bodies: "List[Int32]"): pass

		@property
		def CheckIgnoreObject(self) -> bool: 
			"""Exclude from the search Mobiles which are currently on the global Ignore List. ( default: False, any Item )"""
			return bool() 
		
		@CheckIgnoreObject.setter
		def CheckIgnoreObject(self, CheckIgnoreObject: bool): pass

		@property
		def CheckLineOfSight(self) -> bool: 
			"""Limit the search only to the Mobiles which are in line of sight. (default: false, any Mobile)"""
			return bool() 
		
		@CheckLineOfSight.setter
		def CheckLineOfSight(self, CheckLineOfSight: bool): pass

		@property
		def Enabled(self) -> bool: 
			"""True: The filter is used - False: Return all Mobile. ( default: True, active )"""
			return bool() 
		
		@Enabled.setter
		def Enabled(self, Enabled: bool): pass

		@property
		def Female(self) -> int: 
			"""Limit the search to female Mobile.  (default: -1, any)"""
			return int() 
		
		@Female.setter
		def Female(self, Female: int): pass

		@property
		def Friend(self) -> int: 
			"""Limit the search to friend Mobile. (default: -1, any)"""
			return int() 
		
		@Friend.setter
		def Friend(self, Friend: int): pass

		@property
		def Hues(self) -> "List[Int32]": 
			"""Limit the search to a list of Colors.
			Supports .Add() and .AddRange()"""
			return List[Int32]() 
		
		@Hues.setter
		def Hues(self, Hues: "List[Int32]"): pass

		@property
		def IsGhost(self) -> int: 
			"""Limit the search to Ghost only. (default: -1, any Mobile )
			Match any MobileID in the list:
			402, 403, 607, 608, 694, 695, 970"""
			return int() 
		
		@IsGhost.setter
		def IsGhost(self, IsGhost: int): pass

		@property
		def IsHuman(self) -> int: 
			"""Limit the search to Humans only. (default: -1, any Mobile )
			Match any MobileID in the list:
			183, 184, 185, 186, 400, 
			401, 402, 403, 605, 606,
			607, 608, 666, 667, 694, 
			744, 745, 747, 748, 750,  
			751, 970, 695"""
			return int() 
		
		@IsHuman.setter
		def IsHuman(self, IsHuman: int): pass

		@property
		def Name(self) -> str: 
			"""Limit the search by name of the Mobile."""
			return str() 
		
		@Name.setter
		def Name(self, Name: str): pass

		@property
		def Notorieties(self) -> "List[Byte]": 
			"""Limit the search to the Mobile by notoriety.
			Supports .Add() and .AddRange()
			
			Notorieties:
			1: blue, innocent
			2: green, friend
			3: gray, neutral
			4: gray, criminal
			5: orange, enemy
			6: red, hostile 
			6: yellow, invulnerable"""
			return List[Byte]() 
		
		@Notorieties.setter
		def Notorieties(self, Notorieties: "List[Byte]"): pass

		@property
		def Paralized(self) -> int: 
			"""Limit the search to paralized Mobile. (default: -1, any)"""
			return int() 
		
		@Paralized.setter
		def Paralized(self, Paralized: int): pass

		@property
		def Poisoned(self) -> int: 
			"""Limit the search to only Poisoned Mobiles.  (default: -1, any Mobile)"""
			return int() 
		
		@Poisoned.setter
		def Poisoned(self, Poisoned: int): pass

		@property
		def RangeMax(self) -> float: 
			"""Limit the search by distance, to Mobiles which are at most RangeMax tiles away from the Player. ( default: -1, any Mobile )"""
			return float() 
		
		@RangeMax.setter
		def RangeMax(self, RangeMax: float): pass

		@property
		def RangeMin(self) -> float: 
			"""Limit the search by distance, to Mobiles which are at least RangeMin tiles away from the Player. ( default: -1, any Mobile )"""
			return float() 
		
		@RangeMin.setter
		def RangeMin(self, RangeMin: float): pass

		@property
		def Serials(self) -> "List[Int32]": 
			"""Limit the search to a list of Serials of Mobile to find. (ex: 0x0406EFCA )
			Supports .Add() and .AddRange()"""
			return List[Int32]() 
		
		@Serials.setter
		def Serials(self, Serials: "List[Int32]"): pass

		@property
		def Warmode(self) -> int: 
			"""Limit the search to Mobile War mode. (default: -1, any Mobile)
			-1: any
			0: peace
			1: war"""
			return int() 
		
		@Warmode.setter
		def Warmode(self, Warmode: int): pass



	class TrackingInfo:
		"""		
		<summary>
		The TrackingInfo class hold the latest information about. 
		</summary>
				
		"""
		@property
		def lastUpdate(self) -> "DateTime": return DateTime() 
		
		@lastUpdate.setter
		def lastUpdate(self, lastUpdate: "DateTime"): pass

		@property
		def serial(self) -> "UInt32": return UInt32() 
		
		@serial.setter
		def serial(self, serial: "UInt32"): pass

		@property
		def x(self) -> "UInt16": return UInt16() 
		
		@x.setter
		def x(self, x: "UInt16"): pass

		@property
		def y(self) -> "UInt16": return UInt16() 
		
		@y.setter
		def y(self, y: "UInt16"): pass



class Organizer:
	"""	
	<summary>
	The Organizer class allow you to interect with the Scavenger Agent, via scripting.
	</summary>
		
	"""

	@staticmethod
	def ChangeList(listName: str):
		"""Change the Organizer's active list.
		
		Parameters
		----------
		listName: str
			Name of an existing organizer list.
		
		"""

	@staticmethod
	def FStart():
		"""Start the Organizer Agent on the currently active list.
		
		"""

	@staticmethod
	def FStop():
		"""Stop the Organizer Agent.
		
		"""

	@staticmethod
	def RunOnce(organizerName: str, sourceBag: int, destBag: int, dragDelay: int):
		"""
		
		Parameters
		----------
		organizerName: str
		sourceBag: int
		destBag: int
		dragDelay: int
		
		"""

	@staticmethod
	def Status() -> bool:
		"""Check Organizer Agent status
		
		Returns
		-------
		bool
			True: if the Organizer is running - False: otherwise
		
		"""


class PathFinding:
	"""	
	<summary>
	This class implements the PathFinding algorithm using A-Star. 
	</summary>
		
	"""

	@staticmethod
	def GetPath(dst_x: int, dst_y: int, ignoremob: bool) -> "List[Tile]":
		"""Compute the path for the given destination and returns a list of Tile (coordinates).
		
		Parameters
		----------
		dst_x: int
			Destination X.
		dst_y: int
			Destination Y.
		ignoremob: bool
			Ignores any mobiles with the path calculation.
		
		Returns
		-------
		List[Tile]
			List of Tile objects, each holds a .X and .Y coordinates.
		
		"""

	@staticmethod
	def Go(r: "PathFinding.Route") -> bool:
		"""Check if a destination is reachable.
		
		Parameters
		----------
		r: PathFinding.Route
			A customized Route object.
		
		Returns
		-------
		bool
			True: if a destination is reachable.
		
		"""

	@staticmethod
	def RunPath(path: "List[Tile]", timeout: float, debugMessage: bool, useResync: bool) -> bool:
		"""
		
		Parameters
		----------
		path: List[Tile]
		timeout: float
		debugMessage: bool
		useResync: bool
		
		Returns
		-------
		bool
		
		"""

	@staticmethod
	def Tile(x: int, y: int) -> "Tile":
		"""Create a Tile starting from X,Y coordinates (see PathFindig.RunPath)
		
		Parameters
		----------
		x: int
			X coordinate
		y: int
			Y coordinate
		
		Returns
		-------
		Tile
			Returns a Tile object
		
		"""


	class Route:
		"""		
		<summary>
		The Route class is used to configure the PathFinding.
		</summary>
				
		"""
		@property
		def DebugMessage(self) -> bool: 
			"""Outputs a debug message. (default: False)"""
			return bool() 
		
		@DebugMessage.setter
		def DebugMessage(self, DebugMessage: bool): pass

		@property
		def IgnoreMobile(self) -> bool: 
			"""Ignores any mobiles with the path calculation. (default: 0)"""
			return bool() 
		
		@IgnoreMobile.setter
		def IgnoreMobile(self, IgnoreMobile: bool): pass

		@property
		def MaxRetry(self) -> int: 
			"""Number of attempts untill the path calculation is halted. (default: -1, no limit)"""
			return int() 
		
		@MaxRetry.setter
		def MaxRetry(self, MaxRetry: int): pass

		@property
		def StopIfStuck(self) -> bool: 
			"""Halts the pathfinding fail to walk the path. (default: 0)"""
			return bool() 
		
		@StopIfStuck.setter
		def StopIfStuck(self, StopIfStuck: bool): pass

		@property
		def Timeout(self) -> float: 
			"""Maximum amount of time to run the path. (default: -1, no limit)"""
			return float() 
		
		@Timeout.setter
		def Timeout(self, Timeout: float): pass

		@property
		def UseResync(self) -> bool: 
			"""ReSyncs the path calculation. (default: False)"""
			return bool() 
		
		@UseResync.setter
		def UseResync(self, UseResync: bool): pass

		@property
		def X(self) -> int: 
			"""Sets the destination position X. (default: 0)"""
			return int() 
		
		@X.setter
		def X(self, X: int): pass

		@property
		def Y(self) -> int: 
			"""Sets the destination position Y. (default: 0)"""
			return int() 
		
		@Y.setter
		def Y(self, Y: int): pass



class Player:
	"""	
	<summary>
	The Player class represent the currently logged in character.
	</summary>
		
	"""
	@property
	def AR(self) -> int: 
		"""Resistance to Phisical damage."""
		return int() 
	
	@AR.setter
	def AR(self, AR: int): pass

	@property
	def Backpack(self) -> "Item": 
		"""Player backpack, as Item object."""
		return Item() 
	
	@Backpack.setter
	def Backpack(self, Backpack: "Item"): pass

	@property
	def Bank(self) -> "Item": 
		"""Player bank chest, as Item object."""
		return Item() 
	
	@Bank.setter
	def Bank(self, Bank: "Item"): pass

	@property
	def Body(self) -> int: 
		"""Player Body or MobileID (see: Mobile.Body)"""
		return int() 
	
	@Body.setter
	def Body(self, Body: int): pass

	@property
	def Buffs(self) -> "List[String]": 
		"""List of Player active buffs:
		Meditation
		Agility
		Animal Form
		Arcane Enpowerment
		Arcane Enpowerment (new)
		Arch Protection
		Armor Pierce
		Attunement
		Aura of Nausea
		Bleed
		Bless
		Block
		Bload Oath (caster)
		Bload Oath (curse)
		BloodWorm Anemia
		City Trade Deal
		Clumsy
		Confidence
		Corpse Skin
		Counter Attack
		Criminal
		Cunning
		Curse
		Curse Weapon
		Death Strike
		Defense Mastery
		Despair
		Despair (target)
		Disarm (new)
		Disguised
		Dismount Prevention
		Divine Fury
		Dragon Slasher Fear
		Enchant
		Enemy Of One
		Enemy Of One (new)
		Essence Of Wind
		Ethereal Voyage
		Evasion
		Evil Omen
		Faction Loss
		Fan Dancer Fan Fire
		Feeble Mind
		Feint
		Force Arrow
		Berserk
		Fly
		Gaze Despair
		Gift Of Life
		Gift Of Renewal
		Healing
		Heat Of Battle
		Hiding
		Hiryu Physical Malus
		Hit Dual Wield
		Hit Lower Attack
		Hit Lower Defense
		Honorable Execution
		Honored
		Horrific Beast
		Hawl Of Cacophony
		Immolating Weapon
		Incognito
		Inspire
		Invigorate
		Invisibility
		Lich Form
		Lighting Strike
		Magic Fish
		Magic Reflection
		Mana Phase
		Mass Curse
		Medusa Stone
		Mind Rot
		Momentum Strike
		Mortal Strike
		Night Sight
		NoRearm
		Orange Petals
		Pain Spike
		Paralyze
		Perfection
		Perseverance
		Poison
		Poison Resistance
		Polymorph
		Protection
		Psychic Attack
		Consecrate Weapon
		Rage
		Rage Focusing
		Rage Focusing (target)
		Reactive Armor
		Reaper Form
		Resilience
		Rose Of Trinsic
		Rotworm Blood Disease
		Rune Beetle Corruption
		Skill Use Delay
		Sleep
		Spell Focusing
		Spell Focusing (target)
		Spell Plague
		Splintering Effect
		Stone Form
		Strangle
		Strength
		Surge
		Swing Speed
		Talon Strike
		Vampiric Embrace
		Weaken
		Wraith Form"""
		return List[String]() 
	
	@Buffs.setter
	def Buffs(self, Buffs: "List[String]"): pass

	@property
	def ColdResistance(self) -> int: 
		"""Resistance to Cold damage."""
		return int() 
	
	@ColdResistance.setter
	def ColdResistance(self, ColdResistance: int): pass

	@property
	def DamageChanceIncrease(self) -> int: 
		"""Get total Damage Chance Increase."""
		return int() 
	
	@DamageChanceIncrease.setter
	def DamageChanceIncrease(self, DamageChanceIncrease: int): pass

	@property
	def DefenseChanceIncrease(self) -> int: 
		"""Get total Defense Chance Increase."""
		return int() 
	
	@DefenseChanceIncrease.setter
	def DefenseChanceIncrease(self, DefenseChanceIncrease: int): pass

	@property
	def Dex(self) -> int: 
		"""Stats value for Dexterity."""
		return int() 
	
	@Dex.setter
	def Dex(self, Dex: int): pass

	@property
	def DexterityIncrease(self) -> int: 
		"""Get total Dexterity Increase."""
		return int() 
	
	@DexterityIncrease.setter
	def DexterityIncrease(self, DexterityIncrease: int): pass

	@property
	def Direction(self) -> str: 
		"""Player current direction, as text."""
		return str() 
	
	@Direction.setter
	def Direction(self, Direction: str): pass

	@property
	def EnergyResistance(self) -> int: 
		"""Resistance to Energy damage."""
		return int() 
	
	@EnergyResistance.setter
	def EnergyResistance(self, EnergyResistance: int): pass

	@property
	def EnhancePotions(self) -> int: 
		"""Get total Enhance Potions."""
		return int() 
	
	@EnhancePotions.setter
	def EnhancePotions(self, EnhancePotions: int): pass

	@property
	def FasterCasting(self) -> int: 
		"""Get total Faster Casting."""
		return int() 
	
	@FasterCasting.setter
	def FasterCasting(self, FasterCasting: int): pass

	@property
	def FasterCastRecovery(self) -> int: 
		"""Get total Faster Cast Recovery."""
		return int() 
	
	@FasterCastRecovery.setter
	def FasterCastRecovery(self, FasterCastRecovery: int): pass

	@property
	def Female(self) -> bool: 
		"""Player is a female."""
		return bool() 
	
	@Female.setter
	def Female(self, Female: bool): pass

	@property
	def FireResistance(self) -> int: 
		"""Resistance to Fire damage."""
		return int() 
	
	@FireResistance.setter
	def FireResistance(self, FireResistance: int): pass

	@property
	def Followers(self) -> int: 
		"""Player current amount of pet/followers."""
		return int() 
	
	@Followers.setter
	def Followers(self, Followers: int): pass

	@property
	def FollowersMax(self) -> int: 
		"""Player maximum amount of pet/followers."""
		return int() 
	
	@FollowersMax.setter
	def FollowersMax(self, FollowersMax: int): pass

	@property
	def Gold(self) -> int: 
		"""Player total gold, in the backpack."""
		return int() 
	
	@Gold.setter
	def Gold(self, Gold: int): pass

	@property
	def HasSpecial(self) -> bool: 
		"""Player have a special abilities active."""
		return bool() 
	
	@HasSpecial.setter
	def HasSpecial(self, HasSpecial: bool): pass

	@property
	def HitPointsIncrease(self) -> int: 
		"""Get total Hit Points Increase."""
		return int() 
	
	@HitPointsIncrease.setter
	def HitPointsIncrease(self, HitPointsIncrease: int): pass

	@property
	def HitPointsRegeneration(self) -> int: 
		"""Get total Hit Points Regeneration."""
		return int() 
	
	@HitPointsRegeneration.setter
	def HitPointsRegeneration(self, HitPointsRegeneration: int): pass

	@property
	def Hits(self) -> int: 
		"""Current hit points."""
		return int() 
	
	@Hits.setter
	def Hits(self, Hits: int): pass

	@property
	def HitsMax(self) -> int: 
		"""Maximum hit points."""
		return int() 
	
	@HitsMax.setter
	def HitsMax(self, HitsMax: int): pass

	@property
	def InParty(self) -> bool: 
		"""Player is in praty."""
		return bool() 
	
	@InParty.setter
	def InParty(self, InParty: bool): pass

	@property
	def Int(self) -> int: 
		"""Stats value for Intelligence."""
		return int() 
	
	@Int.setter
	def Int(self, Int: int): pass

	@property
	def IntelligenceIncrease(self) -> int: 
		"""Get total Intelligence Increase."""
		return int() 
	
	@IntelligenceIncrease.setter
	def IntelligenceIncrease(self, IntelligenceIncrease: int): pass

	@property
	def IsGhost(self) -> bool: 
		"""Player is a Ghost"""
		return bool() 
	
	@IsGhost.setter
	def IsGhost(self, IsGhost: bool): pass

	@property
	def LowerManaCost(self) -> int: 
		"""Get total Lower Mana Cost."""
		return int() 
	
	@LowerManaCost.setter
	def LowerManaCost(self, LowerManaCost: int): pass

	@property
	def LowerReagentCost(self) -> int: 
		"""Get total Lower Reagent Cost."""
		return int() 
	
	@LowerReagentCost.setter
	def LowerReagentCost(self, LowerReagentCost: int): pass

	@property
	def Luck(self) -> int: 
		"""Player total luck."""
		return int() 
	
	@Luck.setter
	def Luck(self, Luck: int): pass

	@property
	def Mana(self) -> int: 
		"""Current mana."""
		return int() 
	
	@Mana.setter
	def Mana(self, Mana: int): pass

	@property
	def ManaIncrease(self) -> int: 
		"""Get total Mana Increase."""
		return int() 
	
	@ManaIncrease.setter
	def ManaIncrease(self, ManaIncrease: int): pass

	@property
	def ManaMax(self) -> int: 
		"""Maximum mana."""
		return int() 
	
	@ManaMax.setter
	def ManaMax(self, ManaMax: int): pass

	@property
	def ManaRegeneration(self) -> int: 
		"""Get total Mana Regeneration."""
		return int() 
	
	@ManaRegeneration.setter
	def ManaRegeneration(self, ManaRegeneration: int): pass

	@property
	def Map(self) -> int: 
		"""Player current map, or facet."""
		return int() 
	
	@Map.setter
	def Map(self, Map: int): pass

	@property
	def MaximumHitPointsIncrease(self) -> int: 
		"""Get total Maximum Hit Points Increase."""
		return int() 
	
	@MaximumHitPointsIncrease.setter
	def MaximumHitPointsIncrease(self, MaximumHitPointsIncrease: int): pass

	@property
	def MaximumManaIncrease(self) -> int: 
		"""Get total Maximum Mana Increase."""
		return int() 
	
	@MaximumManaIncrease.setter
	def MaximumManaIncrease(self, MaximumManaIncrease: int): pass

	@property
	def MaximumStaminaIncrease(self) -> int: 
		"""Get total Maximum Stamina Increase."""
		return int() 
	
	@MaximumStaminaIncrease.setter
	def MaximumStaminaIncrease(self, MaximumStaminaIncrease: int): pass

	@property
	def MaxWeight(self) -> int: 
		"""Player maximum weight."""
		return int() 
	
	@MaxWeight.setter
	def MaxWeight(self, MaxWeight: int): pass

	@property
	def MobileID(self) -> int: 
		"""Player MobileID or Body (see: Mobile.MobileID)"""
		return int() 
	
	@MobileID.setter
	def MobileID(self, MobileID: int): pass

	@property
	def Mount(self) -> "Item": 
		"""Player current Mount, as Item object.
		NOTE: On some server the Serial return by this function doesn't match the mount serial."""
		return Item() 
	
	@Mount.setter
	def Mount(self, Mount: "Item"): pass

	@property
	def Name(self) -> str: 
		"""Player name."""
		return str() 
	
	@Name.setter
	def Name(self, Name: str): pass

	@property
	def Notoriety(self) -> int: 
		"""Player notoriety
		1: blue, innocent
		2: green, friend
		3: gray, neutral
		4: gray, criminal
		5: orange, enemy
		6: red, hostile 
		6: yellow, invulnerable"""
		return int() 
	
	@Notoriety.setter
	def Notoriety(self, Notoriety: int): pass

	@property
	def Paralized(self) -> bool: 
		"""Player is Paralized. True also while frozen because of casting of spells."""
		return bool() 
	
	@Paralized.setter
	def Paralized(self, Paralized: bool): pass

	@property
	def Poisoned(self) -> bool: 
		"""Player is Poisoned"""
		return bool() 
	
	@Poisoned.setter
	def Poisoned(self, Poisoned: bool): pass

	@property
	def PoisonResistance(self) -> int: 
		"""Resistance to Poison damage."""
		return int() 
	
	@PoisonResistance.setter
	def PoisonResistance(self, PoisonResistance: int): pass

	@property
	def Position(self) -> "Point3D": 
		"""Current Player position as Point3D object."""
		return Point3D() 
	
	@Position.setter
	def Position(self, Position: "Point3D"): pass

	@property
	def Quiver(self) -> "Item": 
		"""Player quiver, as Item object."""
		return Item() 
	
	@Quiver.setter
	def Quiver(self, Quiver: "Item"): pass

	@property
	def ReflectPhysicalDamage(self) -> int: 
		"""Get total Reflect Physical Damage."""
		return int() 
	
	@ReflectPhysicalDamage.setter
	def ReflectPhysicalDamage(self, ReflectPhysicalDamage: int): pass

	@property
	def Serial(self) -> int: 
		"""Player unique Serial."""
		return int() 
	
	@Serial.setter
	def Serial(self, Serial: int): pass

	@property
	def SpellDamageIncrease(self) -> int: 
		"""Get total Spell Damage Increase."""
		return int() 
	
	@SpellDamageIncrease.setter
	def SpellDamageIncrease(self, SpellDamageIncrease: int): pass

	@property
	def Stam(self) -> int: 
		"""Current stamina."""
		return int() 
	
	@Stam.setter
	def Stam(self, Stam: int): pass

	@property
	def StaminaIncrease(self) -> int: 
		"""Get total Stamina Increase."""
		return int() 
	
	@StaminaIncrease.setter
	def StaminaIncrease(self, StaminaIncrease: int): pass

	@property
	def StaminaRegeneration(self) -> int: 
		"""Get total Stamina Regeneration."""
		return int() 
	
	@StaminaRegeneration.setter
	def StaminaRegeneration(self, StaminaRegeneration: int): pass

	@property
	def StamMax(self) -> int: 
		"""Maximum stamina."""
		return int() 
	
	@StamMax.setter
	def StamMax(self, StamMax: int): pass

	@property
	def StatCap(self) -> int: 
		"""Get the stats cap."""
		return int() 
	
	@StatCap.setter
	def StatCap(self, StatCap: int): pass

	@property
	def StaticMount(self) -> int: 
		"""Retrieves serial of mount set in Filter/Mount GUI."""
		return int() 
	
	@StaticMount.setter
	def StaticMount(self, StaticMount: int): pass

	@property
	def Str(self) -> int: 
		"""Stats value for Strenght."""
		return int() 
	
	@Str.setter
	def Str(self, Str: int): pass

	@property
	def StrengthIncrease(self) -> int: 
		"""Get total Strength Increase."""
		return int() 
	
	@StrengthIncrease.setter
	def StrengthIncrease(self, StrengthIncrease: int): pass

	@property
	def SwingSpeedIncrease(self) -> int: 
		"""Get total Swing Speed Increase."""
		return int() 
	
	@SwingSpeedIncrease.setter
	def SwingSpeedIncrease(self, SwingSpeedIncrease: int): pass

	@property
	def Visible(self) -> bool: 
		"""Player is visible, false if hidden."""
		return bool() 
	
	@Visible.setter
	def Visible(self, Visible: bool): pass

	@property
	def WarMode(self) -> bool: 
		"""Player has war mode active."""
		return bool() 
	
	@WarMode.setter
	def WarMode(self, WarMode: bool): pass

	@property
	def Weight(self) -> int: 
		"""Player current weight."""
		return int() 
	
	@Weight.setter
	def Weight(self, Weight: int): pass

	@property
	def YellowHits(self) -> bool: 
		"""Player HP bar is not blue, but yellow."""
		return bool() 
	
	@YellowHits.setter
	def YellowHits(self, YellowHits: bool): pass

	@staticmethod
	def Area() -> str:
		"""Get the name of the area in which the Player is currently in. (Ex: Britain, Destard, Vesper, Moongate, etc)
		Regions are defined inside by Config/regions.json.
		
		Returns
		-------
		str
			Name of the area. Unknown if not recognized.
		
		"""

	@staticmethod
	def Attack(serial: Union[int, "Mobile"]):
		"""Attack a Mobile.
		
		
		Parameters
		----------
		serial: int or Mobile
			Serial or Mobile to attack.
		
		"""

	@staticmethod
	def AttackLast():
		"""Attack last target.
		
		"""

	@staticmethod
	def BuffsExist(buffname: str) -> bool:
		"""Check if a buff is active, by buff name.
		
		Parameters
		----------
		buffname: str
			Meditation
			Agility
			Animal Form
			Arcane Enpowerment
			Arcane Enpowerment (new)
			Arch Protection
			Armor Pierce
			Attunement
			Aura of Nausea
			Bleed
			Bless
			Block
			Bload Oath (caster)
			Bload Oath (curse)
			BloodWorm Anemia
			City Trade Deal
			Clumsy
			Confidence
			Corpse Skin
			Counter Attack
			Criminal
			Cunning
			Curse
			Curse Weapon
			Death Strike
			Defense Mastery
			Despair
			Despair (target)
			Disarm (new)
			Disguised
			Dismount Prevention
			Divine Fury
			Dragon Slasher Fear
			Enchant
			Enemy Of One
			Enemy Of One (new)
			Essence Of Wind
			Ethereal Voyage
			Evasion
			Evil Omen
			Faction Loss
			Fan Dancer Fan Fire
			Feeble Mind
			Feint
			Force Arrow
			Berserk
			Fly
			Gaze Despair
			Gift Of Life
			Gift Of Renewal
			Healing
			Heat Of Battle
			Hiding
			Hiryu Physical Malus
			Hit Dual Wield
			Hit Lower Attack
			Hit Lower Defense
			Honorable Execution
			Honored
			Horrific Beast
			Hawl Of Cacophony
			Immolating Weapon
			Incognito
			Inspire
			Invigorate
			Invisibility
			Lich Form
			Lighting Strike
			Magic Fish
			Magic Reflection
			Mana Phase
			Mass Curse
			Medusa Stone
			Mind Rot
			Momentum Strike
			Mortal Strike
			Night Sight
			NoRearm
			Orange Petals
			Pain Spike
			Paralyze
			Perfection
			Perseverance
			Poison
			Poison Resistance
			Polymorph
			Protection
			Psychic Attack
			Consecrate Weapon
			Rage
			Rage Focusing
			Rage Focusing (target)
			Reactive Armor
			Reaper Form
			Resilience
			Rose Of Trinsic
			Rotworm Blood Disease
			Rune Beetle Corruption
			Skill Use Delay
			Sleep
			Spell Focusing
			Spell Focusing (target)
			Spell Plague
			Splintering Effect
			Stone Form
			Strangle
			Strength
			Surge
			Swing Speed
			Talon Strike
			Vampiric Embrace
			Weaken
			Wraith Form
		
		Returns
		-------
		bool
			True: if the buff is active - False: otherwise.
		
		"""

	@staticmethod
	def ChatAlliance(msg: Union[int, str]):
		"""
		Send message to the alliace chat.
		
		Parameters
		----------
		msg: int or str
			Message to send.
		
		"""

	@staticmethod
	def ChatChannel(msg: Union[int, str]):
		"""
		Send an chat channel message.
		
		Parameters
		----------
		msg: int or str
			Message to send.
		
		"""

	@staticmethod
	def ChatEmote(color: int, msg: Union[int, str]):
		"""Send an emote in game.
		
		
		Parameters
		----------
		color: int
			Color of the text
		msg: int or str
			Message to send.
		
		"""

	@staticmethod
	def ChatGuild(msg: Union[int, str]):
		"""
		Send message to the guild chat.
		
		Parameters
		----------
		msg: int or str
			Message to send.
		
		"""

	@staticmethod
	def ChatParty(msg: str, recepient_serial: int):
		"""Send message in arty chat. If a recepient_serial is specified, the message is private.
		
		Parameters
		----------
		msg: str
			Text to send.
		recepient_serial: int
			Optional: Target of private message.
		
		"""

	@staticmethod
	def ChatSay(color: int, msg: Union[str, int]):
		"""Send message in game.
		
		
		Parameters
		----------
		color: int
			Color of the text
		msg: str or int
			Message to send.
		
		"""

	@staticmethod
	def ChatWhisper(color: int, msg: Union[str, int]):
		"""Send an wishper message.
		
		
		Parameters
		----------
		color: int
			Color of the text
		msg: str or int
			Message to send.
		
		"""

	@staticmethod
	def ChatYell(color: int, msg: Union[str, int]):
		"""
		Send an yell message.
		
		Parameters
		----------
		color: int
			Color of the text
		msg: str or int
			Message to send.
		
		"""

	@staticmethod
	def CheckLayer(layer: str) -> bool:
		"""Check if a Layer is equipped by the Item.
		
		Parameters
		----------
		layer: str
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
			Hair
			Waist
			InnerTorso
			Bracelet
			FacialHair
			MiddleTorso
			Earrings
			Arms
			Cloak
			OuterTorso
			OuterLegs
			InnerLegs
			Talisman
		
		Returns
		-------
		bool
			True: the Layer is occupied by an Item - False: otherwise.
		
		"""

	@staticmethod
	def DistanceTo(target: Union["Mobile", "Item"]) -> int:
		"""Returns the distance between the Player and a Mobile or an Item.
		
		
		Parameters
		----------
		target: Mobile or Item
			The other Mobile or Item
		
		Returns
		-------
		int
			Distance in number of tiles.
		
		"""

	@staticmethod
	def EquipItem(item: Union["Item", int]):
		"""
		Equip an Item
		
		Parameters
		----------
		item: Item or int
			Serial or Item to equip.
		
		"""

	@staticmethod
	def EquipUO3D(serials: "List[Int32]"):
		"""
		
		Parameters
		----------
		serials: List[Int32]
		
		"""

	@staticmethod
	def Fly(status: bool):
		"""Enable or disable Gargoyle Flying.
		
		Parameters
		----------
		status: bool
			True: Gargoyle Fly ON - False: Gargoyle fly OFF
		
		"""

	@staticmethod
	def GetItemOnLayer(layer: str) -> "Item":
		"""Returns the Item associated with a Mobile Layer.
		
		Parameters
		----------
		layer: str
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
			Hair
			Waist
			InnerTorso
			Bracelet
			FacialHair
			MiddleTorso
			Earrings
			Arms
			Cloak
			OuterTorso
			OuterLegs
			InnerLegs
			Talisman
		
		Returns
		-------
		Item
			Item for the layer. Return null if not found or Layer invalid.
		
		"""

	@staticmethod
	def GetPropStringByIndex(index: int) -> str:
		"""Get a single line of Properties of the Player, from the tooltip, as text.
		
		Parameters
		----------
		index: int
			Line number, start from 0.
		
		Returns
		-------
		str
			Single line of text.
		
		"""

	@staticmethod
	def GetPropStringList() -> "List[String]":
		"""Get the list of Properties of the Player, as list of lines of the tooltip.
		
		Returns
		-------
		List[String]
			List of text lines.
		
		"""

	@staticmethod
	def GetPropValue(name: str) -> int:
		"""Get the numeric value of a specific Player property, from the tooltip.
		
		Parameters
		----------
		name: str
			Name of the property.
		
		Returns
		-------
		int
			n: value of the propery 
			0: property not found.
			1: property found, but not numeric.
		
		"""

	@staticmethod
	def GetRealSkillValue(skillname: str) -> float:
		"""Get the base/real value of the skill for the given the skill name.
		
		Parameters
		----------
		skillname: str
			Alchemy
			Anatomy
			Animal Lore
			Item ID
			Arms Lore
			Parry
			Begging
			Blacksmith
			Fletching
			Peacemaking
			Camping
			Carpentry
			Cartography
			Cooking
			Detect Hidden
			Discordance
			EvalInt
			Healing
			Fishing
			Forensics
			Herding
			Hiding
			Provocation
			Inscribe
			Lockpicking
			Magery
			Magic Resist
			Mysticism
			Tactics
			Snooping
			Musicianship
			Poisoning
			Archery
			Spirit Speak
			Stealing
			Tailoring
			Animal Taming
			Taste ID
			Tinkering
			Tracking
			Veterinary
			Swords
			Macing
			Fencing
			Wrestling
			Lumberjacking
			Mining
			Meditation
			Stealth
			Remove Trap
			Necromancy
			Focus
			Chivalry
			Bushido
			Ninjitsu
			Spell Weaving
			Imbuing
		
		Returns
		-------
		float
			Value of the skill.
		
		"""

	@staticmethod
	def GetSkillCap(skillname: str) -> float:
		"""Get the skill cap for the given the skill name.
		
		Parameters
		----------
		skillname: str
			Alchemy
			Anatomy
			Animal Lore
			Item ID
			Arms Lore
			Parry
			Begging
			Blacksmith
			Fletching
			Peacemaking
			Camping
			Carpentry
			Cartography
			Cooking
			Detect Hidden
			Discordance
			EvalInt
			Healing
			Fishing
			Forensics
			Herding
			Hiding
			Provocation
			Inscribe
			Lockpicking
			Magery
			Magic Resist
			Mysticism
			Tactics
			Snooping
			Musicianship
			Poisoning
			Archery
			Spirit Speak
			Stealing
			Tailoring
			Animal Taming
			Taste ID
			Tinkering
			Tracking
			Veterinary
			Swords
			Macing
			Fencing
			Wrestling
			Lumberjacking
			Mining
			Meditation
			Stealth
			Remove Trap
			Necromancy
			Focus
			Chivalry
			Bushido
			Ninjitsu
			Spell Weaving
			Imbuing
		
		Returns
		-------
		float
			Value of the skill cap.
		
		"""

	@staticmethod
	def GetSkillStatus(skillname: str) -> int:
		"""Get lock status for a specific skill.
		
		Parameters
		----------
		skillname: str
			Alchemy
			Anatomy
			Animal Lore
			Item ID
			Arms Lore
			Parry
			Begging
			Blacksmith
			Fletching
			Peacemaking
			Camping
			Carpentry
			Cartography
			Cooking
			Detect Hidden
			Discordance
			EvalInt
			Healing
			Fishing
			Forensics
			Herding
			Hiding
			Provocation
			Inscribe
			Lockpicking
			Magery
			Magic Resist
			Mysticism
			Tactics
			Snooping
			Musicianship
			Poisoning
			Archery
			Spirit Speak
			Stealing
			Tailoring
			Animal Taming
			Taste ID
			Tinkering
			Tracking
			Veterinary
			Swords
			Macing
			Fencing
			Wrestling
			Lumberjacking
			Mining
			Meditation
			Stealth
			Remove Trap
			Necromancy
			Focus
			Chivalry
			Bushido
			Ninjitsu
			Spell Weaving
			Imbuing
		
		Returns
		-------
		int
			Lock status:
			0: Up     
			1: Down 
			2: Locked 
			-1: Error
		
		"""

	@staticmethod
	def GetSkillValue(skillname: str) -> float:
		"""Get the value of the skill, with modifiers, for the given the skill name.
		
		Parameters
		----------
		skillname: str
			Alchemy
			Anatomy
			Animal Lore
			Item ID
			Arms Lore
			Parry
			Begging
			Blacksmith
			Fletching
			Peacemaking
			Camping
			Carpentry
			Cartography
			Cooking
			Detect Hidden
			Discordance
			EvalInt
			Healing
			Fishing
			Forensics
			Herding
			Hiding
			Provocation
			Inscribe
			Lockpicking
			Magery
			Magic Resist
			Mysticism
			Tactics
			Snooping
			Musicianship
			Poisoning
			Archery
			Spirit Speak
			Stealing
			Tailoring
			Animal Taming
			Taste ID
			Tinkering
			Tracking
			Veterinary
			Swords
			Macing
			Fencing
			Wrestling
			Lumberjacking
			Mining
			Meditation
			Stealth
			Remove Trap
			Necromancy
			Focus
			Chivalry
			Bushido
			Ninjitsu
			Spell Weaving
			Imbuing
		
		Returns
		-------
		float
			Value of the skill.
		
		"""

	@staticmethod
	def GetStatStatus(statname: str) -> int:
		"""Get lock status for a specific stats.
		
		Parameters
		----------
		statname: str
			Strength
			Dexterity
			Intelligence
		
		Returns
		-------
		int
			Lock status:
			0: Up     
			1: Down 
			2: Locked
		
		"""

	@staticmethod
	def GuildButton():
		"""Press the Guild menu button in the paperdoll.
		
		"""

	@staticmethod
	def HeadMessage(color: int, msg: Union[str, int]):
		"""
		Display a message above the Player. Visible only by the Player.
		
		Parameters
		----------
		color: int
			Color of the Text.
		msg: str or int
			Text of the message.
		
		"""

	@staticmethod
	def InRangeItem(item: Union["Item", int], range: int) -> bool:
		"""
		
		Parameters
		----------
		item: Item or int
		range: int
		
		Returns
		-------
		bool
		
		"""

	@staticmethod
	def InRangeMobile(mobile: Union[int, "Mobile"], range: int) -> bool:
		"""
		
		Parameters
		----------
		mobile: int or Mobile
		range: int
		
		Returns
		-------
		bool
		
		"""

	@staticmethod
	def InvokeVirtue(virtue: str):
		"""Invoke a virtue by name.
		
		Parameters
		----------
		virtue: str
			Honor
			Sacrifice
			Valor
			Compassion
			Honesty
			Humility
			Justice
		
		"""

	@staticmethod
	def KickMember(serial: int):
		"""Kick a member from party by serial. Only for party leader
		
		Parameters
		----------
		serial: int
			Serial of the Mobile to remove.
		
		"""

	@staticmethod
	def LeaveParty(force: bool):
		"""Leaves a party.
		
		Parameters
		----------
		force: bool
			True: Leave the party invite even you notin any party.
		
		"""

	@staticmethod
	def MapSay(msg: Union[int, str]):
		"""Send message in the Map chat.
		
		
		Parameters
		----------
		msg: int or str
			Message to send
		
		"""

	@staticmethod
	def PartyAccept(from_serial: int, force: bool) -> bool:
		"""Accept an incoming party offer. In case of multiple party oebnding invitation, from_serial is specified,
		
		Parameters
		----------
		from_serial: int
			Optional: Serial to accept party from.( in case of multiple offers )
		force: bool
			True: Accept the party invite even you are already in a party.
		
		Returns
		-------
		bool
			True: if you are now in a party - False: otherwise.
		
		"""

	@staticmethod
	def PartyCanLoot(CanLoot: bool):
		"""Set the Party loot permissions.
		
		Parameters
		----------
		CanLoot: bool
		
		"""

	@staticmethod
	def PartyInvite():
		"""Invite a person to a party. Prompt for a in-game Target.
		
		"""

	@staticmethod
	def PathFindTo(x: Union[int, "Point3D"], y: Union[int, None], z: Union[int, None]):
		"""Go to the given coordinates using Client-provided pathfinding.
		
		
		Parameters
		----------
		x: int or Point3D
			X map coordinates or Point3D
		y: int or None
			Y map coordinates
		z: int or None
			Z map coordinates
		
		"""

	@staticmethod
	def QuestButton():
		"""Press the Quest menu button in the paperdoll.
		
		"""

	@staticmethod
	def Run(direction: str, checkPosition: bool) -> bool:
		"""Run one step in the specified direction and wait for the confirmation of the new position by the server.
		If the character is not facing the direction, the first step only "turn" the Player in the required direction.
		Optional:
		When checkPosition is True allow for slower but safe walking, the new position confirmed at each step via return value.
		When checkPosition is Flase allow for faster walking/running, but requires custom delay and position checking.
		Info:
		Walking:  5 tiles/sec (~200ms between each step)
		Running: 10 tiles/sec (~100ms between each step)
		
		Parameters
		----------
		direction: str
			North
			South
			East
			West
			Up
			Down
			Left
			Right
		checkPosition: bool
			True: Wait until the server confirm the new Player.Position - False: Don't wait.
		
		Returns
		-------
		bool
			True: Destination reached - False: Coudn't reach the destination.
		
		"""

	@staticmethod
	def SetSkillStatus(skillname: str, status: int):
		"""Set lock status for a specific skill.
		
		Parameters
		----------
		skillname: str
			Alchemy
			Anatomy
			Animal Lore
			Item ID
			Arms Lore
			Parry
			Begging
			Blacksmith
			Fletching
			Peacemaking
			Camping
			Carpentry
			Cartography
			Cooking
			Detect Hidden
			Discordance
			EvalInt
			Healing
			Fishing
			Forensics
			Herding
			Hiding
			Provocation
			Inscribe
			Lockpicking
			Magery
			Magic Resist
			Mysticism
			Tactics
			Snooping
			Musicianship
			Poisoning
			Archery
			Spirit Speak
			Stealing
			Tailoring
			Animal Taming
			Taste ID
			Tinkering
			Tracking
			Veterinary
			Swords
			Macing
			Fencing
			Wrestling
			Lumberjacking
			Mining
			Meditation
			Stealth
			Remove Trap
			Necromancy
			Focus
			Chivalry
			Bushido
			Ninjitsu
			Spell Weaving
			Imbuing
		status: int
			Lock status:
			0: Up     
			1: Down 
			2: Locked
		
		"""

	@staticmethod
	def SetStatStatus(statname: str, status: int):
		"""Set lock status for a specific skill.
		
		Parameters
		----------
		statname: str
		status: int
			Lock status:
			0: Up     
			1: Down 
			2: Locked
		
		"""

	@staticmethod
	def SetWarMode(warflag: bool):
		"""Set war Mode on on/off.
		
		Parameters
		----------
		warflag: bool
			True: War - False: Peace
		
		"""

	@staticmethod
	def SpellIsEnabled(spellname: str) -> bool:
		"""Check if spell is active using the spell name (for spells that have this function).
		
		Parameters
		----------
		spellname: str
			Name of the spell.
		
		Returns
		-------
		bool
			True: the spell is enabled - False: otherwise,.
		
		"""

	@staticmethod
	def SumAttribute(attributename: str) -> float:
		"""Scan all the equipped Item, returns the total value of a specific property. (ex: Lower Reagent Cost )
		NOTE: This function is slow.
		
		Parameters
		----------
		attributename: str
			Name of the property.
		
		Returns
		-------
		float
			The total value as number.
		
		"""

	@staticmethod
	def ToggleAlwaysRun():
		"""Toggle on/off the awlays run flag. 
		NOTE: Works only on OSI client.
		
		"""

	@staticmethod
	def UnEquipItemByLayer(layer: str, wait: bool):
		"""Unequip the Item associated with a specific Layer.
		
		Parameters
		----------
		layer: str
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
			Hair
			Waist
			InnerTorso
			Bracelet
			FacialHair
			MiddleTorso
			Earrings
			Arms
			Cloak
			OuterTorso
			OuterLegs
			InnerLegs
			Talisman
		wait: bool
			Wait for confirmation from the server.
		
		"""

	@staticmethod
	def UseSkill(skillname: str, target: Union["Mobile", int, "Item", bool, None], wait: Union[bool, None]):
		"""
		Use a specific skill, and optionally apply that skill to the target specified.
		
		Parameters
		----------
		skillname: str
			Alchemy
			Anatomy
			Animal Lore
			Item ID
			Arms Lore
			Parry
			Begging
			Blacksmith
			Fletching
			Peacemaking
			Camping
			Carpentry
			Cartography
			Cooking
			Detect Hidden
			Discordance
			EvalInt
			Healing
			Fishing
			Forensics
			Herding
			Hiding
			Provocation
			Inscribe
			Lockpicking
			Magery
			Magic Resist
			Mysticism
			Tactics
			Snooping
			Musicianship
			Poisoning
			Archery
			Spirit Speak
			Stealing
			Tailoring
			Animal Taming
			Taste ID
			Tinkering
			Tracking
			Veterinary
			Swords
			Macing
			Fencing
			Wrestling
			Lumberjacking
			Mining
			Meditation
			Stealth
			Remove Trap
			Necromancy
			Focus
			Chivalry
			Bushido
			Ninjitsu
			Spell Weaving
			Imbuing
		target: Mobile or int or Item or bool or None
			Optional: Serial, Mobile or Item to target. (default: null)
		wait: bool or None
			Optional: True: wait for confirmation from the server (default: False)
		
		"""

	@staticmethod
	def UseSkillOnly(skillname: str, wait: bool):
		"""
		
		Parameters
		----------
		skillname: str
		wait: bool
		
		"""

	@staticmethod
	def Walk(direction: str, checkPosition: bool) -> bool:
		"""Walk one step in the specified direction and wait for the confirmation of the new position by the server.
		If the character is not facing the direction, the first step only "turn" the Player in the required direction.
		Optional:
		When checkPosition is True allow for slower but safe walking, the new position confirmed at each step via return value.
		When checkPosition is Flase allow for faster walking/running, but requires custom delay and position checking.
		Info:
		Walking:  5 tiles/sec (~200ms between each step)
		Running: 10 tiles/sec (~100ms between each step)
		
		Parameters
		----------
		direction: str
			North
			South
			East
			West
			Up
			Down
			Left
			Right
		checkPosition: bool
			True: Wait until the server confirm the new Player.Position - False: Don't wait.
		
		Returns
		-------
		bool
			True: Destination reached - False: Coudn't reach the destination.
		
		"""

	@staticmethod
	def WeaponClearSA():
		"""Disable any active Special Ability of the weapon.
		
		"""

	@staticmethod
	def WeaponDisarmSA():
		"""Toggle Disarm Ability.
		
		"""

	@staticmethod
	def WeaponPrimarySA():
		"""Toggle on/off the primary Special Ability of the weapon.
		
		"""

	@staticmethod
	def WeaponSecondarySA():
		"""Toggle on/off the secondary Special Ability of the weapon.
		
		"""

	@staticmethod
	def WeaponStunSA():
		"""Toggle Stun Ability.
		
		"""

	@staticmethod
	def Zone() -> str:
		"""Get the type of zone in which the Player is currently in.
		Regions are defined inside by Config/regions.json.
		
		Returns
		-------
		str
			Towns
			Dungeons
			Guarded
			Forest
			Unknown
		
		"""


class Point2D:
	"""		
	"""
	@property
	def X(self) -> int: return int() 
	
	@X.setter
	def X(self, X: int): pass

	@property
	def Y(self) -> int: return int() 
	
	@Y.setter
	def Y(self, Y: int): pass

	def ToString(self) -> str:
		"""
		
		Returns
		-------
		str
		
		"""


class Point3D:
	"""		
	"""
	@property
	def X(self) -> int: return int() 
	
	@X.setter
	def X(self, X: int): pass

	@property
	def Y(self) -> int: return int() 
	
	@Y.setter
	def Y(self, Y: int): pass

	@property
	def Z(self) -> int: return int() 
	
	@Z.setter
	def Z(self, Z: int): pass

	def ToString(self) -> str:
		"""
		
		Returns
		-------
		str
		
		"""


class Property:
	"""		
	"""
	@property
	def Args(self) -> str: return str() 
	
	@Args.setter
	def Args(self, Args: str): pass

	@property
	def Number(self) -> int: return int() 
	
	@Number.setter
	def Number(self, Number: int): pass

	def ToString(self) -> str:
		"""
		
		Returns
		-------
		str
		
		"""


class Restock:
	"""	
	<summary>
	The Restock class allow you to interact with the Restock Agent, via scripting.
	</summary>
		
	"""

	@staticmethod
	def ChangeList(listName: str):
		"""Change the Restock's active list.
		
		Parameters
		----------
		listName: str
			Name of an existing restock list.
		
		"""

	@staticmethod
	def FStart():
		"""Start the Restock Agent on the currently active list.
		
		"""

	@staticmethod
	def FStop():
		"""Stop the Restock Agent.
		
		"""

	@staticmethod
	def Status() -> bool:
		"""Check Restock Agent status
		
		Returns
		-------
		bool
			True: if the Restock is running - False: otherwise
		
		"""


class Scavenger:
	"""	
	<summary>
	The Scavenger class allow you to interect with the Scavenger Agent, via scripting.
	</summary>
		
	"""

	@staticmethod
	def ChangeList(listName: str):
		"""Change the Scavenger's active list.
		
		Parameters
		----------
		listName: str
			Name of an existing organizer list.
		
		"""

	@staticmethod
	def GetScavengerBag() -> "UInt32":
		"""Get current Scravenger destination container.
		
		Returns
		-------
		UInt32
			Serial of the container.
		
		"""

	@staticmethod
	def ResetIgnore():
		"""
		
		"""

	@staticmethod
	def RunOnce(scavengerList: "List[Scavenger.ScavengerItem]", millisec: int, filter: "Items.Filter"):
		"""
		
		Parameters
		----------
		scavengerList: List[Scavenger.ScavengerItem]
		millisec: int
		filter: Items.Filter
		
		"""

	@staticmethod
	def Start():
		"""Start the Scavenger Agent on the currently active list.
		
		"""

	@staticmethod
	def Status() -> bool:
		"""Check Scavenger Agent status
		
		Returns
		-------
		bool
			True: if the Scavenger is running - False: otherwise
		
		"""

	@staticmethod
	def Stop():
		"""Stop the Scavenger Agent.
		
		"""


class SellAgent:
	"""	
	<summary>
	The SellAgent class allow you to interect with the SellAgent, via scripting.
	</summary>
		
	"""

	@staticmethod
	def ChangeList(listName: str):
		"""
		
		Parameters
		----------
		listName: str
		
		"""

	@staticmethod
	def Disable():
		"""
		
		"""

	@staticmethod
	def Enable():
		"""
		
		"""

	@staticmethod
	def Status() -> bool:
		"""
		
		Returns
		-------
		bool
		
		"""


class Spells:
	"""	
	<summary>
	The Spells class allow you to cast any spell and use abilities, via scripting.
	</summary>
		
	"""

	@staticmethod
	def Cast(SpellName: str, mobile: Union["Mobile", "UInt32", None], wait: Union[bool, None]):
		"""
		Cast spell using the spell name. See the skill-specific functions to get the full list of spell names.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		Parameters
		----------
		SpellName: str
			Name of the spell to cast.
		mobile: Mobile or UInt32 or None
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastBushido(SpellName: str, wait: bool):
		"""Cast a Bushido spell using the spell name.
		
		Parameters
		----------
		SpellName: str
			Honorable Execution
			Confidence
			Counter Attack
			Lightning Strike
			Evasion
			Momentum Strike
		wait: bool
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastChivalry(SpellName: str, target: Union["UInt32", "Mobile", None], wait: Union[bool, None]):
		"""Cast a Chivalry spell using the spell name.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		
		Parameters
		----------
		SpellName: str
			Curse Weapon
			Pain Spike
			Corpse Skin
			Evil Omen
			Blood Oath
			Wraith Form
			Mind Rot
			Summon Familiar
			Horrific Beast
			Animate Dead
			Poison Strike
			Wither
			Strangle
			Lich Form
			Exorcism
			Vengeful Spirit
			Vampiric Embrace
		target: UInt32 or Mobile or None
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastCleric(SpellName: str, mobile: Union["Mobile", "UInt32", None], wait: Union[bool, None]):
		"""Cast a Cleric spell using the spell name.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		
		Parameters
		----------
		SpellName: str
			Bark Skin : Turns the druid's skin to bark, increasing physical, poison and energy resistence while reducing fire resistence.
			Circle Of Thorns : Creates a ring of thorns preventing an enemy from moving.
			Deadly Spores : The enemy is afflicted by poisonous spores.
			Enchanted Grove : Causes a grove of magical trees to grow, hiding the player for a short time.
			Firefly : Summons a tiny firefly to light the Druid's path. The Firefly is a weak creature with little or no combat skills.
			Forest Kin : Summons from a list of woodland spirits that will fight for the druid and assist him in different ways.
			Grasping Roots : Summons roots from the ground to entangle a single target.
			Hibernate : Causes the target to go to sleep.
			Hollow Reed : Increases both the strength and the intelligence of the Druid.
			Hurricane : Calls forth a violent hurricane that damages any enemies within range.
			Lure Stone : Creates a magical stone that calls all nearby animals to it.
			Mana Spring : Creates a magical spring that restores mana to the druid and any party members within range.
			Mushroom Gateway : A magical circle of mushrooms opens, allowing the Druid to step through it to another location.
			Pack Of Beasts : Summons a pack of beasts to fight for the Druid. Spell length increases with skill.
			Restorative Soil : Saturates a patch of land with power, causing healing mud to seep through . The mud can restore the dead to life.
			Shield Of Earth : A quick-growing wall of foliage springs up at the bidding of the Druid.
			Spring Of Life : Creates a magical spring that heals the Druid and their party.
			Swarm Of Insects : Summons a swarm of insects that bite and sting the Druid's enemies.
			Treefellow : Summons a powerful woodland spirit to fight for the Druid.
			Volcanic Eruption : A blast of molten lava bursts from the ground, hitting every enemy nearby.
		mobile: Mobile or UInt32 or None
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastDruid(SpellName: str, target: Union["UInt32", "Mobile", None], wait: Union[bool, None]):
		"""Cast a Druid spell using the spell name.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		
		Parameters
		----------
		SpellName: str
			Angelic Faith : Turns you into an angel, boosting your stats. At 100 Spirit Speak you get +20 Str/Dex/Int. Every 5 points of SS = +1 point to each stat, at a max of +24. Will also boost your Anatomy, Mace Fighting and Healing, following the same formula.
			Banish Evil : Banishes Undead targets. Auto kills rotting corpses, lich lords, etc. Works well at Doom Champ. Does not produce a corpse however
			Dampen Spirit : Drains the stamina of your target, according to the description
			Divine Focus : Heal for more, but may be broken.
			Hammer of Faith : Summons a War Hammer with Undead Slayer on it for you
			Purge : Cleanses Poison. Better than Cure
			Restoration : Resurrection. Brings the target back with 100% HP/Mana
			Sacred Boon : A HoT, heal over time spell, that heals 10-15 every few seconds
			Sacrifice : Heals your party members when you take damage. Sort of like thorns, but it heals instead of hurts
			Smite : Causes energy damage
			Touch of Life : Heals even if Mortal Strike or poison are active on the target
			Trial by Fire : Attackers receive damage when they strike you, sort of like a temporary RPD buff
		target: UInt32 or Mobile or None
		wait: bool or None
		
		"""

	@staticmethod
	def CastLastSpell(target: Union["UInt32", "Mobile", bool], wait: Union[bool, None]):
		"""Cast again the last casted spell, on last target.
		
		
		Parameters
		----------
		target: UInt32 or Mobile or bool
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastLastSpellLastTarget():
		"""Cast again the last casted spell, on last target.
		
		"""

	@staticmethod
	def CastMagery(SpellName: str, mobile: Union["Mobile", "UInt32", None], wait: Union[bool, None]):
		"""
		Cast a Magery spell using the spell name.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		Parameters
		----------
		SpellName: str
			Clumsy
			Create Food
			Feeblemind
			Heal
			Magic Arrow
			Night Sight
			Reactive Armor
			Weaken
			Agility
			Cunning
			Cure
			Harm
			Magic Trap
			Magic Untrap
			Protection
			Strength
			Bless
			Fireball
			Magic Lock
			Poison
			Telekinesis
			Teleport
			Unlock
			Wall of Stone
			Arch Cure
			Arch Protection
			Curse
			Fire Field
			Greater Heal
			Lightning
			Mana Drain
			Recall
			Blade Spirits
			Dispel Field
			Incognito
			Magic Reflection
			Mind Blast
			Paralyze
			Poison Field
			Summon Creature
			Dispel
			Energy Bolt
			Explosion
			Invisibility
			Mark
			Mass Curse
			Paralyze Field
			Reveal
			Chain Lightning
			Energy Field
			Flamestrike
			Gate Travel
			Mana Vampire
			Mass Dispel
			Meteor Swarm
			Polymorph
			Earthquake
			Energy Vortex
			Resurrection
			Summon Air Elemental
			Summon Daemon
			Summon Earth Elemental
			Summon Fire Elemental
			Summon Water Elemental
		mobile: Mobile or UInt32 or None
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastMastery(SpellName: str, target: Union["UInt32", "Mobile", None], wait: Union[bool, None]):
		"""Cast a Mastery spell using the spell name.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		
		Parameters
		----------
		SpellName: str
			Inspire
			Invigorate
			Resilience
			Perseverance
			Tribulation
			Despair
			Death Ray
			Ethereal Blast
			Nether Blast
			Mystic Weapon
			Command Undead
			Conduit
			Mana Shield
			Summon Reaper
			Enchanted Summoning
			Anticipate Hit
			Warcry
			Intuition
			Rejuvenate
			Holy Fist
			Shadow
			White Tiger Form
			Flaming Shot
			Playing The Odds
			Thrust
			Pierce
			Stagger
			Toughness
			Onslaught
			Focused Eye
			Elemental Fury
			Called Shot
			Saving Throw
			Shield Bash
			Bodyguard
			Heighten Senses
			Tolerance
			Injected Strike
			Potency
			Rampage
			Fists Of Fury
			Knockout
			Whispering
			Combat Training
			Boarding
		target: UInt32 or Mobile or None
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastMysticism(SpellName: str, mobile: Union["Mobile", "UInt32", None], wait: Union[bool, None]):
		"""
		Cast a Mysticism spell using the spell name.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		Parameters
		----------
		SpellName: str
			Animated Weapon
			Healing Stone
			Purge
			Enchant
			Sleep
			Eagle Strike
			Stone Form
			SpellTrigger
			Mass Sleep
			Cleansing Winds
			Bombard
			Spell Plague
			Hail Storm
			Nether Cyclone
			Rising Colossus
		mobile: Mobile or UInt32 or None
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastNecro(SpellName: str, mobile: Union["Mobile", "UInt32", None], wait: Union[bool, None]):
		"""
		Cast a Necromany spell using the spell name.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		Parameters
		----------
		SpellName: str
			Curse Weapon
			Pain Spike
			Corpse Skin
			Evil Omen
			Blood Oath
			Wraith Form
			Mind Rot
			Summon Familiar
			Horrific Beast
			Animate Dead
			Poison Strike
			Wither
			Strangle
			Lich Form
			Exorcism
			Vengeful Spirit
			Vampiric Embrace
		mobile: Mobile or UInt32 or None
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastNinjitsu(SpellName: str, target: Union["UInt32", "Mobile", None], wait: Union[bool, None]):
		"""Cast a Ninjitsu spell using the spell name.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		
		Parameters
		----------
		SpellName: str
			Animal Form
			Backstab
			Surprise Attack
			Mirror Image
			Shadow jump
			Focus Attack
			Ki Attack
		target: UInt32 or Mobile or None
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def CastSpellweaving(SpellName: str, target: Union["UInt32", "Mobile", None], wait: Union[bool, None]):
		"""
		Cast a Spellweaving spell using the spell name.
		Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
		NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.
		
		Parameters
		----------
		SpellName: str
			Arcane Circle
			Gift Of Renewal
			Immolating Weapon
			Attune Weapon
			Thunderstorm
			Natures Fury
			Summon Fey
			Summoniend
			Reaper Form
			Wildfire
			Essence Of Wind
			Dryad Allure
			Ethereal Voyage
			Word Of Death
			Gift Of Life
			Arcane Empowerment
		target: UInt32 or Mobile or None
			Optional: Serial or Mobile to target (default: null)
		wait: bool or None
			Optional: Wait server to confirm. (default: True)
		
		"""

	@staticmethod
	def Interrupt():
		"""Interrupt the casting of a spell by performing an equip/unequip.
		
		"""


class Statics:
	"""	
	<summary>
	The Statics class provides access to informations about the Map, down to the individual tile.
	When using this function it's important to remember the distinction between Land and Tile:
	Land
	----
	For a given (X,Y,map) there can be only 1 (0 zero) Land item, and has 1 specific Z coordinate.
	
	Tile
	----
	For a given (X,Y,map) there can be any number of Tile items.
	</summary>
		
	"""

	@staticmethod
	def CheckDeedHouse(x: int, y: int) -> bool:
		"""Check if the given Tile is occupied by a private house.
		Need to be in-sight, on most servers the maximum distance is 18 tiles.
		
		Parameters
		----------
		x: int
			X coordinate.
		y: int
			Y coordinate.
		
		Returns
		-------
		bool
			True: The tile is occupied - False: otherwise
		
		"""

	@staticmethod
	def GetLandFlag(itemid: int, flagname: str) -> bool:
		"""Land: Check Flag value of a given Land item.
		
		Parameters
		----------
		itemid: int
		flagname: str
			None
			Translucent
			Wall
			Damaging
			Impassable
			Surface
			Bridge
			Window
			NoShoot
			Foliage
			HoverOver
			Roof
			Door
			Wet
		
		Returns
		-------
		bool
			True: if the Flag is active - False: otherwise
		
		"""

	@staticmethod
	def GetLandID(x: int, y: int, map: int) -> int:
		"""Land: Return the StaticID of the Land item, give the coordinates and map.
		
		Parameters
		----------
		x: int
			X coordinate.
		y: int
			Y coordinate.
		map: int
			0 = Felucca
			1 = Trammel
			2 = Ilshenar
			3 = Malas
			4 = Tokuno
			5 = TerMur
		
		Returns
		-------
		int
			Return the StaticID of the Land tile
		
		"""

	@staticmethod
	def GetLandName(StaticID: int) -> str:
		"""Land: Get the name of a Land item given the StaticID.
		
		Parameters
		----------
		StaticID: int
			Land item StaticID.
		
		Returns
		-------
		str
			The name of the Land item.
		
		"""

	@staticmethod
	def GetLandZ(x: int, y: int, map: int) -> int:
		"""Land: Return the Z coordinate (height) of the Land item, give the coordinates and map.
		
		Parameters
		----------
		x: int
			X coordinate.
		y: int
			Y coordinate.
		map: int
			0 = Felucca
			1 = Trammel
			2 = Ilshenar
			3 = Malas
			4 = Tokuno
			5 = TerMur
		
		Returns
		-------
		int
		
		"""

	@staticmethod
	def GetStaticsLandInfo(x: int, y: int, map: int) -> "Statics.TileInfo":
		"""Land: Return a TileInfo representing the Land item for a given X,Y, map.
		
		Parameters
		----------
		x: int
			X coordinate.
		y: int
			Y coordinate.
		map: int
			0 = Felucca
			1 = Trammel
			2 = Ilshenar
			3 = Malas
			4 = Tokuno
			5 = TerMur
		
		Returns
		-------
		Statics.TileInfo
			A single TileInfo related a Land item.
		
		"""

	@staticmethod
	def GetStaticsTileInfo(x: int, y: int, map: int) -> "List[Statics.TileInfo]":
		"""Tile: Return a list of TileInfo representing the Tile items for a given X,Y, map.
		
		Parameters
		----------
		x: int
			X coordinate.
		y: int
			Y coordinate.
		map: int
			0 = Felucca
			1 = Trammel
			2 = Ilshenar
			3 = Malas
			4 = Tokuno
			5 = TerMur
		
		Returns
		-------
		List[Statics.TileInfo]
			A list of TileInfo related to Tile items.
		
		"""

	@staticmethod
	def GetTileFlag(StaticID: int, flagname: str) -> bool:
		"""Tile: Check Flag value of a given Tile item.
		
		Parameters
		----------
		StaticID: int
			StaticID of a Tile item.
		flagname: str
			None
			Translucent
			Wall
			Damaging
			Impassable
			Surface
			Bridge
			Window
			NoShoot
			Foliage
			HoverOver
			Roof
			Door
			Wet
		
		Returns
		-------
		bool
			True: if the Flag is active - False: otherwise
		
		"""

	@staticmethod
	def GetTileHeight(StaticID: int) -> int:
		"""Tile: Get hight of a Tile item, in Z coordinate reference.
		
		Parameters
		----------
		StaticID: int
			Tile item StaticID.
		
		Returns
		-------
		int
			Height of a Tile item.
		
		"""

	@staticmethod
	def GetTileName(StaticID: int) -> str:
		"""Tile: Get the name of a Tile item given the StaticID.
		
		Parameters
		----------
		StaticID: int
			Tile item StaticID.
		
		Returns
		-------
		str
			The name of the Land item.
		
		"""


	class TileInfo:
		"""		
		<summary>
		The TileInfo class hold the values represeting Tile or Land items for a given X,Y coordinate.
		</summary>
				
		"""
		@property
		def StaticHue(self) -> int: return int() 
		
		@StaticHue.setter
		def StaticHue(self, StaticHue: int): pass

		@property
		def StaticID(self) -> int: return int() 
		
		@StaticID.setter
		def StaticID(self, StaticID: int): pass

		@property
		def StaticZ(self) -> int: return int() 
		
		@StaticZ.setter
		def StaticZ(self, StaticZ: int): pass



class Target:
	"""	
	<summary>
	The Target class provides various method for targeting Land, Items and Mobiles in game.
	</summary>
		
	"""

	@staticmethod
	def AttackTargetFromList(target_name: str):
		"""Attack Target from gui filter selector, in Targetting tab.
		
		Parameters
		----------
		target_name: str
		
		"""

	@staticmethod
	def Cancel():
		"""Cancel the current target.
		
		"""

	@staticmethod
	def ClearLast():
		"""Clear the last target.
		
		"""

	@staticmethod
	def ClearLastandQueue():
		"""Clear last target and target queue.
		
		"""

	@staticmethod
	def ClearQueue():
		"""Clear Queue Target.
		
		"""

	@staticmethod
	def GetLast() -> int:
		"""Get serial number of last target
		
		Returns
		-------
		int
			Serial as number.
		
		"""

	@staticmethod
	def GetLastAttack() -> int:
		"""Get serial number of last attack target
		
		Returns
		-------
		int
			Serial as number.
		
		"""

	@staticmethod
	def GetTargetFromList(target_name: str) -> "Mobile":
		"""Get Mobile object from GUI filter selector, in Targetting tab.
		
		Parameters
		----------
		target_name: str
			Name of the target filter.
		
		Returns
		-------
		Mobile
			Mobile object matching. None: not found
		
		"""

	@staticmethod
	def HasTarget() -> bool:
		"""Get status if have in-game cursor has target shape.
		
		Returns
		-------
		bool
			True: Cursor has target - False: otherwise
		
		"""

	@staticmethod
	def Last():
		"""Execute the target on the last Item or Mobile targeted.
		
		"""

	@staticmethod
	def LastQueued():
		"""Enqueue the next target on the last Item or Mobile targeted.
		
		"""

	@staticmethod
	def PerformTargetFromList(target_name: str):
		"""Execute Target from GUI filter selector, in Targetting tab.
		
		Parameters
		----------
		target_name: str
			Name of the target filter.
		
		"""

	def PromptGroundTarget(self, message: str, color: int) -> "Point3D":
		"""Prompt a target in-game, wait for the Player to select the ground. Can also specific a text message for prompt.
		
		Parameters
		----------
		message: str
			Hint on what to select.
		color: int
			Color of the message. (default: 945, gray)
		
		Returns
		-------
		Point3D
			A Point3D object, containing the X,Y,Z coordinate
		
		"""

	def PromptTarget(self, message: str, color: int) -> int:
		"""Prompt a target in-game, wait for the Player to select an Item or a Mobile. Can also specific a text message for prompt.
		
		Parameters
		----------
		message: str
			Hint on what to select.
		color: int
			Color of the message. (default: 945, gray)
		
		Returns
		-------
		int
			Serial of the selected object.
		
		"""

	@staticmethod
	def Self():
		"""Execute the target on the Player.
		
		"""

	@staticmethod
	def SelfQueued():
		"""Enqueue the next target on the Player.
		
		"""

	@staticmethod
	def SetLast(serial: Union[int, "Mobile"], wait: Union[bool, None]):
		"""Set the last target to specific mobile, using the serial.
		
		
		Parameters
		----------
		serial: int or Mobile
			Serial of the Mobile.
		wait: bool or None
			Wait confirmation from the server.
		
		"""

	@staticmethod
	def SetLastTargetFromList(target_name: str):
		"""Set Last Target from GUI filter selector, in Targetting tab.
		
		Parameters
		----------
		target_name: str
			Name of the target filter.
		
		"""

	@staticmethod
	def TargetExecute(x: Union[int, "Item", "Mobile"], y: Union[int, None], z: Union[int, None], StaticID: Union[int, None]):
		"""Execute target on specific serial, item, mobile, X Y Z point.
		
		
		Parameters
		----------
		x: int or Item or Mobile
			X coordinate.
			
			Item object to Target.
			Serial of the Target
			Mobile object to Target.
		y: int or None
			Y coordinate.
		z: int or None
			Z coordinate.
		StaticID: int or None
			ID of Land/Tile
		
		"""

	@staticmethod
	def TargetExecuteRelative(serial: Union[int, "Mobile"], offset: int):
		"""
		Execute target on specific land point with offset distance from Mobile. Distance is calculated by target Mobile.Direction.
		
		Parameters
		----------
		serial: int or Mobile
			Serial of the mobile
			Mobile object to target.
		offset: int
			Distance from the target.
		
		"""

	@staticmethod
	def TargetResource(item_serial: Union[int, "Item"], resource_number: Union[int, str]):
		"""Find and target a resource using the specified item.
		
		
		Parameters
		----------
		item_serial: int or Item
			Item object to use.
		resource_number: int or str
			Resource as standard name or custom number
			0: ore
			1: sand
			2: wood
			3: graves
			4: red_mushrooms
			n: custom
		
		"""

	@staticmethod
	def WaitForTarget(delay: int, noshow: bool) -> bool:
		"""Wait for the cursor to show the target, pause the script for a maximum amount of time. and optional flag True or False. True Not show cursor, false show it
		
		Parameters
		----------
		delay: int
			Maximum amount to wait, in milliseconds
		noshow: bool
			Pevent the cursor to display the target.
		
		Returns
		-------
		bool
		
		"""


class Tile:
	"""	
	<summary>
	Class representing an (X,Y) coordinate. Optimized for pathfinding tasks.
	</summary>
		
	"""
	@property
	def X(self) -> int: 
		"""Coordinate X."""
		return int() 
	
	@X.setter
	def X(self, X: int): pass

	@property
	def Y(self) -> int: 
		"""Coordinate Y."""
		return int() 
	
	@Y.setter
	def Y(self, Y: int): pass

	def Equals(self, obj: object) -> bool:
		"""
		
		Parameters
		----------
		obj: object
		
		Returns
		-------
		bool
		
		"""

	def GetHashCode(self) -> int:
		"""
		
		Returns
		-------
		int
		
		"""

	def ToString(self) -> str:
		"""
		
		Returns
		-------
		str
		
		"""


class Timer:
	"""	
	<summary>
	Timer are normally used to display messages after a certain period of time. 
	They are also often used to keep track of the maximum amount of time for an action to complete.
	</summary>
		
	"""

	@staticmethod
	def Check(name: str) -> bool:
		"""Check if a timer object is expired or not.
		
		Parameters
		----------
		name: str
		
		Returns
		-------
		bool
			true if not expired, false if expired
		
		"""

	@staticmethod
	def Create(name: str, delay: int, message: Union[str, None]):
		"""Create a timer with the provided name that will expire in ms_timer time (in milliseconds)
		
		
		Parameters
		----------
		name: str
			Timer name.
		delay: int
			Delay in milliseconds.
		message: str or None
			Message displayed at timeouit.
		
		"""

	@staticmethod
	def Remaining(name: str) -> int:
		"""Get remaining time for a named timer
		
		Parameters
		----------
		name: str
			Timer name
		
		Returns
		-------
		int
			Returns the milliseconds remaining for a timer.
		
		"""


class Vendor:
	"""	
	<summary>
	@nodoc
	@experimental
	The Vendor class allow you to read the list items purchased last.
	</summary>
		
	"""

	@staticmethod
	def BuyList(vendorSerial: int) -> "List[Vendor.BuyItem]":
		"""Get the list of items purchased in the last trade, with a specific Vendor.
		
		Parameters
		----------
		vendorSerial: int
			Serial of the Vendor (default: -1 - most recent trade)
		
		Returns
		-------
		List[Vendor.BuyItem]
			A list of BuyItem
		
		"""


	class BuyItem:
		"""		
		<summary>
		The BuyItem class store informations about a recently purchased item.
		</summary>
				
		"""
		@property
		def Amount(self) -> int: return int() 
		
		@Amount.setter
		def Amount(self, Amount: int): pass

		@property
		def ItemID(self) -> int: return int() 
		
		@ItemID.setter
		def ItemID(self, ItemID: int): pass

		@property
		def Name(self) -> str: return str() 
		
		@Name.setter
		def Name(self, Name: str): pass

		@property
		def Price(self) -> int: return int() 
		
		@Price.setter
		def Price(self, Price: int): pass

		@property
		def Serial(self) -> int: return int() 
		
		@Serial.setter
		def Serial(self, Serial: int): pass


