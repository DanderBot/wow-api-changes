# Housing

Housing saw broad changes across many namespaces; most are internal UI plumbing plus struct/enum additions. The breaking change is the `IsInsideOwnHouse` → `IsInsideOwnedHouse` rename. Highlights by namespace:

- **C_HousingBlueprint (new namespace)** — full blueprint-sharing system. `ImportBlueprint(shareCode: cstring)`, `ExportBlueprint(type: HousingBlueprintType, name: cstring)`, plus `ExportRoomBlueprint`, `DeleteBlueprint`, `RenameBlueprint`, `IsImportAvailable`/`IsExportAvailable`, `CanImportTypeFromCurrentLocation`, `IsShareCodeValid`, `GetBlueprintHyperlink`, `GetBlueprintTypeForCode`.
- **HousingBlueprintConstants (new namespace)** — supporting types: enums `HousingBlueprintContentType` (None, HouseType, Room, Decor, Dye, Fixture, Other) and `HousingBlueprintUnmetRequirementFlags` (bitfield: InsufficientBudget, MissingRoom, MissingFixture, MissingDecor, MissingDye, MismatchedExteriorFaction, HouseTypeLocked, HouseSizeLocked); structs for blueprint collections/groups/entries.
- **C_HousingUI** — `IsInsideOwnHouse` **renamed** to `IsInsideOwnedHouse() → bool`; new `IsInsideOwnedHouseOrPlot`, `IsInsideOwnedPlot`; new `ResetHouse(resetScope: HousingHouseScope)` (restricted; clears house contents) with `HOUSE_RESET_COMPLETED`/`HOUSE_RESET_FAILED` events; new `HouseFinderIgnoreNeighborhood`.
- **C_HousingLayout** — `GetRoomPlayerIsIn() → roomGUID: WOWGUID` (may return nothing), `GetBaseRoomFloor`.
- **C_HousingDecor** — decor pet-placement: `GetDecorCanAttachPet`, `GetDecorAssignedPetName`, `GetMax/SpentPetPlacementBudget`, `GetBothMaxPlacementBudgets`, `AnyDecorPlacedInRoom`.
- **C_HousingCustomizeMode** — `ApplyPetToSelectedDecor`, `GetSelectedDecorPetInfo`.
- **PlayerHousingConstants** — added `HousingBlueprintFlag`, `HousingHouseScope` enums + a `HousingConsts` table.

---

## Later PTR build additions (2026-06-20)

### C_HouseEditor (HouseEditorUIDocumentation)

**New:**

- `GetHouseEditorPlayerType() → playerType: HouseEditorPlayerType` — the player's relationship to the current house/plot.
- `HouseEditorPlayerType` (enum) — `None`, `Owner`, `Visitor`.

### C_HousingBlueprint (HousingBlueprintUIDocumentation)

**New:**

- `GetExportAvailability() → HousingResult` — Success if the player can export blueprints, else an error type.
- `GetImportAvailability() → HousingResult` — Success if the player can import blueprints, else an error type.
- `GetFeatureAvailability() → HousingResult` — Success if blueprints are enabled as a feature.
- `StartImportRoomBlueprint(shareCode: cstring)` — starts importing a room blueprint (opens Layout Mode to pick a door).
- `HOUSING_BLUEPRINT_IMPORT_STARTED` (event) — a blueprint import began. Payload: none.
- `HOUSING_BLUEPRINTS_AVAILABILITY_CHANGED` (event) — blueprint availability changed. Payload: none.

**Removed:**

- `IsExportAvailable` / `IsImportAvailable` — replaced by `GetExportAvailability` / `GetImportAvailability`.

### C_HousingDecor / C_HousingLayout

**New:**

- `C_HousingDecor.GetBothSpentPlacementBudgets() → spentInterior: number?, spentExterior: number?` — spent interior & exterior placement budgets (nil if not in an owned house/plot).
- `C_HousingLayout.GetSelectedBlueprintFloorplan() → roomID: number, shareCode: cstring` — the selected blueprint floorplan (may return nothing).
- `C_HousingLayout.HasSelectedBlueprintFloorplan() → bool` — whether a blueprint floorplan is selected.

### PlayerHousingConstants (HousingResult enum)

**Changed:**

- Added `AccountBanned`, `BlueprintRoomPlacementRequired`, `MaxPlacedDecorReached`, `MaxStorageDecorReached`; removed `MaxDecorReached` (superseded).
