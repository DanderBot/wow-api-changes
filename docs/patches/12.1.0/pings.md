# Pings

## C_PingSecure (PingManagerSecureDocumentation)

**New:**

- **`SendUnitPing(target: WOWGUID, type: PingSubjectType?, isPlayerResource: bool?) → result: SendPingResult`** — pings a unit by GUID; `isPlayerResource` optionally calls out the player's health/mana for player-frame pings.
- **`SendPlayerSpellPing(spellID: number) → result: SendPingResult`** — pings a player spell action.
- **`SendPlayerItemPing(itemID: number) → result: SendPingResult`** — pings a player item action.
- **`SendHitTestPing(type: PingSubjectType?) → result: SendPingResult`** — pings the current hit-test target.
- **`SetHitTestPingTarget(mousePosX: number, mousePosY: number, forcePointPing: bool?) → state: PingSetTargetState`** — resolves and stores a ping target from a screen position.
- **`SetHitTestTargetAndSendPing() → result: SendPingResult`** — resolves the hit-test target and pings it in one call.
- **`ClearHitTestPingInfo()`** — clears any stored hit-test ping target.
- **`UNIT_PING_PIN_ADDED`** (event) — a ping pin attached to a unit was added. Payload: `guid: WOWGUID, uiTextureKit: textureKit`.
- **`UNIT_PING_PIN_REMOVED`** (event) — a unit ping pin was removed. Payload: `guid: WOWGUID`.
- **`PingActionUIInfo`** (struct) — UI info for an action (spell/item) ping. Fields: `spellID: number, itemID: number, textureFileDataID: number, cooldownInfo: PingActionCooldownUIInfo?`.
- **`PingActionCooldownUIInfo`** (struct) — cooldown display for an action ping. Fields: `durationMs: number, remainingMs: number`.
- **`SendPingResult`** (struct) — result of a send-ping call. Fields: `type: PingSubjectType?, result: PingResult`.

**Removed:**

- **`SendPing`**, `GetTargetWorldPing`, `GetTargetWorldPingAndSend` — superseded by the Send*/HitTest API above.

## PingConstantsDocumentation

**New:**

- **`PingSetTargetState`** (enum) — outcome of resolving a ping target. Values: `Ok, Failed, FailedSilent`.
- **`PingTargetOption`** (enum) — what may be pinged. Values: `All, Environment, Units`.
- **`PingTargetType`** (enum) — kind of target resolved. Values: `Unit, Point, Action`.

**Changed:**

- **`PingSubjectType`** (enum) — added `ActionReady (6), ActionOnCooldown (7), ActionUnavailable (8)`.
- **`PingResult`** (enum) — added `FailedSilent (8)`.

**Removed/relocated:**

- **`ContextualWorldPingResult`** (struct) — removed.
- **`PingCooldownInfo`** (struct) — moved to PingManagerShared.
- **`PingTypeInfo`** (struct) — moved to C_Ping (PingManager).

## C_Ping (PingManagerDocumentation)

**Changed:**

- **`SendMacroPing(macroInfo: PingMacroInfo)`** — now takes a single struct. Before: `SendMacroPing(type: PingSubjectType?, targetToken: cstring?)`.
- **`PingTypeInfo`** (struct) — now lives here. Fields: `orderIndex: number, type: PingSubjectType, uiTextureKitID: textureKit`.

**Removed:**

- **`GetContextualPingTypeForUnit(targetUnit: WOWGUID?) → type: PingSubjectType`** — removed. (`GetCooldownInfo() → cooldownInfo: PingCooldownInfo` is **retained**.)

## PingManagerSharedDocumentation *(new namespace)*

**New:**

- **`PingCooldownInfo`** (struct) — ping cooldown timing. Fields: `startTimeMs: number, endTimeMs: number`.
- **`PingMacroInfo`** (struct) — macro-ping descriptor. Fields: `type: PingSubjectType?, targetToken: cstring?, spellID: number?, itemID: number?`.

---

## Later PTR build additions (2026-06-20)

### C_PingSecure (PingManagerSecureDocumentation)

**New:**

- `SendPlayerSpellCategoryPing(spellCategoryID: number) → result: SendPingResult` — pings a player spell category (secure environment only).
