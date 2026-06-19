# Social, Battle.net & Discord

This patch lands native Discord integration: guilds can link a Discord server channel directly into guild chat, and Discord presence surfaces in WoW's social UI. Alongside it, a broad social-systems reorganisation adds per-system enable/support queries, Battle.net friend "tags" and friend levels, and reveal flows for censored LFG listings.

## C_BattleNet (BattleNetDocumentation)

**New:**

- **`AreTitleFriendsEnabled() → enabled: bool`** — whether Title-level Battle.net friends are enabled.
- **`BNCheckBattleTagInviteToRecentAlly(recentAllyGUID: WOWGUID)`** — checks whether a BattleTag invite can be sent to a recent ally.
- **`BNCheckTitleFriendInviteToUnit(unit: UnitToken)`** — checks whether a Title-friend invite can be sent to a unit.
- **`GetFriendInviteInfo(inviteIndex: luaIndex) → inviteInfo: BNetFriendInviteInfo?`** — pending friend-invite info for an index.
- **`IsBattleNetFriendsListEnabled() → enabled: bool`** — whether the Battle.net friends list is enabled.
- **`IsBattleNetFriendsListSupported() → supported: bool`** — whether the Battle.net friends list is supported on this client.
- **`SendVerifiedBattleNetFriendInvite()`** — sends a verified Battle.net friend invite.
- **`SetFriendTags(id: number, friendTags: table)`** — sets the `BattleNetFriendTag` list for a friend.
- **`BNetFriendInviteInfo`** (struct) — a pending friend invite. Fields: `inviteID: number, accountName: kstringAuroraName, creationTimestamp: number, friendLevel: BattleNetFriendLevel?`.

## C_BattleNet (BattleNetSharedDocumentation) *(new namespace)*

**New:**

- **`BattleNetFriendLevel`** (enum) — relationship level. Values: `BattleTag, RealID, Title`.
- **`BattleNetFriendTag`** (enum) — interest/role tags. Values: `Professions, PvP, Raiding, Dungeons, Delves, Questing, Roleplaying, DamagerRole, HealerRole, TankRole`.

## FriendListDocumentation

**New:**

- **`BATTLE_NET_FRIEND_TAG_ENABLED_STATUS_UPDATED`** (event) — friend-tags enabled status changed. Payload: none.
- **`CONFIRM_BATTLE_NET_FRIEND_INVITE_SHOW`** (event) — prompt to confirm an incoming invite. Payload: `name: cstring, friendLevel: BattleNetFriendLevel`.
- **`SOCIAL_UI_FRIENDS_LIST_SYSTEM_STATUS_UPDATED`** (event) — friends-list system enable/support status changed. Payload: none.

**Removed:**

- **`BATTLETAG_INVITE_SHOW`** (event) — was the BattleTag invite prompt (payload `name: cstring`); replaced by `CONFIRM_BATTLE_NET_FRIEND_INVITE_SHOW`.

## C_SocialRestrictions (SocialRestrictionsDocumentation)

**New:**

- **`IsFriendsDisabled() → disabled: bool`** — whether the friends system is disabled (parental controls / restrictions).

## C_SocialUI (SocialUIDocumentation) *(new namespace)*

**New:**

- **`IsSystemEnabled() → enabled: bool`** — whether the social UI system is enabled.
- **`SOCIAL_UI_SYSTEM_STATUS_UPDATED`** (event) — social UI system status changed. Payload: none.
- **`SocialSystemType`** (enum) — Values: `Friends, QuickJoin, RaidList, RecruitAFriend, RecentAllies`.
- **`SocialUIBlockType`** (enum) — Values: `None, Ignore, BattleNetInviteBlock`.
- **`SocialUIPresenceType`** (enum) — Values: `Unknown, Online, Offline, Away, Busy, AppearOffline`.

## C_SocialQueue (SocialQueueSystemStatusDocumentation) *(new namespace)*

**New:**

- **`IsSystemEnabled() → enabled: bool`** — whether the social queue system is enabled.
- **`IsSystemSupported() → supported: bool`** — whether the social queue system is supported on this client.
- **`SOCIAL_UI_SOCIAL_QUEUE_SYSTEM_STATUS_UPDATED`** (event) — social queue system status changed. Payload: none.

## C_Club (ClubDocumentation)

**Changed:**

- **`ClubStreamType`** (enum) — added `Discord` for guild streams mirrored to a linked Discord channel. Before: `General, Guild, Officer, Other`. After: `General, Guild, Officer, Discord, Other`.

## C_GuildInfo (GuildInfoDocumentation)

**New:**

- **`IsDiscordStreamSeparate() → separateStream: bool`** — whether the linked Discord stream shows as a separate chat stream.
- **`GUILD_RANKS_UPDATE_ACTIVE_PLAYER`** (event) — the active player's guild rank data updated. Payload: none.

## C_ChatInfo (ChatInfoDocumentation)

**New:**

- **`CHAT_MSG_GUILD_DISCORD`** (event) — a guild chat message originating from the linked Discord channel. Payload: the standard `CHAT_MSG` args (`text, playerName, languageName, channelName, …, guid, lineID`) plus `discordInfo: DiscordChatInfo`.

