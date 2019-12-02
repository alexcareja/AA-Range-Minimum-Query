from functools import wraps
from time import time
from Input_Class import Input
from rmq_sparse import RMQSparse
from farach_colton_bender import RMQFCB
from segment_tree import RMQSegment

def speedTest(fn):
	@wraps(fn)
	def wrapper(*args):
		start_time = time()
		result = fn(*args)
		end_time = time()
		#print(f"Executing {fn.__name__}")
		print(f"Time elapsed: {end_time - start_time}\n")
		return result
	return wrapper

@speedTest
def preprocessAlgo(algo, *args):
	print("Preprocessing")
	algo.preprocess()

@speedTest
def answerQueries(algo, indexes, *args):
	print("Answering queries")
	for (x, y) in indexes:
		algo.RMQ(x, y)

inp = Input()
inp.readData("in/test10.in")
sparse = RMQSegment(inp.getVector())
preprocessAlgo(sparse)
answerQueries(sparse, inp.getIndexes())