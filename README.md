# Automation Test Store

## Project Overview

This project is a software QA automation testing project built with Python and Selenium. This project tests the website www.automationteststore.com.

The purpose of the project is to demonstrate automated testing practices, including test automation, page interaction, test data management, and maintainable test structure.

## Technologies

- Python
- Selenium WebDriver
- Pytest
- Git
- GitHub

## Project Structure

```text
Automation_test_store/
├── data.py
├── main.py
├── pages.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup
 Clone the repository and create a Python virtual environment. 
 Install the required dependencies:
     pip install -r requirements.txt

## Running the Tests
The automated test suite runs through GitHub Actions. When changes are pushed to the GitHub repository, the configured workflow automatically executes the Selenium tests using pytest in a headless Chrome environment.

Test execution results can be viewed in the Actions tab of the GitHub repository.

## Project Status
 This project is actively being developed as part of a Software QA automation portfolio.
