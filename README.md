# Revenant-GameDev
This is intended to document my journey as a rookie game developer, using proper Engineering skills to keep myself organized and motivated while also ensuring me the best results. I will build this from the ground up using VSCode with no Game Engine, just pure code. 

# Revenant — A Metroidvania-Roguelite

![Status](https://img.shields.io/badge/status-pre--alpha-orange)
![Engine](https://img.shields.io/badge/prototype-Python%20%2B%20Pygame-blue)
![License](https://img.shields.io/badge/license-UPRM-green)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

> A fast, skill-expressive side-scroller where **your gear defines your build**. No classes—mix weapons, armor, and passives to forge your own combat style.

---

## Table of Contents

1. [Elevator Pitch](#elevator-pitch)
2. [Design Pillars](#design-pillars)
3. [World & Tone](#world--tone)
4. [Core Gameplay Loop](#core-gameplay-loop)
5. [Combat Overview](#combat-overview)
6. [Weapons & Abilities](#weapons--abilities)
7. [Gear & Equipment](#gear--equipment)
8. [Progression](#progression)
9. [Rooms, Biomes & Encounters](#rooms-biomes--encounters)
10. [Enemies & Bosses](#enemies--bosses)
11. [UI/UX](#uiux)
12. [Tech & Scope](#tech--scope)
13. [Repo Structure](#repo-structure)
14. [Getting Started](#getting-started)
15. [Controls (Prototype)](#controls-prototype)
16. [Roadmap](#roadmap)
17. [Contributing](#contributing)
18. [FAQ](#faq)
19. [License & Credits](#license--credits)
20. [Contact](#contact)

---

## Elevator Pitch

Revenant is a 2D action Metroidvania with roguelite runs. Instead of classes, players assemble builds from **weapons (each with unique abilities)** and **gear**. Combat is punchy and combo-driven; exploration is room-based with secrets, traps, and environmental hazards. Death resets the run, but **traits** and **unlocks** persist to enable long-term progression.

---

## Design Pillars

* **Player Expression:** Builds emerge from weapons, armor, accessories, and traits.
* **Clarity First:** Tight controls, readable telegraphs, fair punishments.
* **Meaningful Choices:** Tradeoffs (damage vs. survivability, mobility vs. control).
* **Replayable Routes:** Rooms/biomes remix each run; different loot/affixes.
* **Low Overwhelm:** Simple core, deep mastery (combos, cancels, statuses).

---

## World & Tone

A ruined frontier suspended between decay and rebirth. Relics from prior ages fuel your power; corrupted guardians gate deeper biomes. The “Revenant” returns after every fall—changed by what they’ve learned and equipped.

---

## Core Gameplay Loop

1. **Spawn** in a safe room → choose starting weapon/gear.
2. **Explore** rooms → combat, traversal, secrets, hazards.
3. **Upgrade** via loot, vendors, altars, and events.
4. **Defeat Boss** → unlock next biome, currencies, blueprints.
5. **Die or Extract** → spend currencies on **traits** & **unlocks**.
6. **Repeat** stronger, with new routes and options.

---

## Combat Overview

* Side-scrolling action with dodge, jump, aerial control.
* **Weapons define abilities** (each weapon type grants **3 unique actives**).
* **Combos:** Light/Heavy strings, aerials, and carefully placed **cancel windows**.
* **Resources:** Stamina (mobility/defense), Mana/Charge (abilities), Health (rare heals).
* **Status Tags:** Bleed, Burn, Shock, Guard Break, Stagger windows, etc.

---

## Weapons & Abilities

**Categories (examples):**

* **Melee:** Fists, Daggers, Swords, Greatswords, Maces, Spears
* **Ranged:** Bows, Crossbows, Throwing Blades
* **Magic/Focus:** Tomes, Staves, Seals

Each weapon provides:

* A base moveset (light/heavy/air) with cancel rules
* **3 unique abilities** mapped to ability slots
* A passive flavor (e.g., +stagger on parry; +crit on aerial hits)

**One-handed** types support off-hands (**shields**, orbs, charms).

---

## Gear & Equipment

**Slots:** Helmet • Chestplate • Boots • Accessory • Weapon • Off-hand (optional)

**Armor Types:**

* **Light:** High mobility, lower defense, +crit/skill bias
* **Medium:** Balanced stats, utility affixes
* **Heavy:** High defense/poise, slower stamina regen, counter-oriented

**Affixes/Perks (examples):** % vs airborne, perfect-dodge buff, thorns, elemental procs, resource on kill, **set bonuses**.

---

## Progression

* **In-Run:** Loot, ability upgrades, shortcuts, risky events.
* **Meta (Persistent):**

  * **Traits:** Permanent boosts/mechanics (e.g., extra i-frames, alt-routes).
  * **Blueprints:** Unlock gear into the run pool.
  * **World Upgrades:** Vendors, training rooms, practice dummy.

---

## Rooms, Biomes & Encounters

* **Rooms:** Arenas, traversal, mini-puzzles, secrets, trap corridors.
* **Biomes (examples):** Ruined Outskirts → Sunken Foundry → Gloomwood → Shattered Bastion.
* **Events:** Altars (boons/banes), timed doors, elite ambushes, lore shrines.
* **Hazards:** Spikes, crushers, flame vents, shock pylons, cursed fog.

---

## Enemies & Bosses

* **Enemy Families** share cores with biome variants.
* **Elites** roll modifiers (fast, armored, volatile, summoner).
* **Bosses** teach mechanics, gate biomes, drop unique blueprints & trait currency.

---

## UI/UX

* Minimal, readable HUD; clear stamina/mana/cooldown indicators.
* Status effects use **icon codes** with brief tooltips.
* Accessibility: remappable keys, color-blind friendly icons, screen-shake toggle.

---

## Tech & Scope

* **Prototype Stack:** Python + Pygame (build fundamentals before engine migration).
* **Target Feel:** Retro-inspired 2D (not strictly 8-bit), crisp hit-stop, snappy camera.
* **Later Option:** Consider Godot/Unity once feel is locked.

---

## Repo Structure

```
/game
  /assets            # sprites, fx, sfx, fonts (licensed/attributed)
  /core              # state, scenes, input, timing, resources
  /combat            # hit/hurt boxes, damage, statuses, i-frames
  /entities
    /player          # movement, combos, cancels, ability slots
    /enemies         # AI, families, elites
    /bosses          # phases, arenas, intros/outros
  /gear              # weapons, armor, accessories, affixes, sets
  /world             # rooms, biomes, traps, spawners, loot tables
  /ui                # hud, menus, overlays, notifications
  /systems           # save/meta, traits, unlocks, vendors
  /utils             # math, data, logging, helpers
main.py              # entry point
requirements.txt
README.md
LICENSE
```

---

## Getting Started

### 1) Prerequisites

* **Python 3.10+**
* **Pip** (or pipx/venv)

### 2) Install dependencies

**Windows (PowerShell/CMD):**

```bash
py -m pip install -r requirements.txt
```

**macOS/Linux:**

```bash
python3 -m pip install -r requirements.txt
```

> If `pip` isn’t recognized: reinstall Python and check **“Add Python to PATH”**, or use `py -m pip ...` on Windows.

### 3) Run

```bash
python3 main.py   # or: py main.py (Windows)
```

---

## Controls (Prototype)

* **Move:** A/D or ←/→
* **Jump:** W / Space
* **Dodge/Roll:** Left Shift
* **Light / Heavy:** J / K
* **Abilities 1–3:** U / I / O
* **Interact:** E
* **Pause / Menu:** Esc

> Keybinds will be **remappable** in the options menu as the project matures.

---

## Roadmap

* [ ] **v0.1 Core Loop:** movement, collisions, room loading, basic enemy
* [ ] **v0.2 Combat Core:** combos, cancels, i-frames, damage & stagger, 1–2 weapons
* [ ] **v0.3 Gear Pass:** armor slots, affixes, accessories, loot tables
* [ ] **v0.4 World:** 30–40 rooms, 2 biomes, traps, secrets, vendor/events
* [ ] **v0.5 Boss Alpha:** 1–2 bosses with simple phases & telegraphs
* [ ] **v0.6 UI/UX:** HUD polish, remapping, options
* [ ] **v0.7 Meta:** traits, unlock flow, blueprints, hub loop
* [ ] **v1.0 Alpha:** content pass, balance, performance, controller support

---

## Contributing

We ❤ small, focused PRs!

1. **Open an Issue** to discuss large features/changes first.
2. Follow Conventional Commits (`feat:`, `fix:`, `chore:`…).
3. Include a short GIF/screencap for visual changes (combat feel, UI).
4. Add minimal tests/docs where logic is non-obvious (e.g., cancel windows).
5. Labels used: `good-first-issue`, `help-wanted`, `design-needed`, `discussion`.

**Local Dev Tips**

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python main.py
```

---

## FAQ

**Is this class-based?**
No—builds come from **weapons + gear + traits**.

**What persists after death?**
Traits, unlocks, and hub/world upgrades.

**How hard is it?**
“Tough but fair.” If you can read it, you can beat it.

**Why Python + Pygame?**
To nail feel & systems without heavy engine overhead; migration is an option later.

**Where do I start as a contributor?**
Check issues labeled **`good-first-issue`** or pick a scoped task from the roadmap.
Also, feel free to join our Discord for feedback, suggestions, updates and more!
Link: https://discord.gg/WEjpJ6kH
---

## License & Credits

* **License:** University of Puerto Rico, Mayaguez. CS50-WebDev - Harvard (in-progress)
* Third-party assets (when used) will be credited in `/assets/ATTRIBUTIONS.md`.

---

## Contact

Open a GitHub **Issue** or start a **Discussion → Ideas** to propose features, report bugs, or share feedback.
These features will also be available on our Discord Server.

---

> *Want badges, a banner, and contributor guidelines auto-generated?* Say the word and I’ll draft **`CONTRIBUTING.md`**, **`CODE_OF_CONDUCT.md`**, and a **banner image prompt** you can use to create a repo header.
