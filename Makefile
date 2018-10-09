PROJECT=Recursion
AUTHOR11=Emilie 
AUTHOR12=Pathammavong
AUTHOR21=Oliver 
AUTHOR22=Irwin
PYTHONPATH=./src
export PYTHONPATH
SPHINXBUILD=python3 -m sphinx
CONFIGPATH=.
SOURCEDOC=sourcedoc
DOC=doc

.PHONY: clean doc archive author

clean:
	rm -f *~ */*~
	rm -rf __pycache__ src/__pycache__
	rm -rf $(DOC)
	rm -f "$(PROJECT) - $(AUTHOR12) & $(AUTHOR22)".zip

doc: author
	$(SPHINXBUILD) -c $(CONFIGPATH) -b html $(SOURCEDOC) $(DOC)

archive: clean
	zip -r "$(PROJECT) - $(AUTHOR12) & $(AUTHOR22)".zip .


author:
	sed -i -e 's/^project =.*/project = "$(PROJECT)"/g' conf.py
	sed -i -e 's/^copyright =.*/copyright = "2018, $(AUTHOR11) $(AUTHOR12), $(AUTHOR21) $(AUTHOR22), FIL, FST, Univ. Lille"/g' conf.py
	sed -i -e 's/^author =.*/author = "$(AUTHOR11) $(AUTHOR12), $(AUTHOR21) $(AUTHOR22)"/g' conf.py
