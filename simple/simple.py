import time
import sys

tts = 25

print("Hello, user!")
time.sleep(tts)
with open('/simple/results', 'w') as f:
        sys.stdout = f
        print(f"It's been {tts} seconds!")
