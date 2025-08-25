# API - для игры с собаками

## Запуск
Должна существовать переменная окружения api_config_file
Которая содержит путь к файлу конфигурации, который тоже сам создай на основе config.json


## Vscode - ругается на импорт модулей
По-умолчанию, pylint использует текущую дирректорию. 
Чтобы указать на нужную, добавь в .vscode/settings.json:

```
"pylint.cwd": "${workspaceFolder}/app"
```

В дебаге, то же самое: 
```
{
            "name": "API external ",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "cwd": "${workspaceFolder}/app",
            "env": { "api_config_file": ".config.json" },
            "args": ["main:app", "--host", "0.0.0.0", "--reload"],
            "jinja": true
}
```