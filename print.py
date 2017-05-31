# your code goes here
import sys

conteudo = False
primes = [2,]
cases = []
max_value = 2
for line in sys.stdin :
	line = line.replace('\n','');
	if conteudo :
		case = line.split();	
		from_value = int(case[0])
		to_value = int(case[1])
		cases.append([from_value, to_value])
		if max_value < to_value :
			max_value = to_value
	conteudo = True

inc_value = int(max_value ** (0.5)) + 1
check_candidates_seed = [True] * (inc_value+1)

from_value = 2
while from_value < max_value :
	check_candidates = check_candidates_seed[:]
	i = 0
	for check in check_candidates :
		value  = from_value + i
		if check :
			svalue = (value*value - from_value)
			check_candidates[svalue::value] = [False for aa in check_candidates[svalue::value]]	
			if value in primes :
				check = False
				check_candidates [i] = [False]
			else :
				for prime in primes :
					if prime > value/2 :
						break
					elif value % prime == 0 :
						check = False
						check_candidates [i] = [False]
						break
			
			if check :
				primes.append(value);
				
		if value == max_value :
			break 
		i += 1
	from_value += inc_value

[print(value) for a , b in cases for value in primes if (value >= a and value <= b) ]
