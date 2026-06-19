# Globals & Constants

Global functions and constants defined in Blizzard's **addon Lua** (not in the generated API docs), added or removed between builds. Names only — changed function bodies are out of scope.

!!! note "What new / removed means here"
    A name is tracked as a **global function** when it's defined as `function Name(...)` (any indentation, excluding `local`) or `Name = function(...)`. 12.1.0 split the old monolithic FrameXML into many small addons, so this list is large. **Removed** means the name left the global namespace — usually genuinely deleted (e.g. `MouseIsOver`, `RefreshAuras`) or demoted to a `local`; either way addons can no longer call it. Validated against the source: of the new entries, all but one are genuinely absent in 12.0.7.

## Global functions  (new: 240, removed: 110)

**New:**

- **Blizzard_AccessibilityTemplates**: `GetContributingHeight`
- **Blizzard_AchievementUI**: `ShowAchievementFrameForAchievement`
- **Blizzard_ActionBar**: `SpellFlyout_EscapePressed`
- **Blizzard_ActionStatus**: `ActionStatus_DisplayMessage`, `ActionStatus_OnEvent`, `ActionStatus_OnLoad`, `ActionStatus_OnUpdate`
- **Blizzard_AlliedRacesUI**: `AlliedRacesFrame_TryShow`
- **Blizzard_AnimaDiversionUI**: `TryShowAnimaDiversionFrame`
- **Blizzard_ArchaeologyUI**: `ArchaeologyFrame_ToggleUI`, `ArcheologyDigsiteProgressBar_OnSurveyCast`
- **Blizzard_ArdenwealdGardening**: `ArdenwealdGardening_LoadUI`
- **Blizzard_ArtifactUI**: `ArtifactFrame_OnTraitsRefunded`, `ShowArtifactFrame`, `ShowArtifactRelicForgeFrame`
- **Blizzard_AuctionHouseUI**: `HideAuctionHouseFrame`, `ShowAuctionHouseFrame`
- **Blizzard_AuraContainer**: `call`
- **Blizzard_AzeriteEssenceUI**: `AzeriteEssenceUI_LoadUI`
- **Blizzard_AzeriteUI**: `AzeriteEmpoweredItemUI_LoadUI`
- **Blizzard_BarbershopUI**: `HideBarberShopFrame`, `ShowBarberShopFrame`
- **Blizzard_BattlefieldMap**: `BattlefieldMap_ToggleUI`
- **Blizzard_BehavioralMessaging**: `AddBehavioralMessagingTrayToStatusFrames`, `BehavioralMessagingTray_OnNotification`, `BehavioralMessaging_LoadUI`
- **Blizzard_BlackMarketUI**: `HideBlackMarketFrame`, `ShowBlackMarketFrame`
- **Blizzard_BoostTutorial**: `BoostTutorial_LoadUI`
- **Blizzard_ChallengesUI**: `ChallengeModeCompleteBanner_OnChallengeModeCompleted`, `ShowChallengesKeystoneFrame`
- **Blizzard_ChatFrame**: `ChatAdditionalColor_OpenColorPicker`, `GetChatAdditionalColor`, `IsTypeAdditionalChatColor`
- **Blizzard_Collections**: `ShowHeirloomsJournalToClosestUpgradeablePage`
- **Blizzard_ColorPickerFrame**: `OpacityFrame_EscapePressed`
- **Blizzard_CombatText**: `CombatText_LoadUI`
- **Blizzard_Commentator**: `SetSpectatorModeForOtherFrames`
- **Blizzard_Contribution**: `ContributionCollectionFrame_LoadUI`
- **Blizzard_CooldownViewer**: `CooldownManagerLayout_GetGroupBuffVisualAlerts`, `CooldownManagerLayout_GetHiddenGroupBuffs`, `CooldownManagerLayout_SetGroupBuffVisualAlerts`, `CooldownManagerLayout_SetHiddenGroupBuffs`, `CooldownViewerContextMenu_AddAlertEntryButton`, `CooldownViewerContextMenu_AddNewAlertButton`, `CooldownViewerDraggedItem_Clear`, `CooldownViewerDraggedItem_Pickup`, `CooldownViewerDraggedItem_SetIsLegalTarget`, `ShouldDisplaySpellCooldown`
- **Blizzard_CovenantCallings**: `CovenantCallings_LoadUI`
- **Blizzard_CovenantPreviewUI**: `TryShowCovenantPreviewFrame`
- **Blizzard_DebugTools**: `DebugTools_LoadUI`
- **Blizzard_DeprecatedBattleNet**: `BNGetFriendInviteInfo`, `BNSendVerifiedBattleTagInvite`
- **Blizzard_EditMode**: `EditModeManagerFrame_EscapePressed`
- **Blizzard_EncounterJournal**: `EncounterJournal_SetTabVisibe`, `OpenEncounterJournalToJourney`
- **Blizzard_EventTrace**: `EventTrace_LoadUI`
- **Blizzard_ExpansionTrial**: `ExpansionTrial_LoadUI`
- **Blizzard_FlightMap**: `ShowFlightMapFrame`
- **Blizzard_FrameXML**: `HandleQuestSessionInviteToPartyConfirmation`, `SetGhostFrameShown`, `ShowQuestSessionGroupInviteConfirmation`, `ShowQuestSessionGroupInviteReceivedConfirmation`, `WorldStateChallengeModeAnim_OnFinished`, `WorldStateChallengeModeFrame_UpdateMedal`, `WorldStateChallengeModeFrame_UpdateValues`, `WorldStateChallengeModeTimer_OnUpdate`, `WorldStateChallengeMode_CheckTimers`, `WorldStateChallengeMode_DisplayTimers`, `WorldStateChallengeMode_HideTimer`, `WorldStateChallengeMode_OnEvent`, `WorldStateChallengeMode_OnLoad`, `WorldStateChallengeMode_ShowTimer`, `WorldStateProvingGroundsAnim_OnFinished`, `WorldStateProvingGroundsFrame_UpdateValues`, `WorldStateProvingGroundsTimer_OnUpdate`, `WorldStateProvingGrounds_CheckTimers`, `WorldStateProvingGrounds_DisplayTimers`, `WorldStateProvingGrounds_HideTimer`, `WorldStateProvingGrounds_OnEvent`, `WorldStateProvingGrounds_OnLoad`, `WorldStateProvingGrounds_ShowTimer`
- **Blizzard_FrameXMLUtil**: `FadingFrame_CopyTextScalingTime`, `FadingFrame_GetTextScalingMinHeight`, `FadingFrame_InitSlot`, `FadingFrame_SetTextScaling`, `FadingFrame_StartTextScaling`, `FadingFrame_StopTextScaling`, `FadingFrame_UpdateTextScaling`
- **Blizzard_FramerateFrame**: `FramerateFrame_OnShow`, `FramerateFrame_OnUpdate`, `ToggleFramerate`
- **Blizzard_FriendsFrame**: `ToggleRAFPanel`
- **Blizzard_GMChatUI**: `AddGMChatStatusFrameToStatusFrames`, `GMChatFrame_OnWhisperFromGM`, `RestoreGMChatFrameSession`
- **Blizzard_GameMenu**: `GameMenuFrame_EscapePressed`, `GameMenuFrame_IsShown`, `GameMenuFrame_Show`
- **Blizzard_GameMenuEsc**: `RegisterGameMenuEscHandler`
- **Blizzard_GarrisonBase**: `GetGarrisonMissionFrameNameForFollowerType`, `GetGarrisonTypeForFollowerType`
- **Blizzard_GarrisonUI**: `HideGarrisonMissionFrames`, `HideGarrisonShipyardFrame`, `ShowAdventureMapFrameForFollowerType`, `ShowGarrisonCapacitiveDisplayFrame`, `ShowGarrisonMissionFrameForFollowerType`, `ShowGarrisonRecruiterFrame`, `ShowGarrisonShipyardFrame`
- **Blizzard_GlueParent**: `GlueParent_CheckScreenNarrator`
- **Blizzard_GlueXML**: `AccountLoginEditBox_OnTextChanged`, `AccountLogin_OnEnterPressed`, `MovieFrame_Close`, `RealmList_UpdateSortIndicators`
- **Blizzard_GroupFinder**: `LFGListApplicationViewerRemoveEntryButton_OnClick`, `LFGListApplicationViewer_OpenEditMode`
- **Blizzard_GuildBankUI**: `GuildBankLogScroll`, `HideGuildBankFrame`, `ShowGuildBankFrame`
- **Blizzard_GuildControlUI**: `GuildControlDiscord_Loaded_OnEvent`, `GuildControlDiscord_Loaded_OnLoad`, `GuildControlDiscord_SetGuildSettingsCheckboxes`, `GuildControlRankDiscord_OnLoad`, `GuildControlUI_DiscordFrame_OnLoad`, `GuildControlUI_Discord_HideAll`, `GuildControlUI_Discord_Update`, `GuildControlUI_LoadUI`, `GuildControlUI_OnShow`, `GuildControlUI_Setup`, `GuildControlUI_SetupDiscord`, `GuildControlUI_SetupSelected`, `GuildControlUI_Show`, `GuildControlUI_UnlinkDiscord`, `ResetDiscordSettings`
- **Blizzard_HardcoreUI**: `CheckHardcoreGuildLeadStatus`, `GetDeathStaticPopup`, `ShowHardcoreGuildHandoff`
- **Blizzard_HelpFrame**: `AddTicketStatusFrameToStatusFrames`, `HelpFrame_EscapePressed`
- **Blizzard_HousingBulletinBoard**: `HousingBulletinBoardFrame_LoadUI`
- **Blizzard_HousingControls**: `HousingControls_LoadUI`
- **Blizzard_HousingHouseFinder**: `HouseFinderFrame_LoadUI`
- **Blizzard_HybridMinimap**: `HybridMinimap_LoadUI`
- **Blizzard_ItemSocketingUI**: `ShowItemSocketingFrame`
- **Blizzard_ItemUpgradeUI**: `HideItemUpgradeFrame`, `ShowItemUpgradeFrame`
- **Blizzard_Kiosk**: `KioskFrame_HandlePlayerEnteringWorld`, `Kiosk_LoadUI`
- **Blizzard_LandingSoulbinds**: `LandingSoulbinds_LoadUI`
- **Blizzard_ManagedFrameSystem**: `GetBottomManagedFrameContainer`, `GetPlayerBottomManagedFrameContainer`, `GetRightManagedFrameContainer`
- **Blizzard_MatchCelebrationPartyPoseUI**: `ShowMatchCelebrationPartyPoseFrame`
- **Blizzard_MirrorTimer**: `MirrorTimerFrame_OnEvent`, `MirrorTimerFrame_OnLoad`, `MirrorTimerFrame_OnUpdate`, `MirrorTimerFrame_UpdateHiddenTimers`, `MirrorTimer_Show`
- **Blizzard_MovePad**: `MovePad_LoadUI`
- **Blizzard_NewPlayerExperience**: `NPE_InitializeIfLoaded`
- **Blizzard_OrderHallUI**: `OpenOrderHallTalentUI`
- **Blizzard_PVPUI**: `PVPUI_LoadUI`
- **Blizzard_PartyPoseUI**: `IslandsPartyPoseFrame_TryShow`, `WarfrontsPartyPoseFrame_TryShow`
- **Blizzard_PerksProgram**: `ShowPerksProgramFrame`
- **Blizzard_PhotoSharing**: `PhotoSharingFrame_EscapePressed`
- **Blizzard_PlayerChoice**: `PlayerChoiceFrame_TryShow`, `ShowPendingPlayerChoiceResponseUI`
- **Blizzard_PlayerSpells**: `OpenPlayerSpellsToGlyphTarget`
- **Blizzard_Professions**: `ShowProfessionEquipmentHelpTip`, `ShowProfessionsFrame`
- **Blizzard_ProfessionsCustomerOrders**: `HideProfessionsCustomerOrdersFrame`, `ShowProfessionsCustomerOrdersFrame`
- **Blizzard_RaidUI**: `RaidFrameReadyCheckButton_Update`, `RaidPulloutFrameTemplate_CreateContextMenu`
- **Blizzard_ReforgingUI**: `HideReforgingFrame`, `ShowReforgingFrame`
- **Blizzard_RemixArtifactUI**: `ShowRemixArtifactFrame`
- **Blizzard_ReportFrame**: `ReportFrame_EscapePressed`
- **Blizzard_RuneforgeUI**: `ShowRuneforgeFrame`
- **Blizzard_SettingsDefinitions_Frame**: `IsMouseoverCastSupported`
- **Blizzard_Settings_Shared**: `SettingsPanel_EscapePressed`
- **Blizzard_SharedXML**: `BNet_GetBattleTagComponents`, `BNet_GetBattleTagSelf`, `BNet_GetBroadcastTextSelf`, `BNet_GetFriendLevelRank`, `BNet_IsFriendLevelEqualOrHigher`, `InputBoxInstructions_OnEnter`, `InputBoxInstructions_OnLeave`, `InputBoxInstructions_ShowTooltipIfTruncated`, `LoadAddOnWithErrorHandling`
- **Blizzard_SharedXMLBase**: `ApplySecureDelegatesToTable`
- **Blizzard_SimpleCheckout**: `SimpleCheckout_EscapePressed`
- **Blizzard_SocialUI**: `RecruitAFriendFrameSocialInitializeAADC`
- **Blizzard_SocialUIShared**: `SocialUIContactsFrameInitializeAADC`, `ToggleSocialUI`
- **Blizzard_Soulbinds**: `SoulbindViewer_LoadUI`
- **Blizzard_SplashFrame**: `SplashFrame_EscapePressed`
- **Blizzard_StaticPopup_Game**: `ConfirmDisenchantRollDialog_Show`, `ConfirmLootRollDialog_Show`, `ConfirmTalentWipeDialog_Show`, `GossipConfirmDialog_Show`, `HideInstanceBootDialog`, `HideInstanceLockDialog`, `HideSummonConfirmationDialogs`, `IsSummonConfirmationDialogVisible`, `ShowInstanceBootDialog`, `ShowInstanceLockDialog`, `ShowSummonConfirmationDialog`, `UpdateQuestAcceptLogFullDialog`
- **Blizzard_StoreUI**: `CheckActiveStoreForFree`, `StoreEscapePressed`
- **Blizzard_TrainerUI**: `ClassTrainerCollapseAllButton_OnClick`, `ClassTrainer_HideSkillDetails`, `ClassTrainer_SelectFirstLearnableSkill`, `ClassTrainer_SetSubTextColor`, `ClassTrainer_SetToClassTrainer`, `ClassTrainer_SetToTradeSkillTrainer`, `ClassTrainer_ShowSkillDetails`
- **Blizzard_UIPanels_Game**: `AddPlayerInteractionConditions`, `GetDiscordUserCommunityLink`, `GetDiscordUserLink`, `HideGossipFrame`, `LootFrame_EscapePressed`, `RegisterPlayerInteraction`, `ShowTaxiMapFrame`
- **Blizzard_UIParentPanelManager**: `GetUIPanelLayoutAttribute`, `GetUIPanelLayoutFrame`, `ManageFramePositions`, `SetUIPanelLayoutAttribute`
- **Blizzard_UnitFrame**: `CompactUnitFrameLayoutTemplates_LayoutFrameElement`, `LocalizePlayerFrame_zhCN`, `LocalizePlayerFrame_zhTW`
- **Blizzard_VisualAlerts**: `VisualAlertData_ForEach`, `VisualAlert_GetTypeTemplate`, `VisualAlert_GetTypeText`, `VisualAlerts_RegisterAll`
- **Blizzard_WowSurveyUI**: `AddWowSurveyStatusFrameToStatusFrames`, `WowSurveyStatusFrame_OnSurveyDelivered`

