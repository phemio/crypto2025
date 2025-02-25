### This is the crypto project for practising.

It is a Pytest-BDD framework with POM model.

### Pre-requisite:
- Install jdk version 11+, android SDK, Appium, androidstudo emulator
  
- using npm to install poetry, with pyproject.toml libraries.

To run the assessment:
###Q1 pyramid pattern:
```
py ./tests/steps_def/q1/q1.py
```

###Q2 HKO APP:
This framework will use .yaml file to manage running by app / web. Please change the config.yaml config first befor run pytest

executionConfig:
  device: **emulator_Pixel6a_android**

  platform: **app**

Also run to the emulator and set the emulator name to:

deviceName: "Pixel 6a"


```
pytest -v -s -m "Q2" --alluredir=./Reports/allurereports/test
```

###Q3 SZSE API:
Please also change the config.yaml config first before run pytest and install the correct version chromedriver for your chrome version

executionConfig:
  device: **Win10_Chrome_122**

  platform: **web**
  
```
pytest -v -s -m "Q3" --alluredir=./Reports/allurereports/test
```

Check the allure report
```
allure serve ./Reports/allurereports/test
```
