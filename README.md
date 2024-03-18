# qa-spring24

Run single file  
```
pytest tests/test_1.py -v --alluredir results
```

Run all tests in 8 flows in chrome browser
```
pytest -v -n=8 --browser=chrome --alluredir results
```

View allure report  
```
allure serve results
```  

