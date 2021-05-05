:mod:`Player`
========================================
.. py:module:: Player


Properties
----------------
* Player.AR :mod:`Int32`

* Player.Backpack :mod:`Item`

* Player.Bank :mod:`Item`

* Player.Body :mod:`Int32`

* Player.Buffs :mod:`List[String]`

* Player.ColdResistance :mod:`Int32`

* Player.DamageChanceIncrease :mod:`Int32`

* Player.DefenseChanceIncrease :mod:`Int32`

* Player.Dex :mod:`Int32`

* Player.DexterityIncrease :mod:`Int32`

* Player.Direction :mod:`String`

* Player.EnergyResistance :mod:`Int32`

* Player.EnhancePotions :mod:`Int32`

* Player.FasterCasting :mod:`Int32`

* Player.FasterCastRecovery :mod:`Int32`

* Player.Female :mod:`Boolean`

* Player.FireResistance :mod:`Int32`

* Player.Followers :mod:`Int32`

* Player.FollowersMax :mod:`Int32`

* Player.Gold :mod:`Int32`

* Player.HasSpecial :mod:`Boolean`

* Player.HitPointsIncrease :mod:`Int32`

* Player.HitPointsRegeneration :mod:`Int32`

* Player.Hits :mod:`Int32`

* Player.HitsMax :mod:`Int32`

* Player.InParty :mod:`Boolean`

* Player.Int :mod:`Int32`

* Player.IntelligenceIncrease :mod:`Int32`

* Player.IsGhost :mod:`Boolean`

* Player.LowerManaCost :mod:`Int32`

* Player.LowerReagentCost :mod:`Int32`

* Player.Luck :mod:`Int32`

* Player.Mana :mod:`Int32`

* Player.ManaIncrease :mod:`Int32`

* Player.ManaMax :mod:`Int32`

* Player.ManaRegeneration :mod:`Int32`

* Player.Map :mod:`Int32`

* Player.MaximumHitPointsIncrease :mod:`Int32`

* Player.MaximumManaIncrease :mod:`Int32`

* Player.MaximumStaminaIncrease :mod:`Int32`

* Player.MaxWeight :mod:`Int32`

* Player.MobileID :mod:`Int32`

* Player.Mount :mod:`Item`

* Player.Name :mod:`String`

* Player.Notoriety :mod:`Byte`

* Player.Paralized :mod:`Boolean`

* Player.Poisoned :mod:`Boolean`

* Player.PoisonResistance :mod:`Int32`

* Player.Position :mod:`Point3D`

* Player.Quiver :mod:`Item`

* Player.ReflectPhysicalDamage :mod:`Int32`

* Player.Serial :mod:`Int32`

* Player.SpellDamageIncrease :mod:`Int32`

* Player.Stam :mod:`Int32`

* Player.StaminaIncrease :mod:`Int32`

* Player.StaminaRegeneration :mod:`Int32`

* Player.StamMax :mod:`Int32`

* Player.StatCap :mod:`Int32`

* Player.StaticMount :mod:`Int32`

* Player.Str :mod:`Int32`

* Player.StrengthIncrease :mod:`Int32`

* Player.SwingSpeedIncrease :mod:`Int32`

* Player.Visible :mod:`Boolean`

* Player.WarMode :mod:`Boolean`

* Player.Weight :mod:`Int32`

* Player.YellowHits :mod:`Boolean`


Methods
--------------

.. py:function:: Player.Attack(serial) -> Void


* serial: :mod:`Int32` 




.. py:function:: Player.Attack(m) -> Void


* m: :mod:`Mobile` 




.. py:function:: Player.AttackLast() -> Void







.. py:function:: Player.BuffsExist(buffname) -> Boolean


* buffname: :mod:`String` 




.. py:function:: Player.ChatAlliance(num) -> Void


* num: :mod:`Int32` 




.. py:function:: Player.ChatAlliance(msg) -> Void


* msg: :mod:`String` 




.. py:function:: Player.ChatChannel(msg) -> Void


* msg: :mod:`String` 




.. py:function:: Player.ChatChannel(num) -> Void


* num: :mod:`Int32` 




.. py:function:: Player.ChatEmote(hue, msg) -> Void


* hue: :mod:`Int32` 
* msg: :mod:`String` 




.. py:function:: Player.ChatEmote(hue, num) -> Void


* hue: :mod:`Int32` 
* num: :mod:`Int32` 




.. py:function:: Player.ChatGuild(num) -> Void


* num: :mod:`Int32` 




.. py:function:: Player.ChatGuild(msg) -> Void


* msg: :mod:`String` 




.. py:function:: Player.ChatParty(msg, serial) -> Void


* msg: :mod:`String` 
* serial: :mod:`Int32` 




.. py:function:: Player.ChatSay(hue, msg) -> Void


* hue: :mod:`Int32` 
* msg: :mod:`String` 




.. py:function:: Player.ChatSay(hue, num) -> Void


* hue: :mod:`Int32` 
* num: :mod:`Int32` 




.. py:function:: Player.ChatWhisper(hue, msg) -> Void


* hue: :mod:`Int32` 
* msg: :mod:`String` 




.. py:function:: Player.ChatWhisper(hue, num) -> Void


* hue: :mod:`Int32` 
* num: :mod:`Int32` 




.. py:function:: Player.ChatYell(hue, msg) -> Void


* hue: :mod:`Int32` 
* msg: :mod:`String` 




.. py:function:: Player.ChatYell(hue, num) -> Void


* hue: :mod:`Int32` 
* num: :mod:`Int32` 




.. py:function:: Player.CheckLayer(layer) -> Boolean


* layer: :mod:`String` 




