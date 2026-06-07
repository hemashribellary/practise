name = input('What is your name? ')
age= int(input('How old are you? '))
if age < 18:
    print('relax', name, 'you are not an adult yet. Enjoy your youth!')
elif age == 18:
    print('unfortunately', name, 'you are an adult now.Get ready to face the world!')  
else:
    print('you have already been an adult for', age - 18, 'years,', name, 'you are all grown up!')