# WoW 12.1.0 PTR — API Changes (vs 12.0.7)

A human-readable reference of the Lua API surface changes between the **12.0.7** retail baseline and the **latest 12.1.0 PTR build**, compiled from Blizzard's own API documentation files (`Blizzard_APIDocumentationGenerated`) plus a comparison of the shipped Blizzard addon source between the two builds. Regenerated as new PTR builds land.

Each entry says what an API **does** if it's new, or what's **different** if it changed. Descriptions are grounded in the real function signatures and Blizzard `Documentation` fields, not guessed.

**Notation:** `Func(arg: Type, optional: Type?) → ret: Type` — a trailing `?` marks a nilable (optional) argument or return. A function with no `→` returns nothing. Types are Blizzard's own (`cstring`, `luaIndex`, `WOWGUID`, `bool`, `fileID`, struct/enum names, etc.). Events list their `Payload:`; structs list their `Fields:`; enums list their `Values:`.

---

## Breaking & notable changes (for addon authors)

**Renamed struct field — silent breakage risk.**

`AddPrivateAuraAnchorArgs` (passed to `C_UnitAuras.AddPrivateAuraAnchor`) renamed `showCountdownFrame` → `showCooldownFrame`, and added `showCooldownEdge` and `showDispelIcon`. Addons still passing `showCountdownFrame` will see the cooldown swipe silently stop appearing on private auras. The engine ignores unrecognised keys, so to support both 12.0.7 and 12.1 from a single build, set both keys. Worth a PTR check to confirm whether the old key is still accepted as an alias. Note that a plain surface diff will *not* flag this — it tracks added/removed structs and functions, not renamed fields inside a struct.

**Removed / renamed functions & events.** Code referencing these by their old name will break:

- **`C_UnitAuras.TriggerPrivateAuraShowDispelType`** — removed.
- **`C_PingSecure.SendPing`** / `GetTargetWorldPing` / `GetTargetWorldPingAndSend` — removed; replaced by the type-specific send functions (`SendUnitPing`, `SendPlayerSpellPing`, etc.).
- **`C_Ping.GetContextualPingTypeForUnit`** — removed.
- **`C_DyeColor.GetDyeColorForItem`** / `GetDyeColorForItemLocation` — replaced by plural, list-returning versions.
- **`C_RecruitAFriend.IsEnabled`** — replaced by `IsSystemEnabled` / `IsSystemSupported`.
- **`C_HousingUI.IsInsideOwnHouse`** — renamed to `IsInsideOwnedHouse`.
- **`BATTLETAG_INVITE_SHOW`** (event) — replaced by `CONFIRM_BATTLE_NET_FRIEND_INVITE_SHOW`.
- Global `UIParent_ManageFramePositions` — removed; `Blizzard_UIParent` was split into new managed-frame / UI-mode addons. Use `ManageFramePositions`.
- **`FrameScript.SetTableSecurityOption`** — renamed to `settablesecurity`.
- **`SimpleFrameScriptObject.HasAnyForbiddenAspect`** — removed; use `GetForbiddenAspects` / `GetInheritableForbiddenAspects`.
- **`C_HousingBlueprint.IsImportAvailable` / `IsExportAvailable`** — replaced by `GetImportAvailability` / `GetExportAvailability` (+ `GetFeatureAvailability`).

**Major new systems.**

- **Group Buffs** — hide specific group/raid buffs and configure per-buff visual alerts (`C_UnitAuras.GetHiddenGroupBuffs` / `GetGroupBuffVisualAlerts` + setters and change events, with Cooldown Viewer integration). Frame/aura addons may want to honour the player's hidden-buff list.
- **Discord integration** — guild chat can bridge to a linked Discord channel; new `C_Discord` namespace, Battle.net "title friends", and per-friend interest tags.
- **Radial status bars / textures** — status bars and textures can render as radial progress (`SetRenderMode(Enum.StatusBarRenderMode.Radial)` + radial-progress texture APIs). No Blizzard Lua uses it yet.
- **Roleset / UI-mode visibility** — frames carry "roleset" tags (`SetRolesets`, `C_Roleset.ApplyRolesetFilters`) that gate visibility through the new UI-mode system.
- **Aura Containers & Buttons** — new `AuraContainer` / `AuraButton` widget types let addons display auras in custom, secure ways: the container handles tracking/filtering (`SetUnit`, `AddAuraFilter`, `AddAuraFrame`), and buttons expose presentation setters (icon, duration cooldown/text/bar, stack count). Addons control the look but never touch the underlying aura data. (Widget types + templates are on the **UI Building Blocks** page.)
- **Private Script Objects & Forbidden Aspects** — a new security layer behind the aura system: an object can hide a "Forbidden Partition" from addons, and `ForbiddenAspect` values (`UntrustedScriptExecution`, `EventRegistrations`, `Shown`, `ScriptedInput`, …) restrict what addons may do with an object (e.g. Aura Buttons — addons can't install script handlers, register events, or read `IsShown` on them). `SimpleFrameScriptObject` gained `GetForbiddenAspects` / `GetInheritableForbiddenAspects`; a new `ForbiddenAspectInheritance` enum controls propagation.

**Edit Mode unit-frame icon size split.** `Enum.EditModeUnitFrameSetting.IconSize` was removed and split into separate `BuffIconSize` and `DebuffIconSize`. Code reading that enum value must update.

---

## Sections

- [Auras & Cooldown Viewer](auras.md)
- [Frames, UI & Secure Internals](frames.md)
- [Edit Mode, Nameplates & Misc](edit-mode.md)
- [Pings](pings.md)
- [Gameplay: PvP, Items, Spells, Specs](gameplay.md)
- [Social, Battle.net & Discord](social.md)
- [Housing](housing.md)
- [UI Building Blocks](ui-blocks.md) — templates, mixins, widget types, new addons
- [Globals & Constants](globals.md) — global functions & constants in Blizzard addons
- [Field-level Changes](field-level.md) — field/arg/value-level deltas inside existing entries

---

## Caveats / what this does NOT cover

Coverage now spans the full addon-facing surface: the documented API (functions, events, structs, enums), **field-level changes** inside existing structs/enums, the **UI building blocks** (templates, mixins, widget types, addons), and **globals & constants** defined in Blizzard's addons. Out of scope:

- **Blizzard's internal implementation changes** (function-body rewrites that don't change a public signature, template, or global) are intentionally excluded — they can't affect addons. Use the raw source diff for those.
- **Engine/runtime behaviour** — taint rules, secret-value handling, `error → nil`, re-opened/restricted APIs — isn't visible to a source diff. Cross-check the official PTR patch notes and the WoW Dev Discord `#api-changes` channel.
- Reflects the **latest 12.1.0 PTR build** (regenerated 2026-06-20); subject to change before 12.1 goes live. The UnitAura secret-value changes and some Aura Button protections are rolling out over several PTR builds, so this will keep moving.
