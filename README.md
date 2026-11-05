# 🐍 PaYar (پایار) — Duolingo-Style Offline Python Learning App

**PaYar** (*Python + Yar / Companion*) is a complete, gamified beginner Python learning application designed so learners never get bored. It combines bite-sized interactive Duolingo-style lessons, milestone mini-projects after every unit, a full Capstone Game/Program Studio, and a **100% Offline Python Code Runner (`PyRunner`)**.

---

## ✨ Key Features

1. **🗺️ Gamified Duolingo-Style Skill Path (6 Units, 24 Lessons + 6 Boss Projects)**
   - **Varied Interactive Exercises**: Concept cards with live runnable code, Multiple-choice challenges, Tap-to-assemble Python token tiles, Spot-the-Bug challenges, and Live Code Verification.
   - **Unit Milestone Boss Projects**: After finishing lessons in each unit, learners build a real mini-project based on what they just learned:
     - *Unit 1 Boss*: **Smart Café Receipt & Tip Calculator**
     - *Unit 2 Boss*: **Dragon Cave Decision Adventure**
     - *Unit 3 Boss*: **Secret Vault Codebreaker**
     - *Unit 4 Boss*: **RPG Hero Inventory System**
     - *Unit 5 Boss*: **Secret Spy Cipher Machine**
     - *Unit 6 Boss*: **Mini Arcade Score & Combo Engine**

2. **🛠️ Capstone Game & Program Studio (6 Complete Projects)**
   - Step-by-step guided projects with starter templates, hints, automated test checks, and live interactive previews:
     1. 🎮 **Number Quest (Higher/Lower AI Game)**
     2. ✊ **Rock-Paper-Scissors Tournament Bot**
     3. 🐍 **ASCII Dungeon Treasure Crawler**
     4. 🔐 **Cyber Password Generator & Auditor**
     5. 📝 **Smart Todo & Study XP Planner**
     6. ❌⭕ **Tic-Tac-Toe Board Engine**

3. **💻 100% Offline Python Code Runner (`PyRunner`)**
   - Runs completely offline inside the Android APK and browser with zero internet required.
   - Supports variables, arithmetic, strings, `f-strings`, `if/elif/else`, `for` & `while` loops, `range()`, `lists`, `dicts`, functions (`def`, `return`, recursion), list comprehensions, `try/except`, and built-in `random` & `math` modules.
   - Includes a **Mobile Quick-Keys Bar** (`def`, `for`, `if`, `print()`, `:`, `()`, `[]`, `""`, `Tab`), **Live Variable Inspector**, and **8 Pre-loaded Templates**.

4. **🏆 Full Gamification & Bilingual UI (`English` / `فارسی`)**
   - Daily Streaks 🔥, Hearts ❤️, PyGems 💎, XP Levels ⚡, Sound Effects 🔊,Mascot Outfits 🧙‍♂️, Daily Quests, and the Emerald League Leaderboard.

---

## 📦 Building the Android APK (GitHub Actions)

This repository includes `.github/workflows/build-apk.yml` which automatically compiles both **Debug** and **Signed Release** APKs (`PaYar-Python-v1.0.0-Release.apk`) and publishes them directly to **GitHub Releases** on every push to `main`.
