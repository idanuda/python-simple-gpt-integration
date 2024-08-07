# python-simple-gpt-integration
Simple python flask service with OpenAI GPT Integration.


## Before you begin
Create an OpenAI account with one or more GPT deployments. After you have deployed one or more GPT models, extract the endpoint and api-key to the variables mentioned below.

## Installation 

2. Install the requirements from PyPI
```commandline
pip install your_project_name
```
3. Replace your ENDPOINT and API_KEY in `openai_service`
```python
ENDPOINT = "YOUR_ENDPOINT" 
API_KEY = "YOUR_API_KEY"
```
4. Run the init file
```commandline
$ python __init__.py
```

## Usage
Server will be availble at http://0.0.0.0:8080/api/

