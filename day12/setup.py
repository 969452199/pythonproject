pytest.main(['-v', '-s', 'pyteses.py', '--alluredir', './allure-result', '--clean-alluredir'])
    # time.sleep(1)
    # os.system('xcopy .\\allure-result\public .\\allure-result /e /Y /I')
    time.sleep(1)
    os.system('allure generate ./allure-result -o ./allure-report --clean')
    time.sleep(1)
    os.system('xcopy .\\allure-report\history .\\allure-result\history /e /Y /I')