# Frames, UI & Secure Internals

## FrameScript

**New:**

- **`GetForbiddenObjectTable(object: FrameScriptObject) → forbiddenTable: FrameScriptObject`** — secure-only; retrieves the forbidden-side object table for a script object.
- **`securecopy(value: LuaValueReference, options: SecureCopyOptions?) → copy: LuaValueReference`** — securely copies a Lua value; tables deep-copied with recursive/shared refs preserved, script objects kept by reference, copy receives the current execution taint.
- **`SecureCopyOptions`** (struct) — options for `securecopy`. Fields: `maxTraversalDepth: number (default 100), wrapUntrustedFunctions: bool (default true)`.
- **`SecureDelegateOptions`** (struct) — options for `CreateSecureDelegate`. Fields: `wrapUntrustedFunctions: bool (default true)`.

## SimpleFrameAPI

**New:**

- **`AddRoleset(roleset: string)`** — adds a roleset tag without removing existing ones.
- **`RemoveRoleset(roleset: string)`** — removes a roleset tag.
- **`SetRolesets(rolesetsString: cstring?)`** — sets the frame's roleset tags (comma-separated for multiple; nil clears) — used by the UI-mode system to gate visibility.
- **`GetRolesetNames() → rolesets: table`** — the frame's roleset tags (`{"roleless"}` if none).
- **`GetOnUpdateMode() → onUpdateMode: OnUpdateMode`** — the configured OnUpdate execution mode.
- **`SetOnUpdateMode(onUpdateMode: OnUpdateMode)`** — changes when OnUpdate scripts run for this object.
- **`CreateVectorGraphics(name: cstring?, drawLayer: DrawLayer?, templateName: cstring?, subLevel: number?) → vectorGraphics: SimpleVectorGraphics`** — creates a vector-graphics child region.

## SimpleFrameScriptObjectAPI

**New:**

- **`GetName() → name: cstring`** — the object's name (secret-gated by the ObjectName aspect).
- **`GetObjectTable() → objectTable: FrameScriptObject`** — the script object's backing object table.
- **`HasAnyForbiddenAspect(aspect: ForbiddenAspect) → hasAnyForbiddenAspect: bool`** — whether the object has the supplied forbidden aspect.
- **`HasAnyForbiddenAspects() → hasAnyForbiddenAspects: bool`** — whether the object has any forbidden aspects.

## SimpleFrameScriptObjectConstants *(new namespace)*

**New:**

- **`OnUpdateMode`** (enum) — when OnUpdate scripts run. Values: `Disabled, RunWhenVisible, RunWhenVisibleOnce, RunOnce, RunAlways`.
- **`ScriptBindingType`** (enum) — script binding phase. Values: `Precall, Extrinsic, Postcall`.
- **`ScriptObjectMetatable`** (enum) — Values: `Public, Forbidden`.
- **`ScriptObjectPartition`** (enum) — Values: `Public, Forbidden`.

## SimpleStatusBarAPI

**New:**

- **`GetRenderMode() → renderMode: StatusBarRenderMode`** — the status bar's render mode.
- **`SetRenderMode(renderMode: StatusBarRenderMode)`** — sets the render mode (linear fill vs radial progress).

## SimpleStatusBarConstants

**New:**

- **`StatusBarRenderMode`** (enum) — how the bar renders its fill. Values: `Linear` (existing fill behaviour), `Radial` (drives the managed texture's radial fill percent instead of resizing anchors).

## SimpleTextureBaseAPI

**New (radial progress bar):**

- **`ClearRadialProgressBar()`** — disables radial rendering, restores standard texture display.
- **`Get/SetRadialProgressBarStartOffset(offset: normalizedValue)`** — start angle offset (0–1; 0 = bottom).
- **`Get/SetRadialProgressBarEndOffset(offset: normalizedValue)`** — end angle offset (0–1).
- **`Get/SetRadialProgressBarPercent(percent: normalizedValue)`** — fill percentage (0–1).
- **`Get/SetRadialProgressBarFeather(feather: normalizedValue)`** — edge feather/blur amount.
- **`Get/SetRadialProgressBarReverse(reverse: bool)`** — whether the bar fills counterclockwise.

## SimpleAnimRadialProgressAPI *(new namespace)*

**New:**

- **`Get/SetFromPercent(percent: number)`** — animation's starting radial fill percent.
- **`Get/SetToPercent(percent: number)`** — animation's ending radial fill percent.

## SimpleVectorGraphicsAPI *(new namespace)*

**New:**

- **`SetSVG(svgAsset: FileAsset) → success: bool`** — assigns an SVG asset.
- **`GetSVGFileID() → svgFile: fileID`** — file ID of the assigned SVG.
- **`HasSVG() → hasSVG: bool`** — whether an SVG is assigned.
- **`ClearSVG()`** — clears the assigned SVG.

## C_Roleset (RolesetSystemDocumentation) *(new namespace)*

**New:**

- **`C_Roleset.ApplyRolesetFilters(blockedRolesets: table, allowedRolesets: table)`** — sets/clears both blocklist and allowlist filters atomically with one visibility re-evaluation; empty table clears the corresponding filter.

## DurationTextBindingObjectAPI

**New:**

- **`SetTextColorCurve(curve: LuaColorCurveObject, property: DurationTextBindingProperty)`** — drive a font string's colour from a duration property via a curve.
- **`GetTextColorCurve() → curve: LuaColorCurveObject, property: DurationTextBindingProperty`** — the curve and property in use (may return nothing).
- **`ClearTextColorCurve()`** — clears the colour curve.
- **`GetFormattedTextColor() → color: colorRGBA`** — the colour currently assigned to the configured font string (may return nothing).

## MinimapFrameAPI

**New:**

- **`SetIconScale(scale: number)`** — sets the scale applied to minimap icons.

---

## Later PTR build additions (2026-06-20)

### FrameScript

**New:**

- `settablesecurity(table: LuaValueVariant, option: TableSecurityOption)` — applies a table security option (`DisallowTaintedAccess`, `DisallowSecretKeys`, `SecretWrapContents`). Replaces the removed `SetTableSecurityOption`.

**Removed:**

- `SetTableSecurityOption` — replaced by `settablesecurity`.

### SimpleFrameScriptObjectAPI

**New:**

- `GetForbiddenAspects() → aspects: ForbiddenAspect` — the mask of all forbidden aspects applied to this object.
- `GetInheritableForbiddenAspects(inheritance: ForbiddenAspectInheritance) → aspects: ForbiddenAspect` — the mask of forbidden aspects that can propagate to others.

**Removed:**

- `HasAnyForbiddenAspect` (singular) — removed; the plural `HasAnyForbiddenAspects(aspects: ForbiddenAspect) → bool` is retained.
