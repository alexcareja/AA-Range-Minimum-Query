from functools import wraps
from time import time
from Input_Class import Input
from rmq_sparse import RMQSparse

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args):
		start_time = time()
		result = fn(*args)
		end_time = time()
		print(f"Executing {fn.__name__}")
		print(f"Time elapsed: {end_time - start_time}\n")
		return result
	return wrapper

@speed_test
def preprocess_Sparse_Table(sparse, *args):
	print("Preprocessing")
	sparse.preprocess()

@speed_test
def answer_Queries(sparse, indexes, *args):
	print("Answering queries")
	for (x, y) in indexes:
		sparse.RMQ(x, y)

inp = Input()
inp.readData("test10.in")
sparse = RMQSparse(inp.getVector())
#sparse.preprocess()
preprocess_Sparse_Table(sparse)
answer_Queries(sparse, inp.getIndexes())