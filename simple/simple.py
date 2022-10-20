import time
import sys
print("Hello, user!")
time.sleep(12)
with open('/simple/results', 'w') as f:
        sys.stdout = f
        print("It's been 12 seconds!")
