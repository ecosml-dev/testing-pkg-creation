import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "testing_pkg_creation",
    version = "0.0.1",
    author = "jrmerz",
    description = ("testing of the creation of a pkg"),
    license = "MIT",
    keywords = "test another",
    url = "http://localhost:3000/package/a908a818-5767-4f3a-a34e-226ef2f0f0a7",
    packages=[
        'testing_pkg_creation',
        'testing_pkg_creation.main'
    ],
    package_data={
      'testing_pkg_creation' : ['coefficients/*']
    },
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)