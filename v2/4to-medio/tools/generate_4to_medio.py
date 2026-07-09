# -*- coding: utf-8 -*-
"""
4to Medio V2 generator.
Local-only generation: 5 specialties x 4 units x 12 classes = 240 HTML files.
Every main reading text has exactly 6 paragraphs and keeps the strict v2 class structure.
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
        "course": "4to A",
        "name": "Mecanica Industrial",
        "display": "Mecánica Industrial",
        "field": "industrial mechanics",
        "student": "Diego",
        "workplace": "industrial workshop",
        "job": "CNC operator assistant",
        "first_work": "English CV and mock job interview",
        "source_focus": "CNC and MasterCAM documents consulted with the specialty teachers",
        "reading_assessment": "technical reading assessment based on MasterCAM and CNC materials",
        "evidence": "written English assessment on CNC and MasterCAM concepts, instructions, and terminology",
        "society": "manufacturing, mining, maintenance companies, hospitals, and public services need technicians who can read CNC instructions and follow safe machining procedures",
        "colors": ("#166534", "#16a34a", "#22c55e"),
        "terms": [
            ("CNC machine", "máquina CNC", "/ˌsiː en ˈsiː məˈʃiːn/", "A computer-controlled machine used to cut or shape material."),
            ("MasterCAM", "MasterCAM", "/ˈmæstər kæm/", "CAD/CAM software used to design and program machining operations."),
            ("toolpath", "trayectoria de herramienta", "/ˈtuːlpæθ/", "The path followed by a cutting tool during a CNC operation."),
            ("spindle", "husillo", "/ˈspɪndəl/", "The rotating part of a machine that holds or moves the cutting tool."),
            ("feed rate", "velocidad de avance", "/fiːd reɪt/", "The speed at which the tool moves through the material."),
            ("workpiece", "pieza de trabajo", "/ˈwɜːrkpiːs/", "The material or part being machined."),
            ("fixture", "dispositivo de sujeción", "/ˈfɪkstʃər/", "A device that holds the workpiece in the correct position."),
            ("G-code", "código G", "/ˈdʒiː koʊd/", "Programming language used to control CNC machine movements."),
            ("coolant", "refrigerante", "/ˈkuːlənt/", "Liquid used to reduce heat during machining."),
            ("tolerance", "tolerancia", "/ˈtɒlərəns/", "Allowed variation from a required measurement."),
            ("machining center", "centro de mecanizado", "/məˈʃiːnɪŋ ˈsentər/", "A CNC machine that performs several machining operations."),
            ("simulation", "simulación", "/ˌsɪmjəˈleɪʃən/", "A digital test of a process before real production."),
        ],
        "processes": [
            "programming a toolpath in MasterCAM",
            "setting up a CNC machine",
            "reading G-code before machining",
            "selecting feed rate and spindle speed",
            "simulating a machining operation",
            "measuring a finished workpiece against tolerance",
        ],
        "systems": ["CNC machining workflow", "CAD/CAM production chain", "industrial quality control", "machine safety protocol"],
        "u3_model": "CNC lathe setup: power on, home machine axes, load the program, mount the workpiece, set tool offsets, run simulation, and execute the program",
    },
    "automotriz": {
        "course": "4to B",
        "name": "Mecanica Automotriz",
        "display": "Mecánica Automotriz",
        "field": "automotive mechanics",
        "student": "Sofía",
        "workplace": "automotive workshop",
        "job": "automotive service assistant",
        "first_work": "customer service task in a mechanical workshop, focused on professional communication with the client and explanation of diagnosis and work done or pending",
        "source_focus": "vehicle systems, engine maintenance, brake systems, suspension, steering, electrical systems, front train components, fault diagnosis, and maintenance milestones",
        "reading_assessment": "technical reading assessment based on work guides, automotive systems, fault diagnosis, and vehicle maintenance milestones",
        "evidence": "customer service interaction explaining the diagnosis and the work that was done or will be done",
        "society": "families, emergency services, companies, public transport, and local businesses depend on safe vehicles and clear communication between the workshop and the client",
        "colors": ("#991b1b", "#dc2626", "#f97316"),
        "terms": [
            ("service order", "orden de servicio", "/ˈsɜːrvɪs ˈɔːrdər/", "A document that records the client's request and the work to be done."),
            ("customer complaint", "reclamo del cliente", "/ˈkʌstəmər kəmˈpleɪnt/", "The problem described by the vehicle owner."),
            ("diagnostic scanner", "escáner de diagnóstico", "/ˌdaɪəɡˈnɒstɪk ˈskænər/", "A device that reads vehicle fault codes and system data."),
            ("fault code", "código de falla", "/fɔːlt koʊd/", "A code that indicates a possible problem in a vehicle system."),
            ("maintenance schedule", "programa de mantenimiento", "/ˈmeɪntənəns ˈskedʒuːl/", "A plan that indicates when vehicle service tasks should be done."),
            ("brake system", "sistema de frenos", "/breɪk ˈsɪstəm/", "The system that slows or stops the vehicle."),
            ("suspension", "suspensión", "/səˈspenʃən/", "The system that supports the vehicle and absorbs road impacts."),
            ("steering system", "sistema de dirección", "/ˈstɪrɪŋ ˈsɪstəm/", "The system that controls the direction of the vehicle."),
            ("front axle", "tren delantero", "/frʌnt ˈæksəl/", "The front assembly that supports wheels, steering, and suspension components."),
            ("repair estimate", "presupuesto de reparación", "/rɪˈpeər ˈestɪmət/", "An approximate cost and description of the repair."),
            ("torque wrench", "torquímetro", "/tɔːrk rentʃ/", "A tool used to tighten bolts to a specified torque."),
            ("battery test", "prueba de batería", "/ˈbætəri test/", "A check of battery condition and electrical performance."),
        ],
        "processes": [
            "greeting a customer and recording a complaint",
            "explaining a diagnosis from a scanner report",
            "describing work done and work to be done",
            "checking brakes, suspension, and steering",
            "following a maintenance schedule milestone",
            "preparing a repair estimate for the client",
        ],
        "systems": ["customer service workflow", "engine and vehicle systems", "brake, suspension, and steering systems", "vehicle electrical system"],
        "u3_model": "brake pad replacement: lift the vehicle safely, remove the wheel, remove the caliper, replace pads, reassemble, and test the brakes",
    },
    "electricidad": {
        "course": "4to C",
        "name": "Electricidad",
        "display": "Electricidad",
        "field": "electricity",
        "student": "Mateo",
        "workplace": "electrical workshop",
        "job": "electrical installation assistant",
        "first_work": "English CV and mock job interview",
        "source_focus": "texts about electric motors, magnetism, and key technical terminology related to these contents",
        "reading_assessment": "technical reading assessment based on electric motors, magnetism, and key electrical terminology",
        "evidence": "audiovisual presentation with precise electrical terminology and safety language",
        "society": "homes, workshops, factories, schools, hospitals, and renewable energy projects require safe electrical installations and technicians who can explain risks clearly",
        "colors": ("#92400e", "#f59e0b", "#facc15"),
        "terms": [
            ("electric motor", "motor eléctrico", "/ɪˈlektrɪk ˈmoʊtər/", "A machine that converts electrical energy into mechanical movement."),
            ("magnetic field", "campo magnético", "/mæɡˈnetɪk fiːld/", "The invisible force area around magnets or electric current."),
            ("coil", "bobina", "/kɔɪl/", "A wound wire that creates a magnetic field when current passes through it."),
            ("stator", "estator", "/ˈsteɪtər/", "The stationary part of an electric motor."),
            ("rotor", "rotor", "/ˈroʊtər/", "The rotating part of an electric motor."),
            ("contactor", "contactor", "/kənˈtæktər/", "An electrical switch used to control a motor or circuit."),
            ("three-phase system", "sistema trifásico", "/θriː feɪz ˈsɪstəm/", "An electrical power system using three alternating currents."),
            ("insulation", "aislamiento", "/ˌɪnsəˈleɪʃən/", "Material that prevents unwanted electrical contact."),
            ("winding", "devanado", "/ˈwaɪndɪŋ/", "Wire loops inside a motor or transformer."),
            ("nameplate", "placa de datos", "/ˈneɪmpleɪt/", "A label with technical data about a machine."),
            ("grounding", "puesta a tierra", "/ˈɡraʊndɪŋ/", "A safety connection that directs fault current to earth."),
            ("current draw", "consumo de corriente", "/ˈkʌrənt drɔː/", "The amount of current used by a device while operating."),
        ],
        "processes": [
            "reading a motor nameplate",
            "checking insulation before connection",
            "explaining how a magnetic field moves a rotor",
            "connecting a three-phase motor safely",
            "measuring current draw during a test",
            "applying lockout/tagout before electrical work",
        ],
        "systems": ["electric motor system", "electromagnetism and motor control", "three-phase installation", "motor protection circuit"],
        "u3_model": "three-phase motor connection: verify power is off, identify wiring, connect leads, ground the motor, test rotation, and verify current draw",
    },
    "grafica": {
        "course": "4to D",
        "name": "Grafica",
        "display": "Gráfica",
        "field": "graphic production",
        "student": "Camila",
        "workplace": "graphic production lab",
        "job": "digital print production assistant",
        "first_work": "English CV and mock job interview",
        "source_focus": "documents and materials linked to the recently acquired equipment in the specialty",
        "reading_assessment": "technical reading assessment based on documentation for the recently acquired graphic production equipment",
        "evidence": "explanatory video with professional vocabulary from the graphic production area",
        "society": "schools, companies, public campaigns, local businesses, and community organizations need clear printed and digital communication produced with professional workflows",
        "colors": ("#6b21a8", "#a855f7", "#ec4899"),
        "terms": [
            ("digital press", "prensa digital", "/ˈdɪdʒɪtəl pres/", "A printing machine that produces documents directly from digital files."),
            ("equipment manual", "manual del equipo", "/ɪˈkwɪpmənt ˈmænjuəl/", "A document that explains how to use and maintain a machine."),
            ("RIP software", "software RIP", "/rɪp ˈsɔːftwer/", "Software that prepares digital files for printing."),
            ("print queue", "cola de impresión", "/prɪnt kjuː/", "A list of print jobs waiting to be processed."),
            ("color calibration", "calibración de color", "/ˈkʌlər ˌkælɪˈbreɪʃən/", "Adjustment of equipment to produce accurate colors."),
            ("substrate", "sustrato", "/ˈsʌbstreɪt/", "The material printed on, such as paper, vinyl, or cardboard."),
            ("proof", "prueba de impresión", "/pruːf/", "A test print used to check quality before final production."),
            ("registration", "registro", "/ˌredʒɪˈstreɪʃən/", "Correct alignment of colors or printed elements."),
            ("finishing unit", "unidad de terminación", "/ˈfɪnɪʃɪŋ ˈjuːnɪt/", "Equipment used for cutting, folding, laminating, or binding."),
            ("maintenance log", "registro de mantención", "/ˈmeɪntənəns lɔːɡ/", "A record of cleaning, checks, and equipment service."),
            ("preflight", "revisión previa", "/ˈpriːflaɪt/", "A check of a file before printing."),
            ("bleed", "sangrado", "/bliːd/", "Extra image area that extends beyond the cut line."),
        ],
        "processes": [
            "reading the equipment manual before operation",
            "preflighting a print-ready file",
            "calibrating color before a production run",
            "managing the print queue",
            "producing a proof for approval",
            "recording equipment maintenance after use",
        ],
        "systems": ["digital print workflow", "equipment documentation", "color management system", "production and finishing workflow"],
        "u3_model": "digital print production: read the job ticket, preflight the file, calibrate color, print a proof, correct settings, and produce the final run",
    },
    "electronica": {
        "course": "4to E",
        "name": "Electronica",
        "display": "Electrónica",
        "field": "electronics",
        "student": "Valentina",
        "workplace": "electronics lab",
        "job": "automation and electronics assistant",
        "first_work": "English CV and mock job interview",
        "source_focus": "texts about electric motors, automation with sensors, actuators and PLC, power electronics, servomechanisms, and consumer electronics",
        "reading_assessment": "technical reading assessment based on automation, power electronics, servomechanisms, electric motors, and consumer electronics",
        "evidence": "English demonstration of assembly, checking, or troubleshooting in electronic systems",
        "society": "automation systems, consumer devices, medical equipment, transport, communication networks, and smart homes depend on precise electronic diagnosis and safe repair decisions",
        "colors": ("#1e40af", "#2563eb", "#06b6d4"),
        "terms": [
            ("PLC", "PLC", "/ˌpiː el ˈsiː/", "A programmable logic controller used to automate machines."),
            ("sensor", "sensor", "/ˈsensər/", "A component that detects a physical condition or signal."),
            ("actuator", "actuador", "/ˈæktʃueɪtər/", "A component that creates movement or action in a system."),
            ("servo motor", "servomotor", "/ˈsɜːrvoʊ ˈmoʊtər/", "A motor controlled precisely for position, speed, or movement."),
            ("power electronics", "electrónica de potencia", "/ˈpaʊər ɪˌlekˈtrɒnɪks/", "Electronics used to control and convert electrical power."),
            ("inverter", "inversor", "/ɪnˈvɜːrtər/", "A device that converts DC power into AC power or controls motor speed."),
            ("circuit board", "placa electrónica", "/ˈsɜːrkɪt bɔːrd/", "A board that holds and connects electronic components."),
            ("oscilloscope", "osciloscopio", "/əˈsɪləskoʊp/", "An instrument that displays electrical signals over time."),
            ("relay", "relé", "/ˈriːleɪ/", "An electrically operated switch."),
            ("troubleshooting", "resolución de fallas", "/ˈtrʌbəlˌʃuːtɪŋ/", "The process of finding and correcting problems."),
            ("diode", "diodo", "/ˈdaɪoʊd/", "A component that allows current to flow mainly in one direction."),
            ("transistor", "transistor", "/trænˈzɪstər/", "A component used to switch or amplify electrical signals."),
        ],
        "processes": [
            "wiring a PLC input safely",
            "testing a sensor-actuator sequence",
            "reading a power electronics diagram",
            "checking servo motor movement",
            "troubleshooting a consumer electronics fault",
            "measuring signals with an oscilloscope",
        ],
        "systems": ["automation system", "power electronics circuit", "servomechanism", "consumer electronics troubleshooting workflow"],
        "u3_model": "sensor integration project: select the sensor, connect it to controller pins, upload firmware, calibrate the reading, test the output, and document results",
    },
}

COMMON_TERMS = [
    ("employability", "empleabilidad", "/ɪmˌplɔɪəˈbɪləti/", "Skills and attitudes that help a person get and keep a job."),
    ("CV", "currículum vitae", "/ˌsiː ˈviː/", "A document that summarizes education, skills, and experience."),
    ("job interview", "entrevista laboral", "/dʒɑːb ˈɪntərvjuː/", "A formal conversation for a job application."),
    ("technical vocabulary", "vocabulario técnico", "/ˈteknɪkəl voʊˈkæbjəleri/", "Words used in a specific technical field."),
    ("work order", "orden de trabajo", "/wɜːrk ˈɔːrdər/", "A document that explains a task to be completed."),
    ("procedure", "procedimiento", "/prəˈsiːdʒər/", "A series of ordered steps for completing a task."),
    ("safety precaution", "precaución de seguridad", "/ˈseɪfti prɪˈkɔːʃən/", "An action taken to reduce risk before work."),
    ("manual", "manual", "/ˈmænjuəl/", "A document with instructions, warnings, and technical information."),
    ("evidence", "evidencia", "/ˈevɪdəns/", "Information that supports a conclusion or decision."),
    ("technical report", "informe técnico", "/ˈteknɪkəl rɪˈpɔːrt/", "A structured explanation of a technical situation."),
    ("project defense", "defensa de proyecto", "/ˈprɑːdʒekt dɪˈfens/", "An oral presentation that explains and justifies a project."),
    ("critical thinking", "pensamiento crítico", "/ˈkrɪtɪkəl ˈθɪŋkɪŋ/", "Reasoned analysis used to evaluate information and decisions."),
]

UNIT_PLANS = {
    1: {
        "title": "Professional Profile & Workplace English",
        "product": "CV in English + Mock Job Interview video",
        "theme": "employability, professional profile, CV, and workplace interview communication",
        "classes": [
            ("My Professional Profile", "Present Simple + professional identity", "describe a professional profile for the specialty"),
            ("Job Ads and Requirements", "Must / have to / need to", "identify job requirements and technical skills"),
            ("CV Sections in English", "CV headings + concise noun phrases", "organize a CV using required English sections"),
            ("Objective and Skills", "Action verbs + can / be able to", "write an objective and skill statements for a TP job"),
            ("Technical Vocabulary in a CV", "Noun phrases + technical terms", "include specialty vocabulary in a CV"),
            ("Grammar and Spelling Check", "Past Simple for experience + present for skills", "revise grammar and spelling in CV statements"),
            ("General Interview Questions", "WH-questions + professional answers", "answer general job interview questions"),
            ("Technical Interview Questions", "Because / so / therefore", "answer technical interview questions with evidence"),
            ("Interviewer Performance", "Follow-up questions + polite language", "ask questions and react professionally"),
            ("Video Interview Script", "Dialogue structure + turn-taking", "prepare a paired mock interview script"),
            ("Rehearsal and Feedback", "Pronunciation + fluency practice", "rehearse the interview and improve delivery"),
            ("Mock Job Interview", "Integrated oral performance", "record and submit the interview video"),
        ],
    },
    2: {
        "title": "Advanced Technical Reading & Critical Thinking",
        "product": "Technical reading test + semester integrative assessment",
        "theme": "specialty documentation, explicit information, inference, opinion, and critical analysis",
        "classes": [
            ("Reading Specialty Documents", "Skimming + scanning", "identify main ideas and details in a technical document"),
            ("Vocabulary From Manuals", "Context clues", "infer meaning from technical context"),
            ("Instructions and Warnings", "Imperatives + must / must not", "interpret warnings and mandatory instructions"),
            ("Cause, Risk, and Consequence", "because / so / therefore", "explain causes and consequences in technical situations"),
            ("Diagrams, Labels, and Data", "There is/are + prepositions", "read diagrams, labels, and basic data"),
            ("Critical Reading of Procedures", "Should / shouldn't", "evaluate whether a procedure is safe and complete"),
            ("Preparing a Technical Reading Test", "Question stems + evidence", "prepare for explicit, implicit, analysis, and critical questions"),
            ("Technical Reading Test", "Integrated reading skills", "complete a technical reading assessment"),
            ("Integrative Assessment Part I", "Reading + vocabulary review", "connect technical reading with employability"),
            ("Integrative Assessment Part II", "Oral explanation + reflection", "explain a technical decision orally"),
            ("Critical Reflection", "Opinion paragraphs", "write a reasoned opinion about a technical issue"),
            ("Portfolio Review", "Goal setting language", "review progress and set goals for semester two"),
        ],
    },
    3: {
        "title": "Technical Documentation & Procedures",
        "product": "Oral explanation of a technical procedure (20 pts)",
        "theme": "technical procedures, SOPs, troubleshooting, reports, and oral sequencing",
        "classes": [
            ("Standard Operating Procedures", "Imperatives + sequence connectors", "identify parts of a technical procedure"),
            ("Writing Clear Steps", "First / next / after that / finally", "write clear procedural steps"),
            ("Video Procedure Analysis", "Comparatives + evaluation language", "compare a professional procedure with workshop practice"),
            ("Technical Report Structure", "Report sections + past tense", "recognize report sections and findings"),
            ("Troubleshooting Checklist", "If / then + should", "prepare a troubleshooting checklist"),
            ("Safety Precautions", "Must / have to / should", "explain safety before a procedure"),
            ("Selecting a Procedure", "Justification language", "choose a procedure to explain orally"),
            ("Procedure Script", "Sequencing + purpose clauses", "write a 3-4 minute procedure script"),
            ("Technical Vocabulary Rehearsal", "Word stress + IPA", "rehearse key terms accurately"),
            ("Oral Procedure Practice", "Fluency + signposting", "practice the oral explanation with peer feedback"),
            ("Oral Procedure Evaluation", "Integrated oral performance", "explain a technical procedure in English"),
            ("Project Topic Selection", "Future plans + proposal language", "select a topic for the final project defense"),
        ],
    },
    4: {
        "title": "Innovation, Project Defense & Closure",
        "product": "Advanced reading test + final project defense in English",
        "theme": "advanced technical reading, innovation, project defense, and end-of-cycle reflection",
        "classes": [
            ("Innovation in My Specialty", "Future forms + technical trends", "read about innovation connected to the specialty"),
            ("Benefits and Risks", "On the one hand / however", "analyze benefits and risks of a technical change"),
            ("Comparing Technical Solutions", "Comparatives + superlatives", "compare two technical solutions"),
            ("Debating a Technical Decision", "Opinion and rebuttal language", "defend a technical position with reasons"),
            ("Advanced Reading Review", "Inference + critical reading", "prepare for advanced reading questions"),
            ("Advanced Reading Test", "Integrated reading assessment", "complete an advanced reading assessment"),
            ("Project Problem and Solution", "Problem-solution structure", "define a final project problem and solution"),
            ("Evidence for My Project", "Evidence language", "select evidence that supports the project"),
            ("Project Defense Script", "Presentation structure", "write a clear defense script"),
            ("Visual Support and Questions", "Presentation language + Q&A", "prepare visual support and possible answers"),
            ("Final Project Defense", "Integrated oral defense", "defend the final project in English"),
            ("Closure and Professional Reflection", "Reflection language", "reflect on professional growth and next steps"),
        ],
    },
}

FILL_PATTERNS = {
    1: [
        ("I ___ applying for a position connected to my specialty.", "am"),
        ("My CV ___ technical skills and education.", "includes"),
        ("A good objective ___ clear and specific.", "is"),
        ("I ___ operate basic tools safely.", "can"),
        ("The interviewer ___ at least four questions.", "asks"),
        ("The interviewee ___ use the CV as support.", "can"),
        ("Technical vocabulary ___ the answer more professional.", "makes"),
        ("We ___ two general and two technical questions.", "prepare"),
        ("Pronunciation ___ important in a video interview.", "is"),
        ("The final video ___ approximately five minutes.", "lasts"),
    ],
    2: [
        ("The text ___ technical information from the specialty.", "contains"),
        ("Students ___ scan for specific details.", "must"),
        ("Warnings ___ read before operating equipment.", "are"),
        ("A diagram ___ labels and symbols.", "has"),
        ("The cause ___ explained with evidence.", "is"),
        ("If a step is missing, the procedure ___ be unsafe.", "may"),
        ("The test ___ vocabulary and comprehension.", "includes"),
        ("Critical thinking ___ more than copying information.", "requires"),
        ("An opinion ___ be supported with reasons.", "should"),
        ("The semester portfolio ___ progress.", "shows"),
    ],
    3: [
        ("First, the procedure ___ introduced.", "is"),
        ("The technician ___ safety precautions before starting.", "explains"),
        ("Each step ___ in a clear order.", "is described"),
        ("The student ___ use full sentences, not only words.", "should"),
        ("A checklist ___ prevent mistakes.", "can"),
        ("If the system fails, the technician ___ stop and check evidence.", "must"),
        ("The oral explanation ___ three to four minutes.", "lasts"),
        ("Technical terms ___ pronounced clearly.", "are"),
        ("The conclusion ___ why the procedure matters.", "explains"),
        ("Peer feedback ___ the final performance.", "improves"),
    ],
    4: [
        ("Innovation ___ change a technical workplace.", "can"),
        ("A risk ___ be identified before a project starts.", "should"),
        ("Two solutions ___ compared with evidence.", "are"),
        ("The advanced test ___ inference and critical thinking.", "includes"),
        ("A project defense ___ a problem and a solution.", "presents"),
        ("Students ___ explain why their decision is appropriate.", "must"),
        ("Visual support ___ help the audience understand.", "can"),
        ("Questions ___ answered with clear reasons.", "are"),
        ("The final defense ___ evaluated with a rubric.", "is"),
        ("Professional reflection ___ next steps.", "identifies"),
    ],
}

READING_LABELS = ["Explicit", "Explicit", "Explicit", "Implicit (inference)", "Analysis", "Critical thinking"]


def escape_html(value):
    return html.escape(str(value), quote=False)


def class_file_name(unit_number, class_number, specialty_slug):
    return f"Clase_{class_number:02d}_U{unit_number}_4to_{specialty_slug}.html"


def select_vocab(specialty, class_number):
    specialty_terms = specialty["terms"]
    start = (class_number - 1) % len(specialty_terms)
    rotated_specialty = specialty_terms[start:] + specialty_terms[:start]
    common_start = (class_number - 1) % len(COMMON_TERMS)
    rotated_common = COMMON_TERMS[common_start:] + COMMON_TERMS[:common_start]
    selected = []
    seen = set()
    for term in list(rotated_specialty[:6]) + rotated_common + list(rotated_specialty[6:]):
        key = term[0].lower()
        if key in seen:
            continue
        selected.append(term)
        seen.add(key)
        if len(selected) == 10:
            break
    return selected


def u3_context(specialty, class_number, vocab_terms):
    process_a = specialty["processes"][(class_number - 1) % len(specialty["processes"])]
    process_b = specialty["processes"][class_number % len(specialty["processes"])]
    system = specialty["systems"][(class_number - 1) % len(specialty["systems"])]
    term_a, term_b, term_c = [term[0] for term in vocab_terms[:3]]
    return process_a, process_b, system, term_a, term_b, term_c


def u3_fill_patterns(specialty, class_number, vocab_terms):
    process_a, process_b, system, term_a, term_b, term_c = u3_context(specialty, class_number, vocab_terms)

    if class_number == 1:
        return [
            (f"First, the team ___ the work area before {process_a}.", "checks"),
            (f"Next, the operator ___ {term_a}, {term_b}, and {term_c}.", "verifies"),
            (f"A standard operating procedure ___ the sequence clearly.", "presents"),
            (f"One missed step ___ the full task.", "can affect"),
            (f"The opening checks ___ the rest of the workflow safer.", "make"),
            (f"The text ___ why order matters in technical work.", "explains"),
            (f"The procedure also ___ {system}.", "mentions"),
            (f"Students ___ sequence language such as first and finally.", "use"),
            (f"Clear English ___ apprentices follow the same order.", "helps"),
            (f"An SOP ___ quality, safety, and communication.", "protects"),
        ]
    if class_number == 2:
        return [
            (f"A messy instruction sheet ___ {process_a} difficult to follow.", "makes"),
            (f"First, the technician ___ {term_a}.", "checks"),
            (f"Next, the technician ___ {term_b}.", "prepares"),
            (f"After that, the team ___ alignment with {term_c}.", "confirms"),
            (f"Each instruction ___ only one clear action.", "contains"),
            (f"A good procedure ___ hesitation and repeated questions.", "reduces"),
            (f"The revised version ___ {system}.", "fits"),
            (f"One student ___ the draft aloud to test clarity.", "reads"),
            (f"The listener ___ whenever the sequence is confusing.", "pauses"),
            (f"Clear steps ___ more reliable work.", "create"),
        ]
    if class_number == 3:
        return [
            (f"Both technicians ___ {process_a}, but in different ways.", "explain"),
            (f"The second speaker ___ {term_a}, {term_b}, and {term_c} carefully.", "points to"),
            (f"A good explanation ___ another person understand the risks.", "helps"),
            (f"Speed alone ___ not a sign of professionalism.", "is"),
            (f"Students ___ two demonstrations using comparative language.", "compare"),
            (f"One explanation ___ clearer than the other.", "is"),
            (f"The class ___ the video with {system}.", "connects"),
            (f"Unclear communication ___ a correct action happen at the wrong time.", "can make"),
            (f"Evaluation notes ___ evidence, not personal preference.", "use"),
            (f"A strong explanation ___ correct, understandable, and useful.", "is"),
        ]
    if class_number == 4:
        return [
            (f"The report ___ the context and exact moment of the problem.", "states"),
            (f"A trainee ___ {term_a} while another checked {term_b}.", "inspected"),
            (f"The findings ___ observation from opinion.", "separate"),
            (f"The writer ___ dramatic language in the report.", "avoids"),
            (f"One repeated safety check ___ part of the findings.", "became"),
            (f"The document ___ the wider impact on {system}.", "explains"),
            (f"Students ___ sections like context and recommendation.", "label"),
            (f"A technical report ___ knowledge for the next shift.", "preserves"),
            (f"The structure ___ another technician trust the document.", "helps"),
            (f"Professional tone ___ the report more useful.", "makes"),
        ]
    if class_number == 5:
        return [
            (f"The checklist ___ with simple confirmations before {process_a}.", "starts"),
            (f"Technicians ___ whether {term_a} is in the expected condition.", "check"),
            (f"They also ___ whether {term_b} has been verified.", "confirm"),
            (f"The next block ___ on the process itself.", "focuses"),
            (f"A missing answer today ___ a repeated failure tomorrow.", "can become"),
            (f"Ordered questions ___ the diagnosis from guesswork.", "protect"),
            (f"The checklist ___ the symptom with {system}.", "connects"),
            (f"If the symptom repeats, the team ___ the stage.", "isolates"),
            (f"If the symptom disappears, the technician ___ recent changes.", "reviews"),
            (f"A checklist ___ troubleshooting into justified decisions.", "turns"),
        ]
    if class_number == 6:
        return [
            (f"Before {process_a}, staff ___ the area and secure materials.", "inspect"),
            (f"The first part ___ that {term_a} and {term_b} are ready.", "confirms"),
            (f"A worker ___ a check in the near-miss example.", "skipped"),
            (f"A reading on {term_c} ___ that the setup was incomplete.", "suggested"),
            (f"Safety ___ not separate from technical quality.", "is"),
            (f"If the safety routine fails, the procedure ___ unreliable.", "becomes"),
            (f"The bulletin also ___ {system}.", "mentions"),
            (f"Students ___ recommendations with must and should.", "practice"),
            (f"Technicians ___ continue if a warning sign appears.", "must not"),
            (f"The best procedure ___ safe, clear, and repeatable.", "is"),
        ]
    if class_number == 7:
        return [
            (f"Students ___ one procedure from the monthly workload.", "choose"),
            (f"A familiar task ___ easier to describe.", "is"),
            (f"A more complex option ___ richer vocabulary such as {term_a} and {term_b}.", "includes"),
            (f"The supervisor ___ both students to justify their choice.", "asks"),
            (f"A strong procedure ___ relevance, clear steps, and technical decisions.", "shows"),
            (f"Some procedures ___ to a wider workflow in {system}.", "belong"),
            (f"Students ___ short justifications in English.", "write"),
            (f"A good choice ___ the later oral explanation clearer.", "makes"),
            (f"Choosing a procedure ___ already a technical decision.", "is"),
            (f"The final explanation ___ more authentic after a justified choice.", "sounds"),
        ]
    if class_number == 8:
        return [
            (f"A trainee ___ a procedure script for {process_a}.", "drafts"),
            (f"The opening section ___ the purpose and required materials.", "states"),
            (f"The middle section ___ checks related to {term_a}, {term_b}, and {term_c}.", "includes"),
            (f"The first version ___ too dense for oral presentation.", "is"),
            (f"Shorter sentences ___ the script easier to use.", "make"),
            (f"A good script ___ speaking instead of memorization.", "supports"),
            (f"The conclusion ___ how the task fits into {system}.", "shows"),
            (f"Students ___ purpose clauses such as 'to verify' and 'to prevent'.", "highlight"),
            (f"Clarity ___ stronger than quantity in technical speaking.", "is"),
            (f"The final draft ___ more with fewer words.", "communicates"),
        ]
    if class_number == 9:
        return [
            (f"On rehearsal day, students ___ key terms before explaining {process_a}.", "practice"),
            (f"The pronunciation sheet ___ words such as {term_a}, {term_b}, and {term_c}.", "groups"),
            (f"Students ___ stressed syllables on the sheet.", "mark"),
            (f"Some learners ___ the word on paper but not aloud.", "know"),
            (f"The rehearsal ___ them bridge that gap.", "helps"),
            (f"Each term ___ to an action inside {system}.", "belongs"),
            (f"One student ___ the term while the partner explains its role.", "says"),
            (f"If the explanation is vague, the pair ___ the sentence again.", "reviews"),
            (f"Clear pronunciation ___ professional credibility.", "supports"),
            (f"Accurate terminology ___ the procedure easier to teach.", "makes"),
        ]
    if class_number == 10:
        return [
            (f"One student ___ the sequence while the partner listens.", "presents"),
            (f"The feedback card ___ structure and technical clarity.", "checks"),
            (f"The first attempt ___ too quickly between stages.", "moves"),
            (f"On the second attempt, the speaker ___ clearer signposting.", "adds"),
            (f"Transitions ___ the audience follow the explanation.", "help"),
            (f"The pair also ___ how the task fits into {system}.", "discusses"),
            (f"When roles change, the second student ___ feedback too.", "receives"),
            (f"Peer practice ___ problems while there is still time to improve.", "reveals"),
            (f"Fluency ___ not the same as speaking fast.", "is"),
            (f"Technical fluency ___ guiding the listener with order and confidence.", "means"),
        ]
    if class_number == 11:
        return [
            (f"Each student ___ a real procedure for evaluation day.", "chooses"),
            (f"The strongest presentation ___ careful use of {term_a}.", "shows"),
            (f"One speaker ___ why a verification step matters before mentioning {term_b}.", "explains"),
            (f"The rubric ___ connection with {system}.", "values"),
            (f"Follow-up questions ___ whether the speaker truly understands the procedure.", "reveal"),
            (f"A clear introduction ___ the audience follow the sequence.", "helps"),
            (f"Purpose ___ stronger than repetition in a good performance.", "is"),
            (f"Practice and performance ___ different by the end of the class.", "sound"),
            (f"Technical English ___ meaningful when it explains real work.", "becomes"),
            (f"A strong oral evaluation ___ clarity, sequence, and understanding.", "combines"),
        ]
    return [
        (f"Students ___ possible final project topics connected to {process_a} and {process_b}.", "propose"),
        (f"A strong topic ___ room for vocabulary such as {term_a}, {term_b}, and {term_c}.", "creates"),
        (f"The instructor ___ every student for a problem, purpose, and outcome.", "asks"),
        (f"A weak topic ___ too broad or too vague.", "is"),
        (f"The class ___ how each idea fits into {system}.", "checks"),
        (f"Students ___ short proposal sentences in English.", "write"),
        (f"A good project topic ___ concrete and defensible.", "is"),
        (f"Professional communication ___ with a clear question.", "starts"),
        (f"The final proposal ___ technical reasons, not only enthusiasm.", "needs"),
        (f"Topic selection ___ part of the final defense process.", "becomes"),
    ]


def u3_reading_questions(specialty, class_number, class_title, vocab_terms):
    process_a, process_b, system, term_a, term_b, term_c = u3_context(specialty, class_number, vocab_terms)

    if class_number == 1:
        return [
            f"What sequence does the SOP ask the team to follow before starting?",
            f"Which three items must be checked before action begins?",
            f"What does the procedure say can happen if one step is missed?",
            f"Why does the text present an SOP as more than bureaucracy?",
            f"How does sequence language support technical communication in the reading?",
            f"Should all apprentices learn to explain a standard procedure clearly? Justify with one idea from the text.",
        ]
    if class_number == 2:
        return [
            f"What problem did the first draft instruction sheet have?",
            f"What were the first three rewritten actions in the improved version?",
            f"How did the team test whether the new draft was clear?",
            f"Why can unclear writing produce preventable errors in the workshop?",
            f"How does the text connect clear steps with reliable work?",
            f"Should technical procedures be rewritten when the order is confusing? Justify.",
        ]
    if class_number == 3:
        return [
            f"How were the two technicians different in the training video?",
            f"What terms or objects did the clearer speaker point to?",
            f"What did students decide about speed and professionalism?",
            f"Why can unclear communication be almost the same as a wrong action?",
            f"How does comparative language help evaluate a technical explanation?",
            f"Is a slower but clearer explanation better for training purposes? Justify.",
        ]
    if class_number == 4:
        return [
            f"What did the first section of the report include?",
            f"Who inspected {term_a} and who checked {term_b}?",
            f"What pattern of report sections did students identify?",
            f"Why does the writer avoid dramatic language in the findings?",
            f"How does the report connect one fault with the wider impact on {system}?",
            f"Should technical reports prioritize facts over emotion? Justify with one idea from the text.",
        ]
    if class_number == 5:
        return [
            f"What confirmations appeared at the start of the checklist?",
            f"What questions guided the diagnosis in the second block?",
            f"What did the instructor say about skipping checklist questions?",
            f"Why do ordered questions protect diagnosis from guesswork?",
            f"How does the text show that a checklist supports technical reasoning?",
            f"Would you use a checklist before replacing a component? Justify.",
        ]
    if class_number == 6:
        return [
            f"What precautions did the safety bulletin require before the procedure?",
            f"What recent near miss did the document describe?",
            f"What warning sign showed that the setup was incomplete?",
            f"Why does the text say safety is built into the technical system itself?",
            f"How do must and should become part of real workplace responsibility in the class?",
            f"Should safety language be practiced in English as part of technical training? Justify.",
        ]
    if class_number == 7:
        return [
            f"What options did students consider when choosing a procedure?",
            f"Why did some students prefer familiar tasks and others more complex ones?",
            f"What three criteria did the class identify for a strong choice?",
            f"Why can procedures connected to a wider workflow be better for oral explanation?",
            f"How does the reading show that choosing a procedure is already a technical decision?",
            f"Should students justify their procedure choice before presenting it? Justify.",
        ]
    if class_number == 8:
        return [
            f"What parts did the trainee include in the procedure script?",
            f"Which checks were mentioned in the middle section of the script?",
            f"Why did the instructor ask for shorter sentences?",
            f"Why should a script support speaking instead of memorization?",
            f"How do purpose clauses improve the explanation according to the text?",
            f"Is a shorter and clearer script more effective for oral presentation? Justify.",
        ]
    if class_number == 9:
        return [
            f"What was the first focus of rehearsal day?",
            f"Which difficult words were grouped on the pronunciation sheet?",
            f"What problem appeared when students tried to say the terms aloud?",
            f"Why does the vocabulary sheet connect each term with a real action?",
            f"How does the text link pronunciation with professional credibility?",
            f"Should pronunciation be evaluated in technical procedure explanations? Justify.",
        ]
    if class_number == 10:
        return [
            f"What did the feedback card check during the first practice round?",
            f"What problem did the listener identify in the first attempt?",
            f"What changed in the second attempt?",
            f"Why is signposting important when a procedure belongs to a larger workflow?",
            f"How does peer practice help improve oral technical explanations?",
            f"Is fluency in technical English the same as speaking fast? Justify with one idea from the text.",
        ]
    if class_number == 11:
        return [
            f"What made the strongest presentations sound understood rather than memorized?",
            f"How did one student explain the importance of a verification step?",
            f"What did the teacher's follow-up questions reveal?",
            f"Why does the rubric value connection with {system}?",
            f"How does the text distinguish practice from final performance?",
            f"Should oral procedure evaluation include follow-up questions? Justify.",
        ]
    return [
        f"What did the instructor ask each student to propose for the final project?",
        f"What makes a topic weak and what makes it stronger?",
        f"Which real processes already known by students were mentioned as examples?",
        f"Why does the class revisit {system} when selecting topics?",
        f"How does the reading connect topic selection with professional communication?",
        f"Should a final project topic be concrete and defensible in English? Justify.",
    ]


def make_u3_text(specialty, class_number, class_title, grammar_focus, vocab_terms):
    process_a = specialty["processes"][(class_number - 1) % len(specialty["processes"])]
    process_b = specialty["processes"][class_number % len(specialty["processes"])]
    system = specialty["systems"][(class_number - 1) % len(specialty["systems"])]
    term_a, term_b, term_c = [term[0] for term in vocab_terms[:3]]
    display = specialty["display"]

    if class_number == 1:
        return [
            f"The morning shift in the {specialty['workplace']} begins with a short standard operating procedure for {process_a}. The document is clear: check the work area, review the equipment status, confirm the required information, and only then start the technical task.",
            f"The operator reads the first lines carefully because one missed step can affect the full sequence. In this case, the SOP asks the team to verify {term_a}, confirm the condition of {term_b}, and prepare {term_c} before any movement or adjustment begins.",
            f"A second paragraph explains why order matters. When a technician starts too quickly, small details disappear: a missing label, an unstable reading, or an incorrect tool position. Those details may look minor at the start, but they often explain later problems.",
            f"The procedure also refers to {system}. That system depends on consistency, because every stage prepares the next one. If the opening checks are weak, the rest of the process becomes slower, less safe, and more expensive.",
            f"In the last section, the supervisor reminds new staff to use sequence language when they explain the task: first, next, after that, and finally. Clear language helps apprentices follow the same order without confusion.",
            f"By the end of the reading, the message is simple: a standard operating procedure is not bureaucracy. It is a professional tool that protects quality, safety, and communication in {display}.",
        ]
    if class_number == 2:
        return [
            f"A draft instruction sheet on the supervisor's desk describes {process_a}, but the writing is messy and difficult to follow. Some steps are too long, two actions are mixed in the same sentence, and the final verification appears before the preparation stage.",
            f"The team rewrites the document so that each instruction contains only one clear action. First, the technician checks {term_a}. Next, the technician prepares {term_b}. After that, the technician confirms settings or alignment with {term_c}.",
            f"As the sheet improves, the workshop notices how language changes the quality of work. A good procedure does not only tell people what to do; it also reduces hesitation, repeated questions, and preventable errors.",
            f"The revised version also mentions {system}. Procedures inside that system must be easy to scan quickly because technicians often consult them while working under time pressure.",
            f"To test the new draft, one student reads the instructions aloud while another follows them step by step. Whenever the listener pauses or misunderstands a sequence, the sentence is corrected again.",
            f"The final text proves that technical English should be direct and useful. Clear steps create better routines, and better routines create more reliable work in {display}.",
        ]
    if class_number == 3:
        return [
            f"A training video in the {specialty['workplace']} shows two technicians explaining the same procedure. Both complete {process_a}, but their demonstrations are different in pace, clarity, and detail.",
            f"The first technician works fast and uses many technical words without explanation. The second technician moves more slowly, points to {term_a}, {term_b}, and {term_c}, and explains why each action matters before moving forward.",
            f"After watching both versions, the apprentices compare them. They decide that speed alone is not a sign of professionalism. A good procedure explanation must help another person understand the order, the purpose, and the risks involved.",
            f"The class also connects the video to {system}. In that system, unclear communication can produce a correct action at the wrong time, which is almost the same as a wrong action.",
            f"Students write short evaluation notes using comparative language: one explanation is clearer, another is shorter, and one speaker is more careful with safety details. Their comments are based on evidence from the video, not on personal preference.",
            f"The conclusion is practical: an excellent technical explanation is not only correct. It is also understandable, well sequenced, and useful for someone who needs to repeat the task accurately.",
        ]
    if class_number == 4:
        return [
            f"The workshop manager receives a technical report after a problem appears during {process_a}. The first section states the context, the affected equipment, and the exact moment when the team noticed that something was wrong.",
            f"The second section records the findings. A trainee inspected {term_a}, another checked {term_b}, and the lead technician compared the result with the normal value shown in the previous report. Those details matter because they separate observation from opinion.",
            f"In the findings paragraph, the writer avoids dramatic language. Instead of saying the process was 'a disaster,' the report explains that one stage was incomplete, one measurement was unstable, and one safety check had to be repeated.",
            f"The document then refers to {system} to explain the wider impact. A report should not only mention the isolated fault; it should show how the problem can affect workflow, safety, or final quality.",
            f"When students label the sections, they notice a pattern: context, findings, probable cause, action taken, and recommendation. That structure turns a confusing event into a document that another technician can trust.",
            f"By the final line, the report sounds professional because it is organized, factual, and calm. In {display}, a good report preserves knowledge for the next shift instead of leaving the problem to memory.",
        ]
    if class_number == 5:
        return [
            f"A troubleshooting checklist is attached to a machine after a recurring problem interrupts {process_a}. The checklist starts with simple confirmations: Is the area safe? Is the information complete? Is {term_a} in the expected condition? Has {term_b} been verified?",
            f"The next block focuses on the process itself. The technician must compare the current behavior with the normal sequence, identify which step failed, and note whether the symptom appears every time or only under certain conditions.",
            f"One apprentice wants to skip directly to replacement, but the instructor points at the checklist and says that each question exists for a reason. A missing answer today can become a repeated failure tomorrow.",
            f"The class relates the checklist to {system}. Inside that system, one overlooked clue can hide the real cause. Ordered questions protect the diagnosis from emotion, rush, and guesswork.",
            f"Students then add decision lines: if the symptom repeats, the team should isolate the stage; if the symptom disappears, the technician should inspect recent changes before restarting the full task.",
            f"By the end of the lesson, the checklist looks modest but powerful. It transforms troubleshooting into a sequence of justified decisions instead of a collection of improvised reactions.",
        ]
    if class_number == 6:
        return [
            f"A safety bulletin posted at the entrance of the {specialty['workplace']} reviews precautions required before {process_a}. The document does not begin with the tool or the machine. It begins with people, because safe work starts with the technician's decisions.",
            f"The first part reminds staff to inspect the area, secure loose materials, and confirm that {term_a} and {term_b} are ready for correct use. Only after that can the technical steps begin.",
            f"The second part explains a recent near miss. A worker hurried into the task, skipped a check, and had to stop the process when a reading on {term_c} suggested that the setup was incomplete. No one was hurt, but the message was clear.",
            f"The bulletin also mentions {system}. Safety is not separate from technical quality; it is built into the system itself. If the safety routine fails, the technical routine becomes unreliable as well.",
            f"During discussion, students practice short recommendations in English: technicians must verify, should isolate, and must not continue if a warning sign appears. Those structures sound simple, but they carry real responsibility.",
            f"The reading closes with a sentence every trainee can remember: the best procedure is the one that can be completed safely, explained clearly, and repeated without unnecessary risk.",
        ]
    if class_number == 7:
        return [
            f"The team must choose one procedure from the monthly workload to explain orally. Several options are available: {process_a}, {process_b}, and other routine tasks from {display}. The goal is not to pick the easiest procedure, but the one that best shows sequence, purpose, and safety.",
            f"One student prefers a familiar task because it is easier to describe. Another prefers a more complex procedure because it includes better technical vocabulary such as {term_a} and {term_b}. The supervisor asks both students to justify their choice.",
            f"In the discussion, the class identifies three criteria: relevance to real work, clarity of steps, and opportunity to explain technical decisions. A strong procedure should let the speaker show more than a list of commands.",
            f"The comparison also includes {system}. Some procedures belong to a wider workflow and allow the speaker to connect one action with a larger technical purpose. Those are often better choices for oral explanation.",
            f"Students write short justifications in English using expressions like 'I chose this procedure because...' and 'This option is more useful since...'. Their reasoning becomes part of the professional task.",
            f"By the end of the reading, the class understands that choosing a procedure is already a technical decision. A good choice makes the later explanation clearer, more authentic, and more convincing.",
        ]
    if class_number == 8:
        return [
            f"A trainee drafts a procedure script for {process_a} before the oral presentation. The script is not a full paragraph to memorize. It is a structured guide with an opening, a logical sequence, and a final explanation of why the task matters.",
            f"In the opening section, the trainee names the purpose of the procedure and the materials required. In the middle section, the script moves through the key stages, including checks related to {term_a}, {term_b}, and {term_c}.",
            f"The first version is too dense, so the instructor asks for shorter sentences and clearer transitions. A good script should support speaking, not trap the speaker inside a wall of text.",
            f"The class also connects the script to {system}. When the procedure belongs to a wider system, the conclusion should show the expected result and how the task supports quality or safety in the full workflow.",
            f"Students then highlight purpose clauses such as 'to verify,' 'to prevent,' and 'in order to confirm.' Those phrases help the speaker explain not only what happens, but why each action exists.",
            f"The final script looks smaller than the first draft, but it communicates more. In technical English, clarity is stronger than quantity when the goal is oral explanation.",
        ]
    if class_number == 9:
        return [
            f"On rehearsal day, students stand beside their notes and practice key terms before explaining {process_a}. The instructor does not start with grammar. Instead, the first focus is pronunciation, because unclear terminology can confuse the whole explanation.",
            f"A pronunciation sheet groups difficult words such as {term_a}, {term_b}, and {term_c}. Students mark stressed syllables, repeat the words in short phrases, and connect them with the exact step where each term appears.",
            f"One problem appears immediately: some students know the word on paper but cannot say it naturally while describing the procedure. The rehearsal helps them bridge that gap before the final performance.",
            f"The vocabulary sheet also refers to {system} so that the terms are not learned in isolation. Each word belongs to an action, a part, or a decision inside a real technical context.",
            f"Pairs then test each other. One student says the term, the other explains its role in the procedure. If the explanation sounds vague, both students review the sentence again until the meaning is precise.",
            f"By the end of the activity, pronunciation is no longer a separate drill. It becomes part of professional credibility: if the term is clear, the procedure sounds more confident and more teachable.",
        ]
    if class_number == 10:
        return [
            f"Two classmates meet after lunch to practice an oral explanation of {process_a}. One student presents the sequence while the other listens with a feedback card that checks structure, signposting, and technical clarity.",
            f"During the first attempt, the speaker uses correct vocabulary but jumps too quickly between stages. The listener writes that the explanation should pause after the introduction and should mark transitions more clearly before mentioning {term_a} and {term_b}.",
            f"On the second attempt, the speaker improves by adding verbal signals such as 'first,' 'now,' and 'the final step is...'. The procedure sounds easier to follow because the audience can anticipate the structure.",
            f"The pair also discusses {system}. Good signposting matters because technical procedures often belong to a larger workflow, and the audience needs to see where each action fits.",
            f"When roles change, the second student receives similar feedback about pace, eye contact, and the explanation of {term_c}. Peer practice reveals problems early, while there is still time to improve them.",
            f"At the end of the session, both students agree on one point: fluency is not speaking fast. Fluency in technical English means guiding the listener through a process with confidence and order.",
        ]
    if class_number == 11:
        return [
            f"Evaluation day begins quietly in the {specialty['workplace']} classroom. Each student has chosen a real procedure, organized the sequence, and prepared explanations for the technical decisions behind {process_a} or a related task.",
            f"When the first speaker begins, the audience hears a clear introduction, careful use of {term_a}, and a sequence that moves from preparation to execution without confusion. The strongest presentations do not sound memorized; they sound understood.",
            f"One student pauses to explain why a verification step matters before moving to {term_b}. That brief explanation improves the whole performance because it shows purpose, not just repetition.",
            f"The rubric also values connection with {system}. A procedure is stronger when the student shows how one task influences the larger technical process, the final quality, or workplace safety.",
            f"After each turn, the teacher asks one or two follow-up questions. The answers reveal whether the speaker truly controls the procedure or only remembers isolated lines from the script.",
            f"By the last presentation, the class can hear a real difference between practice and performance. Technical English becomes meaningful when students use it to explain work clearly to another person.",
        ]
    return [
        f"Near the end of the unit, students begin selecting a topic for the final project defense. Each topic must connect with real work in {display}, so the first ideas come from procedures and documents they already know well, such as {process_a} and {process_b}.",
        f"The instructor asks every student to propose a problem, a purpose, and a practical outcome. A weak topic is too broad or too vague. A stronger topic uses a real process, includes evidence, and makes room for vocabulary such as {term_a}, {term_b}, and {term_c}.",
        f"One student wants to focus on efficiency, another on safety, and another on the quality of final results. The discussion shows that a project topic is not only interesting when it sounds modern; it is valuable when it can be defended with clear technical reasons.",
        f"The class also revisits {system} to see which wider workflow or challenge supports each idea. A topic becomes stronger when it belongs to a recognizable technical context instead of floating without connection.",
        f"Students write short proposal sentences and explain why their topic matters for training or real workplace performance. The language of proposal prepares them for the more formal defense that will come later.",
        f"The reading ends with a practical insight: choosing a topic is already part of professional communication. A good project starts with a question that is concrete, relevant, and defensible in English.",
    ]


def make_text(specialty, unit_number, class_number, class_title, grammar_focus, vocab_terms):
    if unit_number == 3:
        return make_u3_text(specialty, class_number, class_title, grammar_focus, vocab_terms)

    unit = UNIT_PLANS[unit_number]
    process_a = specialty["processes"][(class_number - 1) % len(specialty["processes"])]
    process_b = specialty["processes"][class_number % len(specialty["processes"])]
    system = specialty["systems"][(unit_number + class_number - 2) % len(specialty["systems"])]
    vocab_list = ", ".join(term[0] for term in vocab_terms)
    automotriz_note = " In this specialty, the text also emphasizes professional customer service, because the student must explain diagnosis and work clearly to a client." if specialty["name"] == "Mecanica Automotriz" else ""
    return [
        f"{specialty['student']} is a 4th year student in {specialty['display']}. The lesson '{class_title}' belongs to Unit {unit_number}, '{unit['title']}', and connects English with employability, technical reading, and real transition to work or further training. This text is written as an adapted workplace document for a TP student preparing for graduation.",
        f"The interdisciplinary TP plan says that English in 4to Medio must support employability and technical comprehension in {specialty['display']}. For this specialty, the main technical source focus is {specialty['source_focus']}. Therefore, reading, speaking, and writing activities must use information that sounds useful in the {specialty['workplace']} and not only in a general English classroom.{automotriz_note}",
        f"The vocabulary from this text includes these ten terms: {vocab_list}. Students should not memorize the words as isolated items. They should connect each term with a job task, a document, a safety decision, a procedure, a customer interaction, or a project defense in English.",
        f"One process connected to this lesson is {process_a}. Another related process is {process_b}. In both cases, the student needs to identify the purpose, the required materials or information, the safety precautions, and the expected result before explaining the process orally or answering reading questions.",
        f"This class also connects with {system}. The language focus is {grammar_focus}, because students need grammar that helps them describe responsibilities, interpret instructions, justify decisions, and communicate professionally. If the grammar is used with technical content, it becomes a tool for workplace communication instead of a separate rule.",
        f"The final product of the unit is {unit['product']}. The expected evidence in the TP plan includes {specialty['evidence']} and {specialty['reading_assessment']}. In social terms, {specialty['society']}. For that reason, English supports employability, safety, technical rigor, and professional confidence."
    ]


def reading_questions(specialty, unit_number, class_title):
    return [
        f"What specialty is the text about?",
        f"What is the title of today's lesson?",
        f"Name two technical terms or processes mentioned in the text.",
        f"Why does the text connect English with employability in this specialty?",
        f"How does the text show the relationship between technical reading and professional communication?",
        f"Should TP students use English to explain real workplace procedures? Justify your answer with one idea from the text.",
    ]


def shuffled_matching_rows(vocab_terms, class_number):
    definitions = [definition for english_term, spanish_term, ipa_text, definition in vocab_terms]
    if len(definitions) > 1:
        shift = (class_number % (len(definitions) - 1)) + 1
        definitions = definitions[shift:] + definitions[:shift]
    return [
        (english_term, f"{MATCH_LABELS[index]}. {definition}")
        for index, ((english_term, spanish_term, ipa_text, _), definition) in enumerate(zip(vocab_terms, definitions))
    ]


def oral_assessment_section(unit_number, specialty):
    if unit_number == 1:
        links = '<a href="../../rubricas/cv-ingles.html">CV in English rubric</a> · <a href="../../rubricas/mock-interview.html">Mock Job Interview rubric</a>'
        task = "Prepare a CV in English oriented to a TP job and record a paired mock job interview video with at least 4 questions: 2 general and 2 technical."
    elif unit_number == 2:
        links = '<a href="../../rubricas/technical-reading.html">Technical Reading assessment reference</a>'
        task = "Complete a technical reading assessment using vocabulary, explicit information, inference, opinion, and evidence from specialty documents."
    elif unit_number == 3:
        links = '<a href="../../rubricas/procedure-oral.html">Technical Procedure Oral rubric</a>'
        task = f"Explain a technical procedure in English for 3-4 minutes. Model procedure for this specialty: {specialty['u3_model']}."
    else:
        links = '<a href="../../rubricas/advanced-reading.html">Advanced Reading reference</a> · <a href="../../rubricas/final-defense.html">Final Project Defense rubric</a>'
        task = "Complete advanced reading tasks and defend a final technical project in English using evidence, vocabulary, and professional answers."
    return f"""
  <section class=\"card\">
    <h2>🎤 Assessment Link</h2>
    <p><strong>Linked instrument:</strong> {links}</p>
    <p style=\"margin-top:8px;\"><strong>Unit task:</strong> {escape_html(task)}</p>
    <p style=\"margin-top:8px; color:#475569;\">Evidence comes from the 4to Medio TP interdisciplinary plan: employability, technical reading, oral procedure explanation, advanced reading, and final project defense.</p>
  </section>
