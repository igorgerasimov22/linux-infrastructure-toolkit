def print_header():
    """
    Функция добавляет разделитиль
    """
    print("=" * 30)

def print_server_number(number):
    """
    Функция добавляет номер сервера по порядку
    """
    print(f"\nСервер №{number}")


def parse_inventory_file(servers):
    """
    Функция собирает словарь серверов
    """
    parsed_servers = []
    for _ in servers:
        _ = _.strip()
        lines = _.split(',')
        if not _:
            continue
        if len(lines) != 4:
            print(f"Встроке {_} ошибка")
            print(f"Недостаточно или пропущены поля. Строка пропущена.")
            continue
        parsed_servers.append(({"name": lines[0], "ip": lines[1],  "ram": int(lines[2]), "cpu": int(lines[3])}))
    return parsed_servers

def load_inventory_file():
    """
    Функция открывает файл со списком серверов
    """
    servers = []
    with open("servers.txt", "r") as file:
        for line in file:
            servers.append(line)
    return parse_inventory_file(servers)

def print_inventory(server):
    """
    Функция выводит списко серверов
    """
    for number, server in enumerate(server, start=1):
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