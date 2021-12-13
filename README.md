# Advent-of-Code-2021

My solutions to [Advent of Code 2021](https://adventofcode.com/2021)

**SPOILER ALERT:** This repository contains contest solutions. The solutions will be
uploaded at least 30 minutes after the start of each day's contest.

## Stats

### By Day

| Day                          | Level 1 Rank | Level 2 Rank |
| :--------------------------- | :----------: | :----------: |
| 01 (Sonar Sweep)             |     3602     |     2000     |
| 02 (Dive!)                   |     2719     |     1438     |
| 03 (Binary Diagnostic)       |     2266     |     372      |
| 04 (Giant Squid)             |     642      |     763      |
| 05 (Hydrothermal Venture)    |     506      |     418      |
| 06 (Lanternfish)             |     787      |     105      |
| 07 (The Treachery of Whales) |     1207     |     421      |
| 08 (Seven Segment Search)    |     681      |     733      |
| 09 (Smoke Basin)             |     1712     |     1571     |
| 10 (Syntax Scoring)          |     599      |     466      |
| 11 (Dumbo Octopus)           |     1762     |     1553     |
| 12 (Passage Pathing)         |     721      |     1779     |
| 13 (Transparent Origami)     |     628      |     667      |

### By Leaderboard (after Day 02)

| Leaderboard |   Score   |    Rank     |
| :---------- | :-------: | :---------: |
| Worldwide   |   **0**   | **unknown** |
| PyDis       | **23124** |   **10**    |
| PyDis Staff | **1551**  |    **5**    |

## How to Use this Repo?

1. Create a `config.yml` in the root of this repository. Put your AoC token in. You can
   find the token when you inspect the request cookies on AoC's website when you're
   logged in. Put it in `config.yml` as:

   ```yaml
   cookies:
     session: 'Your session key'
   ```

2. Create a virtual environment and install the dependencies in `requirements.txt`
3. To download an input, run `python run.py d <day>`
4. To print calculated result for part 1/2, run `python run.py p <day> 1|2`
5. To submit calculated result for part 1/2, run `python run.py s <day> 1|2`
