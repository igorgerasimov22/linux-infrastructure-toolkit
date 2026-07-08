def print_header():
    print("=" * 30)

def create_servers_dictionary():
    servers = {
        "name": "web01",
        "ip": "192.168.0.1",
        "ram": 32
    }
    return servers

def get_field_name():
    return input("Enter field name: ")


def print_server_field(field_name, servers):
    #if field_name in servers:
        print(servers[field_name])
    #else:
    #    print("ERROR")
    #    print("Field not found")
        

def main():
    print_header()
    servers = create_servers_dictionary()
    field_name = get_field_name()
    try:
        print_server_field(field_name, servers)
    except KeyError:
         print("ERROR")
         print("Field not found")
    print_header()

if __name__ == "__main__":
    main()