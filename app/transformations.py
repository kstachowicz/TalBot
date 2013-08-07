from nltk.corpus import stopwords



def filter_insignificant(chunk, tag_suffixes=['DT', 'CC']):
	good_words = []

	for word, tag in chunk:
		ok = True

		for suffix in tag_suffixes:
			if tag.endswith(suffix):
				ok = False
				break

		if ok:
			good_words.append((word, tag))

	return good_words

def first_chunk_index(chunk, pred, start = 0, step =1):
	l = len(chunk)
	end = l if step > 0 else -1

	for i in range(start, end, step):
		if pred(chunk[i]):
			return i

	return None

def remove_stopwords(chunk):
	english_stops = set(stopwords.words('english'))
	return [word for word in chunk if word[0] not in english_stops]


def swap_verb_phrase(chunk):
	verb_predicate = lambda (word, tag): tag != 'VBG' and tag.startswith('VB') and len(tag) > 2
	verb_id = first_chunk_index(chunk, verb_predicate)

	if verb_id is None:
		return chunk

	return chunk[verb_id + 1:] + chunk[:verb_id]


def swap_infinitive_phrase(chunk):
	in_predicate = lambda (word, tag): tag == 'IN' and word != 'like'
	print chunk
	in_id = first_chunk_index(chunk, in_predicate)

	if in_id is None:
		return chunk

	nn_predicate = lambda (word, tag): tag.startswith('NN')
	nn_id = first_chunk_index(chunk, nn_predicate, start=in_id, step=-1) or 0

	return chunk[:nn_id] + chunk[in_id+1:] + chunk[nn_id:in_id]

def singularize_plurar_noun(chunk):
	nns_predicate = lambda(word, tag): tag == 'NNS'
	nns_id = first_chunk_index(chunk, nns_predicate)
	if nns_predicate is not None and nns_id + 1 < len(chunk) and chunk[nns_id +1][1][:2] == 'NN':
		noun, nns_tag = chunk[nns_id]
		chunk[nns_id] = (noun.rstrip('s'), nns_tag.rstrip('S'))

	return chunk

