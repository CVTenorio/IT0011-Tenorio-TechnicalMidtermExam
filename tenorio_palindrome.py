# Carl Vincent Tenorio TW24 Palindrome
"""
INSTRUCTIONS:
Create a program that will open the
file numbers.txt and check each line if the sum
of the given string digit numbers is palindrome
If the given numbers are 10,20,30,17 then you have to add the numbers (77) then the number
is said to be sum palindrome.
"""
def palindrome(Palindrome_daw):
    return str(Palindrome_daw) == str(Palindrome_daw)[::-1]

def processed_FileData(filename_daw):
    try:
        with open(filename_daw, 'r') as file:
            for line in file:
                num = list(map(int, line.strip().split(',')))
                total_niya = sum(num)
                if palindrome(total_niya):
                    print(f"The sum {total_niya} palindrome daw!\n")
                else:
                    print(f"The sum {total_niya} hindi daw palindrome!\n")
    except FileNotFoundError:
        print("\nFile not found. Maaari mo bang tignan kung tama ang filename and try again.")
    except ValueError:
        print("\nInvalid ang data sa file. Please ensure the file contains comma-separated numbers. ")

def main():
    filename_daw = "numbers.txt"
    processed_FileData (filename_daw)

if __name__ == "__main__":
    main()