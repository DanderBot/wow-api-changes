# Field-level API changes

Changes *inside* API entries that exist in both builds — struct fields, enum values, function arguments/returns, event payloads. New and removed whole entries are on the per-namespace pages; this is the exhaustive field-level complement (the layer a surface diff misses).

## Structs with changed fields

### `AddPrivateAuraAnchorArgs` (struct)

```diff
  unitToken: cstring
  auraIndex: number
  parent: SimpleFrame
+ showCooldownFrame: bool
+ showCooldownEdge: bool
  showCountdownNumbers: bool
+ showDispelIcon: bool
  isContainer: bool
  iconInfo: PrivateAuraIconInfo?
  durationAnchor: AnchorBinding?
- showCountdownFrame: bool
```

### `BNetAccountInfo` (struct)

```diff
  bnetAccountID: number
  accountName: string
  battleTag: string
  isFriend: bool
  isBattleTagFriend: bool
+ friendLevel: BattleNetFriendLevel?
  lastOnlineTime: number
  isAFK: bool
  isDND: bool
  isFavorite: bool
+ friendTags: table
  appearOffline: bool
  customMessage: string
  customMessageTime: number
  note: string
  rafLinkType: RafLinkType
  gameAccountInfo: BNetGameAccountInfo
```

### `BNetGameAccountInfo` (struct)

```diff
  gameAccountID: number
  clientProgram: string
  isOnline: bool
  isGameBusy: bool
  isGameAFK: bool
  wowProjectID: number?
  characterName: string?
  realmName: string?
  realmDisplayName: string?
  realmID: number?
  factionName: string?
  raceName: string?
  classID: number?
  className: string?
+ classFilename: cstring?
  areaName: string?
  characterLevel: number?
  richPresence: string?
  playerGuid: WOWGUID?
  canSummon: bool
  hasFocus: bool
  regionID: number
  isInCurrentRegion: bool
  timerunningSeasonID: number?
```

### `ChatMessageEventParams` (struct)

```diff
  text: cstring
  playerName: cstring
  languageName: cstring
  channelName: cstring
  playerName2: cstring
  specialFlags: cstring
  zoneChannelID: number
  channelIndex: number
  channelBaseName: cstring
  languageID: number
  lineID: number
  guid: WOWGUID
  bnSenderID: number
  isMobile: bool
  isSubtitle: bool
  hideSenderInLetterbox: bool
  suppressRaidIcons: bool
+ discordInfo: DiscordChatInfo
```

### `ClubMemberInfo` (struct)

```diff
  isSelf: bool
  memberId: ClubMemberOpaqueId
  name: string?
  role: ClubRoleIdentifier?
  presence: ClubMemberPresence
  clubType: ClubType?
  guid: WOWGUID?
  bnetAccountId: number?
  memberNote: string?
  officerNote: string?
  classID: number?
  race: number?
  level: number?
  zone: string?
  achievementPoints: number?
  profession1ID: number?
  profession1Rank: number?
  profession1Name: string?
  profession2ID: number?
  profession2Rank: number?
  profession2Name: string?
  lastOnlineYear: number?
  lastOnlineMonth: number?
  lastOnlineDay: number?
  lastOnlineHour: number?
  guildRank: string?
  guildRankOrder: luaIndex?
  isRemoteChat: bool?
  overallDungeonScore: number?
  faction: PvPFaction?
  timerunningSeasonID: number?
+ discordInfo: DiscordChatInfo?
```

### `CooldownViewerCooldown` (struct)

```diff
  cooldownID: number
- spellID: number
+ spellID: number?
+ spellCategoryID: number?
  overrideSpellID: number?
  overrideTooltipSpellID: number?
+ equipSlot: luaIndex?
  linkedSpellIDs: table
  selfAura: bool
  hasAura: bool
  charges: bool
  isKnown: bool
+ isInvisible: bool
  flags: CooldownSetSpellFlags
  category: CooldownViewerCategory
```

### `HousingDecorInstanceInfo` (struct)

```diff
  decorGUID: WOWGUID
  decorID: number
  name: cstring
  isLocked: bool
  canBeCustomized: bool
  canBeRemoved: bool
  isAllowedOutdoors: bool
  isAllowedIndoors: bool
  isRefundable: bool
+ canAttachPet: bool
  dyeSlots: table
  dataTagsByID: LuaValueVariant
  size: HousingCatalogEntrySize
```

