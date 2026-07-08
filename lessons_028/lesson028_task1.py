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
        parsed_line = line.split(':')
        if not parsed_line:
            continue
        parsed_passwd_file.append(parsed_line)
    return parsed_passwd_file

def print_user(users):
    for user in sorted(users):
        print(user[0])

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
        print("Acces dinaed")
    print_header()

if __name__ == "__main__":
    main()