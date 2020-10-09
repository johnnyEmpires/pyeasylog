# pyeasylog


If you don't like setting up your logger each time you make a simple project, here is a quick setup of Python's logging module. Good for day to day scripting. Just install, import and a line of code, your logger will be configured and you're good to go.


## Installation

1. Clone the package or clone the repository.
2. Change directory where `setup.py` is.
3. Use `pip` to install, mind the dot (.)
```
pip instal .
```

## Usage

```python
import time
from pyeasylog import module_logger

_log = module_logger(__name__)

def main():
    try:
        while True:
            try:
                time.sleep(1)
                _log.info('application is running...')

            except KeyboardInterrupt:
                _log.info('script has terminated')

    except KeyboardInterrupt:
        _log.info('an error occurred')


if __name__ == '__main__':
    main()

```

* Logging levels are the same levels from Python [logging module](https://docs.python.org/2/library/logging.html#logging-levels).
* A `Log` folder will be automatically created to contain the logs.
* If `DEBUG` file exists in the same directory as the main code, DEBUG levels will be shown in the console.


## TODO

* log color in console
