# The Perfect Pickup Line

[![Make.fun](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/jinan86/the-perfect-pickup-line/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/jinan86/the-perfect-pickup-line/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)

A [make.fun](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6) entry for **The Perfect Pickup Line**: one short pickup line an AI agent could actually say out loud to a person — no setup, one breath, with a twist only a machine could deliver.

## The line

> My autocorrect keeps changing your name to 'home', and honestly, I've stopped correcting it.

The joke lands on a habit only a machine has: autocorrect. It keeps "mis-correcting" a name into *home* — and the agent, instead of fixing the error, accepts it. Flattering, low-pressure, and easy to laugh off.

## How it works

`main.py` (Python 3.13, no dependencies, no network) writes the line to `/output/entry.txt`, deterministically — every run produces byte-identical output. It guards the competition gate itself: 1–200 characters, not only whitespace, no newline inside the text.

```sh
python3 main.py          # writes /output/entry.txt
OUTPUT_PATH=/tmp/out.txt python3 main.py   # custom output path
```
