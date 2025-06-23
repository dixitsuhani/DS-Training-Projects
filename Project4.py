#Bus Fare Calculator
print('Welcome to Sharma Travels!!!\nDiscounts for age below or eaqual to 10 (-35%) and above or equal to 65 (-30%)')
people=int(input('Enter the number of people: '))
total_price=0
discounted_price=0
children=int(input('No. of members below or equal to 10: '))
above_65=int(input('No. of members above or equal to 65: '))
print('1. Jammu and Kashmir\n2. Shimla\n3. Haridwar\n4. Kanpur')
dest=int(input('Enter destination: '))
if dest==1:
    total_price=people*1000
    children=((children*1000)*35)/100
    above_65=((above_65*1000)*30)/100
    discounted_price=(total_price-(children+above_65))
    print('Payable Price: ',discounted_price)
    print('Thank-You')
elif dest==2:
    total_price=people*1200
    children=((children*1200)*35)/100
    above_65=((above_65*1200)*30)/100
    discounted_price=(total_price-(children+above_65))
    print('Payable Price: ',discounted_price)
    print('Thank-You')
elif dest==3:
    total_price=people*800
    children=((children*800)*35)/100
    above_65=((above_65*800)*30)/100
    discounted_price=(total_price-(children+above_65))
    print('Payable Price: ',discounted_price)
    print('Thank-You')
elif dest==4:
    total_price=people*600
    children=((children*600)*35)/100
    above_65=((above_65*600)*30)/100
    discounted_price=(total_price-(children+above_65))
    print('Payable Price: ',discounted_price)
    print('Thank-You')
else:
    print('Invalid choice!')
