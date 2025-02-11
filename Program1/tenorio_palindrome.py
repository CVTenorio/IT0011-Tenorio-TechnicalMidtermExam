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
                    print(f"The sum {total_niya} is a palindrome daw!\n")
                else:
                    print(f"The sum {total_niya} is not a palindrome daw!\n")
    except FileNotFoundError:
        print("\nFile not found. PLease check mo filename if nandyan and try again.")
    except ValueError:
        print("\nInvalid and data sa file. Please ensure the file contains comma-separated numebers. ")

def inputKa_numero():
    try:
        num = list(map(int, input("Hello Sayo Kaibigan ko!\n""Maglagay ka nang limang numero na nakahiwalay gamit ang commas: ").split(',')))
        if len(num) !=5:
            print("\nMaglagay ka nang sakto na limang numero.")
            return
        total_niya = sum(num)
        if palindrome(total_niya):
            print(f"\nThe sum {total_niya} is a palindrome daw!\n")
        else:
            print(f"\nThe sum {total_niya} hindi daw palindrome!\n")
    except ValueError:
        print("\nInvalid daw ang nilagay mo. Maaari mo bang ulitin ang iyong nilagay. Maglagay lamang nang 5 numbers na nakahiwalay by commas.\n")

def main():
    filename_daw = "numbers.txt"
    processed_FileData (filename_daw)
    inputKa_numero()

if __name__ == "__main__":
    main()