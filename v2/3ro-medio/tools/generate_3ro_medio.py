# -*- coding: utf-8 -*-
"""
3ro Medio V2 generator.
Local-only generation: 5 specialties x 4 units x 12 classes = 240 HTML files.
Requirement: every main reading text has exactly 6 paragraphs.
"""
from pathlib import Path
import html
import sys

SCRIPT_DIR = Path(__file__).parent
LEVEL_DIR = SCRIPT_DIR.parent
V2_DIR = LEVEL_DIR.parent
sys.path.insert(0, str(V2_DIR / "1ro-medio" / "u1"))
from _generate_u1 import TEMPLATE  # noqa: E402

MATCH_LABELS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

SPECIALTIES = {
    "industrial": {
        "course": "3ro A",
        "name": "Mecanica Industrial",
        "display": "Mecánica Industrial",
        "field": "industrial mechanics",
        "student": "Diego",
        "workshop": "industrial workshop",
        "society": "factories, hospitals, mining operations, food plants, and public services depend on safe machines and precise metal parts",
        "colors": ("#166534", "#16a34a", "#22c55e"),
        "tools": [
            ("lathe", "torno", "/leɪð/"), ("milling machine", "fresadora", "/ˈmɪlɪŋ məˈʃiːn/"),
            ("caliper", "pie de metro", "/ˈkælɪpər/"), ("micrometer", "micrómetro", "/maɪˈkrɒmɪtər/"),
            ("wrench", "llave", "/rentʃ/"), ("drill press", "taladro de pedestal", "/drɪl pres/"),
            ("grinder", "esmeril", "/ˈɡraɪndər/"), ("vise", "prensa", "/vaɪs/"),
            ("bearing", "rodamiento", "/ˈbeərɪŋ/"), ("shaft", "eje", "/ʃæft/"),
            ("alignment", "alineación", "/əˈlaɪnmənt/"), ("tolerance", "tolerancia", "/ˈtɒlərəns/"),
        ],
        "processes": ["turning a metal shaft on a lathe", "checking measurements with a caliper", "preventive maintenance of rotating parts", "aligning a machine before operation", "reading a technical drawing", "inspecting bearings and shafts"],
        "systems": ["rotating mechanical systems", "transmission components", "industrial maintenance routines", "precision measurement routines"],
        "year_focus": "conceptos introductorios y rutinas laborales vinculadas a la especialidad",
    },
    "automotriz": {
        "course": "3ro B",
        "name": "Mecanica Automotriz",
        "display": "Mecánica Automotriz",
        "field": "automotive mechanics",
        "student": "Sofia",
        "workshop": "automotive workshop",
        "society": "transport, emergency services, families, agriculture, and local businesses depend on safe and reliable vehicles",
        "colors": ("#991b1b", "#dc2626", "#f97316"),
        "tools": [
            ("scanner", "escáner automotriz", "/ˈskænər/"), ("multimeter", "multímetro", "/ˈmʌltiˌmiːtər/"),
            ("torque wrench", "torquímetro", "/tɔːrk rentʃ/"), ("hydraulic jack", "gato hidráulico", "/haɪˈdrɔːlɪk dʒæk/"),
            ("spark plug", "bujía", "/spɑːrk plʌɡ/"), ("brake pad", "pastilla de freno", "/breɪk pæd/"),
            ("radiator", "radiador", "/ˈreɪdieɪtər/"), ("piston", "pistón", "/ˈpɪstən/"),
            ("crankshaft", "cigüeñal", "/ˈkræŋkʃæft/"), ("lubrication", "lubricación", "/ˌluːbrɪˈkeɪʃən/"),
            ("cooling system", "sistema de refrigeración", "/ˈkuːlɪŋ ˈsɪstəm/"), ("fault code", "código de falla", "/fɔːlt koʊd/"),
        ],
        "processes": ["diagnosing a fault with a scanner", "checking active and passive safety systems", "explaining the four-stroke engine cycle", "checking lubrication and cooling", "inspecting fixed and moving engine parts", "reading fault codes"],
        "systems": ["comfort and safety systems", "engine lubrication and cooling systems", "active and passive safety systems", "basic diagnostic systems"],
        "year_focus": "confort y seguridad del vehiculo, sistemas pasivos y activos, diagnostico basico, piezas del motor, ciclo de Carnot, lubricacion, refrigeracion y cuatro tiempos",
    },
    "electricidad": {
        "course": "3ro C",
        "name": "Electricidad",
        "display": "Electricidad",
        "field": "electricity",
        "student": "Mateo",
        "workshop": "electrical workshop",
        "society": "homes, schools, hospitals, industry, and renewable energy projects depend on safe electrical installations",
        "colors": ("#92400e", "#f59e0b", "#facc15"),
        "tools": [
            ("multimeter", "multímetro", "/ˈmʌltiˌmiːtər/"), ("voltage tester", "probador de voltaje", "/ˈvoʊltɪdʒ ˈtestər/"),
            ("circuit breaker", "disyuntor", "/ˈsɜːrkɪt ˌbreɪkər/"), ("wire stripper", "pelacables", "/ˈwaɪər ˈstrɪpər/"),
            ("conduit", "canalización", "/ˈkɒnduɪt/"), ("solar panel", "panel solar", "/ˈsoʊlər ˈpænəl/"),
            ("inverter", "inversor", "/ɪnˈvɜːrtər/"), ("grounding", "puesta a tierra", "/ˈɡraʊndɪŋ/"),
            ("green hydrogen", "hidrógeno verde", "/ɡriːn ˈhaɪdrədʒən/"), ("smart grid", "red inteligente", "/smɑːrt ɡrɪd/"),
            ("renewable energy", "energía renovable", "/rɪˈnjuːəbəl ˈenərdʒi/"), ("load", "carga eléctrica", "/loʊd/"),
        ],
        "processes": ["testing voltage before touching a circuit", "installing a basic lighting circuit", "connecting a solar panel to an inverter", "checking grounding protection", "explaining how green hydrogen can use renewable electricity", "reading a single-line diagram"],
        "systems": ["renewable energy systems", "electrical safety systems", "green hydrogen production chains", "smart electrical grids"],
        "year_focus": "energias renovables, transicion energetica e hidrogeno verde",
    },
    "grafica": {
        "course": "3ro D",
        "name": "Grafica",
        "display": "Gráfica",
        "field": "graphic production",
        "student": "Camila",
        "workshop": "graphic production lab",
        "society": "schools, companies, public campaigns, local businesses, and community projects depend on clear printed and digital communication",
        "colors": ("#6b21a8", "#a855f7", "#ec4899"),
        "tools": [
            ("Fiery Command WorkStation", "Fiery Command WorkStation", "/ˈfaɪəri kəˈmænd ˈwɜːrkˌsteɪʃən/"),
            ("print queue", "cola de impresión", "/prɪnt kjuː/"), ("RIP", "procesador de imagen raster", "/rɪp/"),
            ("color profile", "perfil de color", "/ˈkʌlər ˈproʊfaɪl/"), ("calibration", "calibración", "/ˌkælɪˈbreɪʃən/"),
            ("proof", "prueba de impresión", "/pruːf/"), ("layout", "diagramación", "/ˈleɪaʊt/"),
            ("bleed", "sangrado", "/bliːd/"), ("crop mark", "marca de corte", "/krɒp mɑːrk/"),
            ("substrate", "sustrato", "/ˈsʌbstreɪt/"), ("preflight", "preflight / revisión previa", "/ˈpriːflaɪt/"),
            ("imposition", "imposición", "/ˌɪmpəˈzɪʃən/"),
        ],
        "processes": ["preflighting a print file", "calibrating color before printing", "managing a print queue in Fiery", "checking bleed and crop marks", "producing a proof for client approval", "exporting a print-ready PDF"],
        "systems": ["digital print workflows", "Fiery Command WorkStation", "color management systems", "client approval workflows"],
        "year_focus": "software Fiery Command WorkStation y flujo de produccion grafica",
    },
    "electronica": {
        "course": "3ro E",
        "name": "Electronica",
        "display": "Electrónica",
        "field": "electronics",
        "student": "Valentina",
        "workshop": "electronics lab",
        "society": "smart homes, robots, medical devices, factories, transport systems, and communication networks depend on electronic systems",
        "colors": ("#1e40af", "#2563eb", "#06b6d4"),
        "tools": [
            ("breadboard", "protoboard", "/ˈbredbɔːrd/"), ("microcontroller", "microcontrolador", "/ˌmaɪkroʊkənˈtroʊlər/"),
            ("sensor", "sensor", "/ˈsensər/"), ("actuator", "actuador", "/ˈæktʃueɪtər/"),
            ("soldering iron", "cautín", "/ˈsɒldərɪŋ ˈaɪərn/"), ("oscilloscope", "osciloscopio", "/əˈsɪləskoʊp/"),
            ("resistor", "resistencia", "/rɪˈzɪstər/"), ("capacitor", "condensador", "/kəˈpæsɪtər/"),
            ("relay", "relé", "/ˈriːleɪ/"), ("automation", "automatización", "/ˌɔːtəˈmeɪʃən/"),
            ("robotics", "robótica", "/roʊˈbɒtɪks/"), ("mechatronics", "mecatrónica", "/ˌmekəˈtrɒnɪks/"),
        ],
        "processes": ["building a digital circuit on a breadboard", "reading sensor data with a microcontroller", "controlling an actuator", "checking signals with an oscilloscope", "explaining a smart home case study", "testing a relay circuit"],
        "systems": ["digital electronics", "home automation", "mechatronics and robotics systems", "sensor-actuator systems"],
        "year_focus": "electronica digital, domotica, automatizacion, mecatronica y robotica mediante estudios de caso",
    },
}

