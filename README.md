[![PyPI Version][pypi-image]][pypi-url]
[![pre-commit.ci Status][pre-commit-ci-image]][pre-commit-ci-url]
[![Build Status][build-image]][build-url]

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/aiopvpc
[pypi-url]: https://pypi.org/project/aiopvpc/
[pre-commit-ci-image]: https://results.pre-commit.ci/badge/github/azogue/aiopvpc/master.svg
[pre-commit-ci-url]: https://results.pre-commit.ci/latest/github/azogue/aiopvpc/master
[build-image]: https://github.com/azogue/aiopvpc/actions/workflows/main.yml/badge.svg
[build-url]: https://github.com/azogue/aiopvpc/actions/workflows/main.yml

# aio-pvpc

_This is a fork of the, now abandoned, [aiopvpc](https://github.com/azogue/aiopvpc) library from
[azogue](https://github.com/azogue). Plese, take note that I expect to improve and do a deep change on this library in the near future._

Simple aio library to download Spanish electricity hourly voluntary prices for the small consumer
(PVPC initials in Spanish). More info in [REE official page](https://www.ree.es/es/operacion/sistema-electrico/pvpc).

Made to support the [**`pvpc_hourly_pricing`** HomeAssistant integration](https://www.home-assistant.io/integrations/pvpc_hourly_pricing/).

<span class="badge-buymeacoffee"><a href="https://www.buymeacoffee.com/chiro79" title="Donate to this project using Buy Me A Coffee"><img src="https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg" alt="Buy Me A Coffee donate button" /></a></span>

_Or to the [original library developer](https://www.buymeacoffee.com/azogue)_

## Install

Install with `pip install aio-pvpc` or clone it to run tests or anything else.

## Usage

```python
import aiohttp
from datetime import datetime, timezone
from aio_pvpc import PVPCData

async with aiohttp.ClientSession() as session:
    pvpc_handler = PVPCData(session=session, tariff="2.0TD")
    esios_data = await pvpc_handler.async_update_all(
        current_data=None, now=datetime.now(timezone.utc)
    )
print(esios_data.sensors["PVPC"])
```
