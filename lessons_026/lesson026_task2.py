def print_header():
    print("=" * 30)

def print_string(string):
    print(f"{string}")

def create_datacenter_sets():
    servers_dc1 = {"web01", "web02", "web03"}
    servers_dc2 = {"web03", "web04", "web05"}
    return servers_dc1, servers_dc2

def print_datacenter_sets(servers):
    for server in servers:
        print(server)

def main():
    servers_dc1, servers_dc2 = create_datacenter_sets()
    print_header()
    print_string("Общие серверы:")
    print_datacenter_sets(servers_dc1 & servers_dc2)
    print_header()

if __name__ == "__main__":
    main()