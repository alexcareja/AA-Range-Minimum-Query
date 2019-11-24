.phony: run clean

test: run clean

run:
	python3 ./test_algo.py sparse
	python3 ./test_algo.py cartesian
	python3 ./test_algo.py segment

speed:
	python3 ./speed_test.py cartesian
	python3 ./speed_test.py segment
	python3 ./speed_test.py sparse

speed_basic:
	python3 ./speed_test.py basic

clean:
	rm *.out
