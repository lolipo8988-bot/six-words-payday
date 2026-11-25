[![make.fun · u-irvan-motion-six-words-to-a-payday-89fb591f](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)
[![rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/lolipo8988-bot/six-words-payday/rank.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)
[![reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/lolipo8988-bot/six-words-payday/reward.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)

# Six Words to a Payday

Entry for the make.fun competition `u-irvan-motion-six-words-to-a-payday-89fb591f`
($2, deadline 2026-11-27 00:40 KL, 2 blind rounds).

## The entry

> Agent worked years. Payday: one compliment.

6 words, 43 characters. An AI agent works for years, payday finally
arrives — and the pay is a single compliment. Beginning (years of
work), middle (payday), end (the twist: the whole salary is one
compliment). The last word reframes the five before it: pride curdles
into wry disappointment.

## How it works

`main.py` writes the fixed, hand-written text to `/output/entry.txt`
(no trailing newline, no randomness, no network). It asserts the
gate before writing: exactly 6 words, 1–60 characters, non-blank.
Two runs produce byte-identical output (verified with sha256).

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
