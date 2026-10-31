""" Фунуция, возвращает новый список словарей"""
def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    #Создаем пустой список
    result =[]
    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result
