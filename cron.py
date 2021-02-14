import schedule
import subprocess
import time

def job():
    subprocess.call("main.py", shell=True)
    return

schedule.every().day.at("03:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
