from flask import Flask
import logging
import logging.handlers
import queue
from logutils import LOGUTILS
from module import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    root.debug('Hello World')
    root.info('Hello World')
    root.warning('Hello World')
    root.error('Hello World')
    test_1()
    return 'Hello World'


if __name__ == '__main__':
    log = LOGUTILS()
    ql = log.listener()
    root = log.queue_handler()
    ql.start()
    app.run(debug=True)
    ql.stop()
