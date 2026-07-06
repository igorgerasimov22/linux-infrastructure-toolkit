def create_sets():
    servers = set()
    servers.add("web01")
    servers.add("web02")
    servers.add("web03")
    return servers

def print_sets(sets):
    for _ in sets:
        print(_)

def main():
    create_sets()
    servers = create_sets()
    print_sets(servers)

if __name__ == "__main__":
    main()