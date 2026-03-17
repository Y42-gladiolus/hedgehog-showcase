#!/usr/bin/env python3
"""🦔 LogGuard — Монитор целостности логов"""
import hashlib, sqlite3, json, time
from pathlib import Path
from datetime import datetime

CONFIG = Path("config.json")
DB = Path("audit.db")
WATCH = Path("logs")

def load_config():
    if CONFIG.exists(): return json.load(open(CONFIG))
    return {"интервал_сек": 300, "email": "admin@example.com", "папка": "logs/"}

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): h.update(chunk)
    return h.hexdigest()

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS proofs (file TEXT, hash TEXT, time TEXT, status TEXT)")
    conn.commit()
    return conn

def main():
    cfg = load_config()
    db = init_db()
    WATCH.mkdir(exist_ok=True)
    print("🦔 LogGuard запущен")
    while True:
        for f in WATCH.glob("*.log"):
            h = hash_file(f)
            t = datetime.now().isoformat()
            db.execute("INSERT INTO proofs VALUES (?,?,?,?)", (str(f), h, t, "OK"))
            db.commit()
            print(f"✓ {f.name}: OK")
        time.sleep(cfg["интервал_сек"])

if __name__ == "__main__": main()
