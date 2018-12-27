#! /usr/bin/python

import sys, time
from daemon import Daemon

class Module(Daemon):
        def run(self):
                while True:
                        time.sleep(1)
if __name__ == "__main__":
        daemon = module('/tmp/daemon-exemple.pid)

     if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)