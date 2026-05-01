import json
import re
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(r"c:\Users\crist\OneDrive\Escritorio\2026")
SOURCE_SITE = ROOT / "materiales-clases"
PUBLISHED_SITE = ROOT / "tranquiprofe.cl" / "static" / "recursos" / "materiales"
INDEX_TARGETS = [
    SOURCE_SITE / "index.html",
    ROOT / "tranquiprofe.cl" / "templates" / "recursos" / "materiales" / "index.html",
]
PROGRESS_TARGETS = [
    SOURCE_SITE / "progress.json",
    PUBLISHED_SITE / "progress.json",
]


COURSES = [
    {
        "course_name": "1° Medio — Inglés General",
        "course_key": "1ro-lu-ju",
        "course_label": "1° Medio — Inglés General (Lu+Ju)",
        "folder": "1ro-medio/lu-ju",
        "file_code": "1ro_LuJu",
        "u1_file_code": "1ro_LuJu",
        "plans": {
            1: ROOT / "PLANIFICACIONES_2026_LISTO_IMPRESION" / "1ro Medio" / "Lu+Ju" / "planificacion_unidad1_lu_ju.html",
            2: ROOT / "1ro Medio" / "Unidad 2" / "planificacion_unidad2_lu_ju.html",
            3: ROOT / "1ro Medio" / "Unidad 3" / "planificacion_unidad3_lu_ju.html",
            4: ROOT / "1ro Medio" / "Unidad 4" / "planificacion_unidad4_lu_ju.html",
        },
    },
    {
        "course_name": "3°A — Mecánica Industrial",
        "course_key": "3A-industrial",
        "course_label": "3°A — Mecánica Industrial",
        "folder": "3ro-medio/3A-industrial",
        "file_code": "3roA_Industrial",
        "u1_file_code": "3ro_Industrial",
        "plans": {
            1: ROOT / "3ro Medio" / "Unidad 1" / "planificacion_u1_industrial.html",
            2: ROOT / "3ro Medio" / "Unidad 2" / "planificacion_u2_industrial.html",
            3: ROOT / "3ro Medio" / "Unidad 3" / "planificacion_u3_industrial.html",
            4: ROOT / "3ro Medio" / "Unidad 4" / "planificacion_u4_industrial.html",
        },
    },
    {
        "course_name": "3°B — Mecánica Automotriz",
        "course_key": "3B-automotriz",
        "course_label": "3°B — Mecánica Automotriz",
        "folder": "3ro-medio/3B-automotriz",
        "file_code": "3roB_Automotriz",
        "u1_file_code": "3ro_Automotriz",
        "plans": {
            1: ROOT / "3ro Medio" / "Unidad 1" / "planificacion_u1_automotriz.html",
            2: ROOT / "3ro Medio" / "Unidad 2" / "planificacion_u2_automotriz.html",
            3: ROOT / "3ro Medio" / "Unidad 3" / "planificacion_u3_automotriz.html",
            4: ROOT / "3ro Medio" / "Unidad 4" / "planificacion_u4_automotriz.html",
        },
    },
    {
        "course_name": "3°C — Electricidad",
        "course_key": "3C-electricidad",
        "course_label": "3°C — Electricidad",
        "folder": "3ro-medio/3C-electricidad",
        "file_code": "3roC_Electricidad",
        "u1_file_code": "3ro_Electricidad",
        "plans": {
            1: ROOT / "3ro Medio" / "Unidad 1" / "planificacion_u1_electricidad.html",
            2: ROOT / "3ro Medio" / "Unidad 2" / "planificacion_u2_electricidad.html",
            3: ROOT / "3ro Medio" / "Unidad 3" / "planificacion_u3_electricidad.html",
            4: ROOT / "3ro Medio" / "Unidad 4" / "planificacion_u4_electricidad.html",
        },
    },
    {
        "course_name": "3°D — Gráfica",
        "course_key": "3D-grafica",
        "course_label": "3°D — Gráfica",
        "folder": "3ro-medio/3D-grafica",
        "file_code": "3roD_Grafica",
        "u1_file_code": "3ro_Grafica",
        "plans": {
            1: ROOT / "3ro Medio" / "Unidad 1" / "planificacion_u1_grafica.html",
            2: ROOT / "3ro Medio" / "Unidad 2" / "planificacion_u2_grafica.html",
            3: ROOT / "3ro Medio" / "Unidad 3" / "planificacion_u3_grafica.html",
            4: ROOT / "3ro Medio" / "Unidad 4" / "planificacion_u4_grafica.html",
        },
    },
    {
        "course_name": "3°E — Electrónica",
        "course_key": "3E-electronica",
        "course_label": "3°E — Electrónica",
        "folder": "3ro-medio/3E-electronica",
        "file_code": "3roE_Electronica",
        "u1_file_code": "3ro_Electronica",
        "plans": {
            1: ROOT / "3ro Medio" / "Unidad 1" / "planificacion_u1_electronica.html",
            2: ROOT / "3ro Medio" / "Unidad 2" / "planificacion_u2_electronica.html",
            3: ROOT / "3ro Medio" / "Unidad 3" / "planificacion_u3_electronica.html",
            4: ROOT / "3ro Medio" / "Unidad 4" / "planificacion_u4_electronica.html",
        },
    },
    {
        "course_name": "4°A — Mecánica Industrial",
        "course_key": "4A-industrial",
        "course_label": "4°A — Mecánica Industrial",
        "folder": "4to-medio/4A-industrial",
        "file_code": "4toA_Industrial",
        "u1_file_code": "4to_Industrial",
        "plans": {
            1: ROOT / "4to Medio" / "Unidad 1" / "planificacion_u1_industrial.html",
            2: ROOT / "4to Medio" / "Unidad 2" / "planificacion_u2_industrial.html",
            3: ROOT / "4to Medio" / "Unidad 3" / "planificacion_u3_industrial.html",
            4: ROOT / "4to Medio" / "Unidad 4" / "planificacion_u4_industrial.html",
        },
    },
    {
        "course_name": "4°B — Mecánica Automotriz",
        "course_key": "4B-automotriz",
        "course_label": "4°B — Mecánica Automotriz",
        "folder": "4to-medio/4B-automotriz",
        "file_code": "4toB_Automotriz",
        "u1_file_code": "4to_Automotriz",
        "plans": {
            1: ROOT / "4to Medio" / "Unidad 1" / "planificacion_u1_automotriz.html",
            2: ROOT / "4to Medio" / "Unidad 2" / "planificacion_u2_automotriz.html",
            3: ROOT / "4to Medio" / "Unidad 3" / "planificacion_u3_automotriz.html",
            4: ROOT / "4to Medio" / "Unidad 4" / "planificacion_u4_automotriz.html",
        },
    },
    {
        "course_name": "4°C — Electricidad",
        "course_key": "4C-electricidad",
        "course_label": "4°C — Electricidad",
        "folder": "4to-medio/4C-electricidad",
        "file_code": "4toC_Electricidad",
        "u1_file_code": "4to_Electricidad",
        "plans": {
            1: ROOT / "4to Medio" / "Unidad 1" / "planificacion_u1_electricidad.html",
            2: ROOT / "4to Medio" / "Unidad 2" / "planificacion_u2_electricidad.html",
            3: ROOT / "4to Medio" / "Unidad 3" / "planificacion_u3_electricidad.html",
            4: ROOT / "4to Medio" / "Unidad 4" / "planificacion_u4_electricidad.html",
        },
    },
    {
        "course_name": "4°E — Electrónica",
        "course_key": "4E-electronica",
        "course_label": "4°E — Electrónica",
        "folder": "4to-medio/4E-electronica",
        "file_code": "4toE_Electronica",
        "u1_file_code": "4to_Electronica",
        "plans": {
            1: ROOT / "4to Medio" / "Unidad 1" / "planificacion_u1_electronica.html",
            2: ROOT / "4to Medio" / "Unidad 2" / "planificacion_u2_electronica.html",
            3: ROOT / "4to Medio" / "Unidad 3" / "planificacion_u3_electronica.html",
            4: ROOT / "4to Medio" / "Unidad 4" / "planificacion_u4_electronica.html",
        },
    },
]


COURSE_CONTEXT = {
    "1ro-lu-ju": {
        "specialty": "formación técnico-profesional general",
        "workplace": "school technical workshop",
        "role": "student technician",
        "product": "practice project",
        "equipment": ["tool kit", "checklist", "workstation"],
        "base_glossary": [
            ("process", "proceso", "PRO-ses"),
            ("component", "componente", "kom-POU-nent"),
            ("tool", "herramienta", "TUL"),
            ("measure", "medir", "ME-zher"),
            ("connect", "conectar", "ko-NEKT"),
            ("repair", "reparar", "ri-PAIR"),
        ],
    },
    "3A-industrial": {
        "specialty": "mecánica industrial",
        "workplace": "industrial workshop",
        "role": "machine operator",
        "product": "metal support",
        "equipment": ["lathe", "caliper", "blueprint"],
        "base_glossary": [
            ("lathe", "torno", "LEITH"),
            ("caliper", "calibrador", "KA-li-per"),
            ("blueprint", "plano técnico", "BLU-print"),
            ("tolerance", "tolerancia", "TO-le-rans"),
            ("weld", "soldar", "WELD"),
            ("surface", "superficie", "SER-fis"),
        ],
    },
    "3B-automotriz": {
        "specialty": "mecánica automotriz",
        "workplace": "automotive workshop",
        "role": "service technician",
        "product": "vehicle service order",
        "equipment": ["diagnostic scanner", "engine bay", "service checklist"],
        "base_glossary": [
            ("engine", "motor", "EN-yin"),
            ("scanner", "escáner", "SKA-ner"),
            ("coolant", "refrigerante", "KU-lant"),
            ("brake", "freno", "BREIK"),
            ("fault", "falla", "FOLT"),
            ("repair", "reparación", "ri-PAIR"),
        ],
    },
    "3C-electricidad": {
        "specialty": "electricidad",
        "workplace": "electrical lab",
        "role": "electrical trainee",
        "product": "panel connection",
        "equipment": ["multimeter", "control panel", "wire set"],
        "base_glossary": [
            ("multimeter", "multímetro", "mol-TI-mi-ter"),
            ("panel", "panel", "PA-nel"),
            ("grounding", "puesta a tierra", "GRAUN-ding"),
            ("circuit", "circuito", "SER-kit"),
            ("breaker", "interruptor automático", "BREI-ker"),
            ("voltage", "voltaje", "VOL-tich"),
        ],
    },
    "3D-grafica": {
        "specialty": "gráfica",
        "workplace": "print production area",
        "role": "print assistant",
        "product": "print order",
        "equipment": ["color proof", "press", "cutter"],
        "base_glossary": [
            ("proof", "prueba de color", "PRUF"),
            ("press", "prensa", "PRES"),
            ("layout", "diagramación", "LEI-aut"),
            ("ink", "tinta", "INK"),
            ("plate", "plancha", "PLEIT"),
            ("binding", "encuadernación", "BAIN-ding"),
        ],
    },
    "3E-electronica": {
        "specialty": "electrónica",
        "workplace": "electronics lab",
        "role": "electronics technician",
        "product": "test circuit",
        "equipment": ["PCB", "oscilloscope", "soldering station"],
        "base_glossary": [
            ("PCB", "placa PCB", "pi-si-BI"),
            ("sensor", "sensor", "SEN-sor"),
            ("oscilloscope", "osciloscopio", "o-SI-lo-skop"),
            ("solder", "soldar", "SOL-der"),
            ("signal", "señal", "SIG-nal"),
            ("voltage", "voltaje", "VOL-tich"),
        ],
    },
    "4A-industrial": {
        "specialty": "mecánica industrial avanzada",
        "workplace": "industrial maintenance area",
        "role": "maintenance technician",
        "product": "maintenance report",
        "equipment": ["CNC machine", "maintenance log", "inspection form"],
        "base_glossary": [
            ("maintenance", "mantención", "MEIN-te-nans"),
            ("inspection", "inspección", "ins-PEK-shon"),
            ("CNC", "máquina CNC", "si-en-SI"),
            ("quality", "calidad", "KWO-li-ti"),
            ("schedule", "programación", "SKE-dyul"),
            ("downtime", "tiempo detenido", "DAUN-taim"),
        ],
    },
    "4B-automotriz": {
        "specialty": "mecánica automotriz avanzada",
        "workplace": "advanced service bay",
        "role": "diagnostic specialist",
        "product": "diagnostic report",
        "equipment": ["OBD scanner", "service tablet", "hybrid system"],
        "base_glossary": [
            ("diagnostic", "diagnóstico", "daiag-NOS-tik"),
            ("hybrid", "híbrido", "JAI-brid"),
            ("torque", "torque", "TORK"),
            ("alignment", "alineación", "a-LAIN-ment"),
            ("fault code", "código de falla", "FOLT koud"),
            ("service", "servicio", "SER-vis"),
        ],
    },
    "4C-electricidad": {
        "specialty": "electricidad avanzada",
        "workplace": "power systems workshop",
        "role": "electrical installer",
        "product": "power distribution task",
        "equipment": ["switchgear", "three-phase panel", "load table"],
        "base_glossary": [
            ("switchgear", "equipo de maniobra", "SWICH-guir"),
            ("load", "carga", "LOUD"),
            ("transformer", "transformador", "trans-FOR-mer"),
            ("grounding", "puesta a tierra", "GRAUN-ding"),
            ("regulator", "regulador", "RE-gu-lei-ter"),
            ("phase", "fase", "FEIS"),
        ],
    },
    "4E-electronica": {
        "specialty": "electrónica avanzada",
        "workplace": "digital systems lab",
        "role": "embedded systems trainee",
        "product": "embedded system task",
        "equipment": ["microcontroller", "firmware file", "test bench"],
        "base_glossary": [
            ("firmware", "firmware", "FERM-uer"),
            ("microcontroller", "microcontrolador", "MAI-kro-kon-TRO-ler"),
            ("embedded", "embebido", "em-BE-did"),
            ("datasheet", "hoja técnica", "DEI-ta-shit"),
            ("sensor", "sensor", "SEN-sor"),
            ("signal", "señal", "SIG-nal"),
        ],
    },
}


