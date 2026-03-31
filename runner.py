import time
import subprocess

INTERVAL = 300  # change to 60 if you want 1 min

while True:
    start = time.time()

    print("Running BMS checker...")
    subprocess.run(["uv", "run", "main.py"])

    elapsed = time.time() - start
    sleep_time = max(0, INTERVAL - elapsed)

    print(f"Sleeping for {sleep_time} seconds...\n")
    time.sleep(sleep_time)
