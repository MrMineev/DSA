import json
import hashlib

def hash(message):
    hash_object = hashlib.sha256(message.encode())
    hash_value = int(hash_object.hexdigest(), 16)
    return hash_value

message = "Hello world!"

keys = json.load(open("data/keys.json", "r"))
signature = json.load(open("data/signature.json", "r"))
r = signature['r']
s = signature['s']

p = keys['p']
q = keys['q']
g = keys['g']
y = keys['y']

w = pow(s, -1, q)
u1 = (hash(message) * w) % q
u2 = (r * w) % q
v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

print(f"V: {v}\nR: {r}")

if v == r:
    print("REAL!")
else:
    print("FAKE!")