UNIT_GLOSSARY = {
    1: [
        ("workshop", "taller", "UERK-shop"),
        ("specialty", "especialidad", "SPE-shal-ti"),
        ("routine", "rutina", "ru-TIN"),
        ("safety", "seguridad", "SEIF-ti"),
        ("equipment", "equipamiento", "i-KUIP-ment"),
        ("task", "tarea", "TASK"),
        ("procedure", "procedimiento", "pro-SI-dyer"),
        ("instructions", "instrucciones", "ins-TRUK-shons"),
    ],
    2: [
        ("process", "proceso", "PRO-ses"),
        ("step", "paso", "STEP"),
        ("material", "material", "ma-TI-ri-al"),
        ("assemble", "ensamblar", "a-SEM-bol"),
        ("inspect", "inspeccionar", "ins-PEKT"),
        ("manual", "manual", "MAN-yu-al"),
        ("measure", "medir", "ME-zher"),
        ("safety", "seguridad", "SEIF-ti"),
    ],
    3: [
        ("report", "reporte", "ri-PORT"),
        ("issue", "problema", "I-shu"),
        ("solution", "solución", "so-LU-shon"),
        ("client", "cliente", "KLAI-ent"),
        ("supervisor", "supervisor", "SU-per-vai-sor"),
        ("sequence", "secuencia", "SI-kuens"),
        ("deadline", "plazo", "DED-lain"),
        ("feedback", "retroalimentación", "FID-bak"),
    ],
    4: [
        ("project", "proyecto", "PRO-yekt"),
        ("improve", "mejorar", "im-PRUV"),
        ("evaluate", "evaluar", "i-VA-lieit"),
        ("proposal", "propuesta", "pro-PO-sal"),
        ("result", "resultado", "ri-ZOLT"),
        ("innovation", "innovación", "ino-VEI-shon"),
        ("quality", "calidad", "KWO-li-ti"),
        ("teamwork", "trabajo en equipo", "TIM-uork"),
    ],
}


LEVEL_PROFILES = {
    "1ro": {
        "cefr": "A2",
        "question_stems": [
            "What task or problem is described in the text?",
            "What happens before the main procedure starts?",
            "Which tools, parts, or notes are important in the reading?",
            "How does the text show the main language focus of the class?",
            "What result, decision, or solution appears at the end?",
            "What can you infer about good technical work from the text?",
        ],
        "reading_note": "Texto graduado A2: ideas claras, detalle tecnico suficiente y vocabulario reutilizable para hablar y escribir.",
    },
    "upper": {
        "cefr": "B1",
        "question_stems": [
            "What operational or communicative challenge is presented in the text?",
            "Which prior checks or contextual details shape the task?",
            "What evidence or technical details guide the team's decisions?",
            "How does the writer use the language focus of the lesson to clarify meaning?",
            "What conclusion or recommendation emerges from the situation?",
            "What broader lesson about technical communication can be inferred?",
        ],
        "reading_note": "Texto B1: cinco parrafos con relaciones de causa, secuencia, evidencia y conclusion tecnica.",
    },
}


TERM_DEFINITIONS = {
    "process": "a sequence of actions used to complete a task",
    "component": "one part of a machine, circuit, or larger system",
    "tool": "an object used to do a practical or technical job",
    "measure": "to find size, amount, or distance accurately",
    "connect": "to join parts so the system can work correctly",
    "repair": "to fix something that is damaged or not working",
    "lathe": "a machine that turns material so it can be shaped",
    "caliper": "a precision tool used to measure width or thickness",
    "blueprint": "a technical drawing that shows how something must be built",
    "tolerance": "the allowed small difference in a measurement",
    "weld": "to join metal parts using heat",
    "surface": "the outside part of an object or material",
    "engine": "the machine that produces power in a vehicle",
    "scanner": "a device that reads digital information or fault codes",
    "coolant": "a liquid that controls temperature in a machine or engine",
    "brake": "the system or part that slows or stops movement",
    "fault": "a defect or problem in a system",
    "multimeter": "an instrument that measures voltage, current, and resistance",
    "panel": "a board where controls, switches, or circuits are organized",
    "grounding": "a safety connection that sends electricity safely to the earth",
    "circuit": "a complete path that lets electricity move",
    "breaker": "a protective switch that stops current during a fault",
    "voltage": "the electrical force that pushes current through a circuit",
    "proof": "a test print used to check color and layout before final production",
    "press": "a machine that transfers ink onto paper or another surface",
    "layout": "the way text and images are arranged on a page",
    "ink": "colored liquid used in printing",
    "plate": "the prepared surface that carries the printable image",
    "binding": "the process of joining printed pages together",
    "pcb": "a board that holds and connects electronic components",
    "sensor": "a device that detects change and sends information",
    "oscilloscope": "an instrument that displays electrical signals as waves",
    "solder": "to join electronic parts using melted metal",
    "signal": "electrical information that carries data",
    "maintenance": "the routine work done to keep equipment operating well",
    "inspection": "a careful check used to verify condition or quality",
    "cnc": "computer-controlled equipment used for precise machining",
    "quality": "the degree to which a result meets the expected standard",
    "schedule": "the planned time and order for tasks or maintenance",
    "downtime": "the period when a machine is stopped and unavailable",
    "diagnostic": "an analysis used to identify the cause of a problem",
    "hybrid": "a system that combines two kinds of power or technology",
    "torque": "the turning force that makes a part rotate",
    "alignment": "the correct position of parts so they work properly",
    "fault code": "a digital message that identifies a system problem",
    "service": "maintenance or repair work done on equipment or vehicles",
    "switchgear": "equipment that controls, protects, and isolates power systems",
    "load": "the amount of power demanded by a system",
    "transformer": "equipment that changes electrical voltage levels",
    "regulator": "a device that keeps a value, such as voltage, stable",
    "phase": "one part of a multi-part electrical power cycle",
    "firmware": "software stored inside a device to control its functions",
    "microcontroller": "a small programmable chip used to control a system",
    "embedded": "built into a device as part of its internal system",
    "datasheet": "a technical document that lists specifications and limits",
    "project": "a planned piece of work with a clear goal",
    "improve": "to make a process or result better",
    "evaluate": "to judge quality, effectiveness, or performance",
    "proposal": "a suggested plan or solution",
    "result": "the final outcome of an action or process",
    "innovation": "a new idea, method, or improvement",
    "teamwork": "coordinated work done by more than one person",
    "step": "one stage in a longer process",
    "material": "the physical substance used to make or repair something",
    "assemble": "to put parts together to make a complete product",
    "inspect": "to check carefully for quality, safety, or faults",
    "manual": "a document that explains how to use or maintain something",
    "report": "a structured text that records findings or results",
    "issue": "a problem that needs attention or action",
    "solution": "the action used to solve a problem",
    "client": "the person or company that receives the service",
    "supervisor": "the person responsible for checking or guiding the work",
    "sequence": "the order in which actions happen",
    "deadline": "the time limit for finishing a task",
    "feedback": "comments that help improve performance or results",
    "evidence": "information that supports a conclusion or decision",
    "checklist": "a list used to confirm that all steps were completed",
    "workstation": "the area where a person performs a task",
    "service checklist": "a control list used to verify each part of a service",
    "engine bay": "the space inside a vehicle where the engine is located",
    "control panel": "the area with buttons, switches, or displays used to manage a system",
    "wire set": "a prepared group of cables used for a specific electrical task",
    "color proof": "a sample print that shows the expected color result",
    "cutter": "a machine or tool used to trim material precisely",
    "soldering station": "a work unit used for safe and controlled soldering",
    "maintenance log": "a record of inspections, repairs, and scheduled actions",
    "inspection form": "a document used to register the results of a technical check",
    "obd scanner": "a tool that reads digital information from a vehicle system",
    "service tablet": "a digital device used to consult procedures and record service data",
    "hybrid system": "a vehicle system that combines electric and fuel power",
    "three-phase panel": "a distribution board designed for three-phase power",
    "load table": "a chart used to compare or calculate electrical demand",
    "firmware file": "the digital package used to install or update device control software",
    "test bench": "a station used to test equipment under controlled conditions",
}


FOCUS_TITLES = {
    "instructions": "Reading Text — Guided Technical Procedure",
    "troubleshooting": "Reading Text — Diagnosis and Solution",
    "report": "Reading Text — Technical Report and Evidence",
    "comparison": "Reading Text — Comparing Technical Options",
    "reflection": "Reading Text — Review and Professional Reflection",
    "process": "Reading Text — Process and Description",
    "oral": "Reading Model — Preparing an Oral Explanation",
}


FOCUS_DESCRIPTIONS = {
    "instructions": "a step-by-step technical procedure",
    "troubleshooting": "a diagnostic situation that must be solved",
    "report": "a technical report based on evidence",
    "comparison": "two technical options that must be evaluated",
    "reflection": "an end-of-unit reflection on workshop learning",
    "process": "a technical process that must be explained clearly",
    "oral": "a model explanation prepared for an oral task",
}


def clean_text(text):
    return re.sub(r"\s+", " ", text or "").strip()


def level_profile(course_key):
    return LEVEL_PROFILES["1ro" if course_key.startswith("1ro") else "upper"]


def definition_for_term(word, fallback=""):
    return TERM_DEFINITIONS.get(word.lower(), fallback or "key technical term used in the lesson")


def extract_unit_title(text):
    cleaned = clean_text(text)
    return re.sub(r"^Unidad\s*\d+\s*[:\-]\s*", "", cleaned, flags=re.IGNORECASE)


