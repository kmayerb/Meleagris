# Meleagris

really basic Meleagris (turkey) of a package for linux or macOSX

Like its namesake, meleagris does nothing useful; it is a testing ground of python build/distribution best practices to help other packages take flight.

It is highly recommended that you develop or run meleagris within a python virtual environment. Doing so isolates the programs dependencies so installing legacy tools won't interfere with any of your other python projects. 

## To use meleagris using python 2.7.11:
```bash
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
pip install git+https://github.com/kmayerb/meleagris.git@master
```
### env should contain:

```bash
Package    Version 
---------- --------
meleagris  0.1.dev0 # <- installed !!!
numpy      1.10.1  
pip        19.1.1  
setuptools 41.0.1  
wheel      0.33.4 
```


## To install the meleagris with its development env using python 2.7.11
```bash
virtualenv venv-dev
source ./venv-dev/bin/activate
pip install -r requirements-dev.txt
pip list
```

### dev-env should contain
```bash
Package            Version 
------------------ --------
atomicwrites       1.3.0   
attrs              19.1.0  
certifi            2019.3.9
configparser       3.7.4   
contextlib2        0.5.5   
funcsigs           1.0.2   
future             0.17.1  
importlib-metadata 0.17    
more-itertools     5.0.0   
numpy              1.10.1  
packaging          19.0    
pathlib2           2.3.3   
pip                19.1.1  
pluggy             0.12.0  
py                 1.8.0   
pyparsing          2.4.0   
pytest             4.6.2   
scandir            1.10.0  
setuptools         41.0.1  
six                1.12.0  
wcwidth            0.1.7   
wheel              0.33.4  
zipp               0.5.1  
```

```
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
conda create -name py27v python=2.7.11 virtualenv
conda activate py27v
virtualenv venv
conda deactivate
conda deactivate
```




