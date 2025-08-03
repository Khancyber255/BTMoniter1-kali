import bluetooth

print("[*] Scanning for Bluetooth devices nearby...")

devices = bluetooth.discover_devices(duration=8, lookup_names=True)

if devices:
    print(f"[+] Found {len(devices)} device(s):")
    for addr, name in devices:
        print(f" - {name} [{addr}]")
else:
    print("[-] No Bluetooth devices found.")