### `LfgEntryData` (struct)

```diff
  activityIDs: table
  requiredItemLevel: number
  requiredHonorLevel: number
  name: kstringLfgListApplicant
  comment: kstringLfgListApplicant
  voiceChat: kstringLfgListApplicant
+ censored: bool
  duration: time_t
  autoAccept: bool
  privateGroup: bool
  questID: number?
  requiredDungeonScore: number?
  requiredPvpRating: number?
  playstyle: LFGEntryPlaystyle?
  generalPlaystyle: LFGEntryGeneralPlaystyle?
  isCrossFactionListing: bool
  newPlayerFriendly: bool
```

### `LfgSearchResultData` (struct)

```diff
  searchResultID: number
  activityIDs: table
  leaderName: string?
  name: kstringLfgListSearch
  comment: kstringLfgListSearch
  voiceChat: kstringLfgListSearch
+ censored: bool
  requiredItemLevel: number
  requiredHonorLevel: number
  hasSelf: bool
  numMembers: number
  numBNetFriends: number
  numCharFriends: number
  numGuildMates: number
  isDelisted: bool
  autoAccept: bool
  isWarMode: bool
  age: time_t
  questID: number?
  leaderOverallDungeonScore: number?
  leaderDungeonScoreInfo: table
  leaderBestDungeonScoreInfo: BestDungeonScoreMapInfo?
  leaderPvpRatingInfo: table
  requiredDungeonScore: number?
  requiredPvpRating: number?
  playstyle: LFGEntryPlaystyle?
  generalPlaystyle: LFGEntryGeneralPlaystyle?
  crossFactionListing: bool?
  leaderFactionGroup: number
  newPlayerFriendly: bool?
  partyGUID: WOWGUID
```

### `PetJournalPetInfo` (struct)

```diff
  speciesID: number
- customName: string?
+ customName: cstring?
- petLevel: number
+ petLevel: number?
- xp: number
+ xp: number?
- maxXP: number
+ maxXP: number?
- displayID: number
+ displayID: number?
- isFavorite: bool
+ isFavorite: bool?
  icon: fileID
- petType: number
+ petType: luaIndex
  creatureID: number
- name: string?
+ name: cstring?
- sourceText: string
+ sourceText: cstring
- description: string
+ description: cstring
- isWild: bool
+ isWild: bool?
  canBattle: bool
  tradable: bool
  unique: bool
  obtainable: bool
+ canAttachToDecor: bool
+ creatureModelScale: number?
```

### `PlaySoundParams` (struct)

```diff
  soundKitID: number
  uiSoundSubType: UISoundSubType
  forceNoDuplicates: bool
  runFinishCallback: bool
  overridePriority: number?
+ volumeOverride: number?
```

### `PlayerChoiceInfo` (struct)

```diff
  objectGUID: WOWGUID
  choiceID: number
  questionText: string
  pendingChoiceText: string
  uiTextureKit: textureKit
  hideWarboardHeader: bool
  keepOpenAfterChoice: bool
  showChoicesAsList: bool
  requiresSelection: bool
  showChoicesAsGrid: bool
+ hideAnswerArt: bool
  options: table
  soundKitID: number?
  closeUISoundKitID: number?
```

### `TieredEntranceTierInfo` (struct)

```diff
  tier: number
  suggestedILvl: number
+ overrideTooltipSpellID: number
  unlocked: bool
  tierDescription: string
  rewards: table
  modifierUIWidgetSetID: number
  lockedReason: cstring?
+ isLFG: bool
```

### `UnitPrivateAuraAnchorInfo` (struct)

```diff
  anchorID: number
  unitToken: string
  auraIndex: number
+ showCooldownFrame: bool
+ showCooldownEdge: bool
  showCountdownNumbers: bool
+ showDispelIcon: bool
  iconWidth: uiUnit?
  iconHeight: uiUnit?
  borderScale: uiUnit?
  isContainer: bool?
  parent: SimpleFrame
- showCountdownFrame: bool
```

## Enums with changed values

