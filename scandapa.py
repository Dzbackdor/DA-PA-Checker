import argparse
import os
import requests
import json
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

def main(scan):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_directory, scan)
    with open(full_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]

    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IlRqZS9VVTBKU09TcHVqcCt2UmlhUVE9PSIsInZhbHVlIjoiVVVQb1Vvc3RHaDk4QlpORjZvNTdOdS9aWHRoQmpTZnBaUGROSS9sRm13THJSWUZHTU9Ja1BweGRqbnVWSS93alAvV1phendOQVpkV084TEwzZGZQMzc3b2dGV1hCS3pEZW9rNUlJc3JZV3hobjRKV0EvekZsOVVheUwwWW9iQngiLCJtYWMiOiI3MmE3OThlNjBmYmUyZWM0MDc2ODFjNDZiZGQwMDJjNWIzYjU2YjNhOTFkY2MyZGMzZjg5YWRiYzM5ZDlmZjllIiwidGFnIjoiIn0%3D',
        'prepostseocom_session': 'eyJpdiI6IkQxaGJMZnVKVEI5clViQUI2Z2lTQWc9PSIsInZhbHVlIjoiNjJ5aTZFWHpEYTd6RkpiN09BbzdidFFQOC8wTmdEeGd4Q1RZMURoM2xJT1h2TnRPYUpzVUh6RTBaREFTNmVIaHlyRFlKbDNPdWRCMG1LK0gvTHZWdm1UVmJvejl0TGxaT1lJa1J2WHJjV3l4WU1vUHhFTGl3MWdVeDdUUnJ4blMiLCJtYWMiOiJiNzhlZGFhZDU2Y2ZmYmU4MDllZDljM2YyMzdiOTQyODg1N2QzMjhiOTg2MjI1ZjQ4NDQxZWYwYjg1OWJmNTk3IiwidGFnIjoiIn0%3D',
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-csrf-token': 'PX2KLg0dAq5EgvjrUOiCzG99vtNBBBp2zfnjR2N8',
        'x-requested-with': 'XMLHttpRequest',
    }

    if not urls:
        print("Tidak ada URL yang ditemukan dalam file.")

    for url in urls:
        payload = {
            'urls[]': url,
            'count': '0',
            'tool_key': 'domain_authority_checker',
        }

        response = requests.post('https://www.prepostseo.com/ajax/check-authority', cookies=cookies, headers=headers, data=payload)
        if response.status_code == 200:
            
            try:
                json_data = response.json()
                for item in json_data:
                    print(f"\033[1;97mURL\033[1;92m: \033[1;97m{url}")
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
                    with open('hasil.txt', 'a', encoding='utf-8') as file:
                        if url.strip():
                            file.write(f"{url}\nDA ➾ {da} | PA ➾ {pa}\n🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸\n")
            except json.JSONDecodeError:
                print("Gagal mem-parsing respons JSON.")
        else:
            print(f"Gagal memproses URL: {url}")

    print(f'\033[1;32mDone proses save as ['+putih+'hasil.txt'+hijau+']\033[1;97m....!!')

if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(description="Process URL file.")
    parser.add_argument("-scan", help="File containing URLs to process.", required=True)
    args = parser.parse_args()
    main(args.scan)