"""


def build_class_html(specialty_slug, specialty, unit_number, class_number, class_title, grammar_focus, objective):
    vocab_terms = select_vocab(specialty, class_number)
    text_paragraphs = make_text(specialty, unit_number, class_number, class_title, grammar_focus, vocab_terms)
    text_html = "\n      ".join(f"<p>{escape_html(paragraph)}</p>" for paragraph in text_paragraphs)
    vocab_rows = "\n      ".join(
        f"<tr><td>{index + 1}</td><td><strong>{escape_html(english_term)}</strong></td><td class='ipa'>{escape_html(ipa_text)}</td><td>{escape_html(spanish_term)}</td></tr>"
        for index, (english_term, spanish_term, ipa_text, definition) in enumerate(vocab_terms)
    )
    fill_source = u3_fill_patterns(specialty, class_number, vocab_terms) if unit_number == 3 else FILL_PATTERNS[unit_number]
    fill_items = "\n      ".join(
        f"<li>{escape_html(sentence).replace('___', '<span class=\"gap\">&nbsp;___&nbsp;</span>')}</li>"
        for sentence, answer in fill_source
    )
    fill_answers = "".join(f"<li>{escape_html(answer)}</li>" for sentence, answer in fill_source)
    if unit_number == 3:
        match_source = shuffled_matching_rows(vocab_terms, class_number)
    else:
        match_source = [(english_term, definition) for english_term, spanish_term, ipa_text, definition in vocab_terms]
    match_rows = "\n      ".join(
        f"<tr><td>{index + 1}</td><td><strong>{escape_html(english_term)}</strong></td><td>{escape_html(definition)}</td></tr>"
        for index, (english_term, definition) in enumerate(match_source)
    )
    questions = u3_reading_questions(specialty, class_number, class_title, vocab_terms) if unit_number == 3 else reading_questions(specialty, unit_number, class_title)
    css_classes = ["explicit", "explicit", "explicit", "implicit", "analysis", "critical"]
    reading_blocks = []
    for index, question_text in enumerate(questions):
        reading_blocks.append(f'<div class="reading-q {css_classes[index]}"><div class="qtype">{READING_LABELS[index]}</div>{escape_html(question_text)}</div>')
    previous_number = class_number - 1 if class_number > 1 else None
    next_number = class_number + 1 if class_number < len(UNIT_PLANS[unit_number]["classes"]) else None
    color_one, color_two, color_three = specialty["colors"]
    html_output = TEMPLATE.format(
        num=class_number,
        title=escape_html(class_title),
        subtitle=escape_html(f"{specialty['course']} · {specialty['display']} · Unit {unit_number}"),
        duration="90 min",
        grammar=escape_html(grammar_focus),
        oa=escape_html("OA9/OA10/OA13/OA14 — Comprender textos tecnicos y laborales, utilizar vocabulario TP, producir respuestas escritas y orales para empleabilidad y comunicacion tecnica."),
        objective=escape_html(f"Apply technical and workplace English to {objective} in {specialty['display']}."),
        text_title=escape_html(f"{class_title} in {specialty['display']}"),
        text_html=text_html,
        vocab_rows=vocab_rows,
        fill_items=fill_items,
        fill_answers=fill_answers,
        match_rows=match_rows,
        reading_html="\n    ".join(reading_blocks),
        closure=escape_html("Exit ticket: write 3 lines that can be reused in your CV, interview, procedure explanation, reading answer, or final project defense."),
        prev_link=class_file_name(unit_number, previous_number, specialty_slug) if previous_number else "#",
        next_link=class_file_name(unit_number, next_number, specialty_slug) if next_number else "#",
        prev_class="" if previous_number else "disabled",
        next_class="" if next_number else "disabled",
    )
    html_output = html_output.replace("linear-gradient(135deg,#1e3a8a,#3730a3,#6366f1)", f"linear-gradient(135deg,{color_one},{color_two},{color_three})")
    html_output = html_output.replace("#3730a3", color_one).replace("#6366f1", color_two).replace("#e0e7ff", "#e5e7eb")
    html_output = html_output.replace(f"Unidad 1 · Clase {class_number}/12", f"Unidad {unit_number} · Clase {class_number}/12 · 4to Medio")
    html_output = html_output.replace(f"Clase {class_number} — U1 — 1ro Medio", f"Clase {class_number} — U{unit_number} — 4to Medio")
    html_output = html_output.replace("<strong>Nivel:</strong> 1ro Medio", "<strong>Nivel:</strong> 4to Medio")
    html_output = html_output.replace("1ro Medio · Unidad 1 — Discovering My Future Career", f"4to Medio · Unidad {unit_number} — {UNIT_PLANS[unit_number]['title']} · {specialty['display']}")
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
<title>4to Medio U{unit_number} — {escape_html(specialty['display'])}</title>
<style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Inter,sans-serif;background:#f8fafc;color:#0f172a;line-height:1.6}}.hero{{background:linear-gradient(135deg,{color_one},{color_two},{color_three});color:white;padding:44px 20px;text-align:center}}.hero h1{{font-size:2rem;font-weight:800}}.hero p{{margin-top:8px;opacity:.92}}main{{max-width:1000px;margin:28px auto;padding:0 16px}}table{{width:100%;border-collapse:collapse;background:white;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(15,23,42,.08)}}th{{background:{color_one};color:white;text-align:left;padding:12px}}td{{padding:12px;border-bottom:1px solid #e2e8f0}}tr:nth-child(even) td{{background:#f8fafc}}a{{color:{color_one};text-decoration:none}}a:hover{{text-decoration:underline}}.note{{background:white;border-left:5px solid {color_two};border-radius:10px;padding:14px 16px;margin-bottom:18px}}</style></head><body><div class="hero"><h1>4to Medio U{unit_number} — {escape_html(unit['title'])}</h1><p>{escape_html(specialty['course'])} · {escape_html(specialty['display'])} · 12 clases · textos de 6 párrafos</p></div><main><div class="note"><strong>Producto:</strong> {escape_html(unit['product'])}. <strong>Foco TP:</strong> {escape_html(specialty['source_focus'])}.</div><table><tr><th>#</th><th>Clase</th><th>Foco lingüístico</th></tr>{''.join(rows)}</table></main></body></html>"""


