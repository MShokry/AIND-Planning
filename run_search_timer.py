import time
import signal
from run_search import *
timeout = time.time() + 60*5 # 5 Minutes sleep

def handle(signum,frame):
	raise TimeoutError()
	#raise Exception("Time Up exeeded 7 Minutes")


#signal.alarm(7*60)

for i in range(1,11):
	start = timer()
	signal.signal(signal.SIGALRM,handle)
	signal.alarm(10*60)
	try :
		main("3","%s" %i)
		#os.system("python run_search.py -p 3 -s 2 ")
	except :
		end = timer()
		print ("### Time Up exeeded 10 Minutes ###", end-start)
		continue
		signal.alarm(0)
	signal.alarm(0)

