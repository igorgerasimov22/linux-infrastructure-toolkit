#!/usr/bin/python3
def create_sets():
    servers = set()
    servers.add("web01")
    servers.add("web02")
    servers.add("web03")
    return servers

def validate_sets(sets):
    server = input("Введите имя сервера: ")
    if server in sets:
        print("Сервер есть во множестве.")
    else:
        print("Сервер отсутствует во множестве.")

def main():
    servers = create_sets()
    validate_sets(servers)

if __name__ == "__main__":
    main()