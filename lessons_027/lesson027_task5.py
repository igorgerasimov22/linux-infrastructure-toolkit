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
    empty_lines = 0
    for line in servers_inventory:
        server = line.strip()
        if not server:
            empty_lines += 1
            continue
        parsed_servers_inventory.append(server)
    return parsed_servers_inventory, empty_lines

def find_duplicates_servers(parsed_servers_inventory):
    uniq_servers = set()
    duplicate_servers = set()
    for server in parsed_servers_inventory:
        if server in uniq_servers:
            duplicate_servers.add(server)
        else:
            uniq_servers.add(server)
    return uniq_servers, duplicate_servers


def print_servers(servers):
    for server in servers:
        print(server)

def main():
    print_header()
    try:
        servers_inventory = load_inventory_file()
        parsed_servers_inventory, empty_lines = parse_servers_inventory(servers_inventory)
        uniq_servers, duplicate_servers = find_duplicates_servers(parsed_servers_inventory)
        print("INVENTORY REPORT\n")
        print(f"Total records: {len(parsed_servers_inventory)}")
        print(f"Unique servers: {len(uniq_servers)}")
        print(f"Duplicate servers: {len(duplicate_servers)}")
        print(f"Empty lines: {empty_lines}\n")
        print("Duplicate servers:")
        print_servers(duplicate_servers)
    except FileNotFoundError:
        print("ERROR")
        print("File not found")
    print_header()

if __name__ == "__main__":
    main()