# UITestFramework
A automatic UI test framework based on Python and Selenium

The project of UItestFramework has these features as follows:
1. The Webdriver module is simply encapsulated to make it more convenient to use. public/common/pyselenium.py
2. Can read data from excel sheet and realize data drive: public/common/datainfo.py
3. With the function of printing logs, the printing results are in the console and files: public/common/log.py, the logs are saved in the directory: report/log/.
4. Read configuration file(.ini): public/common/readconfig.py
5. Email function: public/common/sendmail.py
6. Generating test report with the form of HTML in the directory: report/testreport/
7. Use Page/Object mode to write test scripts


The directory structure of the entire project:
├─config  		        #The directory of config file
│  │  config.ini   	    #main config file
│  │  globalparam.py    #important global parameters, including directory or log report, etc.
│  │  __init__.py
│  │
│
├─data   	#test data
│  └─testdata     	    # test data 
│          searKey.xlsx
│
├─public 
│  │  __init__.py
│  │
│  ├─common  	        #public encapsulated method 
│  │  │  basepage.py
│  │  │  datainfo.py
│  │  │  log.py
│  │  │  mytest.py
│  │  │  publicfunction.py
│  │  │  pyselenium.py
│  │  │  readconfig.py
│  │  │  sendmail.py
│  │  │  __init__.py
│  │  │
│  │
│  ├─pages 	            #stores page classes, designed with Page/Object mode
│  │  │  baiduIndexPage.py
│  │  │  __init__.py
│
├─report 
│  ├─log 
│  │      2016-11-07.log
│  │
│  └─testreport  	    #test report in HTML 
│          TestResult2016-11-07_16_15_51.html
│
└─testcase 	            #directory for testcases
    │  test_baidu.py