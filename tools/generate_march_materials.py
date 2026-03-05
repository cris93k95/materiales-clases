import json
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
        "relative_file": "1ro-medio/lu-ju/u1/Clase_1_U1_1ro_LuJu.html",
        "oa": "OA9",
        "objective": "Identificar el nivel de competencia en inglés de los estudiantes mediante una evaluación diagnóstica integrada con contexto técnico-profesional.",
        "warmup": [
            "Presentación del docente en inglés y contexto del curso técnico-profesional.",
            "Preguntas breves: name, age, interests, preferred specialty.",
            "Lluvia de ideas: palabras en inglés que ya conocen del mundo técnico."
        ],
        "vocab": [
            ("hammer", "martillo"), ("screwdriver", "destornillador"), ("wrench", "llave"),
            ("wire", "cable"), ("circuit", "circuito"), ("printer", "impresora"),
            ("engine", "motor"), ("brake", "freno"), ("panel", "panel"),
            ("switch", "interruptor"), ("battery", "batería"), ("tool", "herramienta")
        ],
        "matching": [
            ("Used to hit nails", "hammer"),
            ("Used to tighten bolts", "wrench"),
            ("Carries electricity", "wire"),
            ("Electrical path", "circuit"),
            ("Stores electrical energy", "battery")
        ],
        "reading_title": "Carlos at the Workshop",
        "reading_paragraphs": [
            "Carlos works at a small automotive workshop in Santiago. Every morning, he checks the engine and prepares his tools.",
            "He changes oil, inspects the brakes, and uses a wrench and screwdriver to adjust parts. He also checks the battery and electrical circuit.",
            "At the end of the day, Carlos writes a short report and cleans the work area. Technical English helps him read manuals and safety instructions."
        ],
        "true_false": [
            ("Carlos works in a workshop in Santiago.", True),
            ("He repairs computers all day.", False),
            ("He checks brakes and oil.", True),
            ("English is not useful for manuals.", False),
            ("Carlos uses technical tools at work.", True)
        ],
        "reflection": "Why is English important for your future technical career?"
    },
    {
        "course_name": "3°A — Mecánica Industrial",
        "course_key": "3A-industrial",
        "course_label": "3°A — Mecánica Industrial",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "relative_file": "3ro-medio/3A-industrial/u1/Clase_1_U1_3roA_Industrial.html",
        "oa": "OA1",
        "objective": "Identificar vocabulario técnico básico en inglés relacionado con la especialidad de Mecánica Industrial mediante la exploración de textos e imágenes del campo profesional.",
        "warmup": [
            "What English words do you already know from your specialty?",
            "Observe workshop images and identify tools/processes.",
            "Share one industrial task you know in Spanish and English."
        ],
        "vocab": [
            ("lathe", "torno"), ("mill", "fresadora"), ("drill press", "taladro de banco"),
            ("welder", "soldadora"), ("caliper", "calibrador"), ("micrometer", "micrómetro"),
            ("file", "lima"), ("grinding wheel", "rueda de esmeril"), ("vise", "tornillo de banco"),
            ("clamp", "abrazadera"), ("blueprint", "plano técnico"), ("tolerance", "tolerancia"),
            ("steel", "acero"), ("aluminum", "aluminio")
        ],
        "matching": [
            ("Machine for cylindrical parts", "lathe"),
            ("Measures very small distances", "micrometer"),
            ("Technical drawing", "blueprint"),
            ("Strong structural metal", "steel"),
            ("Joins metal pieces", "welder")
        ],
        "reading_title": "A Day in an Industrial Workshop",
        "reading_paragraphs": [
            "In the morning, Diego checks the blueprint and prepares steel and aluminum pieces.",
            "He operates the lathe and then measures parts with a caliper and micrometer to verify tolerance.",
            "Later, he uses a welder and finishes the part with a file. English helps him follow machine manuals safely."
        ],
        "true_false": [
            ("Diego checks a blueprint before machining.", True),
            ("A micrometer is used for painting walls.", False),
            ("Tolerance is important in precision work.", True),
            ("Lathe and welder are workshop tools.", True),
            ("English manuals are useless in workshops.", False)
        ],
        "reflection": "Why is technical English important in Industrial Mechanics?"
    },
    {
        "course_name": "3°B — Mecánica Automotriz",
        "course_key": "3B-automotriz",
        "course_label": "3°B — Mecánica Automotriz",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "relative_file": "3ro-medio/3B-automotriz/u1/Clase_1_U1_3roB_Automotriz.html",
        "oa": "OA1",
        "objective": "Identificar vocabulario técnico básico en inglés relacionado con la especialidad de Mecánica Automotriz mediante la exploración de textos e imágenes del campo profesional.",
        "warmup": ["Brainstorm automotive words in English.", "Identify parts in workshop images.", "Share daily tasks of a mechanic."],
        "vocab": [
            ("engine", "motor"), ("brake pad", "pastilla de freno"), ("transmission", "transmisión"),
            ("coolant", "refrigerante"), ("wrench", "llave"), ("jack", "gata"),
            ("spark plug", "bujía"), ("oil filter", "filtro de aceite"), ("radiator", "radiador"),
            ("exhaust", "escape"), ("tire", "neumático"), ("battery", "batería"),
            ("alternator", "alternador"), ("diagnostic scanner", "escáner de diagnóstico")
        ],
        "matching": [
            ("Main power unit of a car", "engine"),
            ("Filters oil impurities", "oil filter"),
            ("Produces electric current", "alternator"),
            ("Reads fault codes", "diagnostic scanner"),
            ("Part used for stopping", "brake pad")
        ],
        "reading_title": "A Day in an Automotive Workshop",
        "reading_paragraphs": [
            "Valentina starts by checking the engine and battery in each vehicle.",
            "She changes the oil filter, inspects brake pads, and uses a diagnostic scanner for error codes.",
            "Before finishing, she verifies coolant and tire condition. English helps her use technical manuals and software."
        ],
        "true_false": [
            ("A diagnostic scanner reads vehicle fault codes.", True),
            ("Brake pads are part of the audio system.", False),
            ("Coolant helps regulate engine temperature.", True),
            ("Alternator is related to electric generation.", True),
            ("Mechanics never need technical English.", False)
        ],
        "reflection": "How does English help in automotive diagnostics?"
    },
    {
        "course_name": "3°C — Electricidad",
        "course_key": "3C-electricidad",
        "course_label": "3°C — Electricidad",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "relative_file": "3ro-medio/3C-electricidad/u1/Clase_1_U1_3roC_Electricidad.html",
        "oa": "OA1",
        "objective": "Identificar vocabulario técnico básico en inglés relacionado con la especialidad de Electricidad mediante la exploración de textos e imágenes del campo profesional.",
        "warmup": ["Brainstorm electric words.", "Identify components in lab images.", "Name one safety rule in English."],
        "vocab": [
            ("wire", "cable"), ("circuit", "circuito"), ("breaker", "disyuntor"), ("panel", "panel"),
            ("switch", "interruptor"), ("outlet", "enchufe"), ("voltage", "voltaje"), ("current", "corriente"),
            ("resistance", "resistencia"), ("multimeter", "multímetro"), ("pliers", "alicate"),
            ("conduit", "conduit/tubo"), ("transformer", "transformador"), ("grounding", "puesta a tierra")
        ],
        "matching": [
            ("Measures voltage and current", "multimeter"),
            ("Protects electrical circuits", "breaker"),
            ("Converts electrical energy levels", "transformer"),
            ("Connection point for devices", "outlet"),
            ("Safety connection to earth", "grounding")
        ],
        "reading_title": "A Day as an Electrician",
        "reading_paragraphs": [
            "Tomás installs conduit and wire in a new building project.",
            "He checks each circuit with a multimeter, then verifies the breaker panel and outlet connections.",
            "Before leaving, he confirms grounding and transformer settings. English helps him read international safety labels."
        ],
        "true_false": [
            ("A multimeter is used for electrical measurements.", True),
            ("Grounding is a safety procedure.", True),
            ("Breaker protects against overcurrent.", True),
            ("Voltage and current mean exactly the same thing.", False),
            ("Electricians never read manuals in English.", False)
        ],
        "reflection": "Why is English useful for electrical safety and standards?"
    },
    {
        "course_name": "3°D — Gráfica",
        "course_key": "3D-grafica",
        "course_label": "3°D — Gráfica",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "relative_file": "3ro-medio/3D-grafica/u1/Clase_1_U1_3roD_Grafica.html",
        "oa": "OA1",
        "objective": "Identificar vocabulario técnico básico en inglés relacionado con la especialidad de Gráfica mediante la exploración de textos e imágenes del campo profesional.",
        "warmup": ["Brainstorm words from print shop.", "Identify printing process steps.", "Discuss CMYK meaning."],
        "vocab": [
            ("ink", "tinta"), ("paper", "papel"), ("plate", "plancha"), ("press", "prensa"),
            ("offset", "offset"), ("digital printing", "impresión digital"), ("binding", "encuadernación"),
            ("color profile", "perfil de color"), ("CMYK", "cian-magenta-amarillo-negro"),
            ("resolution", "resolución"), ("prepress", "preprensa"), ("cutter", "guillotina"),
            ("laminator", "laminadora"), ("densitometer", "densitómetro")
        ],
        "matching": [
            ("Color model for printing", "CMYK"),
            ("Stage before printing", "prepress"),
            ("Machine that cuts paper", "cutter"),
            ("Adds protective film", "laminator"),
            ("Measures ink density", "densitometer")
        ],
        "reading_title": "A Day in a Print Shop",
        "reading_paragraphs": [
            "Paula prepares files in prepress and checks color profile settings.",
            "She operates the press, controls ink levels, and verifies CMYK quality with a densitometer.",
            "Finally, she uses the cutter and laminator for finishing. English is key for software and machine settings."
        ],
        "true_false": [
            ("CMYK is used in printing color processes.", True),
            ("Prepress happens after binding.", False),
            ("A cutter is for paper trimming.", True),
            ("Densitometer checks ink quality.", True),
            ("Printing software never uses English terms.", False)
        ],
        "reflection": "How does English support quality control in print production?"
    },
    {
        "course_name": "3°E — Electrónica",
        "course_key": "3E-electronica",
        "course_label": "3°E — Electrónica",
        "unit_title": "Unidad 1 — Technical Skills & Career Paths",
        "relative_file": "3ro-medio/3E-electronica/u1/Clase_1_U1_3roE_Electronica.html",
        "oa": "OA1",
        "objective": "Identificar vocabulario técnico básico en inglés relacionado con la especialidad de Electrónica mediante la exploración de textos e imágenes del campo profesional.",
        "warmup": ["Brainstorm electronics words.", "Identify components in circuit images.", "Describe one lab task."],
        "vocab": [
            ("resistor", "resistor"), ("capacitor", "capacitor"), ("transistor", "transistor"),
            ("LED", "LED"), ("PCB", "placa PCB"), ("soldering iron", "cautín"),
            ("oscilloscope", "osciloscopio"), ("diode", "diodo"), ("integrated circuit", "circuito integrado"),
            ("sensor", "sensor"), ("amplifier", "amplificador"), ("frequency", "frecuencia"),
            ("signal", "señal"), ("voltage", "voltaje")
        ],
        "matching": [
            ("Tool to solder components", "soldering iron"),
            ("Measures waveforms", "oscilloscope"),
            ("Light-emitting component", "LED"),
            ("Base board for circuits", "PCB"),
            ("One-way current device", "diode")
        ],
        "reading_title": "A Day in an Electronics Lab",
        "reading_paragraphs": [
            "Matías starts by checking a PCB and selecting components like resistors and capacitors.",
            "He solders parts with a soldering iron and verifies signals with an oscilloscope.",
            "At the end, he tests voltage and frequency. English helps him read datasheets and manuals."
        ],
        "true_false": [
            ("An oscilloscope displays signal waveforms.", True),
            ("A diode allows current in both directions equally.", False),
            ("PCB is the base of many electronic circuits.", True),
            ("Soldering iron is used in electronics assembly.", True),
            ("Datasheets are usually written in Spanish only.", False)
        ],
        "reflection": "Why is English essential in electronics documentation?"
    },
    {
        "course_name": "4°A — Mecánica Industrial",
        "course_key": "4A-industrial",
        "course_label": "4°A — Mecánica Industrial",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "relative_file": "4to-medio/4A-industrial/u1/Clase_1_U1_4toA_Industrial.html",
        "oa": "OA1",
        "objective": "Identificar vocabulario técnico avanzado en inglés relacionado con Mecánica Industrial y describir metas profesionales a corto y largo plazo.",
        "warmup": ["Discuss career goals after graduation.", "Analyze international industrial jobs.", "Share one future specialization."],
        "vocab": [
            ("CNC machine", "máquina CNC"), ("lathe", "torno"), ("milling", "fresado"),
            ("hydraulic press", "prensa hidráulica"), ("welding (MIG/TIG)", "soldadura MIG/TIG"),
            ("quality control", "control de calidad"), ("tolerance", "tolerancia"), ("technical drawing", "dibujo técnico")
        ],
        "matching": [
            ("Automated precision machining", "CNC machine"),
            ("Process to join metals", "welding (MIG/TIG)"),
            ("Verification of product standards", "quality control"),
            ("Engineering blueprint", "technical drawing"),
            ("Allowed dimensional variation", "tolerance")
        ],
        "reading_title": "Industrial Mechanics in the Age of Automation",
        "reading_paragraphs": [
            "Modern workshops use CNC machines and automation to improve productivity.",
            "Technicians now combine traditional skills like lathe operation with digital control and quality control systems.",
            "English is essential to understand manuals, international standards, and software interfaces used in smart factories."
        ],
        "true_false": [
            ("CNC technology is part of modern industrial workshops.", True),
            ("Quality control is irrelevant in production.", False),
            ("Technical drawing helps manufacturing accuracy.", True),
            ("Automation removes the need for all human skills.", False),
            ("English supports understanding of international standards.", True)
        ],
        "reflection": "Which advanced skill do you need for Industry 4.0 and why?"
    },
    {
        "course_name": "4°B — Mecánica Automotriz",
        "course_key": "4B-automotriz",
        "course_label": "4°B — Mecánica Automotriz",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "relative_file": "4to-medio/4B-automotriz/u1/Clase_1_U1_4toB_Automotriz.html",
        "oa": "OA1",
        "objective": "Identificar vocabulario técnico avanzado en inglés relacionado con Mecánica Automotriz y describir metas profesionales a corto y largo plazo.",
        "warmup": ["Discuss future jobs in automotive sector.", "Identify new technologies in workshop photos.", "Share goals for specialization."],
        "vocab": [
            ("engine diagnostics", "diagnóstico de motor"), ("OBD scanner", "escáner OBD"),
            ("fuel injection", "inyección de combustible"), ("turbocharger", "turbocargador"),
            ("hybrid system", "sistema híbrido"), ("torque", "torque"),
            ("horsepower", "caballos de fuerza"), ("alignment", "alineación")
        ],
        "matching": [
            ("Reads vehicle diagnostic codes", "OBD scanner"),
            ("Force that rotates engine parts", "torque"),
            ("Power output indicator", "horsepower"),
            ("System combining electric and fuel power", "hybrid system"),
            ("Adjusts wheel angles", "alignment")
        ],
        "reading_title": "The Modern Automotive Technician",
        "reading_paragraphs": [
            "Today’s mechanics use diagnostics software and OBD scanners for faster, accurate repairs.",
            "They must understand hybrid systems, electronic control units, and fuel injection technologies.",
            "Technical English is necessary to read manufacturer updates, troubleshooting guides, and international certifications."
        ],
        "true_false": [
            ("OBD scanner is used for diagnostics.", True),
            ("Hybrid systems combine different power sources.", True),
            ("Alignment refers only to painting cars.", False),
            ("Torque is a key mechanical concept.", True),
            ("Automotive software terms are often in English.", True)
        ],
        "reflection": "What automotive technology do you need to master for your career?"
    },
    {
        "course_name": "4°C — Electricidad",
        "course_key": "4C-electricidad",
        "course_label": "4°C — Electricidad",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "relative_file": "4to-medio/4C-electricidad/u1/Clase_1_U1_4toC_Electricidad.html",
        "oa": "OA1",
        "objective": "Identificar vocabulario técnico avanzado en inglés relacionado con Electricidad y describir metas profesionales a corto y largo plazo.",
        "warmup": ["Discuss career goals in electrical field.", "Analyze modern electrical systems.", "Share one specialization pathway."],
        "vocab": [
            ("three-phase power", "energía trifásica"), ("circuit breaker", "interruptor automático"),
            ("transformer", "transformador"), ("voltage regulator", "regulador de voltaje"),
            ("conduit", "conduit/tubería"), ("switchgear", "equipos de maniobra"),
            ("grounding", "puesta a tierra"), ("load calculation", "cálculo de carga")
        ],
        "matching": [
            ("Converts electrical voltage", "transformer"),
            ("Protects circuit from overload", "circuit breaker"),
            ("Ensures electrical safety to earth", "grounding"),
            ("System with three alternating currents", "three-phase power"),
            ("Determines required electrical demand", "load calculation")
        ],
        "reading_title": "The Professional Electrician in 2026",
        "reading_paragraphs": [
            "Electricians now work in residential, commercial, and industrial projects with digital monitoring systems.",
            "They must handle three-phase installations, switchgear, and load calculation for safe operation.",
            "English helps them understand technical standards, renewable-energy manuals, and smart-home systems."
        ],
        "true_false": [
            ("Three-phase power is used in many industrial systems.", True),
            ("Grounding is optional and never related to safety.", False),
            ("Load calculation is part of electrical design.", True),
            ("Switchgear is related to electrical control and protection.", True),
            ("English is useful for technical standards.", True)
        ],
        "reflection": "Why is advanced English important in modern electrical careers?"
    },
    {
        "course_name": "4°E — Electrónica",
        "course_key": "4E-electronica",
        "course_label": "4°E — Electrónica",
        "unit_title": "Unidad 1 — Industry & Innovation",
        "relative_file": "4to-medio/4E-electronica/u1/Clase_1_U1_4toE_Electronica.html",
        "oa": "OA1",
        "objective": "Identificar vocabulario técnico avanzado en inglés relacionado con Electrónica y describir metas profesionales a corto y largo plazo.",
        "warmup": ["Discuss digital-age electronics careers.", "Identify advanced devices and tools.", "Share personal professional goal."],
        "vocab": [
            ("microcontroller", "microcontrolador"), ("PCB design", "diseño PCB"),
            ("firmware", "firmware"), ("oscilloscope", "osciloscopio"),
            ("soldering station", "estación de soldadura"), ("IoT sensor", "sensor IoT"),
            ("embedded system", "sistema embebido"), ("signal processing", "procesamiento de señal")
        ],
        "matching": [
            ("Brain of many electronic devices", "microcontroller"),
            ("Software embedded in hardware", "firmware"),
            ("Captures physical data for connected systems", "IoT sensor"),
            ("Integrated hardware-software platform", "embedded system"),
            ("Analyzes and modifies electronic signals", "signal processing")
        ],
        "reading_title": "Electronics Technicians in the Digital Age",
        "reading_paragraphs": [
            "Electronics technicians work in PCB manufacturing, IoT development, and smart-device maintenance.",
            "They use oscilloscopes, soldering stations, and microcontrollers to design and troubleshoot systems.",
            "English is necessary for datasheets, firmware documentation, and global technology standards."
        ],
        "true_false": [
            ("Microcontrollers are used in many embedded systems.", True),
            ("Firmware is unrelated to hardware.", False),
            ("IoT sensors connect data to digital networks.", True),
            ("Signal processing is part of electronics careers.", True),
            ("English is useful for datasheet reading.", True)
        ],
        "reflection": "What digital electronics skill is most important for your future?"
    },
]


