# creates tab-separated log files. by: John @_@
# created: May 17, 2020

import logging
import logging.handlers as lh
import os
import time

DBG = False
if 'DEBUG' in os.listdir(os.getcwd()):
    DBG = True
    # print('DEBUG mode enabled!')


fmt = []
fmt.append('%(asctime)s')
fmt.append('%(relativeCreated)3d')
fmt.append('%(name)s')
fmt.append('%(levelname)s') 
fmt.append('%(threadName)s') 
# fmt.append('%(filename)s') 
fmt.append('%(lineno)d') 
fmt.append('%(funcName)s')
fmt.append('%(message)s') 
# fmt.append('%(sinfo)s')

str_fmt = ' '.join(fmt)


formatter_fh = logging.Formatter('\t'.join(fmt))
formatter_ch = logging.Formatter('\t'.join((fmt[0], fmt[1], fmt[3] ,fmt[7])))

date_marker = time.strftime('%Y-%m-%d', time.localtime(time.time()))
log_to_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_to_dir, exist_ok=True)
log_to_file = os.path.join(log_to_dir, f'app_{date_marker}.log')


class CustomStreamHandler(logging.StreamHandler):
    """
    Customized stream handler to override emit method
    """

    def emit(self, record):
        try:
            msg = self.format(record)

            # prevent cmd from complaing when logging latin characters
            msg = msg.replace('á', 'a')
            msg = msg.replace('é', 'e')
            msg = msg.replace('ó', 'o')

            stream = self.stream
            stream.write(msg)
            stream.write(self.terminator)
            self.flush()

        except Exception:
            self.handleError(record)


class CustomTRH(lh.TimedRotatingFileHandler):
    """
    Reimplement emit
    """

    def emit(self, record):
        """
        emit implementation MRO:
        -----------------------
        StreamHandler.emit
        FileHandler.emit
        BaseRotatingHandler.emit
        TimedRotatingFileHandler.emit
        CustomTRH.emit
        CustomStreamHandler.emit
        """
        try:
            # based from StreamHandler
            if self.stream is None:
                self.stream = self._open()
            # based from BaseRotatingHandler
            if self.shouldRollover(record):
                self.doRollover()
            CustomStreamHandler.emit(self, record)
        except Exception:
            self.handleError(record)


def module_logger(logger_name):
    custom_logger = logging.getLogger(logger_name)

    custom_logger.setLevel(logging.DEBUG)
    file_handler = CustomTRH(filename=log_to_file, when='D',
    interval=1, backupCount=30)
    file_handler.setFormatter(formatter_fh)
    file_handler.setLevel(logging.DEBUG)
    custom_logger.addHandler(file_handler)
    console_handler = CustomStreamHandler()
    # console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter_ch)

    if DBG:
        console_handler.setLevel(logging.DEBUG)
    else:
        console_handler.setLevel(logging.INFO)
    
    custom_logger.addHandler(console_handler)
    custom_logger.debug(f'from module logger - DBG : {DBG}')
    custom_logger.debug(f'logger initiated. saving log in {log_to_file}')

    return custom_logger



def main():

    _log = module_logger(__name__)

    try:
        counter = 0

        while True:
            try:
                counter += 1
                time.sleep(1)
                _log.info(f'application is running...{counter}')
                _log.debug('console debug mode')

                if counter > 5:
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