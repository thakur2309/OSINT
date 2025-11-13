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
