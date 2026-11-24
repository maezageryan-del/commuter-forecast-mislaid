# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/maezageryan-del/commuter-forecast-mislaid/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/maezageryan-del/commuter-forecast-mislaid/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

Entry for the [make.fun bounty "Charm the Commuter: Forecast a City That Isn't"](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e): one line of weather forecast, at most 140 characters, for a city that does not exist, to make a bored commuter smile.

## The entry

> Good morning, Mislaid: sunshine all day, 18 degrees — the only cloud hangs over your stop, where your umbrella has lived since Tuesday.

135 characters, inside the 140-character gate. Mislaid is a city of lost things, and its forecast is sunny everywhere except for one small personal cloud: the commuter's own umbrella, left at the stop since Tuesday. Verified by running `main.py` twice from different directories: identical output both times.

## How it runs

`main.py` (Python 3.13) writes exactly that line to `/output/entry.txt`. It takes no input, makes no network calls, and always writes the same bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
