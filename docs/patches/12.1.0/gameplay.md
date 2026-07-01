# Gameplay: PvP, Items, Spells, Specs

## C_PvP (PvpInfoDocumentation)

**New:**

- **`CanSurrenderArena() → canSurrender: bool`** — whether the player can currently surrender the arena match.

## ItemConstantsDocumentation

**New:**

- **`ItemConversionFlags`** (enum) — flags controlling item conversion. Values: `UseInputItemStats`.

## C_Item (ItemDocumentation)

**New:**

- **`DoesItemMatchSpellItemCondition(itemLoc: ItemLocation) → matches: bool`** — whether the item at a location satisfies the current spell's item condition.

## C_Spell (SpellDocumentation)

**New:**

- **`TargetSpellChecksItemCondition() → result: bool`** — whether the pending/target spell evaluates an item condition.

## SpecializationSharedDocumentation

**New:**

- **`GetSpecializationSystem() → system: SpecializationSystem`** — which specialization system is active.

## PaperDollInfoDocumentation

**New:**

- **`GetInventorySlotInfo(slotName: cstring) → invSlot: number, slotTexture: fileID, checkRelic: bool`** — resolves a slot by name (may return nothing) — the C_API equivalent of the old global.
- **`GetInventorySlotInfoForInvSlot(invSlotValue: number) → invSlot: number, slotTexture: fileID, checkRelic: bool, slotName: cstring`** — resolves slot info from a Lua INVSLOT value (may return nothing).

## C_PetJournal (PetJournalInfoDocumentation)

**New:**

- **`GetPetInfoTableBySpeciesID(speciesID: number) → petInfo: PetJournalPetInfo`** — a consolidated pet-info table for a species (may return nothing).

## QuestHubInfoDocumentation

**New:**

- **`IsQuestCurrentlyRelatedToHub(questID: number, hubAreaPoiID: number) → isRelated: bool`** — whether a quest is currently associated with a given hub-area POI.

## CharacterCreationConstantsDocumentation

**New:**

- **`RestrictionType`** (enum) — why a creation option is restricted. Values: `Invalid, ServerExpansion, AccountExpansion, Achievement, Entitlement`.

## C_DyeColor (DyeColorInfoDocumentation)

**New:**

- **`GetDyeColorsForItem(itemLinkOrID: ItemInfo) → dyeColorIDs: table`** — all applicable dye-colour IDs for an item.
- **`GetDyeColorsForItemLocation(itemLocation: ItemLocation) → dyeColorIDs: table`** — all applicable dye-colour IDs for an item at a location.

**Removed:**

- **`GetDyeColorForItem(itemLinkOrID: ItemInfo) → dyeColorID: number?`** and `GetDyeColorForItemLocation(itemLocation: ItemLocation) → dyeColorID: number?` — replaced by the plural versions that return a table of IDs.

---

## Later PTR build additions (2026-06-20)

### C_EncounterJournal (EncounterJournalDocumentation)

**New:**

- `GetDungeonEntrancesForMap(uiMapID: number) → dungeonEntrances: table<DungeonEntranceMapInfo>` — dungeon entrances on a UI map.
- `InstanceHasDifficultyID(difficultyID: number) → bool` — whether the current instance supports a difficulty id.

### C_Navigation (InGameNavigationDocumentation)

**New:**

- `GetNextWaypointForMap(uiMapID: number) → x: number, y: number, waypointDescription: string` — the next waypoint on a UI map (may return nothing). Moved from `C_SuperTrack` (which removed it).

### PlayerChoiceConstantsDocumentation *(new namespace)*

**New:**

- `PlayerChoiceFlags` (enum, bitmask) — display/behaviour flags, e.g. `InfiniteRange`, `KeepOpenAfterChoice`, `ShowChoicesAsList` / `Grid` / `Columns`, `RequiresSelection`, `HideAnswerArt`.
- `PlayerChoiceLayout` (enum) — `Default`, `Grid`, `List`, `Columns`.
- `PlayerChoiceResponseFlags` (enum) — per-response flags, e.g. `ShowAnswerDisabled`, `ShowArtDesaturated`, `HideButton`, `ShowAnswerSelected`.
