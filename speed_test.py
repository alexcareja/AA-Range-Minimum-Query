from functools import wraps
from time import time
from Input_Class import Input
from rmq_sparse import RMQSparse

def speedTest(fn):
	@wraps(fn)
	def wrapper(*args):
		start_time = time()
		result = fn(*args)
		end_time = time()
		print(f"Executing {fn.__name__}")
		print(f"Time elapsed: {end_time - start_time}\n")
		return result
	return wrapper

@speedTest
def preprocessSparseTable(sparse, *args):
	print("Preprocessing")
	sparse.preprocess()

@speedTest
def answerQueries(sparse, indexes, *args):
	print("Answering queries")
	for (x, y) in indexes:
		sparse.RMQ(x, y)

inp = Input()
inp.readData("test10.in")
sparse = RMQSparse(inp.getVector())
#sparse.preprocess()
preprocessSparseTable(sparse)
answerQueries(sparse, inp.getIndexes())