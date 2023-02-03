import phe as paillier
import json

def storeKeys():
	public_key, private_key = paillier.generate_paillier_keypair()
	keys={}
	keys['public_key'] = {'n': public_key.n}
	keys['private_key'] = {'p': private_key.p,'q':private_key.q}
	with open('C:/Users/USER/Desktop/Homomorphic-Encryption/custkeys.json', 'w') as file:
		json.dump(keys, file)

def getKeys():
	with open('C:/Users/USER/Desktop/Homomorphic-Encryption/custkeys.json', 'r') as file:
		keys=json.load(file)
		pub_key=paillier.PaillierPublicKey(n=int(keys['public_key']['n']))
		priv_key=paillier.PaillierPrivateKey(pub_key,keys['private_key']['p'],keys['private_key']['q'])
		return pub_key, priv_key 

def serializeData(public_key, data):
	encrypted_data_list = [public_key.encrypt(x) for x in data]
	encrypted_data={}
	encrypted_data['p_key'] = {'n': public_key.n}
	encrypted_data['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_data_list]
	serialized = json.dumps(encrypted_data)
	return serialized

pub_key, priv_key = getKeys()
data = age, he, al, gen = [27,4,6,1]
serializeData(pub_key, data)
datafile=serializeData(pub_key, data)
with open('C:/Users/USER/Desktop/Homomorphic-Encryption/data.json', 'w') as file: 
    json.dump(datafile, file)
print("=========================custom의 정보가 입력되었습니다=========================\n=========================data파일을 생성했습니다.=========================")