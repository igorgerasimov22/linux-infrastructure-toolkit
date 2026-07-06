#!/bin/usr/python3
def create_sets():
    servers = set()
    servers.add("web01")
    servers.add("web02")
    servers.add("web03")
    return servers

def ask_name_server():
    server = input("Введите имя сервера: ")
    return server

def add_server_to_sets(servers, server):
    servers.add(server)
    return servers

def print_sets(servers):
    for _ in servers:
        print(_)

def main():
    servers = create_sets()
    server = ask_name_server()
    servers = add_server_to_sets(servers, server)
    print_sets(servers)

if __name__ == "__main__":
    main()