from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="umar",
    version="0.1.2",
    packages=find_packages(),
    description="A simple Python package for greeting and adding numbers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Umar Asghar",
    author_email="mrumarasghar@gmail.com",
    url="https://github.com/umarmughal824/umar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
