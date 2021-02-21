# Player    

## Properties  
### Player.AR __Int32__
### Player.Backpack __Item__
### Player.Bank __Item__
### Player.Body __Int32__
### Player.Buffs __List`1__
### Player.ColdResistance __Int32__
### Player.DamageChanceIncrease __Int32__
### Player.DefenseChanceIncrease __Int32__
### Player.Dex __Int32__
### Player.DexterityIncrease __Int32__
### Player.Direction __String__
### Player.EnergyResistance __Int32__
### Player.EnhancePotions __Int32__
### Player.FasterCasting __Int32__
### Player.FasterCastRecovery __Int32__
### Player.Female __Boolean__
### Player.FireResistance __Int32__
### Player.Followers __Int32__
### Player.FollowersMax __Int32__
### Player.Gold __Int32__
### Player.HasSpecial __Boolean__
### Player.HitPointsIncrease __Int32__
### Player.HitPointsRegeneration __Int32__
### Player.Hits __Int32__
### Player.HitsMax __Int32__
### Player.InParty __Boolean__
### Player.Int __Int32__
### Player.IntelligenceIncrease __Int32__
### Player.IsGhost __Boolean__
### Player.LowerManaCost __Int32__
### Player.LowerReagentCost __Int32__
### Player.Luck __Int32__
### Player.Mana __Int32__
### Player.ManaIncrease __Int32__
### Player.ManaMax __Int32__
### Player.ManaRegeneration __Int32__
### Player.Map __Int32__
### Player.MaximumHitPointsIncrease __Int32__
### Player.MaximumManaIncrease __Int32__
### Player.MaximumStaminaIncrease __Int32__
### Player.MaxWeight __Int32__
### Player.MobileID __Int32__
### Player.Mount __Item__
### Player.Name __String__
### Player.Notoriety __Byte__
### Player.Paralized __Boolean__
### Player.Poisoned __Boolean__
### Player.PoisonResistance __Int32__
### Player.Position __Point3D__
### Player.Quiver __Item__
### Player.ReflectPhysicalDamage __Int32__
### Player.Serial __Int32__
### Player.SpellDamageIncrease __Int32__
### Player.Stam __Int32__
### Player.StaminaIncrease __Int32__
### Player.StaminaRegeneration __Int32__
### Player.StamMax __Int32__
### Player.StatCap __Int32__
### Player.StaticMount __Int32__
### Player.Str __Int32__
### Player.StrengthIncrease __Int32__
### Player.SwingSpeedIncrease __Int32__
### Player.Visible __Boolean__
### Player.WarMode __Boolean__
### Player.Weight __Int32__
### Player.YellowHits __Boolean__ 
## Methods  
### Player.Attack
```
Attack(Mobile m) -> Void
```
- __Mobile__ **m**
### Player.Attack
```
Attack(Int32 serial) -> Void
```
- __Int32__ **serial**
### Player.AttackLast
```
AttackLast() -> Void
```
### Player.BuffsExist
```
BuffsExist(String buffname) -> Boolean
```
- __String__ **buffname**
### Player.ChatAlliance
```
ChatAlliance(String msg) -> Void
```
- __String__ **msg**
### Player.ChatAlliance
```
ChatAlliance(Int32 num) -> Void
```
- __Int32__ **num**
### Player.ChatChannel
```
ChatChannel(Int32 num) -> Void
```
- __Int32__ **num**
### Player.ChatChannel
```
ChatChannel(String msg) -> Void
```
- __String__ **msg**
### Player.ChatEmote
```
ChatEmote(Int32 hue, Int32 num) -> Void
```
- __Int32__ **hue** 
- __Int32__ **num**
### Player.ChatEmote
```
ChatEmote(Int32 hue, String msg) -> Void
```
- __Int32__ **hue** 
- __String__ **msg**
### Player.ChatGuild
```
ChatGuild(String msg) -> Void
```
- __String__ **msg**
### Player.ChatGuild
```
ChatGuild(Int32 num) -> Void
```
- __Int32__ **num**
### Player.ChatParty
```
ChatParty(String msg, Int32 serial) -> Void
```
- __String__ **msg** 
- __Int32__ **serial** 0
### Player.ChatSay
```
ChatSay(Int32 hue, String msg) -> Void
```
- __Int32__ **hue** 
- __String__ **msg**
### Player.ChatSay
```
ChatSay(Int32 hue, Int32 num) -> Void
```
- __Int32__ **hue** 
- __Int32__ **num**
### Player.ChatWhisper
```
ChatWhisper(Int32 hue, Int32 num) -> Void
```
- __Int32__ **hue** 
- __Int32__ **num**
### Player.ChatWhisper
```
ChatWhisper(Int32 hue, String msg) -> Void
```
- __Int32__ **hue** 
- __String__ **msg**
### Player.ChatYell
```
ChatYell(Int32 hue, Int32 num) -> Void
```
- __Int32__ **hue** 
- __Int32__ **num**
### Player.ChatYell
```
ChatYell(Int32 hue, String msg) -> Void
```
- __Int32__ **hue** 
- __String__ **msg**
### Player.CheckLayer
```
CheckLayer(String layer) -> Boolean
```
- __String__ **layer**
### Player.DistanceTo
```
DistanceTo(Item i) -> Int32
```
- __Item__ **i**
### Player.DistanceTo
```
DistanceTo(Mobile m) -> Int32
```
- __Mobile__ **m**
### Player.Equals
```
Equals(Object obj) -> Boolean
```
- __Object__ **obj**
### Player.EquipItem
```
EquipItem(Int32 serial) -> Void
```
- __Int32__ **serial**
### Player.EquipItem
```
EquipItem(Item item) -> Void
```
- __Item__ **item**
### Player.EquipUO3D
```
EquipUO3D(List`1 serials) -> Void
```
- __List`1__ **serials**
### Player.Fly
```
Fly(Boolean on) -> Void
```
- __Boolean__ **on**
### Player.GetHashCode
```
GetHashCode() -> Int32
```
### Player.GetItemOnLayer
```
GetItemOnLayer(String layer) -> Item
```
- __String__ **layer**
### Player.GetPropStringByIndex
```
GetPropStringByIndex(Int32 index) -> String
```
- __Int32__ **index**
### Player.GetPropStringList
```
GetPropStringList() -> List`1
```
### Player.GetPropValue
```
GetPropValue(String name) -> Int32
```
- __String__ **name**
### Player.GetRealSkillValue
```
GetRealSkillValue(String skillname) -> Double
```
- __String__ **skillname**
### Player.GetSkillCap
```
GetSkillCap(String skillname) -> Double
```
- __String__ **skillname**
### Player.GetSkillStatus
```
GetSkillStatus(String skillname) -> Int32
```
- __String__ **skillname**
### Player.GetSkillValue
```
GetSkillValue(String skillname) -> Double
```
- __String__ **skillname**
### Player.GetStatStatus
```
GetStatStatus(String statname) -> Int32
```
- __String__ **statname**
### Player.GetType
```
GetType() -> Type
```
### Player.GuildButton
```
GuildButton() -> Void
```
### Player.HeadMessage
```
HeadMessage(Int32 hue, Int32 num) -> Void
```
- __Int32__ **hue** 
- __Int32__ **num**
### Player.HeadMessage
```
HeadMessage(Int32 hue, String message) -> Void
```
- __Int32__ **hue** 
- __String__ **message**
### Player.InRangeItem
```
InRangeItem(Int32 itemserial, Int32 range) -> Boolean
```
- __Int32__ **itemserial** 
- __Int32__ **range**
### Player.InRangeItem
```
InRangeItem(Item i, Int32 range) -> Boolean
```
- __Item__ **i** 
- __Int32__ **range**
### Player.InRangeMobile
```
InRangeMobile(Mobile mob, Int32 range) -> Boolean
```
- __Mobile__ **mob** 
- __Int32__ **range**
### Player.InRangeMobile
```
InRangeMobile(Int32 mobserial, Int32 range) -> Boolean
```
- __Int32__ **mobserial** 
- __Int32__ **range**
### Player.InvokeVirtue
```
InvokeVirtue(String virtue) -> Void
```
- __String__ **virtue**
### Player.KickMember
```
KickMember(Int32 serial) -> Void
```
- __Int32__ **serial**
### Player.LeaveParty
```
LeaveParty() -> Void
```
### Player.MapSay
```
MapSay(String msg) -> Void
```
- __String__ **msg**
### Player.MapSay
```
MapSay(Int32 num) -> Void
```
- __Int32__ **num**
### Player.PartyAccept
```
PartyAccept(Int32 serial) -> Void
```
- __Int32__ **serial** 0
### Player.PartyCanLoot
```
PartyCanLoot(Boolean CanLoot) -> Void
```
- __Boolean__ **CanLoot**
### Player.PartyInvite
```
PartyInvite() -> Void
```
### Player.PathFindTo
```
PathFindTo(Int32 x, Int32 y, Int32 z) -> Void
```
- __Int32__ **x** 
- __Int32__ **y** 
- __Int32__ **z**
### Player.PathFindTo
```
PathFindTo(Point3D Location) -> Void
```
- __Point3D__ **Location**
### Player.QuestButton
```
QuestButton() -> Void
```
### Player.Run
```
Run(String direction, Boolean checkPosition) -> Boolean
```
- __String__ **direction** 
- __Boolean__ **checkPosition** True
### Player.SetSkillStatus
```
SetSkillStatus(String skillname, Int32 status) -> Void
```
- __String__ **skillname** 
- __Int32__ **status**
### Player.SetStatStatus
```
SetStatStatus(String statname, Int32 status) -> Void
```
- __String__ **statname** 
- __Int32__ **status**
### Player.SetWarMode
```
SetWarMode(Boolean warflag) -> Void
```
- __Boolean__ **warflag**
### Player.SpellIsEnabled
```
SpellIsEnabled(String spell) -> Boolean
```
- __String__ **spell**
### Player.SumAttribute
```
SumAttribute(String attributename) -> Single
```
- __String__ **attributename**
### Player.ToggleAlwaysRun
```
ToggleAlwaysRun() -> Void
```
### Player.ToString
```
ToString() -> String
```
### Player.UnEquipItemByLayer
```
UnEquipItemByLayer(String layer, Boolean wait) -> Void
```
- __String__ **layer** 
- __Boolean__ **wait** True
### Player.UseSkill
```
UseSkill(String skillname, Boolean wait) -> Void
```
- __String__ **skillname** 
- __Boolean__ **wait**
### Player.UseSkill
```
UseSkill(String skillname) -> Void
```
- __String__ **skillname**
### Player.UseSkill
```
UseSkill(String skillname, Int32 targetSerial, Boolean wait) -> Void
```
- __String__ **skillname** 
- __Int32__ **targetSerial** 
- __Boolean__ **wait** True
### Player.UseSkill
```
UseSkill(String skillname, EnhancedEntity target, Boolean wait) -> Void
```
- __String__ **skillname** 
- __EnhancedEntity__ **target** 
- __Boolean__ **wait** True
//////
### Player.UseSkillOnly
```
UseSkillOnly(String skillname, Boolean wait) -> Void
```
- __String__ **skillname** 
- __Boolean__ **wait**
### Player.Walk
```
Walk(String direction, Boolean checkPosition) -> Boolean
```
- __String__ **direction** 
- __Boolean__ **checkPosition** True
### Player.WeaponClearSA
```
WeaponClearSA() -> Void
```
### Player.WeaponDisarmSA
```
WeaponDisarmSA() -> Void
```
### Player.WeaponPrimarySA
```
WeaponPrimarySA() -> Void
```
### Player.WeaponSecondarySA
```
WeaponSecondarySA() -> Void
```
### Player.WeaponStunSA
```
WeaponStunSA() -> Void
```