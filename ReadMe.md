# HUDL Login Test

This is a test project for testing the login functionality of a https://www.hudl.com/ website using Selenium and Behave
framework.

## Project Structure

The project consists of the following files:

- `pages.login_page.py`: Contains the implementation of the LoginPage class, which represents the login page of the
  website. It includes methods for navigating to the login page, submitting credentials, checking login status, handling
  errors, and logging out.

- `steps/login_steps.py`: Contains the implementation of the Behave step definitions for the login functionality. It
  includes step definitions for navigating to the login page, submitting valid/invalid/empty credentials, checking for
  error messages, logging out, and other related steps.

- `utils/common_utils.py`: Contains utility functions for reading configuration data from a YAML file. It includes
  a `read_config` function that reads configuration values from a `config.yml` file.

- `config.yml`: Contains configuration variables (email, password).

- `login.feature`: Contains the Behave feature file with scenarios for testing the login functionality. It includes
  scenarios for successful login with valid credentials, unsuccessful login with invalid/empty credentials, and checking
  for error messages and logout functionality.

## Dependencies

The project requires the following dependencies:

- Python v3.x: Make sure to have Python v3.x installed on your system. You can download and install the latest version
  of Python from the official Python website: https://www.python.org/downloads/

- Selenium: A Python library for interacting with web browsers and automating web testing.

- Behave: A BDD (Behavior-Driven Development) framework for Python that allows writing tests in a natural language
  format.

- PyYAML: A YAML parser for Python used for reading configuration data from the `config.yml` file.

- ChromeDriver: The project uses ChromeDriver as the WebDriver for automating the Chrome browser. Make sure to download
  the appropriate version of ChromeDriver that matches your Chrome browser version (check it on chrome://settings/help).
  You can download ChromeDriver from the official ChromeDriver website: https://chromedriver.chromium.org. Extract from
  the zip file executable chromedriver file and put it into your project directory folder.

Make sure to install these dependencies before running the tests using the folowing command line:

```sh
pip install -r requirements.txt
```

to install chromedriver chrome://settings/help

- https://chromedriver.chromium.org/

## Running the Tests

To run the tests, follow these steps:

1. Clone the project to your local machine.
2. Navigate to the project directory.
3. Create and activate a virtual environment (venv)
4. Install the dependencies mentioned above.
5. Run the Behave command to execute the tests:

```sh
behave
```

This will run the tests and generate the test results in the console output.

## Configuration

The project uses a `config.yml` file for storing configuration data such as email and password for testing. Make sure to
update this file with valid credentials before running the tests.

## Note

- Make sure to update the webdriver path or configuration according to your local environment.

- Update the URL of the website being tested in the `navigate_to_login_page` method of `pages.login_page.py` file.

- Update the locators and XPATHs in the `pages.login_page.py` file if the website's DOM structure changes.

- Feel free to extend and modify the test scenarios and step definitions in the `login.feature`
  and `steps/login_steps.py` files according to your testing requirements.

- Remember to close the webdriver session after running the tests by calling the `close_session` method of
  the `LoginPage` class in the appropriate step definition or test teardown.


