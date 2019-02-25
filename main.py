import Threads
import queue
import time
def convert():
	que480 = queue.Queue()
	que720 = queue.Queue()
	endqueue1 = queue.Queue()
	endqueue2 = queue.Queue()

	in_thread = Threads.get_in(que480,que720)
	conv_720 = Threads.Convert720(que720,endqueue1)
	conv_480 = Threads.Convert480(que480,endqueue2)
	conv_720.start()
	conv_480.start()
	in_thread.start()
	while True:
		if (not endqueue1.empty()) and (not endqueue2.empty()):
			print('All Done')
			return 0
		time.sleep(1)


	

if __name__ == '__main__':
	convert()