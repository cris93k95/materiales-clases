import json
import re
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(r"c:\Users\crist\OneDrive\Escritorio\2026")
SITE = ROOT / "materiales-clases"

PLANS = [
    {
        "course_name": "1° Medio — Inglés General",
        "course_key": "1ro-lu-ju",
        "course_label": "1° Medio — Inglés General (Lu+Ju)",
        "unit_title": "Unidad 1 — The World of Technical Work",
        "file_prefix": "1ro_LuJu",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "1ro Medio" / "Lu+Ju" / "planificacion_unidad1_lu_ju.html",
        "output_dir": SITE / "1ro-medio" / "lu-ju" / "u1",
    },
    {
        "course_name": "3°A — Mecánica Industrial",
        "course_key": "3A-industrial",
        "course_label": "3°A — Mecánica Industrial",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roA_Industrial",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_industrial.html",
        "output_dir": SITE / "3ro-medio" / "3A-industrial" / "u1",
    },
    {
        "course_name": "3°B — Mecánica Automotriz",
        "course_key": "3B-automotriz",
        "course_label": "3°B — Mecánica Automotriz",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roB_Automotriz",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_automotriz.html",
        "output_dir": SITE / "3ro-medio" / "3B-automotriz" / "u1",
    },
    {
        "course_name": "3°C — Electricidad",
        "course_key": "3C-electricidad",
        "course_label": "3°C — Electricidad",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roC_Electricidad",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_electricidad.html",
        "output_dir": SITE / "3ro-medio" / "3C-electricidad" / "u1",
    },
    {
        "course_name": "3°D — Gráfica",
        "course_key": "3D-grafica",
        "course_label": "3°D — Gráfica",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roD_Grafica",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_grafica.html",
        "output_dir": SITE / "3ro-medio" / "3D-grafica" / "u1",
    },
    {
        "course_name": "3°E — Electrónica",
        "course_key": "3E-electronica",
        "course_label": "3°E — Electrónica",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roE_Electronica",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_electronica.html",
        "output_dir": SITE / "3ro-medio" / "3E-electronica" / "u1",
    },
    {
        "course_name": "4°A — Mecánica Industrial",
        "course_key": "4A-industrial",
        "course_label": "4°A — Mecánica Industrial",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "file_prefix": "4toA_Industrial",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_industrial.html",
        "output_dir": SITE / "4to-medio" / "4A-industrial" / "u1",
    },
    {
        "course_name": "4°B — Mecánica Automotriz",
        "course_key": "4B-automotriz",
        "course_label": "4°B — Mecánica Automotriz",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "file_prefix": "4toB_Automotriz",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_automotriz.html",
        "output_dir": SITE / "4to-medio" / "4B-automotriz" / "u1",
    },
    {
        "course_name": "4°C — Electricidad",
        "course_key": "4C-electricidad",
        "course_label": "4°C — Electricidad",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "file_prefix": "4toC_Electricidad",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_electricidad.html",
        "output_dir": SITE / "4to-medio" / "4C-electricidad" / "u1",
    },
    {
        "course_name": "4°E — Electrónica",
        "course_key": "4E-electronica",
        "course_label": "4°E — Electrónica",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "file_prefix": "4toE_Electronica",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_electronica.html",
        "output_dir": SITE / "4to-medio" / "4E-electronica" / "u1",
    },
]


def clean_text(text):
    return re.sub(r"\s+", " ", text or "").strip()


def short_title(text, max_len=80):
    if not text:
        return "Clase"
    first = text.split(".")[0].strip()
    return first if len(first) <= max_len else first[: max_len - 3].rstrip() + "..."


def get_phase_items(card, phase_keyword):
    for phase in card.select("div.fase"):
        title = clean_text(phase.select_one(".fase-title").get_text()) if phase.select_one(".fase-title") else ""
        if phase_keyword.lower() not in title.lower():
            continue
        content = phase.select_one(".fase-content")
        if not content:
            return []

        items = []
        for li in content.select("li"):
            txt = clean_text(li.get_text(" "))
            if txt:
                items.append(txt)

        if not items:
            txt = clean_text(content.get_text(" "))
            if txt:
                items = [txt]
        return items

    return []


