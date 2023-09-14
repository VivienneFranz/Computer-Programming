def print_my_name(name):
    print(name)

print_my_name('Bob')

def trip_planner(start, end, duration, mode):
    print(f"It looks like you're taking a trip to {start}")
    print(f"You are planning to get to {end}")
    print(f"It should take you about {duration} hours")
    print(f"I see you are taking a {mode}")

trip_planner('paradigm', 'the Delta Center', 0.5, 'car')
