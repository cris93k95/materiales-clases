import json
import re
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(r"c:\Users\crist\OneDrive\Escritorio\2026")
SITE = ROOT / "materiales-clases"

COURSES = [
    {
        "course_name": "1° Medio — Inglés General",
        "course_key": "1ro-lu-ju",
        "course_label": "1° Medio — Inglés General (Lu+Ju)",
        "unit_title": "Unidad 1 — The World of Technical Work",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "1ro Medio" / "Lu+Ju" / "planificacion_unidad1_lu_ju.html",
        "relative_file": "1ro-medio/lu-ju/u1/Clase_2_U1_1ro_LuJu.html",
        "vocab_review": ["hammer", "screwdriver", "wrench", "wire", "circuit", "engine", "battery", "tool"],
        "reading_text": [
            "Sofía is a first-year technical student. Every day, she learns about tools and safety rules in the workshop.",
            "In class, she reads a short text about a mechanic who checks engines, changes oil, and uses different tools.",
            "After reading, she identifies key words and explains what each tool is used for."
        ],
    },
    {
        "course_name": "3°A — Mecánica Industrial",
        "course_key": "3A-industrial",
        "course_label": "3°A — Mecánica Industrial",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_industrial.html",
        "relative_file": "3ro-medio/3A-industrial/u1/Clase_2_U1_3roA_Industrial.html",
        "vocab_review": ["lathe", "welder", "caliper", "micrometer", "blueprint", "tolerance", "steel", "clamp"],
        "reading_text": [
            "Martín begins his day in an industrial workshop by reviewing a blueprint and preparing the machine area.",
            "He operates a lathe, measures dimensions with a caliper, and checks tolerance using a micrometer.",
            "At the end, he records results and reports quality issues to his supervisor."
        ],
    },
    {
        "course_name": "3°B — Mecánica Automotriz",
        "course_key": "3B-automotriz",
        "course_label": "3°B — Mecánica Automotriz",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_automotriz.html",
        "relative_file": "3ro-medio/3B-automotriz/u1/Clase_2_U1_3roB_Automotriz.html",
        "vocab_review": ["engine", "brake pad", "oil filter", "diagnostic scanner", "radiator", "battery", "coolant", "wrench"],
        "reading_text": [
            "Camila works in an automotive workshop and starts with a quick vehicle inspection.",
            "She checks engine sounds, scans error codes, and inspects brake pads and coolant levels.",
            "Before finishing, she explains to the client what repairs are necessary."
        ],
    },
    {
        "course_name": "3°C — Electricidad",
        "course_key": "3C-electricidad",
        "course_label": "3°C — Electricidad",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_electricidad.html",
        "relative_file": "3ro-medio/3C-electricidad/u1/Clase_2_U1_3roC_Electricidad.html",
        "vocab_review": ["wire", "circuit", "breaker", "panel", "outlet", "multimeter", "transformer", "grounding"],
        "reading_text": [
            "Nicolás works as an electrician trainee in a building project.",
            "He installs wire and conduit, checks circuits with a multimeter, and verifies panel safety.",
            "Finally, he tests outlet voltage and confirms grounding in all areas."
        ],
    },
    {
        "course_name": "3°D — Gráfica",
        "course_key": "3D-grafica",
        "course_label": "3°D — Gráfica",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_grafica.html",
        "relative_file": "3ro-medio/3D-grafica/u1/Clase_2_U1_3roD_Grafica.html",
        "vocab_review": ["ink", "press", "CMYK", "prepress", "resolution", "cutter", "laminator", "binding"],
        "reading_text": [
            "Fernanda starts in prepress by checking file resolution and color profiles.",
            "She prepares ink for the press, verifies CMYK quality, and checks test prints.",
            "Later, she finishes products with a cutter and laminator before binding."
        ],
    },
    {
        "course_name": "3°E — Electrónica",
        "course_key": "3E-electronica",
        "course_label": "3°E — Electrónica",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "3ro Medio" / "Unidad 1" / "planificacion_u1_electronica.html",
        "relative_file": "3ro-medio/3E-electronica/u1/Clase_2_U1_3roE_Electronica.html",
        "vocab_review": ["resistor", "capacitor", "transistor", "PCB", "oscilloscope", "diode", "signal", "voltage"],
        "reading_text": [
            "Ignacio assembles a small circuit on a PCB during electronics lab.",
            "He solders components, checks continuity, and observes waveforms with an oscilloscope.",
            "Then he records voltage and signal results for the final report."
        ],
    },
    {
        "course_name": "4°A — Mecánica Industrial",
        "course_key": "4A-industrial",
        "course_label": "4°A — Mecánica Industrial",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_industrial.html",
        "relative_file": "4to-medio/4A-industrial/u1/Clase_2_U1_4toA_Industrial.html",
        "vocab_review": ["CNC machine", "milling", "hydraulic press", "quality control", "tolerance", "technical drawing"],
        "reading_text": [
            "Paulo followed a career path from technical school to industrial maintenance specialist.",
            "He learned CNC programming, preventive maintenance, and quality control in a metal factory.",
            "English helped him read technical documentation and apply international standards."
        ],
    },
    {
        "course_name": "4°B — Mecánica Automotriz",
        "course_key": "4B-automotriz",
        "course_label": "4°B — Mecánica Automotriz",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_automotriz.html",
        "relative_file": "4to-medio/4B-automotriz/u1/Clase_2_U1_4toB_Automotriz.html",
        "vocab_review": ["engine diagnostics", "OBD scanner", "fuel injection", "hybrid system", "torque", "alignment"],
        "reading_text": [
            "Daniela started as an apprentice and became an automotive diagnostics technician.",
            "She specialized in hybrid systems and uses OBD tools to solve complex faults.",
            "Her English skills improved because she regularly reads software updates and service manuals."
        ],
    },
    {
        "course_name": "4°C — Electricidad",
        "course_key": "4C-electricidad",
        "course_label": "4°C — Electricidad",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_electricidad.html",
        "relative_file": "4to-medio/4C-electricidad/u1/Clase_2_U1_4toC_Electricidad.html",
        "vocab_review": ["three-phase power", "circuit breaker", "transformer", "voltage regulator", "switchgear", "load calculation"],
        "reading_text": [
            "Rocío built her career through internships in residential and industrial electrical projects.",
            "She learned load calculation, transformer maintenance, and protection system testing.",
            "English was key to understanding electrical codes and technical documentation."
        ],
    },
    {
        "course_name": "4°E — Electrónica",
        "course_key": "4E-electronica",
        "course_label": "4°E — Electrónica",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "plan_path": ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "4to Medio" / "Unidad 1" / "planificacion_u1_electronica.html",
        "relative_file": "4to-medio/4E-electronica/u1/Clase_2_U1_4toE_Electronica.html",
        "vocab_review": ["microcontroller", "firmware", "IoT sensor", "embedded system", "signal processing", "PCB design"],
        "reading_text": [
            "Sebastián studied electronics and then worked in IoT device maintenance.",
            "He programs microcontrollers, updates firmware, and validates embedded systems with lab tools.",
            "Reading English datasheets allowed him to solve advanced technical problems."
        ],
    },
]


