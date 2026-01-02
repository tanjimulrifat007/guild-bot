# ==========================================================
#  PROJECT     : FF Guild Glory Engine
#  AUTHOR      : Saurabh 💀
# ==========================================================
# ====== CLASSES FOR CLIENT AND GUILD ENGINE ======
class FFClient:
    def __init__(self, region=None, client_tag=None):
        self.region = region
        self.client_tag = client_tag
        self.status = "INIT"
    def start(self):
        self.status = "RUNNING"
        print(f"[FFClient] Started client for region {self.region} with tag {self.client_tag}")
    def send_packet(self, uid):
        # fake packet send simulation
        time.sleep(0.05)
        return True

class GuildEngine:
    def __init__(self, client=None):
        self.client = client
        self.active = False
    def start(self):
        self.active = True
        print("[GuildEngine] Engine started successfully")
    def process_invitation(self, bot_id, uid):
        time.sleep(0.2)
        if bot_id == 27:
            return False  # simulate failure
        return True

# ==========================================================
# IMPORTS
# ==========================================================
import os
import sys
import time
import json
import random
import logging

# ==========================================================
# COLORS
# ==========================================================
CYAN   = "\033[96m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
RESET  = "\033[0m"

# ==========================================================
# GLOBALS
# ==========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACCESS_FILE = os.path.join(BASE_DIR, "access.txt")
ENGINE = None
CLIENT = None
ACCOUNTS = []

# ==========================================================
# UTILITIES
# ==========================================================
def fake_progress(delay=0.15, steps=15, prefix=""):
    for _ in range(steps):
        print(prefix + ".", end="", flush=True)
        time.sleep(delay)
    print()

def loading_step(title, duration=2):
    print(YELLOW + f"[*] {title}", end="", flush=True)
    fake_progress(0.3, duration*3)

# ==========================================================
# UI / BANNER
# ==========================================================
def show_banner():
    os.system("clear")
    print(CYAN + r"""
 ███████╗███████╗     ██████╗ ██╗   ██╗██╗██╗     ██████╗ 
 ██╔════╝██╔════╝    ██╔════╝ ██║   ██║██║██║     ██╔══██╗
 █████╗  █████╗      ██║  ███╗██║   ██║██║██║     ██║  ██║
 ██╔══╝  ██╔══╝      ██║   ██║██║   ██║██║██║     ██║  ██║
 ██║     ██║         ╚██████╔╝╚██████╔╝██║███████╗██████╔╝
 ╚═╝     ╚═╝          ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ 

        🔥 FF GUILD GLORY ENGINE 🔥

   👑 Developer  : Saurabh 💀
   📸 Instagram : @RealX.SilentZ
   📲 Telegram  : @Phantom4ura

   ⚙ Runtime    : TERMUX / LOCAL
   🌐 Transport : UDP SOCKET
-------------------------------------------------------------
""" + RESET)

# ==========================================================
# ACCOUNTS
# ==========================================================
def load_guest_accounts():
    global ACCOUNTS
    print(YELLOW + "[*] Loading guest accounts..." + RESET)
    if not os.path.exists(ACCESS_FILE):
        print(RED + "[!] access.txt missing" + RESET)
        return
    try:
        with open(ACCESS_FILE, "r") as f:
            data = json.load(f)
            ACCOUNTS = list(data.keys())
    except Exception as e:
        print(RED + "[!] access.txt corrupted" + RESET)
        return
    time.sleep(0.5)
    print(GREEN + f"[✓] Loaded {len(ACCOUNTS)} guest accounts" + RESET)
    fake_progress(0.1, 10, prefix=" [LOAD] ")

def validate_accounts():
    print(YELLOW + "[*] Validating accounts..." + RESET)
    fake_progress(0.2, 10, prefix=" [VALIDATE] ")
    print(GREEN + "[✓] Guest authentication ready" + RESET)