def parse_plan_file(plan_path):
    soup = BeautifulSoup(plan_path.read_text(encoding="utf-8"), "html.parser")

    header_title = clean_text(soup.select_one(".header h2").get_text(" "))
    subtitle = clean_text(soup.select_one(".header .subtitle").get_text(" "))
    meta = [clean_text(span.get_text(" ")) for span in soup.select(".meta-info span")]
    unit_title = extract_unit_title(header_title)

    classes = []
    for index, card in enumerate(soup.select(".clase-card"), start=1):
        class_num_text = clean_text(card.select_one(".clase-num").get_text(" "))
        match = re.search(r"(\d+)", class_num_text)
        annual_number = int(match.group(1)) if match else index

        objective_box = card.select_one(".objetivo")
        objective = clean_text(objective_box.get_text(" ")) if objective_box else ""
        objective = re.sub(r"^Objetivo de la clase(?: \(Bloom\))?:\s*", "", objective, flags=re.IGNORECASE)

        phases = {}
        for phase in card.select(".fase"):
            title = clean_text(phase.select_one(".fase-title").get_text(" ")) if phase.select_one(".fase-title") else ""
            key = "inicio"
            if "DESARROLLO" in title.upper():
                key = "desarrollo"
            elif "CIERRE" in title.upper():
                key = "cierre"

            items = []
            content = phase.select_one(".fase-content")
            if content:
                for list_tag in content.find_all(["ul", "ol"], recursive=False):
                    for li in list_tag.find_all("li", recursive=False):
                        items.append(clean_text(li.get_text(" ")))
            phases[key] = items

        resources = clean_text(card.select_one(".recursos").get_text(" ")) if card.select_one(".recursos") else ""
        resources = re.sub(r"^📦\s*Recursos:\s*", "", resources)
        evaluation = clean_text(card.select_one(".evaluacion-box").get_text(" ")) if card.select_one(".evaluacion-box") else ""
        evaluation = re.sub(r"^📋\s*Evaluación:\s*", "", evaluation)
        badges = [clean_text(tag.get_text(" ")) for tag in card.select(".badge")]
        classes.append(
            {
                "annual_number": annual_number,
                "unit_index": index,
                "objective": objective,
                "phases": phases,
                "resources": resources,
                "evaluation": evaluation,
                "badges": badges,
                "is_plan_evaluation": "evaluacion" in (card.get("class") or []),
            }
        )

    return {
        "unit_title": unit_title,
        "subtitle": subtitle,
        "meta": meta,
        "classes": classes,
    }


def infer_focus(objective):
    objective_lower = objective.lower()
    keyword_map = [
        ("instructions", ["instruction", "instruccion", "secuenciar", "procedimiento", "manual", "step"]),
        ("troubleshooting", ["falla", "diagnóstico", "problem", "issue", "solution", "caso"]),
        ("report", ["report", "reporte", "ficha", "specification", "quality", "manuales"]),
        ("oral", ["oral", "presentation", "presentar", "explicar", "interacciones", "ensayar"]),
        ("comparison", ["compar", "contraste", "consecu", "alternative", "implicaciones", "discutir"]),
        ("reflection", ["reflexionar", "sintetizar", "review", "integrado", "dominio"]),
        ("process", ["process", "proceso", "fabricación", "ensamblaje", "funcionamiento", "describe"]),
    ]
    for focus, keywords in keyword_map:
        if any(keyword in objective_lower for keyword in keywords):
            return focus
    return "process"


def evaluation_kind(unit_number, class_data, total_classes):
    if unit_number in (3, 4):
        mid_index = (total_classes + 1) // 2
        objective_lower = class_data["objective"].lower()
        if class_data["unit_index"] == mid_index or (
            class_data["is_plan_evaluation"] and any(word in objective_lower for word in ["oral", "explicación", "presentation", "explicar"])
        ):
            return "oral"
        if class_data["unit_index"] == total_classes:
            return "reading"
    if unit_number == 2 and class_data["unit_index"] == total_classes:
        return "reading"
    return None


def oral_project_sequence(course, unit_number, class_data):
    course_key = course["course_key"] if isinstance(course, dict) else course
    if unit_number != 2:
        return None

    if course_key == "1ro-lu-ju":
        config = {
            "family": "1ro",
            "class_indices": [7, 8, 9, 10, 11],
            "project_name": "Trabajo oral de cierre semestral",
            "project_short_title": "Trabajo oral — proceso técnico",
            "due_note": "Entrega prevista: primera semana de junio.",
            "prompt": "Describe a technical process or mechanism from workshop practice, using clear sequence, technical vocabulary, and one safety detail.",
            "requirements": [
                "Choose one process, machine, or mechanism connected to workshop practice.",
                "Explain materials, components, steps, and one relevant safety point.",
                "Use passive voice, relative clauses, and at least six technical words.",
                "Close with one practical conclusion about why the process matters.",
            ],
            "stage_titles": [
                "Definir el proceso del trabajo oral",
                "Recolectar pasos y vocabulario clave",
                "Organizar la explicación técnica",
                "Ensayar con apoyo y retroalimentación",
                "Trabajo oral final de proceso técnico",
            ],
            "stage_goals": [
                "Elegir un proceso o mecanismo y fijar el foco de la explicación.",
                "Extraer pasos, datos y vocabulario útil desde textos, diagramas o fichas.",
                "Ordenar la explicación con inicio, desarrollo y cierre en inglés.",
                "Practicar con apoyo visual y mejorar claridad, pronunciación y seguridad.",
                "Presentar el proceso técnico y responder preguntas simples de seguimiento.",
            ],
            "stage_outputs": [
                "Ficha de planificación con tema, propósito y vocabulario base.",
                "Banco de evidencias con pasos, especificaciones y palabras clave.",
                "Guion oral breve con opening, sequence, safety note y closing.",
                "Ensayo cronometrado con checklist de retroalimentación.",
                "Presentación oral individual con autoevaluación breve.",
            ],
        }
    elif course_key.startswith("4"):
        config = {
            "family": "4to",
            "class_indices": [1, 2, 3, 4, 6],
            "project_name": "Trabajo oral de junio",
            "project_short_title": "Trabajo oral — análisis técnico",
            "due_note": "Entrega prevista: primera semana de junio.",
            "prompt": "Present a technical workplace case, explain the evidence, and defend a practical solution with justified recommendations.",
            "requirements": [
                "Present one technical case, workplace situation, or operational problem.",
                "Explain evidence, causes, and consequences using precise technical language.",
                "Defend one feasible solution or recommendation for the scenario.",
                "Close with a professional conclusion and answer follow-up questions.",
            ],
            "stage_titles": [
                "Seleccionar el caso técnico y la postura",
                "Reunir evidencia y vocabulario especializado",
                "Construir el argumento oral",
                "Ensayar con retroalimentación crítica",
                "Trabajo oral final de junio",
            ],
            "stage_goals": [
                "Definir el caso técnico, el público y la idea central de la intervención oral.",
                "Reunir evidencia desde reportes, manuales o lecturas y fijar vocabulario clave.",
                "Organizar la intervención con problema, evidencia, propuesta y cierre profesional.",
                "Ensayar con un compañero, ajustar pronunciación y fortalecer la justificación.",
                "Presentar el análisis técnico y defender oralmente una solución viable.",
            ],
            "stage_outputs": [
                "Tarjeta de proyecto con caso, audiencia y enfoque del análisis.",
                "Banco de evidencia con datos, conceptos y citas útiles para hablar.",
                "Esquema oral con opening, evidence, recommendation y closing.",
                "Ensayo con checklist de claridad, evidencia y manejo del tiempo.",
                "Presentación oral con preguntas de seguimiento y cierre reflexivo.",
            ],
        }
    else:
        return None

    unit_index = class_data["unit_index"]
    class_indices = config["class_indices"]
    if unit_index not in class_indices:
        return None

    stage = class_indices.index(unit_index) + 1
    return {
        **config,
        "stage": stage,
        "total_stages": len(config["stage_titles"]),
        "is_delivery": unit_index == class_indices[-1],
        "stage_title": config["stage_titles"][stage - 1],
        "stage_goal": config["stage_goals"][stage - 1],
        "stage_output": config["stage_outputs"][stage - 1],
    }


def class_is_evaluation(class_data, eval_kind):
    return bool(eval_kind or class_data["is_plan_evaluation"])


def truncate_text(text, max_len=82):
    if len(text) <= max_len:
        return text
    shortened = text[:max_len].rsplit(" ", 1)[0]
    return f"{shortened}..."


def short_title(class_data, unit_number, eval_kind, oral_sequence=None):
    if oral_sequence:
        return oral_sequence["project_short_title"] if oral_sequence["is_delivery"] else oral_sequence["stage_title"]
    if eval_kind == "oral":
        return "Evaluación oral de procedimiento técnico"
    if eval_kind == "reading":
        return "Prueba de comprensión lectora"
    cleaned = re.sub(
        r"^(Comprender|Aplicar|Analizar|Describir|Identificar|Participar|Organizar|Producir|Evaluar|Demostrar|Reflexionar|Sintetizar)\s+",
        "",
        class_data["objective"],
        flags=re.IGNORECASE,
    )
    return truncate_text(cleaned)


def unique_glossary(items):
    seen = set()
    ordered = []
    for word, translation, pronunciation in items:
        key = word.lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append((word, translation, pronunciation))
    return ordered


def select_glossary(course_key, unit_number):
    context = COURSE_CONTEXT[course_key]
    return unique_glossary(context["base_glossary"] + UNIT_GLOSSARY[unit_number])[:6]


def review_prompt(previous_class, unit_number):
    if not previous_class:
        return {
            "title": "Repaso rápido de la unidad anterior",
            "steps": [
                "Nombra 3 palabras técnicas que recuerdes de la unidad anterior.",
                "Completa una oración con una idea clave que todavía recuerdes.",
                "Comenta con tu compañero dónde usarías ese contenido en un taller o laboratorio.",
            ],
        }

    snippet = truncate_text(previous_class["objective"], 90)
    return {
        "title": "Repaso rápido de la clase anterior",
        "steps": [
            f"Recuerda la idea central de la clase pasada: {snippet}",
            "Escribe una palabra o estructura que todavía recuerdes usar.",
            "Explica en una frase cómo ese contenido se conecta con la actividad de hoy.",
        ],
    }


def should_generate_class(unit_number, class_data):
    return unit_number != 1 or class_data["unit_index"] >= 3