UNIT_PLANS = {
    1: {
        "title": "My Technical Skills",
        "product": "Video Presentation: My Technical Skills (24 pts)",
        "theme": "technical identity, tools, systems, and social importance",
        "classes": [
            ("My Technical Identity", "Present Simple + technical identity", "present the specialty and explain an initial technical identity"),
            ("Tools and Equipment I Can Use", "Can / know how to", "describe tools and equipment the student can use"),
            ("Safety and Professional Responsibility", "Have to / must / should", "explain safety rules and professional responsibility"),
            ("Reading Technical Instructions", "Imperatives + sequence connectors", "understand technical instructions and work steps"),
            ("Systems I Understand", "There is / there are + present simple", "describe systems or processes in the specialty"),
            ("Basic Diagnosis and Problem Solving", "Present Simple questions + because/so", "explain basic diagnosis and technical problem solving"),
            ("Why My Specialty Matters", "Because / so / therefore", "argue the social relevance of the specialty"),
            ("Technical Vocabulary for Subtitles", "Noun phrases + adjective order", "prepare precise technical vocabulary for English subtitles"),
            ("Script Structure: My Technical Skills", "Paragraph connectors", "organize the video script into introduction, body, and conclusion"),
            ("Pronunciation and Rehearsal", "Pronunciation focus + word stress", "rehearse technical pronunciation using IPA"),
            ("Recording and English Subtitles", "Accuracy and clarity revision", "record a draft and revise English subtitles"),
            ("Final Video: My Technical Skills", "Integrated oral performance", "submit the final video using the official rubric"),
        ],
    },
    2: {
        "title": "Technical Systems in Action",
        "product": "Technical reading test + process explanation",
        "theme": "systems, procedures, sequence, and technical reading",
        "classes": [
            ("How Technical Systems Work", "Present Simple + system functions", "identify inputs, processes, and outputs in a technical system"),
            ("Reading a Procedure", "Imperatives + sequence connectors", "follow a technical procedure in English"),
            ("Passive Voice in Manuals", "Passive Voice: is/are + past participle", "recognize passive structures in instructions"),
            ("Tools Are Checked First", "Passive Voice + safety sequence", "describe preparation and inspection steps"),
            ("A Process Is Completed Step by Step", "Passive Voice + first/then/finally", "explain a specialty process in order"),
            ("Technical Diagrams and Labels", "There is/are + prepositions", "interpret diagrams, labels, and component positions"),
            ("Cause and Effect in Systems", "because / so / therefore", "explain causes and effects in technical systems"),
            ("Reading Practice: Authentic Manual Extract", "Skimming + scanning", "answer comprehension questions from a manual-style text"),
            ("Comparing Two Procedures", "Comparatives", "compare two technical procedures or tools"),
            ("Preparing a Process Explanation", "Passive Voice review", "prepare an oral explanation of a process"),
            ("Reading Test Practice", "Integrated reading skills", "practice explicit, implicit, analysis, and critical questions"),
            ("Technical Reading Test", "Integrated unit assessment", "complete a reading test connected to the specialty"),
        ],
    },
    3: {
        "title": "Troubleshooting and Case Studies",
        "product": "Case study report + short oral explanation",
        "theme": "faults, evidence, diagnosis, and case studies",
        "classes": [
            ("What Is a Technical Fault?", "Present Simple + technical symptoms", "identify symptoms and faults in a system"),
            ("Evidence Before Action", "Should / must + evidence", "justify evidence-based decisions"),
            ("Past Simple in Case Reports", "Past Simple regular and irregular", "describe what happened in a technical incident"),
            ("Past Continuous in the Workshop", "Past Continuous", "describe actions in progress during an incident"),
            ("When the Problem Appeared", "Past Simple + Past Continuous", "connect events and background actions"),
            ("If the System Fails…", "First Conditional", "predict consequences of technical failures"),
            ("Basic Troubleshooting Flow", "Sequence + conditionals", "explain a troubleshooting sequence"),
            ("Case Study: Human Error", "Cause/effect connectors", "analyze the role of human error"),
            ("Case Study: Maintenance Decision", "Should / shouldn't", "recommend a maintenance action"),
            ("Writing a Case Study Report", "Report structure", "write a short technical report"),
            ("Oral Explanation of a Case", "Past + cause/effect review", "prepare a short oral explanation"),
            ("Case Study Presentation", "Integrated performance", "present a case study and answer questions"),
        ],
    },
    4: {
        "title": "Workplace Communication and Future Projects",
        "product": "Team project pitch + workplace communication portfolio",
        "theme": "workplace communication, future plans, projects, and employability",
        "classes": [
            ("Professional Communication", "Polite requests + workplace language", "communicate respectfully in technical contexts"),
            ("Emails and Work Orders", "Formal email phrases", "write short workplace messages"),
            ("Reporting Progress", "Present Perfect intro + already/yet", "report progress on a technical task"),
            ("Future Improvements", "Will / be going to", "describe future improvements in the specialty"),
            ("If We Improve the System…", "First Conditional", "predict project outcomes"),
            ("Team Roles in a Project", "Role language + responsibilities", "describe team roles and responsibilities"),
            ("Budget, Materials, and Time", "Quantifiers + numbers", "explain basic project resources"),
            ("Risk Communication", "Must / should / may", "communicate technical risks"),
            ("Preparing a Project Pitch", "Persuasive connectors", "organize a short project pitch"),
            ("Visual Support and Subtitles", "Presentation language", "prepare slides, captions, or subtitles"),
            ("Rehearsal and Peer Feedback", "Feedback language", "rehearse and improve the project pitch"),
            ("Final Project Pitch", "Integrated workplace performance", "present a team project pitch in English"),
        ],
    },
}

