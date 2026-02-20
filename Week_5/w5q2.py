# Write a program to simulate simple brute force attack. 
# Try to crack numeric passwords of length 4,6 and 8 digits. 



import time
from itertools import product

def brute_force_numeric(target_password):
    length = len(target_password)
    attempts = 0
    start_time = time.time()

    # Generate all combinations of digits of given length
    for combination in product("0123456789", repeat=length):
        attempts += 1
        guess = ''.join(combination)

        if guess == target_password:
            end_time = time.time()
            return {
                "password": guess,
                "attempts": attempts,
                "time_taken": end_time - start_time
            }

    return None


if __name__ == "__main__":
    target = input("Enter numeric password (4, 6, or 8 digits): ")

    if not target.isdigit() or len(target) not in [4, 6, 8]:
        print("Password must be numeric and 4, 6, or 8 digits long.")
    else:
        print("\nStarting brute force attack...")
        result = brute_force_numeric(target)

        if result:
            print("\nPassword cracked!")
            print(f"Password: {result['password']}")
            print(f"Attempts: {result['attempts']}")
            print(f"Time taken: {result['time_taken']:.4f} seconds")