def build_specialty_index(specialty_slug, specialty):
    color_one, color_two, color_three = specialty["colors"]
    cards = []
    for unit_number, unit in UNIT_PLANS.items():
        cards.append(f"<a class='card' href='u{unit_number}/index.html'><strong>U{unit_number} · {escape_html(unit['title'])}</strong><span>{escape_html(unit['product'])}</span></a>")
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{escape_html(specialty['display'])} — 4to Medio</title><style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Inter,sans-serif;background:#f1f5f9;color:#0f172a}}.hero{{background:linear-gradient(135deg,{color_one},{color_two},{color_three});color:white;padding:48px 20px;text-align:center}}.hero h1{{font-size:2.1rem;font-weight:800}}.hero p{{margin-top:8px;opacity:.9}}main{{max-width:1000px;margin:28px auto;padding:0 16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}.card{{background:white;border-radius:12px;border-top:6px solid {color_two};padding:18px;box-shadow:0 4px 14px rgba(15,23,42,.08);text-decoration:none;color:#0f172a;display:flex;flex-direction:column;gap:8px}}.card span{{color:#64748b;font-size:.9rem}}</style></head><body><div class="hero"><h1>{escape_html(specialty['course'])} · {escape_html(specialty['display'])}</h1><p>4to Medio · 4 unidades · 48 clases · enfoque TP: {escape_html(specialty['source_focus'])}</p></div><main>{''.join(cards)}</main></body></html>"""


