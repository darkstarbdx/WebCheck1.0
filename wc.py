import requests
import logging
import sys
import re
import time
import threading

# Configure logging
logging.basicConfig(filename='website_checker.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Function to print flashing text
def flashing_text():
    while getattr(flashing_thread, "do_run", True):
        sys.stdout.write("\r\033[1;3;34mCHECKING, WAIT A WHILE.....\033[0m")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r                           ")
        sys.stdout.flush()
        time.sleep(0.5)

def check_website_status(url, retry_attempts=10):
    try:
        logging.info(f"Checking status of {url}")
        # Validate URL
        if not re.match(r"^https?://", url):
            raise ValueError("Invalid URL. Make sure to include 'http://' or 'https://'.")

        for attempt in range(1, retry_attempts + 1):
            response = requests.get(url)

            # Check response status code
            if response.status_code == 200:
                logging.info(f"The website {url} is up and running.")
                print(f"\033[1;32mThe website {url} is up and running.\033[0m")
                return
            else:
                logging.warning(f"Attempt {attempt}: The website {url} is down. Status code: {response.status_code}")
                print(f"\033[1;31mAttempt {attempt}: The website {url} is down. Status code: {response.status_code}\033[0m")

            time.sleep(1)  # Wait for 1 second before retrying

        logging.error(f"The website {url} is still down after {retry_attempts} attempts.")
        print(f"\033[1;31mThe website {url} is still down after {retry_attempts} attempts.\033[0m")

    except requests.RequestException as e:
        logging.error(f"Error occurred while trying to connect to {url}: {e}")
        print(f"Error occurred while trying to connect to {url}: {e}")
    except ValueError as e:
        logging.error(f"Invalid URL: {e}")
        print(f"Invalid URL: {e}")

def main():
    # Display ASCII art
    ascii_art = """
   
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░   ░▒▓█▓▒░  ░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ v1.0

				          🔰 𝚆𝚎𝚋𝚜𝚒𝚝𝚎 𝚂𝚝𝚊𝚝𝚞𝚜 𝙲𝚑𝚎𝚌𝚔𝚎𝚛 🔰
                                                                                                                
                                                                                                                

    """
    print(ascii_art)

    # Prompt user for URL
    url = input("\033[1;33mEnter the URL of the website to check:\033[0m ")

    # Start flashing text thread
    global flashing_thread
    flashing_thread = threading.Thread(target=flashing_text)
    flashing_thread.daemon = True
    flashing_thread.start()

    # Check website status
    check_website_status(url)

    # Stop flashing text thread after website checking completes
    flashing_thread.do_run = False

if __name__ == "__main__":
    main()
