def generate_profile(age):
    """Determines the user's 'life stage' based on their age."""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


user_name = input("Enter your full name: ").strip()
birth_year_str = input("Enter your birth year: ").strip()

current_year = 2025

try:
    birth_year = int(birth_year_str)
    if not (1900 < birth_year < current_year):
        print("Year must be between 1901 and 2024. Using 2000 as default.")
        birth_year = 2000
except ValueError:
    print("Invalid year entered. Using 2000 as default.")
    birth_year = 2000

current_age = current_year - birth_year

hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ").strip()
    if hobby.lower() == "stop":
        break
    if hobby:
        hobbies.append(hobby)

life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

print("\n---\nProfile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

if not user_profile["hobbies"]:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile["hobbies"]:
        print(f"- {hobby}")

print("---")
