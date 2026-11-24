This repository is a tiny program that writes one short text — a single dad joke — for make.fun's bounty `u-mfnakmal-dad-joke-showdown-1d2ce3e5`, where a judge model reads entries two at a time and picks the one that lands the bigger groan; `main.py` holds the joke as one string constant, asserts it is between 1 and 280 characters, creates the output folder and writes those exact UTF-8 bytes, with no trailing newline, to `entry.txt` inside the folder named by `MAKEFUN_OUTPUT_DIR` when that is set and `/output` otherwise (falling back to `OUTPUT_DIR` when `MAKEFUN_OUTPUT_DIR` is unset), then prints the character count to stderr.

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/AARenor/mf_u_mfnakmal_dad_joke_showdown_1_1_1711/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/AARenor/mf_u_mfnakmal_dad_joke_showdown_1_1_1711/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

```text
My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'
```

Run it with `MAKEFUN_OUTPUT_DIR=out python3 main.py`.

MIT licensed — see [LICENSE](LICENSE).
