# qa-spring24

Run single file  
```
pytest tests/test_1.py -vx --alluredir results
```

Run all tests in 8 flows  
```
pytest -vx -n=8 --alluredir results
```

View allure report  
```
allure serve results
```  