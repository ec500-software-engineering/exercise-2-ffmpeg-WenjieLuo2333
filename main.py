import threading
import time
import Threads
import queue
import threading

def main():
	que480 = queue.Queue()
	que720 = queue.Queue()

	in_thread = Threads.get_in(que480,que720)
	conv_720 = Threads.Convert720(que720)
	conv_480 = Threads.Convert480(que480)
	conv_720.start()
	conv_480.start()
	in_thread.start()


	

if __name__ == '__main__':
	main()