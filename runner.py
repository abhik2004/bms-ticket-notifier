import time
import random
import subprocess

INTERVAL = 420  # change to 60 if you want 1 min

while True:
    start = time.time()

    print("Running BMS checker...")
    subprocess.run(["uv", "run", "main.py"])

    elapsed = time.time() - start

    jitter = random.randint(-60, 60)  # +/- 1 min
    sleep_time = max(60, INTERVAL + jitter - elapsed)

    print(f"Sleeping for {sleep_time} seconds...\n")
    time.sleep(sleep_time)
