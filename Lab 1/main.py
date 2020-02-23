# main.py
# kbrleson
from lib.pwetty_pwint_0w0 import pretty_print;
from time import process_time 

# 1
def power_set(set):
	if len(set) != 0:
		result = power_set(set[1:])
		return result + [[set[0]] + element for element in result]
	else:
		return [[]]

# 2
def k_subsets_naive(set, cardinality):
	final_set = []
	if (cardinality <= len(set) and cardinality > 0):
		full_set = power_set(set)
		for subset in full_set:
			if (len(subset) == cardinality):
				final_set.append(subset)

	return final_set

# 3
def k_subsets_better(set, cardinality):
	final_set = []
	
	if cardinality > 0 and cardinality <= len(set):
		if cardinality == len(set):
			final_set = [set]
		else: 
			element = set.pop(-1)
			final_set = k_subsets_better(set, cardinality)
			subsets = power_set(set)
			for subset in subsets:
				if len(subset) == cardinality - 1:
					subset.append(element)
					final_set.append(subset)
				
				
			
	return final_set


original_set = ['Torchic', 'Piplup', 'Rowlet']
power_set_result = power_set(original_set)

naive_start_time = process_time()
subsets_naive_result = k_subsets_naive([4, 5, 6, 7], 2)
naive_end_time = process_time()
naive_elapsed = naive_end_time = naive_start_time

better_start_time = process_time()
subsets_better_result = k_subsets_better([4, 5, 6, 7], 3)
better_end_time = process_time()
better_elapsed = better_end_time - better_start_time

pretty_print(original_set, 'Original Set')
pretty_print(power_set_result, 'Power Set')

print('The "k_subsets_naive" function took %f seconds' % naive_elapsed)
pretty_print(subsets_naive_result, 'Naive Subsets')

print('The "k_subsets_better" function took %f seconds' % better_elapsed)
pretty_print(subsets_better_result, 'Better Subsets')