# ==========================================================
# INPUT
# ==========================================================
def ask_guild_id():
    while True:
        gid = input(GREEN + "➤ Enter Target Guild ID : " + RESET).strip()
        if gid.isdigit() and len(gid) == 10:
            return gid
        print(RED + "[!] Guild ID must be 10 digits" + RESET)

def ask_bot_count():
    while True:
        try:
            count = int(input(CYAN + "➤ Select bot count (1-55): " + RESET))
            if 1 <= count <= 55:
                return count
        except:
            pass
        print(RED + "[!] Invalid bot count" + RESET)

# ==========================================================
# CORE PIPELINE
# ==========================================================
def resolve_guild(guild_id):
    loading_step("Resolving guild core")
    print(GREEN + f"[✓] Guild {guild_id} resolved" + RESET)

def initialize_invitation_pipeline():
    loading_step("Building invitation pipeline", 4)
    print(GREEN + "[✓] Invitation pipeline online" + RESET)

def start_client_engine():
    global CLIENT, ENGINE
    print(BLUE + "[*] Starting client transport layer" + RESET)
    CLIENT = FFClient(region="IND", client_tag="GG-RUNTIME")
    CLIENT.start()
    print(BLUE + "[*] Starting guild engine core" + RESET)
    ENGINE = GuildEngine(CLIENT)
    ENGINE.start()

def assign_bots(bot_count):
    print(YELLOW + f"[*] Assigning {bot_count} bots to scheduler" + RESET)
    fake_progress(0.15, bot_count//2, prefix=" [ASSIGN] ")

def send_invitations(bot_count):
    for i in range(1, bot_count + 1):
        uid = ACCOUNTS[i-1] if i-1 < len(ACCOUNTS) else "UNKNOWN_UID"
        print(CYAN + f"[BOT-{i:02}] Sending guild invitation for UID {uid}" + RESET)
        time.sleep(0.7)
        if i == 27:
            print(RED + f"[BOT-{i:02}] attempting request failed from uid {uid}" + RESET)
            print(RED + "[BOT-27] failed request send" + RESET)
            break

def verify_invitation_delivery():
    print(YELLOW + "[*] Verifying invitation delivery..." + RESET)
    fake_progress(0.2, 12, prefix=" [VERIFY] ")
    print(RED + "[!] Partial delivery detected" + RESET)

# ==========================================================
# ERRORS
# ==========================================================
def simulate_udp_failure():
    print(RED + "\n[UDP ERROR] Socket capture failed" + RESET)
    print(RED + "[TRANSPORT] Permission denied on UDP bind()" + RESET)
    print(RED + "[CLIENT] Transport moved to DEGRADED state" + RESET)
    print(RED + "[ENGINE] Guild glory execution halted" + RESET)

def explain_failure_reason():
    print(YELLOW + "\n[INFO] Failure Reason Detected:" + RESET)
    print(YELLOW + " - UDP SERVER SOCKET BLOCKED" + RESET)
    print(YELLOW + " - ISP / NETWORK RESTRICTION" + RESET)
    print(YELLOW + " - ROOT PERMISSION REQUIRED" + RESET)

def show_recovery_tips():
    print(BLUE + "\n[SUGGESTION]" + RESET)
    print(BLUE + " • Try different network" + RESET)
    print(BLUE + " • Use root-enabled environment" + RESET)
    print(BLUE + " • Avoid VPN / Proxy" + RESET)

# ==========================================================
# MAIN CONTROLLER
# ==========================================================
def main_controller():
    show_banner()
    load_guest_accounts()
    validate_accounts()
    guild_id = ask_guild_id()
    resolve_guild(guild_id)
    initialize_invitation_pipeline()
    bot_count = ask_bot_count()
    assign_bots(bot_count)
    start_client_engine()
    send_invitations(bot_count)
    verify_invitation_delivery()
    simulate_udp_failure()
    explain_failure_reason()
    show_recovery_tips()

# ==========================================================
# ENTRY POINT
# ==========================================================
if __name__ == "__main__":
    try:
        main_controller()
    except KeyboardInterrupt:
        print(RED + "\n[!] Process interrupted by user" + RESET)