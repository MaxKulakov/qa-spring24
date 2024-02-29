# qa-spring24

Run single file  
```
pytest tests/test_1.py -vx --alluredir results
```

Run all tests in 4 flows  
```
pytest -vx -n=4 --alluredir results
```

View allure report  
```
allure serve results
```  