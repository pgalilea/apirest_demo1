"""
$ pip install -r requirements.txt
$ uvicorn main:app --reload 
"""

from fastapi import FastAPI

from helpers import buscar_patente

app = FastAPI()


@app.get('/')
def read_root():
	return {'welcome': 'Home'}

@app.get('/patentes/{patente_id}')
def get_patente(patente_id: str):
	
	if patente_id.isnumeric(): # es un ID
		return buscar_patente(ppu_id=int(patente_id))
	
	elif patente_id.isalnum(): # es una patente
		pnf = [d for d in patente_id]
		lt, nmb = tuple(pnf[:4]), ''.join(pnf[-3:])
		pnf = (lt, nmb)

		p_id = buscar_patente(ppu=pnf)
		
		return p_id or {'error': 'Patente no encontrada'}
	

	return {'error': 'Patente no cumple con formato'}
