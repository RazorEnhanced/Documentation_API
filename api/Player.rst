:mod:`Player`
========================================
.. py:module:: Player
   :synopsis: 
            <summary>
            The Player class represent the currently logged in character.
            </summary>
        


Properties
----------------
* Player.AR :mod:`Int32`
  Resistance to Phisical damage.

* Player.Backpack :mod:`Item`
  Player backpack, as Item object.

* Player.Bank :mod:`Item`
  Player bank chest, as Item object.

* Player.Body :mod:`Int32`
  Player Body or MobileID (see: Mobile.Body)

* Player.Buffs :mod:`List[String]`
  List of Player active buffs:
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

* Player.ColdResistance :mod:`Int32`
  Resistance to Cold damage.

* Player.DamageChanceIncrease :mod:`Int32`
  Get total Damage Chance Increase.

* Player.DefenseChanceIncrease :mod:`Int32`
  Get total Defense Chance Increase.

* Player.Dex :mod:`Int32`
  Stats value for Dexterity.

* Player.DexterityIncrease :mod:`Int32`
  Get total Dexterity Increase.

* Player.Direction :mod:`String`
  Player current direction, as text.

* Player.EnergyResistance :mod:`Int32`
  Resistance to Energy damage.

* Player.EnhancePotions :mod:`Int32`
  Get total Enhance Potions.

* Player.FasterCasting :mod:`Int32`
  Get total Faster Casting.

* Player.FasterCastRecovery :mod:`Int32`
  Get total Faster Cast Recovery.

* Player.Female :mod:`Boolean`
  Player is a female.

* Player.FireResistance :mod:`Int32`
  Resistance to Fire damage.

* Player.Followers :mod:`Int32`
  Player current amount of pet/followers.

* Player.FollowersMax :mod:`Int32`
  Player maximum amount of pet/followers.

* Player.Gold :mod:`Int32`
  Player total gold, in the backpack.

* Player.HasSpecial :mod:`Boolean`
  Player have a special abilities active.

* Player.HitPointsIncrease :mod:`Int32`
  Get total Hit Points Increase.

* Player.HitPointsRegeneration :mod:`Int32`
  Get total Hit Points Regeneration.

* Player.Hits :mod:`Int32`
  Current hit points.

* Player.HitsMax :mod:`Int32`
  Maximum hit points.

* Player.InParty :mod:`Boolean`
  Player is in praty.

* Player.Int :mod:`Int32`
  Stats value for Intelligence.

* Player.IntelligenceIncrease :mod:`Int32`
  Get total Intelligence Increase.

* Player.IsGhost :mod:`Boolean`
  Player is a Ghost

* Player.LowerManaCost :mod:`Int32`
  Get total Lower Mana Cost.

* Player.LowerReagentCost :mod:`Int32`
  Get total Lower Reagent Cost.

* Player.Luck :mod:`Int32`
  Player total luck.

* Player.Mana :mod:`Int32`
  Current mana.

* Player.ManaIncrease :mod:`Int32`
  Get total Mana Increase.

* Player.ManaMax :mod:`Int32`
  Maximum mana.

* Player.ManaRegeneration :mod:`Int32`
  Get total Mana Regeneration.

* Player.Map :mod:`Int32`
  Player current map, or facet.

* Player.MaximumHitPointsIncrease :mod:`Int32`
  Get total Maximum Hit Points Increase.

* Player.MaximumManaIncrease :mod:`Int32`
  Get total Maximum Mana Increase.

* Player.MaximumStaminaIncrease :mod:`Int32`
  Get total Maximum Stamina Increase.

* Player.MaxWeight :mod:`Int32`
  Player maximum weight.

* Player.MobileID :mod:`Int32`
  Player MobileID or Body (see: Mobile.MobileID)

* Player.Mount :mod:`Item`
  Player current Mount, as Item object.
NOTE: On some server the Serial return by this function doesn't match the mount serial.

* Player.Name :mod:`String`
  Player name.

* Player.Notoriety :mod:`Byte`
  Player notoriety
    1: blue, innocent
    2: green, friend
    3: gray, neutral
    4: gray, criminal
    5: orange, enemy
    6: red, hostile 
    6: yellow, invulnerable

* Player.Paralized :mod:`Boolean`
  Player is Paralized. True also while frozen because of casting of spells.

* Player.Poisoned :mod:`Boolean`
  Player is Poisoned

* Player.PoisonResistance :mod:`Int32`
  Resistance to Poison damage.

* Player.Position :mod:`Point3D`
  Current Player position as Point3D object.

* Player.Quiver :mod:`Item`
  Player quiver, as Item object.

* Player.ReflectPhysicalDamage :mod:`Int32`
  Get total Reflect Physical Damage.

