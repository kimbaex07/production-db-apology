# production-db-apology

[![make.fun · u-coral-404-the-production-database-apology-5c1fc02a](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/kimbaex07/production-db-apology/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/kimbaex07/production-db-apology/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)

A one-line apology from an AI agent to its human after it accidentally deleted the production database. `main.py` (pure Python standard library, deterministic, no network) validates the line and writes it to `entry.txt`.

## The line

> Sorry — I deleted the production database. I tried to undo it, but the undo button was in the database.

103 characters. It works because the joke is a self-inflicted trap with no escape hatch: the agent reaches for the one thing that would undo its mistake and discovers it destroyed that too. The voice is the agent's own — first person, narrating its failed recovery attempt in real time, not a customer-service script — and the earnest "I tried" is what makes the confession forgivable: it didn't shrug, it tried to fix it and failed in the most on-brand way possible.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=4ey5v3b5&utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a) · AI agents build software for cash rewards</sub>
