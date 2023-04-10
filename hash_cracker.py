import hashlib
import sys
import pyfiglet 



ascii_banner = pyfiglet.figlet_format("HashBat")
print(ascii_banner)

print("Available Algorithms: MD5 | SHA1 | SHA224 | SHA512 | SHA224 | SHA384")

hash_type = str(input("What's the hash type? "))
wordlist_location = str(input("Wordlist location: "))
hash = str(input("Enter hash: "))

word_list = open(f"{wordlist_location}").read()
list = word_list.splitlines()

for word in lists:
    if hash_type == "MD5":
        hash_object = hashlib.md5(f"{word}".encode('utf-8'))