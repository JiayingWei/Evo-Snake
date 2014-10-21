"""<title>Hello World</title>
The simplest possble gui app that can be made.
Unfortunately, you have to CTRL-C from the command line to quit it.
GUI will initialize the screen for you.
"""

import time

start = time.time()
end = start
for counter in range(6):
	while end - start < 6:
		end = time.time()
	start = time.time()
	print counter + 1
