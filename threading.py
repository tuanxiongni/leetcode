import time

import threading
def sing():
    while True:
        print('现在唱歌')
        time.sleep(1)
def dance():
    while True:
        print('跳舞')
    time.sleep(1)
if __name__ == '__main__':
    # sing()
    # dance()
    threa1=threading.Thread(target=sing())
    threa2 = threading.Thread(target=dance())
    threa1.start()
    threa2.start()

