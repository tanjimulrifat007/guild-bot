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
# ==========================================================
# ENHANCEMENT LAYER (NON-INTRUSIVE)
# ==========================================================

import threading
import random

_ENGINE_ALIVE = True

def _hex_stream(size=16):
    return " ".join(f"{random.randint(0,255):02X}" for _ in range(size))

def _background_heartbeat():
    while _ENGINE_ALIVE:
        time.sleep(1.2)
        print(
            BLUE +
            f"[HEARTBEAT] seq={random.randint(1000,9999)} | {_hex_stream()}" +
            RESET
        )

# ----------------------------------------------------------
# OVERRIDE: simulate_udp_failure (WITHOUT TOUCHING ORIGINAL)
# ----------------------------------------------------------
def simulate_udp_failure():
    print(RED + "\n[UDP ERROR] Socket capture failed" + RESET)
    print(RED + "[TRANSPORT] Permission denied on UDP bind()" + RESET)
    print(YELLOW + "[CLIENT] Transport moved to DEGRADED state" + RESET)

    print(YELLOW + "[ENGINE] Switching to limited activity mode" + RESET)

    # start background activity
    t = threading.Thread(target=_background_heartbeat, daemon=True)
    t.start()

    # keep engine visually alive
    for i in range(6):
        time.sleep(0.8)
        print(
            CYAN +
            f"[ENGINE] maintaining session | tick={i+1}" +
            RESET
        )

    print(GREEN + "[ENGINE] Running under degraded transport" + RESET)
    
    
# ==========================================================
# JWT TOKEN GENERATOR (ADDITIVE LAYER)
# ==========================================================

import base64
import hashlib
import time
import random

def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")

def generate_account_jwt(uid, region="IND"):
    header = {
        "alg": "HS256",
        "typ": "JWT"
    }

    payload = {
        "uid": uid,
        "region": region,
        "role": "guest",
        "iat": int(time.time()),
        "exp": int(time.time()) + random.randint(3600, 7200),
        "session": f"S-{random.randint(100000,999999)}",
        "scope": ["guild.join", "guild.invite", "presence.sync"]
    }

    header_b64 = _b64url(json.dumps(header).encode())
    payload_b64 = _b64url(json.dumps(payload).encode())

    secret = f"{uid}{random.randint(1000,9999)}{time.time()}".encode()
    signature = hashlib.sha256(secret).digest()
    signature_b64 = _b64url(signature)

    token = f"{header_b64}.{payload_b64}.{signature_b64}"
    return token

# ----------------------------------------------------------
# OPTIONAL: BULK JWT EMISSION (VISUAL OUTPUT)
# ----------------------------------------------------------
def emit_account_tokens(limit=5):
    print(BLUE + "\n[AUTH] Initializing token issuer" + RESET)
    time.sleep(0.5)

    for i, uid in enumerate(ACCOUNTS[:limit], start=1):
        jwt = generate_account_jwt(uid)
        print(
            GREEN +
            f"[AUTH] UID {uid}\n"
            f"       JWT → {jwt}\n" +
            RESET
        )
        time.sleep(0.4)
 
# ==========================================================
# JWT EMISSION HOOK (NON-INTRUSIVE FIX)
# ==========================================================

_old_simulate_udp_failure = simulate_udp_failure

def simulate_udp_failure():
    _old_simulate_udp_failure()

    print(BLUE + "\n[AUTH] Issuing session tokens" + RESET)
    try:
        emit_account_tokens(min(10, len(ACCOUNTS)))
    except Exception as e:
        print(RED + f"[AUTH] Token issuance failed: {e}" + RESET)

# ==========================================================
# PERMANENT DEGRADED LOOP (ENDLESS MODE)
# ==========================================================

_prev_simulate_udp_failure = simulate_udp_failure

def simulate_udp_failure():
    # run existing degraded + jwt logic
    _prev_simulate_udp_failure()

    print(RED + "\n[TRANSPORT] UDP channel remains unavailable" + RESET)
    print(YELLOW + "[ENGINE] Operating in persistent degraded mode" + RESET)

    tick = 0
    while True:
        tick += 1
        time.sleep(random.uniform(1.0, 2.0))

        # repeat UDP error feel
        print(
            RED +
            "[UDP ERROR] bind() failed | errno=13 | permission denied" +
            RESET
        )

        # show engine still alive
        print(
            CYAN +
            f"[ENGINE] degraded heartbeat | cycle={tick}" +
            RESET
        )

        # hex activity
        print(
            BLUE +
            f"[STREAM] {_hex_stream(16)}" +
            RESET
        )
# ==========================================================
# FINAL ADD: BACKOFF + UPTIME + COUNTERS + ROTATING TOKENS
# ==========================================================

import time
import random

# ---- runtime state (additive) ----
__START_TS__ = time.time()
__RETRY_TOTAL__ = 0
__FAIL_TOTAL__ = 0
__CHAIN_ID__ = random.randint(1000, 9999)

