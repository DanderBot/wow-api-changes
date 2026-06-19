# UI Building Blocks

The reusable building blocks addons can consume — **intrinsic widget types, virtual XML templates, Lua mixins, and Blizzard addons** — none of which appear in the generated API documentation. This is the layer the per-namespace API pages can't see (it's where the new `AuraContainer` / `AuraButton` live, for example).

!!! note "How to read this"
    Items are grouped by the addon that defines them. The diff is keyed by **name**, so something that merely *moved* between addons isn't flagged — only genuinely new or removed names are. Several "new addons" are **modularization splits** (Blizzard breaking previously-inline FrameXML into small standalone addons), not new features.

## Addons

**New addons (29):**

- `Blizzard_AnimatedShine`
- `Blizzard_AuraContainer`
- `Blizzard_ButtonPulse`
- `Blizzard_ChatBubble`
- `Blizzard_ClientSceneVisManager`
- `Blizzard_ColorPickerFrame`
- `Blizzard_DebugUtil`
- `Blizzard_DeprecatedHousing`
- `Blizzard_DeprecatedRaidWarning`
- `Blizzard_Game`
- `Blizzard_GameMenuEsc`
- `Blizzard_HardcoreUI`
- `Blizzard_HousingBlueprint`
- `Blizzard_LFGUtil`
- `Blizzard_ManagedFrameSystem`
- `Blizzard_Narration`
- `Blizzard_Plunderstorm`
- `Blizzard_ProjectConstants`
- `Blizzard_RaidWarning`
- `Blizzard_ShakeUtil`
- `Blizzard_SocialUI`
- `Blizzard_SocialUIShared`
- `Blizzard_SplashFrame`
- `Blizzard_StatusTrayManager`
- `Blizzard_UIModes`
- `Blizzard_UIParentUtil`
- `Blizzard_VisualAlerts`
- `Deprecated_PaperDoll`
- `middleclass`

**Removed addons (1):**

- `Blizzard_DeprecatedHousingCatalog`

## Intrinsic widget types

**New widget types (2):**

- `AuraButton` � defined in `Blizzard_AuraContainer`
- `AuraContainer` � defined in `Blizzard_AuraContainer`

## Virtual templates  (new: 123, removed: 21)

**New templates by addon:**

- **Blizzard_AccessibilityTemplates**
    - `UserScaledButtonFitToTextTemplate` � type `Button`, inherits `UserScaledFrameTemplate, TruncatedTooltipScriptTemplate`, mixin `UserScaledButtonFitToTextMixin`
    - `UserScaledFrameByHeightTemplate` � type `Frame`, mixin `UserScaledFrameByHeightMixin`
- **Blizzard_AuraContainer**
    - `CustomAuraButtonTemplate` � type `AuraButton`
    - `CustomAuraContainerTemplate` � type `AuraContainer`
- **Blizzard_CharacterCustomize**
    - `CharCustomizeAlteredFormDropdownItemIconTemplate` � type `Frame`, mixin `CharCustomizeAlteredFormDropdownItemIconMixin`
    - `CharCustomizeAlteredFormDropdownItemTemplate` � type `Button`, mixin `CharCustomizeAlteredFormDropdownItemMixin`
    - `CharCustomizeAlteredFormsDropdownTemplate` � type `DropdownButton`, mixin `CharCustomizeAlteredFormsDropdownMixin`
- **Blizzard_ChatFrame**
    - `ChatConfigAdditionalColorSwatchTemplate` � type `Frame`, inherits `ChatConfigBorderBoxTemplate`
- **Blizzard_CooldownViewer**
    - `CooldownViewerDraggedItemBaseTemplate` � type `Frame`, mixin `CooldownViewerDraggedItemBaseMixin`
    - `CooldownViewerEditAlertBaseTemplate` � type `Frame`, mixin `CooldownViewerEditAlertBaseMixin`
    - `GroupBuffFilterItemTemplate` � type `Frame`, mixin `GroupBuffFilterItemMixin`
    - `GroupBuffFilterSectionTemplate` � type `Frame`, inherits `ResizeLayoutFrame`, mixin `GroupBuffFilterSectionMixin`
    - `GroupBuffFilterTemplate` � type `Frame`, mixin `GroupBuffFilterMixin`
