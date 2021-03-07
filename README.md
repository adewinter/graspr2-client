Graspr-Client
=============

This is the "client code" for Graspr. This code is used for display and diagnostics of sensor values read by the graspr+teensy boards.


Installation
------------

* Clone this repo
* From this folder, within your terminal, run: `pip install pipenv`. This will install a tool that manages the python environment used by these scripts.
* Next run `pipenv install`. This will install all the required packages used by this repo.
* Run `pipenv shell` to activate the pipenv environment.

Usage
-----

Activate your pipenv environment by running `pipenv shell`.

* To simply display the sensor readings directly in your terminal, run: `python ./bin/print_to_terminal.py`.
* To display pretty graphs of those same readings, run `python ./graspr2/main.py`.  Note the charting app is still WIP so YMMV.