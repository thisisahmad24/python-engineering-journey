
expenses = [200,100,450,333,123,981]
if expenses:
    # Doubled Amount 
    doubled = [e*2 for e in expenses]
    print(doubled)
    # Filtered Amount
    filtered = [e for e in expenses if e > 300]
    print(filtered)
else:
    print("No expenses to process.")
    
