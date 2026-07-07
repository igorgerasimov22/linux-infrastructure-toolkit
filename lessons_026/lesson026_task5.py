def print_header():
    print("=" * 30)

def load_yesterday_servers():
    yesterday_servers = {"web01", "web02", "web03"}
    return yesterday_servers

def load_today_servers():
    today_servers = {"web02", "web03", "web04"}
    return today_servers

def compare_servers(yesterday_servers, today_servers):
    compare_server = yesterday_servers ^ today_servers
    return compare_server

def print_servers(servers):
    for server in sorted(servers):
        print(server)

def main():
    yesterday_servers = load_yesterday_servers()
    today_servers = load_today_servers()
    compare_server = compare_servers(yesterday_servers, today_servers)
    print_header()
    print("Изменения в inventory: ")
    print_servers(compare_server)
    print_header()

if __name__ == "__main__":
    main()