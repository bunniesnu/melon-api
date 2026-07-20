# melon-api

An unofficial API SDK for Melon music app — a Python client for fetching, modeling, and persisting data from multiple Melon endpoints.

## Features

- **Realtime chart** — hourly chart data from `m.app.melon.com`
- **Chart report** — detailed report for a given song
- **Top100 chart** — Melon’s Top100 chart (distinct from the realtime chart)
- **Chart graph** — historical chart position data

## Requirements

- Python 3.10+

## Installation

```bash
pip install melon-api-client
```

Or with uv:

```bash
uv add melon-api-client
```

## Usage

Run the main script to fetch data from all endpoints and save results to `data/`:

```bash
uv run python main.py
```

Each response is saved as a timestamped JSON file (UTC) in the `data/` directory to avoid overwriting previous runs.

### As a library

```python
from melon.chart import MelonClient
with MelonClient() as client:
    chart = client.get_top100_chart()
```

## Development

Clone the repo and install with dev dependencies:

```bash
git clone https://github.com/bunniesnu/melon-api.git
cd melon-api
make install
```

Or manage the environment directly with uv:

```bash
uv sync --all-extras --dev   # install with dev dependencies
uv sync                      # sync environment with lockfile
uv lock                      # update the lockfile
```

Run tests (excludes live API tests by default):

```bash
make test
```

Run live tests (hits real Melon endpoints):

```bash
make test-live
```

Other available targets:

```bash
make help    # list all available targets
make clean   # remove build artifacts and caches
```

## Publishing

Build the package:

```bash
make build
```

Publish to PyPI:

```bash
make publish
```

## Project structure

```
melon-api/
├── src/melon/       # package source
├── tests/           # test suite
├── data/            # output JSON files (gitignored)
├── main.py          # example script hitting all endpoints
└── pyproject.toml
```

## Notes

- The realtime chart and chart report endpoints live on different hosts (`m.app.melon.com` vs `m2.melon.com`); each requires its own full URL.
- `PREDICTEDDATA` may be absent from chart report responses.
- Output uses `model_dump(mode="json", by_alias=True)` to preserve Melon’s original field names.

## Links

- [Repository](https://github.com/bunniesnu/melon-api)
- [PyPI](https://pypi.org/project/melon-api/)

## License

MIT