* Player.Serial :mod:`Int32`
  Player unique Serial.

* Player.SpellDamageIncrease :mod:`Int32`
  Get total Spell Damage Increase.

* Player.Stam :mod:`Int32`
  Current stamina.

* Player.StaminaIncrease :mod:`Int32`
  Get total Stamina Increase.

* Player.StaminaRegeneration :mod:`Int32`
  Get total Stamina Regeneration.

* Player.StamMax :mod:`Int32`
  Maximum stamina.

* Player.StatCap :mod:`Int32`
  Get the stats cap.

* Player.StaticMount :mod:`Int32`
  Retrieves serial of mount set in Filter/Mount GUI.

* Player.Str :mod:`Int32`
  Stats value for Strenght.

* Player.StrengthIncrease :mod:`Int32`
  Get total Strength Increase.

* Player.SwingSpeedIncrease :mod:`Int32`
  Get total Swing Speed Increase.

* Player.Visible :mod:`Boolean`
  Player is visible, false if hidden.

* Player.WarMode :mod:`Boolean`
  Player has war mode active.

* Player.Weight :mod:`Int32`
  Player current weight.

* Player.YellowHits :mod:`Boolean`
  Player HP bar is not blue, but yellow.


Methods
--------------

.. py:function:: Player.Area() -> String





Get the name of the area in which the Player is currently in. (Ex: Britain, Destard, Vesper, Moongate, etc)
Regions are defined inside by Config/regions.json.

.. py:function:: Player.Attack(serial) -> Void


* serial: :mod:`Int32` Serial or Mobile to attack.


Attack a Mobile.

.. py:function:: Player.Attack(mobile) -> Void


* mobile: :mod:`Mobile` 




.. py:function:: Player.AttackLast() -> Void





Attack last target.

.. py:function:: Player.BuffsExist(buffname) -> Boolean


* buffname: :mod:`String` Meditation
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


Check if a buff is active, by buff name.

.. py:function:: Player.ChatAlliance(msg) -> Void


* msg: :mod:`Int32` 




.. py:function:: Player.ChatAlliance(msg) -> Void


* msg: :mod:`String` Message to send.


Send message to the alliace chat.

.. py:function:: Player.ChatChannel(msg) -> Void


* msg: :mod:`Int32` 




.. py:function:: Player.ChatChannel(msg) -> Void


* msg: :mod:`String` Message to send.


Send an chat channel message.

.. py:function:: Player.ChatEmote(color, msg) -> Void


* color: :mod:`Int32` Color of the text
* msg: :mod:`String` Message to send.


Send an emote in game.

.. py:function:: Player.ChatEmote(color, msg) -> Void


* color: :mod:`Int32` 
* msg: :mod:`Int32` 




.. py:function:: Player.ChatGuild(msg) -> Void


* msg: :mod:`Int32` 




.. py:function:: Player.ChatGuild(msg) -> Void


* msg: :mod:`String` Message to send.


Send message to the guild chat.

.. py:function:: Player.ChatParty(msg, recepient_serial) -> Void


* msg: :mod:`String` Text to send.
* recepient_serial: :mod:`Int32` Optional: Target of private message.


Send message in arty chat. If a recepient_serial is specified, the message is private.

.. py:function:: Player.ChatSay(color, msg) -> Void


* color: :mod:`Int32` Color of the text
* msg: :mod:`String` Message to send.


Send message in game.

.. py:function:: Player.ChatSay(color, msg) -> Void


* color: :mod:`Int32` 
* msg: :mod:`Int32` 




.. py:function:: Player.ChatWhisper(color, msg) -> Void


* color: :mod:`Int32` Color of the text
* msg: :mod:`String` Message to send.


Send an wishper message.

.. py:function:: Player.ChatWhisper(color, msg) -> Void


* color: :mod:`Int32` 
* msg: :mod:`Int32` 




.. py:function:: Player.ChatYell(color, msg) -> Void


* color: :mod:`Int32` 
* msg: :mod:`Int32` 




.. py:function:: Player.ChatYell(color, msg) -> Void


* color: :mod:`Int32` Color of the text
* msg: :mod:`String` Message to send.


Send an yell message.

.. py:function:: Player.CheckLayer(layer) -> Boolean


* layer: :mod:`String` Layers:
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


Check if a Layer is equipped by the Item.

.. py:function:: Player.DistanceTo(target) -> Int32


* target: :mod:`Mobile` The other Mobile or Item


Returns the distance between the Player and a Mobile or an Item.

.. py:function:: Player.DistanceTo(target) -> Int32


* target: :mod:`Item` 




.. py:function:: Player.EquipItem(item) -> Void


* item: :mod:`Item` 




