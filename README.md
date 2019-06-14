# Meleagris

really basic Meleagris (turkey) of a package for linux or macOSX

Like its namesake, meleagris does nothing useful; it is a testing ground of python build/distribution best practices to help other packages take flight.

It is highly recommended that you develop or run meleagris within a python virtual environment. Doing so isolates the programs dependencies so installing legacy tools won't interfere with any of your other python projects. 

## To use meleagris using python 2.7.11:
```bash
virtrualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
pip install git+https://github.com/kmayerb/meleagris.git@master
```

## To install the meleagris with its development env using python 2.7.11
```bash
virtrualenv venv-dev
source ./venv-dev/bin/activate
pip install -r requirements-dev.txt
pip install git+https://github.com/kmayerb/meleagris.git@master
```

## Try some trivial commands, if they work meleagris is installed.
```bash
python
import meleagris as ms 
ms.roast.roast_temp()
ms.carve.carve(4,10)
```

## if you don't have virtualenv or pip for python 2.7.11 you can create them very quickly using conda:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install virtualenv 
```

Or, second best, and even faster if you have permissions issues:
```bash
conda create -name py27 python=2.7.11 virtualenv
conda activate py27
virtualenv venv
conda deactivate
conda deactivate
```




