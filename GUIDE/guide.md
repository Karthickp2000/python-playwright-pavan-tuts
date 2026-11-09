Install Pytest-Playwright
 - pip install pytest-playwright
-------------------------------------------------------------------------------------------------------------
Install playwright browsers
 - pip install pytest

Browser Engines: -
chrome & Edge -> chromium
Firefox       -> firefox
Safari        -> webkit
-------------------------------------------------------------------------------------------------------------
Most famous async library
  - pytest-asyncio
Command to install:
  - pip install pytest-asyncio

-------------------------------------------------------------------------------------------------------------
Commands to run in different browsers
-------------------------------------
 - pytest <filename> -s -v --headed --browser firefox --browser chromium

Commands to run in Parelle Mode
-------------------------------
 - pytest <filename> -s -v -n 2 
OR
 - pytest <filename> -s -v --numprocesses 2 
-------------------------------------------------------------------------------------------------------------