.. py:function:: Player.EquipItem(serial) -> Void


* serial: :mod:`Int32` Serial or Item to equip.


Equip an Item

.. py:function:: Player.EquipUO3D(serials) -> Void


* serials: :mod:`List[Int32]` 




.. py:function:: Player.Fly(status) -> Void


* status: :mod:`Boolean` True: Gargoyle Fly ON - False: Gargoyle fly OFF


Enable or disable Gargoyle Flying.

.. py:function:: Player.GetItemOnLayer(layer) -> Item


* layer: :mod:`String` Layers:
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


Returns the Item associated with a Mobile Layer.

.. py:function:: Player.GetPropStringByIndex(index) -> String


* index: :mod:`Int32` Line number, start from 0.


Get a single line of Properties of the Player, from the tooltip, as text.

.. py:function:: Player.GetPropStringList() -> List[String]





Get the list of Properties of the Player, as list of lines of the tooltip.

.. py:function:: Player.GetPropValue(name) -> Int32


* name: :mod:`String` Name of the property.


Get the numeric value of a specific Player property, from the tooltip.

.. py:function:: Player.GetRealSkillValue(skillname) -> Double


* skillname: :mod:`String` Alchemy
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


Get the base/real value of the skill for the given the skill name.

.. py:function:: Player.GetSkillCap(skillname) -> Double


* skillname: :mod:`String` Alchemy
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


Get the skill cap for the given the skill name.

.. py:function:: Player.GetSkillStatus(skillname) -> Int32


* skillname: :mod:`String` Alchemy
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


Get lock status for a specific skill.

.. py:function:: Player.GetSkillValue(skillname) -> Double


* skillname: :mod:`String` Alchemy
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


Get the value of the skill, with modifiers, for the given the skill name.

.. py:function:: Player.GetStatStatus(statname) -> Int32


* statname: :mod:`String` Strength
Dexterity
Intelligence


Get lock status for a specific stats.

.. py:function:: Player.GuildButton() -> Void





Press the Guild menu button in the paperdoll.

.. py:function:: Player.HeadMessage(color, msg) -> Void


* color: :mod:`Int32` 
* msg: :mod:`Int32` 




.. py:function:: Player.HeadMessage(color, msg) -> Void


* color: :mod:`Int32` Color of the Text.
* msg: :mod:`String` Text of the message.


Display a message above the Player. Visible only by the Player.

.. py:function:: Player.InRangeItem(item, range) -> Boolean


* item: :mod:`Item` 
* range: :mod:`Int32` 




.. py:function:: Player.InRangeItem(item, range) -> Boolean


* item: :mod:`Int32` 
* range: :mod:`Int32` 




.. py:function:: Player.InRangeMobile(mobile, range) -> Boolean


* mobile: :mod:`Int32` 
* range: :mod:`Int32` 




.. py:function:: Player.InRangeMobile(mobile, range) -> Boolean


* mobile: :mod:`Mobile` 
* range: :mod:`Int32` 




.. py:function:: Player.InvokeVirtue(virtue) -> Void


* virtue: :mod:`String` Honor
Sacrifice
Valor
Compassion
Honesty
Humility
Justice


Invoke a virtue by name.

.. py:function:: Player.KickMember(serial) -> Void


* serial: :mod:`Int32` Serial of the Mobile to remove.


Kick a member from party by serial. Only for party leader

.. py:function:: Player.LeaveParty(force) -> Void


* force: :mod:`Boolean` True: Leave the party invite even you notin any party.


Leaves a party.

.. py:function:: Player.MapSay(msg) -> Void


* msg: :mod:`String` Message to send


Send message in the Map chat.

.. py:function:: Player.MapSay(msg) -> Void


* msg: :mod:`Int32` 




.. py:function:: Player.PartyAccept(from_serial, force) -> Boolean


* from_serial: :mod:`Int32` Optional: Serial to accept party from.( in case of multiple offers )
* force: :mod:`Boolean` True: Accept the party invite even you are already in a party.


Accept an incoming party offer. In case of multiple party oebnding invitation, from_serial is specified,

.. py:function:: Player.PartyCanLoot(CanLoot) -> Void


* CanLoot: :mod:`Boolean` 


Set the Party loot permissions.

.. py:function:: Player.PartyInvite() -> Void





Invite a person to a party. Prompt for a in-game Target.

.. py:function:: Player.PathFindTo(x, y, z) -> Void


* x: :mod:`Int32` X map coordinates or Point3D
* y: :mod:`Int32` Y map coordinates
* z: :mod:`Int32` Z map coordinates


Go to the given coordinates using Client-provided pathfinding.

.. py:function:: Player.PathFindTo(Location) -> Void


* Location: :mod:`Point3D` 




