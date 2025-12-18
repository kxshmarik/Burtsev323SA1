def parslog(logs: list[str]) -> dict[str, int]:
    """
    Парсит строки логов и считает количество запросов по кодам ответа
    Args:
        logs (list[str]): список строк логов в формате "IP - метод"
    Returns:
        dict[str, int]: словарь с количеством запросов по кодам ответа
    """
    statuss = {}
    for log in logs:
        parts = log.split()                     # Разбиваем строку по пробелам
        status_code = parts[-1]
        if status_code in statuss:        # Увеличение счётчика для кода
            statuss[status_code] += 1
        else:
            statuss[status_code] = 1
    return statuss

def find_most_active_ip(logs: list[str]) -> str:
    """
    Находит IP с наибольшим количеством запросов
    Args:
        logs (list[str]): список строк логов
    Returns:
        str: IP с наибольшим количеством запросов
    """
    ip_counts = {}
    for log in logs:
        ip = log.split()[0]
        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1
    most_active = max(ip_counts.items(), key=lambda x: x[1])   # Находим IP с максимальным количеством запросов
    return most_active[0]

def find_suspicious_ips(logs: list[str], threshold: int) -> list[str]:
    """
    Находит подозрительные IP с ошибками 404 или 500
    Args:
        logs (list[str]): список строк логов
        threshold (int): значение количества ошибок
    Returns:
        list[str]: список подозрительных IP
    """
    error_ips = {}
    for log in logs:
        parts = log.split()
        ip = parts[0]
        statuss = parts[-1]
        if statuss in ['404', '500']:      # Проверка только для 404 и 500
            if ip in error_ips:
                error_ips[ip] += 1
            else:
                error_ips[ip] = 1
    suspicious = [ip for ip, count in error_ips.items() if count >= threshold] # Фильтрация IP с кол-вом ошибок выше порога
    return suspicious

def main() -> None:
    """
    Основная функция для анализа логов веб-сервера
    """
    logs = [      # Исходные данные
        "192.168.1.1 - GET /index.html 200",
        "192.168.1.5 - GET /about 404",
        "192.168.1.1 - POST /login 200",
        "10.0.0.1 - GET /admin 500",
        "192.168.1.1 - GET /products 200",
        "192.168.1.5 - GET /contact 404",
        "10.0.0.1 - GET /dashboard 500",
        "192.168.1.10 - GET /home 200",
        "192.168.1.5 - GET /faq 404",
        "192.168.1.1 - GET /cart 200",
        "10.0.0.1 - POST /api 500",
        "192.168.1.5 - GET /nonexistent 404",
        "192.168.1.10 - GET /profile 200",
        "192.168.1.1 - GET /logout 200"
    ]
    # Считаем количество запросов по кодам
    statuss = parslog(logs) 
    print("1. Количество запросов исходя из ответов:")
    for code in ['200', '404', '500']:
        count = statuss.get(code, 0)
        print(f"   Код {code}: {count} запросов")
    # Самый активный IP
    most_active_ip = find_most_active_ip(logs)
    print(f"\n2. Самый активный IP-адрес: {most_active_ip}")
    # Подозрительные IP
    porog = 2
    suspicious_ips = find_suspicious_ips(logs, porog)
    print(f"\n3. Подозрительные IP-адреса (с {porog}+ ошибок 404 или 500):")
    if suspicious_ips:
        for ip in suspicious_ips:
            print(f"   - {ip}")
    else:
        print("   Подозрительных IP-адресов не найдено")

if __name__ == "__main__":
    main()