# protected_tool_fixed.py
import os, base64, zlib, sys, hashlib, hmac, time
from colorama import Fore, Style, init
init(autoreset=True)

os.system("cls" if os.name == "nt" else "clear")

# Secret must match what encryptor used
SECRET = b"secret!"

# Replace this with the full base64 BLOB produced by your encryptor
BLOB = "C/nOK5ga+rt0nC0qxeYzQLq66Zl9CXLCmCTCyDfoTsv3CG+TfWc/yxa/Wvc6XEjfi/N>

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def decrypt(b64s: str) -> str:
    raw = base64.b64decode(b64s.encode())
    plain = zlib.decompress(xor_bytes(raw, SECRET))
    return plain.decode("utf-8")


VALID_KEY_HASH = "cb4d1f2d4fc24c2b45223a911cbb674712374cc6cd8564c1093ba9e7a>

def check_license(user_input: str) -> bool:
    hashed = hashlib.sha256(user_input.encode()).hexdigest()
    # temporary debug print (remove in production)
    print(Fore.CYAN + f"[DEBUG] user hash: {hashed}")
    return hmac.compare_digest(hashed, VALID_KEY_HASH)

print(Fore.CYAN + "═" * 55)
print(Fore.RED + Style.BRIGHT + "FIREWALL BREAKER OSINT v3.1 [PROTECTED]".c>
print(Fore.YELLOW + "Created by Alok Thakur".center(55))
print(Fore.MAGENTA + "Enter The Licence Key".center(55))                    print(Fore.CYAN + "═" * 55)

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