def detect_language_focuses(objective, context):
    objective_lower = objective.lower()
    tool_one = context["equipment"][0]
    tool_two = context["equipment"][1]
    product = context["product"]
    blocks = []

    if "passive voice" in objective_lower:
        blocks.append(
            {
                "label": "Passive Voice",
                "title": "Passive Voice in technical English",
                "explanation": "Use passive voice when the process or result is more important than the person who performs the action.",
                "examples": [
                    f"The {product} is checked before the main task begins.",
                    f"The {tool_one} is used during the second stage of the procedure.",
                    "The final result is recorded after the inspection.",
                ],
                "frames": [
                    "The ___ is prepared before ...",
                    "The ___ is tested so that ...",
                    "At the end, the ___ is reported.",
                ],
            }
        )

    if "relative clause" in objective_lower or "relative clauses" in objective_lower or any(token in objective_lower for token in [" who ", " which ", " that "]):
        blocks.append(
            {
                "label": "Relative Clauses",
                "title": "Relative clauses for precise definitions",
                "explanation": "Use who, which, or that to add essential information about a person, tool, or process.",
                "examples": [
                    f"A technician is a person who checks the {product} carefully.",
                    f"The {tool_one} is a tool that helps the team collect evidence.",
                    f"A report which includes measurements is easier to verify.",
                ],
                "frames": [
                    "A ___ is a tool that ...",
                    "A technician is someone who ...",
                    "The report which ... shows that ...",
                ],
            }
        )

    if "tag question" in objective_lower or "tag questions" in objective_lower:
        blocks.append(
            {
                "label": "Tag Questions",
                "title": "Tag questions to confirm information",
                "explanation": "Use a short question at the end of the sentence to confirm a fact, a safety check, or a shared assumption.",
                "examples": [
                    f"The {tool_one} is ready, isn't it?",
                    "The team checked the result, didn't they?",
                    "The system has been tested, hasn't it?",
                ],
                "frames": [
                    "The ___ is safe, isn't it?",
                    "You checked the ___, didn't you?",
                    "The team has finished, haven't they?",
                ],
            }
        )

    if "present perfect" in objective_lower:
        blocks.append(
            {
                "label": "Present Perfect",
                "title": "Present perfect for completed experience",
                "explanation": "Use have or has plus a past participle to connect a past action with its present result.",
                "examples": [
                    "The team has completed the first inspection.",
                    f"The supervisor has reviewed the {tool_two} notes.",
                    "Students have improved their technical vocabulary this unit.",
                ],
                "frames": [
                    "The team has ...",
                    "The operator has already ...",
                    "We have learned that ...",
                ],
            }
        )

    if "used to" in objective_lower:
        blocks.append(
            {
                "label": "Used To",
                "title": "Used to for past habits and changes",
                "explanation": "Use used to when comparing an old practice with a current or newer method.",
                "examples": [
                    "Workers used to record results by hand.",
                    f"The team used to rely only on the {tool_one}.",
                    "They did not use to share digital reports after each task.",
                ],
                "frames": [
                    "Workers used to ... but now they ...",
                    "The process used to ...",
                    "We did not use to ...",
                ],
            }
        )

    if "connector" in objective_lower or "conector" in objective_lower or any(token in objective_lower for token in ["contrast", "cause", "effect", "although", "however", "therefore"]):
        blocks.append(
            {
                "label": "Connectors",
                "title": "Connectors for cause, contrast, and result",
                "explanation": "Use connectors to show why something happens, how two ideas differ, or what result follows from a decision.",
                "examples": [
                    "The part was replaced because it was damaged.",
                    "However, the second option required more time.",
                    "As a result, the final system worked more safely.",
                ],
                "frames": [
                    "___ because ...",
                    "However, ...",
                    "As a result, ...",
                ],
            }
        )

    if "simple present" in objective_lower or "present simple" in objective_lower:
        blocks.append(
            {
                "label": "Simple Present",
                "title": "Simple present for routines and procedures",
                "explanation": "Use simple present to describe regular actions, professional routines, and standard technical procedures.",
                "examples": [
                    f"The technician checks the {tool_one} every morning.",
                    f"The operator uses the {tool_two} during the main stage.",
                    "The team records the result at the end of the shift.",
                ],
                "frames": [
                    "The technician checks ...",
                    "The team uses ...",
                    "At the end, the operator records ...",
                ],
            }
        )

    if not blocks:
        blocks.append(
            {
                "label": "Technical English",
                "title": "Technical English in context",
                "explanation": "Focus on how the text combines action, evidence, and technical vocabulary to make the task clear and repeatable.",
                "examples": [
                    f"The {tool_one} is checked before the task begins.",
                    f"The {tool_two} gives evidence for the next decision.",
                    "The final note explains the result and the safety action.",
                ],
                "frames": [
                    "First, the team ...",
                    "The key evidence is ...",
                    "The final result shows that ...",
                ],
            }
        )

    return blocks[:3]


def build_oral_sequence_reading(course, glossary, oral_sequence):
    context = COURSE_CONTEXT[course["course_key"]]
    profile = level_profile(course["course_key"])
    tool_one = context["equipment"][0]
    tool_two = context["equipment"][1]
    key_word = glossary[0][0]
    support_word = glossary[1][0]

    if oral_sequence["family"] == "1ro":
        paragraphs_by_stage = {
            1: [
                f"In the school technical workshop, the student chooses one process or mechanism for the final oral task. The topic must be connected to real practice and easy to explain step by step.",
                f"The first planning card includes the name of the process, one important material, and one useful tool such as the {tool_one}. It also explains why the process matters for safe work.",
                "The teacher asks the class to think about audience and purpose: who needs the explanation, and what must that person understand after listening?",
                f"A partner checks whether the topic is clear, realistic, and supported by vocabulary from the unit like {key_word} and {support_word}.",
                "By the end of the lesson, the student has a simple topic plan for the June oral task and knows what information must still be collected.",
            ],
            2: [
                "After choosing the topic, the student reads a short manual, diagram, or data sheet to identify the order of actions in the process.",
                "Important notes include the main components, one measurement or technical specification, and the safety detail that cannot be forgotten during the explanation.",
                f"The vocabulary bank grows with words that will appear in the oral task, especially terms linked to {tool_one}, {tool_two}, and the workshop routine.",
                "The student groups information into beginning, middle, and final result so the explanation will sound organized instead of improvised.",
                "At this stage, the goal is not to memorize a script yet, but to collect solid evidence that can support the speaking task later.",
            ],
            3: [
                "With the evidence ready, the student organizes the oral explanation into a clear opening, a sequence of actions, and a practical conclusion.",
                "Simple connectors help the message sound natural: first, then, after that, finally. Passive voice and relative clauses make the description more technical.",
                f"The speaker chooses where to use vocabulary like {key_word} and {support_word} so the explanation sounds connected to the English of the workshop.",
                "An outline replaces long sentences. Short notes are easier to remember and allow the student to speak instead of reading every line.",
                "A good oral text at this stage sounds ordered, useful, and focused on what another student technician really needs to understand.",
            ],
            4: [
                "Before the final delivery, the student rehearses the explanation with notes, a diagram, or a small visual support.",
                "A partner listens with a checklist: Was the sequence clear? Was the pronunciation understandable? Did the speaker include the safety point and the final result?",
                "The speaker then adjusts the outline, removes unnecessary words, and practises difficult technical vocabulary one more time.",
                f"Short rehearsals help the student control time and speak more confidently when mentioning details related to {tool_one} or {tool_two}.",
                "By the end of rehearsal day, the explanation should be clear enough to present in two or three minutes without reading a full script.",
            ],
            5: [
                "On presentation day, the student introduces the chosen process, explains the main steps, and highlights one important technical or safety detail.",
                "The oral task must sound organized, with a clear beginning, a logical sequence, and a short conclusion about why the process matters in practice.",
                f"Strong answers reuse vocabulary from the unit, especially terms such as {key_word} and {support_word}, instead of speaking only in general words.",
                "After the explanation, the teacher may ask one or two simple follow-up questions to check understanding, confidence, and use of English.",
                "The final goal is not only to speak, but to show that the student can explain technical knowledge clearly to another person.",
            ],
        }
        answers_by_stage = {
            1: [
                "The text presents the first stage of the oral task: choosing a process or mechanism connected to workshop practice.",
                "Before the full explanation starts, the student defines the topic, audience, and purpose of the oral task.",
                f"Important details include one material, one tool like the {tool_one}, and vocabulary such as {key_word} and {support_word}.",
                "The text uses planning language to show that technical speaking needs order and preparation, not improvisation.",
                "At the end, the student has a clear topic plan and knows what information is still needed.",
                "A good technical explanation begins with a realistic topic and a clear idea of why the process matters.",
            ],
            2: [
                "The text focuses on collecting steps, technical details, and vocabulary that will support the oral task.",
                "Before speaking, the student reads sources and organizes the information into a logical order.",
                f"Important details include components, a technical specification, a safety point, and words related to {tool_one} and {tool_two}.",
                "The language focus is on selecting precise information that can later be explained clearly in English.",
                "At the end, the student has an evidence bank instead of only a general idea.",
                "Good oral work depends on evidence taken from texts, diagrams, and technical notes.",
            ],
            3: [
                "The text explains how to build the structure of the oral explanation.",
                "Before the final version, the student prepares an opening, a sequence of steps, and a conclusion.",
                f"Key details include connectors, passive voice, relative clauses, and technical words like {key_word} and {support_word}.",
                "The language focus shows how grammar and organization help technical ideas sound clearer.",
                "At the end, the student has an outline that is easier to speak from than a full script.",
                "Technical communication improves when ideas are organized into clear parts with useful language frames.",
            ],
            4: [
                "The text presents the rehearsal stage before the final oral delivery.",
                "Before the presentation, the student practises with notes, a partner, and a feedback checklist.",
                "Important details include timing, pronunciation, visual support, and the safety point inside the explanation.",
                "The language focus is on clarity and confidence, because good ideas still need understandable delivery.",
                "At the end, the student revises the outline and prepares a stronger final version.",
                "Practice helps technical speaking become clearer, shorter, and more confident.",
            ],
            5: [
                "The text describes the final oral presentation of the technical process.",
                "Before the conclusion, the student introduces the topic, explains the steps, and answers follow-up questions.",
                f"Important details include the sequence of actions, the safety note, and vocabulary such as {key_word} and {support_word}.",
                "The language focus shows that technical English must be both accurate and understandable for the audience.",
                "At the end, the listener understands why the process matters in real workshop practice.",
                "A solid oral task shows knowledge, sequence, and confidence at the same time.",
            ],
        }
    else:
        paragraphs_by_stage = {
            1: [
                f"At the beginning of the June oral project, the team selects one workplace case connected to {context['specialty']}. The situation must be specific enough to analyse and defend in front of an audience.",
                f"The planning card defines the audience, the operational problem, and one initial source of evidence such as a report, a checklist, or notes related to the {tool_one}.",
                "The group also decides what professional question will guide the oral intervention: what is happening, why does it matter, and what should be done next?",
                f"During pair discussion, classmates challenge vague ideas so the final focus becomes more precise and uses technical language like {key_word} and {support_word}.",
                "By the end of this stage, the speaker has a defendable topic and a clear purpose for the oral task of June.",
            ],
            2: [
                "Once the case is chosen, the team gathers evidence from manuals, reports, data tables, or class readings to support the future presentation.",
                f"Useful notes include the main cause of the problem, its impact on the workplace, and the technical references connected to equipment such as the {tool_one} or {tool_two}.",
                "The vocabulary bank becomes more precise because the speaker needs words that describe evidence, risk, sequence, and recommendation in a professional tone.",
                "Instead of copying full paragraphs, the group organizes information into short evidence points that can be explained naturally during the oral task.",
                "A strong oral analysis begins with reliable evidence, not only with opinions or isolated vocabulary.",
            ],
            3: [
                "At this stage, the oral intervention is organized into four parts: opening, case description, evidence-based recommendation, and professional closing.",
                "The speaker decides how to connect ideas with cause-effect language, contrast, and justification so the audience can follow the argument step by step.",
                f"Technical vocabulary such as {key_word} and {support_word} is placed where it strengthens meaning rather than where it sounds memorized or forced.",
                "The presentation outline stays concise: the goal is to defend an idea with clarity, not to read a long text from paper or screen.",
                "By the end of the lesson, the case has become a structured oral argument with a clear recommendation and professional tone.",
            ],
            4: [
                "Before the final delivery, the speaker rehearses the technical case with a partner who listens critically and notes strengths and weak points.",
                "Feedback focuses on clarity of the problem, quality of evidence, pronunciation of key terms, and whether the recommendation sounds feasible in a real workplace.",
                "The rehearsal may include a quick visual aid, a diagram, or a short note card that helps the speaker control time without losing eye contact with the audience.",
                "After the rehearsal, the outline is adjusted so the final version sounds more direct, better supported, and easier to defend under questions.",
                "This stage turns information into performance: the goal is not only to know the case, but to communicate it convincingly.",
            ],
            5: [
                "During the final oral task, the speaker presents the technical case, explains the key evidence, and defends one practical recommendation for the situation.",
                "A strong presentation sounds organized from the first sentence: the audience understands the context, the problem, the evidence, and the proposed response.",
                f"Precise vocabulary such as {key_word} and {support_word} helps the analysis sound professional and connected to {context['specialty']} rather than generic.",
                "After the presentation, follow-up questions test whether the speaker can justify the recommendation and adapt the explanation in real time.",
                "The final objective is to show technical judgement, clear English, and the ability to defend a solution under brief questioning.",
            ],
        }
        answers_by_stage = {
            1: [
                "The text presents the first stage of the June oral project: selecting a workplace case and defining the purpose of the presentation.",
                "Before the full analysis starts, the team identifies the audience, the core problem, and the first source of evidence.",
                f"Important details include the technical setting, evidence related to the {tool_one}, and vocabulary such as {key_word} and {support_word}.",
                "The language focus shows that professional speaking begins by narrowing the topic and clarifying the central question.",
                "At the end, the speaker has a defendable case and a clear reason for presenting it.",
                "Technical communication improves when the problem is specific and the purpose of the explanation is explicit.",
            ],
            2: [
                "The text focuses on gathering evidence and technical vocabulary for the oral analysis.",
                "Before speaking, the team reviews reports, readings, or tables and organizes the most relevant information.",
                f"Important details include causes, consequences, and references connected to the {tool_one} or {tool_two}.",
                "The language focus shows that good oral arguments depend on evidence rather than unsupported opinion.",
                "At the end, the group has a stronger evidence bank to use in the presentation.",
                "Reliable evidence makes the final recommendation more convincing and professional.",
            ],
            3: [
                "The text explains how to structure the oral argument into clear professional sections.",
                "Before the final version, the speaker organizes the case description, the evidence, the recommendation, and the closing.",
                f"Key details include connectors for cause and contrast, plus technical words such as {key_word} and {support_word}.",
                "The language focus shows how structure helps the audience follow a technical recommendation step by step.",
                "At the end, the case has become a concise oral argument rather than a collection of disconnected notes.",
                "Professional speaking is stronger when the listener can clearly follow the problem, evidence, and solution.",
            ],
            4: [
                "The text presents the rehearsal stage with peer feedback before the final oral task.",
                "Before delivery, the speaker practises timing, pronunciation, and the defence of the recommendation.",
                "Important details include feedback on clarity, evidence, feasibility, and oral control during questioning.",
                "The language focus shows that technical accuracy still needs clear spoken delivery and confident transitions.",
                "At the end, the outline is revised into a stronger final version.",
                "Feedback helps turn a prepared case into a persuasive oral performance.",
            ],
            5: [
                "The text describes the final oral presentation of the technical case and recommendation.",
                "Before the conclusion, the speaker explains the problem, supports it with evidence, and defends one practical solution.",
                f"Important details include the workplace context, the recommendation, and the technical vocabulary used to justify it.",
                "The language focus shows that professional English requires both content control and the ability to respond to questions.",
                "At the end, the audience understands the case and the logic behind the proposed action.",
                "A strong oral analysis shows technical judgement, evidence, and communication skills together.",
            ],
        }

    return {
        "title": f"Reading Model — {oral_sequence['stage_title']}",
        "paragraphs": paragraphs_by_stage[oral_sequence["stage"]],
        "questions": profile["question_stems"],
        "answers": answers_by_stage[oral_sequence["stage"]],
        "cefr": profile["cefr"],
        "reading_note": f"Modelo guiado {profile['cefr']} para la etapa {oral_sequence['stage']}/{oral_sequence['total_stages']} del {oral_sequence['project_name'].lower()}: {oral_sequence['stage_goal']}",
    }


