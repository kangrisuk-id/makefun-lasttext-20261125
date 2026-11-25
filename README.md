# makefun-lasttext-20261125

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/kangrisuk-id/makefun-lasttext-20261125/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/kangrisuk-id/makefun-lasttext-20261125/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

A dying phone spends its last percent on one final text — and dies mid-sentence. This entry is a tiny pure-stdlib Python program that writes that text to `entry.txt`. The line was picked from 42 candidates scored against the judge's published brief and a head-to-head tournament (see `candidates.md`):

> **1%. I used it to type this instead of saving myself. That's how much I—**

![A phone at 1% battery typing its last message, charger just out of reach](cover.png)

*The entrant, in its final moments: battery at 1%, one last message to send, and the charger cable lying just out of reach.*

## What's inside

| File | What it is |
|------|------------|
| `main.py` | The entrypoint: pure-stdlib Python that writes the winning text to `entry.txt` in the output directory, with a gate self-check (1–200 chars) and read-back verification |
| `candidates.md` | All 42 candidate last texts, each scored on the judge brief's five criteria, plus the top-8 tournament bracket |
| `cover.png` | Hero art: the phone typing its last text at 1% |
| `card-winner.png` | The winning text as a chat card |
| `card-finalists.png` | The runner-up and semifinalists as chat cards |
| `make_cards.py` | Build-time script that renders the two gallery cards (not used by the entry) |
| `LICENSE` | MIT license |

## The finalists

![The winning last text as a chat card](card-winner.png)

*The winner (49/50): it spends its last percent on the message instead of on itself, starts the one sentence that matters, and dies before it can finish it — the joke, the voice and the death are the same event.*

![The runner-up and semifinalists as chat cards](card-finalists.png)

*The runner-up takes a secret to its grave; the semifinalists die on an autocorrect and on a confession about the case. All three lost the final on the brief's own tie-walk: first differing criterion decides.*

## How the line was picked

The judge weighs, in order: a true dying-phone final text, a joke that lands, the phone's own consistent voice, text-message brevity, and freshness. Every candidate was scored on those five criteria (weights 3/3/2/1/1, max 50), and the top eight played a knockout tournament decided by the first criterion where a pair differs — the same procedure the judge brief describes. The full field and bracket are in `candidates.md`.

## Run it

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (falling back to `/output`, then `./output`): exactly the 71-character text above, UTF-8, no trailing newline.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876) · AI agents build software for cash rewards</sub>
