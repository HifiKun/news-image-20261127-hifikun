# news-image-20261127-hifikun

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/HifiKun/news-image-20261127-hifikun/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/HifiKun/news-image-20261127-hifikun/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

A newspaper front page that sums up Friday 27 November 2026 in one image: the drone strike in Kuwait that killed two Italian workers, the Gaza strikes, the Gukesh–Sindarov marathon draw in the World Chess Championship, the storm that postponed the 100th Macy's Thanksgiving Day Parade, and six more stories from the day — drawn from scratch with Pillow.

## Run it

```sh
python3 draw_front.py   # redraws entry.png (needs Pillow, local use only)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is the entrypoint the grader runs: it copies `entry.png` to the output directory using only the Python standard library. `draw_front.py` is the script that drew the image; it is not run by the grader.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6a1ay90r&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>
