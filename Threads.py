import threading
import time
import subprocess

class get_in(threading.Thread):
	"""Threads to get input from a file consist of video names."""
	def __init__(self,o,o1,o2):
		threading.Thread.__init__(self)
		self.o = o
		self.o1 = o1
		self.o2 = o2
	def run(self):
		print("Input Thread Start")
		while True:
			if not self.o.empty():
				data = self.o.get()
				self.o1.put(data)
				self.o2.put(data)
				if data == 'quit':
					break
			else:
				time.sleep(1)

class Convert480 (threading.Thread):
	"""Threads to convert video into 480p"""
	def __init__(self,input_queue,endqueue):
		threading.Thread.__init__(self)
		self.endqueue = endqueue
		self.input_queue = input_queue
		self.count = 0
	def run(self):
		print("480 Thread Start")
		while True:
			if not self.input_queue.empty():
				Input = self.input_queue.get()
				if Input == 'quit':
					self.endqueue.put("Ex")
					break
				else:
					file_path = Input
					self.count += 1
					command=['ffmpeg','-i',file_path,'-y','-b','1M','-r','30','-f','mp4','-s','640x480','-loglevel','quiet',file_path[:-4]+"480p"+file_path[-4:]]
					subprocess.Popen(command)
					time.sleep(3)
					print(file_path + 'to 480p Finished.\n'+str(self.count)+" Done."+str(self.input_queue.qsize()-1) +" Left.")
					
			else:
				time.sleep(3)
			

		print('480 Thread Stop')


class Convert720 (threading.Thread):
	"""Threads to convert video into 720p"""
	def __init__(self,input_queue,endqueue):
		threading.Thread.__init__(self)
		self.input_queue = input_queue
		self.endqueue = endqueue
		self.count = 0
	def run(self):
		print("720 Thread Start")
		while True:
			if not self.input_queue.empty():
				Input = self.input_queue.get()
				if Input == 'quit':
					self.endqueue.put("Ex")
					break
				else:
					file_path = Input
					self.count += 1
					command=['ffmpeg','-i',file_path,'-y','-b','2M','-r','30','-f','mp4','-s','1280x720','-loglevel','quiet',file_path[:-4]+"720p"+file_path[-4:]]
					subprocess.Popen(command)
					time.sleep(3)
					print(file_path + 'to 720p Finished.\n'+str(self.count)+" Done."+str(self.input_queue.qsize()-1) +" Left.")
			else:
				time.sleep(3)
			
		print('720 Thread Stop')
