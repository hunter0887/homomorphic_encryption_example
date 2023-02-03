from linmodel_1 import LinModel
import phe as paillier
import json

def getData():
	with open('C:/Users/USER/Desktop/Homomorphic-Encryption/data.json', 'r') as file: 
		d=json.load(file)
		data=json.loads(d)
		return data

def computeData():
	data=getData()
	mycoef=LinModel().getCoef()
	pk=data['p_key']
	pubkey= paillier.PaillierPublicKey(n=int(pk['n']))
	enc_nums_rec = [paillier.EncryptedNumber(pubkey, int(x[0], int(x[1]))) for x in data['values']]
	results=sum([mycoef[i]*enc_nums_rec[i] for i in range(len(mycoef))])
	return results, pubkey																				#비직렬화 값 나옴

def serializeData():
	results, pubkey = computeData()
	encrypted_data={}
	encrypted_data['pubkey'] = {'n': pubkey.n}
	encrypted_data['values'] = (str(results.ciphertext()), results.exponent)
	serialized = json.dumps(encrypted_data)
	return serialized																					#직렬화 값 나옴

def main():
	datafile=serializeData()
	with open('C:/Users/USER/Desktop/Homomorphic-Encryption/answer.json', 'w') as file:		#공개키, 암호문, 지수 등이 직렬화된 값으로 answer을 전달
		json.dump(datafile, file)

if __name__=='__main__':
	main()

print("=========================딥러닝 결과를 생성하였습니다.=========================")