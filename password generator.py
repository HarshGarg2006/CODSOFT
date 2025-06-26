import secrets, string
def generate_password(ensure_complexity=True):
    if length < 4:
        raise ValueError("Password must have atleast 4 characters")
    
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if not ensure_complexity:
            return password
        
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
            return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length (≥ 4): "))
        password = generate_password(length)
        print("Generated Password:",password)
    except ValueError as e:
        print("Error:",e)
  
