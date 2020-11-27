# Sample Library

- Always a good idea to create a virtual environment.
- A virtual environment consists of a certain Python version and some libraries.

## Steps

1. Create Virtual Environment

   `python -m venv venv`

2. Run to open the VENV

   `bash` - `source <venv>/bin/activate`
   `Powershell` - `<venv>/bin/activate.ps1`
   `cmd` - `<venv>/bin/activate.bat`

3. Install `wheel`, `setuptools` and `twine` in `venv bash`

   `pip install <package-name>`

4. Create Folder Structure
   1. Create an empty file called `setup.py`. This is one of the most important files when **creating a Python library**!
   2. Create an empty file called `README.md`. This is the place where you can write markdown to **describe the contents of your library** for other users.
   3. Create a folder called `mypythonlib`, or whatever you want your **Python library to be called when you pip install it**. (The name should be unique on pip if you want to publish it later.)
   4. Create an empty file inside mypythonlib that is called `__init__.py`. Basically, any folder that has an `__init__.py` file in it, will be **included in the library** when we build it. Most of the time, you can leave the `__init__.py` files empty. Upon import, the code within `__init__.py` gets executed, so it should contain only the minimal amount of code that is needed to be able to run your project. For now, we will leave them as is.

## Sources

1. [How to create a Python Library](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f)
2. [venv](https://docs.python.org/3/library/venv.html)
