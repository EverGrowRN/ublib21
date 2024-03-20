# UBLib21

## Usage



## Extra (for developers)
### Development

1. Clone this repo
~~~
git clone https://github.com/EverGrowRN/ublib21.git
~~~
2. Create a virtual environment with Python 3.11.3 or above.
~~~
virtualenv venv --python=3.11.3
~~~
3. Activate environment
~~~
# Linux
source ./venv/bin/activate

# Windows (i.e. using PowerShell)
./venv/Scripts/activate.ps1
~~~
4. Install requirements
~~~
pip install -r requirements
~~~


### Testing
1. Install the package as development. Run on the project root directory the following
~~~
pip install .[dev]
~~~
2. Install pytest
~~~
pip install pytest
~~~
3. Run tests. Run on the project root directory the following
~~~
pytest
~~~

### Deploy python package

https://packaging.python.org/en/latest/tutorials/packaging-projects/

#### To build:
~~~
py -m build
~~~

#### To push package (test):
~~~
py -m twine upload --repository testpypi dist/*
~~~