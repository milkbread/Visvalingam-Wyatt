Visvalingam-Wyatt
=================

Simple Python-Implementation of a [famous algorithm](http://www2.dcs.hull.ac.uk/CISRG/publications/DPs/DP10/DP10.html)

Download the repository:

```sh
git clone https://github.com/milkbread/Visvalingam-Wyatt.git
```


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

View results in browser (exemplary workflow for tests):

* Download the repository

* Simplify your data

	```sh
	python simplify.py -i in.json -o out.json -t 0.0005
	```

* setup local server (!necessary for D3.js!)

	```sh
	python -m SimpleHTTPServer 8888
	```

* open in browser: [localhost:8888/index.html](http://localhost:8888/index.html)

* On Demand: adjust the filenames within the index.html (lines 24 & 28)

* evaluate the resulting data and try another threshold

*Impacient to see some results? See the [index.html](http://milkbread.github.io/Visvalingam-Wyatt) here!*


Inspired by M.Bostocks JavaScript-Implementation:

* [Explanation](http://bost.ocks.org/mike/simplify/)
* [Code](http://bost.ocks.org/mike/simplify/simplify.js)

