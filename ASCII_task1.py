#kieran burnett
#10-10-2014
#ASCII task one

num = int(input("Please enter a number to be converted to ASCII: "))
text = input("Please enter a word to be turned into its ASCII number: ")

num_p = chr(num)
text_p = ord(text)

print(" The number you entered in ASCII: ",num_p)
print(" Then number of the letter you entered: ",text_p)
