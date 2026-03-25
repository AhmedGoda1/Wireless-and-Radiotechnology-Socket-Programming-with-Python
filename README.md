# TCP Client–Server Communication

A simple TCP socket system where a client sends random temperature readings to a server every 5 seconds.

---

## How to run

### Local test

**Terminal 1 — start the server:**
```
python server.py
```

**Terminal 2 — start the client:**
```
python client.py
```

You should see the server print each temperature message as it arrives.

---

### Cross-device test (two devices on the same network)

1. Find your laptop's local IP address:
   - Windows: `ipconfig` → look for IPv4 Address
   - macOS/Linux: `ifconfig` or `ip a` → look for `inet` under your Wi-Fi adapter

2. On the **laptop**, run the server (no changes needed):
   ```
   python server.py
   ```

3. On the **second device** (or a second terminal on the same laptop), edit `client.py` and change:
   ```python
   HOST = '127.0.0.1'
   ```
   to your laptop's local IP, for example:
   ```python
   HOST = '192.168.1.42'
   ```
   Then run:
   ```
   python client.py
   ```

> If using a **mobile hotspot**: connect your laptop to the hotspot, find the IP your laptop was assigned, then connect a second device to the same hotspot and point `client.py` at that IP.

---

## Test results

### Localhost test
- Both scripts run on the same machine
- Server prints received messages every 5 seconds
- Example output:

```
Server listening on port 65432 ...
Connected by ('127.0.0.1', 52341)
Received: Temperature: 23.5 C
Received: Temperature: 27.1 C
Received: Temperature: 19.8 C
```

### Cross-device test
- Server running on laptop connected to mobile hotspot
- Client running on a second device on the same network
- Messages received successfully every 5 seconds

<img width="1875" height="991" alt="Screenshot 2026-03-25 153552" src="https://github.com/user-attachments/assets/d7864163-b191-4e07-9407-55b01d402fa6" />

---
