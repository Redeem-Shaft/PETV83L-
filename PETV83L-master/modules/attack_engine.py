import threading
import time
from faker import Faker
fake = Faker()

def start_attack(mode, logger):
    def run():
        logger.log(f"[bold red]> Starting {mode.upper()} attack...[/bold red]")
        for _ in range(10):
            if mode == "rogue":
                logger.log(f"New device connected: {fake.mac_address()} ({fake.ipv4()})")
            elif mode == "deauth":
                logger.log(f"Deauth sent to: {fake.mac_address()}")
            elif mode == "crack":
                logger.log(f"Trying password: {fake.password()} -> [italic]failed[/italic]")
            time.sleep(0.8)
        logger.log(f"[bold green]> {mode.upper()} simulation completed.[/bold green]")

    threading.Thread(target=run).start()
