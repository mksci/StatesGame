
states=[
    'Alabama',
    'Alaska',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana' ,
    'Maine',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming' 
]

states2 = []


print ('Zobaczmy ile z 50 stanow USA potrafisz wymienic w ciagu 6 minut.\nAby zakonczyc gre przed czasem wpisz \'wyjdz\'. Zaczynajmy!')

points=0 
errors=0

import time

now = time.time()
time_limit = 360
end_time = now + time_limit


while True:
    user_guess = str(input())
    if user_guess.lower() == 'wyjdz':
        break
    elif user_guess in states:
        points+=1
        print('Dobrze! Zgaduj dalej')
        states.remove(user_guess) 
        states2.append(user_guess)
    elif user_guess in states2:
        print('Podales juz ten stan. Probuj dalej')
    elif time.time() >= end_time:
        print('Czas minal.')
        break    
    else:
        print('Nie ma takiego stanu. Probuj dalej')
        #errors+=1
        #if errors > 2:
            #break
print('Gra skonczona. Odgadles %d stanow.' %points)



