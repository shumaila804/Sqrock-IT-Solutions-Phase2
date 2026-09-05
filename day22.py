import time

class RateLimiter:
    def __init__(self, token_capacity, refill_rate_per_sec):
        self.capacity = token_capacity
        self.refill_rate = refill_rate_per_sec
        self.ledger = {}

    def allow_request(self, client_ip):
        now = time.time()
        if client_ip not in self.ledger:
            self.ledger[client_ip] = {"tokens": self.capacity, "last_updated": now}
        
        state = self.ledger[client_ip]
        elapsed = now - state["last_updated"]
        
        # Replenish tokens linearly based on elapsed time
        state["tokens"] = min(self.capacity, state["tokens"] + (elapsed * self.refill_rate))
        state["last_updated"] = now
        
        if state["tokens"] >= 1:
            state["tokens"] -= 1
            return True
        return False

# Local orchestration check simulating rapid requests from a client IP
if __name__ == "__main__":
    limiter = RateLimiter(token_capacity=3, refill_rate_per_sec=0.5)
    test_ip = "192.168.1.50"
    
    print(f"[*] Testing Rate Limiter for Client IP: {test_ip}\n")
    for i in range(1, 6):
        allowed = limiter.allow_request(test_ip)
        if allowed:
            print(f"[REQUEST {i}] ALLOWED: Token available, processing request...")
        else:
            print(f"[REQUEST {i}] BLOCKED: Rate limit exceeded (Too Many Requests).")
        time.sleep(0.2) # Short delay between rapid requests