import time
import sys
print("Hello, user!")
time.sleep(9)
with open('/simple/results', 'w') as f:
        sys.stdout = f
        print("It's been 9 seconds!")
