from Crypto.PublicKey import DSA
import json
import time
import random

start = time.time()

# Generate p, q, and g
key = DSA.generate(2048)

x = random.randint(1, key.q - 1)
y = pow(key.g, x, key.p)

end = time.time()

# Extract p, q, and g
data = {
    'p': key.p,
    'q': key.q,
    'g': key.g,
    'x': x,
    'y': y
}

with open("data/keys.json", "w") as file:
    json.dump(data, file)

print(f"[TIME]: {str(end - start)}")


