arQuote = ["in", "rather", "someone", "a", "change", "be", "else's", "powerful", "cloud", "rainbow"]
# The above array contains a scrambled quote.  Follow the steps below to unscramble it.
# start with the array above (you can copy this code to PyCharm as a template)

# 1. Sort the list alphabetically
print(arQuote)
arQuote.sort()
print(arQuote)

# 2. Use pop() to remove the third element
arQuote.pop(2)
print(arQuote)

# 3. Use remove() to remove the element containing "powerful"
arQuote.remove("powerful")
print(arQuote)

# 4. Make a copy of the array called arQuote2
arQuote2 = arQuote.copy()
print(arQuote2, "<-", "This is the copy.")

# 5. Copy from the 2nd element of arQuote2 to the 1st element of arQuote
arQuote[0] = arQuote2[1]
print(arQuote)

# 6. Copy from the 1st element of arQuote2 to the 2nd element of arQuote
arQuote[1] = arQuote2 [0]
print(arQuote)

# 7. Use pop() to remove the 8th element of the array and store in a variable
strPoppedWord = arQuote.pop(7)
print(arQuote)

# 8. Use pop() to remove the 7th element of the array
arQuote.pop(6)
print(arQuote)

# 9. Copy the current arQuote into arQuote2 again
arQuote2 = arQuote.copy()
print(arQuote)

# 10. Copy from the 6th element of arQuote2 to the 3rd element of arQuote
arQuote[2]  = arQuote2[5]
print(arQuote)

# 11. Copy from the 3rd element of arQuote2 to the 6th element of arQuote
arQuote[5] = arQuote2[2]
print(arQuote)

# 12. Copy from the 5th element of arQuote2 to the 4th element of arQuote
arQuote[3] = arQuote2[4]
print(arQuote)

# 13. Copy from the 4th element of arQuote2 to the 5th element of arQuote
arQuote[4] = arQuote2[3]
print(arQuote)

# 14. insert the value you stored in the variable into the 5th position in arQuote
arQuote.insert(4, strPoppedWord)

# 14(a). Increase readability
arQuote[0] = arQuote[0].capitalize()


# 15. Use a for loop to print each element of the array in order.
for i in arQuote:
    print(i, end=" ")
print("\n")


# Here's some more that I wanted to do, but for the sake of brevity, decided to comment out
# arQuoteReadable = arQuote.copy()
# arQuoteReadable.append(".")
# print(arQuoteReadable)