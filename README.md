# atm_controller
## Description
This repository is sample code of ATMcontroller for coding test.
------------
## Environment
OS: Windows 11
------------
## Dependencies
Python >= 3.8.3
------------
## Installation
```bash
git clone https://github.com/jungjh404/atm_controller.git
```
------------
## Files
```bash
├──atm.py
├──bank.py
├──test.py

```
bank.py: This file is simplified version of bank API.
atm.py: It is controller of ATM.
test.py: It is test file to check validity of ATM controller.
------------
## Usage
For testing atm controller, you can use test.py as follows

```bash
python test.py
```
## Troubleshooting
If you run this code in linux or mac, there will be encoding error.
You can fix it by using dos2unix
### Ubuntu
```bash
    sudo apt-get install dos2unix
    dos2unix atm.py
    dos2unix bank.py
    dos2unix test.py
```

### MAC OS
```bash
    brew install dos2unix
    dos2unix atm.py
    dos2unix bank.py
    dos2unix test.py
```
------------