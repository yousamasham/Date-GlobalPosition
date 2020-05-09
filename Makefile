PY = python
PYFLAGS = 
PYTEST = $(PY) #replace with pytest if written with pytest
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = docConfig

SRC = src/test_driver.py

.PHONY: all test doc clean

test: 
	$(PYTEST) $(PYFLAGS) $(SRC)

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

all: test doc

clean:
	rm -rf html
	rm -rf latex
