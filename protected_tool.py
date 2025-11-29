# protected_tool_fixed.py
import os, base64, zlib, sys, hashlib, hmac, time
from colorama import Fore, Style, init
init(autoreset=True)

os.system("cls" if os.name == "nt" else "clear")

# Secret must match what encryptor used
SECRET = b"secret!"  

# Replace this with the full base64 BLOB produced by your encryptor
BLOB = "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"

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def decrypt(b64s: str) -> str:
    raw = base64.b64decode(b64s.encode())
    plain = zlib.decompress(xor_bytes(raw, SECRET))
    return plain.decode("utf-8")


VALID_KEY_HASH = "cb4d1f2d4fc24c2b45223a911cbb674712374cc6cd8564c1093ba9e7a45db501"

def check_license(user_input: str) -> bool:
    hashed = hashlib.sha256(user_input.encode()).hexdigest()
    # temporary debug print (remove in production)
    print(Fore.CYAN + f"[DEBUG] user hash: {hashed}")
    return hmac.compare_digest(hashed, VALID_KEY_HASH)

print(Fore.CYAN + "═" * 55)
print(Fore.RED + Style.BRIGHT + "FIREWALL BREAKER OSINT v3.1 [PROTECTED]".center(55))
print(Fore.YELLOW + "Created by Alok Thakur".center(55))
print(Fore.MAGENTA + "Enter The Licence Key".center(55))
print(Fore.CYAN + "═" * 55)

key = input(Fore.YELLOW + Style.BRIGHT + "\nEnter License Key: ").strip()

if not check_license(key):
    print(Fore.RED + "\nInvalid Key! Access Denied.")
    sys.exit(1)

print(Fore.GREEN + "Key Verified! Starting...\n")
time.sleep(1)

try:
    code = decrypt(BLOB)
    ns = {}
    exec(code, ns)
    ns["run"]()
except Exception as e:
    print(Fore.RED + f"Error: {e}")
    sys.exit(1)
