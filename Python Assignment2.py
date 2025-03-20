def list_operations():
    # Create an empty list
    my_list = []
    print("Empty list created:", my_list)
    
    # Append elements 10, 20, 30, 40
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print("After appending elements:", my_list)
    
    # Insert value 15 at the second position (index 1)
    my_list.insert(1, 15)
    print("After inserting 15 at position 2:", my_list)
    
    # Extend my_list with [50, 60, 70]
    my_list.extend([50, 60, 70])
    print("After extending the list:", my_list)
    
    # Remove the last element
    my_list.pop()
    print("After removing the last element:", my_list)
    
    # Sort in ascending order
    my_list.sort()
    print("After sorting in ascending order:", my_list)
    
    # Find and print the index of value 30
    index_of_30 = my_list.index(30)
    print(f"The index of value 30 is: {index_of_30}")
    
    return my_list

# Call the function to see the results
final_list = list_operations()
print("Final list:", final_list)
