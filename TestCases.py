from SeatingChart import create_seating_chart

test_name = "test_case_1"
num_tables = 4
guest_list = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Isabella", "Jack", "Kate", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rose", "Sarah", "Tom"]
planner_preferences = [
    {"preference": "avoid", "guests": ["Alice", "Bob"]},
    {"preference": "avoid", "guests": ["Charlie", "David"]},
    {"preference": "avoid", "guests": ["Emily", "Frank"]},
    {"preference": "avoid", "guests": ["Grace", "Henry"]},
    {"preference": "avoid", "guests": ["Isabella", "Jack"]},
    {"preference": "avoid", "guests": ["Kate", "Liam"]},
    {"preference": "avoid", "guests": ["Mia", "Noah"]},
    {"preference": "avoid", "guests": ["Olivia", "Peter"]},
    {"preference": "avoid", "guests": ["Quinn", "Rose"]},
    {"preference": "avoid", "guests": ["Sarah", "Tom"]},
    {"preference": "pair", "guests": ["Alice", "Charlie"]},
    {"preference": "pair", "guests": ["David", "Emily"]},
    {"preference": "pair", "guests": ["Frank", "Grace"]},
    {"preference": "pair", "guests": ["Henry", "Isabella"]},
    {"preference": "pair", "guests": ["Jack", "Kate"]},
    {"preference": "pair", "guests": ["Liam", "Mia"]},
    {"preference": "pair", "guests": ["Noah", "Olivia"]},
    {"preference": "pair", "guests": ["Peter", "Quinn"]},
    {"preference": "pair", "guests": ["Rose", "Sarah"]},
    {"preference": "pair", "guests": ["Tom", "Alice"]}
]
seating_chart = create_seating_chart(num_tables, guest_list, planner_preferences, test_name)

test_name = "test_case_2"
num_tables = 5
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
result = create_seating_chart(num_tables, guest_list, planner_preferences, test_name)


test_name = "test_case_3"
num_tables = 2
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
result = create_seating_chart(num_tables, guest_list, planner_preferences, test_name)


test_name = "test_case_4"
num_tables = 4
guest_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Isabelle", "John", "Katie", "Liam", "Mary", "Nancy", "Olivia", "Peter", "Quinn", "Rachel", "Sarah", "Tom"]
result = create_seating_chart(num_tables, guest_list, [], test_name)


test_name = "test_case_5"
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
result = create_seating_chart(num_tables, guest_list, planner_preferences, test_name)
