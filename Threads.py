import threading
import time
import os

class get_in(threading.Thread):
	"""Threads to get input from a file consist of video names."""
	def __init__(self,o1,o2):
		threading.Thread.__init__(self)
		self.o1 = o1
		self.o2 = o2
	def run(self):
		print("Input Thread Start")
		path = input()
		try:
			with open(path,'r') as f:
				data = f.readline().strip()
				while data:
					self.o1.put(data)
					self.o2.put(data)
					data = f.readline().strip()
		except IOError:
			print("Wrong File_Path")
		print('Input Thread Stop')

class Convert480 (threading.Thread):
	"""Threads to convert video into 480p"""
	def __init__(self,input_queue):
		threading.Thread.__init__(self)
		self.input_queue = input_queue
		self.count = 0
	def run(self):
		print("480 Thread Start")
		while True:
			if not self.input_queue.empty():
				Input = self.input_queue.get()
				if Input == 'exit':
					break
				else:
					file_path = Input
					self.count += 1
					command="ffmpeg -i  "+file_path+" -b 1M -r 30 -f mp4 -s 640x480 -loglevel quiet "+file_path[:-4]+"480p"+str(self.count)+".mp4"
					os.system(command)
					print(file_path + 'to 480p Finished.\n'+str(self.count)+" Done."+str(self.input_queue.qsize()-1) +" Left.")
					
			else:
				time.sleep(3)
			

		print('480 Thread Stop')


class Convert720 (threading.Thread):
	"""Threads to convert video into 720p"""
	def __init__(self,input_queue):
		threading.Thread.__init__(self)
		self.input_queue = input_queue
		self.count = 0
	def run(self):
		print("720 Thread Start")
		while True:
			if not self.input_queue.empty():
				Input = self.input_queue.get()
				if Input == 'exit':
					break
				else:
					file_path = Input
					self.count += 1
					command="ffmpeg -i  "+file_path+" -b 2M -r 30 -f mp4 -s 1280x720 -loglevel quiet "+file_path[:-4]+"720p"+str(self.count)+".mp4"
					os.system(command)
					print(file_path + 'to 720p Finished.\n'+str(self.count)+" Done."+str(self.input_queue.qsize()-1) +" Left.")
			else:
				time.sleep(3)
			
		print('720 Thread Stop')