- **Blizzard_EditMode**
    - `EditModeRaidWarningSystemTemplate` � type `Frame`, inherits `EditModeSystemTemplate`, mixin `EditModeRaidWarningSystemMixin`
- **Blizzard_Fonts_Shared**
    - `EditBoxFont_25` � type `FontFamily`
    - `GlueFontDisableLogin` � type `Font`, inherits `GlueFontNormalLogin`
    - `GlueFontHighlightLogin` � type `Font`, inherits `GlueFontNormalLogin`
    - `GlueFontNormalLogin` � type `Font`, inherits `SystemFont_Shadow_Outline_Login`
    - `GlueLoginEditBoxFont` � type `Font`, inherits `EditBoxFont_25`
    - `NumberFont_Outline_Large2` � type `FontFamily`
    - `System15Font_Shadow` � type `FontFamily`
    - `SystemFont_NamePlateLevel` � type `FontFamily`
    - `SystemFont_Shadow_Outline_Login` � type `FontFamily`
    - `UserScaledFontGame15Shadow` � type `Font`, inherits `Game15Font_Shadow`
    - `UserScaledFontSystem15Shadow` � type `Font`, inherits `System15Font_Shadow`
- **Blizzard_FriendsFrame**
    - `FriendRequestsListRealIDWarningTemplate` � type `Frame`, mixin `FriendRequestsListRealIDWarningMixin`
    - `FriendRequestsListSocialCardAcceptButtonTemplate` � type `Button`, inherits `UserScaledFrameTemplate`, mixin `FriendRequestsListSocialCardAcceptButtonMixin`
    - `FriendRequestsListSocialCardDeclineButtonTemplate` � type `DropdownButton`, inherits `UserScaledFrameTemplate`, mixin `FriendRequestsListSocialCardDeclineButtonMixin`
    - `FriendRequestsListSocialCardTemplate` � type `Button`, mixin `FriendRequestsListSocialCardMixin`
    - `FriendRequestsListSocialViewTemplate` � type `Frame`, inherits `SocialUIContactsFrameTemplate`, mixin `FriendRequestsListSocialViewMixin`
    - `FriendsListSocialCardFavoriteDisplayTemplate` � type `Frame`, inherits `UserScaledFrameTemplate`, mixin `FriendsListSocialCardFavoriteDisplayMixin`
    - `FriendsListSocialCardGameIconHolderTemplate` � type `Frame`
    - `FriendsListSocialCardPartyButtonTemplate` � type `Button`, inherits `SocialCardActionButtonTemplate`, mixin `FriendsListSocialCardPartyButtonMixin`
    - `FriendsListSocialCardRAFSummonButtonTemplate` � type `Button`, inherits `SocialCardActionButtonTemplate`, mixin `FriendsListSocialCardRAFSummonButtonMixin`
    - `FriendsListSocialCardStateDisplayTemplate` � type `Frame`, inherits `UserScaledFrameTemplate`, mixin `FriendsListSocialCardStateDisplayMixin`
    - `FriendsListSocialCardTemplate` � type `Button`, mixin `FriendsListSocialCardMixin`
    - `FriendsListSocialViewTemplate` � type `Frame`, inherits `SocialUIContactsFrameTemplate`, mixin `FriendsListSocialViewMixin`
- **Blizzard_GuildBankUI**
    - `GuildBankPopupButtonTemplate` � type `CheckButton`, inherits `PopupButtonTemplate`, mixin `GuildBankPopupButtonMixin`
- **Blizzard_GuildControlUI**
    - `DiscordLinkedTemplate` � type `Frame`
    - `DiscordUnlinkedTemplate` � type `Frame`
- **Blizzard_HouseEditor**
    - `CustomizeDecorPetFrameTemplate` � type `Frame`, mixin `CustomizeDecorPetFrameMixin`
    - `DecorCustomizationsPaneTemplate` � type `Frame`, inherits `ResizeLayoutFrame`, mixin `DecorCustomizationsPaneMixin`
    - `DecorPetCustomizationTemplate` � type `Frame`, mixin `DecorPetCustomizationMixin`
    - `HouseEditorPetCountTemplate` � type `Frame`, inherits `HouseEditorBudgetCountTemplate`, mixin `HouseEditorPetCountMixin`
    - `HousingPetEntryTemplate` � type `Button`, mixin `HousingPetEntryMixin`
