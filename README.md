# Advent-of-Code-2021

My solutions to [Advent of Code 2021](https://adventofcode.com/2021)

**SPOILER ALERT:** This repository contains contest solutions. The solutions will be
uploaded at least 30 minutes after the start of each day's contest.

## Stats

### By Day

| Day                          | Level 1 Rank | Level 2 Rank | Note                                                 |
| :--------------------------- | :----------: | :----------: | :--------------------------------------------------- |
| 01 (Sonar Sweep)             |     3602     |     2000     |                                                      |
| 02 (Dive!)                   |     2719     |     1438     |                                                      |
| 03 (Binary Diagnostic)       |     2266     |     372      |                                                      |
| 04 (Giant Squid)             |     642      |     763      |                                                      |
| 05 (Hydrothermal Venture)    |     506      |     418      |                                                      |
| 06 (Lanternfish)             |     787      |     105      |                                                      |
| 07 (The Treachery of Whales) |     1207     |     421      |                                                      |
| 08 (Seven Segment Search)    |     681      |     733      |                                                      |
| 09 (Smoke Basin)             |     1712     |     1571     |                                                      |
| 10 (Syntax Scoring)          |     599      |     466      |                                                      |
| 11 (Dumbo Octopus)           |     1762     |     1553     |                                                      |
| 12 (Passage Pathing)         |     721      |     1779     |                                                      |
| 13 (Transparent Origami)     |     628      |     667      |                                                      |
| 14 (Extended Polymerization) |     379      |     2804     |                                                      |
| 15 (Chiton)                  |     3920     |     2898     |                                                      |
| 16 (Packet Decoder)          |     1212     |     954      |                                                      |
| 17 (Trick Shot)              |     129      |     2436     |                                                      |
| 18 (Snailfish)               |     1033     |     1200     |                                                      |
| 19 (Beacon Scanner)          |    10945     |    10675     | Inefficient solution                                 |
| 20 (Trench Map)              |     255      |     263      | Analysis TBD                                         |
| 21 (Dirac Dics)              |     546      |     1058     | Analysis TBD                                         |
| 22 (Reactor Reboot)          |     1020     |     9160     | Inefficient solution                                 |
| 23 (Amphipod)                |      13      |     1254     | Inefficient solution; Part 1 originally done by hand |
| 24 (Arithmetic Logic Unit)   |     1177     |     1073     | Inefficent solution; Originally done by hand         |
| 25 (Sea Cucumber)            |     906      |     789      | Analysis TBD                                         |

### By Leaderboard (after Day 02)

| Leaderboard |   Score   |   Rank   |
| :---------- | :-------: | :------: |
| Worldwide   |  **88**   | **>100** |
| PyDis       | **45598** |  **14**  |
| PyDis Staff | **2988**  |  **2**   |

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
