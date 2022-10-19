import time
import sys
print("Hello, user!")
time.sleep(5)
with open('/simple/results', 'w') as f:
        sys.stdout = f
        print("It's been 5 seconds!")
