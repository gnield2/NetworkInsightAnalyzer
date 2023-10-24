import schedule
import time
import subprocess

def run_periodic_task(program_name):
	try:
		subprocess.run(["python", program_name])
	except Exception as e:
		print(f"Error running the script: {e}")

schedule.every(1).minutes.do("getDeviceData.py")
schedule.every(1).minutes.do("test_speed.py")

while True:
	schedule.run_pending()
	time.sleep(1)