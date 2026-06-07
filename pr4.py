genre = input('please select a genre from the below options: \n1. crime \n2. fiction \n3. mystery')
if genre == 'crime':
    print('you have selected crime genre. Here are some book recommendations for you: \n1. A Good Girl guide to murder \n2. not quite dead yet')
elif genre == 'fiction':
    print('you have selected fiction genre. Here are some book recommendations for you: \n1. The hunger games \n2. the maze runner')
elif genre == 'mystery':
    print('you have selected mystery genre. Here are some book recommendations for you: \n1. the inheritance games \n2. The silent patient')
else:
    print('Invalid genre selected.')