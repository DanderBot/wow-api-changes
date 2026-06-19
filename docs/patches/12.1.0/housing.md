# Housing

Housing saw broad changes across many namespaces; most are internal UI plumbing plus struct/enum additions. The breaking change is the `IsInsideOwnHouse` → `IsInsideOwnedHouse` rename. Highlights by namespace:

- **C_HousingBlueprint (new namespace)** — full blueprint-sharing system. `ImportBlueprint(shareCode: cstring)`, `ExportBlueprint(type: HousingBlueprintType, name: cstring)`, plus `ExportRoomBlueprint`, `DeleteBlueprint`, `RenameBlueprint`, `IsImportAvailable`/`IsExportAvailable`, `CanImportTypeFromCurrentLocation`, `IsShareCodeValid`, `GetBlueprintHyperlink`, `GetBlueprintTypeForCode`.
- **HousingBlueprintConstants (new namespace)** — supporting types: enums `HousingBlueprintContentType` (None, HouseType, Room, Decor, Dye, Fixture, Other) and `HousingBlueprintUnmetRequirementFlags` (bitfield: InsufficientBudget, MissingRoom, MissingFixture, MissingDecor, MissingDye, MismatchedExteriorFaction, HouseTypeLocked, HouseSizeLocked); structs for blueprint collections/groups/entries.
- **C_HousingUI** — `IsInsideOwnHouse` **renamed** to `IsInsideOwnedHouse() → bool`; new `IsInsideOwnedHouseOrPlot`, `IsInsideOwnedPlot`; new `ResetHouse(resetScope: HousingHouseScope)` (restricted; clears house contents) with `HOUSE_RESET_COMPLETED`/`HOUSE_RESET_FAILED` events; new `HouseFinderIgnoreNeighborhood`.
- **C_HousingLayout** — `GetRoomPlayerIsIn() → roomGUID: WOWGUID` (may return nothing), `GetBaseRoomFloor`.
- **C_HousingDecor** — decor pet-placement: `GetDecorCanAttachPet`, `GetDecorAssignedPetName`, `GetMax/SpentPetPlacementBudget`, `GetBothMaxPlacementBudgets`, `AnyDecorPlacedInRoom`.
- **C_HousingCustomizeMode** — `ApplyPetToSelectedDecor`, `GetSelectedDecorPetInfo`.
- **PlayerHousingConstants** — added `HousingBlueprintFlag`, `HousingHouseScope` enums + a `HousingConsts` table.
