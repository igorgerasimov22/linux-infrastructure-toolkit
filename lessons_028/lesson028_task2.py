def print_header():
    print("=" * 30)

def load_passwd_file():
    passwd_file = []
    with open("/etc/passwd", "r") as file:
        for line in file:
            passwd_file.append(line)
    return passwd_file

def parse_passwd_file(passwd_file):
    parsed_passwd_file = []
    for line in passwd_file:
        line = line.strip()
        if not line:
            continue
        user = line.split(':')
        parsed_passwd_file.append(
            {
                "username": user[0],
                "password": user[1],
                "uid": int(user[2]),
                "gid": int(user[3]),
                "description": user[4],
                "home": user[5],
                "shell": user[6]
            }
        )
    return parsed_passwd_file

def print_users(parsed_passwd_file):
    allowed_shells = {"/bin/bash", "/bin/sh", "/bin/zsh"}
    for line in parsed_passwd_file:
        if line['shell'] in allowed_shells:
            print(f"username: {line['username']}\tshell: {line['shell']}")

def main():
    print_header()
    try:
        passwd_file = load_passwd_file()
        parsed_passwd_file = parse_passwd_file(passwd_file)
        print_users(parsed_passwd_file)
    except FileNotFoundError:
        print("ERROR")
        print("File not found")
    except PermissionError:
        print("ERROR")
        print("Access denied")
    print_header()

if __name__ == "__main__":
    main()