def build_matching_html(matching):
    left = []
    right = []
    for idx, (desc, word) in enumerate(matching, start=1):
        key = chr(64 + idx)
        left.append(f"<div class=\"match-item\" data-match=\"{key}\" onclick=\"selectMatch(this,'left')\">{desc}</div>")
        right.append(f"<div class=\"match-item\" data-match=\"{key}\" onclick=\"selectMatch(this,'right')\">{word}</div>")
    return "".join(left), "".join(right)


def build_tf_html(tf_questions):
    blocks = []
    for idx, (statement, answer_true) in enumerate(tf_questions, start=1):
        true_correct = "true" if answer_true else "false"
        false_correct = "false" if answer_true else "true"
        blocks.append(
            f"""
            <div class=\"quiz-item\">
                <p>{idx}. {statement}</p>
                <div class=\"quiz-options\">
                    <button class=\"quiz-btn\" onclick=\"checkAnswer(this,{true_correct})\">TRUE</button>
                    <button class=\"quiz-btn\" onclick=\"checkAnswer(this,{false_correct})\">FALSE</button>
                </div>
            </div>
            """
        )
    return "".join(blocks)


def build_vocab_html(vocab):
    cards = []
    for word, meaning in vocab:
        cards.append(
            f"""
            <div class=\"vocab-card\" onclick=\"this.classList.toggle('revealed')\">
                <div class=\"word\">{word}</div>
                <div class=\"meaning\">{meaning}</div>
                <div class=\"hint\">👆 clic para ver</div>
            </div>
            """
        )
    return "".join(cards)