def parse_vocab_from_development(dev_items):
    joined = " ".join(dev_items)
    patterns = [
        r"palabras clave(?: del área)?:\s*([^\.]+)\.",
        r"key words?:\s*([^\.]+)\.",
        r"vocabulary[^:]*:\s*([^\.]+)\.",
    ]
    for pattern in patterns:
        m = re.search(pattern, joined, flags=re.IGNORECASE)
        if m:
            raw = m.group(1)
            words = [clean_text(w) for w in raw.split(",")]
            words = [w for w in words if w and len(w) < 40]
            return words[:16]
    return []


def parse_reading_title(dev_items):
    joined = " ".join(dev_items)
    m = re.search(r"[\"']([^\"']{5,80})[\"']", joined)
    if m:
        return clean_text(m.group(1))
    return "Reading text"


def parse_reflection(close_items):
    for item in close_items:
        if "why" in item.lower() and "?" in item:
            return item
    return "Why is it important to know English in your career?"


def extract_classes(plan_path):
    html = plan_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    results = []
    for card in soup.select("div.clase-card"):
        class_num_span = card.select_one(".clase-num")
        class_num_text = clean_text(class_num_span.get_text()) if class_num_span else ""
        match = re.search(r"(\d+)", class_num_text)
        class_num = int(match.group(1)) if match else None
        if class_num is None:
            continue

        objective = ""
        objective_div = card.select_one(".objetivo")
        if objective_div:
            objective = clean_text(objective_div.get_text(" "))
            objective = objective.replace("Objetivo de la clase (Bloom):", "").replace("Objetivo de la clase:", "").strip()

        badges = [clean_text(b.get_text()) for b in card.select(".badge") if clean_text(b.get_text())]
        oa_label = " · ".join(badges) if badges else "OA"

        is_eval = "evaluacion" in card.get("class", []) or bool(card.select_one(".badge-eval"))

        start_items = get_phase_items(card, "INICIO")
        dev_items = get_phase_items(card, "DESARROLLO")
        close_items = get_phase_items(card, "CIERRE")

        vocab = parse_vocab_from_development(dev_items)
        reading_title = parse_reading_title(dev_items)
        reflection = parse_reflection(close_items)

        results.append(
            {
                "class_num": class_num,
                "objective": objective,
                "oa": oa_label,
                "is_eval": is_eval,
                "start_items": start_items,
                "dev_items": dev_items,
                "close_items": close_items,
                "vocab": vocab,
                "reading_title": reading_title,
                "reflection": reflection,
            }
        )

    return sorted(results, key=lambda x: x["class_num"])


def li_list(items):
    if not items:
        return "<li>Actividad guiada por el docente según planificación.</li>"
    return "".join(f"<li>{item}</li>" for item in items[:8])


def vocab_cards(words):
    if not words:
        return ""
    cards = []
    for word in words:
        cards.append(
            "<div class=\"vocab-card\" onclick=\"this.classList.toggle('revealed')\">"
            f"<div class=\"word\">{word}</div>"
            "<div class=\"meaning\">Definición/traducción trabajada en clase</div>"
            "<div class=\"hint\">clic para marcar aprendida</div>"
            "</div>"
        )
    return "".join(cards)


def development_cards(items):
    if not items:
        return "<div class=\"task-card\"><label><input type=\"checkbox\" class=\"task-check\"/> Actividades de desarrollo según planificación.</label></div>"
    cards = []
    for item in items[:6]:
        cards.append(
            "<div class=\"task-card\">"
            f"<label><input type=\"checkbox\" class=\"task-check\"/> {item}</label>"
            "</div>"
        )
    return "".join(cards)


