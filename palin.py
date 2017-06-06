'''
PALIN - The Next Palindrome
http://www.spoj.com/problems/PALIN/
'''

def calculate_palin(number):
	new_number = number + 1 
	chars = str(new_number)
	n = len(chars)
	i = 0
	while i <= n / 2 :
		rchars = chars[::-1]
		num_ini = int(chars[i])
		num_fini = int(rchars[i])
		if num_ini == num_fini  :
			inc = 0
		elif  num_ini - num_fini < 0 :
			if i  == n/2 :
				inc = (num_fini - num_ini) / 10
			else :
				inc = (num_ini - num_fini) + 10
		else :
			inc = num_ini - num_fini
		new_number += int( inc * ( 10 ** i ) )
		chars = []
		chars = str(new_number)
		i += 1
		
	return new_number


qtd = int(input())
for _ in range(qtd):
    number = int(input().split()[0])
    print(calculate_palin(number))

