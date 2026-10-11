import os

# Bad practice that Bandit will detect
def run_command(user_input):
    os.system(user_input)  # (Command Injection)

print("Hello DevSecOps!")