## C_Discord (DiscordDocumentation) *(new namespace)*

**New:**

- **`Authorize()`** — begins the Discord OAuth flow.
- **`RefreshAuth()`** — refreshes cached Discord OAuth credentials.
- **`IsUserOAuthed() → hasOAuth: bool`** — whether OAuth is complete.
- **`IsEnabled() → enabled: bool`** — whether the Discord integration is enabled.
- **`GetDiscordUserID() → userID: DiscordID`** — the linked Discord user ID.
- **`GetDisplayNameType() → type: DiscordDisplayNameType`** — the configured display-name type.
- **`GetNumDiscordServers() → count: number`** — number of linkable Discord servers.
- **`GetServerName(index: luaIndex) → name: string`** — server name at the index.
- **`GetServerLinkableChannels(index: luaIndex)`** — requests the linkable channels for a server (no documented return).
- **`GetNumDiscordChannels(serverIndex: luaIndex) → count: number`** — channel count for a server.
- **`GetDiscordChannelName(serverIndex: luaIndex, channelIndex: luaIndex) → name: string`** — channel name.
- **`UpdateDiscordServers()`** — refreshes the cached server list.
- **`GuildLink(serverIndex: luaIndex, channelIndex: luaIndex)`** — links the guild to a Discord server/channel.
- **`GuildUnlink()`** — removes the guild's Discord link.
- **`IsGuildChannelLinked() → isLinked: bool`** — whether the guild has a linked channel.
- **`GetGuildLinkStatus() → isFullyLinked: bool, linkedChannelName: string, linkedServerName: string`** — current link status and names.
- **`UpdateGuildLobby()`** — refreshes the guild's Discord lobby state.
- **`IsGuildSettingSet(setting: DiscordGuildSettings) → isSet: bool`** — whether a guild Discord setting is on.
- **`SetGuildSetting(setting: DiscordGuildSettings, set: bool)`** — toggles a guild Discord setting.
- Events (all payload: none unless noted): `DISCORD_STATUS_UPDATE`, `DISCORD_LINK_UPDATE`, `DISCORD_SERVER_LIST_UPDATE`, `DISCORD_GUILD_LOBBY_UPDATE`, `DISCORD_GUILD_SETTINGS_UPDATE`, `DISCORD_GUILD_ACHIEVEMENT` (Payload: `achievementID: number`).

## DiscordConstantsDocumentation *(new namespace)*

**New:**

- **`DiscordAccountType`** (enum) — Values: `Normal, Provisional`.
- **`DiscordDisplayNameType`** (enum) — Values: `Default, LastOnline, GlobalName`.
- **`DiscordGuildSettings`** (enum) — Values: `SeparateStream`.
- **`DiscordChatInfo`** (struct) — Discord metadata on a bridged message. Fields: `userID: DiscordID, globalName: string, type: DiscordDisplayNameType, lastOnlineGUID: WOWGUID, lastOnlineName: string, hasAttachment: bool, hasPoll: bool, hasEmbed: bool, hasSticker: bool, hasEmoji: bool, hasForwardedMessage: bool, forwardedMessage: string, fromDiscord: bool`.

## C_LFGList (LFGListInfoDocumentation)

**New:**

- **`ConfirmCensoredActiveEntry()`** — confirms keeping the player's active entry despite censored text.
- **`DoesCensoredTextMatch(name: cstring, comment: cstring) → isMatch: bool`** — whether a name/comment matches censored text.
- **`IsCensoredActiveEntryUnresolved() → isUnresolved: bool`** — whether the active entry has unresolved censored content.
- **`RevealCensoredActiveEntry()`** — reveals the censored content of the active entry.
- **`RevealCensoredSearchResult(searchResultID: number)`** — reveals the censored content of a search result.
- **`LFG_LIST_CENSORED_ACTIVE_ENTRY_UPDATE`** (event) — active entry's censored status changed. Payload: `isCensored: bool`.
- **`LFG_LIST_REVEALED_CENSORED_ACTIVE_ENTRY`** (event) — active entry's censored content was revealed. Payload: none.

## C_RecruitAFriend (RecruitAFriendDocumentation)

**New:**

- **`IsSystemEnabled() → enabled: bool`** — whether Recruit A Friend is enabled.
- **`IsSystemSupported() → supported: bool`** — whether Recruit A Friend is supported on this client.

**Removed:**

- **`IsEnabled() → enabled: bool`** — replaced by the `IsSystemEnabled` / `IsSystemSupported` pair.

## RecruitAFriendSharedDocumentation

**New:**

- **`RecruitAFriendFailure`** (enum) — failure reasons for RAF summon/recruit. Values: `Success, NotLinked, NotNow, NoTarget, NotInParty, SummonLevelMax, SummonCooldown, InsufExpanLvl, Offline, MapIncomingTransferNotAllowed, NotInClassic`.

## AccountConstantsDocumentation

**New:**

- **`AccountGetListRequestType`** (enum) — type of account list request. Values: `None, Battlepets`.
