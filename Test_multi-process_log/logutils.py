# import logging
import logging.handlers
import queue


class LOGUTILS:
    def __init__(self):
        self.queue = queue.Queue()

    def stream_handler(self):
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(levelname)s %(filename)s %(process)d %(thread)d  %(threadName)s: %(message)s')
        handler.setFormatter(formatter)
        handler.setLevel(logging.WARNING)
        return handler

    def file_handler(self):
        handler = logging.FileHandler("qhql.log")
        formatter = logging.Formatter('%(levelname)s %(filename)s %(process)d %(thread)d  %(threadName)s: %(message)s')
        handler.setFormatter(formatter)
        handler.setLevel(logging.WARNING)
        return handler

    def listener(self):
        stream_handler = self.stream_handler()
        ql = logging.handlers.QueueListener(self.queue, stream_handler, self.file_handler())
        return ql

    def queue_handler(self):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)  # Log level = DEBUG
        qh = logging.handlers.QueueHandler(self.queue)
        root.addHandler(qh)
        return root
