print('guess the number game')
s_num=13
u_num=int(input('enter your guess: '))
if u_num == s_num:
    print('congratulations! you guessed it right.')
elif u_num== s_num+1 or u_num==s_num-1:
    print('close enough to the correct answer.')
else:
    print('try again.')