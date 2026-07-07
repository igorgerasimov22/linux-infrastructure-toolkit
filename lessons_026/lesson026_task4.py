def print_header():
    print("=" * 30)

def create_inventory():
    servers_yesterday = {"web01", "web02", "web03", "web04"}
    servers_today = {"web02", "web03", "web05"}
    return servers_yesterday, servers_today

def print_servers(servers):
    for server in sorted(servers):
        print(server)

def main():
    servers_yesterday, servers_today = create_inventory()
    print_header()
    print("Исчезнувшие серверы:")
    print_servers(servers_yesterday - servers_today)
    print_header()

if __name__ == "__main__":
    main()