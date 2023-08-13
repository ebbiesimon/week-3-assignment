
minimum_lenght = 9
maximum_lenght = 12
minimum_spec_chars = 3
minimum_alphabets = 5
minimum_numeric_chars = 3
special_chars = {'&', '#', '$', '!', '?', '"', '(', ')'}


def validate_password(password):
    if len(password) < minimum_lenght or len(password) > maximum_lenght:
        return "Validation Failed: Password length should be between 9 and 12"

    special_char_count = 0
    alpha_char_count = 0
    numeric_char_count = 0

    for char in password:
        if char in special_chars:
            special_char_count += 1
        elif char.isalpha():
            alpha_char_count += 1
        elif char.isdigit():
            numeric_char_count += 1

        if (
            special_char_count >= minimum_spec_chars
            and alpha_char_count >= minimum_alphabets
            and numeric_char_count >= minimum_numeric_chars
        ):
            return "Validation Succeeded!"

    if special_char_count < minimum_spec_chars:
        return "Validation Failed: You need to have a minimum of 3 special characters"
    elif alpha_char_count < minimum_alphabets:
        return "Validation Failed: You need to have a minimum of 5 alpha characters"
    elif numeric_char_count < minimum_numeric_chars:
        return "Validation Failed: You need to have a minimum of 3 digits"


def main():
    password = input("Please enter your password: ")
    result = validate_password(password)
    print(result)


if __name__ == "__main__":
    main()
