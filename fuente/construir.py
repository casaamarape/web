"""Genera index.html y el catálogo del chat a partir de los archivos fuente.
Uso (desde la raíz del repositorio):  python3 fuente/construir.py
"""
import json, os
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
P = json.load(open(os.path.join(AQUI, 'productos.json'), encoding='utf-8'))
M = json.load(open(os.path.join(AQUI, 'menu.json'), encoding='utf-8'))
ids = {p['id'] for p in P}
for g in M:
    for i in g['ids'] + [i for s in g['subs'] for i in s['ids']]:
        assert i in ids, f"El menú '{g['l']}' usa un producto que no existe: {i}"
sinfoto = [p['id'] for p in P if not os.path.exists(os.path.join(RAIZ, 'img', p['id'] + '.jpg'))]
if sinfoto: print('Aviso: productos sin foto en img/:', sinfoto)
t = open(os.path.join(AQUI, 'plantilla.html'), encoding='utf-8').read()
html = t.replace('__PRODUCTS__', json.dumps(P, ensure_ascii=False)).replace('__MENU__', json.dumps(M, ensure_ascii=False))
open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf-8').write(html)
cats = {p['id']: [] for p in P}
for g in M:
    for s in g['subs']:
        for i in s['ids']: cats[i].append(f"{g['l']} > {s['l']}")
    if not g['subs']:
        for i in g['ids']: cats[i].append(g['l'])
cat = [{'id': p['id'], 'nombre': p['name'], 'precio': p['price'], 'opciones': [f"{v[0]}: S/ {v[1]}" for v in p['variants']] if p.get('variants') else None,
        'categorias': sorted(set(cats[p['id']])), 'contenido': p['items'], 'cumpleanos': bool(p.get('cumple')),
        'anticipacion_dias': p.get('lead', 0), 'solo_turno_tarde': bool(p.get('pm'))} for p in P]
json.dump(cat, open(os.path.join(RAIZ, 'netlify', 'functions', 'catalog.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print(f'Listo: index.html y catálogo del chat con {len(P)} productos.')
