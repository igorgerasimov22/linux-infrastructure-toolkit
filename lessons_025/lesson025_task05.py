def create_sets():
    servers = set()
    servers.add("web01")
    servers.add("web02")
    servers.add("web03")
    return servers

def print_server_sets(server_sets):
    for _ in server_sets:
        print(_)

def ask_user_delete_server_on_sets():
    server = input("Какой сервер удалить из множества: ")
    return server

def delete_server_on_sets(server, server_sets):
    server_sets.remove(server)
    return server_sets

def main():
    servers_set = create_sets()
    print_server_sets(servers_set)
    server = ask_user_delete_server_on_sets()
    servers_set = delete_server_on_sets(server, servers_set)
    print_server_sets(servers_set)

if __name__ == "__main__":
    main()