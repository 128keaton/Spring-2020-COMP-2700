# power_set.py

from lib.pwetty_pwint_0w0 import pretty_print;

def power_set(set):
	if len(set) != 0:
		result = power_set(set[1:])
		return result + [[set[0]] + element for element in result]
	else:
		return [[]]

def k_subsets_naive(set, cardinality):
	final_set = []
	if (cardinality <= len(set) and cardinality > 0):
		full_set = power_set(set)
		for subset in full_set:
			if (len(subset) == cardinality):
				final_set.append(subset)

	return final_set




original_set = ['Torchic', 'Piplup', 'Rowlet']
power_set_result = power_set(original_set)
subsets_result = k_subsets_naive([4, 5, 6], 2)

pretty_print(original_set, 'Original Set')
pretty_print(power_set_result, 'Power Set')
pretty_print(subsets_result, 'Native Subsets')