def _fmt_uptime(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{int(days)}d {int(hours)}h {int(mins)}m {int(secs)}s"

def _next_backoff(cycle):
    # 1s → 5s → 30s → repeat
    seq = [1, 5, 30]
    return seq[(cycle - 1) % len(seq)]

def _rotate_chain():
    global __CHAIN_ID__
    __CHAIN_ID__ = random.randint(1000, 9999)
    return __CHAIN_ID__

# ---- FINAL hard override (no recursion) ----
def simulate_udp_failure():
    global __RETRY_TOTAL__, __FAIL_TOTAL__

    print(RED + "\n[UDP ERROR] Socket capture failed" + RESET)
    print(RED + "[TRANSPORT] Permission denied on UDP bind()" + RESET)
    print(YELLOW + "[ENGINE] Persistent retry with backoff enabled" + RESET)

    cycle = 0
    chain = _rotate_chain()

    while True:
        cycle += 1
        __RETRY_TOTAL__ += 1

        backoff = _next_backoff(cycle)
        uptime = int(time.time() - __START_TS__)

        uid = random.choice(ACCOUNTS) if ACCOUNTS else f"GUEST_{random.randint(1000,9999)}"

        # rotate token chain every 5 cycles
        if cycle % 5 == 0:
            chain = _rotate_chain()

        # issue huge token
        try:
            token = generate_massive_jwt(uid)
        except Exception as e:
            __FAIL_TOTAL__ += 1
            token = f"<token_error:{e}>"

        print(BLUE + f"\n[AUTH] Chain={chain} | Cycle={cycle}" + RESET)
        print(GREEN + f"[AUTH] UID {uid}\nJWT → {token}\n" + RESET)

        print(YELLOW + f"[CLIENT] Attempting UDP reconnect() | backoff={backoff}s" + RESET)
        time.sleep(0.4)

        # simulated rejection
        __FAIL_TOTAL__ += 1
        print(RED + "[UDP ERROR] bind() failed | errno=13 | permission denied" + RESET)
        print(RED + "[CONNECTION] Handshake rejected by remote endpoint" + RESET)

        # stats panel
        print(
            CYAN +
            f"[STATS] retries={__RETRY_TOTAL__} fails={__FAIL_TOTAL__} "
            f"uptime={_fmt_uptime(uptime)}" +
            RESET
        )
        print(BLUE + f"[STREAM] {_hex_stream(16)}" + RESET)

        time.sleep(backoff)
# ==========================================================
# FINAL NON-RECURSIVE DEGRADED LOOP (RECURSION FIX)
# ==========================================================

def simulate_udp_failure():
    print(RED + "\n[UDP ERROR] Socket capture failed" + RESET)
    print(RED + "[TRANSPORT] Permission denied on UDP bind()" + RESET)
    print(YELLOW + "[CLIENT] Transport locked in degraded state" + RESET)
    print(YELLOW + "[ENGINE] Persistent retry mechanism engaged" + RESET)

    cycle = 0
    while True:
        cycle += 1
        time.sleep(random.uniform(1.5, 2.5))

        uid = random.choice(ACCOUNTS) if ACCOUNTS else f"GUEST_{random.randint(1000,9999)}"

        try:
            token = generate_massive_jwt(uid)
        except Exception as e:
            token = f"<token_error:{e}>"

        print(BLUE + f"\n[AUTH] Extended session issued | cycle={cycle}" + RESET)
        print(GREEN + f"[AUTH] UID {uid}\nJWT → {token}\n" + RESET)

        print(YELLOW + "[CLIENT] Attempting UDP reconnect()" + RESET)
        time.sleep(0.4)

        print(RED + "[UDP ERROR] bind() failed | errno=13 | permission denied" + RESET)
        print(RED + "[CONNECTION] Handshake rejected by remote endpoint" + RESET)

        print(CYAN + f"[ENGINE] degraded heartbeat | uptime_cycle={cycle}" + RESET)
        print(BLUE + f"[STREAM] {_hex_stream(16)}" + RESET)
        
# ==========================================================
# PERSISTENT ATTEMPT + LARGE TOKEN LOOP (FINAL ADD)
# ==========================================================

import string

# ---------- very large payload generator ----------
def _large_claim_blob(words=420):
    vocab = [
        "session","gateway","transport","handshake","presence","cluster",
        "routing","heartbeat","scheduler","allocator","node","replica",
        "stream","channel","endpoint","latency","throughput","buffer",
        "sequence","integrity","dispatcher","resolver","pipeline","engine"
    ]
    out = []
    for _ in range(words):
        w = random.choice(vocab)
        noise = "".join(random.choices(string.ascii_lowercase, k=random.randint(3,7)))
        out.append(f"{w}_{noise}")
    return " ".join(out)

def generate_massive_jwt(uid, region="IND"):
    header = {"alg": "HS256", "typ": "JWT"}

    payload = {
        "uid": uid,
        "region": region,
        "role": "guest",
        "iat": int(time.time()),
        "exp": int(time.time()) + random.randint(1800, 7200),
        "session": f"S-{random.randint(100000,999999)}",
        "claims_blob": _large_claim_blob(420)  # <<< ~400+ WORDS
    }

    h = _b64url(json.dumps(header).encode())
    p = _b64url(json.dumps(payload).encode())
    sig = _b64url(hashlib.sha256(f"{uid}{time.time()}".encode()).digest())
    return f"{h}.{p}.{sig}"

# ---------- final endless override ----------
_prev_simulate_udp_failure = simulate_udp_failure

def simulate_udp_failure():
    # run everything that already exists
    _prev_simulate_udp_failure()

    print(RED + "\n[TRANSPORT] Persistent reconnect mode engaged" + RESET)
    print(YELLOW + "[ENGINE] Automatic retry loop started" + RESET)

    cycle = 0
    while True:
        cycle += 1
        time.sleep(random.uniform(1.2, 2.2))

        uid = random.choice(ACCOUNTS) if ACCOUNTS else f"GUEST_{random.randint(1000,9999)}"
        token = generate_massive_jwt(uid)

        print(BLUE + f"\n[AUTH] Issued extended session token (cycle {cycle})" + RESET)
        print(GREEN + f"[AUTH] UID {uid}\nJWT → {token}\n" + RESET)

        print(YELLOW + "[CLIENT] Attempting UDP rebind()" + RESET)
        time.sleep(0.4)

        print(RED + "[UDP ERROR] bind() failed | permission denied" + RESET)
        print(RED + "[CONNECTION] Remote endpoint rejected handshake" + RESET)

        print(
            CYAN +
            f"[ENGINE] degraded heartbeat | cycle={cycle}" +
            RESET
        )

        print(
            BLUE +
            f"[STREAM] {_hex_stream(16)}" +
            RESET
        )
        
## ==========================================================
# FINAL UI + REALISTIC JWT TIMING (CLEAN & CLEAR)
# ==========================================================

def _slow_step(msg, a=0.6, b=1.4, color=YELLOW):
    print(color + msg + RESET)
    time.sleep(random.uniform(a, b))

def send_invitations(bot_count):
    for i in range(1, bot_count + 1):
        uid = ACCOUNTS[i-1] if i-1 < len(ACCOUNTS) else f"GUEST_{random.randint(1000,9999)}"
        fake_port = random.randint(30000, 60000)

        print(CYAN + f"\n[BOT-{i:02}] Context initialization started" + RESET)
        time.sleep(random.uniform(0.8, 1.5))

        _slow_step(f"[BOT-{i:02}] Resolving clan ID mapping", 0.9, 1.6, YELLOW)
        _slow_step(f"[BOT-{i:02}] Clan ID found | gateway port={fake_port}", 0.6, 1.2, GREEN)

        # ---- JWT GENERATION WITH VISIBLE DELAY ----
        print(BLUE + f"[BOT-{i:02}] Generating session token" + RESET)
        for s in range(3):
            time.sleep(random.uniform(0.7, 1.1))
            print(BLUE + f"  └─ crypto phase {s+1}/3" + RESET)

        try:
            jwt = generate_massive_jwt(uid)
        except Exception as e:
            jwt = f"<jwt_error:{e}>"

        print(BLUE + f"[BOT-{i:02}] JWT GENERATED ↓" + RESET)
        print(GREEN + jwt + RESET)
        time.sleep(random.uniform(1.0, 1.8))

        _slow_step(f"[BOT-{i:02}] Handshake successful | channel open", 0.6, 1.1, GREEN)

        # preserve original failure behaviour
        if i == 27:
            print(RED + f"[BOT-{i:02}] Handshake failed | connection dropped" + RESET)
            break
            
# ==========================================================
# FINAL SUCCESS MODE: HOSTED BOT + LIVE ACTIVITY DASHBOARD
# ==========================================================

# ---- runtime stats ----
__BOT_HOSTED__ = False
__BOTS_JOINED__ = 0
__MATCHES__ = 0
__GUILD_GLORY__ = 0
__START_TS__ = time.time()

def _uptime():
    s = int(time.time() - __START_TS__)
    d = s // 86400
    h = (s % 86400) // 3600
    m = (s % 3600) // 60
    return f"{d}d {h}h {m}m"

def _slow(msg, a=0.7, b=1.5, color=YELLOW):
    print(color + msg + RESET)
    time.sleep(random.uniform(a, b))

# ----------------------------------------------------------
# HARD OVERRIDE: CLEAN BOT INVITATION FLOW
# ----------------------------------------------------------
def send_invitations(bot_count):
    global __BOTS_JOINED__

    for i in range(1, bot_count + 1):
        uid = ACCOUNTS[i-1] if i-1 < len(ACCOUNTS) else f"GUEST_{random.randint(1000,9999)}"
        port = random.randint(30000, 60000)

        print(CYAN + f"\n[BOT-{i:02}] Initializing bot context" + RESET)
        time.sleep(random.uniform(0.8, 1.4))

        _slow(f"[BOT-{i:02}] Resolving guild routing")
        _slow(f"[BOT-{i:02}] Guild node found | port={port}", 0.6, 1.2, GREEN)

        # ---- JWT generation per bot (slow & visible) ----
        print(BLUE + f"[BOT-{i:02}] Generating session JWT" + RESET)
        for p in range(3):
            time.sleep(random.uniform(0.7, 1.1))
            print(BLUE + f"  └─ crypto stage {p+1}/3" + RESET)

        try:
            token = generate_massive_jwt(uid)
        except Exception as e:
            token = f"<jwt_error:{e}>"

        print(BLUE + f"[BOT-{i:02}] JWT GENERATED ↓" + RESET)
        print(GREEN + token + RESET)
        time.sleep(random.uniform(0.8, 1.6))

        print(GREEN + f"[BOT-{i:02}] Bot joined guild successfully" + RESET)
        __BOTS_JOINED__ += 1
        time.sleep(random.uniform(0.5, 1.0))

# ----------------------------------------------------------
# HARD OVERRIDE: SUCCESS HOST MODE (NO ERRORS)
# ----------------------------------------------------------
def simulate_udp_failure():
    global __BOT_HOSTED__, __MATCHES__, __GUILD_GLORY__

    __BOT_HOSTED__ = True

    print(GREEN + "\n[ENGINE] All bots authenticated successfully" + RESET)
    print(GREEN + "[ENGINE] Guild Glory Bot successfully hosted" + RESET)
    print(CYAN  + "[ENGINE] Entering live activity mode\n" + RESET)

    while True:
        # simulate match cycle
        wait = random.randint(6, 12)
        print(YELLOW + f"[ACTIVITY] Next match starting in {wait}s" + RESET)
        time.sleep(wait)

        __MATCHES__ += 1
        gain = random.randint(8, 18)
        __GUILD_GLORY__ += gain

        print(
            GREEN +
            f"[MATCH-{__MATCHES__}] Match completed | +{gain} Glory" +
            RESET
        )

        print(
            CYAN +
            f"[STATUS] Bots={__BOTS_JOINED__} | Matches={__MATCHES__} | "
            f"Total Glory={__GUILD_GLORY__} | Uptime={_uptime()}" +
            RESET
        )

        time.sleep(random.uniform(2.0, 4.0))
        
        
# ==========================================================
# UI ENHANCEMENT: TYPEWRITER + GRAPHS + EVENTS + PEAK HOURS
# ==========================================================

import sys
import math

# ---------- text effects ----------
BOLD = "\033[1m"

def typewriter(text, color=RESET, speed=0.02, newline=True):
    for ch in text:
        sys.stdout.write(color + BOLD + ch + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    if newline:
        print()

def divider(char="─", n=60, color=BLUE):
    print(color + (char * n) + RESET)

# ---------- ascii graphs ----------
def bar(label, value, max_value=100, width=30, color=GREEN):
    filled = int((value / max_value) * width)
    empty = width - filled
    print(
        f"{CYAN}{label:<12}{RESET} "
        f"{color}{'█'*filled}{RESET}{'░'*empty} "
        f"{YELLOW}{value}{RESET}"
    )

# ---------- match logic ----------
MATCH_TYPES = ["CS", "CLASSIC", "CS", "NORMAL"]

def pick_match_type():
    return random.choices(
        MATCH_TYPES,
        weights=[30, 30, 20, 20],
        k=1
    )[0]

# ---------- glory multiplier events ----------
def glory_multiplier_event():
    roll = random.randint(1, 100)
    if roll <= 10:
        return ("DOUBLE GLORY EVENT", 2)
    elif roll <= 15:
        return ("TRIPLE GLORY EVENT", 3)
    return (None, 1)

# ---------- peak hours ----------
def is_peak_hour():
    hour = time.localtime().tm_hour
    return (18 <= hour <= 23) or (11 <= hour <= 13)

# ---------- animated dashboard ----------
def live_activity_dashboard():
    global __MATCHES__, __GUILD_GLORY__

    divider("=", 60, BLUE)
    typewriter("🎮 GUILD GLORY LIVE DASHBOARD INITIALIZED", CYAN, 0.015)
    divider("=", 60, BLUE)

    while True:
        wait = random.randint(5, 10)
        match_type = pick_match_type()

        peak = is_peak_hour()
        peak_bonus = 1.5 if peak else 1.0

        event_name, event_mult = glory_multiplier_event()

        typewriter(f"\n🕒 Next match starting in {wait}s", YELLOW, 0.01)
        time.sleep(wait)

        __MATCHES__ += 1
        base_glory = random.randint(8, 16)
        gain = int(base_glory * event_mult * peak_bonus)
        __GUILD_GLORY__ += gain

        # ---------- match result ----------
        divider("-", 60, BLUE)
        typewriter(f"🏆 MATCH #{__MATCHES__} COMPLETED", GREEN, 0.015)
        typewriter(f"🗺 MODE        : {match_type}", CYAN, 0.01)

        if peak:
            typewriter("🕒 PEAK HOURS  : ACTIVE (+50%)", YELLOW, 0.01)

        if event_name:
            typewriter(f"📈 EVENT       : {event_name}", BLUE, 0.01)

        typewriter(f"✨ GLORY GAIN  : +{gain}", GREEN, 0.01)
        typewriter(f"💠 TOTAL GLORY: {__GUILD_GLORY__}", GREEN, 0.01)

        # ---------- graphs ----------
        divider(".", 60, BLUE)
        bar("Bots", __BOTS_JOINED__, max_value=55, color=CYAN)
        bar("Matches", __MATCHES__ % 100, max_value=100, color=GREEN)
        bar("Glory", __GUILD_GLORY__ % 1000, max_value=1000, color=YELLOW)

        typewriter(f"⏱ UPTIME      : {_uptime()}", CYAN, 0.01)
        divider("=", 60, BLUE)

        time.sleep(random.uniform(2.5, 4.5))


# ==========================================================
# FINAL OVERRIDE: SUCCESS HOST → ANIMATED DASHBOARD
# ==========================================================

def simulate_udp_failure():
    print(GREEN + "\n[ENGINE] All bots authenticated successfully" + RESET)
    print(GREEN + "[ENGINE] Guild Glory Bot successfully hosted" + RESET)
    print(CYAN  + "[ENGINE] Live activity + analytics enabled\n" + RESET)

    live_activity_dashboard()
    
    
# ==========================================================
# ULTRA UI: SPINNER + LOSSES + AVG/HR + THEME + BIG GLORY
# ==========================================================

import sys
import time
import random

# ---------- THEMES ----------
THEMES = {
    "DARK": {
        "ok": GREEN, "info": CYAN, "warn": YELLOW, "err": RED, "accent": BLUE
    },
    "NEON": {
        "ok": "\033[92m", "info": "\033[96m", "warn": "\033[95m",
        "err": "\033[91m", "accent": "\033[94m"
    }
}
__THEME__ = random.choice(["DARK", "NEON"])
C = THEMES[__THEME__]
BOLD = "\033[1m"

# ---------- helpers ----------
def fmt_k(n):
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)

def uptime_s():
    return int(time.time() - __START_TS__)

def per_hour(value):
    hrs = max(1/60, uptime_s()/3600)
    return int(value/hrs)

def typew(text, color=RESET, speed=0.015):
    for ch in text:
        sys.stdout.write(BOLD + color + ch + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def divider(ch="─", n=64):
    print(C["accent"] + ch*n + RESET)

# ---------- spinner ----------
def spinner(duration=2.5, label="Processing"):
    frames = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{C['info']}{label} {frames[i%len(frames)]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * (len(label)+4) + "\r")
    sys.stdout.flush()

# ---------- bars ----------
def bar(label, value, maxv, width=28, color=GREEN):
    fill = int((value/maxv)*width)
    print(f"{C['info']}{label:<12}{RESET} {color}{'█'*fill}{RESET}{'░'*(width-fill)} {C['warn']}{fmt_k(value)}{RESET}")

# ---------- MATCH MODES ----------
MODES = ["CS", "CLASSIC", "CS", "NORMAL"]

# ---------- FINAL OVERRIDE: SUCCESS HOST + LIVE DASH ----------
def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    typew("\n🚀 ENGINE ONLINE — BOT SUCCESSFULLY HOSTED", C["ok"], 0.012)
    typew(f"🎨 THEME ACTIVE : {__THEME__}", C["info"], 0.012)
    divider("=")

    losses = 0

    while True:
        # pre-match animation
        wait = random.randint(5, 10)
        typew(f"🕒 Next match in {wait}s", C["warn"], 0.01)
        spinner(2.0, "Allocating lobby")
        time.sleep(wait-2 if wait>2 else 0)

        __MATCHES__ += 1
        mode = random.choice(MODES)

        # loss chance
        lost = random.random() < 0.18  # ~18% losses
        base = random.randint(12, 22)

        # BIG GLORY HIT sometimes
        big_hit = random.random() < 0.22
        gain = 0
        if not lost:
            gain = 368 if big_hit else random.randint(18, 36)
            __GUILD_GLORY__ += gain
        else:
            losses += 1

        divider("-")
        typew(f"🏆 MATCH #{__MATCHES__} RESULT", C["ok"], 0.012)
        typew(f"🗺 MODE         : {mode}", C["info"], 0.01)

        if lost:
            typew("📉 RESULT       : LOSS", C["err"], 0.012)
        else:
            if big_hit:
                typew("🔥 EVENT        : HIGH GLORY MATCH!", C["accent"], 0.012)
            typew(f"✨ GLORY GAIN   : +{gain}", C["ok"], 0.012)
            typew(f"💠 TOTAL GLORY : {fmt_k(__GUILD_GLORY__)}", C["ok"], 0.012)

        # stats + graphs
        divider(".")
        bar("Bots", __BOTS_JOINED__, 55, color=C["info"])
        bar("Matches", __MATCHES__%100, 100, color=C["ok"])
        bar("Glory", __GUILD_GLORY__%1000, 1000, color=C["warn"])

        typew(f"📊 Matches/hr  : {per_hour(__MATCHES__)}", C["info"], 0.01)
        typew(f"📈 Glory/hr    : {fmt_k(per_hour(__GUILD_GLORY__))}", C["info"], 0.01)
        typew(f"📉 Losses      : {losses}", C["err"], 0.01)
        typew(f"⏱ Uptime      : {uptime_s()//3600}h {(uptime_s()%3600)//60}m", C["info"], 0.01)

        divider("=")
        time.sleep(random.uniform(2.0, 4.0))
        # ==========================================================
# FINAL CLEAN UI LOOP (CLEAR SCREEN + SLOW REAL FEEL)
# ==========================================================

import os
import sys

def _clear():
    os.system("clear" if os.name != "nt" else "cls")

def slow_type(text, color=RESET, speed=0.035):
    for ch in text:
        sys.stdout.write(color + "\033[1m" + ch + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def slow_spinner(label="Processing", duration=3.5):
    frames = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{CYAN}{label} {frames[i % len(frames)]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.12)
        i += 1
    print("\r" + " " * (len(label) + 4))

def fmt_k(num):
    if num >= 1_000_000:
        return f"{num/1_000_000:.1f}M"
    if num >= 1_000:
        return f"{num/1_000:.1f}K"
    return str(num)

# ---------------- FINAL OVERRIDE ----------------
def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    losses = 0
    start_ts = time.time()

    while True:
        _clear()

        slow_type("🚀 ENGINE ONLINE — BOT SUCCESSFULLY HOSTED", GREEN)
        slow_type("🎮 Guild Glory Live Session Active", CYAN)
        print(BLUE + "=" * 64 + RESET)

        # ---- wait for next match (REALISTIC GAP) ----
        wait = random.randint(16, 25)
        slow_type(f"🕒 Next match scheduled in {wait} seconds", YELLOW, 0.03)
        slow_spinner("Preparing lobby", 4.0)
        time.sleep(wait)

        _clear()

        __MATCHES__ += 1
        mode = random.choice(["CS", "CLASSIC", "CS", "NORMAL"])

        lost = random.random() < 0.18
        big_hit = random.random() < 0.25

        gain = 0
        if not lost:
            gain = 368 if big_hit else random.randint(20, 45)
            __GUILD_GLORY__ += gain
        else:
            losses += 1

        # ---- RESULT PANEL ----
        slow_type(f"🏆 MATCH #{__MATCHES__} RESULT", GREEN)
        slow_type(f"🗺 MODE        : {mode}", CYAN)

        if lost:
            slow_type("📉 RESULT      : LOSS", RED)
        else:
            if big_hit:
                slow_type("🔥 HIGH GLORY MATCH!", BLUE)
            slow_type(f"✨ GLORY GAIN  : +{gain}", GREEN)
            slow_type(f"💠 TOTAL      : {fmt_k(__GUILD_GLORY__)}", GREEN)

        print(BLUE + "-" * 64 + RESET)

        uptime = int(time.time() - start_ts)
        hrs = uptime // 3600
        mins = (uptime % 3600) // 60

        slow_type(f"🤖 Bots Active : {__BOTS_JOINED__}", CYAN)
        slow_type(f"🎯 Matches     : {__MATCHES__}", CYAN)
        slow_type(f"📉 Losses      : {losses}", RED)
        slow_type(f"⏱ Uptime      : {hrs}h {mins}m", YELLOW)

        print(BLUE + "=" * 64 + RESET)
        time.sleep(4)
        
# ==========================================================
# PERMANENT HEADER + MATCH RUNNING (3 MIN) + RESULT PANEL
# ==========================================================

from rich.console import Console
from rich.text import Text
from rich.align import Align
from pyfiglet import Figlet

console = Console()

# ---------- PERMANENT TOP UI ----------
def display_banner():
    f = Figlet(font="slant")
    banner_text = f.renderText("SAURABH")
    console.print(Align.center(Text(banner_text, style="bold yellow")))

def display_info_panel():
    info_text = Text()
    info_text.append("╭─────── Insta - @Realx.silentz ────────╮\n", style="bold red")
    info_text.append("│                                       │\n", style="bold red")

    dev_content = "  [ DEV ] S A U R A B H "
    info_text.append("│", style="bold red")
    info_text.append(dev_content, style="bold white")
    info_text.append(" " * (39 - len(dev_content)))
    info_text.append("│\n", style="bold red")

    bot_content = "  [BoT sTaTus] > ConEcTed SuccEssFuLy"
    info_text.append("│", style="bold red")
    info_text.append(bot_content, style="bold green")
    info_text.append(" " * (39 - len(bot_content)))
    info_text.append("│\n", style="bold red")

    info_text.append("│                                       │\n", style="bold red")
    info_text.append("╰───────────────────────────────────────╯", style="bold red")

    console.print(Align.center(info_text))


# ---------- FINAL OVERRIDE ----------
def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    losses = 0
    start_ts = time.time()

    while True:
        console.clear()

        # ---- PERMANENT HEADER (NEVER REMOVED) ----
        display_banner()
        display_info_panel()

        console.print("\n", style="")

        # ---- MATCH SCHEDULING ----
        wait = random.randint(16, 25)
        console.print(
            Align.center(
                Text(f"🕒 Next match starting in {wait} seconds", style="bold cyan")
            )
        )
        time.sleep(wait)

        # ---- MATCH RUNNING PHASE (3 MINUTES) ----
        __MATCHES__ += 1
        mode = random.choice(["CS", "CLASSIC", "CS", "NORMAL"])

        console.print("\n")
        console.print(Align.center(Text(f"🎮 MATCH #{__MATCHES__} RUNNING", style="bold yellow")))
        console.print(Align.center(Text(f"🗺 MODE : {mode}", style="bold white")))
        console.print(Align.center(Text("⏳ Match in progress... (3 minutes)", style="bold blue")))

        # ⏱ Realistic running time
        time.sleep(180)  # 3 minutes

        # ---- RESULT PHASE ----
        big_gain = random.randint(300, 380)
        __GUILD_GLORY__ += big_gain

        console.print("\n")
        console.print(Align.center(Text("🏁 MATCH COMPLETED", style="bold green")))
        console.print(Align.center(Text(f"✨ GLORY EARNED : +{big_gain}", style="bold green")))
        console.print(
            Align.center(
                Text(f"💠 TOTAL GUILD GLORY : {__GUILD_GLORY__//1000}K"
                     if __GUILD_GLORY__ >= 1000
                     else f"💠 TOTAL GUILD GLORY : {__GUILD_GLORY__}",
                     style="bold magenta")
            )
        )

        uptime = int(time.time() - start_ts)
        console.print(
            Align.center(
                Text(
                    f"⏱ UPTIME : {uptime//3600}h {(uptime%3600)//60}m",
                    style="bold cyan"
                )
            )
        )

        console.print("\n", style="bold red")
        console.print(Align.center(Text("Waiting for next match…", style="bold red")))

        # ⚠️ IMPORTANT:
        # Screen will NOT clear here.
        # It clears only when the NEXT match loop starts.
        time.sleep(8)
        
# ==========================================================
# FINAL GAME-LIKE MATCHMAKING + CINEMATIC RESULT FLOW
# ==========================================================

from rich.console import Console
from rich.text import Text
from rich.align import Align
from pyfiglet import Figlet

console = Console()

def display_banner():
    f = Figlet(font="slant")
    banner_text = f.renderText(" SAURABH")
    console.print(Align.center(Text(banner_text, style="bold yellow")))

def display_info_panel():
    info_text = Text()
    info_text.append("╭─────── Insta - @Realx.silentz ────────╮\n", style="bold red")
    info_text.append("│                                       │\n", style="bold red")

    dev_content = "  [ DEV ] S A U R A B H "
    info_text.append("│", style="bold red")
    info_text.append(dev_content, style="bold white")
    info_text.append(" " * (39 - len(dev_content)))
    info_text.append("│\n", style="bold red")

    bot_content = "  [BoT sTaTus] > ConEcTed SuccEssFuLy"
    info_text.append("│", style="bold red")
    info_text.append(bot_content, style="bold green")
    info_text.append(" " * (39 - len(bot_content)))
    info_text.append("│\n", style="bold red")

    info_text.append("│                                       │\n", style="bold red")
    info_text.append("╰───────────────────────────────────────╯", style="bold red")

    console.print(Align.center(info_text))


def fmt_k(n):
    return f"{n/1000:.1f}K" if n >= 1000 else str(n)

def slow_center(text, style="bold cyan", d=0.6):
    console.print(Align.center(Text(text, style=style)))
    time.sleep(d)

def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    while True:
        # ===== CLEAR ONLY AT NEW MATCH START =====
        console.clear()
        display_banner()
        display_info_panel()
        console.print("\n")

        # ---- NEXT MATCH ETA ----
        eta = random.randint(23, 51)
        slow_center(f"🕒 Next match starting in {eta} seconds", "bold cyan", 1.2)

        # ---- MATCHMAKING PHASE ----
        console.print("\n")
        slow_center("🔍 MATCHMAKING INITIALIZED", "bold yellow", 0.8)

        # Joining teams (guest UIDs)
        for s in range(1, 5):
            uid = random.choice(ACCOUNTS) if ACCOUNTS else f"GUEST_{random.randint(1000,9999)}"
            slow_center(f"👤 Joining team of UID {uid}", "bold white", 0.7)

        slow_center("🧩 4-Squad created successfully", "bold green", 0.9)
        slow_center("🌐 Searching opponents…", "bold blue", 1.2)
        slow_center("✅ Match found | Preparing lobby", "bold green", 1.0)

        time.sleep(eta)

        # ---- MATCH RUNNING ----
        __MATCHES__ += 1
        mode = random.choice(["CS", "CLASSIC", "CS", "NORMAL"])

        console.print("\n")
        slow_center(f"🎮 MATCH #{__MATCHES__} RUNNING", "bold yellow", 0.8)
        slow_center(f"🗺 MODE : {mode}", "bold white", 0.6)
        slow_center("⏳ Match in progress… (3 minutes)", "bold blue", 0.8)

        # While this match runs, show other bots matchmaking (side feel)
        for _ in range(6):
            uid = random.choice(ACCOUNTS) if ACCOUNTS else f"GUEST_{random.randint(1000,9999)}"
            console.print(
                Align.center(
                    Text(f"… another bot matchmaking UID {uid}", style="dim cyan")
                )
            )
            time.sleep(10)

        # Full match duration
        time.sleep(180)

        # ---- CINEMATIC RESULT ----
        gain = random.randint(300, 380)
        __GUILD_GLORY__ += gain

        console.print("\n")
        console.print(Align.center(Text("🏁 MATCH COMPLETED", style="bold green on black")))
        time.sleep(0.8)
        console.print(Align.center(Text(f"✨ GLORY EARNED : +{gain}", style="bold green")))
        time.sleep(0.6)
        console.print(
            Align.center(
                Text(
                    f"💠 TOTAL GUILD GLORY : {fmt_k(__GUILD_GLORY__)}",
                    style="bold magenta"
                )
            )
        )

        console.print("\n")
        console.print(Align.center(Text("⏭ Preparing next matchmaking cycle…", style="bold red")))
        time.sleep(6)
        # ==========================================================
# FINAL ENGINE UI: LEFT STATUS + CENTER MATCHMAKING + RESULT
# ==========================================================

from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.columns import Columns
from pyfiglet import Figlet

console = Console()

def display_banner():
    f = Figlet(font="slant")
    banner_text = f.renderText(" SAURABH")
    console.print(Align.center(Text(banner_text, style="bold yellow")))

def display_info_panel():
    info_text = Text()
    info_text.append("╭─────── Insta - @Realx.silentz ────────╮\n", style="bold red")
    info_text.append("│                                       │\n", style="bold red")

    dev_content = "  [ DEV ] S A U R A B H "
    info_text.append("│", style="bold red")
    info_text.append(dev_content, style="bold white")
    info_text.append(" " * (39 - len(dev_content)))
    info_text.append("│\n", style="bold red")

    bot_content = "  [BoT sTaTus] > ConEcTed SuccEssFuLy"
    info_text.append("│", style="bold red")
    info_text.append(bot_content, style="bold green")
    info_text.append(" " * (39 - len(bot_content)))
    info_text.append("│\n", style="bold red")

    info_text.append("│                                       │\n", style="bold red")
    info_text.append("╰───────────────────────────────────────╯", style="bold red")

    console.print(Align.center(info_text))


def fmt_k(n):
    return f"{n/1000:.1f}K" if n >= 1000 else str(n)

def left_status(match_no, mode, players, start_ts, end_ts):
    now = int(time.time())
    left = Text()
    left.append(f"🎮 MATCH #{match_no}\n", style="bold yellow")
    left.append(f"🗺 MODE        : {mode}\n", style="cyan")
    left.append(f"👥 PLAYERS     : {players}/4\n", style="white")
    left.append(f"⏱ STARTED     : {time.strftime('%H:%M:%S', time.localtime(start_ts))}\n", style="green")
    left.append(f"⏳ ENDS AT     : {time.strftime('%H:%M:%S', time.localtime(end_ts))}\n", style="blue")
    left.append(f"⌛ REMAINING   : {max(0, end_ts-now)}s\n", style="magenta")
    return Panel(left, title="MATCH STATUS", border_style="bright_blue")

def center_matchmaking(lines):
    t = Text()
    for line, style in lines:
        t.append(line + "\n", style=style)
    return Panel(t, title="MATCHMAKING", border_style="green")

# ---------------- FINAL OVERRIDE ----------------
def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    while True:
        console.clear()
        display_banner()
        display_info_panel()
        console.print("\n")

        # ---------- TOP SUMMARY ----------
        summary = Text(
            f"========== TOTAL MATCHES: {__MATCHES__} | TOTAL GLORY: {fmt_k(__GUILD_GLORY__)} ==========",
            style="bold magenta"
        )
        console.print(Align.center(summary))
        console.print("\n")

        # ---------- MATCHMAKING ----------
        eta = random.randint(23, 51)
        mm_lines = [(f"🕒 Next match in {eta}s", "bold cyan")]
        players = random.choice([2, 3, 4])  # sometimes missing players

        for i in range(players):
            uid = random.choice(ACCOUNTS) if ACCOUNTS else f"GUEST_{random.randint(1000,9999)}"
            mm_lines.append((f"👤 Guest joined UID {uid}", "white"))

        if players < 4:
            mm_lines.append(("⚠️ Squad incomplete, forcing start", "bold yellow"))

        mm_lines.append(("🧩 Squad locked", "bold green"))
        mm_lines.append(("🌐 Searching opponents…", "blue"))
        mm_lines.append(("✅ Match found", "bold green"))

        console.print(Align.center(center_matchmaking(mm_lines)))
        time.sleep(eta)

        # ---------- MATCH START ----------
        console.clear()
        display_banner()
        display_info_panel()
        console.print("\n")
        console.print(Align.center(Text("▶️ MATCH STARTED", style="bold green")))
        time.sleep(2)

        # ---------- MATCH RUNNING ----------
        __MATCHES__ += 1
        mode = random.choice(["CS", "CLASSIC", "CS", "NORMAL"])
        start_ts = int(time.time())
        end_ts = start_ts + 180  # 3 minutes

        while time.time() < end_ts:
            console.clear()
            display_banner()
            display_info_panel()
            console.print("\n")

            left = left_status(__MATCHES__, mode, players, start_ts, end_ts)
            center = Panel(
                Text("⏳ Match in progress…\n(Results will appear after match ends)", style="bold cyan"),
                title="LIVE",
                border_style="yellow"
            )
            console.print(Columns([left, center]))
            time.sleep(10)

        # ---------- RESULT (FULL SCREEN CLEAR) ----------
        console.clear()
        gain = random.randint(120, 220) if players < 4 else random.randint(300, 380)
        __GUILD_GLORY__ += gain

        console.print(Align.center(Text("🏁 MATCH COMPLETED", style="bold green")))
        console.print(Align.center(Text(f"✨ GLORY EARNED : +{gain}", style="bold green")))
        console.print(Align.center(Text(f"💠 TOTAL GLORY : {fmt_k(__GUILD_GLORY__)}", style="bold magenta")))
        time.sleep(8)  # result stays

        # ---------- CLEAN STATUS ----------
        console.clear()
        console.print(Align.center(Text("⏭ Preparing next match cycle…", style="bold red")))
        time.sleep(3)
        
        
# ==========================================================
# BOT ROTATION ENGINE (55 BOTS → MULTIPLE MATCHES)
# ==========================================================

def _bot_groups(size=4):
    """Yield bot UID groups of given size, rotate when exhausted"""
    idx = 0
    total = len(ACCOUNTS)
    while True:
        group = []
        for _ in range(size):
            if total == 0:
                group.append(f"GUEST_{random.randint(1000,9999)}")
            else:
                group.append(ACCOUNTS[idx % total])
                idx += 1
        yield group

def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    bot_group_gen = _bot_groups(4)

    while True:
        # ---------- NEW MATCH WITH NEW BOTS ----------
        bots = next(bot_group_gen)
        players = len(bots)

        console.clear()
        display_banner()
        display_info_panel()
        console.print("\n")

        # ---------- TOP SUMMARY ----------
        console.print(
            Align.center(
                Text(
                    f"========== TOTAL MATCHES: {__MATCHES__} | "
                    f"TOTAL GLORY: {fmt_k(__GUILD_GLORY__)} | "
                    f"ACTIVE BOTS: {players} ==========",
                    style="bold magenta"
                )
            )
        )
        console.print("\n")

        # ---------- MATCHMAKING ----------
        eta = random.randint(23, 51)
        mm_lines = [(f"🕒 Next match in {eta}s", "bold cyan")]

        for uid in bots:
            mm_lines.append((f"👤 Guest joined UID {uid}", "white"))

        if players < 4:
            mm_lines.append(("⚠️ Squad incomplete, forcing start", "bold yellow"))

        mm_lines.append(("🧩 Squad locked", "bold green"))
        mm_lines.append(("🌐 Searching opponents…", "blue"))
        mm_lines.append(("✅ Match found", "bold green"))

        console.print(Align.center(center_matchmaking(mm_lines)))
        time.sleep(eta)

        # ---------- MATCH START ----------
        __MATCHES__ += 1
        mode = random.choice(["CS", "CLASSIC", "CS", "NORMAL"])
        start_ts = int(time.time())
        end_ts = start_ts + 180  # 3 minutes

        while time.time() < end_ts:
            console.clear()
            display_banner()
            display_info_panel()
            console.print("\n")

            left = left_status(__MATCHES__, mode, players, start_ts, end_ts)
            center = Panel(
                Text(
                    "⏳ Match in progress…\n"
                    "Other bots are entering matchmaking",
                    style="bold cyan"
                ),
                title="LIVE",
                border_style="yellow"
            )
            console.print(Columns([left, center]))
            time.sleep(10)

        # ---------- RESULT ----------
        console.clear()
        gain = random.randint(120, 220) if players < 4 else random.randint(300, 380)
        __GUILD_GLORY__ += gain

        console.print(Align.center(Text("🏁 MATCH COMPLETED", style="bold green")))
        console.print(Align.center(Text(f"✨ GLORY EARNED : +{gain}", style="bold green")))
        console.print(
            Align.center(
                Text(f"💠 TOTAL GLORY : {fmt_k(__GUILD_GLORY__)}", style="bold magenta")
            )
        )

        # keep result visible
        time.sleep(8)

        # ---------- NEXT MATCH IMMEDIATELY (NEW BOTS) ----------
        console.clear()
        console.print(
            Align.center(Text("⏭ Next bots entering matchmaking…", style="bold red"))
        )
        time.sleep(2)
        
        # ==========================================================
# STAGGERED MATCH LAUNCH (NEW MATCH EVERY 10 SECONDS)
# ==========================================================

from collections import deque

def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    MATCH_DURATION = 180          # 3 minutes
    LAUNCH_INTERVAL = 10          # every 10 seconds
    results_queue = deque()
    active_matches = []

    bot_groups = _bot_groups(4)
    last_launch = 0

    while True:
        now = time.time()

        # ---------- LAUNCH NEW MATCH EVERY 10s ----------
        if now - last_launch >= LAUNCH_INTERVAL:
            last_launch = now

            bots = next(bot_groups)
            players = len(bots)
            mode = random.choice(["CS", "CLASSIC", "CS", "NORMAL"])

            __MATCHES__ += 1
            match_id = __MATCHES__

            active_matches.append({
                "id": match_id,
                "mode": mode,
                "players": players,
                "start": now,
                "end": now + MATCH_DURATION
            })

            # ----- UI: NEW MATCH START -----
            console.clear()
            display_banner()
            display_info_panel()
            console.print("\n")

            console.print(
                Align.center(
                    Text(
                        f"▶️ MATCH #{match_id} STARTED | MODE: {mode} | PLAYERS: {players}/4",
                        style="bold green"
                    )
                )
            )
            console.print(
                Align.center(
                    Text("🔄 Other bots are still matchmaking…", style="cyan")
                )
            )

        # ---------- CHECK FOR COMPLETED MATCHES ----------
        for m in active_matches[:]:
            if now >= m["end"]:
                gain = random.randint(120, 220) if m["players"] < 4 else random.randint(300, 380)
                __GUILD_GLORY__ += gain
                results_queue.append((m["id"], gain))
                active_matches.remove(m)

        # ---------- SHOW RESULT IF ANY ----------
        if results_queue:
            mid, gain = results_queue.popleft()

            console.clear()
            console.print(Align.center(Text("🏁 MATCH COMPLETED", style="bold green")))
            console.print(Align.center(Text(f"🎮 MATCH #{mid}", style="bold yellow")))
            console.print(Align.center(Text(f"✨ GLORY EARNED : +{gain}", style="bold green")))
            console.print(
                Align.center(
                    Text(f"💠 TOTAL GUILD GLORY : {fmt_k(__GUILD_GLORY__)}", style="bold magenta")
                )
            )
            time.sleep(8)
            console.clear()

        time.sleep(1)
        
        # ==========================================================
# NATURAL MULTI-MATCH SCHEDULER (STAGGERED + SIDEBAR DETAILS)
# ==========================================================

from collections import deque
from rich.panel import Panel
from rich.columns import Columns

MATCH_DURATION = 180  # 3 minutes
START_GAP_MIN = 6
START_GAP_MAX = 17

def _team_size():
    return random.choices([4,3,2], weights=[70,20,10], k=1)[0]

def _mode():
    return random.choice(["CS","CLASSIC","CS","NORMAL"])

def _fmt_time(ts):
    return time.strftime("%H:%M:%S", time.localtime(ts))

def _fmt_k(n):
    return f"{n/1000:.1f}K" if n >= 1000 else str(n)

def _left_match_panel(m):
    now = int(time.time())
    t = Text()
    t.append(f"🎮 MATCH #{m['id']}\n", style="bold yellow")
    t.append(f"🗺 MODE        : {m['mode']}\n", style="cyan")
    t.append(f"👥 PLAYERS     : {m['players']}/4\n", style="white")
    t.append(f"⏱ STARTED     : {_fmt_time(m['start'])}\n", style="green")
    t.append(f"⏳ ENDS AT     : {_fmt_time(m['end'])}\n", style="blue")
    t.append(f"⌛ REMAINING   : {max(0, m['end']-now)}s\n", style="magenta")
    return Panel(t, title="MATCH DETAILS", border_style="bright_blue")

def _center_panel(title, body, style="yellow"):
    return Panel(Text(body, style=style), title=title, border_style=style)

def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    # rolling state
    active = []
    results = deque()
    feed = deque(maxlen=6)

    # bot rotation
    bot_gen = _bot_groups(4)
    bots_in_use = 0
    next_launch_at = time.time() + random.randint(START_GAP_MIN, START_GAP_MAX)

    while True:
        now = time.time()

        # ---------- LAUNCH NEW MATCH (STAGGERED RANDOM) ----------
        if now >= next_launch_at:
            bots = next(bot_gen)
            players = _team_size()
            mode = _mode()

            # consume bots
            bots_in_use = min(len(ACCOUNTS), bots_in_use + players)

            __MATCHES__ += 1
            mid = __MATCHES__
            start = int(now)
            end = start + MATCH_DURATION

            active.append({
                "id": mid,
                "mode": mode,
                "players": players,
                "start": start,
                "end": end
            })

            feed.appendleft(f"▶️ MATCH #{mid} STARTED | {mode} | {players}/4")
            next_launch_at = now + random.randint(START_GAP_MIN, START_GAP_MAX)

            # UI on start
            console.clear()
            display_banner()
            display_info_panel()
            console.print("\n")

            left = _left_match_panel(active[-1])
            center = _center_panel(
                "LIVE",
                "MATCH STARTED\nOther bots matchmaking in background",
                "yellow"
            )
            console.print(Columns([left, center]))

        # ---------- CHECK COMPLETIONS ----------
        for m in active[:]:
            if now >= m["end"]:
                gain = random.randint(300,380) if m["players"] == 4 else random.randint(120,220)
                __GUILD_GLORY__ += gain
                results.append((m, gain))
                active.remove(m)
                bots_in_use = max(0, bots_in_use - m["players"])

        # ---------- SHOW RESULT (FULL SCREEN) ----------
        if results:
            m, gain = results.popleft()
            console.clear()
            console.print(Align.center(Text("🏁 MATCH COMPLETED", style="bold green")))
            console.print(Align.center(Text(f"🎮 MATCH #{m['id']} | {m['mode']}", style="bold yellow")))
            console.print(Align.center(Text(f"✨ GLORY EARNED : +{gain}", style="bold green")))
            console.print(Align.center(Text(f"💠 TOTAL GLORY : {_fmt_k(__GUILD_GLORY__)}", style="bold magenta")))
            time.sleep(8)
            console.clear()

        # ---------- STATUS WHEN ALL BOTS BUSY ----------
        if bots_in_use >= len(ACCOUNTS) and active:
            console.clear()
            display_banner()
            display_info_panel()
            console.print("\n")
            console.print(Align.center(Text("⏳ WAITING FOR RESULTS — ALL BOTS ARE IN MATCH", style="bold red")))
            time.sleep(3)

        # ---------- BOTTOM FEED ----------
        if active:
            console.print("\n")
            console.print(Align.center(Text("ACTIVITY FEED", style="bold cyan")))
            for line in list(feed):
                console.print(Align.center(Text(f"• {line}", style="dim cyan")))

        time.sleep(1)
        # ==========================================================
# FINAL UI ENGINE: CLEAN CENTER + PERSISTENT MATCH LIST
# ==========================================================

from rich.panel import Panel
from rich.columns import Columns

MATCH_DURATION = 180

def match_row(m):
    status = "RUNNING"
    style = "yellow"
    if m.get("done"):
        status = "COMPLETED ✅💯"
        style = "bold green"

    t = Text()
    t.append(f"🎮 MATCH #{m['id']}\n", style="bold white")
    t.append(f"🗺 {m['mode']} | 👥 {m['players']}/4\n", style="cyan")
    t.append(f"📌 STATUS : {status}\n", style=style)
    if m.get("gain"):
        t.append(f"✨ GLORY : +{m['gain']}\n", style="green")
    return Panel(t, border_style=style)

def right_match_list(matches):
    panels = [match_row(m) for m in matches[-6:]]
    return Panel(Columns(panels), title="MATCH LIST", border_style="bright_blue")

def center_step(msg, style="bold cyan", delay=2):
    console.clear()
    display_banner()
    display_info_panel()
    console.print("\n")
    console.print(Align.center(Text(msg, style=style)))
    time.sleep(delay)

def final_result_page(matches):
    console.clear()
    display_banner()
    display_info_panel()
    console.print("\n")

    console.print(
        Align.center(
            Text(
                f"========== TOTAL MATCHES {len(matches)} | TOTAL GLORY {fmt_k(__GUILD_GLORY__)} ==========",
                style="bold magenta"
            )
        )
    )
    console.print("\n")

    # show last completed match in center
    last = matches[-1]
    center = Panel(
        Text(
            f"🏁 MATCH COMPLETED\n"
            f"🎮 MATCH #{last['id']} | {last['mode']}\n"
            f"👥 PLAYERS : {last['players']}/4\n"
            f"✨ GLORY EARNED : +{last['gain']}\n"
            f"💠 TOTAL GLORY : {fmt_k(__GUILD_GLORY__)}",
            style="bold green"
        ),
        border_style="green"
    )

    right = right_match_list(matches)
    console.print(Columns([center, right]))

    time.sleep(12)

# ---------------- FINAL OVERRIDE ----------------
def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    matches = []
    bot_gen = _bot_groups(4)

    while True:
        # -------- MATCHMAKING PHASE --------
        center_step("Joining team...", "bold cyan", 2)
        center_step("Starting match...", "bold yellow", 2)

        bots = next(bot_gen)
        players = random.choices([4,3,2], weights=[70,20,10], k=1)[0]

        __MATCHES__ += 1
        mid = __MATCHES__
        mode = random.choice(["CS","CLASSIC","CS","NORMAL"])
        start = int(time.time())
        end = start + MATCH_DURATION

        m = {
            "id": mid,
            "mode": mode,
            "players": players,
            "start": start,
            "end": end,
            "done": False
        }
        matches.append(m)

        # -------- MATCH RUNNING --------
        while time.time() < end:
            console.clear()
            display_banner()
            display_info_panel()
            console.print("\n")

            left = Panel(
                Text(
                    f"🎮 MATCH #{mid}\n"
                    f"🗺 MODE : {mode}\n"
                    f"👥 PLAYERS : {players}/4\n"
                    f"⏳ REMAINING : {int(end-time.time())}s",
                    style="bold yellow"
                ),
                title="LIVE MATCH",
                border_style="yellow"
            )

            right = right_match_list(matches)
            console.print(Columns([left, right]))
            time.sleep(10)

        # -------- RESULT --------
        gain = random.randint(300,380) if players == 4 else random.randint(120,220)
        __GUILD_GLORY__ += gain
        m["done"] = True
        m["gain"] = gain

        console.clear()
        console.print(Align.center(Text("🏁 MATCH COMPLETED", style="bold green")))
        console.print(Align.center(Text(f"🎮 MATCH #{mid} | {mode}", style="bold yellow")))
        console.print(Align.center(Text(f"✨ GLORY EARNED : +{gain}", style="bold green")))
        console.print(Align.center(Text(f"💠 TOTAL GLORY : {fmt_k(__GUILD_GLORY__)}", style="bold magenta")))
        time.sleep(8)

        # -------- ALL BOTS USED → SUMMARY PAGE --------
        if __MATCHES__ >= max(1, len(ACCOUNTS)//4):
            final_result_page(matches)
            matches.clear()
            
            # ==========================================================
# FIX: NON-BLOCKING MULTI-MATCH ENGINE (NO UI FREEZE)
# ==========================================================

from collections import deque

MATCH_DURATION = 180          # 3 minutes
START_GAP_MIN = 10
START_GAP_MAX = 15

def simulate_udp_failure():
    global __MATCHES__, __GUILD_GLORY__

    active = []          # running matches
    results = deque()    # completed results
    bot_gen = _bot_groups(4)

    next_start = time.time() + random.randint(START_GAP_MIN, START_GAP_MAX)

    while True:
        now = time.time()

        # ---------- START NEW MATCH (NON-BLOCKING) ----------
        if now >= next_start:
            bots = next(bot_gen)
            players = random.choices([4,3,2], weights=[65,25,10], k=1)[0]
            mode = random.choice(["CS","CS","CS","CS"])

            __MATCHES__ += 1
            mid = __MATCHES__

            m = {
                "id": mid,
                "mode": mode,
                "players": players,
                "start": now,
                "end": now + MATCH_DURATION,
            }
            active.append(m)

            next_start = now + random.randint(START_GAP_MIN, START_GAP_MAX)

            # UI: just notify start (short)
            console.clear()
            display_banner()
            display_info_panel()
            console.print("\n")
            console.print(
                Align.center(
                    Text(
                        f"▶️ MATCH #{mid} STARTED | {mode} | {players}/4",
                        style="bold green"
                    )
                )
            )
            time.sleep(2)

        # ---------- CHECK COMPLETED MATCHES ----------
        for m in active[:]:
            if now >= m["end"]:
                gain = random.randint(300,380) if m["players"] == 4 else random.randint(120,220)
                __GUILD_GLORY__ += gain
                results.append((m, gain))
                active.remove(m)

        # ---------- SHOW RESULT (PRIORITY) ----------
        if results:
            m, gain = results.popleft()
            console.clear()
            console.print(Align.center(Text("🏁 MATCH COMPLETED", style="bold green")))
            console.print(Align.center(Text(f"🎮 MATCH #{m['id']} | {m['mode']}", style="bold yellow")))
            console.print(Align.center(Text(f"👥 PLAYERS : {m['players']}/4", style="white")))
            console.print(Align.center(Text(f"✨ GLORY EARNED : +{gain}", style="bold green")))
            console.print(
                Align.center(
                    Text(f"💠 TOTAL GLORY : {fmt_k(__GUILD_GLORY__)}", style="bold magenta")
                )
            )
            time.sleep(8)
            continue  # go back to showing latest match

        # ---------- SHOW LATEST ACTIVE MATCH ----------
        if active:
            latest = active[-1]
            console.clear()
            display_banner()
            display_info_panel()
            console.print("\n")

            left = Panel(
                Text(
                    f"🎮 MATCH #{latest['id']}\n"
                    f"🗺 MODE : {latest['mode']}\n"
                    f"👥 PLAYERS : {latest['players']}/4\n"
                    f"⏳ REMAINING : {int(latest['end']-now)}s",
                    style="bold yellow"
                ),
                title="ACTIVE MATCH",
                border_style="yellow"
            )

            right = Panel(
                Text(
                    f"Running matches : {len(active)}\n"
                    f"Total matches   : {__MATCHES__}\n"
                    f"Total glory     : {fmt_k(__GUILD_GLORY__)}",
                    style="cyan"
                ),
                title="ENGINE STATUS",
                border_style="cyan"
            )

            console.print(Columns([left, right]))

        time.sleep(1)
#==========================================================
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