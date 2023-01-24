import mcstatus

print("""
             \033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m
  \033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m            __  __      ___        _   __   __           
  \033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m \033[44mA\u001b[0m\033[44mA\u001b[0m           |  \/  | __ / __| _ _  (_) / _| / _| ___  _ _ 
  \033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[33mT\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[33mT\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[42mS\u001b[0m\033[33mT\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m \033[44mA\u001b[0m\033[44mA\u001b[0m           | |\/| |/ _|\__ \| ' \ | ||  _||  _|/ -_)| '_|
  \033[33mT\u001b[0m\033[33mT\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[42mS\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m \033[44mA\u001b[0m\033[44mA\u001b[0m           |_|  |_|\__||___/|_||_||_||_|  |_|  \___||_|  
  \033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m
  \033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m
  \033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m
  \033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m\033[33mT\u001b[0m
       \033[44mA\u001b[0m\033[44mA\u001b[0m\033[44mA\u001b[0m
        \033[44mA\u001b[0m
""")

print('Enter the IP address and port of the server in the format "IP:Port"')
server_raw = input()
print('Enter the timeout time.')
delay = input()

try:
    float_delay = float(delay)
except ValueError:
    print(f"Cannot convert '{delay}' to float.")

try:
    server = mcstatus.JavaServer.lookup(server_raw, timeout=float_delay)
    status = server.status()

    print(f"\nMOTD: {status.description}")
    print(f"\nVERSION: {status.version.name}")
    print(f"\nPLAYERS: {status.players.online} online")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