def clean_text(text):
    return re.sub(r"\s+", " ", text or "").strip()


def extract_class2_data(plan_path):
    html = plan_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    class2 = None
    for card in soup.select("div.clase-card"):
        num = card.select_one(".clase-num")
        if num and "Clase 2" in clean_text(num.get_text()):
            class2 = card
            break

    if not class2:
        return {
            "objective": "Desarrollar comprensión lectora y uso de vocabulario técnico en contexto profesional.",
            "inicio": ["Warm-up de vocabulario técnico.", "Predicciones sobre el texto."],
            "desarrollo": ["Lectura guiada.", "Preguntas de comprensión.", "Práctica oral en parejas."],
            "cierre": ["Resumen breve de aprendizajes.", "Reflexión final."],
        }

    objective = ""
    obj = class2.select_one(".objetivo")
    if obj:
        objective = clean_text(obj.get_text(" "))
        objective = objective.replace("Objetivo de la clase (Bloom):", "").replace("Objetivo de la clase:", "").strip()

    def phase_items(keyword):
        for phase in class2.select("div.fase"):
            t = phase.select_one(".fase-title")
            if not t or keyword.lower() not in clean_text(t.get_text()).lower():
                continue
            content = phase.select_one(".fase-content")
            if not content:
                return []
            return [clean_text(li.get_text(" ")) for li in content.select("li") if clean_text(li.get_text(" "))]
        return []

    return {
        "objective": objective,
        "inicio": phase_items("INICIO"),
        "desarrollo": phase_items("DESARROLLO"),
        "cierre": phase_items("CIERRE"),
    }


