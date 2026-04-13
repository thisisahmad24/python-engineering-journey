from engine import *

add_entry(1000, "food", "pizza")
add_entry(300, "travel", "bus")

print("Filtered:", filter_category("food"))
print("Sorted:", sort_by_amount())
print("Analysis:", analyze())

update_entry(1, {"amount": 1500})
delete_entry(2)

pretty()