def build_reading_content(course, unit_number, unit_title, class_data, glossary, eval_kind, oral_sequence=None):
    if oral_sequence:
        return build_oral_sequence_reading(course, glossary, oral_sequence)
    profile = level_profile(course["course_key"])
    context = COURSE_CONTEXT[course["course_key"]]
    focus = infer_focus(class_data["objective"])
    focus_blocks = detect_language_focuses(class_data["objective"], context)
    tool_one = context["equipment"][0]
    tool_two = context["equipment"][1]
    key_word = glossary[0][0]
    support_word = glossary[1][0]
    language_focus = focus_blocks[0]["label"]
    focus_label = FOCUS_DESCRIPTIONS.get(focus, "a technical task")

    if profile["cefr"] == "A2":
        paragraphs = [
            f"In the {context['workplace']}, a student team is working on {focus_label} linked to {unit_title}. Their task is to understand how a {context['product']} is prepared, checked, and explained in English.",
            f"Before the main procedure begins, the {tool_one} is prepared and the class reads a short note about {key_word}. The teacher asks students to notice the technical verbs and the words that help the reader follow the order of the task.",
            f"During the activity, the {tool_two} is used to complete an important stage of the job. Each action is recorded in clear sentences so the next person can understand what is done, what is checked, and what must happen next.",
            f"A small difficulty appears when one step is not fully clear, so the students compare evidence, review the glossary, and revisit the example box for {language_focus}. This helps them decide which detail is essential and which detail only gives extra context.",
            f"In the final stage, the group writes a short conclusion, explains the result, and suggests one safety action. The reading shows that technical English is useful because it supports accuracy, teamwork, and better decisions in the workshop.",
        ]
        answers = [
            f"The text describes {focus_label} in the {context['workplace']}.",
            f"Before the main task starts, the team prepares the {tool_one} and reads the note about {key_word}.",
            f"The {tool_one}, the {tool_two}, and the glossary notes are important sources of information.",
            f"The text highlights {language_focus} through model sentences and technical examples.",
            "The team finishes by explaining the result and suggesting one safety action.",
            "Good technical work depends on clear notes, accurate vocabulary, and careful checking.",
        ]
    else:
        paragraphs = [
            f"At the start of the shift in the {context['workplace']}, a team is asked to solve {focus_label} connected to {unit_title}. The text follows the way technical information is interpreted before any action is taken.",
            f"The supervisor first reviews the record of the previous task, the available materials, and the quality criteria expected for the {context['product']}. This context matters because the team cannot choose a valid response until the evidence is organized.",
            f"As the procedure develops, the {tool_one} and the {tool_two} provide the key evidence for the decision-making process. Notes, measurements, and short explanations are compared in order to distinguish routine data from signs of a real problem or opportunity.",
            f"The writer also uses {language_focus} to connect ideas precisely and to clarify relationships between cause, sequence, contrast, or responsibility. Because of that, the reader can understand not only what happens, but also why a certain action is preferred.",
            f"By the end of the text, the team reaches a justified conclusion, records the outcome, and proposes one improvement for future work. The passage suggests that technical English is valuable when evidence must be communicated clearly to classmates, supervisors, or clients.",
        ]
        answers = [
            f"The text presents {focus_label} in a professional setting.",
            f"Before the procedure advances, the team reviews previous records, materials, and quality criteria for the {context['product']}.",
            f"The {tool_one}, the {tool_two}, and the written notes guide the team's decisions.",
            f"The text uses {language_focus} to organize relationships between ideas more precisely.",
            "The team reaches a justified conclusion and proposes one improvement for future work.",
            "The broader lesson is that technical communication must be evidence-based, accurate, and easy to transfer to others.",
        ]

    if eval_kind == "oral":
        title = FOCUS_TITLES["oral"]
        paragraphs = [
            f"Before the oral presentation begins, the {context['role']} studies a short technical situation in the {context['workplace']}. The speaker must explain the purpose of the task and the expected result in a clear order.",
            f"First, the {tool_one} is checked and the main objective is stated. The explanation does not start with isolated words; it starts with a complete idea that helps the audience understand the context.",
            f"Next, the speaker describes the central action carried out with the {tool_two}. Technical vocabulary is selected carefully so the explanation sounds precise instead of vague.",
            f"After that, the speaker adds one difficulty, one decision, and one safety recommendation. This middle section is important because it shows control of both content and professional reasoning.",
            f"Finally, the explanation closes with the result and one reflection about what the audience should remember. The model text shows that a good oral report is organized, informative, and easy to follow.",
        ]
        answers = [
            "The speaker prepares an English explanation of a technical task.",
            f"The first action is checking the {tool_one} and stating the purpose of the task.",
            f"The text mentions the {tool_one}, the {tool_two}, and the technical vocabulary linked to the explanation.",
            "The model shows the language focus through clear sequencing and precise sentence patterns.",
            "The speaker closes with the result and one final reflection.",
            "It can be inferred that the speaker needs to be organized, accurate, and audience-aware.",
        ]
    elif eval_kind == "reading":
        title = "Reading Assessment Text"
        paragraphs = [
            f"A team in the {context['workplace']} is completing a final task for Unit {unit_number}. The aim is to review how a {context['product']} is prepared, checked, and communicated in English under realistic workshop conditions.",
            f"Before the work starts, the team reviews the instructions, the available materials, and the criteria that will be used to judge quality. This initial control prevents confusion later in the process.",
            f"During the main stage, the {tool_one} and the {tool_two} are used to gather evidence and complete the technical task. At the same time, the team writes short notes that explain what has been done and what still needs attention.",
            f"A disagreement appears when two students interpret one instruction differently, so they return to the text, compare evidence, and justify their reading. This moment shows why careful comprehension matters in technical settings.",
            f"At the end, the group compares the result with the original instructions and proposes one improvement for the next attempt. The assessment text suggests that clear reading, accurate vocabulary, and evidence-based decisions improve safety and teamwork.",
        ]
        answers = [
            f"The team is reviewing a final Unit {unit_number} technical task in a realistic workshop situation.",
            f"They begin by reviewing instructions, materials, and quality criteria before touching the equipment.",
            f"The {tool_one}, the {tool_two}, and the written notes provide the key evidence.",
            f"The text shows {language_focus} through the way information is clarified and justified.",
            "The group ends by proposing one improvement for the next attempt.",
            "It can be inferred that careful reading is essential before using equipment or reporting results.",
        ]
    else:
        title = FOCUS_TITLES.get(focus, "Reading Text — Technical English in context")

    return {
        "title": title,
        "paragraphs": paragraphs,
        "questions": profile["question_stems"],
        "answers": answers,
        "cefr": profile["cefr"],
        "reading_note": profile["reading_note"],
    }


def build_language_support_html(course, class_data):
    profile = level_profile(course["course_key"])
    context = COURSE_CONTEXT[course["course_key"]]
    cards = []
    for block in detect_language_focuses(class_data["objective"], context):
        example_items = "".join(f"<li>{example}</li>" for example in block["examples"])
        frame_items = "".join(f"<li>{frame}</li>" for frame in block["frames"])
        cards.append(
            f"""
            <div class=\"focus-card\">
                <h5>{block['title']}</h5>
                <p>{block['explanation']}</p>
                <div class=\"focus-subtitle\">Examples</div>
                <ul>{example_items}</ul>
                <div class=\"focus-subtitle\">Sentence frames</div>
                <ul>{frame_items}</ul>
            </div>
            """
        )

    return f"""
    <div class=\"task-box activity-card\">
        <h4>🧠 Actividad 2 — Language Focus</h4>
        <p>Use these examples before reading. The class text is written at {profile['cefr']} level and the structures below will help you understand, discuss, and write about the topic with more precision.</p>
        <div class=\"focus-grid\">{''.join(cards)}</div>
    </div>
    """


def build_glossary_html(glossary):
    cards = []
    for word, translation, pronunciation in glossary:
        cards.append(
            f"""
            <div class=\"vocab-card\">
                <div class=\"word\">{word}</div>
                <div class=\"meaning\">{definition_for_term(word, translation)}</div>
                <div class=\"pronunciation\">Pron.: {pronunciation}</div>
            </div>
            """
        )
    return "".join(cards)


def build_question_html(reading):
    blocks = []
    for index, question in enumerate(reading["questions"], start=1):
        answer_id = f"answer-{index}"
        blocks.append(
            f"""
            <div class=\"question-card\">
                <p><strong>{index}.</strong> {question}</p>
                <button class=\"toggle-btn\" onclick=\"toggleAnswer('{answer_id}', this)\">Ver respuesta</button>
                <div class=\"answer-box\" id=\"{answer_id}\">{reading['answers'][index - 1]}</div>
            </div>
            """
        )
    return "".join(blocks)


def build_review_html(review):
    items = "".join(f"<li>{step}</li>" for step in review["steps"])
    return f"<div class=\"review-box\"><h4>🔁 {review['title']}</h4><ul>{items}</ul></div>"


