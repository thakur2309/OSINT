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
