import threading
import time
import os
import queue
import threading

class thread720p(threading.Thread):
	def __init__(self,que):
		threading.Thread.__init__(self,Inqueue)
		self.Inqueue = Inqueue
		self.thread_stop = False
	def run(self):
		while self.thread_stop is False:
			try:
				video = Inqueue.get()
				os.system("ffmpeg -i "+video+" -b 2M -r 30 -f mp4 -s 1280x720 -loglevel quiet "+str(COUNT_HQ)+"_HQ.mp4")
			except IOError:
				print("Wrong File_Path")
		print('Input Thread Stop')



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