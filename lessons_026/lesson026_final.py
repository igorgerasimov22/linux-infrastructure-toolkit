def print_header():
    print("=" * 30)

def print_title(all, uniq, duplicate):
    print("\nINVENTORY REPORT")
    print(f"\nВсего записей: {all}")
    print(f"\nУникальных серверов: {uniq}")
    print(f"\nДубликатов: {duplicate}\n")

def load_inventory():
    servers_inventory = []
    with open("servers.txt", "r") as file:
        for server in file:
            servers_inventory.append(server)
    return servers_inventory

def parse_servers_inventory(servers_inventory):
    parsed_servers_inventory = []
    for server in servers_inventory:
        server = server.strip()
        parsed_servers_inventory.append(server)
    return parsed_servers_inventory

def find_duplicate_servers(servers):
    uniq_servers = set()
    duplicate_servers = set()
    for server in servers:
        if server in uniq_servers:
            duplicate_servers.add(server)
        else:
            uniq_servers.add(server)
    return duplicate_servers, uniq_servers

def print_servers(servers):
    for server in sorted(servers):
        print(server)

def main():
    servers_inventory = load_inventory()
    print_header()
    parsed_servers_inventory = parse_servers_inventory(servers_inventory)
    duplicate_servers, uniq_servers = find_duplicate_servers(parsed_servers_inventory)
    print_title(len(parsed_servers_inventory), len(uniq_servers), len(duplicate_servers))
    print_header()
    print("Дубли: ")
    print_servers(duplicate_servers)
    print_header()

if __name__ == "__main__":
    main()