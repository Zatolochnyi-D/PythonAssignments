# Task 3
def delete_third_elements(list):
    print(list)                    # Print initial list.
    counter = 2 % len(list)        # Start counter that will identify index to remove. Start from 2 (third element). Take remaining
    while (True):                  # if list length is less than 2.
        del list[counter]
        print(list)                # Print list with remove element.
        if (len(list) == 0):       # Stop iteration when list is empty.
            break
        counter += 2               # If list is still not empty, increase counter by 3 - 1 to get next third element. Limit by length of list. How it workds:
        counter %= len(list)       # [1, 2, 3, 1, 2, 3] -> [1, 2, 1, 2, 3]
                                   #        ↑ pointer     pointer ↑     ↑ next needed element

# Demonstration
delete_third_elements([1, 2, 3, 4, 5, 6]) # Expected: [1, 2, 3, 4, 5, 6]
                                          #           [1, 2, 4, 5, 6]
                                          #           [1, 2, 4, 5]
                                          #           [1, 2, 5]
                                          #           [1, 5]
                                          #           [1]
                                          #           []