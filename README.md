# Age Authentication Application

## Environment Setup
To create and activate a virtual environment, and then install the required packages listed in the `requirements.txt` file, use the following commands:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt

# Run the application
python app.py
```

## Maintaining Dependencies
After installing any new library, make sure to update the `requirements.txt` file by running the following command:

```bash
# Update the requirements.txt file
pip freeze > requirements.txt
```

## Ignoring Test Data
To prevent test data files from being tracked by Git, add the appropriate patterns to the `.gitignore` file. For example:

```bash
# Ignore test data files
test_data/
*.testdata
```
