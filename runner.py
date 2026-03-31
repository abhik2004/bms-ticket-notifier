import time
import subprocess

INTERVAL = 300

while True:
    start = time.time()

    print("Running BMS checker...")
    subprocess.run(["python", "main.py"])

    elapsed = time.time() - start
    sleep_time = max(0, INTERVAL - elapsed)

    print(f"Sleeping for {sleep_time} seconds...\n")
    time.sleep(sleep_time)
