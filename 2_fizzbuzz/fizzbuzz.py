# Program bude postupne vypisovat cisla od 1 do n,
# ak je cislo delitelne 3 tak namieso neho vypise fizz,
# ak je delitelne 5 tak namiesto neho vypise buzz a
# ak je delitelne 3 a 5 tak namiesto neho vypise fizzbuzz

n = 20

# Vseobecne dobre riesenie, kazdy pripad popisany (pripadne aj nepopisany) zo
# zadanie je explicitne vyrieseny
for i in range(1,n):
    if i%3 == 0 and i%5 == 0:
        print('fizzbuzz')
    elif i%3 == 0:
        print('fizz')
    elif i%5 == 0:
        print ('buzz')
    else:
        print(i)