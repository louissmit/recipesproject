
def get_embedding(vocab):
	embedding_path = "embeddings-scaled.EMBEDDING_SIZE=50.txt"
	new_embedding = ""
	f = open(embedding_path, 'r')
	line = f.readline()
	i = 0
	while line:
		words = line.split(" ")
		if words[0] in vocab:
			print line
			i+=1
			new_embedding += line
		line = f.readline()

	print len(vocab) - i
	f = open("new_embedding.txt", 'w')
	f.write(new_embedding)
