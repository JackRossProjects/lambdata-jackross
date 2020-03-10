# setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="jackrossprojects-lambdata",
    version="1.0",
    author="Jack Ross",
    author_email="jackross210@gmail.com",
    description="test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/jackrossprojects/lambdata-jackross",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
