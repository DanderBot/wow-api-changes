# WoW API Changes

A living reference of **World of Warcraft Lua API changes** between game builds — what's new, what changed, and what was removed each patch, with full function signatures, event payloads, struct fields, and enum values.

Built for addon developers. Each patch has its own page (see the navigation on the left). Use the **search box** at the top to jump straight to a function, event, struct, or namespace.

## Patches

- [**12.1.0 (PTR)** — vs 12.0.7](patches/12.1.0/index.md)

## How this is compiled

Each page is produced by comparing Blizzard's own API documentation files (`Blizzard_APIDocumentationGenerated`) between two game builds, cross-referenced against the shipped Blizzard addon source. Signatures and descriptions are grounded in the real doc files, not guessed.

!!! warning "Caveats"
    PTR data is subject to change before a patch goes live. Engine/runtime behaviour changes (taint rules, secret-value handling, `error → nil`) are **not** visible to a source diff — cross-check the official PTR patch notes and the WoW Dev Discord `#api-changes` channel.
