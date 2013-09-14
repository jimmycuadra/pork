# Pork

[![Build Status](https://travis-ci.org/jimmycuadra/pork.png?branch=master)](https://travis-ci.org/jimmycuadra/pork)

**Pork** is a command line tool for quick storage and retrieval of text snippets. It is a port of [Bang](https://github.com/jimmycuadra/bang) to Python.

## Python versions

Pork has been tested only under Python 2.7.

## Installation

Run `pip install pork`.

## Usage

For detailed usage instructions, run `pork -h`.

To set a key, run `pork KEY VALUE`.

To print value of a key, run `pork KEY`. If the key doesn't exist, there will be no output.

To delete a key, run `pork -d KEY`.

To list all keys (or print help if there are no keys stored yet), simply run `pork`.

## Development

1. Clone the repository.
1. Run `pip install -r requirements-dev.txt` to install all the dependencies.
1. Run `scripts/pork` to run the program.
1. Run `scripts/test` to run the tests.