- **Blizzard_HousingBlueprint**
    - `HousingBlueprintBaseFrameTemplate` � type `Frame`, mixin `HousingBlueprintBaseFrameMixin`
    - `HousingBlueprintBudgetTemplate` � type `Frame`, inherits `ResizeLayoutFrame`, mixin `HousingBlueprintBudgetMixin`
    - `HousingBlueprintCollectionEntryTemplate` � type `Button`, mixin `HousingBlueprintCollectionEntryMixin`
    - `HousingBlueprintCollectionGroupTemplate` � type `Frame`, mixin `HousingBlueprintCollectionGroupMixin`
    - `HousingBlueprintCollectionTemplate` � type `Frame`, mixin `HousingBlueprintCollectionMixin`
    - `HousingBlueprintContentEntryTemplate` � type `Button`, mixin `HousingBlueprintContentEntryMixin`
    - `HousingBlueprintContentGroupTemplate` � type `EventFrame`, mixin `HousingBlueprintContentGroupMixin`
    - `HousingBlueprintExportContentTemplate` � type `Frame`
    - `HousingBlueprintImportContentTemplate` � type `Frame`
- **Blizzard_HousingControls**
    - `HousingBlueprintActionButtonTemplate` � type `Button`, inherits `HousingControlActionButtonTemplate`, mixin `HousingBlueprintActionButtonMixin`
- **Blizzard_ManagedFrameSystem**
    - `BottomManagedFrameTemplate` � type `Frame`, inherits `ManagedFrameTemplate`
    - `ManagedFrameContainer` � type `Frame`, inherits `ManagedFrameContainerBaseTemplate`
    - `ManagedFrameContainerBaseTemplate` � type `Frame`, inherits `VerticalLayoutFrame`, mixin `ManagedFrameContainerMixin`
    - `ManagedFrameTemplate` � type `Frame`, mixin `ManagedFrameMixin`
    - `RightManagedFrameTemplate` � type `Frame`, inherits `ManagedFrameTemplate`
- **Blizzard_Menu**
    - `WowMenuDropdownHighlightButtonTemplate` � type `Button`, inherits `DarkMenuElementTemplate`
- **Blizzard_NamePlates**
    - `NamePlateCastingBarTemplate` � type `StatusBar`, inherits `CastingBarFrameAnimsTemplate`, mixin `NamePlateCastingBarMixin`
- **Blizzard_PingUI**
    - `UnitPingIconFrameTemplate` � type `Frame`, mixin `UnitPingIconFrameMixin`
- **Blizzard_QuickJoin**
    - `QuickJoinFrameSocialTemplate` � type `Frame`, inherits `CallbackRegistrantTemplate`, mixin `QuickJoinFrameSocialMixin`
- **Blizzard_RaidWarning**
    - `RaidWarningFrameTemplate` � type `Frame`, mixin `RaidWarningFrameMixin`
- **Blizzard_RecentAllies**
    - `RecentAlliesCardStateDisplayTemplate` � type `Frame`, inherits `UserScaledFrameTemplate`, mixin `RecentAlliesCardStateDisplayMixin`
    - `RecentAlliesSocialCardFriendRequestSentDisplayTemplate` � type `Frame`, inherits `UserScaledFrameTemplate`, mixin `RecentAlliesSocialCardFriendRequestSentDisplayMixin`
    - `RecentAlliesSocialCardPartyButtonTemplate` � type `Button`, inherits `SocialCardActionButtonTemplate`, mixin `RecentAlliesSocialCardPartyButtonMixin`
    - `RecentAlliesSocialCardPinDisplayTemplate` � type `Frame`, inherits `UserScaledFrameTemplate`, mixin `RecentAlliesSocialCardPinDisplayMixin`
    - `RecentAlliesSocialCardTemplate` � type `Button`, mixin `RecentAlliesSocialCardMixin`
    - `RecentAlliesSocialViewTemplate` � type `Frame`, inherits `SocialUIContactsFrameTemplate`, mixin `RecentAlliesSocialViewMixin`
