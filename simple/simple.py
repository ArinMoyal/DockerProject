import time
import sys

tts = 7

print("Hello, user!")
time.sleep(tts)
with open('/simple/results', 'w') as f:
        sys.stdout = f
        print(f"It's been {tts} seconds!")
