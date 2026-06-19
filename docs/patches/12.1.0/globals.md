# Globals & Constants

Global functions and constants defined in Blizzard's **addon Lua** (not in the generated API docs), added or removed between builds. Each function shows its parameter signature where it's on one line in source. Bodies are out of scope.

!!! note "What new / removed means here"
    A name is tracked as a **global function** when it's defined as `function Name(...)` (any indentation, excluding `local`) or `Name = function(...)`. 12.1.0 split the old monolithic FrameXML into many small addons, so this list is large. **Removed** means the name left the global namespace — usually genuinely deleted (e.g. `MouseIsOver`, `RefreshAuras`) or demoted to a `local`; either way addons can no longer call it. Validated against the source: of the new entries, all but one are genuinely absent in 12.0.7.

## Global functions  (new: 240, removed: 110)

**New:**

- **Blizzard_AccessibilityTemplates**: `GetContributingHeight(elem)`
- **Blizzard_AchievementUI**: `ShowAchievementFrameForAchievement(achievementID)`
- **Blizzard_ActionBar**: `SpellFlyout_EscapePressed()`
- **Blizzard_ActionStatus**: `ActionStatus_DisplayMessage(text, ignoreNewbieTooltipSetting)`, `ActionStatus_OnEvent(self, event, ...)`, `ActionStatus_OnLoad(self)`, `ActionStatus_OnUpdate(self)`
- **Blizzard_AlliedRacesUI**: `AlliedRacesFrame_TryShow(raceID)`
- **Blizzard_AnimaDiversionUI**: `TryShowAnimaDiversionFrame(...)`
- **Blizzard_ArchaeologyUI**: `ArchaeologyFrame_ToggleUI()`, `ArcheologyDigsiteProgressBar_OnSurveyCast(event, ...)`
- **Blizzard_ArdenwealdGardening**: `ArdenwealdGardening_LoadUI()`
- **Blizzard_ArtifactUI**: `ArtifactFrame_OnTraitsRefunded(numRefunded, refundedTier)`, `ShowArtifactFrame()`, `ShowArtifactRelicForgeFrame()`
- **Blizzard_AuctionHouseUI**: `HideAuctionHouseFrame()`, `ShowAuctionHouseFrame()`
- **Blizzard_AuraContainer**: `call(must not be a forbidden object)`
- **Blizzard_AzeriteEssenceUI**: `AzeriteEssenceUI_LoadUI()`
- **Blizzard_AzeriteUI**: `AzeriteEmpoweredItemUI_LoadUI()`
- **Blizzard_BarbershopUI**: `HideBarberShopFrame()`, `ShowBarberShopFrame()`
- **Blizzard_BattlefieldMap**: `BattlefieldMap_ToggleUI()`
- **Blizzard_BehavioralMessaging**: `AddBehavioralMessagingTrayToStatusFrames(statusFrames)`, `BehavioralMessagingTray_OnNotification(event, ...)`, `BehavioralMessaging_LoadUI()`
- **Blizzard_BlackMarketUI**: `HideBlackMarketFrame()`, `ShowBlackMarketFrame()`
- **Blizzard_BoostTutorial**: `BoostTutorial_LoadUI()`
- **Blizzard_ChallengesUI**: `ChallengeModeCompleteBanner_OnChallengeModeCompleted(event, ...)`, `ShowChallengesKeystoneFrame()`
- **Blizzard_ChatFrame**: `ChatAdditionalColor_OpenColorPicker(self)`, `GetChatAdditionalColor(type)`, `IsTypeAdditionalChatColor(type)`
- **Blizzard_Collections**: `ShowHeirloomsJournalToClosestUpgradeablePage()`
- **Blizzard_ColorPickerFrame**: `OpacityFrame_EscapePressed()`
- **Blizzard_CombatText**: `CombatText_LoadUI()`
- **Blizzard_Commentator**: `SetSpectatorModeForOtherFrames(spectatorMode)`
- **Blizzard_Contribution**: `ContributionCollectionFrame_LoadUI()`
- **Blizzard_CooldownViewer**: `CooldownManagerLayout_GetGroupBuffVisualAlerts(layout)`, `CooldownManagerLayout_GetHiddenGroupBuffs(layout)`, `CooldownManagerLayout_SetGroupBuffVisualAlerts(layout, visualAlerts)`, `CooldownManagerLayout_SetHiddenGroupBuffs(layout, hiddenGroupBuffs)`, `CooldownViewerContextMenu_AddAlertEntryButton(rootDescription, alertType, payloadText, eventText, editCallback, deleteCallback, playSampleCallback)`, `CooldownViewerContextMenu_AddNewAlertButton(rootDescription, text, isEnabled, onClickCallback, disabledTooltipCallback)`, `CooldownViewerDraggedItem_Clear()`, `CooldownViewerDraggedItem_Pickup(iconFileID)`, `CooldownViewerDraggedItem_SetIsLegalTarget(isLegal)`, `ShouldDisplaySpellCooldown(cooldownInfo)`
- **Blizzard_CovenantCallings**: `CovenantCallings_LoadUI()`
- **Blizzard_CovenantPreviewUI**: `TryShowCovenantPreviewFrame(...)`
- **Blizzard_DebugTools**: `DebugTools_LoadUI()`
- **Blizzard_DeprecatedBattleNet**: `BNGetFriendInviteInfo(inviteIndex)`, `BNSendVerifiedBattleTagInvite()`
- **Blizzard_EditMode**: `EditModeManagerFrame_EscapePressed()`
- **Blizzard_EncounterJournal**: `EncounterJournal_SetTabVisibe(tab, visible)`, `OpenEncounterJournalToJourney(factionID)`
- **Blizzard_EventTrace**: `EventTrace_LoadUI()`
- **Blizzard_ExpansionTrial**: `ExpansionTrial_LoadUI()`
- **Blizzard_FlightMap**: `ShowFlightMapFrame()`
- **Blizzard_FrameXML**: `HandleQuestSessionInviteToPartyConfirmation(name, willConvertToRaid)`, `SetGhostFrameShown(shown)`, `ShowQuestSessionGroupInviteConfirmation(invite, text)`, `ShowQuestSessionGroupInviteReceivedConfirmation(name, text)`, `WorldStateChallengeModeAnim_OnFinished(self)`, `WorldStateChallengeModeFrame_UpdateMedal(self, elapsedTime)`, `WorldStateChallengeModeFrame_UpdateValues(self, elapsedTime)`, `WorldStateChallengeModeTimer_OnUpdate(self, elapsed)`, `WorldStateChallengeMode_CheckTimers(...)`, `WorldStateChallengeMode_DisplayTimers(lineFrame, nextAnchor, maxHeight, frameWidth)`, `WorldStateChallengeMode_HideTimer(timerID)`, `WorldStateChallengeMode_OnEvent(self, event, ...)`, `WorldStateChallengeMode_OnLoad(self)`, `WorldStateChallengeMode_ShowTimer(timerID, elapsedTime, times)`, `WorldStateProvingGroundsAnim_OnFinished(self)`, `WorldStateProvingGroundsFrame_UpdateValues(self, elapsedTime)`, `WorldStateProvingGroundsTimer_OnUpdate(self, elapsed)`, `WorldStateProvingGrounds_CheckTimers(...)`, `WorldStateProvingGrounds_DisplayTimers(lineFrame, nextAnchor, maxHeight, frameWidth)`, `WorldStateProvingGrounds_HideTimer(timerID)`, `WorldStateProvingGrounds_OnEvent(self, event, ...)`, `WorldStateProvingGrounds_OnLoad(self)`, `WorldStateProvingGrounds_ShowTimer(timerID, elapsedTime, duration, medalIndex, currWave, maxWave)`
- **Blizzard_FrameXMLUtil**: `FadingFrame_CopyTextScalingTime(sourceFadingFrame, targetFadingFrame)`, `FadingFrame_GetTextScalingMinHeight(fadingFrame)`, `FadingFrame_InitSlot(fadingFrame, fadeInTime, fadeOutTime, minHeight, maxHeight, scaleUpTime, scaleDownTime)`, `FadingFrame_SetTextScaling(fadingFrame, minHeight, maxHeight, scaleUpTime, scaleDownTime)`, `FadingFrame_StartTextScaling(fadingFrame)`, `FadingFrame_StopTextScaling(fadingFrame)`, `FadingFrame_UpdateTextScaling(fadingFrame, elapsedTime)`
- **Blizzard_FramerateFrame**: `FramerateFrame_OnShow(self)`, `FramerateFrame_OnUpdate(self, elapsed)`, `ToggleFramerate(benchmark)`
- **Blizzard_FriendsFrame**: `ToggleRAFPanel()`
- **Blizzard_GMChatUI**: `AddGMChatStatusFrameToStatusFrames(statusFrames)`, `GMChatFrame_OnWhisperFromGM(event, ...)`, `RestoreGMChatFrameSession(lastTalkedToGM)`
- **Blizzard_GameMenu**: `GameMenuFrame_EscapePressed()`, `GameMenuFrame_IsShown()`, `GameMenuFrame_Show()`
- **Blizzard_GameMenuEsc**: `RegisterGameMenuEscHandler(priority, handler)`
- **Blizzard_GarrisonBase**: `GetGarrisonMissionFrameNameForFollowerType(followerTypeID)`, `GetGarrisonTypeForFollowerType(followerTypeID)`
- **Blizzard_GarrisonUI**: `HideGarrisonMissionFrames()`, `HideGarrisonShipyardFrame()`, `ShowAdventureMapFrameForFollowerType(followerType)`, `ShowGarrisonCapacitiveDisplayFrame()`, `ShowGarrisonMissionFrameForFollowerType(followerType)`, `ShowGarrisonRecruiterFrame()`, `ShowGarrisonShipyardFrame(followerTypeID)`
- **Blizzard_GlueParent**: `GlueParent_CheckScreenNarrator()`
- **Blizzard_GlueXML**: `AccountLoginEditBox_OnTextChanged(self)`, `AccountLogin_OnEnterPressed()`, `MovieFrame_Close()`, `RealmList_UpdateSortIndicators()`
- **Blizzard_GroupFinder**: `LFGListApplicationViewerRemoveEntryButton_OnClick(self)`, `LFGListApplicationViewer_OpenEditMode()`
- **Blizzard_GuildBankUI**: `GuildBankLogScroll()`, `HideGuildBankFrame()`, `ShowGuildBankFrame()`
- **Blizzard_GuildControlUI**: `GuildControlDiscord_Loaded_OnEvent(self, event)`, `GuildControlDiscord_Loaded_OnLoad(self)`, `GuildControlDiscord_SetGuildSettingsCheckboxes(self)`, `GuildControlRankDiscord_OnLoad(self)`, `GuildControlUI_DiscordFrame_OnLoad(self)`, `GuildControlUI_Discord_HideAll(self)`, `GuildControlUI_Discord_Update(self)`, `GuildControlUI_LoadUI()`, `GuildControlUI_OnShow(self)`, `GuildControlUI_Setup()`, `GuildControlUI_SetupDiscord(self)`, `GuildControlUI_SetupSelected(selected)`, `GuildControlUI_Show()`, `GuildControlUI_UnlinkDiscord()`, `ResetDiscordSettings()`
- **Blizzard_HardcoreUI**: `CheckHardcoreGuildLeadStatus()`, `GetDeathStaticPopup()`, `ShowHardcoreGuildHandoff()`
- **Blizzard_HelpFrame**: `AddTicketStatusFrameToStatusFrames(statusFrames)`, `HelpFrame_EscapePressed()`
- **Blizzard_HousingBulletinBoard**: `HousingBulletinBoardFrame_LoadUI()`
- **Blizzard_HousingControls**: `HousingControls_LoadUI()`
- **Blizzard_HousingHouseFinder**: `HouseFinderFrame_LoadUI()`
- **Blizzard_HybridMinimap**: `HybridMinimap_LoadUI()`
- **Blizzard_ItemSocketingUI**: `ShowItemSocketingFrame()`
- **Blizzard_ItemUpgradeUI**: `HideItemUpgradeFrame()`, `ShowItemUpgradeFrame()`
- **Blizzard_Kiosk**: `KioskFrame_HandlePlayerEnteringWorld(isInitialLogin, isUIReload)`, `Kiosk_LoadUI()`
- **Blizzard_LandingSoulbinds**: `LandingSoulbinds_LoadUI()`
- **Blizzard_ManagedFrameSystem**: `GetBottomManagedFrameContainer()`, `GetPlayerBottomManagedFrameContainer()`, `GetRightManagedFrameContainer()`
- **Blizzard_MatchCelebrationPartyPoseUI**: `ShowMatchCelebrationPartyPoseFrame(partyPoseID, won)`
- **Blizzard_MirrorTimer**: `MirrorTimerFrame_OnEvent(self, event, ...)`, `MirrorTimerFrame_OnLoad(self)`, `MirrorTimerFrame_OnUpdate(frame, elapsed)`, `MirrorTimerFrame_UpdateHiddenTimers(elapsed)`, `MirrorTimer_Show(timer, value, maxvalue, scale, paused, label)`
- **Blizzard_MovePad**: `MovePad_LoadUI()`
- **Blizzard_NewPlayerExperience**: `NPE_InitializeIfLoaded()`
- **Blizzard_OrderHallUI**: `OpenOrderHallTalentUI(garrisonType)`
- **Blizzard_PVPUI**: `PVPUI_LoadUI()`
- **Blizzard_PartyPoseUI**: `IslandsPartyPoseFrame_TryShow(mapID, winner)`, `WarfrontsPartyPoseFrame_TryShow(mapID, winner)`
- **Blizzard_PerksProgram**: `ShowPerksProgramFrame()`
- **Blizzard_PhotoSharing**: `PhotoSharingFrame_EscapePressed()`
- **Blizzard_PlayerChoice**: `PlayerChoiceFrame_TryShow()`, `ShowPendingPlayerChoiceResponseUI()`
- **Blizzard_PlayerSpells**: `OpenPlayerSpellsToGlyphTarget(event, ...)`
- **Blizzard_Professions**: `ShowProfessionEquipmentHelpTip(skillLineID)`, `ShowProfessionsFrame()`
- **Blizzard_ProfessionsCustomerOrders**: `HideProfessionsCustomerOrdersFrame()`, `ShowProfessionsCustomerOrdersFrame()`
- **Blizzard_RaidUI**: `RaidFrameReadyCheckButton_Update()`, `RaidPulloutFrameTemplate_CreateContextMenu(self)`
- **Blizzard_ReforgingUI**: `HideReforgingFrame()`, `ShowReforgingFrame()`
- **Blizzard_RemixArtifactUI**: `ShowRemixArtifactFrame()`
- **Blizzard_ReportFrame**: `ReportFrame_EscapePressed()`
- **Blizzard_RuneforgeUI**: `ShowRuneforgeFrame(isUpgrade)`
- **Blizzard_SettingsDefinitions_Frame**: `IsMouseoverCastSupported()`
- **Blizzard_Settings_Shared**: `SettingsPanel_EscapePressed()`
- **Blizzard_SharedXML**: `BNet_GetBattleTagComponents(battleTag)`, `BNet_GetBattleTagSelf()`, `BNet_GetBroadcastTextSelf()`, `BNet_GetFriendLevelRank(friendLevel)`, `BNet_IsFriendLevelEqualOrHigher(friendLevel, comparisonLevel)`, `InputBoxInstructions_OnEnter(self)`, `InputBoxInstructions_OnLeave(self)`, `InputBoxInstructions_ShowTooltipIfTruncated(self)`, `LoadAddOnWithErrorHandling(name)`
- **Blizzard_SharedXMLBase**: `ApplySecureDelegatesToTable(tbl)`
- **Blizzard_SimpleCheckout**: `SimpleCheckout_EscapePressed()`
- **Blizzard_SocialUI**: `RecruitAFriendFrameSocialInitializeAADC(tabData)`
- **Blizzard_SocialUIShared**: `SocialUIContactsFrameInitializeAADC(tabData)`, `ToggleSocialUI()`
- **Blizzard_Soulbinds**: `SoulbindViewer_LoadUI()`
- **Blizzard_SplashFrame**: `SplashFrame_EscapePressed()`
- **Blizzard_StaticPopup_Game**: `ConfirmDisenchantRollDialog_Show(rollID, rollType)`, `ConfirmLootRollDialog_Show(rollID, rollType)`, `ConfirmTalentWipeDialog_Show(cost, talentType)`, `GossipConfirmDialog_Show(optionID, text, cost)`, `HideInstanceBootDialog()`, `HideInstanceLockDialog()`, `HideSummonConfirmationDialogs()`, `IsSummonConfirmationDialogVisible()`, `ShowInstanceBootDialog()`, `ShowInstanceLockDialog(enforceTime)`, `ShowSummonConfirmationDialog(summonReason, skipStartingArea)`, `UpdateQuestAcceptLogFullDialog()`
- **Blizzard_StoreUI**: `CheckActiveStoreForFree(event)`, `StoreEscapePressed()`
- **Blizzard_TrainerUI**: `ClassTrainerCollapseAllButton_OnClick(self)`, `ClassTrainer_HideSkillDetails()`, `ClassTrainer_SelectFirstLearnableSkill()`, `ClassTrainer_SetSubTextColor(button, r, g, b)`, `ClassTrainer_SetToClassTrainer()`, `ClassTrainer_SetToTradeSkillTrainer()`, `ClassTrainer_ShowSkillDetails()`
- **Blizzard_UIPanels_Game**: `AddPlayerInteractionConditions(interactionType, conditions)`, `GetDiscordUserCommunityLink(linkDisplayText, bnetIDAccount, discordUserID, clubId, streamId, epoch, position)`, `GetDiscordUserLink(linkDisplayText, bnetIDAccount, discordUserID, lineID, chatGroup, chatTarget)`, `HideGossipFrame()`, `LootFrame_EscapePressed()`, `RegisterPlayerInteraction(interactionType, frameInfo)`, `ShowTaxiMapFrame()`
- **Blizzard_UIParentPanelManager**: `GetUIPanelLayoutAttribute(name)`, `GetUIPanelLayoutFrame()`, `ManageFramePositions()`, `SetUIPanelLayoutAttribute(name, value)`
- **Blizzard_UnitFrame**: `CompactUnitFrameLayoutTemplates_LayoutFrameElement(frame, element, templateType, containerTypeKey)`, `LocalizePlayerFrame_zhCN()`, `LocalizePlayerFrame_zhTW()`
- **Blizzard_VisualAlerts**: `VisualAlertData_ForEach(callback)`, `VisualAlert_GetTypeTemplate(visualAlertType)`, `VisualAlert_GetTypeText(visualAlertType)`, `VisualAlerts_RegisterAll(manager)`
- **Blizzard_WowSurveyUI**: `AddWowSurveyStatusFrameToStatusFrames(statusFrames)`, `WowSurveyStatusFrame_OnSurveyDelivered(event)`