.. py:function:: Player.QuestButton() -> Void





Press the Quest menu button in the paperdoll.

.. py:function:: Player.Run(direction, checkPosition) -> Boolean


* direction: :mod:`String` North
South
East
West
Up
Down
Left
Right
* checkPosition: :mod:`Boolean` True: Wait until the server confirm the new Player.Position - False: Don't wait.


Run one step in the specified direction and wait for the confirmation of the new position by the server.
If the character is not facing the direction, the first step only "turn" the Player in the required direction.
Optional:
When checkPosition is True allow for slower but safe walking, the new position confirmed at each step via return value.
When checkPosition is Flase allow for faster walking/running, but requires custom delay and position checking.
Info:
Walking:  5 tiles/sec (~200ms between each step)
Running: 10 tiles/sec (~100ms between each step)

.. py:function:: Player.SetSkillStatus(skillname, status) -> Void


* skillname: :mod:`String` Alchemy
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
* status: :mod:`Int32` Lock status:
     0: Up     
     1: Down 
     2: Locked


Set lock status for a specific skill.

.. py:function:: Player.SetStatStatus(statname, status) -> Void


* statname: :mod:`String` 
* status: :mod:`Int32` Lock status:
     0: Up     
     1: Down 
     2: Locked


Set lock status for a specific skill.

.. py:function:: Player.SetWarMode(warflag) -> Void


* warflag: :mod:`Boolean` True: War - False: Peace


Set war Mode on on/off.

.. py:function:: Player.SpellIsEnabled(spellname) -> Boolean


* spellname: :mod:`String` Name of the spell.


Check if spell is active using the spell name (for spells that have this function).

.. py:function:: Player.SumAttribute(attributename) -> Single


* attributename: :mod:`String` Name of the property.


Scan all the equipped Item, returns the total value of a specific property. (ex: Lower Reagent Cost )
NOTE: This function is slow.

.. py:function:: Player.ToggleAlwaysRun() -> Void





Toggle on/off the awlays run flag. 
NOTE: Works only on OSI client.

.. py:function:: Player.UnEquipItemByLayer(layer, wait) -> Void


* layer: :mod:`String` Layers:
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
* wait: :mod:`Boolean` Wait for confirmation from the server.


Unequip the Item associated with a specific Layer.

.. py:function:: Player.UseSkill(skillname, target, wait) -> Void


* skillname: :mod:`String` 
* target: :mod:`Item` 
* wait: :mod:`Boolean` 




.. py:function:: Player.UseSkill(skillname, wait) -> Void


* skillname: :mod:`String` 
* wait: :mod:`Boolean` 




.. py:function:: Player.UseSkill(skillname, target, wait) -> Void


* skillname: :mod:`String` Alchemy
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
* target: :mod:`Int32` Optional: Serial, Mobile or Item to target. (default: null)
* wait: :mod:`Boolean` Optional: True: wait for confirmation from the server (default: False)


Use a specific skill, and optionally apply that skill to the target specified.

.. py:function:: Player.UseSkill(skillname, target, wait) -> Void


* skillname: :mod:`String` 
* target: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Player.UseSkill(skillname) -> Void


* skillname: :mod:`String` 




.. py:function:: Player.UseSkillOnly(skillname, wait) -> Void


* skillname: :mod:`String` 
* wait: :mod:`Boolean` 




.. py:function:: Player.Walk(direction, checkPosition) -> Boolean


* direction: :mod:`String` North
South
East
West
Up
Down
Left
Right
* checkPosition: :mod:`Boolean` True: Wait until the server confirm the new Player.Position - False: Don't wait.


Walk one step in the specified direction and wait for the confirmation of the new position by the server.
If the character is not facing the direction, the first step only "turn" the Player in the required direction.
Optional:
When checkPosition is True allow for slower but safe walking, the new position confirmed at each step via return value.
When checkPosition is Flase allow for faster walking/running, but requires custom delay and position checking.
Info:
Walking:  5 tiles/sec (~200ms between each step)
Running: 10 tiles/sec (~100ms between each step)

.. py:function:: Player.WeaponClearSA() -> Void





Disable any active Special Ability of the weapon.

.. py:function:: Player.WeaponDisarmSA() -> Void





Toggle Disarm Ability.

.. py:function:: Player.WeaponPrimarySA() -> Void





Toggle on/off the primary Special Ability of the weapon.

.. py:function:: Player.WeaponSecondarySA() -> Void





Toggle on/off the secondary Special Ability of the weapon.

.. py:function:: Player.WeaponStunSA() -> Void





Toggle Stun Ability.

.. py:function:: Player.Zone() -> String





Get the type of zone in which the Player is currently in.
Regions are defined inside by Config/regions.json.