- **Blizzard_RecruitAFriend**
    - `RewardClaimingTemplate` � type `Frame`, mixin `RewardClaimingMixin`
- **Blizzard_SharedXML**
    - `NarratableTooltipTemplate` � type `Frame`, mixin `NarratableTooltipMixin`
    - `PingableActionButtonTemplate` � type `Frame`, inherits `PingReceiverAttributeTemplate`, mixin `PingableType_ActionButtonMixin`
    - `PingableCooldownViewerItemTemplate` � type `Frame`, inherits `PingReceiverAttributeTemplate`, mixin `PingableType_CooldownViewerItemMixin`
- **Blizzard_SocialUI**
    - `RaidFrameSocialClassTypeTemplate` � type `Frame`, mixin `RaidFrameSocialClassTypeMixin`
    - `RaidFrameSocialGroupTemplate` � type `Frame`, mixin `RaidFrameSocialGroupMixin`
    - `RaidFrameSocialPlayerTemplate` � type `Button`, inherits `UIButtonTemplate`, mixin `RaidFrameSocialPlayerMixin`
    - `RaidFrameSocialTemplate` � type `Frame`, inherits `CallbackRegistrantTemplate`, mixin `RaidFrameSocialMixin`
    - `RecruitAFriendFrameSocialTemplate` � type `Frame`, inherits `CallbackRegistrantTemplate`, mixin `RecruitAFriendFrameSocialMixin`
    - `RecruitActivityButtonSocialTemplate` � type `Button`, inherits `RecruitActivityButtonTemplate`
    - `RecruitListButtonSocialTemplate` � type `Button`, mixin `RecruitListButtonSocialMixin`
    - `RewardClaimingSocialTemplate` � type `Frame`, inherits `UserScaledFrameByHeightTemplate`, mixin `RewardClaimingMixin`
    - `SocialUIBattleNetBarTemplate` � type `Frame`
    - `SocialUIBattleNetBroadcastFrameTemplate` � type `Frame`, inherits `ResizeLayoutFrame`, mixin `SocialUIBattleNetBroadcastFrameMixin, SocialUISystemMixin`
    - `SocialUIBattleNetControlsContainerTemplate` � type `Frame`, mixin `SocialUIBattleNetControlsContainerMixin`
    - `SocialUIBattleNetMenuButtonTemplate` � type `DropdownButton`, mixin `SocialUIBattleNetMenuButtonMixin`
    - `SocialUIBattleNetUnavailableNoticeButtonTemplate` � type `Button`, inherits `UIPanelInfoButton`, mixin `SocialUIBattleNetUnavailableNoticeButtonMixin`
    - `SocialUIBattleNetUnavailableNoticeFrameTemplate` � type `Frame`, inherits `ResizeLayoutFrame`, mixin `SocialUIBattleNetUnavailableNoticeFrameMixin`
    - `SocialUICopyBattleTagToClipboardButtonTemplate` � type `Button`, mixin `SocialUICopyBattleTagToClipboardButtonMixin`
    - `SocialUIIgnoreListEntryTemplate` � type `Button`, mixin `SocialUIIgnoreListEntryMixin`
    - `SocialUIIgnoreListFrameTemplate` � type `Frame`, inherits `ButtonFrameTemplate, UserScaledFrameTemplate`, mixin `SocialUIIgnoreListMixin, SocialUISystemMixin`
    - `SocialUIIgnoreListHeaderTemplate` � type `Frame`, mixin `SocialUIIgnoreListHeaderMixin`
    - `SocialUIOnlineStatusDropdownTemplate` � type `DropdownButton`, inherits `WowStyle1DropdownTemplate`, mixin `SocialUIOnlineStatusDropdownMixin`
    - `SocialUIPersonalBattleTagDisplayTemplate` � type `Frame`, mixin `SocialUIPersonalBattleTagDisplayMixin`
    - `SocialUIRaidInfoContentFrameTemplate` � type `Button`, mixin `SocialUIRaidInfoContentFrameMixin`
    - `SocialUIRaidInfoFrameTemplate` � type `Frame`, mixin `SocialUIRaidInfoFrameMixin, SocialUISystemMixin`
    - `SocialUITabTemplate` � type `Button`, inherits `LargeSideTabButtonTemplate`, mixin `SocialUITabMixin`
