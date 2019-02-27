import subprocess
import json
import main
import queue
from pytest import approx
class TestClass(object):
	def test_one(self):
		in_queue = queue.Queue()
		for i in range(3):
			in_queue.put('video'+str(i+1)+'.avi')
		in_queue.put('quit')
		result=check_out(in_queue)
		assert result==0

def check_out(input_queue):
	q1 = queue.Queue()
	q2 = queue.Queue()
	while not input_queue.empty():
		tmp = input_queue.get()
		q1.put(tmp)
		q2.put(tmp)
	main.convert(q1)
	while not q2.empty():
		vi = q2.get()
		if vi == 'quit':
			break
		ori_log = []
		log480 = []
		log720 = []
		ori_log = json.loads(subprocess.check_output(['ffprobe', '-v', 'warning','-print_format', 'json','-show_format',vi]))	
		while True:
			try:
				print(vi[:-4]+'480p'+vi[-4:])
				log480 = json.loads(subprocess.check_output(['ffprobe', '-v', 'warning',
										'-print_format', 'json',
										'-show_format',
										vi[:-4]+'480p'+vi[-4:]]))
				log720 = json.loads(subprocess.check_output(['ffprobe', '-v', 'warning',
										'-print_format', 'json',
										'-show_format',
										vi[:-4]+'720p'+vi[-4:]]))
				if log480 != [] and log720 != []:
					break
			except IOError:
				continue
		
		
		ori_duration = float(ori_log['format']['duration'])
		duration480 = float(log480['format']['duration'])
		duration720 = float(log720['format']['duration'])
		if not ori_duration == approx(duration480,abs=1e-1):
			return 1
		if not ori_duration == approx(duration720,abs=1e-1):
			return 1
	return 0
