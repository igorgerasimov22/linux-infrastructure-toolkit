def print_header():
    print("=" * 30)

def create_inventory_sets():
    servers_yesterday = {"web01", "web02", "web03"}
    servers_today = {"web02", "web03", "web04"}
    return servers_yesterday, servers_today

def print_servers(servers):
    for server in servers:
        print(server)

def main():
    servers_yesterday, servers_today = create_inventory_sets()
    print_header()
    print("Серверы появившиеся сегодня: ")
    print_servers(servers_today - servers_yesterday)
    print_header()

if __name__ == "__main__":
    main()