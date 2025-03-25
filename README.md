To create and activate a virtual environment, and then install the required packages listed in the `requirements.txt` file, use the following commands:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```
