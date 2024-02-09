import signal
import atexit

from  multicast.listener import listen , shutdown

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    listen()
    atexit.register(shutdown)