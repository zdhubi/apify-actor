from datetime import datetime

def write_log(count):
    timestamp = datetime.utcnow().isoformat()
    with open("count.log", "a") as f:
        f.write(f"{timestamp} – {count} products processed\n")
