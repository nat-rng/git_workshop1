def palindrome(x):
    rev = x [::-1]
    if rev == x:
        print "is a palindrome"
    else:
        print "not palindrome"

x = "sas"
palindrome(x)