def print_header():
    print("=" * 30)

def load_inventory_file():
    servers_inventory = []
    with open("servers.txt", "r") as servers:
        for server in servers:
            servers_inventory.append(server)
    return servers_inventory

def parse_servers_inventory(servers_inventory):
    parsed_servers_inventory = []
    for line in servers_inventory:
        server = line.strip()
        if not server:
            continue
        parsed_servers_inventory.append(server)
    return parsed_servers_inventory

def print_servers(servers):
    for server in servers:
        print(server)

def main():
    print_header()
    servers_inventory = load_inventory_file()
    parsed_servers_inventory = parse_servers_inventory(servers_inventory)
    print_servers(parsed_servers_inventory)
    print_header()

if __name__ == "__main__":
    main()