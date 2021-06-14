:mod:`Spells`
========================================
.. py:module:: Spells
   :synopsis: 
            <summary>
            The Spells class allow you to cast any spell and use abilities, via scripting.
            </summary>
        



Methods
--------------

.. py:function:: Spells.Cast(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.Cast(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.Cast(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Name of the spell to cast.
* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast spell using the spell name. See the skill-specific functions to get the full list of spell names.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.CastBushido(SpellName, wait) -> Void


* SpellName: :mod:`String` Honorable Execution
Confidence
Counter Attack
Lightning Strike
Evasion
Momentum Strike
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast a Bushido spell using the spell name.

.. py:function:: Spells.CastChivalry(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Curse Weapon
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
* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast a Chivalry spell using the spell name.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.CastChivalry(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastChivalry(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.CastCleric(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Bark Skin : Turns the druid's skin to bark, increasing physical, poison and energy resistence while reducing fire resistence.
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
* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast a Cleric spell using the spell name.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.CastCleric(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.CastCleric(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastDruid(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Angelic Faith : Turns you into an angel, boosting your stats. At 100 Spirit Speak you get +20 Str/Dex/Int. Every 5 points of SS = +1 point to each stat, at a max of +24. Will also boost your Anatomy, Mace Fighting and Healing, following the same formula.
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
* target: :mod:`UInt32` 
* wait: :mod:`Boolean` 


Cast a Druid spell using the spell name.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.CastDruid(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.CastDruid(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastLastSpell(target, wait) -> Void


* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast again the last casted spell, on last target.

.. py:function:: Spells.CastLastSpell(m, wait) -> Void


* m: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastLastSpell(wait) -> Void


* wait: :mod:`Boolean` 




.. py:function:: Spells.CastLastSpellLastTarget() -> Void





Cast again the last casted spell, on last target.

.. py:function:: Spells.CastMagery(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.CastMagery(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastMagery(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Clumsy
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
* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast a Magery spell using the spell name.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.CastMastery(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Inspire
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
* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast a Mastery spell using the spell name.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.CastMastery(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastMastery(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.CastMysticism(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastMysticism(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.CastMysticism(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Animated Weapon
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
* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast a Mysticism spell using the spell name.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.CastNecro(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastNecro(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.CastNecro(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Curse Weapon
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
* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast a Necromany spell using the spell name.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.CastNinjitsu(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.CastNinjitsu(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Animal Form
Backstab
Surprise Attack
Mirror Image
Shadow jump
Focus Attack
Ki Attack
* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast a Ninjitsu spell using the spell name.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.CastNinjitsu(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastSpellweaving(SpellName, mobile, wait) -> Void


* SpellName: :mod:`String` 
* mobile: :mod:`Mobile` 
* wait: :mod:`Boolean` 




.. py:function:: Spells.CastSpellweaving(SpellName) -> Void


* SpellName: :mod:`String` 




.. py:function:: Spells.CastSpellweaving(SpellName, target, wait) -> Void


* SpellName: :mod:`String` Arcane Circle
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
* target: :mod:`UInt32` Optional: Serial or Mobile to target (default: null)
* wait: :mod:`Boolean` Optional: Wait server to confirm. (default: True)


Cast a Spellweaving spell using the spell name.
Optionally is possible to specify the Mobile or a Serial as target of the spell. Upon successful casting, the target will be executed automatiaclly by the server.
NOTE: The "automatic" target is not supported by all shards, but you can restort to the Target class to handle it manually.

.. py:function:: Spells.Interrupt() -> Void





Interrupt the casting of a spell by performing an equip/unequip.
