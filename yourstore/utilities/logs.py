import logging
import time


class Logger:

    def __int__(self,logger,file_level=logging.INFO):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt=logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] -[%(levelname)s - %?(message)s')

        currt_time=time.strftime("%Y-%m-%d")
        self.Loffilename='..\\logs\\log' + currt_time +'.txt'

        fh=logging.FileHandler(self.Loffilename,mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)












def log():
    logging.basicConfig(filename="..\\logs\\logfile.log",
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:S %p',
                        level=logging.INFO)

    logger = logging.getLogger()
    return logger

logger=log()
logger.info("this is our first ")


