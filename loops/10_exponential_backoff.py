import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
	print("attempt:", attempts + 1, "wait_timme:", wait_time) 
	time.sleep(wait_time)
	attempts = attempts + 1  # also written by +=1
	wait_time = wait_time * 2 # *= 2