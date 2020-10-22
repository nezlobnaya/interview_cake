def merge_lists(my_list, vlads_list):
    # Set up our merged_list
    merged_list_size = len(my_list) + len(vlads_list)
    merged_list = [None] * merged_list_size

    current_index_vlads = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_vlads_list_exhausted = current_index_vlads >= len(vlads_list)
        if (not is_my_list_exhausted and
                (is_vlads_list_exhausted or
                 my_list[current_index_mine] < vlads_list[current_index_vlads])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = vlads_list[current_index_vlads]
            current_index_vlads += 1

        current_index_merged += 1

    return merged_list

    # O(n) time and O(n)O(n)O(n) additional space, 
    # where nnn is the number of items in the merged list. 
my_list     = [3, 4, 6, 10, 11, 15]
vlads_list = [1, 5, 8, 12, 14, 19]
print(merge_lists(my_list, vlads_list))