- **`ClubStreamType`** — added `Discord`.
- **`CompanionConfigSlotTypes`** — added `Flavor`.
- **`CooldownViewerCategory`** — added `EquipSlotEssential`, `EquipSlotTracked`, `GroupBuff`, `SpecAgnosticEssential`, `SpecAgnosticTracked`.
- **`EditModeAccountSetting`** — added `ShowRaidWarning`.
- **`EditModeMinimapSetting`** — added `IconScale`.
- **`EditModeSystem`** — added `RaidWarning`.
- **`EditModeUnitFrameSetting`** — added `BuffIconSize`, `DebuffIconSize`; removed `IconSize`.
- **`FragmentID`** — added `FMapObject`, `FWorldStateListenerData`.
- **`FrameTutorialAccount`** — added `HousingPetBeds`.
- **`HouseFinderSuggestionReason`** — added `Relinquished`.
- **`HousingResult`** — added `BlueprintCodeInvalid`, `BlueprintGenericExportError`, `BlueprintGenericImportError`, `BlueprintLocationInvalid`, `BlueprintNameInvalid`, `BlueprintNotFound`, `BlueprintRequirementsUnmet`, `BlueprintStorageLimit`, `BlueprintTypeInvalid`, `BlueprintVersionInvalid`, `InsufficientRoomBudget`, `InvalidExteriorDocument`, `InvalidInteriorDocument`, `RoomPlacementOutOfBounds`.
- **`NamePlateStyle`** — added `Classic`.
- **`PingResult`** — added `FailedSilent`.
- **`PingSubjectType`** — added `ActionOnCooldown`, `ActionReady`, `ActionUnavailable`.
- **`SecretAspect`** — added `RadialProgress`.
- **`TieredEntranceType`** — added `Lairs`.
- **`TooltipDataLineType`** — added `ItemSpellTriggerOnEquip`, `ItemSpellTriggerOnProc`, `ItemSpellTriggerOnUse`.

## Functions with changed signatures

#### `C_ActionBar.ForceUpdateAction`

- args: `slotID: luaIndex` → `slotID: luaIndex, suppressEvents: bool`

#### `C_CombatAudioAlert.SpeakText`

- returns: `(none)` → `utteranceID: number`

#### `C_HousingDecor.GetMaxPlacementBudget`

- returns: `maxBudget: number` → `maxBudget: number?`

#### `C_HousingDecor.GetSpentPlacementBudget`

- returns: `totalCost: number` → `totalCost: number?`

#### `C_HousingLayout.GetRoomPlacementBudget`

- returns: `placementBudget: number` → `placementBudget: number?`

#### `C_HousingLayout.GetSpentPlacementBudget`

- returns: `spentPlacementBudget: number` → `spentPlacementBudget: number?`

#### `C_Ping.SendMacroPing`

- args: `type: PingSubjectType?, targetToken: cstring?` → `macroInfo: PingMacroInfo`

#### `C_QuestHub.IsQuestCurrentlyRelatedToHub`

- args: `questID: number, areaPoiID: number` → `questID: number, hubAreaPoiID: number`

#### `C_RecruitAFriend.CanSummonFriend`

- returns: `result: bool` → `canSummon: bool, reason: RecruitAFriendFailure`

#### `C_Sound.PlaySound`

- args: `soundKitID: number, uiSoundSubType: UISoundSubType, forceNoDuplicates: bool, runFinishCallback: bool, overridePriority: number?` → `soundKitID: number, uiSoundSubType: UISoundSubType, forceNoDuplicates: bool, runFinishCallback: bool, overridePriority: number?, volumeOverride: number?`

#### `C_Spell.GetSpellName`

- returns: `name: string` → `name: cstring`

#### `C_Spell.GetSpellTexture`

- returns: `iconID: fileID, originalIconID: fileID` → `iconID: fileID, originalIconID: fileID, conditionalIconID: fileID?`

#### `FrameScript.CreateSecureDelegate`

- args: `luaFunction: LuaValueReference` → `luaFunction: LuaValueReference, options: SecureDelegateOptions?`

#### `SimpleAnimAPI.GetScript`

- args: `scriptTypeName: cstring, bindingType: number?` → `scriptTypeName: ScriptTypeName, bindingType: ScriptBindingType`
- returns: `script: luaFunction` → `script: LuaFunctionReference`

#### `SimpleAnimAPI.HookScript`

