
import numpy as np
from fastapi import FastAPI, Path, Query

from helpers import buscar_patente

app = FastAPI()


@app.get('/', summary='Inicio')
def read_root():
	return {'welcome': 'Home'}

@app.get('/patentes/{patente_id}', summary='Obtener patente')
def get_patente(patente_id: str = Path(..., description='Patente o ID')):
	
	if patente_id.isnumeric(): # es un ID
		ppu_id = int(patente_id)
		if ppu_id<=0: return {'error': 'El ID de patente debe ser mayor de cero'}
		return buscar_patente(ppu_id=ppu_id)
	
	elif patente_id.isalnum(): # es una patente
		pnf = [d for d in patente_id]
		lt, nmb = tuple(pnf[:4]), ''.join(pnf[-3:])
		pnf = (lt, nmb)

		p_id = buscar_patente(ppu=pnf)
		
		return p_id or {'error': 'Patente no encontrada'}
	
	return {'error': 'Patente no cumple con formato'}

@app.get('/sumatoria-matriz', summary='Obtener sumatoria')
def get_sum_M(*,
	R: int = Query(..., description='Cantidad de filas', gt=0),
	C: int = Query(..., description='Cantidad de columnas', gt=0),
	Z: int = Query(..., description='', gt=0, le=1000000),
	X: int = Query(..., description='', ge=0),
	Y: int = Query(..., description='', ge=0)):

	m = np.array([np.arange(Z, R+Z) for _ in range(C)]).T
	
	print(m)
	print(m[:Y, :X])

	return {'sumatoria': int(m[:Y, :X].sum())}
