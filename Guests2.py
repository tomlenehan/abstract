from SeatingChart3 import create_seating_chart


# Test case 3
num_tables = 6
guest_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Isabelle", "John", "Katie", "Liam", "Mary", "Nancy", "Olivia", "Peter", "Quinn", "Rachel", "Sarah", "Tom"]
planner_preferences = [
    {"preference": "avoid", "guests": ["Alice", "Bob"]},
    {"preference": "avoid", "guests": ["Eve", "Frank"]},
    {"preference": "avoid", "guests": ["Liam", "Mary"]},
    {"preference": "pair", "guests": ["Charlie", "David"]},
    {"preference": "pair", "guests": ["Katie", "John"]},
    {"preference": "pair", "guests": ["Quinn", "Rachel"]},
    {"preference": "pair", "guests": ["Sarah", "Tom"]}
]
result = create_seating_chart(num_tables, guest_list, planner_preferences)
print(result)
