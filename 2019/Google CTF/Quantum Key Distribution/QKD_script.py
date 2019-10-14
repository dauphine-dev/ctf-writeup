import json
import random
import requests

def rotate_45(qubit):
	qubit = complex(qubit["real"], qubit["imag"]) * complex(0.707, 0.707)
	return {"real": qubit.real, "imag": qubit.imag}

def gen_qubits():
	base = [random.choice('+x') for _ in range(512)]
	qubits = [random.choice([{"real": 0, "imag": 1}, {"real": 0, "imag": -1}]) for _ in range(512)]
	qubits = [q if b == '+' else rotate_45(q) for b, q in zip(base, qubits)]

basis = ["+","x","x","+","x","x","x","+","x","+","+","x","+","+","+","x","x","+","+","x","x","+","x","x","+","x","+","x","+","+","x","x","x","x","x","x","+","+","+","x","x","x","x","x","x","+","x","+","+","x","+","+","x","+","x","x","x","x","x","+","x","+","+","+","+","x","x","+","+","+","x","x","+","x","x","x","+","+","x","+","x","+","x","x","+","+","x","+","x","x","+","x","+","x","x","x","+","x","+","x","+","+","x","x","+","+","+","x","x","x","+","x","+","x","x","+","x","x","x","+","+","+","x","+","x","x","+","x","+","+","+","+","+","x","x","x","+","x","+","+","+","+","+","x","+","+","+","+","+","+","x","+","x","+","+","+","+","+","x","x","x","+","x","+","x","x","+","+","x","+","x","+","+","x","x","+","+","+","x","x","+","+","+","x","x","x","+","x","x","x","x","x","+","+","+","+","x","+","x","+","x","x","+","+","+","x","+","+","+","+","+","+","x","x","+","+","x","x","+","+","x","x","x","x","x","+","+","+","x","x","+","+","x","x","+","x","x","x","x","+","+","+","+","+","+","x","x","x","x","x","x","+","+","x","+","+","x","+","x","x","x","x","x","x","x","x","x","+","x","x","+","x","+","+","x","x","+","x","+","+","x","+","x","+","x","+","x","+","+","+","x","+","+","x","+","+","+","x","+","x","+","x","+","x","+","+","+","+","+","+","x","+","x","x","x","+","x","x","x","+","+","x","x","x","x","+","x","x","+","x","+","+","+","+","x","x","+","+","+","x","x","+","x","+","+","+","x","x","x","+","+","+","+","x","+","+","+","+","+","x","+","+","+","x","+","x","x","x","+","+","x","x","x","+","x","+","x","x","x","x","x","+","x","+","+","x","x","x","x","+","x","x","+","+","x","+","x","x","+","x","x","x","+","x","x","x","x","x","x","+","+","+","+","+","x","+","+","x","x","+","x","x","+","x","+","+","x","+","x","+","x","+","+","x","x","+","+","+","x","+","x","x","+","x","+","+","x","x","x","+","+","x","x","x","x","+","+","+","x","x","x","x","+","x","x","+","x","x","+","+","+","x","x","+","+","+","x","+","+","+","x","+","+","+","+","x","x","x","+","x","x","+","x","+","x","x","+","+","x","x","x","x","+","+","+","+","+","+","x","x","x","+"]
qubits = [{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":-0.707,"imag":0.707},{"real":-0.707,"imag":0.707},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0,"imag":-1},{"real":0,"imag":-1},{"real":0,"imag":1},{"real":0,"imag":1},{"real":0.707,"imag":-0.707},{"real":0.707,"imag":-0.707},{"real":-0.707,"imag":0.707},{"real":0,"imag":1}]

link = 'https://cryptoqkd.web.ctfcompetition.com/qkd/qubits'
headers = {"Content-Type": "application/json"}
data = json.dumps({"basis": basis, "qubits": qubits})
r = requests.session().post(link, data=data, headers=headers)
resp = json.loads(r.text)
print(hex(int(resp['announcement'], 16) ^ 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)[2:])

'''
$ echo "946cff6c9d9efed002233a6a6c7b83b1" > /tmp/plain.key; xxd -r -p /tmp/plain.key > /tmp/enc.key
$ echo "U2FsdGVkX19OI2T2J9zJbjMrmI0YSTS+zJ7fnxu1YcGftgkeyVMMwa+NNMG6fGgjROM/hUvvUxUGhctU8fqH4titwti7HbwNMxFxfIR+lR4=" | openssl enc -d -aes-256-cbc -pbkdf2 -md sha1 -base64 --pass file:/tmp/enc.key
>>> CTF{you_performed_a_quantum_key_exchange_with_a_satellite}
'''