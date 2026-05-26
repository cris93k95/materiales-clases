import json, re, datetime
from pathlib import Path

today = datetime.date.today().isoformat()

specs_4to = ['4A-industrial','4B-automotriz','4C-electricidad','4E-electronica']
specs_3ro = ['3A-industrial','3B-automotriz','3C-electricidad','3D-grafica','3E-electronica']

titles = {}
for s in specs_4to:
    titles[f'{s}/u2/Clase_3'] = 'Clase 3 — Debate Prep: organizar argumentos PRO/CON (B1)'
    titles[f'{s}/u2/Clase_4'] = 'Clase 4 — Debate Day: debate estructurado (B1)'
for s in specs_3ro:
    titles[f'{s}/u2/Clase_3'] = 'Clase 3 — Debate Prep: preparar el mini-debate (A2)'
    titles[f'{s}/u2/Clase_4'] = 'Clase 4 — Mini-Debate Day (A2)'

p = Path('progress.json')
data = json.loads(p.read_text(encoding='utf-8'))
data['lastUpdated'] = today
for pid, title in titles.items():
    if pid in data['classes']:
        data['classes'][pid]['status'] = 'done'
        data['classes'][pid]['title'] = title
        data['classes'][pid]['date'] = today
p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
print('progress.json updated:', len(titles), 'entries')

idx = Path('index.html')
html = idx.read_text(encoding='utf-8')
count = 0
for pid, title in titles.items():
    pattern = re.compile(
        r'(data-progress-id="' + re.escape(pid) + r'"[^>]*>\s*<span class="num">\d+</span>\s*<span class="title">)([^<]*)(</span>)'
    )
    new_html, n = pattern.subn(lambda m: m.group(1) + title + m.group(3), html)
    if n:
        html = new_html
        count += n
idx.write_text(html, encoding='utf-8')
print('index.html titles replaced:', count)
