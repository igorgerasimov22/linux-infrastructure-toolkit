def print_header():
    """
    Функция добавляет разделитель
    """
    print("=" * 30)

def print_server_number(number):
    """
    Функция добавляет номер сервера по порядку
    """
    print(f"\nСервер №{number}")


def parse_inventory(server):
    """
    Функция собирает словарь серверов
    """
    parsed_servers = []
    for line in server:
        line = line.strip()
        lines = line.split(',')
        if not line:
            continue
        if len(lines) != 4:
            print(f"В строке {line} ошибка")
            print(f"Недостаточно или пропущены поля. Строка пропущена.")
            continue
        parsed_servers.append(({"name": lines[0], "ip": lines[1],  "ram": int(lines[2]), "cpu": int(lines[3])}))
    return parsed_servers

def load_inventory_file():
    """
    Функция открывает файл со списком серверов
    """
    try:
        print("")
    exe
    servers = []
    with open("servers.txt", "r") as file:
        for line in file:
            servers.append(line)
    return parse_inventory(servers)

def print_inventory(servers):
    """
    Функция выводит список серверов
    """
    for number, server in enumerate(servers, start=1):
        print_server_number(number)
        for key, value in server.items():
            print(f"{key}: {value}")

def main():
    print_header()
    servers = load_inventory_file()
    print_inventory(servers)
    print_header()

if __name__ == "__main__":
    main()
