# atm_controller
>[1. Description](#1-description)  
>[2. Environment](#2-environment)  
>[3. Dependencies](#3-dependencies)  
>[4. Installation](#4-installation)  
>[5. Files](#5-files)  
>[6. Usage](#6-usage)  
>[7. Troubleshooting](#7-troubleshooting)  
>>[1) Ubuntu](#1-ubuntu)  
>>[2) MacOS](#2-mac-os)  

## 1. Description
This repository is sample code of ATMcontroller for coding test.  
## 2. Environment
OS: Windows 11

## 3. Dependencies
    Python >= 3.8.3

## 4. Installation
```bash
git clone https://github.com/jungjh404/atm_controller.git
```

## 5. Files
```bash
├──atm.py
├──bank.py
├──test.py
```

bank.py: This file is simplified version of bank API.

atm.py: It is controller of ATM.

test.py: It is test file to check validity of ATM controller.

## 6. Usage
For testing atm controller, you can use test.py as follows

```bash
python test.py
```
## 7. Troubleshooting
If you run this code in linux or mac, there will be encoding error.
You can fix it by using dos2unix
### 1) Ubuntu
```bash
sudo apt-get install dos2unix
dos2unix atm.py
dos2unix bank.py
dos2unix test.py
```

### 2) MAC OS
```bash
brew install dos2unix
dos2unix atm.py
dos2unix bank.py
dos2unix test.py
```