from itertools import combinations_with_replacement, product, islice

letters = combinations_with_replacement('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)
numbers = [f'{n:03}' for n in range(1000)]
patentes = tuple(product(letters, numbers)) # huge tuples


def buscar_patente(ppu=None, ppu_id=None):
	
	if ppu:
		i = 0

		for p in patentes:
			if ppu==p: return {'patente':f'{"".join(p[0])}{p[1]}', 'id':i}
			i+=1
	
	elif ppu_id:
		ptt = list(islice(patentes, ppu_id, ppu_id+1))[0]

		return {'patente':f'{"".join(ptt[0])}{ptt[1]}', 'id':ppu_id}
