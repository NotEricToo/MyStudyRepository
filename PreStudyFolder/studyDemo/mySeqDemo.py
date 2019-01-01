class mySeq:
	def __init__(self):
		self.mseq = ['I','II','III','IV']

	def __len__(self):
		return len(self.mseq)

	def __getitem__(self,key):
		if 0 <= key < 4 :
			return self.mseq[key]

if __name__ == '__main__':
	m = mySeq()
	print('Len of mySeq : ',len(m))
	for i in range(len(m.mseq)):
		print(m.mseq[i])