ALLOWED_SHELLS = {
    "/bin/bash", 
    "/bin/sh", 
    "/bin/zsh"
}

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
        if not line:
            continue
        line = line.strip()
        user = line.split(':')
        parsed_passwd_file.append(user)
    return parsed_passwd_file

def create_users_index(users):
    users_index = []
    for user in users:
        users_index.append({
            user[0]: {
                "username": user[0],
                "password": user[1],
                "uid": user[2],
                "gid": user[3],
                "description": user[4],
                "home": user[5],
                "shell": user[6]
            }
        })
    return users_index

def print_user(passwd_file):
    for user in passwd_file:
        print(user["igor"])

def main():
    passwd_file = load_passwd_file()
    parsed_passwd_file = parse_passwd_file(passwd_file)
    users_index = create_users_index(parsed_passwd_file)
    
    print_header()
    print_user(users_index)
    print_header()

if __name__ == "__main__":
    main()