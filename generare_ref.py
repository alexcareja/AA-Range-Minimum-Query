from rmq_banal import RMQ_banal
from Input_Class import Input

inp = Input()
for t in range(11):
	inp.readData(f"in/test{t}.in")
	with open(f"ref/test{t}.ref", "w") as file:
		for (x, y) in inp.getIndexes():
			result = RMQ_banal(inp.getVector(), x, y)
			file.write(str(result))
			file.write("\n")