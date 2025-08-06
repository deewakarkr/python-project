def is_palindrome(s):
    return s == s[::-1]

def find_palindromic_substrings(string):
    palindromes = []

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substr = string[i:j]
            if is_palindrome(substr):
                palindromes.append(substr)

    return palindromes

# Example usage
input_str = "madam"
result = find_palindromic_substrings(input_str)
print("Palindromic Substrings:", result)