**Removed:**

- **Blizzard_Calendar**: `CloseCalendarMenus`
- **Blizzard_FrameXMLBase**: `AddFrameLock`, `IsFrameLockActive`, `IsFrameSmartShown`, `RegisterNewFrameLock`, `RemoveFrameLock`, `SetFrameLock`, `SmartHide`, `SmartShow`, `UpdateFrameLock`
- **Blizzard_FrameXMLUtil**: `RaidBossEmoteFrame_OnEvent`, `RaidBossEmoteFrame_OnLoad`, `RaidNotice_ClearSlot`, `RaidNotice_OnUpdate`, `RaidNotice_SetSlot`, `RaidWarningFrame_OnEvent`, `RaidWarningFrame_OnLoad`
- **Blizzard_FriendsFrame**: `BattleTagInviteFrame_Show`, `FriendsFrameAddFriendButton_OnClick`, `FriendsFrame_CloseQuickJoinHelpTip`, `FriendsFriendsButton_SetSelected`, `FriendsFriendsFrame_Close`, `FriendsFriends_InitButton`, `FriendsFriends_SetSelection`, `ToggleRafPanel`
- **Blizzard_GlueXML**: `RealmListTab_OnClick`, `RealmList_ClickButton`, `RealmSelectButton_OnClick`, `RealmSelectButton_OnDoubleClick`
- **Blizzard_QuickJoin**: `QuickJoin_JoinQueueButtonOnClick`
- **Blizzard_TrainerUI**: `ClassTrainerFrame_Hide`, `ClassTrainerFrame_Show`
- **Blizzard_Transmog**: `DisplayTypeUnassignedSupported`, `HelpPlatesSupported`
- **Blizzard_UIParent**: `AnimateTexCoords`, `AnimatedShine_OnUpdate`, `Arena_LoadUI`, `AuctionFrame_LoadUI`, `BFAMissionFrame_EscapePressed`, `BetterDate`, `BoostTutorial_AttemptLoad`, `BuildColoredListString`, `BuildIconArray`, `BuildListString`, `BuildMultilineTooltip`, `BuildNewLineListString`, `ButtonPulse_OnUpdate`, `CanGroupInvite`, `CommunitiesFrame_IsEnabled`, `ConvertRGBtoColorString`, `CraftFrame_LoadUI`, `ExpansionTrial_CheckLoadUI`, `GetBindingFromClick`, `GetDungeonNameWithDifficulty`, `GetNotchHeight`, `GetScaledCursorPositionForFrame`, `GetScreenHeightScale`, `GetScreenWidthScale`, `GetSmoothProgressChange`, `GetSocialColoredName`, `GetSortedSelfResurrectOptions`, `GetUIParentOffset`, `GlyphFrame_LoadUI`, `InviteToGroup`, `IsLevelAtEffectiveMaxLevel`, `IsPlayerAtEffectiveMaxLevel`, `KeyBindingFrame_LoadUI`, `LocalizePlayerFrame`, `LocalizezhCN`, `LocalizezhTW`, `MajorFactions_LoadUI`, `MouseIsOver`, `NPETutorial_AttemptToBegin`, `NPE_CheckTutorials`, `OpenAchievementFrameToAchievement`, `OrderHallMissionFrame_EscapePressed`, `OrderHallTalentFrame_EscapePressed`, `OutfitterUI_LoadUI`, `QuestChoice_LoadUI`, `RaidBrowser_IsEmpowered`, `RealPartyIsFull`, `RecentTimeDate`, `RefreshAuras`, `ReverseQuestObjective`, `SetDesaturation`, `ShowResurrectRequest`, `ToggleLFGFrame`, `ToggleRaidBrowser`, `ToggleWoWHackCharacterUI`, `TokenFrame_LoadUI`, `TradeSkillFrame_LoadUI`, `TrialAccountCapReached_Inform`, `UIDoFramesIntersect`, `UIParentLoadAddOn`, `UIParent_OnEvent`, `UIParent_OnHide`, `UIParent_OnLoad`, `UIParent_OnShow`, `UIParent_OnUpdate`, `UIParent_Shared_OnEvent`, `UIParent_Shared_OnLoad`, `UIParent_UpdateTopFramePositions`, `UnitHasMana`, `UpdateUIElementsForClientScene`, `WoWHackSpellsUI_LoadUI`, `WorldFrame_OnLoad`, `WorldFrame_OnUpdate`
- **Blizzard_UIParentPanelManager**: `UIParent_ManageFramePositions`
- **Blizzard_UnitFrame**: `CompactUnitFrame_GetOptionDisplayOnlyHealerPowerBars`, `CompactUnitFrame_GetOptionDisplayPowerBar`

