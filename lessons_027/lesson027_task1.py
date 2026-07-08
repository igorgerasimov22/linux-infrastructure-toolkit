def print_header():
    print("=" * 30)

def load_inventory():
    inventory_file_name = input("Enter inventory file name: ")
    servers_inventory = []
    with open(inventory_file_name, "r") as file:
        for server in file:
            server = server.strip()
            servers_inventory.append(server)
    return servers_inventory
    
def print_servers(servers):
    for server in servers:
        print(server)

def main():
    print_header()
    try:
        server_inventory_list = load_inventory()
        print_servers(server_inventory_list)
    except FileNotFoundError:
        print("File not found")
        print("Script terminated")
    print_header()

if __name__ == "__main__":
    main()