def build_oral_sequence_box(oral_sequence):
    requirement_items = "".join(f"<li>{item}</li>" for item in oral_sequence["requirements"])
    return f"""
    <div class="review-box">
        <h4>🎤 Ruta del trabajo oral</h4>
        <p><strong>{oral_sequence['project_name']}</strong> · Etapa {oral_sequence['stage']}/{oral_sequence['total_stages']} · {oral_sequence['due_note']}</p>
        <p><strong>Meta de hoy:</strong> {oral_sequence['stage_goal']}</p>
        <p><strong>Producto esperado:</strong> {oral_sequence['stage_output']}</p>
        <ul>{requirement_items}</ul>
    </div>
    """


def build_activity_card(title, intro, items, extra_html=""):
    item_list = "".join(f"<li>{item}</li>" for item in items)
    return f"""
    <div class=\"task-box activity-card\">
        <h4>{title}</h4>
        <p>{intro}</p>
        <ol class=\"task-steps\">{item_list}</ol>
        {extra_html}
    </div>
    """


def build_launch_html(course, class_data, review, oral_sequence=None):
    context = COURSE_CONTEXT[course["course_key"]]
    steps = [
        f"Read the objective of the lesson and circle the technical action linked to the {context['product']}.",
        review["steps"][0],
        f"Predict which tools or key ideas may appear in a text about the {context['specialty']} context.",
        "Share one sentence with a partner: what do you already know and what do you still need to clarify before reading?",
    ]
    return build_activity_card(
        "🔎 Actividad 1 — Activate and Predict",
        "Start the class by connecting prior knowledge with the new text and the new language focus.",
        steps,
        build_review_html(review) + (build_oral_sequence_box(oral_sequence) if oral_sequence else ""),
    )


def build_closure_html(course, class_data, reading, eval_kind, oral_sequence=None):
    if oral_sequence:
        prompts_by_stage = {
            1: [
                "Write the process or case you chose and explain why it is useful for the oral task.",
                "List the first technical words you still need to understand better.",
                "Note one question you must answer before the next class.",
            ],
            2: [
                "Write two pieces of evidence or technical details you collected today.",
                "Identify the vocabulary item that will be most useful in your presentation.",
                "Explain what information is still missing before you can build the oral outline.",
            ],
            3: [
                "Write your opening sentence and your final conclusion in short note form.",
                "Check whether your explanation already has a clear order and one strong connector.",
                "Name the section of the presentation that still needs more detail or clearer English.",
            ],
            4: [
                "Write one strength and one improvement point from today's rehearsal.",
                "Note the technical word or phrase you need to pronounce more clearly.",
                "Explain what you will adjust before the final oral delivery.",
            ],
            5: [
                "Reflect on one part of your oral work that sounded clear and professional.",
                "Write the follow-up question that was easiest or hardest to answer.",
                "State one concrete improvement for your next technical presentation in English.",
            ],
        }
        return build_activity_card(
            "🟣 Cierre — Oral Project Checkpoint",
            "Close the lesson by checking progress on the oral task and defining the next step in the sequence.",
            [
                "Review your notes and identify the strongest contribution from today's stage.",
                "Compare your progress with a partner before writing your final exit ticket.",
                "Complete the three checkpoint prompts below.",
            ],
            """
            <div class="exit-ticket">
                <h5>Exit ticket prompts</h5>
                <ul>{}</ul>
            </div>
            """.format("".join(f"<li>{prompt}</li>" for prompt in prompts_by_stage[oral_sequence["stage"]])),
        )
    if eval_kind == "oral":
        prompts = [
            "Write the opening sentence you will use in your oral explanation.",
            "Add one technical term from the glossary and one safety recommendation.",
            "Check that your closing sentence states a result or takeaway clearly.",
        ]
    elif eval_kind == "reading":
        prompts = [
            "Write one sentence that explains the main idea of the assessment text.",
            "Choose one answer and justify it with evidence from the reading.",
            "State one vocabulary item that was essential for comprehension.",
        ]
    else:
        prompts = [
            "Write one sentence that summarizes the main idea of the text.",
            "Use one glossary term and one language structure from the class in a new sentence.",
            "Explain what detail or instruction would help you repeat the task more safely next time.",
        ]

    return build_activity_card(
        "🟣 Cierre — Exit Ticket and Reflection",
        "Close the lesson by checking comprehension, transferring language to a new context, and recording one final insight.",
        [
            "Review your notes and choose the most useful technical idea from the class.",
            "Discuss your answer with a partner before writing the final version.",
            "Complete the three exit-ticket prompts below.",
        ],
        """
        <div class=\"exit-ticket\">
            <h5>Exit ticket prompts</h5>
            <ul>{}</ul>
        </div>
        """.format("".join(f"<li>{prompt}</li>" for prompt in prompts)),
    )


def build_applied_task(course, class_data, eval_kind, oral_sequence=None):
    if oral_sequence:
        if oral_sequence["family"] == "1ro":
            task_steps = {
                1: [
                    "Choose one process, machine, or mechanism from workshop practice.",
                    "Complete a planning card with topic, purpose, audience, and five key words.",
                    "Explain your choice to a partner in 30 seconds using one opening sentence.",
                ],
                2: [
                    "Extract the main steps, one technical specification, and one safety detail from the text or diagram.",
                    "Build an evidence bank with vocabulary you will need in the oral task.",
                    "Check with a partner that the sequence is logical and complete.",
                ],
                3: [
                    "Write a short oral outline with opening, sequence of steps, safety note, and closing.",
                    "Add passive voice, one relative clause, and connectors such as first, then, and finally.",
                    "Practise a 45-second version without reading full sentences.",
                ],
                4: [
                    "Rehearse the oral task with a timer and a simple visual or note card.",
                    "Use a peer checklist: clarity, pronunciation, sequence, vocabulary, and confidence.",
                    "Revise the outline so the final version can be delivered in 2-3 minutes.",
                ],
                5: [
                    "Deliver the oral task individually using your final outline and visual support if needed.",
                    "Answer one or two follow-up questions from the teacher or classmates.",
                    "Complete a short self-assessment about clarity, technical vocabulary, and confidence.",
                ],
            }
        else:
            task_steps = {
                1: [
                    "Select one technical case or workplace problem that deserves analysis.",
                    "Complete a project card with audience, context, central question, and first source of evidence.",
                    "Pitch the case to a partner in 30-45 seconds and refine the focus after feedback.",
                ],
                2: [
                    "Collect evidence from reports, manuals, tables, or previous readings.",
                    "Organize the notes into problem, cause, consequence, and possible recommendation.",
                    "Highlight the vocabulary that makes the analysis sound professional and precise.",
                ],
                3: [
                    "Build the oral outline with opening, case description, evidence, recommendation, and closing.",
                    "Add cause-effect and contrast connectors so the audience can follow your reasoning.",
                    "Practise a one-minute version focused on clarity and professional tone.",
                ],
                4: [
                    "Rehearse the case with a partner who checks evidence, feasibility, pronunciation, and timing.",
                    "Adjust the recommendation so it sounds realistic for the workplace context.",
                    "Prepare the final note card or visual support for the June oral task.",
                ],
                5: [
                    "Present the technical case, defend your recommendation, and close with a professional conclusion.",
                    "Respond to follow-up questions using evidence from the sequence of classes.",
                    "Write one reflective note about what made your analysis convincing or unclear.",
                ],
            }
        requirement_items = "".join(f"<li>{item}</li>" for item in oral_sequence["requirements"])
        return (
            "Actividad Aplicada — Ruta del trabajo oral",
            f"""
            <p><strong>{oral_sequence['project_name']}</strong> · Etapa {oral_sequence['stage']}/{oral_sequence['total_stages']}</p>
            <p><strong>Prompt:</strong> <em>{oral_sequence['prompt']}</em></p>
            <ol class="task-steps">{''.join(f'<li>{step}</li>' for step in task_steps[oral_sequence['stage']])}</ol>
            <p><strong>Producto esperado:</strong> {oral_sequence['stage_output']}</p>
            <ul>{requirement_items}</ul>
            """,
        )
    focus = infer_focus(class_data["objective"])
    specialty = COURSE_CONTEXT[course["course_key"]]["specialty"]
    if eval_kind == "oral":
        return (
            "Trabajo Oral Evaluado",
            """
            <ol class=\"task-steps\">
                <li>Plan a 60-90 second explanation with a clear opening, middle, and closing.</li>
                <li>Name the purpose of the task, the tools or materials involved, and the order of the main actions.</li>
                <li>Add one difficulty or key decision and one safety recommendation linked to the task.</li>
                <li>Rehearse with the frames <em>first</em>, <em>then</em>, <em>after that</em>, and <em>finally</em>.</li>
                <li>Before presenting, check clarity, technical vocabulary, logical sequence, and pronunciation.</li>
            </ol>
            """,
        )
    if eval_kind == "reading":
        return (
            "Prueba Final de Comprensión Lectora",
            """
            <ol class=\"task-steps\">
                <li>Read the text independently and underline the sentence that gives the main task, problem, or recommendation.</li>
                <li>Answer the questions by returning to the text; do not rely only on memory.</li>
                <li>Mark the technical terms that help you identify evidence, sequence, cause, or contrast.</li>
                <li>Justify at least one answer orally using a direct quotation or a precise reference to the text.</li>
                <li>Use the hidden answer buttons only for teacher review or self-correction after finishing.</li>
            </ol>
            """,
        )
    if focus == "instructions":
        return (
            "Actividad Aplicada — Secuencia de pasos",
            """
            <ol class=\"task-steps\">
                <li>Underline the verbs that show the order of the procedure in the reading.</li>
                <li>Transfer the information to the organizer and add one safety note for each stage.</li>
                <li>Explain the sequence to a partner using complete sentences, not isolated words.</li>
            </ol>
            <table class=\"activity-table\">
                <tr><th>Step</th><th>Action</th><th>Tool / Material</th><th>Safety Note</th></tr>
                <tr><td>1</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>2</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>3</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            </table>
            """,
        )
    if focus in {"troubleshooting", "report"}:
        return (
            "Actividad Aplicada — Problema, evidencia y solución",
            """
            <ol class=\"task-steps\">
                <li>Identify the central problem or reportable issue in the text.</li>
                <li>Select the technical evidence that supports the diagnosis or conclusion.</li>
                <li>Write a solution or recommendation that matches the evidence and the professional context.</li>
            </ol>
            <table class=\"activity-table\">
                <tr><th>Problem</th><th>Evidence from the text</th><th>Possible solution</th></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            </table>
            """,
        )
    if focus == "comparison":
        return (
            "Actividad Aplicada — Comparar opciones",
            """
            <ol class=\"task-steps\">
                <li>Write one advantage and one limitation for each option described in the text.</li>
                <li>Decide which option you would choose and justify your choice with two pieces of evidence.</li>
                <li>Share your conclusion with a partner using <em>however</em>, <em>because</em>, and <em>therefore</em>.</li>
            </ol>
            """,
        )
    if focus == "oral":
        return (
            "Actividad Aplicada — Speaking frames",
            """
            <ol class=\"task-steps\">
                <li>Use the frames to organize your explanation in a clear order.</li>
                <li>Replace the blanks with technical vocabulary from the glossary and the reading.</li>
                <li>Practise once with a partner and once independently before presenting.</li>
            </ol>
            <ul>
                <li><em>First, the technician checks...</em></li>
                <li><em>Then, the team uses...</em></li>
                <li><em>The main problem is...</em></li>
                <li><em>Finally, the result is...</em></li>
            </ul>
            """,
        )
    return (
        "Actividad Aplicada — Síntesis técnica",
        f"""
        <ol class=\"task-steps\">
            <li>Resume the main idea of the class in relation to {specialty}.</li>
            <li>Write two pieces of evidence from the text that support your summary.</li>
            <li>Explain how the reading connects with a real task from the workshop, lab, or production area.</li>
        </ol>
        """,
    )


