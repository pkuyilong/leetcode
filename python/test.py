import logging
import time
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.info(time.time())
    print(time.localtime())


