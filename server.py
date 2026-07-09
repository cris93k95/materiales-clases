import http.server
import os
import re
from functools import partial
from urllib.parse import unquote

PORT = int(os.environ.get("PORT", 8080))
SITE_ROOT = os.path.join(os.path.dirname(__file__), "v2")

# El sitio publicado sirve directamente el contenido de ./v2 en la raiz.
CLASS_RE = re.compile(r'^/(1ro-medio|3ro-medio|4to-medio)/.*/clase[^/]*\.html$', re.IGNORECASE)

# Snippet inyectado antes de </body> en cada página de clase del sitio V2.
# Agrega dos botones: descargar la clase actual (PDF) y la unidad completa (PDF).
INJECT_SNIPPET = r"""<!-- pdf-export injected -->
<style>
  .pdf-export-bar{position:fixed;right:18px;bottom:18px;z-index:99999;display:flex;flex-direction:column;gap:10px;font-family:'Inter',system-ui,sans-serif;}
  .pdf-export-bar button{cursor:pointer;border:none;border-radius:10px;padding:12px 16px;font-size:.9rem;font-weight:700;color:#fff;box-shadow:0 6px 18px rgba(15,23,42,.25);transition:transform .15s,box-shadow .15s;}
  .pdf-export-bar button:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(15,23,42,.35);}
  .pdf-btn-class{background:linear-gradient(135deg,#2563eb,#4f46e5);}
  .pdf-btn-unit{background:linear-gradient(135deg,#0f766e,#16a34a);}
  .pdf-export-bar button:disabled{opacity:.6;cursor:progress;}
  @media print{.pdf-export-bar{display:none!important;}}
</style>
<div class="pdf-export-bar no-print">
  <button class="pdf-btn-class" onclick="pdfDownloadClass()">🖨️ Descargar esta clase (PDF)</button>
  <button class="pdf-btn-unit" onclick="pdfDownloadUnit(this)">📚 Descargar unidad completa (PDF)</button>
</div>
<script>
function pdfDownloadClass(){ window.print(); }
async function pdfDownloadUnit(btn){
  const win = window.open('', '_blank');
  if(!win){ alert('Permite las ventanas emergentes para descargar la unidad completa.'); return; }
  win.document.write('<!doctype html><meta charset="utf-8"><title>Preparando unidad…</title><body style="font-family:Inter,system-ui,sans-serif;padding:48px;color:#0f172a;font-size:1.1rem">Preparando la unidad completa… por favor espera.</body>');
  const original = btn.textContent;
  btn.disabled = true; btn.textContent = 'Preparando unidad…';
  try{
    const path = location.pathname;
    const dir = path.substring(0, path.lastIndexOf('/') + 1);
    const idxRes = await fetch(dir + 'index.html', {cache:'no-store'});
    if(!idxRes.ok) throw new Error('No se encontró el índice de la unidad.');
    const idxDoc = new DOMParser().parseFromString(await idxRes.text(), 'text/html');
    const seen = new Set();
    const files = [];
    idxDoc.querySelectorAll('a[href]').forEach(a=>{
      const href = a.getAttribute('href');
      if(!href) return;
      const clean = href.split('#')[0].split('?')[0];
      if(clean.includes('/')) return;            // solo clases hermanas de esta unidad
      if(!/\.html$/i.test(clean)) return;
      if(/index\.html$/i.test(clean)) return;
      if(!/clase/i.test(clean)) return;
      if(seen.has(clean)) return;
      seen.add(clean); files.push(clean);
    });
    if(files.length === 0) throw new Error('No se encontraron clases en esta unidad.');
    const styleSeen = new Set();
    let headStyles = '';
    let bodyParts = '';
    for(const f of files){
      const r = await fetch(dir + f, {cache:'no-store'});
      if(!r.ok) continue;
      const d = new DOMParser().parseFromString(await r.text(), 'text/html');
      d.querySelectorAll('.pdf-export-bar').forEach(e=>e.remove());
      d.querySelectorAll('style').forEach(s=>{
        const key = s.textContent.trim().slice(0,120);
        if(styleSeen.has(key)) return;
        styleSeen.add(key); headStyles += s.outerHTML;
      });
      bodyParts += '<section class="pdf-unit-class">' + d.body.innerHTML + '</section>';
    }
    const combined = '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">' + headStyles +
      '<style>.pdf-unit-class{page-break-after:always;}.pdf-unit-class:last-child{page-break-after:auto;}@media print{.pdf-export-bar{display:none!important;}}</style>' +
      '</head><body>' + bodyParts + '</body></html>';
    win.document.open();
    win.document.write(combined);
    win.document.close();
    win.focus();
    setTimeout(()=>{ try{ win.print(); }catch(e){} }, 700);
  }catch(err){
    try{ win.close(); }catch(e){}
    alert('No se pudo generar el PDF de la unidad: ' + (err && err.message ? err.message : err));
  }finally{
    btn.disabled = false; btn.textContent = original;
  }
}
</script>
"""


class InjectingHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        raw = self.path.split('?', 1)[0].split('#', 1)[0]
        path = unquote(raw)
        if CLASS_RE.search(path):
            fs_path = self.translate_path(self.path)
            if os.path.isfile(fs_path):
                try:
                    with open(fs_path, 'rb') as f:
                        content = f.read().decode('utf-8', 'replace')
                except OSError:
                    return super().do_GET()
                if '</body>' in content:
                    content = content.replace('</body>', INJECT_SNIPPET + '</body>', 1)
                else:
                    content += INJECT_SNIPPET
                data = content.encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
                self.wfile.write(data)
                return
        return super().do_GET()


handler = partial(InjectingHandler, directory=SITE_ROOT)
handler.func.extensions_map.update({".html": "text/html; charset=utf-8"})

with http.server.HTTPServer(("0.0.0.0", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