def build_material_page(meta, class_info, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    class_num = class_info["class_num"]
    objective = class_info["objective"] or "Objetivo según planificación de la unidad."
    reflection = class_info["reflection"]
    vocab_html = vocab_cards(class_info["vocab"])
    reading_title = class_info["reading_title"]

    html = f"""<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Clase {class_num} — {meta['course_label']}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Inter', sans-serif; background: #f0f2f5; color: #333; line-height: 1.7; }}
        .header {{ background: linear-gradient(135deg, #1565c0, #1e88e5); color: white; padding: 35px 20px; text-align: center; }}
        .header h1 {{ font-size: 1.8em; font-weight: 700; margin-bottom: 5px; }}
        .header h2 {{ font-size: 1.15em; font-weight: 300; margin-bottom: 8px; }}
        .header .meta {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 12px; }}
        .header .meta span {{ background: rgba(255,255,255,0.2); padding: 5px 14px; border-radius: 20px; font-size: 0.85em; }}
        .container {{ max-width: 920px; margin: 25px auto; padding: 0 15px; }}

        .objective-card {{ background: white; border-radius: 12px; padding: 24px; margin-bottom: 22px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border-left: 5px solid #1565c0; }}
        .objective-card h3 {{ color: #1565c0; margin-bottom: 8px; }}
        .objective-en {{ background: #e3f2fd; padding: 10px 14px; border-radius: 8px; margin-top: 10px; font-style: italic; color: #0d47a1; }}

        .section {{ background: white; border-radius: 12px; margin-bottom: 22px; overflow: hidden; box-shadow: 0 2px 12px rgba(0,0,0,0.06); }}
        .section-header {{ padding: 14px 22px; color: white; font-weight: 600; font-size: 1.05em; }}
        .inicio {{ background: #2e7d32; }}
        .desarrollo {{ background: #1565c0; }}
        .cierre {{ background: #6a1b9a; }}
        .section-body {{ padding: 18px 22px; }}
        .section-body ul {{ margin-left: 18px; }}
        .section-body li {{ margin-bottom: 8px; }}

        .task-card {{ background: #f5f5f5; border: 1px solid #e0e0e0; border-radius: 10px; padding: 12px 14px; margin-bottom: 10px; }}
        .task-card input {{ margin-right: 8px; }}

        .vocab-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); gap: 10px; margin-top: 12px; }}
        .vocab-card {{ background: #e3f2fd; border: 2px solid #90caf9; border-radius: 10px; padding: 12px; text-align: center; cursor: pointer; }}
        .vocab-card .word {{ font-weight: 700; color: #0d47a1; }}
        .vocab-card .meaning {{ font-size: 0.8em; color: #666; margin-top: 4px; display: none; }}
        .vocab-card.revealed .meaning {{ display: block; }}
        .vocab-card .hint {{ font-size: 0.72em; color: #888; margin-top: 4px; }}
        .vocab-card.revealed .hint {{ display: none; }}

        .reading-box {{ background: #fafafa; border: 1px solid #e0e0e0; border-radius: 10px; padding: 16px; margin-top: 12px; }}
        .reading-box h4 {{ color: #1565c0; margin-bottom: 8px; }}

        .ticket-box {{ background: linear-gradient(135deg, #ede7f6, #e3f2fd); border: 2px dashed #1565c0; border-radius: 12px; padding: 18px; }}
        .ticket-input {{ width: 100%; padding: 9px 12px; border: 1px solid #ddd; border-radius: 8px; margin-top: 8px; }}

        .score-bar {{ background: white; border-radius: 10px; padding: 12px 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); display: flex; justify-content: space-between; align-items: center; }}
        .score {{ font-weight: 700; color: #1565c0; }}
        .footer {{ text-align: center; color: #999; font-size: 0.8em; margin: 18px 0; }}
    </style>
</head>
<body>
<div class=\"header\">
    <h1>CLASS {class_num} — {meta['course_label'].upper()}</h1>
    <h2>{meta['unit_title']}</h2>
    <div class=\"meta\">
        <span>📘 {class_info['oa']}</span>
        <span>⏱ 90 minutos</span>
        <span>🧭 Material de clase</span>
    </div>
</div>

<div class=\"container\">
    <div class=\"objective-card\">
        <h3>🎯 Objetivo de la clase</h3>
        <p>{objective}</p>
        <div class=\"objective-en\">Class focus: active vocabulary + guided practice + exit ticket.</div>
    </div>

    <div class=\"section\">
        <div class=\"section-header inicio\">🟢 Inicio (15 min)</div>
        <div class=\"section-body\"><ul>{li_list(class_info['start_items'])}</ul></div>
    </div>

    <div class=\"section\">
        <div class=\"section-header desarrollo\">🔵 Desarrollo (60 min)</div>
        <div class=\"section-body\">
            {development_cards(class_info['dev_items'])}
            {('<h4 style="margin-top:12px; color:#1565c0;">📖 Vocabulary Cards</h4><div class="vocab-grid">' + vocab_html + '</div>') if vocab_html else ''}
            <div class=\"reading-box\">
                <h4>📚 Reading Organizer — {reading_title}</h4>
                <p><strong>Before reading:</strong> What do you think this text is about?</p>
                <p><strong>While reading:</strong> Underline key words and verbs.</p>
                <p><strong>After reading:</strong> Write 3 key ideas from the text.</p>
            </div>
        </div>
    </div>

    <div class=\"section\">
        <div class=\"section-header cierre\">🟣 Cierre (15 min)</div>
        <div class=\"section-body\">
            <ul>{li_list(class_info['close_items'])}</ul>
            <div class=\"ticket-box\">
                <h4>🎫 Exit Ticket</h4>
                <input class=\"ticket-input\" placeholder=\"1) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"2) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"3) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"4) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"5) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"Reflection: {reflection}\" />
            </div>
        </div>
    </div>

    <div class=\"score-bar\">
        <span>📊 Progreso de actividades completadas:</span>
        <span class=\"score\" id=\"progressScore\">0</span>
    </div>

    <div class=\"footer\">{meta['course_label']} — Clase {class_num}, Unidad 1 — Inglés 2026</div>
</div>

<script>
    const checks = document.querySelectorAll('.task-check');
    function updateScore() {{
        let done = 0;
        checks.forEach(c => {{ if (c.checked) done++; }});
        document.getElementById('progressScore').textContent = done + ' / ' + checks.length;
    }}
    checks.forEach(c => c.addEventListener('change', updateScore));
    updateScore();
</script>
</body>
</html>
"""

    output_path.write_text(html, encoding="utf-8")


def load_progress():
    progress_path = SITE / "progress.json"
    if progress_path.exists():
        return progress_path, json.loads(progress_path.read_text(encoding="utf-8"))
    return progress_path, {"lastUpdated": str(date.today()), "classes": {}}


def save_progress(progress_path, data):
    data["lastUpdated"] = str(date.today())
    progress_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def update_index(materials):
    index_path = SITE / "index.html"
    soup = BeautifulSoup(index_path.read_text(encoding="utf-8"), "html.parser")

    course_map = {}
    for item in materials:
        course_map.setdefault(item["course_name"], []).append(item)

    for course_section in soup.select(".course-section"):
        h3 = course_section.select_one(".course-header h3")
        if not h3:
            continue

        course_name = clean_text(h3.get_text())
        if course_name not in course_map:
            continue

        unit_group = course_section.select_one(".unit-group")
        if not unit_group:
            continue

        unit_classes = unit_group.select_one(".unit-classes")
        if not unit_classes:
            continue

        unit_classes.clear()

        for item in sorted(course_map[course_name], key=lambda x: x["class_num"]):
            tag_class = "tag-eval" if item["is_eval"] else "tag-clase"
            tag_label = "Evaluación" if item["is_eval"] else "Clase"
            link_html = (
                f"<a class=\"class-link\" href=\"{item['href']}\" data-progress-id=\"{item['progress_id']}\">"
                f"<span class=\"num\">{item['class_num']}</span>"
                f"<span class=\"title\">{item['title']}</span>"
                f"<span class=\"tag {tag_class}\">{tag_label}</span>"
                f"<span class=\"status-badge status-pending\" data-status-badge>⏳ Pendiente</span>"
                f"</a>"
            )
            unit_classes.append(BeautifulSoup(link_html, "html.parser"))

    index_path.write_text(str(soup), encoding="utf-8")


def main():
    all_materials = []
    progress_path, progress = load_progress()

    for plan in PLANS:
        classes = extract_classes(plan["plan_path"])

        for c in classes:
            class_num = c["class_num"]
            file_name = f"Clase_{class_num}_U1_{plan['file_prefix']}.html"
            output_path = plan["output_dir"] / file_name

            build_material_page(plan, c, output_path)

            href = str(output_path.relative_to(SITE)).replace("\\", "/")
            title = f"Clase {class_num} — {short_title(c['objective'])}"
            progress_id = f"{plan['course_key']}/u1/Clase_{class_num}"

            progress["classes"][progress_id] = {
                "status": progress["classes"].get(progress_id, {}).get("status", "pending"),
                "title": title,
            }

            all_materials.append(
                {
                    "course_name": plan["course_name"],
                    "class_num": class_num,
                    "title": title,
                    "href": href,
                    "is_eval": c["is_eval"],
                    "progress_id": progress_id,
                }
            )

    save_progress(progress_path, progress)
    update_index(all_materials)


if __name__ == "__main__":
    main()
