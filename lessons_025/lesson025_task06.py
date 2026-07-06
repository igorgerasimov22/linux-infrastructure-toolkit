def create_server_list():
    servers = [
        "web01",
        "web02",
        "web03",
        "web01",
        "web02"
    ]
    return servers

def create_server_sets(servers_list):
    servers_set = set()
    for server_list in servers_list:
        servers_set.add(server_list)
    return servers_set

def print_servers(servers):
    for _ in servers:
        print(_)

def main():
    servers_list = create_server_list()
    servers_set = create_server_sets(servers_list)
    print(f"Всего серверов: {len(servers_list)}")
    print(f"Уникальных серверов: {len(servers_set)}")

if __name__ == "__main__":
    main()