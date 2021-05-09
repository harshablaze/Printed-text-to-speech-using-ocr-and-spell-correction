**NOTE:** I developed this project on Windows 10 X64bit OS and Python 3.9.2 X64bit version python Environment<br>
      this may not work on linux os because the path indication and tesseract.exe path used in src code file runs on windows
***
## **Setting up the project**

**1. After Downloading the project**
* `src>cd 4-4-project`

**2. activate the env**
* `src\4-4-project>.\env\Scripts\activate`

**NOTE**: if your env is activated you get (env) before your src path if env failed to activate then follow step 3 else go to step 4

**3. install requirements.txt**
* `src\4-4-project>pip install -r requirements.txt`
***
## **Run the project**

**4. to start the project**
* `src\4-4-project>python start.py`
***
## **Troubleshooting errors**
**1. if you encountered errors in installing requirements.txt**
 * check python architecture
```
src\4-4-project>python
>>import platform
>>platform.architecture()
```
output: `('64bit', 'WindowsPE')`

**2. if errors encountered after executing [start.py](https://github.com/harshablaze/4-4-project/blob/main/start.py)**
 * check if it is package error or input files error or path errors and rectify manually

**any issues connect with me through [linkedin](https://www.linkedin.com/in/sri-harsha-mullapudi-014623172/)** 