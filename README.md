# demoblaze-tests

## Introduction
This repository contains some tests over **[DEMO ONLINE SHOP](https://www.demoblaze.com/index.html)**.

Testframework (main tools):
- *Selenium IDE* (GoogleChrome extension) to record test steps
- *Selenium Python library* for final test implementation
- *Python 3.10.4* has been used

### REQUIRED
**ChromeDriver** must be on your PC. Instructions:
1. Go to [chromedriver/downloads](https://sites.google.com/chromium.org/driver/)
2. Download *.zip*
3. Extract *chromedriver.exe* file to */Programs Files/* path
4. Copy path where *chromedriver.exe* file was placed
5. Reference path in tests

### Aspects to be considered
- Tests can only be launched from Windows.
- It has been observed that the following message error is displayed on logging while test execution:
````ERROR:device_event_log_impl.cc(214)] [18:46:06.359] USB: usb_device_handle_win.cc:1049 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)````
However, tests pass. According to [stackoverflow answer](https://stackoverflow.com/questions/64940553/failed-to-read-descriptor-from-node-connection-a-device-attached-to-the-system): *"This error isn't harmful and doesn't blocks the spawning of the new Browsing Context i.e. the Chrome Browser session. So you can safely ignore the error."*

### How to launch tests
From ````venv````:
````
pytest -s .\tests.py 
````
