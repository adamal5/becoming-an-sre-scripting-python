# Python Scripting: URL Accessibility Checker Script

## Overview
This Python script is a straightforward tool for checking the accessibility of a list of URLs. It uses the `requests` library to make HTTP requests to each URL and determines whether each is accessible, providing error codes for any that are not.

## Features
- **URL Accessibility Testing:** Quickly checks whether a list of URLs is accessible.
- **Error Code Reporting:** For inaccessible URLs, the script reports the HTTP status code or error encountered.
- **Simple and Efficient:** Easy-to-use script for rapid URL accessibility checks.

## Prerequisites
- Python 3.x
- `requests` Python library

## Installation
1. **Install Python:**
   - If not already installed, download and install Python from [python.org](https://www.python.org/).

2. **Install Requests Library:**
   - Install the `requests` library using pip:
     ```
     pip install requests
     ```

## Usage
1. **Running the Script:**
   - Execute the script in a Python environment:
     ```
     python url_checker.py
     ```
   - Replace `url_checker.py` with the path to your script if necessary.

2. **Customizing URL List:**
   - Edit the `urls` list in the script to include the URLs you want to check.

## Script Structure
- **Import Statement:** The script begins by importing the `requests` library.
- **Function Definition:** It defines a `check_urls` function to assess each URL's accessibility.
- **URL List and Execution:** Contains a predefined list of URLs and calls the `check_urls` function to perform the check.
- **Results Output:** Outputs the status of each URL to the console.

## License
This project is released under the [MIT License](LICENSE.md).