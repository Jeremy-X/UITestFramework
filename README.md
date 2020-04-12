The project of UItestFramework has these features as follows:<br>
1. The Webdriver module is simply encapsulated to make it more convenient to use. public/common/pyselenium.py<br>
2. Can read data from excel sheet and realize data drive: public/common/datainfo.py<br>
3. With the function of printing logs, the printing results are in the console and files: public/common/log.py, the logs are saved in the directory: report/log/.<br>
4. Read configuration file(.ini): public/common/readconfig.py<br>
5. Email function: public/common/sendmail.py<br>
6. Generating test report with the form of HTML in the directory: report/testreport/<br>
7. Use Page/Object mode to write test scripts<br>

                      
The directory structure of the entire project: <br>
├─config  		#The directory of config file <br>
│  │  config.ini   	#main config file<br>
│  │  globalparam.py  #important global parameters, including directory or log report, etc.<br>
│  │  __init__.py<br>
│  │<br>
│<br>
├─data   	#test data<br>
│  └─testdata     	# test data <br>
│          searKey.xlsx<br>
│<br>
├─public <br>
│  │  __init__.py<br>
│  │<br>
│  ├─common  	#public encapsulated method <br>
│  │  │  basepage.py<br>
│  │  │  datainfo.py<br>
│  │  │  log.py<br>
│  │  │  mytest.py<br>
│  │  │  publicfunction.py<br>
│  │  │  pyselenium.py<br>
│  │  │  readconfig.py<br>
│  │  │  sendmail.py<br>
│  │  │  __init__.py<br>
│  │  │<br>
│  │<br>
│  ├─pages 	#stores page classes, designed with Page/Object mode<br>
│  │  │  baiduIndexPage.py<br>
│  │  │  __init__.py<br>
│<br>
├─report <br>
│  ├─log <br>
│  │      2016-11-07.log<br>
│  │<br>
│  └─testreport  	#test report in HTML <br>
│          TestResult2016-11-07_16_15_51.html<br>
│<br>
└─testcase 	#directory for testcases<br>
    │  test_baidu.py<br>