**Removed:**

- **Blizzard_Calendar**: `CloseCalendarMenus()`
- **Blizzard_FrameXMLBase**: `AddFrameLock(lock)`, `IsFrameLockActive(lock)`, `IsFrameSmartShown(frame)`, `RegisterNewFrameLock(tag, customFrameLock, includeHideMost)`, `RemoveFrameLock(lock)`, `SetFrameLock(lock, enabled)`, `SmartHide(frame)`, `SmartShow(frame)`, `UpdateFrameLock(frame)`
- **Blizzard_FrameXMLUtil**: `RaidBossEmoteFrame_OnEvent(self, event, ...)`, `RaidBossEmoteFrame_OnLoad(self)`, `RaidNotice_ClearSlot(slotFrame)`, `RaidNotice_OnUpdate(noticeFrame, elapsedTime)`, `RaidNotice_SetSlot(slotFrame, textString, colorInfo, minHeight, displayTime)`, `RaidWarningFrame_OnEvent(self, event, message)`, `RaidWarningFrame_OnLoad(self)`
- **Blizzard_FriendsFrame**: `BattleTagInviteFrame_Show(name)`, `FriendsFrameAddFriendButton_OnClick(self)`, `FriendsFrame_CloseQuickJoinHelpTip()`, `FriendsFriendsButton_SetSelected(button, selected)`, `FriendsFriendsFrame_Close()`, `FriendsFriends_InitButton(button, elementData)`, `FriendsFriends_SetSelection(friendID)`, `ToggleRafPanel()`
- **Blizzard_GlueXML**: `RealmListTab_OnClick(tab)`, `RealmList_ClickButton(self, doubleClick)`, `RealmSelectButton_OnClick(self)`, `RealmSelectButton_OnDoubleClick(self)`
- **Blizzard_QuickJoin**: `QuickJoin_JoinQueueButtonOnClick(self)`
- **Blizzard_TrainerUI**: `ClassTrainerFrame_Hide()`, `ClassTrainerFrame_Show()`
- **Blizzard_Transmog**: `DisplayTypeUnassignedSupported()`, `HelpPlatesSupported()`
- **Blizzard_UIParent**: `AnimateTexCoords(texture, textureWidth, textureHeight, frameWidth, frameHeight, numFrames, elapsed, throttle)`, `AnimatedShine_OnUpdate(elapsed)`, `Arena_LoadUI()`, `AuctionFrame_LoadUI()`, `BFAMissionFrame_EscapePressed()`, `BetterDate(formatString, timeVal)`, `BoostTutorial_AttemptLoad()`, `BuildColoredListString(...)`, `BuildIconArray(parent, baseName, template, rowSize, numRows, onButtonCreated)`, `BuildListString(...)`, `BuildMultilineTooltip(globalStringName, tooltip, r, g, b)`, `BuildNewLineListString(...)`, `ButtonPulse_OnUpdate(elapsed)`, `CanGroupInvite()`, `CommunitiesFrame_IsEnabled()`, `ConvertRGBtoColorString(color)`, `CraftFrame_LoadUI()`, `ExpansionTrial_CheckLoadUI()`, `GetBindingFromClick(input)`, `GetDungeonNameWithDifficulty(name, difficultyName)`, `GetNotchHeight()`, `GetScaledCursorPositionForFrame(frame)`, `GetScreenHeightScale()`, `GetScreenWidthScale()`, `GetSmoothProgressChange(value, displayedValue, range, elapsed, minPerSecond, maxPerSecond)`, `GetSocialColoredName(displayName, guid)`, `GetSortedSelfResurrectOptions()`, `GetUIParentOffset()`, `GlyphFrame_LoadUI()`, `InviteToGroup(name)`, `IsLevelAtEffectiveMaxLevel(level)`, `IsPlayerAtEffectiveMaxLevel()`, `KeyBindingFrame_LoadUI()`, `LocalizePlayerFrame(offsXVehicle, offsYVehicle, offsX, offsY)`, `LocalizezhCN()`, `LocalizezhTW()`, `MajorFactions_LoadUI()`, `MouseIsOver(region, topOffset, bottomOffset, leftOffset, rightOffset)`, `NPETutorial_AttemptToBegin(event)`, `NPE_CheckTutorials()`, `OpenAchievementFrameToAchievement(achievementID)`, `OrderHallMissionFrame_EscapePressed()`, `OrderHallTalentFrame_EscapePressed()`, `OutfitterUI_LoadUI()`, `QuestChoice_LoadUI()`, `RaidBrowser_IsEmpowered()`, `RealPartyIsFull()`, `RecentTimeDate(year, month, day, hour)`, `RefreshAuras(frame, unit, numAuras, suffix, checkCVar, showBuffs)`, `ReverseQuestObjective(text, objectiveType)`, `SetDesaturation(texture, desaturation)`, `ShowResurrectRequest(offerer)`, `ToggleLFGFrame()`, `ToggleRaidBrowser()`, `ToggleWoWHackCharacterUI()`, `TokenFrame_LoadUI()`, `TradeSkillFrame_LoadUI()`, `TrialAccountCapReached_Inform(capType)`, `UIDoFramesIntersect(frame1, frame2)`, `UIParentLoadAddOn(name)`, `UIParent_OnEvent(self, event, ...)`, `UIParent_OnHide(self)`, `UIParent_OnLoad(self)`, `UIParent_OnShow(self)`, `UIParent_OnUpdate(self, elapsed)`, `UIParent_Shared_OnEvent(self, event, ...)`, `UIParent_Shared_OnLoad(self)`, `UIParent_UpdateTopFramePositions()`, `UnitHasMana(unit)`, `UpdateUIElementsForClientScene(sceneType)`, `WoWHackSpellsUI_LoadUI()`, `WorldFrame_OnLoad(self)`, `WorldFrame_OnUpdate(self, elapsed)`
- **Blizzard_UIParentPanelManager**: `UIParent_ManageFramePositions()`
- **Blizzard_UnitFrame**: `CompactUnitFrame_GetOptionDisplayOnlyHealerPowerBars(frame, options)`, `CompactUnitFrame_GetOptionDisplayPowerBar(frame, options)`

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

