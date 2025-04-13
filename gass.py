import re
import time
import random
import os
import sys
from urllib.parse import urlparse
from colorama import Fore, init

init(autoreset=True)

def Banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    banner_text = '''

               __
              / _)
     _/\/\/\_/ / 
   _|         /  
 _|  (  | (  |   
/__.-'|_|--|_|  
=======================
[ Domain Extractor Pro ]
'''
    for line in banner_text.split('\n'):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.03)

def extract_domains_from_file(filename):
    extracted_domains = set()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
                for url in urls:
                    parsed = urlparse(url)
                    domain = parsed.netloc
                    if domain not in extracted_domains:
                        extracted_domains.add(domain)
                        print(Fore.RED + '[Extracted] ' + Fore.GREEN + domain)
        return extracted_domains
    except FileNotFoundError:
        print(Fore.RED + f"[!] File '{filename}' tidak ditemukan!")
        return set()
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")
        return set()

def save_domains(domains, output_file='domain.txt'):
    with open(output_file, 'w') as out:
        for domain in sorted(domains):
            out.write(domain + '\n')
    print(Fore.CYAN + f"\n[+] Total {len(domains)} domain disimpan di '{output_file}'")

def main():
    Banner()
    filename = input(Fore.YELLOW + "\n[?] Masukkan nama file (contoh: list.txt): ").strip()
    domains = extract_domains_from_file(filename)
    if domains:
        save_domains(domains)

if __name__ == "__main__":
    main()
