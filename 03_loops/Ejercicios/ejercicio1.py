import os

os.system("clear" if os.name == "posix" else "cls")

contacts = {
    'Bob': 'ilovebunnies@gmail.com',
    'Wendy': 'ilovebirds@hotmail.com',
    'Cecilia': 'ilovecats@outlook.com'
}

# Add new key - value
contacts["alex"] = "coolalex@gmail.com"

# Remove item
contacts.pop("Wendy")

print(contacts)

print(f"Is alex in the dictionary? {'alex' in contacts}")

siblings = {
    'Bob': 3,
    'Wendy': 1,
    'Cecilia': 2
}

has_pet = {
    'Bob': True,
    'Wendy': False,
    'Cecilia': True
}

print(contacts["Bob"])
print(f"Siblings: {siblings}")
print(f"Has Pet: {has_pet}")

print("\n.keys() method")
for key in contacts.keys():
    print(key)

print("\n.values() method")
for value in contacts.values():
    print(value)

print("\n.items() method")
print(contacts.items())
for key, value in contacts.items():
    print(f"{key} : {value}")