COMMON_TERMS = [
    ("procedure", "procedimiento", "/prəˈsiːdʒər/"), ("safety", "seguridad", "/ˈseɪfti/"),
    ("system", "sistema", "/ˈsɪstəm/"), ("evidence", "evidencia", "/ˈevɪdəns/"),
    ("fault", "falla", "/fɔːlt/"), ("maintenance", "mantención", "/ˈmeɪntənəns/"),
    ("diagram", "diagrama", "/ˈdaɪəɡræm/"), ("report", "informe", "/rɪˈpɔːrt/"),
    ("subtitle", "subtítulo", "/ˈsʌbˌtaɪtəl/"), ("rubric", "rúbrica", "/ˈruːbrɪk/"),
    ("criterion", "criterio", "/kraɪˈtɪəriən/"), ("workflow", "flujo de trabajo", "/ˈwɜːrkfloʊ/"),
    ("teamwork", "trabajo en equipo", "/ˈtiːmwɜːrk/"), ("accuracy", "precisión", "/ˈækjərəsi/"),
]

DEFINITIONS = {
    "procedure": "A series of ordered steps for completing a task.",
    "safety": "Conditions and actions that protect people from harm.",
    "system": "A group of connected parts that work together.",
    "evidence": "Information that supports a conclusion or diagnosis.",
    "fault": "A defect or problem in a component or system.",
    "maintenance": "Actions done to keep equipment working correctly.",
    "diagram": "A simplified drawing that explains parts or connections.",
    "report": "A written or oral explanation of what happened or was done.",
    "subtitle": "Written text on a video that shows spoken words.",
    "rubric": "Document with criteria used to evaluate performance.",
    "criterion": "One standard used to evaluate a task.",
    "workflow": "Organized sequence of work steps.",
    "teamwork": "Cooperation between people to achieve a common goal.",
    "accuracy": "Quality of being correct and precise.",
}

FILL_PATTERNS = {
    1: [("I ___ a student in this specialty.", "am"), ("My specialty ___ useful for society.", "is"), ("Technicians ___ technical vocabulary.", "use"), ("We ___ three tools in the video.", "describe"), ("A good technician ___ safety rules.", "follows"), ("I ___ explain two processes.", "can"), ("The final video ___ subtitles.", "needs"), ("My classmates ___ pronunciation.", "practice"), ("The rubric ___ 24 points.", "has"), ("This unit ___ technical identity.", "builds")],
    2: [("First, the tools ___ checked.", "are"), ("Then, the procedure ___ followed.", "is"), ("The system ___ tested safely.", "is"), ("Components ___ identified in the diagram.", "are"), ("The result ___ recorded in a report.", "is"), ("Students ___ scan for details.", "can"), ("The manual ___ clear warnings.", "includes"), ("Two procedures ___ compared.", "are"), ("A process ___ explained step by step.", "is"), ("Technical reading ___ practice.", "requires")],
    3: [("The fault ___ identified from evidence.", "is"), ("The technician ___ ask questions first.", "should"), ("Yesterday, the system ___ unexpectedly.", "failed"), ("Students ___ writing a report when the teacher arrived.", "were"), ("If the system fails, the team ___ stop the process.", "will"), ("The cause ___ be checked carefully.", "must"), ("Human error ___ accidents.", "can cause"), ("The evidence ___ collected before action.", "is"), ("A recommendation ___ included in the report.", "is"), ("The case study ___ presented orally.", "is")],
    4: [("Could you ___ the work order, please?", "check"), ("I ___ already finished the first step.", "have"), ("We are ___ to improve the system.", "going"), ("If we improve safety, the risk ___ decrease.", "will"), ("Each team member ___ a role.", "has"), ("The project ___ materials and time.", "needs"), ("We ___ communicate risks clearly.", "must"), ("The pitch ___ explain the problem and solution.", "should"), ("Subtitles ___ support the presentation.", "can"), ("Feedback ___ the final pitch.", "improves")],
}

READING_LABELS = ["Explicit", "Explicit", "Explicit", "Implicit (inference)", "Analysis", "Critical thinking"]


def escape_html(value):
    return html.escape(str(value), quote=False)


def unit_dir_for(specialty_slug, unit_number):
    return LEVEL_DIR / specialty_slug / f"u{unit_number}"


def class_file_name(unit_number, class_number, specialty_slug):
    return f"Clase_{class_number:02d}_U{unit_number}_3ro_{specialty_slug}.html"


