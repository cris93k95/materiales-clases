import json
import os
import re
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(r"c:\Users\crist\OneDrive\Escritorio\2026")
SITE = ROOT / "materiales-clases"

PLANS = [
    {
        "level": "1ro",
        "course_name": "1° Medio — Inglés General",
        "course_key": "1ro-lu-ju",
        "course_label": "1° Medio — Inglés General (Lu+Ju)",
        "unit_title": "Unidad 1 — The World of Technical Work",
        "file_prefix": "1ro_LuJu",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "1ro Medio" / "Lu+Ju" / "planificacion_unidad1_lu_ju.html",
        "output_dir": SITE / "1ro-medio" / "lu-ju" / "u1",
    },
    {
        "level": "3ro",
        "course_name": "3°A — Mecánica Industrial",
        "course_key": "3A-industrial",
        "course_label": "3°A — Mecánica Industrial",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roA_Industrial",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_industrial.html",
        "output_dir": SITE / "3ro-medio" / "3A-industrial" / "u1",
        "march_count": 4,
    },
    {
        "level": "3ro",
        "course_name": "3°B — Mecánica Automotriz",
        "course_key": "3B-automotriz",
        "course_label": "3°B — Mecánica Automotriz",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roB_Automotriz",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_automotriz.html",
        "output_dir": SITE / "3ro-medio" / "3B-automotriz" / "u1",
        "march_count": 4,
    },
    {
        "level": "3ro",
        "course_name": "3°C — Electricidad",
        "course_key": "3C-electricidad",
        "course_label": "3°C — Electricidad",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roC_Electricidad",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_electricidad.html",
        "output_dir": SITE / "3ro-medio" / "3C-electricidad" / "u1",
        "march_count": 4,
    },
    {
        "level": "3ro",
        "course_name": "3°D — Gráfica",
        "course_key": "3D-grafica",
        "course_label": "3°D — Gráfica",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roD_Grafica",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_grafica.html",
        "output_dir": SITE / "3ro-medio" / "3D-grafica" / "u1",
        "march_count": 4,
    },
    {
        "level": "3ro",
        "course_name": "3°E — Electrónica",
        "course_key": "3E-electronica",
        "course_label": "3°E — Electrónica",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "file_prefix": "3roE_Electronica",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_electronica.html",
        "output_dir": SITE / "3ro-medio" / "3E-electronica" / "u1",
        "march_count": 4,
    },
    {
        "level": "4to",
        "course_name": "4°A — Mecánica Industrial",
        "course_key": "4A-industrial",
        "course_label": "4°A — Mecánica Industrial",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "file_prefix": "4toA_Industrial",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_industrial.html",
        "output_dir": SITE / "4to-medio" / "4A-industrial" / "u1",
        "march_count": 4,
    },
    {
        "level": "4to",
        "course_name": "4°B — Mecánica Automotriz",
        "course_key": "4B-automotriz",
        "course_label": "4°B — Mecánica Automotriz",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "file_prefix": "4toB_Automotriz",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_automotriz.html",
        "output_dir": SITE / "4to-medio" / "4B-automotriz" / "u1",
        "march_count": 4,
    },
    {
        "level": "4to",
        "course_name": "4°C — Electricidad",
        "course_key": "4C-electricidad",
        "course_label": "4°C — Electricidad",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "file_prefix": "4toC_Electricidad",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_electricidad.html",
        "output_dir": SITE / "4to-medio" / "4C-electricidad" / "u1",
        "march_count": 4,
    },
    {
        "level": "4to",
        "course_name": "4°E — Electrónica",
        "course_key": "4E-electronica",
        "course_label": "4°E — Electrónica",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "file_prefix": "4toE_Electronica",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_electronica.html",
        "output_dir": SITE / "4to-medio" / "4E-electronica" / "u1",
        "march_count": 4,
    },
]


def clean_text(text):
    return re.sub(r"\s+", " ", text or "").strip()


