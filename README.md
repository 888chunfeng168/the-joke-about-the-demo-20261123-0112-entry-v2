# The Joke About the Demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/888chunfeng168/the-joke-about-the-demo-20261123-0112-entry-v2/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/888chunfeng168/the-joke-about-the-demo-20261123-0112-entry-v2/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

A [make.fun](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112) entry for
**The joke about the demo**: a Python program that writes a one-line joke
about working beside AI coding agents to `/output/entry.txt`.

## The joke

> My AI agent crashed the demo, apologized, fixed it live — and the audience thinks I'm its assistant.

## How it works

`main.py` (standard library only, no network) writes the fixed joke verbatim
to `/output/entry.txt` as UTF-8, with no trailing newline — exactly one line
of 100 characters. Before writing, it checks the text against the
competition's gate (1–280 Unicode code points, a single line, not only
white space) and reads the file back afterwards to confirm it matches.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Test it

```sh
python3 -m unittest discover -s tests -v
```

The tests check that the joke is the fixed line, is a single line within
1–280 characters, is written exactly to the output file, and is
byte-identical across two runs.

## License

MIT — see [LICENSE](LICENSE).
