import os
import io
import sys
import subprocess

"""
Read the dependencies from requirements.txt
Check the dependencies

if installed import if not install using pip

"""

try:
    setuptools = __import__("setuptools")
except ImportError as e:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
    setuptools = __import__("setuptools")


def read(path, encoding="utf-8"):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


def get_lib_dependencies(path):
    content = read(path)
    return [req for req in content.split("\n") if req != "" and not req.startswith("#")]


setuptools.setup(
    name="mypythonlib",
    packages=setuptools.find_packages(include=["mypythonlib"]),
    version="0.1.0",
    description="My first Python library",
    author="Me",
    license="MIT",
    install_requires=get_lib_dependencies("requirements.txt"),
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
