import os
import sys
import json

# Путь к конфигу из env и потом преобразование json в словарь config

config_file = os.getenv('api_config_file')
if config_file is None:
    config_file = 'config.json'

try:
    with open(config_file, 'r', encoding='utf-8') as file:
        config = json.load(file)
except Exception as e:
    print(e)
    sys.exit(1)

if os.environ.get("API_DB_HOST"):
    config['db']['host'] = os.environ.get("API_DB_HOST")