---
layout: default
title: Reference
nav_order: 6
has_children: true
permalink: /reference/
---

# Quick Reference
{: .no_toc }

Fast lookup tables for items, spells, enemies, and game mechanics.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What's in Reference?

This section provides quick-lookup tables and comprehensive data for experienced players who need to check stats quickly without reading full guides.

### Available References

- **[Spells]({{ site.baseurl }}/reference/spells/)** - Complete spell list with costs, ranges, and effects
- **[Bestiary]({{ site.baseurl }}/reference/bestiary/)** - Enemy stats, abilities, and battle appearances
- **[Shops]({{ site.baseurl }}/reference/shops/)** - All shop locations with complete inventories
- **[Secrets]({{ site.baseurl }}/reference/secrets/)** - All hidden items and their locations

---

## How Experience Works

### Standard Level System

For each battle, there's a "standard" level your characters should be at. The game awards experience based on how far above or below this level you are:

- **Below standard**: More experience per action
- **At standard**: Normal experience
- **Above standard**: Less experience per action

### Experience from Actions

| Action | Experience Gain |
|:-------|:----------------|
| **Physical Attack** | Varies by level difference |
| **Attack Spell** | Varies by level difference |
| **Spell on Ally** | Based on TARGET's level |
| **Spell on Self** | Fixed "at-standard" amount |

{: .note }
> Casting spells on yourself always gives consistent experience, which enables the "experience cheating" method.

---

## Item Rarity Guide

### Unique Items (One-time only)

These items can only be obtained once:

| Item | Type | Location | Value |
|:-----|:-----|:---------|:------|
| Caliburn | Sword | Defeat Kane (6.1) | 4000G |
| Rune Bow | Bow | Defeat Sabrina (5.5) | 3400G |
| Runewand | Staff | Defeat Xeno (6.3) | 3000G |
| Vandal Heart | Sword | End of Act V | Priceless |
| Ragnarok | Axe | Cobalt Beach chest (6.2) | 4500G |
| Panzer Claws | Claws | Defeat Kurtz (5.2) | 1200G |

### Secret Items

Hidden items found by examining special tiles:

| Item | Use | Acts Found |
|:-----|:----|:-----------|
| Mad Book | Hold magic (Spellbind) | 1.1, 2.2 |
| Mushroom | Poison magic | 1.2, 2.1 |
| Moonpie | Healing (Self Healing) | 2.1 |
| Ironboot | Protect (Perfect Guard) | 2.4, 3.4 |
| Unicorn | Attack (Rainbow Storm) | 3.3 |
| Kingfoil | Healing (Healing Circle) | 4.2, 4.5 |
| Helstone | Attack (Thunder Ball) | 5.2 |
| Shivbook | Attack (Dagger Storm) | 5.5 |
| Necklace | Attack (Dark Hurricane) | 6.1 |

### Money Items

Items with no use except selling:

- **Gold Coin** (1000G)
- **Gold Axe** (4000G)
- **Mithril** (5000G)

---

## Class Effectiveness Chart

### Attack Bonuses

| Attacker Class | Bonus vs. | Penalty vs. |
|:---------------|:----------|:------------|
| Archer/Bowman/Sniper | Flying, Mages | Knights |
| Knight/Duelist | Archers | Armor |
| Mage/Sorceror/Enchanter | Armor | Mages |
| Airman/Hawknight/Sky Lord | Ground | Archers |

---

## Battle Conditions Quick Reference

### Victory Conditions by Type

| Condition | What to Do | Examples |
|:----------|:-----------|:---------|
| Defeat Boss | Kill specific enemy | Most boss battles |
| Destroy All | Kill all enemies | Standard battles |
| Reach Exit | Move to door/gate | Castle entrances |
| Defend X Turns | Survive/protect | Tower Defense (3.1) |
| Time Limit | Complete in X turns | Prison escape battles |
| No Escapes | Stop enemies fleeing | Reed Highway (3.4) |

### Defeat Conditions

| Condition | Means |
|:----------|:------|
| Death of Ash | Ash must survive (always) |
| Death of Character | Specific ally must survive |
| Object Destroyed | Protect towers, gates, etc. |
| Time Up | Complete before turn limit |

---

## Stat Abbreviations

| Abbr. | Full Name | What It Does |
|:------|:----------|:-------------|
| **ATK** | Attack | Physical damage dealt |
| **DEF** | Defense | Physical damage reduced |
| **AGL** | Agility | Turn order, evasion |
| **HP** | Hit Points | Health |
| **MP** | Magic Points | Spell casting resource |

---

## Spell Range Notation

Spell ranges are noted as **R/F** (Range/Field):

- **Range (R)**: How far you can target (in squares)
- **Field (F)**: Area of effect (diameter in squares)

Examples:
- **4/0**: Range 4, single target
- **5/2**: Range 5, 2-square diameter splash
- **0/1**: Self-centered, 1-square radius around caster
- **inf/inf**: Hits entire battlefield

---

## Equipment Progression

### When to Shop

| Act | Best Available | Cost Level |
|:----|:---------------|:-----------|
| I | Iron equipment | ~500G per piece |
| II | Steel equipment | ~1,800G per piece |
| III-IV | Great/Master equipment | ~6,000G per piece |
| V-VI | Dragon/Kevlar equipment | ~7,000G+ per piece |

{: .important }
> Always fully equip your party before major boss battles!

---

## Map Coordinate System

Hidden items and chests use an (x,y) coordinate system:

- **x** = Squares East from SW corner
- **y** = Squares North from SW corner
- **(0,0)** = Southwest corner of map

Example: **(15,10)** means 15 squares East, 10 squares North from the SW corner.

---

## Common Abbreviations

| Abbr. | Meaning |
|:------|:--------|
| **NPC** | Non-player character |
| **XP/EXP** | Experience points |
| **AOE** | Area of effect |
| **HP/MP** | Hit points / Magic points |
| **SW/NE** | Southwest / Northeast |
| **L.10/L.20** | Level 10 / Level 20 |

---

## Quick Tips

### Shopping
- Advancement to new class auto-equips basic gear
- Always check shops after each advancement
- Sell money items (Gold Axe, Mithril) immediately

### Battle Preparation
- Save before every battle
- Check taverns for hints and items
- Advance characters at levels 10 and 20

### In-Battle Controls
- **△** - Top-down map view
- **□** - Jump to next unused character
- **○** - Check enemy movement range
- **✕** - Check unit status

---

## Next Steps

Explore detailed reference pages:

- [Complete Spell List]({{ site.baseurl }}/reference/spells/)
- [Bestiary & Enemy Database]({{ site.baseurl }}/reference/bestiary/)
- [Shop Inventories]({{ site.baseurl }}/reference/shops/)
- [Secret Items Guide]({{ site.baseurl }}/reference/secrets/)