- args: `scriptTypeName: cstring, script: luaFunction, bindingType: number?` → `scriptTypeName: ScriptTypeName, script: LuaFunctionReference, bindingType: ScriptBindingType`
- returns: `(none)` → `success: bool`

#### `SimpleAnimAPI.SetScript`

- args: `scriptTypeName: cstring, script: luaFunction?` → `scriptTypeName: ScriptTypeName, script: LuaFunctionReference?`

#### `SimpleAnimGroupAPI.GetScript`

- args: `scriptTypeName: cstring, bindingType: number?` → `scriptTypeName: ScriptTypeName, bindingType: ScriptBindingType`
- returns: `script: luaFunction` → `script: LuaFunctionReference`

#### `SimpleAnimGroupAPI.HookScript`

- args: `scriptTypeName: cstring, script: luaFunction, bindingType: number?` → `scriptTypeName: ScriptTypeName, script: LuaFunctionReference, bindingType: ScriptBindingType`
- returns: `(none)` → `success: bool`

#### `SimpleAnimGroupAPI.SetScript`

- args: `scriptTypeName: cstring, script: luaFunction?` → `scriptTypeName: ScriptTypeName, script: LuaFunctionReference?`

#### `SimpleScriptRegionAPI.GetScript`

- args: `scriptTypeName: cstring, bindingType: number?` → `scriptTypeName: ScriptTypeName, bindingType: ScriptBindingType`
- returns: `script: luaFunction` → `script: LuaFunctionReference`

#### `SimpleScriptRegionAPI.HookScript`

- args: `scriptTypeName: cstring, script: luaFunction, bindingType: number?` → `scriptTypeName: ScriptTypeName, script: LuaFunctionReference, bindingType: ScriptBindingType`
- returns: `(none)` → `success: bool`

#### `SimpleScriptRegionAPI.SetScript`

- args: `scriptTypeName: cstring, script: luaFunction?` → `scriptTypeName: ScriptTypeName, script: LuaFunctionReference?`

## Events with changed payloads

- **`ChatCombatMsgArenaPointsGain`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgAchievement`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgAfk`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBgSystemAlliance`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBgSystemHorde`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBgSystemNeutral`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBn`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBnInlineToastAlert`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBnInlineToastBroadcast`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBnInlineToastBroadcastInform`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBnInlineToastConversation`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBnWhisper`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBnWhisperInform`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgBnWhisperPlayerOffline`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgChannel`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgChannelJoin`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgChannelLeave`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgChannelList`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgChannelNotice`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgChannelNoticeUser`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgCombatFactionChange`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgCombatHonorGain`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgCombatMiscInfo`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgCombatXpGain`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgCommunitiesChannel`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgCurrency`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgDnd`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgEmote`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgFiltered`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgGuild`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgGuildAchievement`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgGuildItemLooted`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgIgnored`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgInstanceChat`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgInstanceChatLeader`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgLoot`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgMoney`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgMonsterEmote`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgMonsterParty`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgMonsterSay`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgMonsterWhisper`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgMonsterYell`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgOfficer`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgOpening`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgParty`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgPartyLeader`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgPetBattleCombatLog`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgPetBattleInfo`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgPetInfo`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgPing`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgRaid`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgRaidBossEmote`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgRaidBossWhisper`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgRaidLeader`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgRaidWarning`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgRestricted`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgSay`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgSkill`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgSystem`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgTargeticons`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgTextEmote`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgTradeskills`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgVoiceText`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgWhisper`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgWhisperInform`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`ChatMsgYell`** — payload `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool` → `text: cstring, playerName: cstring, languageName: cstring, channelName: cstring, playerName2: cstring, specialFlags: cstring, zoneChannelID: number, channelIndex: number, channelBaseName: cstring, languageID: number, lineID: number, guid: WOWGUID, bnSenderID: number, isMobile: bool, isSubtitle: bool, hideSenderInLetterbox: bool, suppressRaidIcons: bool, discordInfo: DiscordChatInfo`
- **`SpellUpdateCooldown`** — payload `spellID: number?, baseSpellID: number?, category: number?, startRecoveryCategory: number?` → `spellID: number?, baseSpellID: number?, category: number?, startRecoveryCategory: number?, itemID: number?`