def select_vocab(specialty, unit_number, class_number):
    source_terms = COMMON_TERMS[(class_number - 1) % len(COMMON_TERMS):] + COMMON_TERMS[: (class_number - 1) % len(COMMON_TERMS)]
    combined_terms = list(specialty["tools"][:6]) + source_terms + list(specialty["tools"][6:])
    selected_terms = []
    seen_terms = set()
    for term in combined_terms:
        term_key = term[0].lower()
        if term_key in seen_terms:
            continue
        selected_terms.append(term)
        seen_terms.add(term_key)
        if len(selected_terms) == 10:
            break
    return selected_terms


def make_u3_text(specialty, class_number, class_title, grammar_focus):
    process_a = specialty["processes"][(class_number - 1) % len(specialty["processes"])]
    process_b = specialty["processes"][class_number % len(specialty["processes"])]
    system_a = specialty["systems"][(class_number - 1) % len(specialty["systems"])]
    tools = specialty["tools"]
    tool_a = tools[(class_number - 1) % len(tools)][0]
    tool_b = tools[class_number % len(tools)][0]
    tool_c = tools[(class_number + 1) % len(tools)][0]
    display = specialty["display"]

    if class_number == 1:
        return [
            f"At the {specialty['workshop']}, a new trainee notices that a {tool_a} is giving unusual results during a routine task in {display}. The supervisor explains that a technical fault is not only a dramatic breakdown. A fault can be a strange noise, an unstable reading, a delayed reaction, or a result that does not match the expected quality standard.",
            f"Before touching the equipment, the team compares normal operation with the current symptoms. In this case, the process of {process_a} should feel stable and predictable, but today the response is slow and inconsistent. That small difference is enough to begin a fault report.",
            f"The trainee writes down three visible clues: a warning light, an unusual vibration, and a repeated delay in the system response. The supervisor says that good technicians do not guess first. They observe, compare, and describe the problem in clear language.",
            f"The workshop discussion also mentions {system_a}. A system may fail because of wear, poor adjustment, contamination, or a human mistake during setup. Students learn that the first question is not 'How do I fix it?' but 'What exactly is failing and what evidence do I have?'",
            f"During the break, the trainee checks the vocabulary board and reviews words such as {tool_b} and {tool_c}. Those terms are useful because the report must describe the symptom, the affected part, and the probable impact on safety or quality. Grammar matters too: simple present helps describe what normally happens and what happens now.",
            f"At the end of the shift, the supervisor closes the notebook and says that technical English begins with precise observation. If the description of the fault is weak, the diagnosis will also be weak. For that reason, identifying symptoms clearly is the first professional habit in troubleshooting.",
        ]
    if class_number == 2:
        return [
            f"A notice on the wall of the {specialty['workshop']} says: 'Evidence before action.' One morning, a student wants to restart a task immediately after a problem appears during {process_a}, but the instructor stops the group and asks for proof first.",
            f"The class gathers around the workstation and collects evidence step by step. They check readings, inspect parts, compare the current result with the previous one, and ask who last adjusted the equipment. No repair begins until the information is written in a simple checklist.",
            f"One student points at {tool_a}, another checks {tool_b}, and a third student records the order of events. The instructor explains that professional decisions should be based on observable facts, not on panic, memory, or personal preference.",
            f"The team also reviews {system_a}. In a technical environment, one incorrect action can hide the real cause of the fault. If someone changes a setting too early, the original evidence disappears and the diagnosis becomes less reliable.",
            f"Because of that, the group practices short recommendations in English: students should photograph the problem, must label the evidence, and should not replace components without a reason. The grammar of advice becomes part of the technical method.",
            f"By the end of the lesson, the trainees understand a simple rule: evidence protects both the machine and the technician. A careful record saves time, supports communication, and helps the next person continue the work with confidence.",
        ]
    if class_number == 3:
        return [
            f"The following report was found in the folder of the {specialty['workshop']}: 'Yesterday, the team started {process_a} at 9:10. The equipment responded normally at first, but a minor fault appeared after the second verification.' The document is short, direct, and written in past tense because it records finished actions.",
            f"The report continues with a timeline. A student checked {tool_a}, another student cleaned the area, and the instructor confirmed that the setup had followed the standard sequence. After that, the group noticed that one part was not aligned correctly.",
            f"Instead of writing opinions, the author used concrete verbs: inspected, measured, compared, stopped, and reported. Those verbs help the reader understand what happened, in what order, and why the final decision was necessary.",
            f"In the second paragraph, the writer mentions {system_a} and explains how the fault affected the full process. Even a small incident can become serious if the report ignores time, sequence, and evidence.",
            f"Students underline key verbs and rewrite weak sentences. For example, 'there was a problem' becomes 'the technician measured an unstable value during {process_b}.' Better verbs create better reports.",
            f"When the class finishes, everyone agrees that a case report is not just school writing. In a real workplace, a past-tense report becomes a record for maintenance, training, and safety decisions.",
        ]
    if class_number == 4:
        return [
            f"At 10:30, the {specialty['workshop']} was busy. One group was finishing {process_a}, another was preparing tools, and the instructor was checking a previous task. While those actions were in progress, a fault appeared and interrupted the normal rhythm of the room.",
            f"Because several things were happening at the same time, the students had to reconstruct the scene carefully. One trainee was holding {tool_a}, another was reading a value on {tool_b}, and a classmate was moving materials away from the work area.",
            f"The incident was not dramatic, but it was confusing. The first report only said that the problem started 'during the activity.' That was not enough, so the group added more precise background information about what each person was doing at that moment.",
            f"The class then linked the situation to {system_a}. Complex systems rarely fail in isolation; often a small mistake, a distraction, or a badly timed action changes the result of the whole sequence.",
            f"Students practice English forms such as 'was checking,' 'were preparing,' and 'was recording' because those structures help describe the background of an incident. Without that grammar, the report sounds incomplete and unclear.",
            f"The final version shows that time and context matter. A good technician does not only say what happened; the technician also explains what was happening around the fault when the problem began.",
        ]
    if class_number == 5:
        return [
            f"A maintenance log from the {specialty['workshop']} describes a problem that appeared halfway through {process_a}. At first, everything seemed normal. Then a strange symptom appeared while the operator was continuing the task, and the team had to connect the exact moment of the fault with the actions that came before it.",
            f"The log says that the operator had already checked {tool_a} and had confirmed the first measurements. While the second stage was running, a new reading appeared on {tool_b}, and the group stopped the activity to avoid extra damage.",
            f"Students read the timeline and mark two kinds of information: the short actions that moved the story forward and the longer background actions that were still in progress. That contrast helps them understand why the problem appeared when it did.",
            f"The instructor then introduces {system_a} as the broader context. A system can look normal for several minutes and still hide a weak point. The visible problem often begins only after earlier conditions combine in the wrong way.",
            f"As they rewrite the case, students use past simple for the key events and past continuous for the background. The grammar supports the logic of the diagnosis: first the setup happened, then the process was continuing, and finally the fault became visible.",
            f"In the last discussion, the class concludes that timing is part of evidence. Knowing when a problem appeared can reveal whether the cause came from setup, operation, wear, or communication failure.",
        ]
    if class_number == 6:
        return [
            f"A laminated poster in the {specialty['workshop']} presents a warning scenario: if the system fails during {process_a}, the team must react in an ordered way. The document does not try to scare students; it helps them predict consequences before a real fault happens.",
            f"The first part of the poster explains that a small error can grow quickly. If a reading on {tool_a} is ignored, the next stage may produce false data. If a student continues without checking {tool_b}, the fault may affect more than one component.",
            f"The second part lists likely consequences: wasted material, unsafe operation, incorrect diagnosis, and poor communication between team members. Each consequence is connected to a preventive action written in simple English.",
            f"The instructor adds an example from {system_a}. In that system, one wrong decision can change the full sequence of work. Prediction is useful because it trains students to think one step ahead instead of reacting too late.",
            f"During pair work, students complete sentences such as 'If the system fails, we will...' and 'If we ignore the evidence, the result will...'. The conditional form becomes part of technical reasoning, not just a grammar exercise.",
            f"By the end of the lesson, the class understands that prevention begins in language. When technicians can describe possible consequences clearly, they are better prepared to protect equipment, people, and time.",
        ]
    if class_number == 7:
        return [
            f"A whiteboard in the {specialty['workshop']} shows a basic troubleshooting flow for a recurring problem. The first box says 'Observe,' the second says 'Collect evidence,' the third says 'Test one cause at a time,' and the last says 'Confirm the result.' The sequence looks simple, but it keeps the diagnosis organized.",
            f"Students follow the flow using a sample situation related to {process_a}. First, they identify the symptom. Next, they inspect {tool_a} and compare it with {tool_b}. After that, they test only one possible cause before moving to the next idea.",
            f"The instructor warns that many beginners jump directly to replacement. They change a part, restart the system, and hope for the best. That is not troubleshooting; it is guessing. A flow works because it reduces confusion.",
            f"The sample case also uses {system_a} to show how one small clue may lead to a larger explanation. A change in one area of the system can be the effect of a different cause somewhere else.",
            f"Students then explain the flow aloud with sequence expressions and conditional language. They say what happens first, what should happen next, and what to do if the first hypothesis fails. Speaking the sequence helps them internalize the logic.",
            f"The lesson closes with a practical reminder: troubleshooting is a path, not a magic moment. When the path is clear, the report, the explanation, and the final decision become stronger.",
        ]
    if class_number == 8:
        return [
            f"A case study from the {specialty['workshop']} describes a fault that was caused by human error, not by a broken machine. During {process_a}, one technician skipped a confirmation step because the team was in a hurry to finish before lunch.",
            f"At first, the result looked acceptable. However, a second check with {tool_a} and {tool_b} showed that one value did not match the expected standard. The machine was working, but the procedure had not been followed correctly.",
            f"The report does not blame one person aggressively. Instead, it asks what conditions made the error possible: time pressure, weak communication, incomplete supervision, and a false sense of confidence.",
            f"The class links the case to {system_a}. Human error often happens inside a larger environment. Poor routines, missing labels, or unclear instructions create opportunities for mistakes long before the final fault appears.",
            f"Students use cause-and-effect connectors to explain the chain of events. They practice sentences such as 'because the check was skipped' and 'therefore the final result was inaccurate.' The language helps them think responsibly about process failures.",
            f"In the final reflection, the group agrees that technical English should name the problem clearly without hiding the lesson. A professional case study transforms a mistake into a safer routine for the next team.",
        ]
    if class_number == 9:
        return [
            f"A maintenance supervisor places two options on the table after a minor fault appears during {process_a}. Option A is to continue working and review the result later. Option B is to stop, inspect the evidence carefully, and perform preventive maintenance before restarting.",
            f"The team studies measurements from {tool_a}, notes from the previous shift, and a quick visual check of {tool_b}. None of the signs show total failure, but several clues suggest that the equipment is moving away from normal conditions.",
            f"Students debate which decision is more responsible. One group thinks production should continue because the workshop is under pressure. Another group argues that early maintenance is cheaper and safer than a larger repair later.",
            f"The discussion becomes more meaningful when the instructor connects it with {system_a}. In technical work, a good decision is not only fast; it is justified by evidence, safety, and long-term reliability.",
            f"As they write recommendations, students use expressions such as should, should not, and it would be better to. The language of recommendation allows them to support a maintenance decision with reasons instead of intuition.",
            f"The text ends with the supervisor's final note: preventive action may look slow in the moment, but it often protects time, quality, and trust. A good technician knows when stopping is the smartest move.",
        ]
    if class_number == 10:
        return [
            f"The class reads a short model report about a fault detected during {process_a}. The report begins with a clear title, identifies the equipment or system involved, and states the observable symptom in the first lines.",
            f"In the second section, the writer summarizes the evidence: readings from {tool_a}, inspection notes from {tool_b}, and comments from the technician who first noticed the problem. Each piece of information is brief, concrete, and connected to the diagnosis.",
            f"The next paragraph explains the probable cause and the action that followed. Instead of dramatic language, the report uses calm and precise statements. That tone makes the document useful for another technician who may read it later.",
            f"Students also review how {system_a} is mentioned in a professional report. The text does not try to explain everything about the system. It includes only the details needed to understand the case and the recommendation.",
            f"When students write their own version, they separate symptom, evidence, cause, action, and final result. The structure helps them transform a confusing event into a document that can be reviewed, shared, and improved.",
            f"By the last paragraph, the class sees that a case study report is more than homework. In technical environments, good writing keeps knowledge inside the team and prevents the same problem from being repeated.",
        ]
    if class_number == 11:
        return [
            f"Before speaking in front of the group, a trainee reviews a real case from the {specialty['workshop']}. The case began during {process_a}, continued through a short diagnosis, and ended with a clear recommendation based on evidence.",
            f"The trainee organizes the explanation into four parts: the symptom, the evidence, the probable cause, and the lesson learned. To support the explanation, the student highlights key terms such as {tool_a}, {tool_b}, and {tool_c}.",
            f"The goal is not to memorize a perfect speech. The goal is to explain the case clearly enough that a classmate can understand what happened and why one decision was better than another.",
            f"The instructor reminds the group that {system_a} should appear only when it helps clarify the case. A short explanation with a clear structure is stronger than a long explanation full of disconnected details.",
            f"Students rehearse with past forms and cause-and-effect connectors. They also practice short transitions such as first, then, because of this, and finally. Those expressions guide the listener through the logic of the case.",
            f"At the end of the rehearsal, the trainee sounds more confident. Technical English becomes useful when it supports a clear explanation, not when it overwhelms the audience with isolated vocabulary.",
        ]
    return [
        f"Presentation day arrives at the {specialty['workshop']}, and each student brings a short case study connected to {display}. One group presents a problem related to {process_a}, while another focuses on {process_b}. Every presentation includes evidence, diagnosis, and a practical recommendation.",
        f"The audience listens for concrete information. A strong presentation identifies the symptom quickly, names the relevant tools or parts, and explains the sequence that led to the fault. Weak presentations usually skip evidence and jump straight to conclusions.",
        f"One presenter uses {tool_a} and {tool_b} as examples to explain how the diagnosis was confirmed. Another student shows how a missing check created confusion before the team found the real cause. The variety of cases helps the class compare methods.",
        f"During the feedback round, the instructor asks how each case connects with {system_a}. That question forces students to move beyond the isolated incident and think about the wider technical context.",
        f"The class also evaluates communication. Students notice that the best speakers use simple transitions, clear past forms, and short sentences with cause-and-effect connectors. Their English sounds purposeful because it is tied to evidence.",
        f"By the final applause, the room understands the main lesson of the unit: a technical case is useful only when it is different from other cases in details, but solid in structure. Good troubleshooting depends on observation, reasoning, and communication together.",
    ]


