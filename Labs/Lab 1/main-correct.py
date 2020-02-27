import copy

def power_set(S):
	if len(S) == 0:
		return [[]]
	else:
		x = S.pop()
		ps = power_set(S)
		ps_copy = copy.deepcopy(ps)
		for i in ps_copy:
			i.append(x)
		return ps + ps_copy


def k_subsets_better(S, k):
	if k < 0 or k > len(S):
		return []
	elif k == len(S):
		return [S]
	else:
		x = S.pop()
		S_copy = copy.deepcopy(S)
		subsets_with_x = k_subsets_better(S, k-1)
		for i in subsets_with_x:
			i.append(x)
		subsets_without_x = k_subsets_better(S_copy, k)
		return subsets_with_x + subsets_without_x


if __name__ == "__main__":
	S = [1, 2, 3, 4, 5]
	S_copy = copy.deepcopy(S)
	print(power_set(S))

	print(k_subsets_better(S_copy, 4))