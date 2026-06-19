# WoW API Changes

A living reference of World of Warcraft Lua API changes between game builds, for addon developers.

**📖 Live site:** https://danderbot.github.io/wow-api-changes/

Each patch page lists new / changed / removed functions, events, structs, and enums — with full signatures — compiled from Blizzard's API documentation files (`Blizzard_APIDocumentationGenerated`) and addon source between two builds.

## Patches

- [12.1.0 (PTR) — vs 12.0.7](docs/patches/12.1.0.md)

## How it's built

The site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and auto-deployed to GitHub Pages by a GitHub Action on every push to `main`. The contents page (left nav + per-page table of contents) and the search box are generated automatically from the markdown.

## Local preview

    pip install -r requirements.txt
    mkdocs serve

Then open http://127.0.0.1:8000/.

## Contributing

Spotted an error or have a correction for a PTR change? Open an issue or a pull request against the relevant `docs/patches/<version>.md` file.