def make_text(specialty, unit_number, class_number, class_title, grammar_focus):
    if unit_number == 3:
        return make_u3_text(specialty, class_number, class_title, grammar_focus)

    unit = UNIT_PLANS[unit_number]
    process_a = specialty["processes"][(class_number - 1) % len(specialty["processes"])]
    process_b = specialty["processes"][class_number % len(specialty["processes"])]
    system_a = specialty["systems"][(unit_number + class_number - 2) % len(specialty["systems"])]
    tools = ", ".join(term[0] for term in specialty["tools"][:4])
    student = specialty["student"]
    display = specialty["display"]
    return [
        f"{student} is a 3rd year student in {display}. The lesson '{class_title}' belongs to Unit {unit_number}, '{unit['title']}', a unit focused on {unit['theme']}. The reading is written as an adapted technical workplace text, similar to the kind of explanation students may find in a manual, training note, or workshop guide.",
        f"In the {specialty['workshop']}, English is used to identify tools, follow procedures, read labels, and explain decisions. This is especially important for {specialty['field']} because many manuals, digital interfaces, catalogues, and safety warnings use international English terms. The language objective today is connected to {grammar_focus}.",
        f"The technical vocabulary for this class includes tools and concepts such as {tools}. These terms are not decorative words for a list; they are words that help students describe real work. When a student says the word accurately, writes it correctly, and understands its purpose, the student is closer to professional communication.",
        f"The first process connected to this lesson is {process_a}. The second process is {process_b}. Students are not expected to master every advanced detail yet, but they should understand the purpose of the process, identify the main steps, and explain at least one risk or quality requirement in simple English.",
        f"This lesson also connects with {system_a}. A system has parts, inputs, outputs, rules, and possible failures. If students learn to describe those elements in English, they can answer reading questions, prepare subtitles, write short reports, and speak about their technical skills with more confidence.",
        f"The final purpose is not only to pass an English activity. By the end of the lesson, students should collect ideas for an oral or written product connected to the unit. In social terms, {specialty['society']}. For that reason, technical English supports employability, safety, service, and civic responsibility."
    ]


