import time

print('Press ENTER to begin, Press Ctrl + C to stop')
while True:
	try:
		input()
		start_time = time.time()
		print('Started')
		while True:
			print('Time Elapsed: ', round(time.time()-start_time, 2), 'secs', end='\r')
	except KeyboardInterrupt:
		print('Stopped')
		end_time = time.time()
		print('Total Time:', round(end_time-start_time, 2), 'secs')
		break