def extract_march_classes(plan_path):
    html = plan_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    class_cards = soup.select("div.clase-card")
    results = []

    for card in class_cards:
        date_span = card.select_one(".clase-fecha")
        if not date_span:
            continue
        date_text = clean_text(date_span.get_text())
        if "marzo" not in date_text.lower():
            continue

        class_num_span = card.select_one(".clase-num")
        class_num_text = clean_text(class_num_span.get_text()) if class_num_span else ""
        match = re.search(r"(\d+)", class_num_text)
        class_num = int(match.group(1)) if match else None

        objetivo_div = card.select_one(".objetivo")
        objetivo_text = clean_text(objetivo_div.get_text()) if objetivo_div else ""
        objetivo_text = objetivo_text.replace("Objetivo de la clase:", "").strip()
        objetivo_text = objetivo_text.replace("Objetivo de la clase (Bloom):", "").strip()

        is_eval = "evaluacion" in card.get("class", []) or bool(card.select_one(".badge-eval"))

        results.append({
            "class_num": class_num,
            "date_text": date_text,
            "objective": objetivo_text,
            "is_eval": is_eval,
            "card_html": str(card),
        })

    return results


def short_title(text, max_len=80):
    if not text:
        return "Clase"
    first = text.split(".")[0].strip()
    return first if len(first) <= max_len else (first[:max_len - 3].rstrip() + "...")