def reading_questions(specialty, unit_number, class_title):
    unit = UNIT_PLANS[unit_number]
    return [
        f"What specialty is the text about?",
        f"What is the title of today's lesson?",
        f"Name two technical tools, systems, or processes mentioned in the text.",
        f"Why is English useful in this specialty according to the text?",
        f"How does the text connect technical vocabulary with professional communication?",
        f"Do you think technical English should be evaluated in TP specialties? Justify your answer with one reason from the text.",
    ]


def matching_rows(vocab_terms):
    result = []
    for english_term, spanish_term, ipa_text in vocab_terms:
        definition = DEFINITIONS.get(english_term, f"A technical term in the specialty related to {spanish_term}.")
        result.append((english_term, definition))
    return result[:10]


def shuffled_matching_rows(vocab_terms, class_number):
    rows = matching_rows(vocab_terms)
    definitions = [definition for term, definition in rows]
    if len(definitions) > 1:
        shift = (class_number % (len(definitions) - 1)) + 1
        definitions = definitions[shift:] + definitions[:shift]
    return [
        (term, f"{MATCH_LABELS[index]}. {definition}")
        for index, ((term, _), definition) in enumerate(zip(rows, definitions))
    ]


def oral_assessment_section(unit_number, specialty):
    rubric_link = "../../rubricas/my-technical-skills.html"
    if unit_number == 1:
        task_text = "Video Presentation: My Technical Skills. Include 3 tools/equipment, 2 systems/processes, social importance, and English subtitles."
    elif unit_number == 2:
        task_text = "Short process explanation. Use sequence language, passive voice, and at least 5 technical terms from the specialty."
    elif unit_number == 3:
        task_text = "Case study explanation. Describe the fault, evidence, cause, recommendation, and safety lesson."
    else:
        task_text = "Team project pitch. Present a workplace problem, proposed solution, materials, risks, and expected impact."
    return f"""
  <section class=\"card\">
    <h2>🎤 Oral Production Assessment</h2>
    <p><strong>Linked instrument:</strong> <a href=\"{rubric_link}\">Video Presentation: My Technical Skills — 3ro Medio rubric</a></p>
    <p style=\"margin-top:8px;\"><strong>Unit task:</strong> {escape_html(task_text)}</p>
    <p style=\"margin-top:8px; color:#475569;\">Rubric criteria used as reference: Content, Technical Vocabulary, Pronunciation, Fluency, Structure, and Subtitles.</p>
  </section>
"""


