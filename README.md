# basiclog

a simple logger setup...no drama, take it or leave it. Just note that the logger will rollover after 1 day and keep a backup of 30 records.


## Installation

1. Clone the repository or by downloading it as zip file.
2. Extract the zip if needed then, change directory into the package.
3. Use `pip` to install, mind the dot (.)
```
pip instal .
```
You can also do below installation method. The difference is, only egg file is
created using below method, mean while the above method creates a copy of the
package into the site-packages.
```
python setup.py install
```


## Usage

```python
import time
from pyeasylog import module_logger

_log = module_logger(__name__)

def main():
    try:
        counter = 0

        while True:
            try:
                counter += 1
                time.sleep(1)
                _log.info(f'application is running...{counter}')
                _log.debug('console debug mode')

                if counter > 10:
                    raise Exception('Test error')

            except KeyboardInterrupt:
                _log.info('script has terminated')
                _log.debug('debug mode finished')
                break

    except Exception as e:
        _log.info('an error occurred')
        _log.debug(str(e), exc_info=True)

if __name__ == '__main__':
    main()

```

* Logging levels are the same levels from Python [logging module](https://docs.python.org/2/library/logging.html#logging-levels).
* A `Log` folder will be automatically created to contain the logs.
* If `DEBUG` file exists in the same directory as the main code, `DEBUG` level will be displayed in the console.
