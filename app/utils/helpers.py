from itertools import product, islice

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_patentes():
	"""Esta función hace el heavy lifting."""
	return product(product(letters, repeat=4), [f'{n:03}' for n in range(1000)])

def buscar_patente(ppu=None, ppu_id=None, brute=False):
	
	if ppu:
		if not brute: return {'patente':f'{"".join(ppu[0])}{ppu[1]}', 'id':calc_id(ppu)}

		i = 1
		for p in get_patentes():
			if ppu==p: return {'patente':f'{"".join(p[0])}{p[1]}', 'id':i}
			i+=1

	elif ppu_id:
		# if not brute: return calc_ppu(ppu_id)

		ptt = list(islice(get_patentes(), ppu_id-1, ppu_id))[0]

		return {'patente':f'{"".join(ptt[0])}{ptt[1]}', 'id':ppu_id}

def calc_id(ppu):
	"""
	Dada una patente, aplica una fórmula para calcular su Id.

	Multiplica cada letra por (largo del abecedario elevado a la posición) por 1000.
	Luego, suma todos los elementos.
	"""

	lts, nmb = ppu
	lt_ix = [letters.index(lt) for lt in lts]
	
	q_lts = len(letters) # podría ser fijo: 26
	exps = range(len(lt_ix)-1, -1, -1)
	
	ppu_id = [lt_ix[i]*(q_lts**exps[i])*1000 for i in range(len(exps))]
	print('Elementos sumatoria:', ppu_id+[int(nmb)+1])

	return sum(ppu_id) + int(nmb)+1

def calc_ppu(_id):
	"""
	Dado un Id, calcula su patente correspondiente.
	"""

	return {}

def validar_formato(ppu):
	if len(ppu)!=7: return {'error': 'El largo de la patente debe ser 7'}
	elif not ppu[:4].isalpha(): return {'error': 'Los 4 primeros componentes deben ser caracteres'}
	elif ppu[4:].isnumeric(): return {'error': 'Los últimos 3 dígitos deben ser numéricos'}

	return True
