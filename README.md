# demoblaze-tests

## Introduction
This repository contains some tests over **[DEMO ONLINE SHOP](https://www.demoblaze.com/index.html)**.

Testframework (main tools):
- *Selenium IDE* (GoogleChrome extension) to record test steps
- *Selenium Python library* for final test implementation
- *Python 3.10.4* has been used

## REQUIRED
**ChromeDriver** must be on your PC. Instructions:
1. Go to [chromedriver/downloads](https://sites.google.com/chromium.org/driver/)
2. Download *.zip*
3. Extract *chromedriver.exe* file to */Programs Files/* path
4. Copy path where *chromedriver.exe* file was placed
5. Reference path in tests

## How to launch tests
From *venv*:
````
pytest -s .\tests.py 
````