from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]

setup(
    name="codetest",
    version="1.1.0",
    description="A testing library for coding problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anuragpatil94/codetest",
    author="Anurag Patil",
    author_email="aspanurag@gmail.com",
    license="MIT",
    classifiers=classifiers,
    install_requires=[""],
    packages=find_packages(),
    keywords=["testing", "library", "Coding"],
)
