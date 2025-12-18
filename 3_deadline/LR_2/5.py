def filter_logs(log_lst: list, keyword: str):
    for log in log_lst:
        if keyword in log:
            yield log
            
# Пример использования
logs = [
    "INFO: Server started",
    "ERROR: Database connection failed",
    "INFO: User logged in",
    "ERROR: File not found",
    "WARNING: Ashot near",
    "INFO: Ashot at the counter",
]

print("Все ошибки (ERROR):")
for error in filter_logs(logs, "ERROR"):
    print(error)

print("\nВсе информационные сообщения (INFO):")
for info in filter_logs(logs, "INFO"):
    print(info)

print("\nВсе предупреждения (WARNING):")
for warning in filter_logs(logs, "WARNING"):
    print(warning)