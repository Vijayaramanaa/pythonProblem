#month starts from jan to may
expence = [2200,2350,2600,2130,2190]

# 1.)  In Feb, how many dollars you spent extra compare to January?
spent_Extra = expence[1]-expence[0]
print(spent_Extra)

#2. Find out your total expense in first quarter (first three months) of the year.
total_exp = expence[0]+expence[1]+expence[2]
print(total_exp)

#3. Find out if you spent exactly 2000 dollars in any month
2000 in expence
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expence.append(1980)
print(expence)

'''5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''
exchange = expence[3]-200
expence[3] = exchange
print(expence)

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list

length = len(heros)
print(length)

#2. Add 'black panther' at the end of this list

heros.append('black panther')
print(heros)

'''3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'''

heros.remove('black panther')
heros.insert(2,'black panther')
print(heros)

'''4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.'''

heros[1:3] = ['doctor strange']
print(heros)

heros.sort()
print(heros)

''' 3.) Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function'''
a = int(input("Enter the number range to find odd no. :"))
sotreNum = []
for i in range(1,a+1):
    if i % 2 != 0:
        sotreNum.append(i)
print(sotreNum)