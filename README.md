Visvalingam-Wyatt
=================

Simple Python-Implementation of a [famous algorithm](http://www2.dcs.hull.ac.uk/CISRG/publications/DPs/DP10/DP10.html)

Execute by:

* Dummy
	```sh
	python simplify.py -i <inFile> -o <outFile> -t <tolerance>  	
	```

* Example
	```sh
	python simplify.py -i in.json -o out.json -t 0.0005
	```

* Help
	```sh
	python simplify.py -h
	```

View results in browser:

* setup local server (!necessary for D3.js!)

	```sh
	python -m SimpleHTTPServer 8888
	```
* open in browser: [localhost:8888/index.html](http://localhost:8888/index.html)


Inspired by M.Bostocks JavaScript-Implementation:

* [Explanation](http://bost.ocks.org/mike/simplify/)
* [Code](http://bost.ocks.org/mike/simplify/simplify.js)

