class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Step 1: Create a dictionary for list1 with the string as the key and its index as the value
        index_map = {s: i for i, s in enumerate(list1)}
        
        # Step 2: Initialize variables to track the minimum index sum and result
        min_sum = float('inf')
        result = []
        
        # Step 3: Iterate through list2 and find common strings
        for j, s in enumerate(list2):
            if s in index_map:
                # Calculate the index sum
                index_sum = index_map[s] + j
                
                # Step 4: Update the result based on the index sum
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [s]  # Start a new result list
                elif index_sum == min_sum:
                    result.append(s)  # Add to the current result list if index sum is the same
        
        # Step 5: Return the result
        return result
        

        