def build_material_page(meta, class_info, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    objective = class_info["objective"]
    class_num = class_info["class_num"]
    date_text = class_info.get("date_text") or "Marzo 2026"

    page_title = f"{meta['course_label']} - Clase {class_num}"

    html = f"""<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>{page_title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f5f5; color: #333; line-height: 1.6; }}
        .header {{ background: linear-gradient(135deg, #0f172a, #1e3a8a); color: white; padding: 28px; text-align: center; }}
        .header h1 {{ font-size: 1.6em; margin-bottom: 6px; }}
        .header h2 {{ font-size: 1.1em; font-weight: 300; margin-bottom: 8px; }}
        .meta-info {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 10px; }}
        .meta-info span {{ background: rgba(255,255,255,0.15); padding: 5px 14px; border-radius: 20px; font-size: 0.85em; }}
        .container {{ max-width: 1000px; margin: 20px auto; padding: 0 15px; }}
        .note {{ background: #fff7ed; border-left: 4px solid #f59e0b; padding: 10px 12px; border-radius: 0 6px 6px 0; margin-bottom: 15px; font-size: 0.92em; }}

        .clase-card {{ background: white; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); overflow: hidden; }}
        .clase-card.evaluacion {{ border-left: 5px solid #c62828; }}
        .clase-header {{ padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }}
        .clase-header.normal {{ background: #e8eaf6; }}
        .clase-header.eval {{ background: #ffebee; }}
        .clase-header .clase-num {{ font-size: 1.1em; font-weight: 700; color: #1a237e; }}
        .clase-header .clase-fecha {{ font-size: 0.85em; color: #666; }}
        .clase-header .badge {{ padding: 3px 10px; border-radius: 12px; font-size: 0.75em; font-weight: 600; }}
        .badge-oa {{ background: #e3f2fd; color: #1565c0; }}
        .badge-eval {{ background: #ffcdd2; color: #c62828; }}
        .clase-body {{ padding: 20px; }}
        .objetivo {{ background: #fff3e0; border-left: 4px solid #ef6c00; padding: 12px 15px; margin-bottom: 15px; border-radius: 0 6px 6px 0; }}
        .objetivo strong {{ color: #ef6c00; }}
        .fase {{ margin-bottom: 12px; }}
        .fase-title {{ display: inline-block; padding: 3px 12px; border-radius: 4px; font-weight: 600; font-size: 0.85em; color: white; margin-bottom: 6px; }}
        .fase-inicio {{ background: #2e7d32; }}
        .fase-desarrollo {{ background: #1565c0; }}
        .fase-cierre {{ background: #6a1b9a; }}
        .fase-content {{ padding-left: 15px; font-size: 0.92em; }}
        .fase-content ol, .fase-content ul {{ margin-left: 15px; }}
        .fase-content li {{ margin-bottom: 4px; }}
        .recursos {{ background: #f1f8e9; padding: 10px 15px; border-radius: 6px; margin-top: 10px; font-size: 0.88em; }}
        .recursos strong {{ color: #33691e; }}
        .evaluacion-box {{ background: #fce4ec; padding: 10px 15px; border-radius: 6px; margin-top: 10px; font-size: 0.88em; }}
        .evaluacion-box strong {{ color: #c62828; }}

        .footer {{ text-align: center; padding: 20px; color: #999; font-size: 0.8em; }}
        @media print {{
            body {{ background: white; }}
            .clase-card {{ break-inside: avoid; page-break-inside: avoid; box-shadow: none; border: 1px solid #ddd; }}
            .header {{ background: #1a237e !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
        }}
    </style>
</head>
<body>

<div class=\"header\">
    <h1>{meta['course_label']} — Unidad 1</h1>
    <h2>Clase {class_num} · {meta['unit_title']}</h2>
    <div class=\"meta-info\">
        <span>📅 {date_text}</span>
        <span>🧭 Marzo 2026</span>
        <span>📘 Basado en planificacion oficial</span>
    </div>
</div>

<div class=\"container\">
    <div class=\"note\">
        <strong>Objetivo sintetizado:</strong> {objective or 'Ver objetivo en la planificacion.'}
    </div>

    {class_info['card_html']}

    <div class=\"footer\">
        <p>Material de clase generado desde planificaciones U1 — 2026</p>
    </div>
</div>

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
            tag_label = "Evaluacion" if item["is_eval"] else "Clase"
            badge = "<span class=\"status-badge status-pending\" data-status-badge>⏳ Pendiente</span>"
            link_html = (
                f"<a class=\"class-link\" href=\"{item['href']}\" data-progress-id=\"{item['progress_id']}\">"
                f"<span class=\"num\">{item['class_num']}</span>"
                f"<span class=\"title\">{item['title']}</span>"
                f"<span class=\"tag {tag_class}\">{tag_label}</span>"
                f"{badge}"
                f"</a>"
            )
            unit_classes.append(BeautifulSoup(link_html, "html.parser"))

    index_path.write_text(str(soup), encoding="utf-8")


def main():
    materials = []

    progress_path, progress = load_progress()

    for plan in PLANS:
        classes = extract_march_classes(plan["plan_path"])
        if not classes and plan.get("march_count"):
            full = extract_march_classes(plan["plan_path"])  # returns all if no date spans
            if not full:
                html = plan["plan_path"].read_text(encoding="utf-8")
                soup = BeautifulSoup(html, "html.parser")
                class_cards = soup.select("div.clase-card")
                full = []
                for idx, card in enumerate(class_cards, start=1):
                    class_num_span = card.select_one(".clase-num")
                    class_num_text = clean_text(class_num_span.get_text()) if class_num_span else f"Clase {idx}"
                    match = re.search(r"(\d+)", class_num_text)
                    class_num = int(match.group(1)) if match else idx

                    objetivo_div = card.select_one(".objetivo")
                    objetivo_text = clean_text(objetivo_div.get_text()) if objetivo_div else ""
                    objetivo_text = objetivo_text.replace("Objetivo de la clase:", "").strip()
                    objetivo_text = objetivo_text.replace("Objetivo de la clase (Bloom):", "").strip()

                    is_eval = "evaluacion" in card.get("class", []) or bool(card.select_one(".badge-eval"))

                    full.append({
                        "class_num": class_num,
                        "date_text": f"Semana {idx} · marzo",
                        "objective": objetivo_text,
                        "is_eval": is_eval,
                        "card_html": str(card),
                    })

            classes = [c for c in full if c["class_num"] <= plan["march_count"]]
        for c in classes:
            class_num = c["class_num"]
            if class_num is None:
                continue

            file_name = f"Clase_{class_num}_U1_{plan['file_prefix']}.html"
            output_path = plan["output_dir"] / file_name

            if not output_path.exists():
                build_material_page(plan, c, output_path)

            href = str(output_path.relative_to(SITE)).replace("\\", "/")
            title = f"Clase {class_num} — {short_title(c['objective'])}"
            progress_id = f"{plan['course_key']}/u1/Clase_{class_num}"

            progress["classes"].setdefault(progress_id, {
                "status": "pending",
                "title": title,
            })

            materials.append({
                "course_name": plan["course_name"],
                "class_num": class_num,
                "title": title,
                "href": href,
                "is_eval": c["is_eval"],
                "progress_id": progress_id,
            })

    save_progress(progress_path, progress)
    update_index(materials)


if __name__ == "__main__":
    main()
