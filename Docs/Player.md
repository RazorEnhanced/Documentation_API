# Player    

## Properties  
### Player.AR
### Player.Backpack
### Player.Bank
### Player.Body
### Player.Buffs
### Player.ColdResistance
### Player.DamageChanceIncrease
### Player.DefenseChanceIncrease
### Player.Dex
### Player.DexterityIncrease
### Player.Direction
### Player.EnergyResistance
### Player.EnhancePotions
### Player.FasterCasting
### Player.FasterCastRecovery
### Player.Female
### Player.FireResistance
### Player.Followers
### Player.FollowersMax
### Player.Gold
### Player.HasSpecial
### Player.HitPointsIncrease
### Player.HitPointsRegeneration
### Player.Hits
### Player.HitsMax
### Player.InParty
### Player.Int
### Player.IntelligenceIncrease
### Player.IsGhost
### Player.LowerManaCost
### Player.LowerReagentCost
### Player.Luck
### Player.Mana
### Player.ManaIncrease
### Player.ManaMax
### Player.ManaRegeneration
### Player.Map
### Player.MaximumHitPointsIncrease
### Player.MaximumManaIncrease
### Player.MaximumStaminaIncrease
### Player.MaxWeight
### Player.MobileID
### Player.Mount
### Player.Name
### Player.Notoriety
### Player.Paralized
### Player.Poisoned
### Player.PoisonResistance
### Player.Position
### Player.Quiver
### Player.ReflectPhysicalDamage
### Player.Serial
### Player.SpellDamageIncrease
### Player.Stam
### Player.StaminaIncrease
### Player.StaminaRegeneration
### Player.StamMax
### Player.StatCap
### Player.StaticMount
### Player.Str
### Player.StrengthIncrease
### Player.SwingSpeedIncrease
### Player.Visible
### Player.WarMode
### Player.Weight
### Player.YellowHits 
## Methods  
### Player.Attack
```py
Player.Attack(Mobile m)
- Mobile **m** ____```
### Player.Attack
```py
Player.Attack(Int32 serial)
- Int32 **serial** ____```
### Player.AttackLast
```py
Player.AttackLast()```
### Player.BuffsExist
```py
Player.BuffsExist(String buffname)
- String **buffname** ____```
### Player.ChatAlliance
```py
Player.ChatAlliance(String msg)
- String **msg** ____```
### Player.ChatAlliance
```py
Player.ChatAlliance(Int32 num)
- Int32 **num** ____```
### Player.ChatChannel
```py
Player.ChatChannel(Int32 num)
- Int32 **num** ____```
### Player.ChatChannel
```py
Player.ChatChannel(String msg)
- String **msg** ____```
### Player.ChatEmote
```py
Player.ChatEmote(Int32 hue, Int32 num)
- Int32 **hue** ____
- Int32 **num** ____```
### Player.ChatEmote
```py
Player.ChatEmote(Int32 hue, String msg)
- Int32 **hue** ____
- String **msg** ____```
### Player.ChatGuild
```py
Player.ChatGuild(String msg)
- String **msg** ____```
### Player.ChatGuild
```py
Player.ChatGuild(Int32 num)
- Int32 **num** ____```
### Player.ChatParty
```py
Player.ChatParty(String msg, Int32 serial)
- String **msg** ____
- Int32 **serial** __0__```
### Player.ChatSay
```py
Player.ChatSay(Int32 hue, String msg)
- Int32 **hue** ____
- String **msg** ____```
### Player.ChatSay
```py
Player.ChatSay(Int32 hue, Int32 num)
- Int32 **hue** ____
- Int32 **num** ____```
### Player.ChatWhisper
```py
Player.ChatWhisper(Int32 hue, Int32 num)
- Int32 **hue** ____
- Int32 **num** ____```
### Player.ChatWhisper
```py
Player.ChatWhisper(Int32 hue, String msg)
- Int32 **hue** ____
- String **msg** ____```
### Player.ChatYell
```py
Player.ChatYell(Int32 hue, Int32 num)
- Int32 **hue** ____
- Int32 **num** ____```
### Player.ChatYell
```py
Player.ChatYell(Int32 hue, String msg)
- Int32 **hue** ____
- String **msg** ____```
### Player.CheckLayer
```py
Player.CheckLayer(String layer)
- String **layer** ____```
### Player.DistanceTo
```py
Player.DistanceTo(Item i)
- Item **i** ____```
### Player.DistanceTo
```py
Player.DistanceTo(Mobile m)
- Mobile **m** ____```
### Player.Equals
```py
Player.Equals(Object obj)
- Object **obj** ____```
### Player.EquipItem
```py
Player.EquipItem(Int32 serial)
- Int32 **serial** ____```
### Player.EquipItem
```py
Player.EquipItem(Item item)
- Item **item** ____```
### Player.EquipUO3D
```py
Player.EquipUO3D(List`1 serials)
- List`1 **serials** ____```
### Player.Fly
```py
Player.Fly(Boolean on)
- Boolean **on** ____```
### Player.GetHashCode
```py
Player.GetHashCode()```
### Player.GetItemOnLayer
```py
Player.GetItemOnLayer(String layer)
- String **layer** ____```
### Player.GetPropStringByIndex
```py
Player.GetPropStringByIndex(Int32 index)
- Int32 **index** ____```
### Player.GetPropStringList
```py
Player.GetPropStringList()```
### Player.GetPropValue
```py
Player.GetPropValue(String name)
- String **name** ____```
### Player.GetRealSkillValue
```py
Player.GetRealSkillValue(String skillname)
- String **skillname** ____```
### Player.GetSkillCap
```py
Player.GetSkillCap(String skillname)
- String **skillname** ____```
### Player.GetSkillStatus
```py
Player.GetSkillStatus(String skillname)
- String **skillname** ____```
### Player.GetSkillValue
```py
Player.GetSkillValue(String skillname)
- String **skillname** ____```
### Player.GetStatStatus
```py
Player.GetStatStatus(String statname)
- String **statname** ____```
### Player.GetType
```py
Player.GetType()```
### Player.GuildButton
```py
Player.GuildButton()```
### Player.HeadMessage
```py
Player.HeadMessage(Int32 hue, Int32 num)
- Int32 **hue** ____
- Int32 **num** ____```
### Player.HeadMessage
```py
Player.HeadMessage(Int32 hue, String message)
- Int32 **hue** ____
- String **message** ____```
### Player.InRangeItem
```py
Player.InRangeItem(Int32 itemserial, Int32 range)
- Int32 **itemserial** ____
- Int32 **range** ____```
### Player.InRangeItem
```py
Player.InRangeItem(Item i, Int32 range)
- Item **i** ____
- Int32 **range** ____```
### Player.InRangeMobile
```py
Player.InRangeMobile(Mobile mob, Int32 range)
- Mobile **mob** ____
- Int32 **range** ____```
### Player.InRangeMobile
```py
Player.InRangeMobile(Int32 mobserial, Int32 range)
- Int32 **mobserial** ____
- Int32 **range** ____```
### Player.InvokeVirtue
```py
Player.InvokeVirtue(String virtue)
- String **virtue** ____```
### Player.KickMember
```py
Player.KickMember(Int32 serial)
- Int32 **serial** ____```
### Player.LeaveParty
```py
Player.LeaveParty()```
### Player.MapSay
```py
Player.MapSay(String msg)
- String **msg** ____```
### Player.MapSay
```py
Player.MapSay(Int32 num)
- Int32 **num** ____```
### Player.PartyAccept
```py
Player.PartyAccept(Int32 serial)
- Int32 **serial** __0__```
### Player.PartyCanLoot
```py
Player.PartyCanLoot(Boolean CanLoot)
- Boolean **CanLoot** ____```
### Player.PartyInvite
```py
Player.PartyInvite()```
### Player.PathFindTo
```py
Player.PathFindTo(Int32 x, Int32 y, Int32 z)
- Int32 **x** ____
- Int32 **y** ____
- Int32 **z** ____```
### Player.PathFindTo
```py
Player.PathFindTo(Point3D Location)
- Point3D **Location** ____```
### Player.QuestButton
```py
Player.QuestButton()```
### Player.Run
```py
Player.Run(String direction, Boolean checkPosition)
- String **direction** ____
- Boolean **checkPosition** __True__```
### Player.SetSkillStatus
```py
Player.SetSkillStatus(String skillname, Int32 status)
- String **skillname** ____
- Int32 **status** ____```
### Player.SetStatStatus
```py
Player.SetStatStatus(String statname, Int32 status)
- String **statname** ____
- Int32 **status** ____```
### Player.SetWarMode
```py
Player.SetWarMode(Boolean warflag)
- Boolean **warflag** ____```
### Player.SpellIsEnabled
```py
Player.SpellIsEnabled(String spell)
- String **spell** ____```
### Player.SumAttribute
```py
Player.SumAttribute(String attributename)
- String **attributename** ____```
### Player.ToggleAlwaysRun
```py
Player.ToggleAlwaysRun()```
### Player.ToString
```py
Player.ToString()```
### Player.UnEquipItemByLayer
```py
Player.UnEquipItemByLayer(String layer, Boolean wait)
- String **layer** ____
- Boolean **wait** __True__```
### Player.UseSkill
```py
Player.UseSkill(String skillname, Boolean wait)
- String **skillname** ____
- Boolean **wait** ____```
### Player.UseSkill
```py
Player.UseSkill(String skillname)
- String **skillname** ____```
### Player.UseSkill
```py
Player.UseSkill(String skillname, Int32 targetSerial, Boolean wait)
- String **skillname** ____
- Int32 **targetSerial** ____
- Boolean **wait** __True__```
### Player.UseSkill
```py
Player.UseSkill(String skillname, EnhancedEntity target, Boolean wait)
- String **skillname** ____
- EnhancedEntity **target** ____
- Boolean **wait** __True__```
//////
### Player.UseSkillOnly
```py
Player.UseSkillOnly(String skillname, Boolean wait)
- String **skillname** ____
- Boolean **wait** ____```
### Player.Walk
```py
Player.Walk(String direction, Boolean checkPosition)
- String **direction** ____
- Boolean **checkPosition** __True__```
### Player.WeaponClearSA
```py
Player.WeaponClearSA()```
### Player.WeaponDisarmSA
```py
Player.WeaponDisarmSA()```
### Player.WeaponPrimarySA
```py
Player.WeaponPrimarySA()```
### Player.WeaponSecondarySA
```py
Player.WeaponSecondarySA()```
### Player.WeaponStunSA
```py
Player.WeaponStunSA()```