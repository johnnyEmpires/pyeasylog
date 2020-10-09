# easy-py-log

A minimal and quick setup logging module. Just install, import and initial and you're good to go.


## Installation

1. Clone the package or clone the repository.
2. Change directory where `setup.py` is.
3. Install using `pip`.
```shell
pip instal .
```

## Usage
```python
import time
from easylog import module_logger

_log = module_logger(__name__)

def main():
    try:
        while True:
            time.sleep(1)
            _log.info('application is running...')

    except Exception as e:
        _log.info('an error occurred')
        _log.info('script has terminated')


if __name__ == '__main__':
    main()

```