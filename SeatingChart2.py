import random

def create_seating_chart(num_tables, guest_list, planner_preferences=None):
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
                guest_preferences[guest2]["avoid"].append(guest1)
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
                if guest not in tables[table] and all(avoid not in
                                                      tables[table] for avoid in avoid_list):
                    tables[table].append(guest)
                    seated = True

        # print(tables)
        for table in tables:
            print(table, tables[table])