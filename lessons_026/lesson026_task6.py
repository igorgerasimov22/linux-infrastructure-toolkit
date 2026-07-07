def print_header():
    print("=" * 30)

def load_inventory():
    servers = [
        "web01",
        "web02",
        "web03",
        "web01",
        "web04",
        "web02",
        "web05",
        "web03"
    ]
    return servers

def create_servers_inventory(servers):
    servers_inventory = set()
    for server in servers:
        if server in servers_inventory:
            print(f"Найден дубликат: {server}")
            continue
        else:
            servers_inventory.add(server)
    return servers_inventory

def print_servers(servers):
    for server in sorted(servers):
        print(server)

def main():
    print_header()
    servers_list = load_inventory()
    servers_inventory = create_servers_inventory(servers_list)
    print_header()
    print_servers(servers_inventory)
    print_header()

if __name__ == "__main__":
    main()