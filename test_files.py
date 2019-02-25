import subprocess
import json
import main
from pytest import approx
def test_video():
	#foloowing subprocess function borrowed from exercise-2-ffmpeg-zywan
	ori_log = json.loads(subprocess.check_output(['ffprobe', '-v', 'warning','-print_format', 'json','-show_format','video.mp4']))
	main.convert()
	log480 = json.loads(subprocess.check_output(['ffprobe', '-v', 'warning',
									'-print_format', 'json',
									'-show_format',
									'video480p.mp4']))
	log720 = json.loads(subprocess.check_output(['ffprobe', '-v', 'warning',
									'-print_format', 'json',
									'-show_format',
									'video720p.mp4']))
	ori_duration = float(ori_log['format']['duration'])
	duration480 = float(log480['format']['duration'])
	duration720 = float(log720['format']['duration'])
	assert ori_duration == approx(duration480,abs=1e-1)
	assert ori_duration == approx(duration720,abs=1e-1)
	print("All test passed")

if __name__ == '__main__':
	test_video()