- **Blizzard_SocialUIShared**
    - `SocialCardActionButtonTemplate` � type `Button`, mixin `SocialCardActionButtonMixin`
    - `SocialCardPresenceHolderTemplate` � type `Frame`, inherits `UserScaledFrameTemplate`, mixin `SocialCardPresenceHolderMixin`
    - `SocialUIActionButtonTemplate` � type `Button`, inherits `UserScaledButtonFitToTextTemplate, SharedButtonTemplate`
    - `SocialUIContactsFrameTemplate` � type `Frame`, mixin `SocialUIContactsFrameMixin`
    - `SocialUIFilterBarTemplate` � type `Frame`
    - `SocialUIScrollableHeaderTemplate` � type `Button`, inherits `ListHeaderVisualTemplate, ListHeaderCodeTemplate, UserScaledFrameTemplate`, mixin `SocialUIScrollableHeaderMixin`
    - `SocialUIScrollableSpacerTemplate` � type `Frame`, mixin `SocialUIScrollableSpacerMixin`
    - `SocialUISearchBoxTemplate` � type `EditBox`, inherits `SearchBoxNineSliceTemplate, UserScaledFrameTemplate`, mixin `SocialUISearchBoxMixin`
    - `SocialUISearchFilterDropdownTemplate` � type `DropdownButton`, inherits `WowStyle1FilterDropdownTemplate, UserScaledFrameTemplate`, mixin `SocialUIOnlineSearchFilterDropdownMixin`
- **Blizzard_UnitFrame**
    - `CompactUnitFrameContainerTemplate` � type `Frame`, inherits `GridLayoutFrame`, mixin `CompactUnitFrameContainerMixin`
    - `ContainedCompactUnitFrameTemplate` � type `Button`, inherits `CompactUnitFrameTemplate`
    - `PlayerBottomManagedFrameTemplate` � type `Frame`, inherits `ManagedFrameTemplate`
    - `PlayerManagedContainerTemplate` � type `Frame`, inherits `VerticalLayoutFrame`, mixin `ManagedFrameContainerMixin`
- **Blizzard_VisualAlerts**
    - `VisualAlertBaseTemplate` � type `Frame`, inherits `AnimateWhileShownTemplate`, mixin `VisualAlertBaseMixin`
    - `VisualAlertFlashBaseTemplate` � type `Frame`, inherits `VisualAlertBaseTemplate`, mixin `VisualAlertFlashBaseMixin`
    - `VisualAlertFlashBlueTemplate` � type `Frame`, inherits `VisualAlertFlashBaseTemplate`
    - `VisualAlertFlashCyanTemplate` � type `Frame`, inherits `VisualAlertFlashBaseTemplate`
    - `VisualAlertFlashGreenTemplate` � type `Frame`, inherits `VisualAlertFlashBaseTemplate`
    - `VisualAlertFlashRedTemplate` � type `Frame`, inherits `VisualAlertFlashBaseTemplate`
    - `VisualAlertMarchingAntsBaseTemplate` � type `Frame`, inherits `VisualAlertBaseTemplate`, mixin `VisualAlertMarchingAntsBaseMixin`
    - `VisualAlertMarchingAntsBlueTemplate` � type `Frame`, inherits `VisualAlertMarchingAntsBaseTemplate`
    - `VisualAlertMarchingAntsCyanTemplate` � type `Frame`, inherits `VisualAlertMarchingAntsBaseTemplate`
    - `VisualAlertMarchingAntsGreenTemplate` � type `Frame`, inherits `VisualAlertMarchingAntsBaseTemplate`
    - `VisualAlertMarchingAntsRedTemplate` � type `Frame`, inherits `VisualAlertMarchingAntsBaseTemplate`
    - `VisualAlertsManagerTemplate` � type `Frame`, mixin `VisualAlertsManagerMixin`

**Removed templates:**

