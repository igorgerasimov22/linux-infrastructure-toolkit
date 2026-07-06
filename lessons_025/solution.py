def print_header():
    print("=" * 30)

def print_title():
    print("ИНВЕНТОРИЗАЦИЯ СЕРВЕРОВ")

def print_server_number(number):
    print(f"\nСервер №{number}")

def load_inventory_file():
    servers = []
    with open("servers.txt", "r") as file:
        for line in file:
            servers.append(line)
    return servers

def parse_servers_line(servers_file):
    servers_line = []
    for server_line in servers_file:
        server_line = server_line.strip()
        server_lines = server_line.split(',')
        if not server_line:
            continue
        if len(server_lines) != 4:
            print(f"В строке сервера {server_lines[0]} ошибка!")
            print(f"Строка пропущена.")
            continue
        
        servers_line.append({"name": server_lines[0], "ip": server_lines[1], "ram": int(server_lines[2]), "cpu": int(server_lines[3])})
    return servers_line

def print_inventory(servers):
    """
    Функция выводит список серверов
    """
    for number, server in enumerate(servers, start=1):
        print_server_number(number)
        for key, value in server.items():
            print(f"{key}: {value}")

def main():
    servers = []
    servers_file = []
    print_header()
    print_title()
    servers_file = load_inventory_file()
    servers = parse_servers_line(servers_file)
    print_inventory(servers)
    print_header()

if __name__ == "__main__":
    main()