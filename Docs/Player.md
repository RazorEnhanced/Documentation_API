# Player    

## Properties  
## Player.AR
## Player.Backpack
## Player.Bank
## Player.Body
## Player.Buffs
## Player.ColdResistance
## Player.DamageChanceIncrease
## Player.DefenseChanceIncrease
## Player.Dex
## Player.DexterityIncrease
## Player.Direction
## Player.EnergyResistance
## Player.EnhancePotions
## Player.FasterCasting
## Player.FasterCastRecovery
## Player.Female
## Player.FireResistance
## Player.Followers
## Player.FollowersMax
## Player.Gold
## Player.HasSpecial
## Player.HitPointsIncrease
## Player.HitPointsRegeneration
## Player.Hits
## Player.HitsMax
## Player.InParty
## Player.Int
## Player.IntelligenceIncrease
## Player.IsGhost
## Player.LowerManaCost
## Player.LowerReagentCost
## Player.Luck
## Player.Mana
## Player.ManaIncrease
## Player.ManaMax
## Player.ManaRegeneration
## Player.Map
## Player.MaximumHitPointsIncrease
## Player.MaximumManaIncrease
## Player.MaximumStaminaIncrease
## Player.MaxWeight
## Player.MobileID
## Player.Mount
## Player.Name
## Player.Notoriety
## Player.Paralized
## Player.Poisoned
## Player.PoisonResistance
## Player.Position
## Player.Quiver
## Player.ReflectPhysicalDamage
## Player.Serial
## Player.SpellDamageIncrease
## Player.Stam
## Player.StaminaIncrease
## Player.StaminaRegeneration
## Player.StamMax
## Player.StatCap
## Player.StaticMount
## Player.Str
## Player.StrengthIncrease
## Player.SwingSpeedIncrease
## Player.Visible
## Player.WarMode
## Player.Weight
## Player.YellowHits 
## Methods  
### Player.Attack
``` python
Player.Attack(Mobile m)
  Mobile m #
```
### Player.Attack
``` python
Player.Attack(Int32 serial)
  Int32 serial #
```
### Player.AttackLast
``` python
Player.AttackLast()

```
### Player.BuffsExist
``` python
Player.BuffsExist(String buffname)
  String buffname #
```
### Player.ChatAlliance
``` python
Player.ChatAlliance(String msg)
  String msg #
```
### Player.ChatAlliance
``` python
Player.ChatAlliance(Int32 num)
  Int32 num #
```
### Player.ChatChannel
``` python
Player.ChatChannel(Int32 num)
  Int32 num #
```
### Player.ChatChannel
``` python
Player.ChatChannel(String msg)
  String msg #
```
### Player.ChatEmote
``` python
Player.ChatEmote(Int32 hue, Int32 num)
  Int32 hue #
  Int32 num #
```
### Player.ChatEmote
``` python
Player.ChatEmote(Int32 hue, String msg)
  Int32 hue #
  String msg #
```
### Player.ChatGuild
``` python
Player.ChatGuild(String msg)
  String msg #
```
### Player.ChatGuild
``` python
Player.ChatGuild(Int32 num)
  Int32 num #
```
### Player.ChatParty
``` python
Player.ChatParty(String msg, Int32 serial)
  String msg #
  Int32 serial #0
```
### Player.ChatSay
``` python
Player.ChatSay(Int32 hue, String msg)
  Int32 hue #
  String msg #
```
### Player.ChatSay
``` python
Player.ChatSay(Int32 hue, Int32 num)
  Int32 hue #
  Int32 num #
```
### Player.ChatWhisper
``` python
Player.ChatWhisper(Int32 hue, Int32 num)
  Int32 hue #
  Int32 num #
```
### Player.ChatWhisper
``` python
Player.ChatWhisper(Int32 hue, String msg)
  Int32 hue #
  String msg #
```
### Player.ChatYell
``` python
Player.ChatYell(Int32 hue, Int32 num)
  Int32 hue #
  Int32 num #
```
### Player.ChatYell
``` python
Player.ChatYell(Int32 hue, String msg)
  Int32 hue #
  String msg #
```
### Player.CheckLayer
``` python
Player.CheckLayer(String layer)
  String layer #
```
### Player.DistanceTo
``` python
Player.DistanceTo(Item i)
  Item i #
```
### Player.DistanceTo
``` python
Player.DistanceTo(Mobile m)
  Mobile m #
```
### Player.Equals
``` python
Player.Equals(Object obj)
  Object obj #
```
### Player.EquipItem
``` python
Player.EquipItem(Int32 serial)
  Int32 serial #
```
### Player.EquipItem
``` python
Player.EquipItem(Item item)
  Item item #
```
### Player.EquipUO3D
``` python
Player.EquipUO3D(List`1 serials)
  List`1 serials #
```
### Player.Fly
``` python
Player.Fly(Boolean on)
  Boolean on #
```
### Player.GetHashCode
``` python
Player.GetHashCode()

```
### Player.GetItemOnLayer
``` python
Player.GetItemOnLayer(String layer)
  String layer #
```
### Player.GetPropStringByIndex
``` python
Player.GetPropStringByIndex(Int32 index)
  Int32 index #
```
### Player.GetPropStringList
``` python
Player.GetPropStringList()

```
### Player.GetPropValue
``` python
Player.GetPropValue(String name)
  String name #
```
### Player.GetRealSkillValue
``` python
Player.GetRealSkillValue(String skillname)
  String skillname #
```
### Player.GetSkillCap
``` python
Player.GetSkillCap(String skillname)
  String skillname #
```
### Player.GetSkillStatus
``` python
Player.GetSkillStatus(String skillname)
  String skillname #
```
### Player.GetSkillValue
``` python
Player.GetSkillValue(String skillname)
  String skillname #
```
### Player.GetStatStatus
``` python
Player.GetStatStatus(String statname)
  String statname #
```
### Player.GetType
``` python
Player.GetType()

```
### Player.GuildButton
``` python
Player.GuildButton()

```
### Player.HeadMessage
``` python
Player.HeadMessage(Int32 hue, Int32 num)
  Int32 hue #
  Int32 num #
```
### Player.HeadMessage
``` python
Player.HeadMessage(Int32 hue, String message)
  Int32 hue #
  String message #
```
### Player.InRangeItem
``` python
Player.InRangeItem(Int32 itemserial, Int32 range)
  Int32 itemserial #
  Int32 range #
```
### Player.InRangeItem
``` python
Player.InRangeItem(Item i, Int32 range)
  Item i #
  Int32 range #
```
### Player.InRangeMobile
``` python
Player.InRangeMobile(Mobile mob, Int32 range)
  Mobile mob #
  Int32 range #
```
### Player.InRangeMobile
``` python
Player.InRangeMobile(Int32 mobserial, Int32 range)
  Int32 mobserial #
  Int32 range #
```
### Player.InvokeVirtue
``` python
Player.InvokeVirtue(String virtue)
  String virtue #
```
### Player.KickMember
``` python
Player.KickMember(Int32 serial)
  Int32 serial #
```
### Player.LeaveParty
``` python
Player.LeaveParty()

```
### Player.MapSay
``` python
Player.MapSay(String msg)
  String msg #
```
### Player.MapSay
``` python
Player.MapSay(Int32 num)
  Int32 num #
```
### Player.PartyAccept
``` python
Player.PartyAccept(Int32 serial)
  Int32 serial #0
```
### Player.PartyCanLoot
``` python
Player.PartyCanLoot(Boolean CanLoot)
  Boolean CanLoot #
```
### Player.PartyInvite
``` python
Player.PartyInvite()

```
### Player.PathFindTo
``` python
Player.PathFindTo(Int32 x, Int32 y, Int32 z)
  Int32 x #
  Int32 y #
  Int32 z #
```
### Player.PathFindTo
``` python
Player.PathFindTo(Point3D Location)
  Point3D Location #
```
### Player.QuestButton
``` python
Player.QuestButton()

```
### Player.Run
``` python
Player.Run(String direction, Boolean checkPosition)
  String direction #
  Boolean checkPosition #True
```
### Player.SetSkillStatus
``` python
Player.SetSkillStatus(String skillname, Int32 status)
  String skillname #
  Int32 status #
```
### Player.SetStatStatus
``` python
Player.SetStatStatus(String statname, Int32 status)
  String statname #
  Int32 status #
```
### Player.SetWarMode
``` python
Player.SetWarMode(Boolean warflag)
  Boolean warflag #
```
### Player.SpellIsEnabled
``` python
Player.SpellIsEnabled(String spell)
  String spell #
```
### Player.SumAttribute
``` python
Player.SumAttribute(String attributename)
  String attributename #
```
### Player.ToggleAlwaysRun
``` python
Player.ToggleAlwaysRun()

```
### Player.ToString
``` python
Player.ToString()

```
### Player.UnEquipItemByLayer
``` python
Player.UnEquipItemByLayer(String layer, Boolean wait)
  String layer #
  Boolean wait #True
```
### Player.UseSkill
``` python
Player.UseSkill(String skillname, Boolean wait)
  String skillname #
  Boolean wait #
```
### Player.UseSkill
``` python
Player.UseSkill(String skillname)
  String skillname #
```
### Player.UseSkill
``` python
Player.UseSkill(String skillname, Int32 targetSerial, Boolean wait)
  String skillname #
  Int32 targetSerial #
  Boolean wait #True
```
### Player.UseSkill
``` python
Player.UseSkill(String skillname, EnhancedEntity target, Boolean wait)
  String skillname #
  EnhancedEntity target #
  Boolean wait #True
```
//////
### Player.UseSkillOnly
``` python
Player.UseSkillOnly(String skillname, Boolean wait)
  String skillname #
  Boolean wait #
```
### Player.Walk
``` python
Player.Walk(String direction, Boolean checkPosition)
  String direction #
  Boolean checkPosition #True
```
### Player.WeaponClearSA
``` python
Player.WeaponClearSA()

```
### Player.WeaponDisarmSA
``` python
Player.WeaponDisarmSA()

```
### Player.WeaponPrimarySA
``` python
Player.WeaponPrimarySA()

```
### Player.WeaponSecondarySA
``` python
Player.WeaponSecondarySA()

```
### Player.WeaponStunSA
``` python
Player.WeaponStunSA()

```