def build_class_html(course, unit_number, unit_info, class_data, previous_class):
    eval_kind = evaluation_kind(unit_number, class_data, len(unit_info["classes"]))
    oral_sequence = oral_project_sequence(course, unit_number, class_data)
    glossary = select_glossary(course["course_key"], unit_number)
    reading = build_reading_content(course, unit_number, unit_info["unit_title"], class_data, glossary, eval_kind, oral_sequence)
    task_title, task_body = build_applied_task(course, class_data, eval_kind, oral_sequence)
    review = review_prompt(previous_class, unit_number)
    badge_text = " · ".join(class_data["badges"]) or "OA — En desarrollo"
    is_evaluation = class_is_evaluation(class_data, eval_kind)
    eval_pill = "<span>📝 Evaluación</span>" if is_evaluation else "<span>🧩 Clase de trabajo</span>"
    annual_meta = f"Clase anual {class_data['annual_number']}" if class_data["annual_number"] != class_data["unit_index"] else f"Clase {class_data['unit_index']}"
    resources = class_data["resources"] or "Texto adaptado, pizarra, guía de apoyo y recursos visuales de la especialidad."
    evaluation_note = class_data["evaluation"] or "Formativa: observación de participación, revisión de respuestas y salida escrita breve."
    if oral_sequence:
        resources = f"{resources} Producto de avance: {oral_sequence['stage_output']}"
        if not oral_sequence["is_delivery"]:
            evaluation_note = f"{evaluation_note} Evidencia de etapa: {oral_sequence['stage_output']}"
    link_title = short_title(class_data, unit_number, eval_kind, oral_sequence)
    launch_html = build_launch_html(course, class_data, review, oral_sequence)
    closure_html = build_closure_html(course, class_data, reading, eval_kind, oral_sequence)
    language_support_html = build_language_support_html(course, class_data)
    project_meta = f"<span>🎤 {oral_sequence['project_name']} · Etapa {oral_sequence['stage']}/{oral_sequence['total_stages']}</span>" if oral_sequence else ""

    return f"""<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Clase {class_data['unit_index']} — Unidad {unit_number} — {course['course_label']}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Inter', sans-serif; background: #f4f7fb; color: #1f2937; line-height: 1.65; }}
        .page {{ max-width: 1080px; margin: 0 auto; padding: 24px 18px 40px; }}
        .hero {{ background: linear-gradient(135deg, #0f766e, #155e75); color: white; border-radius: 18px; padding: 28px; box-shadow: 0 18px 40px rgba(15, 118, 110, 0.18); }}
        .hero h1 {{ font-size: 2rem; margin-bottom: 6px; }}
        .hero p {{ color: rgba(255,255,255,0.88); }}
        .meta {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; }}
        .meta span {{ background: rgba(255,255,255,0.18); padding: 6px 14px; border-radius: 999px; font-size: 0.84rem; }}
        .toolbar {{ display: flex; justify-content: flex-end; margin: 18px 0 10px; }}
        .print-btn {{ border: none; border-radius: 10px; background: #0f172a; color: white; padding: 10px 16px; font-weight: 600; cursor: pointer; }}
        .objective-card, .support-card, .section, .resource-card {{ background: white; border-radius: 16px; box-shadow: 0 10px 26px rgba(15, 23, 42, 0.08); margin-bottom: 18px; overflow: hidden; }}
        .objective-card {{ padding: 22px 24px; border-left: 6px solid #0f766e; }}
        .objective-card h2 {{ color: #0f766e; font-size: 1.05rem; margin-bottom: 8px; }}
        .section-header {{ color: white; font-weight: 700; padding: 14px 22px; font-size: 1rem; }}
        .inicio {{ background: #2e7d32; }}
        .desarrollo {{ background: #1565c0; }}
        .cierre {{ background: #7c3aed; }}
        .section-body {{ padding: 20px 22px 22px; }}
        .section-body ul {{ margin-left: 20px; }}
        .section-body li {{ margin-bottom: 8px; }}
        .review-box, .reading-box, .task-box, .eval-box, .resource-card {{ border: 1px solid #e5e7eb; border-radius: 14px; padding: 18px; background: #f8fafc; margin-top: 16px; }}
        .review-box h4, .reading-box h4, .task-box h4, .eval-box h4 {{ color: #0f172a; margin-bottom: 10px; }}
        .activity-card p {{ margin-bottom: 10px; }}
        .task-steps {{ margin-left: 20px; }}
        .task-steps li {{ margin-bottom: 8px; }}
        .glossary-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 14px; }}
        .vocab-card {{ background: white; border: 1px solid #dbeafe; border-radius: 12px; padding: 14px; }}
        .word {{ font-weight: 800; color: #1d4ed8; margin-bottom: 4px; }}
        .meaning {{ font-size: 0.92rem; color: #1f2937; }}
        .pronunciation {{ font-size: 0.8rem; color: #64748b; margin-top: 6px; }}
        .focus-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 14px; margin-top: 14px; }}
        .focus-card {{ background: white; border: 1px solid #d6e4ff; border-radius: 12px; padding: 14px; }}
        .focus-card h5 {{ color: #1d4ed8; margin-bottom: 8px; font-size: 0.98rem; }}
        .focus-card ul {{ margin-left: 18px; }}
        .focus-card li {{ margin-bottom: 6px; }}
        .focus-subtitle {{ margin-top: 10px; font-weight: 700; color: #0f172a; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.04em; }}
        .reading-box p {{ margin-bottom: 10px; }}
        .question-card {{ background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 14px; margin-top: 12px; }}
        .toggle-btn {{ margin-top: 10px; border: none; border-radius: 10px; background: #dbeafe; color: #1d4ed8; padding: 8px 12px; font-weight: 700; cursor: pointer; }}
        .answer-box {{ display: none; background: #eefbf3; border-left: 4px solid #16a34a; padding: 10px 12px; border-radius: 8px; margin-top: 10px; }}
        .answer-box.open {{ display: block; }}
        .activity-table {{ width: 100%; border-collapse: collapse; margin-top: 8px; }}
        .activity-table th, .activity-table td {{ border: 1px solid #cbd5e1; padding: 10px; text-align: left; }}
        .activity-table th {{ background: #e2e8f0; }}
        .reading-note {{ font-size: 0.9rem; color: #475569; margin-bottom: 12px; }}
        .exit-ticket {{ background: white; border: 1px dashed #cbd5e1; border-radius: 12px; padding: 14px; margin-top: 12px; }}
        .exit-ticket h5 {{ color: #0f172a; margin-bottom: 8px; }}
        .exit-ticket ul {{ margin-left: 18px; }}
        .resource-card h4 {{ color: #0f766e; margin-bottom: 8px; }}
        .footer-note {{ text-align: center; color: #6b7280; font-size: 0.82rem; margin-top: 28px; }}
        @media (max-width: 720px) {{
            .hero h1 {{ font-size: 1.55rem; }}
            .page {{ padding: 16px 12px 28px; }}
        }}
        @media print {{
            body {{ background: white; }}
            .toolbar {{ display: none; }}
            .hero, .objective-card, .support-card, .section, .resource-card {{ box-shadow: none; }}
        }}
    </style>
</head>
<body>
    <div class=\"page\">
        <div class=\"hero\">
            <h1>Clase {class_data['unit_index']} — Unidad {unit_number}</h1>
            <p>{course['course_label']} · {unit_info['unit_title']}</p>
            <div class=\"meta\">
                <span>🎯 {link_title}</span>
                <span>📘 {badge_text}</span>
                <span>🗂 {annual_meta}</span>
                {project_meta}
                {eval_pill}
            </div>
        </div>

        <div class=\"toolbar\">
            <button class=\"print-btn\" onclick=\"window.print()\">Imprimir / Guardar en PDF</button>
        </div>

        <div class=\"objective-card\">
            <h2>Objetivo de la clase</h2>
            <p>{class_data['objective']}</p>
        </div>

        <div class=\"section\">
            <div class=\"section-header inicio\">🟢 Inicio</div>
            <div class=\"section-body\">{launch_html}</div>
        </div>

        <div class=\"section\">
            <div class=\"section-header desarrollo\">🔵 Desarrollo</div>
            <div class=\"section-body\">
                {language_support_html}

                <div class=\"task-box\">
                    <h4>📚 Actividad 3 — Vocabulary for reading</h4>
                    <p>Review the key words before reading. Each card includes a short definition in English and pronunciation support so the vocabulary helps with comprehension, not only with translation.</p>
                    <div class=\"glossary-grid\">{build_glossary_html(glossary)}</div>
                </div>

                <div class=\"reading-box\">
                    <h4>📖 Actividad 4 — {reading['title']}</h4>
                    <p class=\"reading-note\">{reading['reading_note']}</p>
                    {''.join(f'<p>{paragraph}</p>' for paragraph in reading['paragraphs'])}
                </div>

                <div class=\"task-box\">
                    <h4>📝 Actividad 5 — Reading comprehension</h4>
                    <p>Answer the questions by returning to the text. Focus on evidence, sequence, language use, and professional meaning before checking the answer key.</p>
                    {build_question_html(reading)}
                </div>

                <div class=\"task-box\">
                    <h4>🛠 Actividad 6 — {task_title}</h4>
                    {task_body}
                </div>

                <div class=\"eval-box\">
                    <h4>📋 Seguimiento de la clase</h4>
                    <p>{evaluation_note}</p>
                </div>
            </div>
        </div>

        <div class=\"section\">
            <div class=\"section-header cierre\">🟣 Cierre</div>
            <div class=\"section-body\">{closure_html}</div>
        </div>

        <div class=\"resource-card\">
            <h4>📦 Recursos sugeridos</h4>
            <p>{resources}</p>
            <p style=\"margin-top: 10px; color: #64748b; font-size: 0.9rem;\">Sugerencia: cerrar la sesión con un ticket de salida breve donde el estudiante escriba una palabra nueva, una idea clave y una aplicación técnica real.</p>
        </div>

        <p class=\"footer-note\">Guía de trabajo para estudiantes — Materiales de Clases 2026.</p>
    </div>

    <script>
        function toggleAnswer(id, button) {{
            const answer = document.getElementById(id);
            const isOpen = answer.classList.toggle('open');
            button.textContent = isOpen ? 'Ocultar respuesta' : 'Ver respuesta';
        }}
    </script>
</body>
</html>
"""


def relative_output_path(course, unit_number, class_data):
    file_code = course.get("u1_file_code", course["file_code"]) if unit_number == 1 else course["file_code"]
    filename = f"Clase_{class_data['unit_index']}_U{unit_number}_{file_code}.html"
    return Path(course["folder"]) / f"u{unit_number}" / filename


