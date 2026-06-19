# Edit Mode, Nameplates & Misc

## EditModeManagerConstantsDocumentation

**New:**

- **`EditModeRaidWarningSetting`** (enum) — settings for the new Raid Warning system. Values: `None`.

**Changed:**

- **`EditModeSystem`** (enum) — added `RaidWarning (24)` (`TotemActionBar` shifts to 25).
- **`EditModeAccountSetting`** (enum) — added `ShowRaidWarning (33)` (`ShowTotemActionBar` shifts to 34).
- **`EditModeMinimapSetting`** (enum) — added `IconScale (3)`.
- **`EditModeUnitFrameSetting`** (enum) — the single `IconSize (19)` aura setting was **split**: slot 19 repurposed to `DebuffIconSize`, new `BuffIconSize (22)` appended. Buff and debuff icon sizes are now controlled independently; code reading the old `IconSize` must update.

## NamePlateConstantsDocumentation

**Changed:**

- **`NamePlateStyle`** (enum) — added `Classic (6)`. Values: `Modern, Thin, Block, HealthFocus, CastFocus, Legacy, Classic`.

## C_CVar (CVarDocumentation)

**New:**

- **`GetCVar(name: cstring) → value: string?`** — the current string value of a CVar by name (now part of the documented `C_CVar` surface).

## C_Sound (SoundDocumentation)

**New:**

- **`PlaySoundWithOptions(params: PlaySoundParams) → success: bool, soundHandle: SoundHandle`** — plays a sound from an options struct (may return nothing).
- **`PlaySoundParams`** (struct) — options for the above. Fields: `soundKitID: number, uiSoundSubType: UISoundSubType, forceNoDuplicates: bool, runFinishCallback: bool, overridePriority: number?, volumeOverride: number?, …`.

## MacroConstantsDocumentation *(new namespace)*

**New:**

- **`MacroConsts`** (constants) — macro count limits. Values: `MAX_ACCOUNT_MACROS = 120, MAX_CHARACTER_MACROS = 30`.

## DelvesConstantsDocumentation

**Changed:**

- **`TieredEntranceType`** (enum) — added `Lairs (4)`.
- **`CompanionConfigSlotTypes`** (enum) — added `Flavor (3)`.

## C_DelvesUI (DelvesUIDocumentation)

**New:**

- **`GetFlavorNodeForCompanion(companionID: number?) → nodeID: number`** — the flavor trait node ID for a delve companion.
- **`GetFlavorNodeNameForCompanion(companionID: number?) → name: cstring`** — the display name of that flavor node.