def build_level_index():
    cards = []
    for specialty_slug, specialty in SPECIALTIES.items():
        color_one, color_two, color_three = specialty["colors"]
        cards.append(f"<a class='card' style='border-top-color:{color_two}' href='{specialty_slug}/index.html'><strong>{escape_html(specialty['course'])} · {escape_html(specialty['display'])}</strong><span>4 unidades · 48 clases · textos de 6 párrafos</span></a>")
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>4to Medio — V2</title><style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Inter,sans-serif;background:#f1f5f9;color:#0f172a}}.hero{{background:linear-gradient(135deg,#111827,#475569,#14b8a6);color:white;padding:48px 20px;text-align:center}}.hero h1{{font-size:2.1rem;font-weight:800}}.hero p{{margin-top:8px;opacity:.9}}main{{max-width:1040px;margin:28px auto;padding:0 16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}.card{{background:white;border-radius:12px;border-top:6px solid #14b8a6;padding:18px;box-shadow:0 4px 14px rgba(15,23,42,.08);text-decoration:none;color:#0f172a;display:flex;flex-direction:column;gap:8px}}.card span{{color:#64748b;font-size:.9rem}}</style></head><body><div class="hero"><h1>4to Medio — Inglés Técnico V2</h1><p>5 especialidades · 4 unidades · 240 clases locales · sin deploy</p></div><main>{''.join(cards)}</main></body></html>"""