## Constants  (new: 13 values + 0 strings, removed: 22)

**New constants (non-string):**

- **Blizzard_ActionStatus**: `ACTION_STATUS_FADETIME`
- **Blizzard_ChatFrame**: `CHAT_CONFIG_ADDITIONAL_COLORS`
- **Blizzard_CooldownViewer**: `CDM_HIDE_INVISIBLE_ITEMS`
- **Blizzard_GlueXMLBase**: `CHAR_CREATE_USES_MODEL_FOG`
- **Blizzard_GuildBankUI**: `GB_ICON_FILENAMES`
- **Blizzard_MirrorTimer**: `MIRRORTIMER_NUMTIMERS`
- **Blizzard_Narration**: `DWELL_TIME_DEFAULT`
- **Blizzard_RaidUI**: `TARGET_UPDATE_TIMER`
- **Blizzard_TimeManager**: `CLOCK_Y_OVERRIDE`
- **Blizzard_TrainerUI**: `SKILL_TEXT_WIDTH`, `TRAINER_FILTER_AVAILABLE_BOOL`, `TRAINER_FILTER_UNAVAILABLE_BOOL`, `TRAINER_FILTER_USED_BOOL`

**Removed constants:**

- **Blizzard_CooldownViewer**: `CDMVIS_ALERT_COLOR_BLUE`, `CDMVIS_ALERT_COLOR_CYAN`, `CDMVIS_ALERT_COLOR_GOLD`, `CDMVIS_ALERT_COLOR_GREEN`, `CDMVIS_ALERT_COLOR_RED`
- **Blizzard_FrameXMLBase**: `FRAMELOCK_STATES`, `FRAMELOCK_STATE_PRIORITIES`
- **Blizzard_FrameXMLUtil**: `RAID_NOTICE_DEFAULT_HOLD_TIME`, `RAID_NOTICE_FADE_IN_TIME`, `RAID_NOTICE_FADE_OUT_TIME`
- **Blizzard_FriendsFrame**: `FRIENDS_FRIENDS_ALL`, `FRIENDS_FRIENDS_MUTUAL`, `FRIENDS_FRIENDS_POTENTIAL`
- **Blizzard_MicroMenu**: `PERFORMANCEBAR_UPDATE_INTERVAL`
- **Blizzard_Minimap**: `GAMETIME_AM`, `GAMETIME_PM`
- **Blizzard_UIParent**: `BOSS_FRAME_CASTBAR_HEIGHT`, `FRAMERATE_FREQUENCY`, `MAX_ACCOUNT_MACROS`, `MAX_CHARACTER_MACROS`, `PULSEBUTTONS`, `SHINES_TO_ANIMATE`

