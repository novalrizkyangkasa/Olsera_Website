access/run tc :
olsera_automation/tests/testcase.py

command : PYTHONPATH=../.. pytest testcase.py
with allure report : PYTHONPATH=../.. pytest testcase.py --alluredir=./reports
