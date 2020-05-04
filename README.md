# zentest-demo
This is a demo project for web application testing. This test framework is based on Behavior-driven development (BDD) 
technique.

## Requirements
- [Python3](https://www.python.org/)
- [Pip](https://pypi.org/project/pip/)
- [Chrome browser](https://www.google.com/intl/en_en/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/)

## How to install
- clone this repository
- install all require libraries:
```console
pip3 install -r requirements.txt
```
- download `chromedriver` to `./sell_tests/configurations/` directory
- set test account data (EMAIL, PASSWORD) in `./sell_tests/configurations/account_configuration.py` file

## How to use
To run all test features use the following command:
```console
python -m behave ./sell_tests/features/
```