def rubric_page(title, subtitle, note, criteria):
    rows = "".join(f"<tr><td><strong>{escape_html(name)}</strong></td><td>{escape_html(description)}</td><td>{escape_html(points)}</td></tr>" for name, description, points in criteria)
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{escape_html(title)}</title><style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');body{{font-family:Inter,sans-serif;background:#f8fafc;color:#0f172a;line-height:1.6;margin:0}}header{{background:linear-gradient(135deg,#0f172a,#334155);color:white;padding:40px 20px;text-align:center}}main{{max-width:940px;margin:28px auto;padding:0 16px}}table{{width:100%;border-collapse:collapse;background:white;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(15,23,42,.12)}}th{{background:#0f172a;color:white;text-align:left;padding:12px}}td{{padding:12px;border-bottom:1px solid #e2e8f0}}.note{{background:white;border-left:5px solid #14b8a6;border-radius:10px;padding:14px 16px;margin-bottom:18px}}</style></head><body><header><h1>{escape_html(title)}</h1><p>{escape_html(subtitle)}</p></header><main><div class="note">{escape_html(note)}</div><table><tr><th>Criterio / Referencia</th><th>Descriptor esperado</th><th>Puntaje</th></tr>{rows}</table></main></body></html>"""


def build_rubrics():
    rubrics = {
        "cv-ingles.html": rubric_page(
            "Curriculum Vitae en Inglés",
            "4to Medio · Unidad 1 · Instrumento real CV Inglés",
            "Cada estudiante entrega un CV en inglés orientado a un puesto coherente con su especialidad TP. Secciones esperadas: Personal Info, Objective, Education, Work Experience/Internship, Skills, Languages, References.",
            [
                ("Sections & Structure", "CV with required sections in logical and professional order.", "4 pts"),
                ("Grammar & Spelling", "Correct English, careful spelling, present tense for skills and past tense for experience.", "4 pts"),
                ("Technical Vocabulary & Action Verbs", "5+ relevant technical terms and effective action verbs.", "4 pts"),
                ("Relevance & Coherence of Content", "Objective, skills, and education coherent with the TP job profile.", "4 pts"),
                ("Professional Presentation & Format", "Clean, consistent, legible, professional format.", "4 pts"),
                ("Puntualidad en la Entrega", "Submission on time according to class instructions.", "4 pts"),
            ],
        ),
        "mock-interview.html": rubric_page(
            "Mock Job Interview — Video",
            "4to Medio · Unidad 1 · Trabajo en parejas · Instrumento real Mock Interview",
            "Paired video: one interviewer and one interviewee. The interview includes at least 4 questions, 2 general and 2 technical. Approximate duration: 5 minutes. The interviewee may use the CV as support.",
            [
                ("Pronunciation & Intonation", "Clear, natural pronunciation and professional intonation.", "4 pts"),
                ("Fluency & Confidence", "Reasonable to natural flow with preparation and confidence.", "4 pts"),
                ("Use of Technical Vocabulary", "Specialty vocabulary used correctly and naturally, ideally 5+ terms.", "4 pts"),
                ("Content & Coherence of Responses", "Relevant, coherent, developed responses connected to experience and goals.", "4 pts"),
                ("Interviewer Performance", "Clear questions, follow-up comments, and credible professional tone.", "4 pts"),
                ("Video Production Quality", "Clear audio, stable image, appropriate light, and visible effort.", "4 pts"),
                ("Puntualidad en la Entrega", "Video submitted on time according to class instructions.", "4 pts"),
            ],
        ),
        "technical-reading.html": rubric_page(
            "Prueba de Comprensión Lectora Técnica",
            "4to Medio · Unidad 2 · 30 pts · 60% exigencia",
            "Assessment reference from 4to planning: 8 pts vocabulary, 10 pts explicit comprehension, and 12 pts inference/opinion based on specialty documents.",
            [
                ("Technical Vocabulary", "Recognizes and uses technical terms from the specialty text.", "8 pts"),
                ("Explicit Comprehension", "Identifies specific information, instructions, warnings, and details.", "10 pts"),
                ("Inference and Opinion", "Explains implied information and supports an opinion with evidence.", "12 pts"),
            ],
        ),
        "procedure-oral.html": rubric_page(
            "Explicación Oral de Procedimiento Técnico",
            "4to Medio · Unidad 3 · 20 pts · 5 criterios x 4 pts",
            "Students explain a technical procedure in English for 3-4 minutes. Expected structure: introduction, safety precautions, sequenced steps, and conclusion.",
            [
                ("Procedure Structure", "Clear introduction, purpose, ordered steps, and conclusion.", "4 pts"),
                ("Safety and Technical Accuracy", "Safety precautions and technical details are accurate and relevant.", "4 pts"),
                ("Technical Vocabulary", "Specialty terms are used correctly and in context.", "4 pts"),
                ("Pronunciation and Fluency", "Speech is understandable, prepared, and mostly fluent.", "4 pts"),
                ("Professional Communication", "Uses signposting, visual/keyword support, and answers brief questions clearly.", "4 pts"),
            ],
        ),
        "advanced-reading.html": rubric_page(
            "Prueba de Comprensión Lectora Avanzada",
            "4to Medio · Unidad 4 · 30 pts · 60% exigencia",
            "Assessment reference from 4to planning for advanced reading: technical vocabulary, explicit information, inference, analysis, and critical response.",
            [
                ("Vocabulary and Concepts", "Explains advanced technical terms and concepts from the text.", "8 pts"),
                ("Explicit and Inferential Reading", "Answers explicit and implicit questions with textual evidence.", "12 pts"),
                ("Analysis and Critical Response", "Evaluates a technical decision, innovation, risk, or solution with reasons.", "10 pts"),
            ],
        ),
        "final-defense.html": rubric_page(
            "Final Project Defense in English",
            "4to Medio · Unidad 4 · 20 pts · 5 criterios x 4 pts",
            "Students defend a final technical project in English. The defense presents a problem, a solution, evidence, technical vocabulary, and answers to questions.",
            [
                ("Problem and Context", "Clearly explains the technical problem and why it matters.", "4 pts"),
                ("Technical Solution", "Presents a feasible solution with accurate technical content.", "4 pts"),
                ("Evidence and Reasoning", "Uses evidence to justify decisions and expected impact.", "4 pts"),
                ("Delivery and Technical Vocabulary", "Speaks clearly and uses relevant specialty vocabulary.", "4 pts"),
                ("Questions and Professional Closure", "Answers questions and closes with a professional reflection.", "4 pts"),
            ],
        ),
    }
    for file_name, content in rubrics.items():
        (LEVEL_DIR / "rubricas" / file_name).write_text(content, encoding="utf-8")


def main():
    LEVEL_DIR.mkdir(parents=True, exist_ok=True)
    (LEVEL_DIR / "rubricas").mkdir(parents=True, exist_ok=True)
    build_rubrics()
    total_classes = 0
    for specialty_slug, specialty in SPECIALTIES.items():
        specialty_dir = LEVEL_DIR / specialty_slug
        specialty_dir.mkdir(parents=True, exist_ok=True)
        (specialty_dir / "index.html").write_text(build_specialty_index(specialty_slug, specialty), encoding="utf-8")
        for unit_number, unit in UNIT_PLANS.items():
            output_dir = specialty_dir / f"u{unit_number}"
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
