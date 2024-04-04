
import argparse
import requests
import json
import sys
from bs4 import BeautifulSoup
from colorama import Fore,Back,init


B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
H = Fore.BLACK
Y = Fore.YELLOW

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
hijau   =   "\033[1;92m"
putih   =   "\033[1;97m"
abu     =   "\033[1;90m"
kuning  =   "\033[1;93m"
ungu    =   "\033[1;95m"
merah   =   "\033[1;91m"
biru    =   "\033[1;96m"
kuning2 =   "\33[1;33m"
biru2   =   "\33[0;36m"

def banner():
    print(f"""{G}
██████╗  █████╗     ██████╗  █████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██║  ██║███████║    ██████╔╝███████║    ███████╗██║     ███████║██╔██╗ ██║
██║  ██║██╔══██║    ██╔═══╝ ██╔══██║    ╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝██║  ██║    ██║     ██║  ██║    ███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
\033[1;31m{'Bulk Cek DA PA - Cek domain authority ['+putih+'500 URLs'+re+']':^88}\033[1;97m
\033[1;97m{Fore.YELLOW+'['+hijau+'•'+Fore.YELLOW+']'+Fore.WHITE+'Creat By Dzone':^95}
==========================================================================
""")


def set_session_cookie():
    session = requests.Session()
    urldapa = "https://www.prepostseo.com/id/domain-authority-checker"
    response = session.get(urldapa)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        hd_token = soup.find('input', {'name': '_token'})
        if hd_token:
            hdr_token = hd_token['value']
        else:
            print("Token CSRF tidak ditemukan.")
            sys.exit(1)
    else:
        print("Gagal mengatur session cookie.")
        sys.exit(1)

    return session, hdr_token

def get_domain_authority(session, token, url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-csrf-token': token,
        'x-requested-with': 'XMLHttpRequest',
    }
    payload = {
        'urls[]': url,
        'count': '0',
        'tool_key': 'domain_authority_checker',
    }
    response = session.post('https://www.prepostseo.com/ajax/check-authority', headers=headers, data=payload)

    if response.status_code == 200:
        json_data = response.json()
        try:
            for item in json_data:
                url = item['url']
                print("\033[1;93mDA \033[1;92m➾ \033[1;97m", item['domain_auth'], end='')
                if int(item['domain_auth']) > 9:
                    print(" \033[1;32m•\033[1;91mHigh\033[1;97m", end='')
                print()
                print("\033[1;93mPA \033[1;92m➾ \033[1;97m", item['page_auth'], end='')
                if int(item['page_auth']) > 9:
                    print(" \033[1;32m•\033[1;91mHigh\033[1;97m", end='')
                print()
                print("\033[1;93mSpam Score \033[1;92m➾ \033[1;97m", item['spam_score'])
                print("\033[1;93mMoz Rank \033[1;92m➾ \033[1;97m", item['m_rank'])
                print("\033[1;93mData Source \033[1;92m➾ \033[1;97m", item['data_source'])
                print("----------------------------------------")
                da = item['domain_auth']
                pa = item['page_auth']
                ss = item['spam_score']
                with open('result.txt', 'a', encoding='utf-8') as file:
                        if url.strip():
                            file.write(f"{url}\nDA ➾ {da} | PA ➾ {pa} | Spam Score ➾ {ss}\n🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸\n")
        except json.JSONDecodeError:
            print("Gagal mem-parsing respons JSON.")
    else:
        print("Gagal melakukan permintaan.")

def main():
    parser = argparse.ArgumentParser(description="Scan domain authority for URLs in a file.")
    parser.add_argument("-scan", dest="filename", required=True, help="Path to the file containing URLs to scan.")
    args = parser.parse_args()

    with open(args.filename, "r") as file:
        urls = [line.strip() for line in file.readlines() if line.strip()]

    if not urls:
        print("Tidak ada URL yang ditemukan dalam file.")
        return

    session, token = set_session_cookie()

    for url in urls:
        print(f"Scanning URL: \033[1;32m{url}")
        get_domain_authority(session, token, url)

if __name__ == "__main__":
    banner()
    main()