- `CDMVISBaseTemplate` (was in `Blizzard_CooldownViewer`)
- `CDMVISFlashBase` (was in `Blizzard_CooldownViewer`)
- `CDMVISFlashBlue` (was in `Blizzard_CooldownViewer`)
- `CDMVISFlashCyan` (was in `Blizzard_CooldownViewer`)
- `CDMVISFlashGreen` (was in `Blizzard_CooldownViewer`)
- `CDMVISFlashRed` (was in `Blizzard_CooldownViewer`)
- `CDMVISMarchingAntsBase` (was in `Blizzard_CooldownViewer`)
- `CDMVISMarchingAntsBlue` (was in `Blizzard_CooldownViewer`)
- `CDMVISMarchingAntsCyan` (was in `Blizzard_CooldownViewer`)
- `CDMVISMarchingAntsGreen` (was in `Blizzard_CooldownViewer`)
- `CDMVISMarchingAntsRed` (was in `Blizzard_CooldownViewer`)
- `CooldownViewerSettingsDraggedItemTemplate` (was in `Blizzard_CooldownViewer`)
- `HousingDashboardSideTabTemplate` (was in `Blizzard_HousingDashboard`)
- `PlayerFrameBottomManagedFrameTemplate` (was in `Blizzard_UnitFrame`)
- `PlayerFrameManagedContainerTemplate` (was in `Blizzard_UnitFrame`)
- `RaidBossEmoteFrameTemplate` (was in `Blizzard_FrameXML`)
- `UIParentBottomManagedFrameTemplate` (was in `Blizzard_UIParent`)
- `UIParentManagedFrameContainer` (was in `Blizzard_UIParent`)
- `UIParentManagedFrameTemplate` (was in `Blizzard_UIParent`)
- `UIParentRightManagedFrameTemplate` (was in `Blizzard_UIParent`)
- `WowMenuDropdownHighlightRadioTemplate` (was in `Blizzard_Menu`)

## Lua mixins  (new: 169, removed: 11)

**New mixins by addon:**

