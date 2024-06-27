import requests
import time


def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "up"
        else:
            return "down"
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "down"


def main():
    url = "application url"
    while True:
        status = check_application_status(url)
        if status == "up":
            print(f"Application is up at {time.ctime()}")
        else:
            print(f"Application is down at {time.ctime()}")
        time.sleep(60)


if __name__ == "__main__":
    main()
