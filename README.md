These instructions will get you to run the automated tests on your machine in no time.

### Prerequisites

Make sure you have python and pip installed on your machine. Check it by running the following command in your terminal/Command Prompt.
Also make sure you have Chrome browser installed.

```
python --version
pip --version
```

### Installing

If you do not have either of those installed. Download and Install it from the following location.

```
https://pip.pypa.io/en/stable/installing/
```

Once Pip and Python are installed, run the following to download the required libraries in order to run the tests

```
sudo pip install pytest
sudo pip install selenium
```

It may ask you to enter your password, this is required to install it in the lib folder.

Download chromedriver and extract it to the desired location from the following link.

```
https://chromedriver.storage.googleapis.com/index.html?path=2.33/
```
Make sure you extract the executable from the zip file. Make sure you use the file as per your OS i.e. Linux, Windows or MacOS.

Use the location of the chromedriver and enter it in line no. 9 in **test_nomis_solutions.py** file. As an example,
```
driver = webdriver.Chrome('/Users/karan/Desktop/chromedriver')
```
Save the file and navigate to the folder where you have all the test files.

## Running the tests

In your terminal/Command prompt once run the following to start the automated tests.
```
py.test test_nomis_solutions.py
```
The tests will run independent of each other and it will give a complete test run result stating how many tests passed or failed.

```
======= 3 passed in 38.36 seconds =======
```