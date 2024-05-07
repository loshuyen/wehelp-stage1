# Before activating this project...
- make sure to add a config.py file in the root directory
- inside config.py, insert the following code
```python
class Config:
    MYSQL_PASSWORD = "[your MySQL password]"
    SESSION_SECRET_KEY = "[a random combination of strings]"
```