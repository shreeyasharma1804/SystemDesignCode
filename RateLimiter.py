import time

shards = [inMemoryCache1 := {}, inMemoryCache2 := {}, inMemoryCache3 := {}] # shards
nShards = len(shards)
ipWithTimeOut = {}
nRequestsAllowed = 10
timeOut = 10
sendRequestAfter = 15


def hashIP(ip):
    octets = ip.split('.')
    totalSum = 0
    for octet in octets:
        totalSum += sum(int(digit) for digit in octet)
    return totalSum

        
def rateLimiter(ip, timeStamp, totalSum):
    shard = shards[totalSum%nShards]
    ipRequestTimes = shard.get(ip, [])
    if(len(ipRequestTimes) == 0):
        shard[ip] = [timeStamp]
    elif(len(ipRequestTimes) < nRequestsAllowed):
        shard[ip].append(timeStamp)
    elif(len(ipRequestTimes) == nRequestsAllowed):
        if(ip in ipWithTimeOut and timeStamp - shard[ip][-1] >= sendRequestAfter):
            del ipWithTimeOut[ip]
            SendHTTPResponse(200)
        elif(ip in ipWithTimeOut and timeStamp - shard[ip][-1] < sendRequestAfter):
            SendHTTPResponse(500)
        elif(ip not in ipWithTimeOut and timeStamp - shard[ip][0] > timeOut):
            SendHTTPResponse(200)
        elif(ip not in ipWithTimeOut and timeStamp - shard[ip][0] < timeOut):
            ipWithTimeOut[ip] = 1
            SendHTTPResponse(500)
        shard[ip].pop(0)
        shard[ip].append(timeStamp)
        
def SendHTTPResponse(responseCose):
    pass
    
            
            
# Read The HTTP request to get the IP address and timestamp
ip = "192.168.1.6"
timeStamp = time.time()
totalSum = hashIP(ip)
rateLimiter(ip, timeStamp, totalSum)

