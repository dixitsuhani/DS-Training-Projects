#Library Fine Calculator
fine=5
title=input('Enter the name of the book: ')
book_id=int(input('Book ID: '))
returnInDays=int(input('No. of days you want to keep the book: '))
day_returned=int(input('No. of days the book is kept for: '))
if day_returned>returnInDays:
    print('Fine: ',(day_returned-returnInDays)*fine)
else:
    print('No fine!')