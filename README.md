## Kantar recruitment task

---

Sample navigation and tests of the YouTube page for videos searched by the keyword "Python" 


---


### Table of Contents

- [Technologies](#Technologies)
- [Project Tree](#Project-Tree)
- [How To Run Tests](#How-To-Run-Tests)
- [Autho Info](#author-info)

---



### Technologies

- pytest 7.1.2
- selenium 4.3.0
- allure-pytest 2.9.45
- webdriver-manager 3.4.2

To install all required libraries, type in terminal:
```
pip install -r requirements.txt
```
Installation will add some additional libraries (additional modules supporting pytest and selenium)

  
[Back to the Top ^](#Table-of-Contents)

---

### Project Tree

The project structure:


    
    Kantar_recr_task
    |
    |---  pages
    |     |--- YT_home_page.py
    |     `--- YT_results_list_page.py
    |      
    |--- tests
    |    `---  pages
    |          |--- base_test_class.py
    |          |--- test_01_YT_home_page.py
    |          |--- test_02_YT_search_results_page.py
    |          `--- test_03_YT_next_video_play.py
    |
    |---  utils
    |     |--- json_reader.py
    |     |--- locators.py
    |     |--- test_data.py
    |     |--- video_info.json
    |     `--- web_urls.json
    |
    |--- conftest.py
    |--- README.md
    `--- requirements.txt


[Back to the Top ^](#Table-of-Contents)

---

### How To Run Tests
To run all tests, type:

```
pytest -v tests
```

or choosing specific file, add file path;

```
pytest -v tests/test_suites/testsuite_all_tests.py 
```

- To screen Allure tests report, prepare report data:
```
python -m pytest tests/test_suites/testsuite_all_tests.py --alluredir ./results
```
- then call to screen it in default web browser
```
libs/allure-2.13.9/bin/allure serve ./results  
```
[Back to the Top ^](#Table-of-Contents)

---

### Author Info

- Przemyslaw Hinca -> Github: [pshemekhinca](https://github.com/pshemekhinca)

[Back to the Top ^](#Table-of-Contents)