def build_class_html(specialty_slug, specialty, unit_number, class_number, class_title, grammar_focus, objective):
    vocab_terms = select_vocab(specialty, unit_number, class_number)
    text_paragraphs = make_text(specialty, unit_number, class_number, class_title, grammar_focus)
    text_html = "\n      ".join(f"<p>{escape_html(paragraph)}</p>" for paragraph in text_paragraphs)
    vocab_rows = "\n      ".join(
        f"<tr><td>{term_index + 1}</td><td><strong>{escape_html(english_term)}</strong></td><td class='ipa'>{escape_html(ipa_text)}</td><td>{escape_html(spanish_term)}</td></tr>"
        for term_index, (english_term, spanish_term, ipa_text) in enumerate(vocab_terms)
    )
    fill_items = "\n      ".join(
        f"<li>{escape_html(sentence).replace('___', '<span class=\"gap\">&nbsp;___&nbsp;</span>')}</li>"
        for sentence, answer in FILL_PATTERNS[unit_number]
    )
    fill_answers = "".join(f"<li>{escape_html(answer)}</li>" for sentence, answer in FILL_PATTERNS[unit_number])
    match_source = shuffled_matching_rows(vocab_terms, class_number) if unit_number == 3 else matching_rows(vocab_terms)
    match_rows = "\n      ".join(
        f"<tr><td>{row_index + 1}</td><td><strong>{escape_html(term)}</strong></td><td>{escape_html(definition)}</td></tr>"
        for row_index, (term, definition) in enumerate(match_source)
    )
    questions = reading_questions(specialty, unit_number, class_title)
    reading_blocks = []
    css_classes = ["explicit", "explicit", "explicit", "implicit", "analysis", "critical"]
    for question_index, question_text in enumerate(questions):
        reading_blocks.append(f'<div class="reading-q {css_classes[question_index]}"><div class="qtype">{READING_LABELS[question_index]}</div>{escape_html(question_text)}</div>')
    class_plan = UNIT_PLANS[unit_number]["classes"]
    previous_number = class_number - 1 if class_number > 1 else None
    next_number = class_number + 1 if class_number < len(class_plan) else None
    color_one, color_two, color_three = specialty["colors"]
    html_output = TEMPLATE.format(
        num=class_number,
        title=escape_html(class_title),
        subtitle=escape_html(f"{specialty['course']} · {specialty['display']} · Unit {unit_number}"),
        duration="90 min",
        grammar=escape_html(grammar_focus),
        oa=escape_html("OA9/OA10/OA13/OA14 — Comprender textos tecnicos adaptados, usar vocabulario de especialidad y producir respuestas orales/escritas en ingles tecnico."),
        objective=escape_html(f"Apply technical English to {objective} in {specialty['display']}.") ,
        text_title=escape_html(f"{class_title} in {specialty['display']}"),
        text_html=text_html,
        vocab_rows=vocab_rows,
        fill_items=fill_items,
        fill_answers=fill_answers,
        match_rows=match_rows,
        reading_html="\n    ".join(reading_blocks),
        closure=escape_html("Exit ticket: write 3 lines that can be reused in your oral/written product for this unit."),
        prev_link=class_file_name(unit_number, previous_number, specialty_slug) if previous_number else "#",
        next_link=class_file_name(unit_number, next_number, specialty_slug) if next_number else "#",
        prev_class="" if previous_number else "disabled",
        next_class="" if next_number else "disabled",
    )
    html_output = html_output.replace("linear-gradient(135deg,#1e3a8a,#3730a3,#6366f1)", f"linear-gradient(135deg,{color_one},{color_two},{color_three})")
    html_output = html_output.replace("#3730a3", color_one).replace("#6366f1", color_two).replace("#e0e7ff", "#e5e7eb")
    html_output = html_output.replace(f"Unidad 1 · Clase {class_number}/12", f"Unidad {unit_number} · Clase {class_number}/12 · 3ro Medio")
    html_output = html_output.replace(f"Clase {class_number} — U1 — 1ro Medio", f"Clase {class_number} — U{unit_number} — 3ro Medio")
    html_output = html_output.replace("<strong>Nivel:</strong> 1ro Medio", "<strong>Nivel:</strong> 3ro Medio")
    html_output = html_output.replace("1ro Medio · Unidad 1 — Discovering My Future Career", f"3ro Medio · Unidad {unit_number} — {UNIT_PLANS[unit_number]['title']} · {specialty['display']}")
    html_output = html_output.replace('href="../index.html">📚 Índice U1', f'href="index.html">📚 Índice U{unit_number}')
    html_output = html_output.replace("<h2>📖 Reading Text —", "<h2>📖 Reading Text (6 paragraphs) —")
    html_output = html_output.replace("\n\n  <section class=\"card\">\n    <h2>🚪 Cierre / Exit Ticket</h2>", oral_assessment_section(unit_number, specialty) + "\n  <section class=\"card\">\n    <h2>🚪 Cierre / Exit Ticket</h2>")
    return html_output


def build_unit_index(specialty_slug, specialty, unit_number):
    unit = UNIT_PLANS[unit_number]
    color_one, color_two, color_three = specialty["colors"]
    rows = []
    for class_index, (class_title, grammar_focus, objective) in enumerate(unit["classes"], start=1):
        file_name = class_file_name(unit_number, class_index, specialty_slug)
        rows.append(f"<tr><td>{class_index}</td><td><a href=\"{file_name}\"><strong>{escape_html(class_title)}</strong></a></td><td>{escape_html(grammar_focus)}</td></tr>")
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>3ro Medio U{unit_number} — {escape_html(specialty['display'])}</title>
<style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Inter,sans-serif;background:#f8fafc;color:#0f172a;line-height:1.6}}.hero{{background:linear-gradient(135deg,{color_one},{color_two},{color_three});color:white;padding:44px 20px;text-align:center}}.hero h1{{font-size:2rem;font-weight:800}}.hero p{{margin-top:8px;opacity:.92}}main{{max-width:1000px;margin:28px auto;padding:0 16px}}table{{width:100%;border-collapse:collapse;background:white;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(15,23,42,.08)}}th{{background:{color_one};color:white;text-align:left;padding:12px}}td{{padding:12px;border-bottom:1px solid #e2e8f0}}tr:nth-child(even) td{{background:#f8fafc}}a{{color:{color_one};text-decoration:none}}a:hover{{text-decoration:underline}}.note{{background:white;border-left:5px solid {color_two};border-radius:10px;padding:14px 16px;margin-bottom:18px}}</style></head><body><div class="hero"><h1>3ro Medio U{unit_number} — {escape_html(unit['title'])}</h1><p>{escape_html(specialty['course'])} · {escape_html(specialty['display'])} · 12 clases · textos de 6 párrafos</p></div><main><div class="note"><strong>Producto:</strong> {escape_html(unit['product'])}. <a href="../../rubricas/my-technical-skills.html">Rúbrica base My Technical Skills</a>.</div><table><tr><th>#</th><th>Clase</th><th>Foco lingüístico</th></tr>{''.join(rows)}</table></main></body></html>"""