def build_vocab_html(vocab_words):
    cards = []
    for w in vocab_words:
        cards.append(
            f"""
            <div class=\"vocab-card\" onclick=\"this.classList.toggle('revealed')\">
                <div class=\"word\">{w}</div>
                <div class=\"meaning\">Repasar definición en clase</div>
                <div class=\"hint\">👆 clic para ver</div>
            </div>
            """
        )
    return "".join(cards)


def build_question_items():
    return """
    <ol>
        <li>What is the main job/task described in the text?</li>
        <li>Which technical tools or systems are mentioned?</li>
        <li>What sequence of actions appears in the routine?</li>
        <li>Why is English useful in this professional context?</li>
        <li>What challenge does the professional face and how is it solved?</li>
        <li>What skill from this text is relevant for your own future career?</li>
    </ol>
    """


def build_tf_block():
    return """
    <div class=\"quiz-item\"><p>1. The text describes professional technical tasks.</p><div class=\"quiz-options\"><button class=\"quiz-btn\" onclick=\"checkAnswer(this,true)\">TRUE</button><button class=\"quiz-btn\" onclick=\"checkAnswer(this,false)\">FALSE</button></div></div>
    <div class=\"quiz-item\"><p>2. English is not necessary in technical jobs.</p><div class=\"quiz-options\"><button class=\"quiz-btn\" onclick=\"checkAnswer(this,false)\">TRUE</button><button class=\"quiz-btn\" onclick=\"checkAnswer(this,true)\">FALSE</button></div></div>
    <div class=\"quiz-item\"><p>3. The routine includes specific tools and procedures.</p><div class=\"quiz-options\"><button class=\"quiz-btn\" onclick=\"checkAnswer(this,true)\">TRUE</button><button class=\"quiz-btn\" onclick=\"checkAnswer(this,false)\">FALSE</button></div></div>
    """


