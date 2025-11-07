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

# SHA256 of "ALOKTHAKUR2025"
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