def build_specialty_index(specialty_slug, specialty):
    color_one, color_two, color_three = specialty["colors"]
    cards = []
    for unit_number, unit in UNIT_PLANS.items():
        cards.append(f"<a class='card' href='u{unit_number}/index.html'><strong>U{unit_number} · {escape_html(unit['title'])}</strong><span>{escape_html(unit['product'])}</span></a>")
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{escape_html(specialty['display'])} — 3ro Medio</title><style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Inter,sans-serif;background:#f1f5f9;color:#0f172a}}.hero{{background:linear-gradient(135deg,{color_one},{color_two},{color_three});color:white;padding:48px 20px;text-align:center}}.hero h1{{font-size:2.1rem;font-weight:800}}.hero p{{margin-top:8px;opacity:.9}}main{{max-width:1000px;margin:28px auto;padding:0 16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}.card{{background:white;border-radius:12px;border-top:6px solid {color_two};padding:18px;box-shadow:0 4px 14px rgba(15,23,42,.08);text-decoration:none;color:#0f172a;display:flex;flex-direction:column;gap:8px}}.card span{{color:#64748b;font-size:.9rem}}</style></head><body><div class="hero"><h1>{escape_html(specialty['course'])} · {escape_html(specialty['display'])}</h1><p>3ro Medio · 4 unidades · 48 clases · textos de 6 párrafos</p></div><main>{''.join(cards)}</main></body></html>"""


def build_level_index():
    cards = []
    for specialty_slug, specialty in SPECIALTIES.items():
        color_one, color_two, color_three = specialty["colors"]
        cards.append(f"<a class='card' style='border-top-color:{color_two}' href='{specialty_slug}/index.html'><strong>{escape_html(specialty['course'])} · {escape_html(specialty['display'])}</strong><span>4 unidades · 48 clases · textos de 6 párrafos</span></a>")
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>3ro Medio — V2</title><style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Inter,sans-serif;background:#f1f5f9;color:#0f172a}}.hero{{background:linear-gradient(135deg,#0f172a,#334155,#f97316);color:white;padding:48px 20px;text-align:center}}.hero h1{{font-size:2.1rem;font-weight:800}}.hero p{{margin-top:8px;opacity:.9}}main{{max-width:1040px;margin:28px auto;padding:0 16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}.card{{background:white;border-radius:12px;border-top:6px solid #f97316;padding:18px;box-shadow:0 4px 14px rgba(15,23,42,.08);text-decoration:none;color:#0f172a;display:flex;flex-direction:column;gap:8px}}.card strong{{font-size:1.05rem}}.card span{{color:#64748b;font-size:.9rem}}</style></head><body><div class="hero"><h1>3ro Medio — Inglés Técnico V2</h1><p>5 especialidades · 4 unidades · 240 clases locales · sin deploy</p></div><main>{''.join(cards)}</main></body></html>"""


def build_rubric_summary():
    criteria = [
        ("Content / Contenido", "Clearly describes 3 tools, 2 systems/processes, and the importance of the specialty."),
        ("Technical Vocabulary / Vocabulario Técnico", "Uses 5+ technical terms accurately and naturally."),
        ("Pronunciation / Pronunciación", "Technical terms are clear, accurate, and understandable."),
        ("Fluency / Fluidez", "Maintains communication with natural rhythm and clear audio/video quality."),
        ("Structure / Estructura", "Includes introduction, body, and conclusion in a coherent order."),
        ("Subtitles / Subtítulos", "English subtitles are accurate, well synced, and reflect the oral text."),
    ]
    rows = "".join(f"<tr><td><strong>{escape_html(name)}</strong></td><td>{escape_html(description)}</td><td>4 pts</td></tr>" for name, description in criteria)
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Rubrica My Technical Skills — 3ro Medio</title><style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');body{{font-family:Inter,sans-serif;background:#fff7ed;color:#431407;line-height:1.6;margin:0}}header{{background:linear-gradient(135deg,#9a3412,#f97316);color:white;padding:40px 20px;text-align:center}}main{{max-width:920px;margin:28px auto;padding:0 16px}}table{{width:100%;border-collapse:collapse;background:white;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(67,20,7,.12)}}th{{background:#9a3412;color:white;text-align:left;padding:12px}}td{{padding:12px;border-bottom:1px solid #fed7aa}}.note{{background:white;border-left:5px solid #f97316;border-radius:10px;padding:14px 16px;margin-bottom:18px}}</style></head><body><header><h1>Video Presentation: My Technical Skills</h1><p>3ro Medio · 24 puntos · 6 criterios x 4 pts · subtítulos en inglés obligatorios</p></header><main><div class="note">Producto: video individual de 2 a 3 minutos sobre habilidades técnicas de la especialidad. Debe incluir 3 herramientas/equipos, 2 sistemas/procesos y relevancia social.</div><table><tr><th>Criterio</th><th>Excelente (referencia)</th><th>Puntaje</th></tr>{rows}</table></main></body></html>"""


def main():
    LEVEL_DIR.mkdir(parents=True, exist_ok=True)
    (LEVEL_DIR / "rubricas").mkdir(parents=True, exist_ok=True)
    (LEVEL_DIR / "rubricas" / "my-technical-skills.html").write_text(build_rubric_summary(), encoding="utf-8")
    total_classes = 0
    for specialty_slug, specialty in SPECIALTIES.items():
        (LEVEL_DIR / specialty_slug).mkdir(parents=True, exist_ok=True)
        (LEVEL_DIR / specialty_slug / "index.html").write_text(build_specialty_index(specialty_slug, specialty), encoding="utf-8")
        for unit_number, unit in UNIT_PLANS.items():
            output_dir = unit_dir_for(specialty_slug, unit_number)
            output_dir.mkdir(parents=True, exist_ok=True)
            for class_number, (class_title, grammar_focus, objective) in enumerate(unit["classes"], start=1):
                output_path = output_dir / class_file_name(unit_number, class_number, specialty_slug)
                output_path.write_text(build_class_html(specialty_slug, specialty, unit_number, class_number, class_title, grammar_focus, objective), encoding="utf-8")
                total_classes += 1
            (output_dir / "index.html").write_text(build_unit_index(specialty_slug, specialty, unit_number), encoding="utf-8")
            print(f"✓ {specialty_slug}/u{unit_number} — 12 classes")
    (LEVEL_DIR / "index.html").write_text(build_level_index(), encoding="utf-8")
    print(f"Done. {total_classes} classes generated locally in {LEVEL_DIR}")

if __name__ == "__main__":
    main()
