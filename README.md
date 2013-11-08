## Visvalingam-Wyatt-DemoVersion
## =================

This is branch of the Visvalingam-Wyatt, where I added some code that enables me to:
	* extract single steps of the algorithm
	* get the triangle- and linegeometries of each step
	* store the single steps as DemoJSON-file

***You can find the specification for the DemoJSON-file*** [here](https://github.com/WebGeneralisation/VisualiseAlgorithms)


### Execute the demoVersion:

```sh
python simplify.py -i demoData.geojson -o simpleDData.geojson -t 0.0005
```

### View the DemoJSON in browser:

* Download the repository

* Simplify your demo data (!Should not contain too many points, as you'll get a step for each one!)

	```sh
	python simplify.py -i demoData.geojson -o simpleDData.geojson -t 0.0005
	```

* this produces:
	- simpleDData.geojson
	- demo.json

* setup local server (!necessary for D3.js!)

	```sh
	python -m SimpleHTTPServer 8888
	```

* open in browser: [localhost:8888/index.html](http://localhost:8888/index.html)


### Inspired by M.Bostocks JavaScript-Implementation:

* [Explanation](http://bost.ocks.org/mike/simplify/)
* [Code](http://bost.ocks.org/mike/simplify/simplify.js)

