from __future__ import print_function
from threading import Semaphore, Lock, Thread
from random import random, randint
from time import sleep, time
from timeit import Timer
import sys

class Lightswitch:
	def __init__(self):
		self.mutex = Lock()
		self.count = 0

	def lock(self, sem):
		with self.mutex:
			self.count += 1
			if self.count == 1:
				sem.acquire()

	def unlock(self, sem):
		with self.mutex:
			self.count -= 1
			if self.count == 0:
				sem.release()

def act_as_baboon(my_id, init_side):
	global MAX_CROSS
	side = init_side
	start = time()
	while times_across[my_id] < MAX_CROSS:
		with turnstile:
			switches[side].lock(rope)
		with multiplex:
			#print('baboon', my_id, 'crossing from', side_names[side])
			sleep(random() * 5)  # simulate crossing
		switches[side].unlock(rope)
		side = 1 - side
		times_across[my_id] += 1
	tt = time()-start
	print("Baboon ", my_id, " Finished in ", tt, "s")
	return tt

ROPE_MAX	= 5
NUM_BABOONS = 10
MAX_CROSS = 3
side_names  = ['west', 'east']
times_across = list()

def runTest():
	global time_across
	time_across = list()
	for i in range(NUM_BABOONS):
		times_across.append(0)
	print(time_across)
	bthreads   = []
	for i in range(NUM_BABOONS):
		bid, bside = i, randint(0, 1)
		bthreads.append(Thread(target=act_as_baboon, args=[bid, bside]))

	for t in bthreads:
		t.start()
	for t in bthreads:
		t.join()



if __name__ == '__main__':
	rope	   = Lock()
	turnstile  = Lock()
	switches   = [Lightswitch(), Lightswitch()]
	multiplex  = Semaphore(ROPE_MAX)
	print("Timing 3 runs 10 baboons crossing 50 times")

	timer = Timer(runTest)
	elapTime = timer.timeit(3)
	print("Total time = ", elapTime, "s")
	print("Average time per run = ", elapTime/3, "s")