- **Blizzard_AccessibilityTemplates**: `UserScaledButtonFitToTextMixin`, `UserScaledFrameByHeightMixin`
- **Blizzard_ActionBar**: `BaseActionButtonInfoMixin`
- **Blizzard_CharacterCustomize**: `CharCustomizeAlteredFormDropdownItemIconMixin`, `CharCustomizeAlteredFormDropdownItemMixin`, `CharCustomizeAlteredFormsDropdownMixin`
- **Blizzard_ClientSceneVisManager**: `ClientSceneVisManagerMixin`
- **Blizzard_CooldownViewer**: `CooldownViewerDraggedItemBaseMixin`, `CooldownViewerEditAlertBaseMixin`, `GroupBuffFilterEditVisualAlertMixin`, `GroupBuffFilterItemMixin`, `GroupBuffFilterMixin`, `GroupBuffFilterSectionMixin`
- **Blizzard_EditMode**: `EditModeRaidWarningSystemMixin`
- **Blizzard_FrameXMLUtil**: `GroupBuffMixin`
- **Blizzard_FriendsFrame**: `BattleNetInviteFrameMixin`, `FriendRequestsListRealIDWarningMixin`, `FriendRequestsListSocialCardAcceptButtonMixin`, `FriendRequestsListSocialCardDeclineButtonMixin`, `FriendRequestsListSocialCardMixin`, `FriendRequestsListSocialViewMixin`, `FriendsFrameAddFriendButtonMixin`, `FriendsFriendsWaitFrameMixin`, `FriendsListSocialCardFavoriteDisplayMixin`, `FriendsListSocialCardMixin`, `FriendsListSocialCardPartyButtonMixin`, `FriendsListSocialCardRAFSummonButtonMixin`, `FriendsListSocialCardStateDisplayMixin`, `FriendsListSocialViewMixin`
- **Blizzard_GlueXML**: `AccountLoginEditBoxMixin`, `AccountLoginMenuButtonMixin`, `CharSelectEnterWorldButtonMixin`, `CharacterSelectAddGroupButtonMixin`, `CharacterSelectBackToActiveButtonMixin`, `CharacterSelectCreateCharacterButtonMixin`, `CharacterSelectDeleteCharacterButtonMixin`, `CharacterSelectRotateButtonMixin`, `CharacterSelectUndeleteButtonMixin`, `CharacterSelectVisibilityToggleButtonMixin`, `RealmListRealmButtonMixin`, `RealmListSortButtonMixin`, `RealmListTabButtonMixin`
- **Blizzard_GuildBankUI**: `GuildBankPopupButtonMixin`, `GuildBankPopupCancelButtonMixin`, `GuildBankPopupEditBoxMixin`, `GuildBankPopupOkayButtonMixin`, `GuildItemSearchBoxMixin`
- **Blizzard_HouseEditor**: `CustomizeDecorPetFrameMixin`, `DecorCustomizationsPaneMixin`, `DecorPetCustomizationMixin`, `HouseEditorPetCountMixin`, `HousingPetEntryMixin`, `PetCustomizationsPaneExpandButtonMixin`
- **Blizzard_HousingBlueprint**: `HousingBlueprintBaseFrameMixin`, `HousingBlueprintBudgetMixin`, `HousingBlueprintCollectionEntryMixin`, `HousingBlueprintCollectionGroupMixin`, `HousingBlueprintCollectionMixin`, `HousingBlueprintContentEntryMixin`, `HousingBlueprintContentGroupMixin`, `HousingBlueprintContentListFrameMixin`, `HousingBlueprintExportFrameMixin`, `HousingBlueprintExportInputContentMixin`, `HousingBlueprintExportSuccessContentMixin`, `HousingBlueprintImportFrameMixin`, `HousingBlueprintImportInputContentMixin`, `HousingBlueprintImportLoadingFrameMixin`, `HousingBlueprintImportValidationContentMixin`, `HousingBlueprintRenameFrameMixin`
- **Blizzard_HousingControls**: `HousingBlueprintActionButtonMixin`, `HousingOwnerControlsLayoutMixin`, `HousingVisitorControlsLayoutMixin`
- **Blizzard_HousingHouseFinder**: `IgnoreNeighborhoodButtonMixin`
- **Blizzard_HousingTutorials**: `HousePetBedTutorialMixin`
- **Blizzard_ManagedFrameSystem**: `ManagedFrameContainerMixin`, `ManagedFrameMixin`
- **Blizzard_Narration**: `NarrationEditBoxMixin`, `NarrationForwardDescriptionToParentMixin`, `NarrationForwardNameToParentMixin`, `NarrationForwardToParentMixin`, `NarrationHTMLMixin`, `NarrationManagerMixin`, `NarrationSearchBoxMixin`, `NarrationSkipTooltipsMixin`, `NarrationSliderMixin`, `NarrationSourceMouseMixin`, `NarrationStaticDescriptionMixin`, `NarrationStaticNameMixin`
- **Blizzard_PingUI**: `UnitPingIconFrameMixin`
- **Blizzard_PrivateAurasUI**: `PrivateRaidBossEmoteFrameMixin`
- **Blizzard_QuickJoin**: `JoinQueueButtonMixin`, `QuickJoinFrameSocialMixin`
- **Blizzard_RaidWarning**: `GlobalRaidWarningFrameMixin`, `RaidWarningFrameMixin`
- **Blizzard_RecentAllies**: `RecentAlliesCardStateDisplayMixin`, `RecentAlliesSocialCardFriendRequestSentDisplayMixin`, `RecentAlliesSocialCardMixin`, `RecentAlliesSocialCardPartyButtonMixin`, `RecentAlliesSocialCardPinDisplayMixin`, `RecentAlliesSocialViewMixin`
- **Blizzard_RecruitAFriend**: `RewardClaimingMixin`
- **Blizzard_SettingsDefinitions_Shared**: `SettingsAdvancedControlNarrationMixin`, `SettingsTabNarrationMixin`
- **Blizzard_Settings_Shared**: `SettingsButtonNarrationContextMixin`, `SettingsCheckboxNarrationContextMixin`, `SettingsDropdownNarrationContextMixin`, `SettingsSliderNarrationContextMixin`
- **Blizzard_SharedXML**: `NarratableTooltipMixin`, `PingableType_ActionButtonMixin`, `PingableType_CooldownViewerItemMixin`, `PingableType_PlayerUnitFrameMixin`, `UIPanelCloseButtonNarrationMixin`
- **Blizzard_SocialUI**: `RaidFrameSocialAllAssistMixin`, `RaidFrameSocialClassTypeMixin`, `RaidFrameSocialGroupMixin`, `RaidFrameSocialMixin`, `RaidFrameSocialPlayerMixin`, `RecruitAFriendFrameSocialMixin`, `RecruitListButtonSocialMixin`, `SocialRaidInfoMixin`, `SocialUIBattleNetBroadcastEditBoxMixin`, `SocialUIBattleNetBroadcastFrameMixin`, `SocialUIBattleNetControlsContainerMixin`, `SocialUIBattleNetMenuButtonMixin`, `SocialUIBattleNetUnavailableNoticeButtonMixin`, `SocialUIBattleNetUnavailableNoticeFrameMixin`, `SocialUICopyBattleTagToClipboardButtonMixin`, `SocialUIFrameMixin`, `SocialUIIgnoreListEntryMixin`, `SocialUIIgnoreListHeaderMixin`, `SocialUIIgnoreListMixin`, `SocialUIOnlineStatusDropdownMixin`, `SocialUIPersonalBattleTagDisplayMixin`, `SocialUIRaidInfoContentFrameMixin`, `SocialUIRaidInfoExtendMixin`, `SocialUIRaidInfoFrameMixin`, `SocialUITabMixin`
- **Blizzard_SocialUIShared**: `SocialCardActionButtonMixin`, `SocialCardPresenceHolderMixin`, `SocialUIActionButtonMixin`, `SocialUIContactsFrameMixin`, `SocialUIOnlineSearchFilterDropdownMixin`, `SocialUIScrollableElementExtentPreviewerMixin`, `SocialUIScrollableHeaderMixin`, `SocialUIScrollableSpacerMixin`, `SocialUISearchBoxMixin`, `SocialUISystemMixin`
- **Blizzard_StaticPopup**: `StaticPopupDialogNarrationMixin`
- **Blizzard_UIModes**: `UIModeManagerMixin`
- **Blizzard_UIPanels_Game**: `PaperDollItemSlotButtonBaseMixin`
- **Blizzard_UnitFrame**: `CompactUnitFrameContainerMixin`, `PlayerBottomManagedFrameContainerMixin`, `TargetAuraFrameMixin`, `TargetBuffFrameMixin`, `TargetDebuffFrameMixin`, `TargetFrameInstanceMixin`, `TargetFramePrivateAuraAnchorMixin`
- **Blizzard_UnitPopup**: `UnitPopupBnetFriendTagButtonBaseMixin`, `UnitPopupBnetFriendTagInterestsSubsectionTitleMixin`, `UnitPopupBnetFriendTagRolesSubsectionTitleMixin`, `UnitPopupBnetFriendTagsButtonMixin`
- **Blizzard_UnitPopupShared**: `UnitPopupAddTitleFriendButtonMixin`, `UnitPopupDeleteDiscordMessageButtonMixin`
- **Blizzard_VisualAlerts**: `VisualAlertBaseMixin`, `VisualAlertFlashBaseMixin`, `VisualAlertMarchingAntsBaseMixin`, `VisualAlertMixin`, `VisualAlertTargetMixin`, `VisualAlertsManagerMixin`

**Removed mixins:**

`CDMVISBaseMixin`, `CDMVISFlashBaseMixin`, `CDMVISMarchingAntsBaseMixin`, `CooldownViewerSettingsDraggedItemMixin`, `CooldownViewerVisualAlertMixin`, `CooldownViewerVisualAlertsManagerMixin`, `PlayerFrameBottomManagedFramesContainerMixin`, `SpellBookCategoryTabMixin`, `UIParentManagedFrameContainerMixin`, `UIParentManagedFrameMixin`, `VisitorControlFrameMixin`


> Coverage note: 28 anonymous `virtual="true"` child elements (inline, referenced by `parentKey` rather than `name`) are excluded — they aren't inheritable templates, so this is not a coverage gap.
