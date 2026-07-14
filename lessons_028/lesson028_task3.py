def print_header():
    print("=" * 30)

def load_passwd_file():
    passwd_file = []
    with open("/etc/passwd", "r") as passwd:
        for line in passwd:
            passwd_file.append(line)
    return passwd_file

def parse_passwd_file(passwd_file):
    parsed_passwd_file = []
    for line in passwd_file:
        line = line.strip()
        if not line:
            continue
        user = line.split(':')
        parsed_passwd_file.append({
            "username": user[0],
            "password": user[1],
            "uid": int(user[2]),
            "gid": int(user[3]),
            "description": user[4],
            "home": user[5],
            "shell": user[6]
        })
    return parsed_passwd_file

def create_users_index(parsed_passwd_file):
    users_index = {}
    for user in parsed_passwd_file:
        users_index[user["username"]] = user
    return users_index

def print_user(users_index, username):
    user = users_index[username]
    print(f"Username: {user['username']}")
    print(f"UID     : {user['uid']}")
    print(f"GID     : {user['gid']}")
    print(f"HOME    : {user['home']}")
    print(f"SHELL   : {user['shell']}")

def main():
    print_header()
    print("Linux Users Analyzer\n")
    try:
        passwd_file = load_passwd_file()
        parsed_passwd_file = parse_passwd_file(passwd_file)
        users_index = create_users_index(parsed_passwd_file)
        print_user(users_index, "root")
    except FileNotFoundError:
        print("ERROR")
        print("File not found")
    except PermissionError:
        print("ERROR")
        print("Access denied")
    except KeyError:
        print("ERROR")
        print("User not found")
    print_header()

if __name__ == "__main__":
    main()