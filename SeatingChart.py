# Author: Tom Lenehan
import json
import random


# given the number of tables, the list of guests, and the planner's preferences, return a seating chart
# num_tables is an integer
# guest_list is a list of strings
# planner_preferences is a list of dictionaries, each dictionary has the following keys:
# "preference": "avoid" or "pair"
# "guests": a list of two guests
#
# the output seating_chart is a dictionary, where the keys are the table numbers and the values are lists of guests
def create_seating_chart(num_tables, guest_list, planner_preferences=None, test_name='test_case'):
    tables = {}
    for i in range(1, num_tables + 1):
        tables[f"table_{i}"] = []

    guest_preferences = {}
    if planner_preferences:
        for pref in planner_preferences:
            guest1 = pref["guests"][0]
            guest2 = pref["guests"][1]
            if guest1 not in guest_preferences:
                guest_preferences[guest1] = {"avoid": [], "pair": []}
            if guest2 not in guest_preferences:
                guest_preferences[guest2] = {"avoid": [], "pair": []}
            if pref["preference"] == "avoid":
                guest_preferences[guest1]["avoid"].append(guest2)
            elif pref["preference"] == "pair":
                guest_preferences[guest1]["pair"].append(guest2)

    for guest in guest_list:
        # Look up the guest's preferences
        preferred_pair = guest_preferences.get(guest, {}).get("pair", [])
        avoid_list = guest_preferences.get(guest, {}).get("avoid", [])

        # seat the guest at a preferred table
        preferred_table = None
        for table in tables:
            if guest not in tables[table] and all(pair in tables[table] for pair in preferred_pair):
                tables[table].append(guest)
                preferred_table = table
                break

        # If preferred table isn't found, seat randomly
        if not preferred_table:
            seated = False
            while not seated:
                table = random.choice(list(tables.keys()))
                if guest not in tables[table] and all(avoid not in tables[table] for avoid in avoid_list):
                    tables[table].append(guest)
                    seated = True

    # Write tables to a JSON file
    with open(test_name+'.json', 'w') as f:
        json.dump(tables, f)
