import sys
import requests

def download_url_and_get_all_hrefs(url):
    hrefs = []
    response = requests.get(url)
    if response.status_code == 200:
        obsah = response.content.decode('utf-8', errors='ignore')
        casti = obsah.split('href="')
        for cast in casti[1:]:
            konec = cast.find('"')
            odkaz = cast[:konec]
            hrefs.append(odkaz)
    return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        print(odkazy)
    except IndexError:
        print("Chyba: Nezadali jste URL jako argument")
        print("Pouziti: python sixth.py <url>")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
