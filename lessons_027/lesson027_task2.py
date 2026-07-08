def print_header():
    print("=" * 30)

def create_lists():
    numbers = [10, 20, 30]
    return numbers

def get_index_of_numbers():
    index_number = int(input("Enter index number on lists:"))
    return index_number

def print_index_of_list(numbers, index_number):
    print(numbers[index_number])

def main():
    numbers = create_lists()
    index_number = get_index_of_numbers()
    print_header()
    try:
        print_index_of_list(numbers, index_number)
    except IndexError:
        print(f"Index {index_number} not found")
    print_header()

if __name__ == "__main__":
    main()