def build_class_html(course):
    vocab_html = build_vocab_html(course["vocab"])
    left_html, right_html = build_matching_html(course["matching"])
    tf_html = build_tf_html(course["true_false"])
    reading_html = "".join(f"<p>{p}</p>" for p in course["reading_paragraphs"])

    total_points = len(course["matching"]) + len(course["true_false"])

    return f"""<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Clase 1 — {course['course_label']}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Inter', sans-serif; background: #f0f2f5; color: #333; line-height: 1.7; }}
        .header {{ background: linear-gradient(135deg, #1565c0, #1e88e5); color: white; padding: 35px 20px; text-align: center; }}
        .header h1 {{ font-size: 1.9em; font-weight: 700; margin-bottom: 5px; }}
        .header h2 {{ font-size: 1.1em; font-weight: 300; margin-bottom: 8px; }}
        .header .meta {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 12px; }}
        .header .meta span {{ background: rgba(255,255,255,0.2); padding: 5px 14px; border-radius: 20px; font-size: 0.85em; }}
        .container {{ max-width: 920px; margin: 24px auto; padding: 0 15px; }}

        .objective-card {{ background: white; border-radius: 12px; padding: 24px; margin-bottom: 22px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border-left: 5px solid #1565c0; }}
        .objective-card h3 {{ color: #1565c0; margin-bottom: 8px; }}

        .section {{ background: white; border-radius: 12px; margin-bottom: 22px; overflow: hidden; box-shadow: 0 2px 12px rgba(0,0,0,0.06); }}
        .section-header {{ padding: 14px 22px; color: white; font-weight: 600; font-size: 1.05em; }}
        .inicio {{ background: #2e7d32; }}
        .desarrollo {{ background: #1565c0; }}
        .cierre {{ background: #6a1b9a; }}
        .section-body {{ padding: 18px 22px; }}

        .section-body ul {{ margin-left: 18px; }}
        .section-body li {{ margin-bottom: 8px; }}

        .vocab-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); gap: 10px; margin-top: 12px; }}
        .vocab-card {{ background: #e3f2fd; border: 2px solid #90caf9; border-radius: 10px; padding: 12px; text-align: center; cursor: pointer; }}
        .vocab-card .word {{ font-weight: 700; color: #0d47a1; }}
        .vocab-card .meaning {{ font-size: 0.8em; color: #666; margin-top: 4px; display: none; }}
        .vocab-card.revealed .meaning {{ display: block; }}
        .vocab-card .hint {{ font-size: 0.72em; color: #888; margin-top: 4px; }}
        .vocab-card.revealed .hint {{ display: none; }}

        .matching-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 12px; }}
        .match-item {{ background: white; border: 2px solid #e0e0e0; border-radius: 8px; padding: 11px; text-align: center; margin-bottom: 8px; cursor: pointer; }}
        .match-item:hover {{ border-color: #1565c0; }}
        .match-item.selected {{ border-color: #1565c0; background: #e3f2fd; }}
        .match-item.matched {{ border-color: #2e7d32; background: #e8f5e9; color: #2e7d32; }}

        .reading-box {{ background: #fafafa; border: 1px solid #e0e0e0; border-radius: 10px; padding: 16px; margin-top: 12px; }}
        .reading-box h4 {{ color: #1565c0; margin-bottom: 8px; }}

        .quiz-item {{ background: #f7f7f7; border: 1px solid #e0e0e0; border-radius: 8px; padding: 12px; margin-bottom: 10px; }}
        .quiz-options {{ display: flex; gap: 10px; margin-top: 8px; }}
        .quiz-btn {{ padding: 7px 14px; border-radius: 8px; border: 2px solid #e0e0e0; background: white; cursor: pointer; }}
        .quiz-btn.correct {{ border-color: #2e7d32; background: #e8f5e9; color: #2e7d32; font-weight: 700; }}
        .quiz-btn.incorrect {{ border-color: #c62828; background: #ffebee; color: #c62828; }}

        .ticket-box {{ background: linear-gradient(135deg, #ede7f6, #e3f2fd); border: 2px dashed #1565c0; border-radius: 12px; padding: 18px; }}
        .ticket-input {{ width: 100%; padding: 9px 12px; border: 1px solid #ddd; border-radius: 8px; margin-top: 8px; }}

        .score-bar {{ background: white; border-radius: 10px; padding: 12px 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); display: flex; justify-content: space-between; align-items: center; }}
        .score {{ font-weight: 700; color: #1565c0; }}
        .footer {{ text-align: center; color: #999; font-size: 0.8em; margin: 18px 0; }}
    </style>
</head>
<body>
<div class=\"header\">
    <h1>CLASS 1 — {course['course_label'].upper()}</h1>
    <h2>{course['unit_title']}</h2>
    <div class=\"meta\">
        <span>📘 {course['oa']}</span>
        <span>⏱ 90 min</span>
        <span>🧭 Guía de estudiante</span>
    </div>
</div>

<div class=\"container\">
    <div class=\"objective-card\">
        <h3>🎯 Objetivo de la clase</h3>
        <p>{course['objective']}</p>
    </div>

    <div class=\"section\">
        <div class=\"section-header inicio\">🟢 Inicio (15 min)</div>
        <div class=\"section-body\">
            <ul>{''.join(f'<li>{item}</li>' for item in course['warmup'])}</ul>
        </div>
    </div>

    <div class=\"section\">
        <div class=\"section-header desarrollo\">🔵 Desarrollo (60 min)</div>
        <div class=\"section-body\">
            <h4>📖 Activity 1: Vocabulary</h4>
            <p>Haz clic en cada tarjeta para ver la traducción y estudiar vocabulario técnico.</p>
            <div class=\"vocab-grid\">{vocab_html}</div>

            <h4 style=\"margin-top:14px;\">🔗 Activity 2: Matching</h4>
            <p>Relaciona descripción y término técnico.</p>
            <div class=\"matching-grid\">
                <div>{left_html}</div>
                <div>{right_html}</div>
            </div>
            <p id=\"matchScore\" style=\"font-weight:600;color:#2e7d32;\"></p>

            <h4 style=\"margin-top:14px;\">📚 Activity 3: Reading</h4>
            <div class=\"reading-box\">
                <h4>{course['reading_title']}</h4>
                {reading_html}
            </div>

            <h4 style=\"margin-top:14px;\">✅ Activity 4: True or False</h4>
            {tf_html}
        </div>
    </div>

    <div class=\"section\">
        <div class=\"section-header cierre\">🟣 Cierre (15 min)</div>
        <div class=\"section-body\">
            <div class=\"ticket-box\">
                <h4>🎫 Exit Ticket</h4>
                <input class=\"ticket-input\" placeholder=\"1) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"2) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"3) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"4) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"5) New word + meaning\" />
                <input class=\"ticket-input\" placeholder=\"Reflection: {course['reflection']}\" />
            </div>
        </div>
    </div>

    <div class=\"score-bar\"><span>📊 Puntaje actividades</span><span class=\"score\" id=\"totalScore\">0 / {total_points}</span></div>
    <div class=\"footer\">{course['course_label']} — Clase 1, Unidad 1 — Inglés 2026</div>
</div>

<script>
    let score = 0;
    function updateScore() {{
        document.getElementById('totalScore').textContent = score + ' / {total_points}';
    }}

    function checkAnswer(btn, isCorrect) {{
        const buttons = btn.parentElement.querySelectorAll('.quiz-btn');
        buttons.forEach(b => b.disabled = true);
        if (isCorrect) {{ btn.classList.add('correct'); score++; }}
        else {{ btn.classList.add('incorrect'); buttons.forEach(b => {{ if (b !== btn) b.classList.add('correct'); }}); }}
        updateScore();
    }}

    let selectedLeft = null, selectedRight = null, matches = 0;
    function selectMatch(el, side) {{
        if (el.classList.contains('matched')) return;
        if (side === 'left') {{ if (selectedLeft) selectedLeft.classList.remove('selected'); selectedLeft = el; el.classList.add('selected'); }}
        else {{ if (selectedRight) selectedRight.classList.remove('selected'); selectedRight = el; el.classList.add('selected'); }}

        if (selectedLeft && selectedRight) {{
            if (selectedLeft.dataset.match === selectedRight.dataset.match) {{
                selectedLeft.classList.remove('selected'); selectedRight.classList.remove('selected');
                selectedLeft.classList.add('matched'); selectedRight.classList.add('matched');
                matches++; score++; updateScore();
                if (matches === {len(course['matching'])}) document.getElementById('matchScore').textContent = '🎉 ¡Matching completo!';
            }} else {{
                selectedLeft.classList.remove('selected'); selectedRight.classList.remove('selected');
            }}
            selectedLeft = null; selectedRight = null;
        }}
    }}
</script>
</body>
</html>
"""