def build_class2_html(course, parsed):
    vocab_html = build_vocab_html(course["vocab_review"])
    reading_html = "".join(f"<p>{p}</p>" for p in course["reading_text"])
    init_list = "".join(f"<li>{i}</li>" for i in (parsed["inicio"][:4] or ["Activación y prelectura."]))
    dev_list = "".join(f"<li>{i}</li>" for i in (parsed["desarrollo"][:6] or ["Lectura guiada y comprensión."]))
    close_list = "".join(f"<li>{i}</li>" for i in (parsed["cierre"][:4] or ["Cierre y reflexión."]))

    return f"""<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Clase 2 — {course['course_label']}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Inter', sans-serif; background: #f0f2f5; color: #333; line-height: 1.7; }}
        .header {{ background: linear-gradient(135deg, #0d47a1, #1565c0); color: white; padding: 34px 20px; text-align: center; }}
        .header h1 {{ font-size: 1.85em; margin-bottom: 5px; }}
        .header .meta {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 10px; }}
        .header .meta span {{ background: rgba(255,255,255,0.2); padding: 5px 14px; border-radius: 20px; font-size: 0.85em; }}
        .container {{ max-width: 930px; margin: 24px auto; padding: 0 15px; }}
        .card {{ background: white; border-radius: 12px; padding: 20px; margin-bottom: 18px; box-shadow: 0 2px 10px rgba(0,0,0,0.06); }}
        .card h3 {{ color: #1565c0; margin-bottom: 8px; }}
        ul, ol {{ margin-left: 20px; }}
        li {{ margin-bottom: 7px; }}
        .section-title {{ color: white; font-weight: 600; padding: 10px 14px; border-radius: 8px; margin-bottom: 10px; display: inline-block; }}
        .inicio {{ background: #2e7d32; }}
        .desarrollo {{ background: #1565c0; }}
        .cierre {{ background: #6a1b9a; }}

        .vocab-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); gap: 10px; margin-top: 10px; }}
        .vocab-card {{ background: #e3f2fd; border: 2px solid #90caf9; border-radius: 10px; padding: 12px; text-align: center; cursor: pointer; }}
        .vocab-card .word {{ font-weight: 700; color: #0d47a1; }}
        .vocab-card .meaning {{ font-size: 0.8em; color: #666; margin-top: 4px; display: none; }}
        .vocab-card.revealed .meaning {{ display: block; }}
        .vocab-card .hint {{ font-size: 0.72em; color: #888; margin-top: 4px; }}
        .vocab-card.revealed .hint {{ display: none; }}

        .reading-box {{ background: #fafafa; border: 1px solid #e0e0e0; border-radius: 10px; padding: 14px; margin-top: 10px; }}
        .task-box {{ background: #f7f7f7; border: 1px solid #e0e0e0; border-radius: 10px; padding: 14px; margin-top: 10px; }}
        .quiz-item {{ background: #f7f7f7; border: 1px solid #e0e0e0; border-radius: 8px; padding: 12px; margin-bottom: 10px; }}
        .quiz-options {{ display: flex; gap: 10px; margin-top: 8px; }}
        .quiz-btn {{ padding: 7px 14px; border-radius: 8px; border: 2px solid #e0e0e0; background: white; cursor: pointer; }}
        .quiz-btn.correct {{ border-color: #2e7d32; background: #e8f5e9; color: #2e7d32; font-weight: 700; }}
        .quiz-btn.incorrect {{ border-color: #c62828; background: #ffebee; color: #c62828; }}

        .ticket-input {{ width: 100%; padding: 9px 12px; border: 1px solid #ddd; border-radius: 8px; margin-top: 8px; }}
        .score {{ font-weight: 700; color: #1565c0; }}
    </style>
</head>
<body>
<div class=\"header\">
    <h1>CLASS 2 — {course['course_label'].upper()}</h1>
    <div class=\"meta\">
        <span>📘 OA1 · OA3</span>
        <span>⏱ 90 min</span>
        <span>🧭 Guía de estudiante completa</span>
    </div>
</div>

<div class=\"container\">
    <div class=\"card\"><h3>🎯 Objetivo de la clase</h3><p>{parsed['objective']}</p></div>

    <div class=\"card\">
        <div class=\"section-title inicio\">Inicio (15 min)</div>
        <ul>{init_list}</ul>
    </div>

    <div class=\"card\">
        <div class=\"section-title desarrollo\">Desarrollo (60 min)</div>
        <ul>{dev_list}</ul>

        <h3 style=\"margin-top:14px;\">📖 Activity 1 — Vocabulary Review</h3>
        <div class=\"vocab-grid\">{vocab_html}</div>

        <h3 style=\"margin-top:14px;\">📚 Activity 2 — Reading</h3>
        <div class=\"reading-box\">{reading_html}</div>

        <h3 style=\"margin-top:14px;\">📝 Activity 3 — Comprehension Questions</h3>
        <div class=\"task-box\">{build_question_items()}</div>

        <h3 style=\"margin-top:14px;\">📊 Activity 4 — Task / Tool / Time Table</h3>
        <div class=\"task-box\">
            <table style=\"width:100%; border-collapse: collapse;\">
                <tr><th style=\"border:1px solid #ddd; padding:8px;\">Task</th><th style=\"border:1px solid #ddd; padding:8px;\">Tool/System</th><th style=\"border:1px solid #ddd; padding:8px;\">Time of day</th></tr>
                <tr><td style=\"border:1px solid #ddd; padding:8px;\">&nbsp;</td><td style=\"border:1px solid #ddd; padding:8px;\">&nbsp;</td><td style=\"border:1px solid #ddd; padding:8px;\">&nbsp;</td></tr>
                <tr><td style=\"border:1px solid #ddd; padding:8px;\">&nbsp;</td><td style=\"border:1px solid #ddd; padding:8px;\">&nbsp;</td><td style=\"border:1px solid #ddd; padding:8px;\">&nbsp;</td></tr>
                <tr><td style=\"border:1px solid #ddd; padding:8px;\">&nbsp;</td><td style=\"border:1px solid #ddd; padding:8px;\">&nbsp;</td><td style=\"border:1px solid #ddd; padding:8px;\">&nbsp;</td></tr>
            </table>
        </div>

        <h3 style=\"margin-top:14px;\">✅ Activity 5 — True/False Check</h3>
        {build_tf_block()}

        <h3 style=\"margin-top:14px;\">🗣 Activity 6 — Speaking Frames</h3>
        <div class=\"task-box\">
            <p><strong>Use these frames in pairs:</strong></p>
            <ul>
                <li>"Every day, the technician checks ..."</li>
                <li>"First ..., then ..., finally ..."</li>
                <li>"The most important skill is ... because ..."</li>
            </ul>
        </div>
    </div>

    <div class=\"card\">
        <div class=\"section-title cierre\">Cierre (15 min)</div>
        <ul>{close_list}</ul>
        <h3 style=\"margin-top:10px;\">🎫 Exit Ticket</h3>
        <input class=\"ticket-input\" placeholder=\"Write 3 new words from today + meaning\" />
        <input class=\"ticket-input\" placeholder=\"Reflection: What was the most useful skill in this lesson?\" />
        <p class=\"score\" id=\"totalScore\" style=\"margin-top:8px;\">0 / 3 puntos</p>
    </div>
</div>

<script>
    let score = 0;
    function checkAnswer(btn, isCorrect) {{
        const buttons = btn.parentElement.querySelectorAll('.quiz-btn');
        buttons.forEach(b => b.disabled = true);
        if (isCorrect) {{ btn.classList.add('correct'); score++; }}
        else {{ btn.classList.add('incorrect'); buttons.forEach(b => {{ if (b !== btn) b.classList.add('correct'); }}); }}
        document.getElementById('totalScore').textContent = score + ' / 3 puntos';
    }}
</script>
</body>
</html>
"""


