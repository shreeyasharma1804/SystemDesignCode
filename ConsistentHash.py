import random

N_SERVERS = 20
ITERATIONS = 50

servers = ["s"+str(i+1) for i in range(N_SERVERS)]


def ServerHealthStatus():
    return [0 if random.random() <= 0.5 else 1 for i in range(N_SERVERS)]


def hashNum():
    return random.randint(0, N_SERVERS)


while (True):
    healthStatus = ServerHealthStatus()
    hash = hashNum()
    print(f"Server to be accessed: {hash}")
    server = hash
    if (server >= N_SERVERS):
        server = 0
    if (healthStatus[server] == 0):
        while (server < N_SERVERS and healthStatus[server] == 0):
            print(f"Server health down: {server}")
            server += 1
            if (server == N_SERVERS):
                server = 0
    print(f"Request Complete: {server}")
