def iterate_noloops(ilist, start, end):
	if start == end:
		return

	elif type(ilist[start]) is list:
		iterate_noloops(ilist[start], 0, len(ilist[start]))

	else:
		print(ilist[start])

	iterate_noloops(ilist, start+1, end)
  
  
  
new_list = ['sam', [['Test', [['one', [], []]], ['file.txt', ['id1', 1, 0]]], ['Test2', [], ['file2.txt', ['id2', 3, 2]]]], []]