def update_index():
    index_path = SITE / "index.html"
    soup = BeautifulSoup(index_path.read_text(encoding="utf-8"), "html.parser")

    by_course = {c["course_name"]: c for c in COURSES}

    for section in soup.select(".course-section"):
        h3 = section.select_one(".course-header h3")
        if not h3:
            continue
        course_name = h3.get_text(strip=True)
        if course_name not in by_course:
            continue

        course = by_course[course_name]
        unit_classes = section.select_one(".unit-group .unit-classes")
        if not unit_classes:
            continue

        existing = list(unit_classes.select("a.class-link"))
        has_class2 = any((a.get("data-progress-id") or "").endswith("/Clase_2") for a in existing)
        if has_class2:
            continue

        class2_link = (
            f"<a class=\"class-link\" href=\"{course['relative_file']}\" data-progress-id=\"{course['course_key']}/u1/Clase_2\">"
            f"<span class=\"num\">2</span>"
            f"<span class=\"title\">Clase 2 — Comprensión lectora y práctica guiada</span>"
            f"<span class=\"tag tag-clase\">Clase</span>"
            f"<span class=\"status-badge status-pending\" data-status-badge>⏳ Pendiente</span>"
            f"</a>"
        )
        unit_classes.append(BeautifulSoup(class2_link, "html.parser"))

    index_path.write_text(str(soup), encoding="utf-8")


def update_progress():
    progress_path = SITE / "progress.json"
    data = json.loads(progress_path.read_text(encoding="utf-8")) if progress_path.exists() else {"classes": {}}
    data["lastUpdated"] = str(date.today())

    for c in COURSES:
        key = f"{c['course_key']}/u1/Clase_2"
        data.setdefault("classes", {})[key] = {
            "status": "pending",
            "title": "Clase 2 — Comprensión lectora y práctica guiada",
        }

    progress_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    for c in COURSES:
        parsed = extract_class2_data(c["plan_path"])
        out = SITE / c["relative_file"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build_class2_html(c, parsed), encoding="utf-8")

    update_index()
    update_progress()


if __name__ == "__main__":
    main()
