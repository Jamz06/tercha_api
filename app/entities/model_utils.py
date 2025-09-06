from enum import Enum



class DbAnswers(str, Enum):
    """
        Ответы от БД для обработки
        Успех, дубликат, ошибка и т.д.
    """

    SUCCESS = 'success'
    DUP_VAL = 'dup_val'
    ERROR = 'ERROR'