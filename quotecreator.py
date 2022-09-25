clippings = []
booklist = []

with open ('myclippings.txt', 'rt') as myfile:  #Reading the text file from Kindle
    for quote in myfile:          
       clippings.append(quote)

maxbooklength = len(clippings)/5; # to ensure while loop does not go above its length
divider = clippings[4] #to identify a new quote
i = 0

while i < maxbooklength-1: 
         if clippings[i*5-1] == divider: #if it finds a divider, means we have a quote
            book = clippings[i*5]; #book is found by looking one position before the divider.
            if book not in booklist: #if we haven't already saved the book
               booklist.append(book) #saving the book to the list of books
         i = i + 1;


print("\nQuotes from saved books in Kindle\n")
for i in range(len(booklist)): #printing out all the books in a list
   if i > 0:
      print(i, booklist[i], end="")

while True:
   
   booknr = int(input('\nWhich book would you like to list quotes for? '))
   chosen_book = booklist[booknr]
   print('\nThanks! Here are the saved quotes from the book: ' + str(chosen_book))

   i = 0

   amount = 0
   while i < maxbooklength-1:
      this_book = clippings[i*5] #walking through each book in the list of quotes
      if this_book == chosen_book: #if there's a match between the book in the loop and selected book
         this_quote = clippings[i*5+3] #quote is found by looking 3 steps ahead
         if len(this_quote) > 30: #Ignoring quotes that are too short
            amount = amount + 1 #to store amount of quotes found for each search
            print(this_quote)

      i = i + 1

   response = (input('Whoa! That was ' + str(amount) + ' quotes from the book ' + str(chosen_book) + '\nWould you like to do another search (Y/N)? '))
   if response == "N":
               False
   else:
      True
