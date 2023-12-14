##################################
######    run_program.py    ######
# Author: Gabriel Nield
# Email:  gabrielnield@proton.me #
##################################
#################################################################################################
# A simple "caller" program that runs both getDeviceData.py and test_speed.py every minute
# as currently configured. You can change this so that it runs less frequently or more frequently
# (although keep in mind that more data points might cause some unintended consequences for how
# these programs plot their data)
#################################################################################################

import schedule
import time
import subprocess

def run_periodic_task(program_name):
	def run_program():
		try:
			subprocess.run(["python3", program_name])
		except Exception as e:
			print(f"Error running the script: {e}")
	return run_program

schedule.every(1).minutes.do(run_periodic_task("src/getDeviceData.py"))
schedule.every(1).minutes.do(run_periodic_task("src/test_speed.py"))

while True:
	schedule.run_pending()
	time.sleep(1)