def write_class_files():
    for course in COURSES:
        out = SITE / course["relative_file"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build_class_html(course), encoding="utf-8")


def cleanup_extra_files():
    keep = {str((SITE / c["relative_file"]).resolve()).lower() for c in COURSES}

    for folder in [
        SITE / "1ro-medio" / "lu-ju" / "u1",
        SITE / "3ro-medio" / "3A-industrial" / "u1",
        SITE / "3ro-medio" / "3B-automotriz" / "u1",
        SITE / "3ro-medio" / "3C-electricidad" / "u1",
        SITE / "3ro-medio" / "3D-grafica" / "u1",
        SITE / "3ro-medio" / "3E-electronica" / "u1",
        SITE / "4to-medio" / "4A-industrial" / "u1",
        SITE / "4to-medio" / "4B-automotriz" / "u1",
        SITE / "4to-medio" / "4C-electricidad" / "u1",
        SITE / "4to-medio" / "4E-electronica" / "u1",
    ]:
        if not folder.exists():
            continue
        for f in folder.glob("Clase_*_U1_*.html"):
            if str(f.resolve()).lower() not in keep:
                f.unlink(missing_ok=True)


def update_index():
    index_path = SITE / "index.html"
    soup = BeautifulSoup(index_path.read_text(encoding="utf-8"), "html.parser")

    by_course = {c["course_name"]: c for c in COURSES}

    for course_section in soup.select(".course-section"):
        h3 = course_section.select_one(".course-header h3")
        if not h3:
            continue
        course_name = h3.get_text(strip=True)
        if course_name not in by_course:
            continue

        course = by_course[course_name]
        unit_group = course_section.select_one(".unit-group")
        if not unit_group:
            continue

        unit_classes = unit_group.select_one(".unit-classes")
        if not unit_classes:
            continue

        unit_classes.clear()
        link_html = (
            f"<a class=\"class-link\" href=\"{course['relative_file'].replace('\\\\', '/')}\" data-progress-id=\"{course['course_key']}/u1/Clase_1\">"
            f"<span class=\"num\">1</span>"
            f"<span class=\"title\">Clase 1 — {course['objective'][:75]}...</span>"
            f"<span class=\"tag tag-clase\">Clase</span>"
            f"<span class=\"status-badge status-pending\" data-status-badge>⏳ Pendiente</span>"
            f"</a>"
        )
        unit_classes.append(BeautifulSoup(link_html, "html.parser"))

    index_path.write_text(str(soup), encoding="utf-8")


def update_progress():
    progress_path = SITE / "progress.json"
    data = {"lastUpdated": str(date.today()), "classes": {}}
    for course in COURSES:
        key = f"{course['course_key']}/u1/Clase_1"
        data["classes"][key] = {
            "status": "pending",
            "title": "Clase 1 — Material de clase interactivo"
        }
    progress_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    write_class_files()
    cleanup_extra_files()
    update_index()
    update_progress()


if __name__ == "__main__":
    main()
