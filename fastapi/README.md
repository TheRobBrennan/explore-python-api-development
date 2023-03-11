# Welcome
Let's refer to the `How to create an API in Python with FastAPI` section in the blog post [How to create an API in Python](https://anderfernandez.com/en/blog/how-to-create-api-python/) as a starting point.

## Local development

### Install dependencies and run our project

```sh
# Verify that you have Python installed on your machine
% python3 --version

# Create a new virtual environment for the project
% python3 -m venv .venv

# Select your new environment by using the Python: Select Interpreter command in VS Code
#   - Enter the path: ./.venv/bin/python

# Activate your virtual environment
# % source /Users/rob/repos/explore-python-api-development/fastapi/.venv/bin/activate
% source /path/to/explore-python-api-development/fastapi/.venv/bin/activate
(.venv) %

# Make sure you are in the FastAPI directory
(.venv) % cd fastapi

# Install Python packages in a virtual environment
(.venv) % pip install fastapi
(.venv) % pip install uvicorn
(.venv) % pip install pandas
(.venv) % pip install matplotlib
(.venv) % pip install requests

# Let's start our FastAPI server - Available at http://127.0.0.1:8000/
(.venv) % uvicorn main:app --reload

# When you are ready to generate a requirements.txt file
(.venv) % pip freeze > requirements.txt

# What happens if you want to uninstall a package?

# Uninstall the package from your virtual environment
# (.venv) % pip uninstall simplejson

# Remove the dependency from requirements.txt if it exists
# (.venv) % pip uninstall -r requirements.txt

# Install the packages from requirements.txt
(.venv) % pip install -r requirements.txt
```
