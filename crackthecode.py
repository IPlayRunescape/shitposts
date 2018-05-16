import sys
def main():
    secret = 'b'
    user = str(input("Guess the secret number\n"))
    if user == secret:
        print("Good job! You get nothing")
        input()
        sys.exit(1)
    else:
        print("Nope")
        sys.exit(1)
main()