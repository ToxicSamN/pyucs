import sys
import logging
import logging.handlers


class Logger:

    loglevel = logging.INFO

    def __init__(self, log_file='/var/log/ucs.log',
                 error_log_file='/var/log/ucs_err.log',
                 log_size_MB=10, max_logs=8,
                 formatter=logging.Formatter("%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s"),
                 log_level=logging.INFO):
        self.loggers = {}
        self.log_level = log_level
        self.log_file = log_file
        self.error_log_file = error_log_file

        self.formatter = formatter
        self.logsize = log_size_MB * 1048576
        self.max_logs = max_logs

    def get_logger(self, name):

        if self.loggers.get(name):
            return self.loggers.get(name)

        logger = logging.getLogger(name)
        logger.setLevel(self.log_level)

        dfh = logging.StreamHandler(stream=sys.stdout)
        dfh.setLevel(logging.DEBUG)
        dfh.setFormatter(self.formatter)

        lfh = logging.handlers.RotatingFileHandler(self.log_file,
                                                   mode='a',
                                                   maxBytes=self.logsize,
                                                   backupCount=self.max_logs,
                                                   encoding='utf8',
                                                   delay=False)
        lfh.setLevel(logging.INFO)
        lfh.setFormatter(self.formatter)

        efh = logging.handlers.RotatingFileHandler(self.error_log_file,
                                                   mode='a',
                                                   maxBytes=self.logsize,
                                                   backupCount=self.max_logs,
                                                   encoding='utf8',
                                                   delay=False)
        efh.setLevel(logging.ERROR)
        efh.setFormatter(self.formatter)

        logger.addHandler(lfh)
        logger.addHandler(efh)

        self.loggers.update({name: logger})

        return logger
