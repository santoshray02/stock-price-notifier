import setuptools
from distutils.core import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stock-price-notifier",
    version="0.0.1",
    author="Santosh Ray",
    author_email="rayskumar02@gmail.com",
    description="A very simple stock price notifier for desktop ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/santoshray02/stock-price-notifier",
    packages=setuptools.find_packages(),
    install_requires=[
          'beautifulsoup4==4.6.0',
          'requests==2.20.0',
      ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
