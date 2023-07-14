import json
import random
import hashlib

def sign(message):
    hash_object = hashlib.sha256(message.encode())
    hash_value = int(hash_object.hexdigest(), 16)

    keys = json.load(open("data/keys.json", "r"))

    p = keys['p']
    q = keys['q']
    g = keys['g']
    x = keys['x']
    y = keys['y']

    r = 0
    s = 0

    index = 0

    while True:
        k = random.randint(1, q - 1)

        print(f"-- STEP -- {index}")

        r = pow(g, k, p) % q

        k_inverse = pow(k, -1, q)  # Calculate k^-1 modulo q
        s = (k_inverse * (hash_value + (x * r))) % q

        if r != 0 and s != 0:
            break

        index += 1

    res = {
        'r': r,
        's': s
    }

    json.dump(res, open("data/signature.json", "w"))

sign("Hello world!")

