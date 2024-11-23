import requests
import time

def scan_webpage_for_string(url, target_string):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Ensure the request was successful
        if target_string in response.text:
            print("String found!")
            return True
        else:
            print("String not found, checking again in 1 minute...")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

          
            
TOKEN = ''
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

# Example usage:
url_to_scan = "https://ra.co/events/1910964"
string_to_find = '"validType":"VALID"'

chat_id = "-1002151144544"
# message = "BILLETS RDY! https://ra.co/events/1910964#tickets"
message = ""
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

print(requests.get(url).json()) # this sends the message

while True:
    variable = scan_webpage_for_string(url_to_scan, string_to_find)
    if variable == True:

        print(requests.get(url).json()) # this sends the message
        # Wait for 1 minute before checking again
        time.sleep(60)


print(requests.get(url).json()) # this sends the message