.. py:function:: Player.DistanceTo(m) -> Int32


* m: :mod:`Mobile` 




.. py:function:: Player.DistanceTo(i) -> Int32


* i: :mod:`Item` 




.. py:function:: Player.EquipItem(item) -> Void


* item: :mod:`Item` 




.. py:function:: Player.EquipItem(serial) -> Void


* serial: :mod:`Int32` 




.. py:function:: Player.EquipUO3D(serials) -> Void


* serials: :mod:`List[Int32]` 




.. py:function:: Player.Fly(on) -> Void


* on: :mod:`Boolean` 




.. py:function:: Player.GetItemOnLayer(layer) -> Item


* layer: :mod:`String` 




.. py:function:: Player.GetPropStringByIndex(index) -> String


* index: :mod:`Int32` 




.. py:function:: Player.GetPropStringList() -> List[String]







.. py:function:: Player.GetPropValue(name) -> Int32


* name: :mod:`String` 




.. py:function:: Player.GetRealSkillValue(skillname) -> Double


* skillname: :mod:`String` 




.. py:function:: Player.GetSkillCap(skillname) -> Double


* skillname: :mod:`String` 




.. py:function:: Player.GetSkillStatus(skillname) -> Int32


* skillname: :mod:`String` 




.. py:function:: Player.GetSkillValue(skillname) -> Double


* skillname: :mod:`String` 




.. py:function:: Player.GetStatStatus(statname) -> Int32


* statname: :mod:`String` 




.. py:function:: Player.GuildButton() -> Void







.. py:function:: Player.HeadMessage(hue, message) -> Void


* hue: :mod:`Int32` 
* message: :mod:`String` 




.. py:function:: Player.HeadMessage(hue, num) -> Void


* hue: :mod:`Int32` 
* num: :mod:`Int32` 




.. py:function:: Player.InRangeItem(i, range) -> Boolean


* i: :mod:`Item` 
* range: :mod:`Int32` 




.. py:function:: Player.InRangeItem(itemserial, range) -> Boolean


* itemserial: :mod:`Int32` 
* range: :mod:`Int32` 




.. py:function:: Player.InRangeMobile(mob, range) -> Boolean


* mob: :mod:`Mobile` 
* range: :mod:`Int32` 




.. py:function:: Player.InRangeMobile(mobserial, range) -> Boolean


* mobserial: :mod:`Int32` 
* range: :mod:`Int32` 




.. py:function:: Player.InvokeVirtue(virtue) -> Void


* virtue: :mod:`String` 




.. py:function:: Player.KickMember(serial) -> Void


* serial: :mod:`Int32` 




.. py:function:: Player.LeaveParty() -> Void







.. py:function:: Player.MapSay(num) -> Void


* num: :mod:`Int32` 




.. py:function:: Player.MapSay(msg) -> Void


* msg: :mod:`String` 




.. py:function:: Player.PartyAccept(serial) -> Void


* serial: :mod:`Int32` 




.. py:function:: Player.PartyCanLoot(CanLoot) -> Void


* CanLoot: :mod:`Boolean` 




.. py:function:: Player.PartyInvite() -> Void







.. py:function:: Player.PathFindTo(x, y, z) -> Void


* x: :mod:`Int32` 
* y: :mod:`Int32` 
* z: :mod:`Int32` 




.. py:function:: Player.PathFindTo(Location) -> Void


* Location: :mod:`Point3D` 




.. py:function:: Player.QuestButton() -> Void







.. py:function:: Player.Run(direction, checkPosition) -> Boolean


* direction: :mod:`String` 
* checkPosition: :mod:`Boolean` 




.. py:function:: Player.SetSkillStatus(skillname, status) -> Void


* skillname: :mod:`String` 
* status: :mod:`Int32` 




.. py:function:: Player.SetStatStatus(statname, status) -> Void


* statname: :mod:`String` 
* status: :mod:`Int32` 




.. py:function:: Player.SetWarMode(warflag) -> Void


* warflag: :mod:`Boolean` 




.. py:function:: Player.SpellIsEnabled(spell) -> Boolean


* spell: :mod:`String` 




.. py:function:: Player.SumAttribute(attributename) -> Single


* attributename: :mod:`String` 




.. py:function:: Player.ToggleAlwaysRun() -> Void







.. py:function:: Player.UnEquipItemByLayer(layer, wait) -> Void


* layer: :mod:`String` 
* wait: :mod:`Boolean` 




.. py:function:: Player.UseSkill(skillname) -> Void


* skillname: :mod:`String` 




.. py:function:: Player.UseSkill(skillname, targetSerial, wait) -> Void


* skillname: :mod:`String` 
* targetSerial: :mod:`Int32` 
* wait: :mod:`Boolean` 




.. py:function:: Player.UseSkill(skillname, target, wait) -> Void


* skillname: :mod:`String` 
* target: :mod:`EnhancedEntity` 
* wait: :mod:`Boolean` 


//////

.. py:function:: Player.UseSkill(skillname, wait) -> Void


* skillname: :mod:`String` 
* wait: :mod:`Boolean` 




.. py:function:: Player.UseSkillOnly(skillname, wait) -> Void


* skillname: :mod:`String` 
* wait: :mod:`Boolean` 




.. py:function:: Player.Walk(direction, checkPosition) -> Boolean


* direction: :mod:`String` 
* checkPosition: :mod:`Boolean` 




.. py:function:: Player.WeaponClearSA() -> Void







.. py:function:: Player.WeaponDisarmSA() -> Void







.. py:function:: Player.WeaponPrimarySA() -> Void







.. py:function:: Player.WeaponSecondarySA() -> Void







.. py:function:: Player.WeaponStunSA() -> Void






