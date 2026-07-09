def print_header():
    print("=" * 30)

def load_passwd_file():
    passwd_file = []
    with open("/etc/passwd","r") as file:
        for line in file:
            passwd_file.append(line)
    return passwd_file

def parse_passwd_file(passwd_file):
    parsed_passwd_file = []
    for line in passwd_file:
        line = line.strip()
        if not line:
            continue
        parsed_line = line.split(':')
        parsed_passwd_file.append({
            "username": parsed_line[0],
            "password": parsed_line[1],
            "uid": int(parsed_line[2]),
            "gid": int(parsed_line[3]),
            "description": parsed_line[4],
            "home": parsed_line[5],
            "shell": parsed_line[6]
        })
    return parsed_passwd_file

def print_user(users):
    for user in users:
        print(f"{user['username']}: {user['shell']}")
    #for number, user in enumerate(users, start=0):
    #    for key, value in user.items():
    #        print(f"{user["username"]}: {user["shell"]}")

def main():
    print_header()
    print("Linux users:")
    try:
        passwd_file = load_passwd_file()
        parsed_passwd_file = parse_passwd_file(passwd_file)
        print_user(parsed_passwd_file)
    except FileNotFoundError:
        print("ERROR")
        print("File not found")
    except PermissionError:
        print("ERROR")
        print("Access dinaed")
    print_header()

if __name__ == "__main__":
    main()