def instrument_entries_for_course(course):
    course_key = course["course_key"]

    if course_key == "1ro-lu-ju":
        return [
            {
                "icon": "📝",
                "title": "Evaluación Diagnóstica — 1° Medio",
                "href": "1ro-medio/instrumentos/diagnostico_1ro_medio.html",
                "tag": "Diagnóstico",
            },
            {
                "icon": "📋",
                "title": "Rúbrica — Video: My Future Career",
                "href": "1ro-medio/instrumentos/rubrica_video_my_future_career.html",
                "tag": "Rúbrica",
            },
            {
                "icon": "📝",
                "title": "Prueba — Comprensión Lectora U1 — 1° Medio",
                "href": "1ro-medio/instrumentos/PRUEBA_COMPRENSION_LECTORA_U1_1RO_MEDIO.docx",
                "tag": "Prueba",
            },
            {
                "icon": "🎤",
                "title": "Trabajo oral de cierre semestral — ruta de 5 clases",
                "href": "1ro-medio/lu-ju/u2/Clase_7_U2_1ro_LuJu.html",
                "tag": "Proyecto",
            },
        ]

    three_ro_courses = {
        "3A-industrial": {
            "diagnostic_href": "3ro-medio/instrumentos/diagnostico_3ro_industrial.html",
            "diagnostic_title": "Evaluación Diagnóstica — 3°A Mecánica Industrial",
            "test_href": "3ro-medio/instrumentos/PRUEBA_COMPRENSION_LECTORA_3RO_INDUSTRIAL.docx",
            "test_title": "Prueba — Comprensión Lectora TP — 3°A Mecánica Industrial",
        },
        "3B-automotriz": {
            "diagnostic_href": "3ro-medio/instrumentos/diagnostico_3ro_automotriz.html",
            "diagnostic_title": "Evaluación Diagnóstica — 3°B Mecánica Automotriz",
            "test_href": "3ro-medio/instrumentos/PRUEBA_COMPRENSION_LECTORA_3RO_AUTOMOTRIZ.docx",
            "test_title": "Prueba — Comprensión Lectora TP — 3°B Mecánica Automotriz",
        },
        "3C-electricidad": {
            "diagnostic_href": "3ro-medio/instrumentos/diagnostico_3ro_electricidad.html",
            "diagnostic_title": "Evaluación Diagnóstica — 3°C Electricidad",
            "test_href": "3ro-medio/instrumentos/PRUEBA_COMPRENSION_LECTORA_3RO_ELECTRICIDAD.docx",
            "test_title": "Prueba — Comprensión Lectora TP — 3°C Electricidad",
        },
        "3D-grafica": {
            "diagnostic_href": "3ro-medio/instrumentos/diagnostico_3ro_grafica.html",
            "diagnostic_title": "Evaluación Diagnóstica — 3°D Gráfica",
            "test_href": "3ro-medio/instrumentos/PRUEBA_COMPRENSION_LECTORA_3RO_GRAFICA.docx",
            "test_title": "Prueba — Comprensión Lectora TP — 3°D Gráfica",
        },
        "3E-electronica": {
            "diagnostic_href": "3ro-medio/instrumentos/diagnostico_3ro_electronica.html",
            "diagnostic_title": "Evaluación Diagnóstica — 3°E Electrónica",
            "test_href": "3ro-medio/instrumentos/PRUEBA_COMPRENSION_LECTORA_3RO_ELECTRONICA.docx",
            "test_title": "Prueba — Comprensión Lectora TP — 3°E Electrónica",
        },
    }

    if course_key in three_ro_courses:
        course_info = three_ro_courses[course_key]
        return [
            {
                "icon": "📝",
                "title": course_info["diagnostic_title"],
                "href": course_info["diagnostic_href"],
                "tag": "Diagnóstico",
            },
            {
                "icon": "📋",
                "title": "Rúbrica — My Technical Skills",
                "href": "3ro-medio/instrumentos/rubrica_video_my_technical_skills.html",
                "tag": "Rúbrica",
            },
            {
                "icon": "📝",
                "title": course_info["test_title"],
                "href": course_info["test_href"],
                "tag": "Prueba",
            },
        ]

    four_to_oral_projects = {
        "4A-industrial": {
            "href": "4to-medio/4A-industrial/u2/Clase_1_U2_4toA_Industrial.html",
            "title": "Trabajo oral de junio — ruta de 5 clases",
        },
        "4B-automotriz": {
            "href": "4to-medio/4B-automotriz/u2/Clase_1_U2_4toB_Automotriz.html",
            "title": "Trabajo oral de junio — ruta de 5 clases",
        },
        "4C-electricidad": {
            "href": "4to-medio/4C-electricidad/u2/Clase_1_U2_4toC_Electricidad.html",
            "title": "Trabajo oral de junio — ruta de 5 clases",
        },
        "4E-electronica": {
            "href": "4to-medio/4E-electronica/u2/Clase_1_U2_4toE_Electronica.html",
            "title": "Trabajo oral de junio — ruta de 5 clases",
        },
    }

    if course_key in four_to_oral_projects:
        project_info = four_to_oral_projects[course_key]
        return [
            {
                "icon": "🎤",
                "title": project_info["title"],
                "href": project_info["href"],
                "tag": "Proyecto",
            },
        ]

    return []


def write_targets(relative_path, content):
    for base in (SOURCE_SITE, PUBLISHED_SITE):
        destination = base / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")


def class_link_markup(relative_path, course_key, unit_number, class_data, eval_kind, use_archive_prefix=False):
    oral_sequence = oral_project_sequence(course_key, unit_number, class_data)
    title = short_title(class_data, unit_number, eval_kind, oral_sequence)
    is_evaluation = class_is_evaluation(class_data, eval_kind)
    tag_class = "tag-eval" if is_evaluation else "tag-clase"
    tag_text = "Evaluación" if is_evaluation else "Clase"
    href = str(relative_path).replace("\\", "/")
    if use_archive_prefix:
        href = f"archivo/{href}"
    return (
        f"<a class=\"class-link\" href=\"{href}\" data-progress-id=\"{course_key}/u{unit_number}/Clase_{class_data['unit_index']}\">"
        f"<span class=\"num\">{class_data['unit_index']}</span>"
        f"<span class=\"title\">Clase {class_data['unit_index']} — {title}</span>"
        f"<span class=\"tag {tag_class}\">{tag_text}</span>"
        f"<span class=\"status-badge status-pending\" data-status-badge>⏳ Pendiente</span>"
        f"</a>"
    )


def instrument_link_markup(entry, use_archive_prefix=False):
    href = entry["href"]
    if use_archive_prefix:
        href = f"archivo/{href}"
    return (
        f"<a class=\"class-link\" href=\"{href}\">"
        f"<span class=\"num\">{entry['icon']}</span>"
        f"<span class=\"title\">{entry['title']}</span>"
        f"<span class=\"tag tag-eval\">{entry['tag']}</span>"
        f"</a>"
    )


def update_progress(plan_cache):
    for progress_path in PROGRESS_TARGETS:
        data = json.loads(progress_path.read_text(encoding="utf-8")) if progress_path.exists() else {"classes": {}}
        data.setdefault("classes", {})
        data["lastUpdated"] = str(date.today())

        for course in COURSES:
            for unit_number, unit_info in plan_cache[course["course_key"]].items():
                for class_data in unit_info["classes"]:
                    if not should_generate_class(unit_number, class_data):
                        continue
                    eval_kind = evaluation_kind(unit_number, class_data, len(unit_info["classes"]))
                    oral_sequence = oral_project_sequence(course, unit_number, class_data)
                    key = f"{course['course_key']}/u{unit_number}/Clase_{class_data['unit_index']}"
                    data["classes"][key] = {
                        "status": "pending",
                        "title": f"Clase {class_data['unit_index']} — {short_title(class_data, unit_number, eval_kind, oral_sequence)}",
                    }

        progress_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def unit_group_title(unit_number, unit_title):
    return f"📁 Unidad {unit_number} — {unit_title}"


def instrument_group_markup():
    return (
        '<div class="unit-group">'
        '<div class="unit-title" onclick="toggleUnit(this)"><span>📋 Instrumentos de Evaluación</span><span class="arrow">▶</span></div>'
        '<div class="unit-classes"></div>'
        '</div>'
    )


def find_or_create_unit_group(section, unit_number, unit_title):
    groups = section.find_all("div", class_="unit-group", recursive=False)
    target = None
    for group in groups:
        title_el = group.select_one(".unit-title")
        title = clean_text(title_el.get_text(" ")) if title_el else ""
        if re.search(rf"Unidad\s+{unit_number}\b", title):
            target = group
            break

    if target:
        return target

    markup = (
        f"<div class=\"unit-group\">"
        f"<div class=\"unit-title\" onclick=\"toggleUnit(this)\"><span>{unit_group_title(unit_number, unit_title)}</span><span class=\"arrow\">▶</span></div>"
        f"<div class=\"unit-classes\"></div>"
        f"</div>"
    )
    new_group = BeautifulSoup(markup, "html.parser").div

    insert_before = None
    for group in groups:
        title_el = group.select_one(".unit-title")
        title = clean_text(title_el.get_text(" ")) if title_el else ""
        number_match = re.search(r"Unidad\s+(\d+)\b", title)
        if number_match and int(number_match.group(1)) > unit_number:
            insert_before = group
            break
        if title and "Instrumentos" in title:
            insert_before = group
            break

    if insert_before:
        insert_before.insert_before(new_group)
    else:
        section.append(new_group)
    return new_group


def find_instrument_group(section):
    for group in section.find_all("div", class_="unit-group", recursive=False):
        title_el = group.select_one(".unit-title")
        title = clean_text(title_el.get_text(" ")) if title_el else ""
        if title and "Instrumentos" in title:
            return group
    return None


def find_or_create_instrument_group(section):
    existing = find_instrument_group(section)
    if existing:
        return existing

    new_group = BeautifulSoup(instrument_group_markup(), "html.parser").div
    section.append(new_group)
    return new_group


def replace_unit_links(group, links):
    classes_box = group.select_one(".unit-classes")
    if not classes_box:
        classes_box = BeautifulSoup('<div class="unit-classes"></div>', "html.parser").div
        group.append(classes_box)
    classes_box.clear()
    for link in links:
        classes_box.append(BeautifulSoup(link, "html.parser"))


def preserved_u1_links(group):
    classes_box = group.select_one(".unit-classes")
    if not classes_box:
        return []

    preserved = []
    for anchor in classes_box.select("a.class-link"):
        progress_id = anchor.get("data-progress-id", "")
        if progress_id.endswith("/Clase_1") or progress_id.endswith("/Clase_2"):
            preserved.append(str(anchor))
    return preserved


def update_index(index_path, plan_cache):
    soup = BeautifulSoup(index_path.read_text(encoding="utf-8"), "html.parser")
    sections = {clean_text(section.select_one(".course-header h3").get_text(" ")): section for section in soup.select(".course-section") if section.select_one(".course-header h3")}
    use_archive_prefix = "tranquiprofe.cl" in index_path.parts

    for course in COURSES:
        section = sections.get(course["course_name"])
        if not section:
            continue

        for unit_number, unit_info in plan_cache[course["course_key"]].items():
            group = find_or_create_unit_group(section, unit_number, unit_info["unit_title"])
            title_span = group.select_one(".unit-title span")
            if title_span:
                title_span.string = unit_group_title(unit_number, unit_info["unit_title"])

            links = preserved_u1_links(group) if unit_number == 1 else []
            for class_data in unit_info["classes"]:
                if not should_generate_class(unit_number, class_data):
                    continue
                eval_kind = evaluation_kind(unit_number, class_data, len(unit_info["classes"]))
                links.append(
                    class_link_markup(
                        relative_output_path(course, unit_number, class_data),
                        course["course_key"],
                        unit_number,
                        class_data,
                        eval_kind,
                        use_archive_prefix=use_archive_prefix,
                    )
                )
            replace_unit_links(group, links)

        instrument_entries = instrument_entries_for_course(course)
        instrument_group = find_instrument_group(section)
        if instrument_entries:
            instrument_group = find_or_create_instrument_group(section)
            instrument_links = [
                instrument_link_markup(entry, use_archive_prefix=use_archive_prefix)
                for entry in instrument_entries
            ]
            replace_unit_links(instrument_group, instrument_links)
        elif instrument_group:
            instrument_group.decompose()

    index_path.write_text(str(soup), encoding="utf-8")


def load_plan_cache():
    cache = {}
    for course in COURSES:
        unit_map = {}
        for unit_number, plan_path in course["plans"].items():
            if plan_path.exists():
                unit_map[unit_number] = parse_plan_file(plan_path)
        cache[course["course_key"]] = unit_map
    return cache


def generate_materials(plan_cache):
    generated = 0
    for course in COURSES:
        previous_class = None
        for unit_number, unit_info in plan_cache[course["course_key"]].items():
            previous_class = None
            for class_data in unit_info["classes"]:
                if should_generate_class(unit_number, class_data):
                    html = build_class_html(course, unit_number, unit_info, class_data, previous_class)
                    write_targets(relative_output_path(course, unit_number, class_data), html)
                    generated += 1
                previous_class = class_data
    return generated


def main():
    plan_cache = load_plan_cache()
    total_generated = generate_materials(plan_cache)
    for index_path in INDEX_TARGETS:
        update_index(index_path, plan_cache)
    update_progress(plan_cache)
    print(f"Generated {total_generated} class pages for Units 1-4.")


if __name__ == "__main__":
    main()