# mac_converter

## About
This python script takes a list of MAC addresses as input, and outputs them in Cisco's format.

For example:
`A1:B2:C3:D4:E5:FF` becomes `a1b2.c3d4.e5ff`

## Prerequisites
- python3

## Installation

- Clone the repo
```bash
git clone https://github.com/StevenKelso/mac_converter
```

- cd into the directory
```bash
cd mac_converter
```

## Usage

- Run the script using python3
```bash
python3 converter.py
```
- Enter a list of MACs as you want, one on each line.

- Enter 'end' when you're done listing the MACs you want converted.

- The script will list the standard format MACs and Cisco format MACs side by side.
