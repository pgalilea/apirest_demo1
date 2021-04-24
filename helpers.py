from itertools import combinations_with_replacement, product, islice

def get_patentes():
	"""Esta función hace el heavy lifting."""
	return product(product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=4), [f'{n:03}' for n in range(1000)])

def buscar_patente(ppu=None, ppu_id=None):
	
	if ppu:
		i = 1
		for p in get_patentes():
			if ppu==p: return {'patente':f'{"".join(p[0])}{p[1]}', 'id':i}
			i+=1

	elif ppu_id:
		ptt = list(islice(get_patentes(), ppu_id-1, ppu_id))[0]

		return {'patente':f'{"".join(ptt[0])}{ptt[1]}', 'id':ppu_id}
