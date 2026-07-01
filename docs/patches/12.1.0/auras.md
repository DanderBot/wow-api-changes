# Auras & Cooldown Viewer

## C_UnitAuras (UnitAuraDocumentation)

**New:**

- **`GetHiddenGroupBuffs() → spellIDs: table<number>`** — the list of group-buff spell IDs the player has hidden.
- **`SetHiddenGroupBuffs(spellIDs: table<number>)`** — sets the list of group-buff spell IDs to hide.
- **`GetGroupBuffVisualAlerts() → visualAlerts: table<GroupBuffVisualAlertInfo>`** — the configured group-buff visual alerts.
- **`SetGroupBuffVisualAlerts(visualAlerts: table<GroupBuffVisualAlertInfo>)`** — sets the group-buff visual alerts.
- **`HIDDEN_GROUP_BUFFS_CHANGED`** (event) — the hidden group-buff list changed. Payload: `spellIDs: table<number>`.
- **`GROUP_BUFF_VISUAL_ALERTS_CHANGED`** (event) — group-buff visual alerts changed. Payload: `visualAlerts: table<GroupBuffVisualAlertInfo>`.

**Removed:**

- **`TriggerPrivateAuraShowDispelType`** — gone in 12.1.0.

## UnitConstantsDocumentation

**New:**

- **`GroupBuffVisualAlertInfo`** (struct) — pairs a group-buff spell with its alert style. Fields: `spellID: number, visualValue: VisualAlertType`.

**Changed:**

`AddPrivateAuraAnchorArgs` (struct) — args for `C_UnitAuras.AddPrivateAuraAnchor`. `showCountdownFrame` was **renamed** to `showCooldownFrame`; `showCooldownEdge` and `showDispelIcon` were added; all bool fields now default `false`:

```diff
  unitToken: cstring
  auraIndex: number
  parent: SimpleFrame
- showCountdownFrame: bool
+ showCooldownFrame: bool
+ showCooldownEdge: bool
  showCountdownNumbers: bool
+ showDispelIcon: bool
  isContainer: bool
  iconInfo: PrivateAuraIconInfo?
  durationAnchor: AnchorBinding?
```

## UnitAuraConstantsDocumentation *(new namespace)*

**New:**

- **`UnitAuraUIConstants`** (constants) — list-size caps. Values: `HIDDEN_GROUP_BUFF_LIST_SIZE = 32, GROUP_BUFF_VISUAL_ALERT_LIST_SIZE = 32`.

## C_CooldownViewer (CooldownViewerDocumentation)

**New:**

- **`GetGroupBuffItems() → groupBuffItems: table<GroupBuffItem>`** — the available group-buff items.
- **`GroupBuffItem`** (struct) — a group-buff entry. Fields: `spellID: number, name: cstring, iconID: fileID, flags: GroupBuffItemFlags, isKnown: bool`.

**Changed:**

`CooldownViewerCooldown` (struct, returned by `GetCooldownViewerCooldownInfo`) — `spellID` became nilable; `spellCategoryID`, `equipSlot`, and `isInvisible` were added:

```diff
  cooldownID: number
- spellID: number
+ spellID: number?
+ spellCategoryID: number?
  overrideSpellID: number?
  overrideTooltipSpellID: number?
+ equipSlot: luaIndex?
  linkedSpellIDs: table<number>
  selfAura: bool
  hasAura: bool
  charges: bool
  isKnown: bool
+ isInvisible: bool
  flags: CooldownSetSpellFlags
  category: CooldownViewerCategory
```

## CooldownViewerConstantsDocumentation

**New:**

- **`CooldownViewerSound`** (enum) — selectable "ready" alert sound; 94 values (0–93), e.g. `TextToSpeech (0)`, `AnimalsCat (1)`, `War3Bell (56)`.
- **`GroupBuffItemFlags`** (enum) — flags for group-buff items. Values: `HideByDefault`.
- **`GroupBuffUIConstants`** (constants) — Values: `GROUP_BUFF_ITEM_LIST_SIZE = 16`.

**Changed:**

- **`CooldownViewerCategory`** (enum) — grew from 4 to 9 values; added `GroupBuff (4), SpecAgnosticEssential (5), SpecAgnosticTracked (6), EquipSlotEssential (7), EquipSlotTracked (8)`.
- **`CooldownViewerUIConstants`** (constants) — added `COOLDOWN_VIEWER_SPEC_AGNOSTIC_PARENT_ID = 0`.

## SecretAspectConstantsDocumentation

**Changed:**

- **`SecretAspect`** (enum, bitfield) — added `RadialProgress (8388608)`; now 30 values.

## ForbiddenAspectConstantsDocumentation *(new namespace)*

**New:**

- **`ForbiddenAspect`** (enum) — aspects forbidden from being set on protected frames. Values: `SetToDefaults, ScriptBindings`.

## VisualAlertConstantsDocumentation *(new namespace)*

**New:**

- **`VisualAlertType`** (enum) — visual alert styles for group buffs. Values: `MarchingAnts (+ Cyan/Red/Green/Blue), Flash (+ Cyan/Red/Green/Blue)`.

## TooltipInfoSharedDocumentation

**Changed:**

- **`TooltipDataLineType`** (enum) — added `ItemSpellTriggerOnUse (44), ItemSpellTriggerOnEquip (45), ItemSpellTriggerOnProc (46)` — tag tooltip lines for an item's Use/Equip/on-proc spell effects.

---

## Later PTR build additions (2026-06-20)

### ForbiddenAspectConstantsDocumentation

The forbidden-partition security layer behind Aura Buttons expanded substantially.

**New:**

- `ForbiddenAspectInheritance` (enum) — how forbidden aspects propagate. Values: `Parent` (through object hierarchies), `Layout` (through the anchor graph).

**Changed:** `ForbiddenAspect` (enum) — added values (bitmask), each restricting a facet of the security system:

- `UntrustedScriptExecution` (4) — blocks execution of all scripts on the object (propagates to children).
- `UntrustedLayoutScriptExecution` (8) — blocks layout scripts (e.g. OnSizeChanged); propagates to children and anything anchored to it.
- `EventRegistrations` (16) — blocks querying/modifying registered script events.
- `AlwaysPropagateInput` (32) — forces mouse/keypress input propagation (propagates to children).
- `ScriptedInput` (64) — blocks APIs that trigger synthetic input from scripts.
- `QueryFocus` (128) — blocks APIs that query input focus state.
- `Shown` (256) — blocks control of a region's shown state.
