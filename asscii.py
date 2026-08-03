# ==========================================
# Character ↔ ASCII Conversions in Python
# ==========================================

# Input a single character
ch = input("Enter a character: ")

# -------------------------------------------------
# Character -> ASCII
# ord() converts a character to its ASCII value
# Example: 'A' -> 65, 'a' -> 97
# -------------------------------------------------
ascii_value = ord(ch)
print("ASCII Value :", ascii_value)


# -------------------------------------------------
# ASCII -> Character
# chr() converts an ASCII value back to a character
# Example: 65 -> 'A', 97 -> 'a'
# -------------------------------------------------
print("Character from ASCII :", chr(ascii_value))


# -------------------------------------------------
# Position of lowercase letter (a=0, b=1, ..., z=25)
# Formula: ord(ch) - ord('a')
# Example: d -> 3
# -------------------------------------------------
if 'a' <= ch <= 'z':
    print("Lowercase Position :", ord(ch) - ord('a'))


# -------------------------------------------------
# Position of uppercase letter (A=0, B=1, ..., Z=25)
# Formula: ord(ch) - ord('A')
# Example: D -> 3
# -------------------------------------------------
if 'A' <= ch <= 'Z':
    print("Uppercase Position :", ord(ch) - ord('A'))


# -------------------------------------------------
# Convert Lowercase -> Uppercase
# Difference between lowercase and uppercase = 32
# Example: a(97) -> A(65)
# -------------------------------------------------
if 'a' <= ch <= 'z':
    print("Uppercase :", chr(ord(ch) - 32))


# -------------------------------------------------
# Convert Uppercase -> Lowercase
# Example: A(65) -> a(97)
# -------------------------------------------------
if 'A' <= ch <= 'Z':
    print("Lowercase :", chr(ord(ch) + 32))


# -------------------------------------------------
# Check if character is a digit using ASCII
# ASCII of '0' = 48
# ASCII of '9' = 57
# -------------------------------------------------
if 48 <= ord(ch) <= 57:
    print("It is a Digit")


# -------------------------------------------------
# Check if character is an uppercase letter
# ASCII of 'A' = 65
# ASCII of 'Z' = 90
# -------------------------------------------------
if 65 <= ord(ch) <= 90:
    print("It is an Uppercase Letter")


# -------------------------------------------------
# Check if character is a lowercase letter
# ASCII of 'a' = 97
# ASCII of 'z' = 122
# -------------------------------------------------
if 97 <= ord(ch) <= 122:
    print("It is a Lowercase Letter")
