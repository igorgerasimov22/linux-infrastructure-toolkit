def print_header():
    print("=" * 30)

def create_numbers_list():
    numbers_list = [10, 20, 30]
    return numbers_list

def get_index_number():
    index_number = int(input("Enter a number index of list: "))
    return index_number

def print_number(numbers_list, index_number):
    print(numbers_list[index_number])

def main():
    print_header()
    numbers_list = create_numbers_list()
    try:
        index_number = get_index_number()
        print_number(numbers_list, index_number)
    except ValueError:
        print("ERROR")
        print("Index must be a number")
        print_header()
    except IndexError:
        print("ERROR")
        print("Element not found")
        print_header()
        exit

if __name__ == "__main__":
    main()