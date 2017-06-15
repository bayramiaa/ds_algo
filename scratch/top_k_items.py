## Given an array of n items. return top K items
import random
import heapq

array = [random.randint(1, 10) for _ in range(10)]

def return_top_k(arr, k):  # O(n + (n)log(n))

	## get item counts
	count_dic = {}
	for item in arr: ## O(n)
		count_dic[item] = count_dic.get(item, 0) + 1

	freq_list = []
	for key, val in count_dic.iteritems(): ## O(n)
		freq_list.append((-val, key))

	heapq.heapify(freq_list) #nlogn

	topk = []
	for i in range(k): ## O(klog(n))
		 topk.append(heapq.heappop(freq_list)[1])
	
	return freq_list

return_top_k(array, 3)



array = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6 ]
def return_top_k2(arr, k): # O(n + (n)log(k))

	count_dict = {}
	for item in arr: ## O(n)
		count_dict[item] = count_dict.get(item, 0) + 1

	heap = []
	for key, val in count_dict.iteritems(): ## O(n)
		if len(heap) < 3:
			heapq.heappush(heap, (val, key)) # O(log(k))
		else:
			m = heapq.heappop(heap)
			if val > m[0]:
				heapq.heappush(heap, (val, key)) # O(log(k)
			else:
				heapq.heappush(heap, m)

	resp = []
	while len(heap) > 0: # O(klog(k))
		resp.append(heapq.heappop(heap)[1])
	return resp

return_top_k2(array, 3)
