# -*- coding: utf-8 -*-
"""
3ro Medio · Unidad 1 — My Technical Skills
Genera 5 especialidades x 12 clases = 60 HTML.
Requisito nuevo: cada texto de lectura tiene exactamente 6 párrafos.
"""
from pathlib import Path
import html
import sys

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT.parent.parent / "1ro-medio" / "u1"))
from _generate_u1 import TEMPLATE  # noqa: E402

SPECIALTIES = {
    "industrial": {
        "course": "3ro A",
        "name": "Mecánica Industrial",
        "slug": "industrial",
        "color1": "#166534", "color2": "#16a34a", "color3": "#22c55e",
        "field": "industrial mechanics",
        "student": "Diego",
        "workshop": "the industrial workshop",
        "society": "factories, hospitals, mining companies, and public services depend on safe machines and precise metal parts",
        "tools": [("lathe", "torno", "/leɪð/"), ("milling machine", "fresadora", "/ˈmɪlɪŋ məˈʃiːn/"), ("caliper", "pie de metro", "/ˈkælɪpər/"), ("micrometer", "micrómetro", "/maɪˈkrɒmɪtər/"), ("wrench", "llave", "/rentʃ/"), ("drill press", "taladro de pedestal", "/drɪl pres/"), ("grinder", "esmeril", "/ˈɡraɪndər/"), ("vise", "prensa", "/vaɪs/"), ("bearing", "rodamiento", "/ˈbeərɪŋ/"), ("shaft", "eje", "/ʃæft/")],
        "processes": ["turning a metal shaft on a lathe", "checking measurements with a caliper", "preventive maintenance of rotating parts", "aligning a machine before operation", "reading a technical drawing"],
        "systems": ["rotating mechanical systems", "transmission components", "industrial maintenance routines"],
        "foci": ["precision", "preventive maintenance", "technical drawings", "metal shaping", "workshop safety"],
    },
    "automotriz": {
        "course": "3ro B",
        "name": "Mecánica Automotriz",
        "slug": "automotriz",
        "color1": "#991b1b", "color2": "#dc2626", "color3": "#f97316",
        "field": "automotive mechanics",
        "student": "Sofía",
        "workshop": "the automotive workshop",
        "society": "transport, emergency services, families, and local businesses depend on safe and reliable vehicles",
        "tools": [("scanner", "escáner automotriz", "/ˈskænər/"), ("multimeter", "multímetro", "/ˈmʌltiˌmiːtər/"), ("torque wrench", "torquímetro", "/tɔːrk rentʃ/"), ("hydraulic jack", "gato hidráulico", "/haɪˈdrɔːlɪk dʒæk/"), ("spark plug", "bujía", "/spɑːrk plʌɡ/"), ("brake pad", "pastilla de freno", "/breɪk pæd/"), ("radiator", "radiador", "/ˈreɪdieɪtər/"), ("piston", "pistón", "/ˈpɪstən/"), ("crankshaft", "cigüeñal", "/ˈkræŋkʃæft/"), ("lubrication", "lubricación", "/ˌluːbrɪˈkeɪʃən/")],
        "processes": ["diagnosing a fault with a scanner", "checking active and passive safety systems", "explaining the four-stroke engine cycle", "checking lubrication and cooling", "inspecting fixed and moving engine parts"],
        "systems": ["comfort and safety systems", "engine lubrication and cooling systems", "active and passive safety systems"],
        "foci": ["basic diagnosis", "engine parts", "four-stroke cycle", "comfort and safety", "lubrication and cooling"],
    },
    "electricidad": {
        "course": "3ro C",
        "name": "Electricidad",
        "slug": "electricidad",
        "color1": "#92400e", "color2": "#f59e0b", "color3": "#facc15",
        "field": "electricity",
        "student": "Mateo",
        "workshop": "the electrical workshop",
        "society": "homes, schools, hospitals, industry, and renewable energy projects depend on safe electrical installations",
        "tools": [("multimeter", "multímetro", "/ˈmʌltiˌmiːtər/"), ("voltage tester", "probador de voltaje", "/ˈvoʊltɪdʒ ˈtestər/"), ("circuit breaker", "disyuntor", "/ˈsɜːrkɪt ˌbreɪkər/"), ("wire stripper", "pelacables", "/ˈwaɪər ˈstrɪpər/"), ("conduit", "canalización", "/ˈkɒnduɪt/"), ("solar panel", "panel solar", "/ˈsoʊlər ˈpænəl/"), ("inverter", "inversor", "/ɪnˈvɜːrtər/"), ("grounding", "puesta a tierra", "/ˈɡraʊndɪŋ/"), ("green hydrogen", "hidrógeno verde", "/ɡriːn ˈhaɪdrədʒən/"), ("smart grid", "red inteligente", "/smɑːrt ɡrɪd/")],
        "processes": ["testing voltage before touching a circuit", "installing a basic lighting circuit", "connecting a solar panel to an inverter", "checking grounding protection", "explaining how green hydrogen can use renewable electricity"],
        "systems": ["renewable energy systems", "electrical safety systems", "green hydrogen production chains"],
        "foci": ["renewable energy", "energy transition", "green hydrogen", "safe installations", "electrical measurement"],
    },
    "grafica": {
        "course": "3ro D",
        "name": "Gráfica",
        "slug": "grafica",
        "color1": "#6b21a8", "color2": "#a855f7", "color3": "#ec4899",
        "field": "graphic production",
        "student": "Camila",
        "workshop": "the graphic production lab",
        "society": "schools, companies, public campaigns, and community projects depend on clear printed and digital communication",
        "tools": [("Fiery Command WorkStation", "Fiery Command WorkStation", "/ˈfaɪəri kəˈmænd ˈwɜːrkˌsteɪʃən/"), ("print queue", "cola de impresión", "/prɪnt kjuː/"), ("RIP", "procesador de imagen raster", "/rɪp/"), ("color profile", "perfil de color", "/ˈkʌlər ˈproʊfaɪl/"), ("calibration", "calibración", "/ˌkælɪˈbreɪʃən/"), ("proof", "prueba de impresión", "/pruːf/"), ("layout", "diagramación", "/ˈleɪaʊt/"), ("bleed", "sangrado", "/bliːd/"), ("crop mark", "marca de corte", "/krɒp mɑːrk/"), ("substrate", "sustrato", "/ˈsʌbstreɪt/")],
        "processes": ["preflighting a print file", "calibrating color before printing", "managing a print queue in Fiery", "checking bleed and crop marks", "producing a proof for client approval"],
        "systems": ["digital print workflows", "Fiery Command WorkStation", "color management systems"],
        "foci": ["Fiery Command WorkStation", "print workflow", "color accuracy", "file preparation", "client communication"],
    },
    "electronica": {
        "course": "3ro E",
        "name": "Electrónica",
        "slug": "electronica",
        "color1": "#1e40af", "color2": "#2563eb", "color3": "#06b6d4",
        "field": "electronics",
        "student": "Valentina",
        "workshop": "the electronics lab",
        "society": "smart homes, robots, medical devices, factories, and communication networks depend on electronic systems",
        "tools": [("breadboard", "protoboard", "/ˈbredbɔːrd/"), ("microcontroller", "microcontrolador", "/ˌmaɪkroʊkənˈtroʊlər/"), ("sensor", "sensor", "/ˈsensər/"), ("actuator", "actuador", "/ˈæktʃueɪtər/"), ("soldering iron", "cautín", "/ˈsɒldərɪŋ ˈaɪərn/"), ("oscilloscope", "osciloscopio", "/əˈsɪləskoʊp/"), ("resistor", "resistencia", "/rɪˈzɪstər/"), ("capacitor", "condensador", "/kəˈpæsɪtər/"), ("relay", "relé", "/ˈriːleɪ/"), ("automation", "automatización", "/ˌɔːtəˈmeɪʃən/")],
        "processes": ["building a digital circuit on a breadboard", "reading sensor data with a microcontroller", "controlling an actuator", "checking signals with an oscilloscope", "explaining a smart home case study"],
        "systems": ["digital electronics", "home automation", "mechatronics and robotics systems"],
        "foci": ["digital components", "home automation", "automation", "mechatronics", "robotics case studies"],
    },
}

CLASS_PLAN = [
    (1, "My Technical Identity", "Present Simple + technical identity", "presentar la especialidad y explicar identidad técnica inicial"),
    (2, "Tools and Equipment I Can Use", "Can / know how to", "describir herramientas y equipos que el estudiante sabe usar"),
    (3, "Safety and Professional Responsibility", "Have to / must / should", "explicar normas de seguridad y responsabilidad profesional"),
    (4, "Reading Technical Instructions", "Imperatives + sequence connectors", "comprender instrucciones técnicas y pasos de trabajo"),
    (5, "Systems I Understand", "There is / there are + present simple", "describir sistemas o procesos propios de la especialidad"),
    (6, "Basic Diagnosis and Problem Solving", "Present Simple questions + because/so", "explicar diagnóstico básico de fallas o problemas técnicos"),
    (7, "Why My Specialty Matters", "Because / so / therefore", "argumentar relevancia social de la especialidad"),
    (8, "Technical Vocabulary for Subtitles", "Noun phrases + adjective order", "preparar vocabulario técnico preciso para subtítulos en inglés"),
    (9, "Script Structure: My Technical Skills", "Paragraph connectors", "organizar guion del video en introducción, desarrollo y cierre"),
    (10, "Pronunciation and Rehearsal", "Pronunciation focus + stress", "ensayar pronunciación de vocabulario técnico con IPA"),
    (11, "Recording and English Subtitles", "Revision: accuracy and clarity", "grabar versión preliminar y revisar subtítulos en inglés"),
    (12, "Final Video: My Technical Skills", "Integrated oral performance", "entregar video final con rúbrica My Technical Skills"),
]

FILL_BY_CLASS = {
    1: [("I ___ a third-year TP student.", "am"), ("My specialty ___ important for society.", "is"), ("Technicians ___ technical problems every day.", "solve"), ("I ___ basic tools in the workshop.", "use"), ("My classmates ___ safety rules.", "follow"), ("A good technician ___ clearly.", "communicates"), ("We ___ technical vocabulary in English.", "learn"), ("This field ___ discipline and curiosity.", "requires"), ("My specialty ___ practical and useful.", "is"), ("I ___ my technical identity step by step.", "build")],
    2: [("I ___ use a multimeter safely.", "can"), ("She ___ read a simple diagram.", "can"), ("We ___ operate tools without permission.", "can't"), ("They ___ explain two processes.", "can"), ("A technician ___ identify basic parts.", "can"), ("I ___ use protective equipment.", "can"), ("He ___ repair complex systems alone yet.", "can't"), ("Students ___ learn from practice.", "can"), ("You ___ present three tools in the video.", "can"), ("My team ___ pronounce technical terms.", "can")],
    3: [("Students ___ wear PPE in the workshop.", "must"), ("A technician ___ check the area before working.", "has to"), ("We ___ ignore warning signs.", "must not"), ("Tools ___ be stored after use.", "should"), ("The teacher ___ supervise risky tasks.", "has to"), ("I ___ report unsafe conditions.", "must"), ("Workers ___ communicate clearly.", "should"), ("You ___ follow the procedure.", "must"), ("Equipment ___ be inspected regularly.", "should"), ("Safety ___ come before speed.", "must")],
    4: [("___, read the instruction sheet.", "First"), ("___, identify the tools required.", "Then"), ("___, prepare the work area.", "Next"), ("___ that, follow each step carefully.", "After"), ("___, clean the station.", "Finally"), ("The manual ___ the correct order.", "shows"), ("Students ___ follow instructions exactly.", "must"), ("A warning label ___ danger.", "indicates"), ("The process ___ be checked twice.", "should"), ("Technical English ___ help with manuals.", "can")],
    5: [("There ___ several parts in this system.", "are"), ("There ___ one main control unit.", "is"), ("The system ___ energy or information.", "transfers"), ("Components ___ together to complete a task.", "work"), ("There ___ a clear input and output.", "is"), ("A technician ___ the function of each part.", "explains"), ("There ___ safety risks in the process.", "are"), ("The diagram ___ the connections.", "shows"), ("Students ___ the system in simple English.", "describe"), ("There ___ a reason for every step.", "is")],
    6: [("What ___ the problem?", "is"), ("Why ___ the system fail?", "does"), ("The technician checks the tool ___ it may be damaged.", "because"), ("The result is wrong, ___ the measurement is repeated.", "so"), ("Does the system ___ normally?", "work"), ("Students ___ basic symptoms.", "identify"), ("A diagnosis ___ evidence.", "needs"), ("The team asks questions ___ they need details.", "because"), ("The component is replaced, ___ the test is repeated.", "so"), ("A good technician ___ before acting.", "thinks")],
    7: [("My specialty is important ___ it solves real problems.", "because"), ("Technicians protect people, ___ safety matters.", "therefore"), ("The community needs this work, ___ students train seriously.", "so"), ("I chose this field ___ I like practical work.", "because"), ("Technology changes, ___ technicians keep learning.", "therefore"), ("Good service builds trust, ___ communication is important.", "so"), ("This job supports society ___ it keeps systems working.", "because"), ("We learn English, ___ manuals are often in English.", "because"), ("A technician must be responsible, ___ mistakes can be serious.", "because"), ("This field creates opportunities, ___ it matters for young people.", "therefore")],
    8: [("I need a ___ description. (clear / technical)", "clear technical"), ("This is a ___ tool. (small / digital)", "small digital"), ("We use ___ vocabulary. (specific / technical)", "specific technical"), ("The video needs ___ subtitles. (accurate / English)", "accurate English"), ("She explains a ___ process. (basic / safe)", "basic safe"), ("The manual has ___ instructions. (short / clear)", "short clear"), ("He describes a ___ system. (modern / electrical)", "modern electrical"), ("I prepared a ___ script. (simple / organized)", "simple organized"), ("They used ___ examples. (real / workshop)", "real workshop"), ("We practiced ___ pronunciation. (careful / technical)", "careful technical")],
    9: [("My introduction ___ my name and specialty.", "includes"), ("The body ___ three tools.", "describes"), ("The conclusion ___ why the specialty matters.", "explains"), ("First, I ___ myself.", "introduce"), ("Then, I ___ my tools.", "present"), ("Next, I ___ two systems.", "explain"), ("Finally, I ___ the importance of my specialty.", "state"), ("My script ___ be 2 to 3 minutes long.", "should"), ("Subtitles ___ match my speech.", "must"), ("I ___ key words, not a full text.", "use")],
    10: [("Technical words ___ clear pronunciation.", "need"), ("The stress in 'technician' ___ on the second syllable.", "falls"), ("Students ___ record a rehearsal.", "should"), ("I ___ repeat difficult words.", "can"), ("Peer feedback ___ improve fluency.", "helps"), ("My voice ___ be clear.", "must"), ("I ___ slowly and confidently.", "speak"), ("The IPA symbol ___ guide pronunciation.", "can"), ("We ___ long pauses.", "avoid"), ("Practice ___ confidence.", "builds")],
    11: [("My video ___ include English subtitles.", "must"), ("Subtitles ___ reflect exactly what I say.", "must"), ("I ___ going to record a draft.", "am"), ("The sound ___ be clear.", "should"), ("The light ___ help the viewer.", "should"), ("I ___ check grammar before submitting.", "must"), ("My subtitles ___ technical vocabulary.", "include"), ("I ___ edit mistakes carefully.", "can"), ("The video ___ last 2 to 3 minutes.", "should"), ("I ___ ready to improve my draft.", "am")],
    12: [("The final video ___ evaluated with a rubric.", "is"), ("Each criterion ___ four points.", "has"), ("My presentation ___ include three tools.", "must"), ("I ___ explain two systems or processes.", "must"), ("I ___ justify social importance.", "must"), ("Subtitles ___ required.", "are"), ("The maximum score ___ 24 points.", "is"), ("I ___ speak for 2 to 3 minutes.", "should"), ("The teacher ___ evaluate clarity and content.", "will"), ("I ___ proud of my technical skills.", "am")],
}

READING_TYPES = {
    1: ["What specialty does the student belong to?", "What does the field require?", "What does the student build step by step?", "Why is technical identity described as a process?", "How does the text connect English with technical training?", "Should every TP student define a technical identity early? Justify."],
    2: ["Name three tools or equipment mentioned in the text.", "What can the student explain in the video?", "What should students not do without permission?", "Why is 'can' useful for presenting technical skills?", "How do tools and processes work together in this specialty?", "Is knowing how to use a tool enough to be a good technician? Justify."],
    3: ["What must students wear in the workshop?", "What should be inspected regularly?", "What comes before speed?", "Why can unsafe conditions affect the whole group?", "How does responsibility connect with professional safety?", "Should a student be evaluated on safety attitudes, not only technical results? Explain."],
    4: ["What is the first step in the process?", "What does a warning label indicate?", "What should be checked twice?", "Why does a technical manual need a clear order?", "Analyze how sequence connectors help the reader follow instructions.", "Should students use English manuals even when a Spanish version exists? Justify."],
    5: ["What does the system transfer or control?", "What does the diagram show?", "What should students describe in simple English?", "Why is there a reason for every step in a technical system?", "Explain the relationship between input, process, and output.", "Can a technician repair a system without understanding its parts? Justify."],
    6: ["What kind of questions does the technician ask?", "Why is the test repeated?", "What does a diagnosis need?", "Why should a technician think before acting?", "Analyze how evidence supports problem solving.", "Is speed or accuracy more important in technical diagnosis? Justify."],
    7: ["Why is the specialty important?", "What builds trust?", "Why do technicians keep learning?", "Why does the text connect service with community needs?", "Explain how technical work can support society beyond the workshop.", "Which TP specialty has the greatest social impact? Defend your answer respectfully."],
    8: ["What do subtitles need to be?", "What kind of vocabulary does the video require?", "What kind of examples were practiced?", "Why must subtitles match the speech exactly?", "Analyze how precise noun phrases improve technical communication.", "Should subtitles be graded as written production? Justify."],
    9: ["What does the introduction include?", "What does the body describe?", "How long should the script be?", "Why should students use key words instead of reading a full text?", "Analyze the function of introduction, body, and conclusion in a technical presentation.", "Is a good script more important than natural speaking? Justify."],
    10: ["Where does the stress fall in 'technician'?", "What should students record?", "What builds confidence?", "Why does peer feedback improve fluency?", "Analyze how IPA can support pronunciation even for beginners.", "Should pronunciation be evaluated in a technical English video? Justify."],
    11: ["What must the video include?", "How long should the video last?", "What should be checked before submitting?", "Why are sound and light part of communication?", "Analyze the connection between subtitles and oral accuracy.", "Should students be allowed to edit their videos before submission? Justify."],
    12: ["How many tools must the student include?", "How many points is the maximum score?", "What must the student justify?", "Why are subtitles required in the final video?", "Analyze how the final video combines oral, written, and technical skills.", "After this unit, what is the strongest evidence of a student's technical progress? Justify."],
}

# Extra vocabulary per class to avoid the same 10 words every time.
CLASS_EXTRA = {
    1: [("identity", "identidad", "/aɪˈdentəti/"), ("specialty", "especialidad", "/ˈspeʃəlti/"), ("role", "rol", "/roʊl/")],
    2: [("equipment", "equipo", "/ɪˈkwɪpmənt/"), ("to handle", "manejar", "/tu ˈhændəl/"), ("procedure", "procedimiento", "/prəˈsiːdʒər/")],
    3: [("PPE", "EPP", "/piː piː iː/"), ("hazard", "riesgo", "/ˈhæzərd/"), ("warning", "advertencia", "/ˈwɔːrnɪŋ/")],
    4: [("manual", "manual", "/ˈmænjuəl/"), ("instruction", "instrucción", "/ɪnˈstrʌkʃən/"), ("sequence", "secuencia", "/ˈsiːkwəns/")],
    5: [("system", "sistema", "/ˈsɪstəm/"), ("input", "entrada", "/ˈɪnpʊt/"), ("output", "salida", "/ˈaʊtpʊt/")],
    6: [("diagnosis", "diagnóstico", "/ˌdaɪəɡˈnoʊsɪs/"), ("fault", "falla", "/fɔːlt/"), ("symptom", "síntoma", "/ˈsɪmptəm/")],
    7: [("society", "sociedad", "/səˈsaɪəti/"), ("service", "servicio", "/ˈsɜːrvɪs/"), ("impact", "impacto", "/ˈɪmpækt/")],
    8: [("subtitle", "subtítulo", "/ˈsʌbˌtaɪtəl/"), ("accuracy", "precisión", "/ˈækjərəsi/"), ("phrase", "frase", "/freɪz/")],
    9: [("script", "guion", "/skrɪpt/"), ("introduction", "introducción", "/ˌɪntrəˈdʌkʃən/"), ("conclusion", "conclusión", "/kənˈkluːʒən/")],
    10: [("pronunciation", "pronunciación", "/prəˌnʌnsiˈeɪʃən/"), ("stress", "acento", "/stres/"), ("rehearsal", "ensayo", "/rɪˈhɜːrsəl/")],
    11: [("recording", "grabación", "/rɪˈkɔːrdɪŋ/"), ("draft", "borrador", "/drɑːft/"), ("editing", "edición", "/ˈedɪtɪŋ/")],
    12: [("rubric", "rúbrica", "/ˈruːbrɪk/"), ("criterion", "criterio", "/kraɪˈtɪəriən/"), ("score", "puntaje", "/skɔːr/")],
}


def e(text):
    return html.escape(str(text), quote=False)


def class_vocab(spec, class_num):
    words = CLASS_EXTRA[class_num] + spec["tools"]
    unique = []
    seen = set()
    for word in words:
        if word[0].lower() not in seen:
            unique.append(word)
            seen.add(word[0].lower())
        if len(unique) == 10:
            break
    return unique


def make_text(spec, class_num, title):
    student = spec["student"]
    name = spec["name"]
    field = spec["field"]
    workshop = spec["workshop"]
    tools = ", ".join(t[0] for t in spec["tools"][:4])
    processes = spec["processes"]
    systems = spec["systems"]
    foci = ", ".join(spec["foci"][:3])
    society = spec["society"]
    # Exactly 6 paragraphs in every class.
    return [
        f"{student} is a 3rd year student in {name}. This unit is called 'My Technical Skills' because students are preparing an individual video presentation in English. In the video, each student must describe three tools or pieces of equipment, explain two systems or processes, and justify why {field} is important for society.",
        f"The class focus today is '{title}'. In {workshop}, technical English is not decorative; it is a practical tool for understanding manuals, safety labels, diagrams, software menus, and international vocabulary. Students use English to name objects accurately and to explain what they can do with them.",
        f"For this specialty, the first technical references are {tools}. These words appear in workshop routines, teacher explanations, catalogues, short manuals, and safety instructions. When students pronounce them correctly, they sound more professional and can participate in technical conversations with more confidence.",
        f"The main processes connected to this lesson include {processes[class_num % len(processes)]} and {processes[(class_num + 1) % len(processes)]}. Students do not need to master every advanced detail yet, but they do need to explain the basic purpose, the main steps, and the safety conditions of each process in simple English.",
        f"This content also connects with the year focus for {name}: {foci}. These topics will return during the year in reading tasks, technical vocabulary work, oral activities, and written comprehension. The objective is to build a bridge between English class and real TP learning, not to study isolated words.",
        f"By the end of the lesson, students should have evidence for their final video. They should be able to say what they know, what they can do, what they still need to practice, and why their specialty matters. In social terms, {society}. That is why technical skills are also civic skills."
    ]


def reading_questions(class_num):
    qs = READING_TYPES[class_num]
    return {
        "explicit": qs[:3],
        "implicit": [qs[3]],
        "analysis": [qs[4]],
        "critical": [qs[5]],
    }


def matching_for(vocab):
    definitions = {
        "identity": "A person's sense of who they are and what role they build.",
        "specialty": "A specific technical area studied in TP education.",
        "role": "Function or responsibility someone has in a context.",
        "equipment": "Tools or machines used for a specific technical task.",
        "to handle": "To use or manage something with control and care.",
        "procedure": "A fixed series of steps for doing a task correctly.",
        "PPE": "Personal protective equipment used to reduce risk.",
        "hazard": "Something that can cause harm or damage.",
        "warning": "Message or sign that alerts people to danger.",
        "manual": "Document that explains how to use or repair something.",
        "instruction": "Direction that tells someone what to do.",
        "sequence": "Order of steps in a process.",
        "system": "Group of connected parts that work together.",
        "input": "Energy, material, or information entering a system.",
        "output": "Result produced by a system.",
        "diagnosis": "Process of identifying a problem from evidence.",
        "fault": "Problem or defect in a component or system.",
        "symptom": "Visible sign that indicates a possible problem.",
        "society": "People living together in organized communities.",
        "service": "Work done to help people or keep systems operating.",
        "impact": "Effect or influence on people or situations.",
        "subtitle": "Written text on a video that shows spoken words.",
        "accuracy": "Quality of being correct and precise.",
        "phrase": "Small group of words with meaning.",
        "script": "Written plan of what a speaker will say.",
        "introduction": "Opening part of a presentation.",
        "conclusion": "Final part that closes the presentation.",
        "pronunciation": "The way a word is spoken.",
        "stress": "Emphasis placed on a syllable in a word.",
        "rehearsal": "Practice before a final performance.",
        "recording": "Audio or video captured electronically.",
        "draft": "First version of a product before correction.",
        "editing": "Process of improving a video, text, or recording.",
        "rubric": "Evaluation document with criteria and scores.",
        "criterion": "One standard used to evaluate performance.",
        "score": "Number of points obtained in an evaluation.",
    }
    rows = []
    for en, es, ipa in vocab:
        rows.append((en, definitions.get(en, f"Technical term in the specialty related to {es}.")))
    return rows[:10]


def make_html(spec, class_num, class_title, grammar, objective, prev_num, next_num):
    vocab = class_vocab(spec, class_num)
    text = make_text(spec, class_num, class_title)
    reading = reading_questions(class_num)
    text_html = "\n      ".join(f"<p>{e(p)}</p>" for p in text)
    vocab_rows = "\n      ".join(f"<tr><td>{i+1}</td><td><strong>{e(en)}</strong></td><td class='ipa'>{e(ipa)}</td><td>{e(es)}</td></tr>" for i, (en, es, ipa) in enumerate(vocab))
    fill_items = "\n      ".join(f"<li>{e(q).replace('___', '<span class=\"gap\">&nbsp;___&nbsp;</span>')}</li>" for q, a in FILL_BY_CLASS[class_num])
    fill_answers = "".join(f"<li>{e(a)}</li>" for q, a in FILL_BY_CLASS[class_num])
    match_rows = "\n      ".join(f"<tr><td>{i+1}</td><td><strong>{e(concept)}</strong></td><td>{e(defn)}</td></tr>" for i, (concept, defn) in enumerate(matching_for(vocab)))
    rq = []
    for q in reading["explicit"]:
        rq.append(f'<div class="reading-q explicit"><div class="qtype">Explicit</div>{e(q)}</div>')
    for q in reading["implicit"]:
        rq.append(f'<div class="reading-q implicit"><div class="qtype">Implicit (inference)</div>{e(q)}</div>')
    for q in reading["analysis"]:
        rq.append(f'<div class="reading-q analysis"><div class="qtype">Analysis</div>{e(q)}</div>')
    for q in reading["critical"]:
        rq.append(f'<div class="reading-q critical"><div class="qtype">Critical thinking</div>{e(q)}</div>')
    html_out = TEMPLATE.format(
        num=class_num,
        title=e(class_title),
        subtitle=e(f"{spec['course']} · {spec['name']} · U1"),
        duration="90 min",
        grammar=e(grammar),
        oa=e("OA9/OA10/OA13 — Comprender textos técnicos adaptados, usar vocabulario de la especialidad y producir una presentación oral breve sobre habilidades técnicas."),
        objective=e(f"Aplicar inglés técnico para {objective} en {spec['name']}."),
        text_title=e(f"{class_title} in {spec['name']}"),
        text_html=text_html,
        vocab_rows=vocab_rows,
        fill_items=fill_items,
        fill_answers=fill_answers,
        match_rows=match_rows,
        reading_html="\n    ".join(rq),
        closure=e("Exit ticket: write 3 sentences that can be used later in your 'My Technical Skills' video."),
        prev_link=f"Clase_{prev_num:02d}_U1_3ro_{spec['slug']}.html" if prev_num else "#",
        next_link=f"Clase_{next_num:02d}_U1_3ro_{spec['slug']}.html" if next_num else "#",
        prev_class="" if prev_num else "disabled",
        next_class="" if next_num else "disabled",
    )
    html_out = html_out.replace("linear-gradient(135deg,#1e3a8a,#3730a3,#6366f1)", f"linear-gradient(135deg,{spec['color1']},{spec['color2']},{spec['color3']})")
    html_out = html_out.replace("#3730a3", spec["color1"]).replace("#6366f1", spec["color2"]).replace("#e0e7ff", "#e5e7eb")
    html_out = html_out.replace(f"Unidad 1 · Clase {class_num}/12", f"Unidad 1 · Clase {class_num}/12 · 3ro Medio")
    html_out = html_out.replace(f"Clase {class_num} — U1 — 1ro Medio", f"Clase {class_num} — U1 — 3ro Medio")
    html_out = html_out.replace("<strong>Nivel:</strong> 1ro Medio", "<strong>Nivel:</strong> 3ro Medio")
    html_out = html_out.replace("1ro Medio · Unidad 1 — Discovering My Future Career", f"3ro Medio · Unidad 1 — My Technical Skills · {spec['name']}")
    html_out = html_out.replace('href="../index.html">📚 Índice U1', 'href="index.html">📚 Índice U1')
    # Strengthen the required six-paragraph signal in the UI.
    html_out = html_out.replace("<h2>📖 Reading Text —", "<h2>📖 Reading Text (6 paragraphs) —")
    return html_out


def make_specialty_index(spec):
    rows = "\n".join(
        f"<tr><td>{num}</td><td><a href=\"Clase_{num:02d}_U1_3ro_{spec['slug']}.html\"><strong>{e(title)}</strong></a></td><td>{e(grammar)}</td></tr>"
        for num, title, grammar, objective in CLASS_PLAN
    )
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>3ro Medio U1 — {e(spec['name'])}</title>
<style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Inter,sans-serif;background:#f8fafc;color:#0f172a;line-height:1.6}}.hero{{background:linear-gradient(135deg,{spec['color1']},{spec['color2']},{spec['color3']});color:white;padding:44px 20px;text-align:center}}.hero h1{{font-size:2rem;font-weight:800}}.hero p{{margin-top:8px;opacity:.92}}main{{max-width:1000px;margin:28px auto;padding:0 16px}}table{{width:100%;border-collapse:collapse;background:white;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(15,23,42,.08)}}th{{background:{spec['color1']};color:white;text-align:left;padding:12px}}td{{padding:12px;border-bottom:1px solid #e2e8f0}}tr:nth-child(even) td{{background:#f8fafc}}a{{color:{spec['color1']};text-decoration:none}}a:hover{{text-decoration:underline}}.note{{background:white;border-left:5px solid {spec['color2']};border-radius:10px;padding:14px 16px;margin-bottom:18px}}</style></head><body><div class="hero"><h1>3ro Medio U1 — My Technical Skills</h1><p>{e(spec['course'])} · {e(spec['name'])} · textos de 6 párrafos · video individual con subtítulos</p></div><main><div class="note"><strong>Producto final:</strong> Video Presentation: My Technical Skills — 3 herramientas/equipos, 2 sistemas/procesos, importancia social de la especialidad, subtítulos en inglés.</div><table><tr><th>#</th><th>Clase</th><th>Foco lingüístico</th></tr>{rows}</table></main></body></html>"""


def make_level_index():
    cards = []
    for spec in SPECIALTIES.values():
        cards.append(f"<a class='card' style='border-top-color:{spec['color2']}' href='{spec['slug']}/u1/index.html'><strong>{e(spec['course'])} · {e(spec['name'])}</strong><span>Unidad 1 · 12 clases · textos de 6 párrafos</span></a>")
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>3ro Medio — V2</title><style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Inter,sans-serif;background:#f1f5f9;color:#0f172a}}.hero{{background:linear-gradient(135deg,#0f172a,#334155,#f97316);color:white;padding:48px 20px;text-align:center}}.hero h1{{font-size:2.1rem;font-weight:800}}.hero p{{margin-top:8px;opacity:.9}}main{{max-width:1040px;margin:28px auto;padding:0 16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}.card{{background:white;border-radius:12px;border-top:6px solid #f97316;padding:18px;box-shadow:0 4px 14px rgba(15,23,42,.08);text-decoration:none;color:#0f172a;display:flex;flex-direction:column;gap:8px}}.card strong{{font-size:1.05rem}}.card span{{color:#64748b;font-size:.9rem}}.card:hover{{transform:translateY(-2px);transition:.15s}}</style></head><body><div class="hero"><h1>3ro Medio — Inglés Técnico V2</h1><p>Unidad 1 disponible para las cinco especialidades · My Technical Skills</p></div><main>{''.join(cards)}</main></body></html>"""


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    for spec in SPECIALTIES.values():
        out_dir = ROOT.parent / spec["slug"] / "u1"
        out_dir.mkdir(parents=True, exist_ok=True)
        for i, (num, title, grammar, objective) in enumerate(CLASS_PLAN):
            prev_num = CLASS_PLAN[i-1][0] if i > 0 else None
            next_num = CLASS_PLAN[i+1][0] if i < len(CLASS_PLAN)-1 else None
            path = out_dir / f"Clase_{num:02d}_U1_3ro_{spec['slug']}.html"
            path.write_text(make_html(spec, num, title, grammar, objective, prev_num, next_num), encoding="utf-8")
            print(f"✓ {spec['slug']}/u1/{path.name}")
        (out_dir / "index.html").write_text(make_specialty_index(spec), encoding="utf-8")
        print(f"✓ {spec['slug']}/u1/index.html")
    (ROOT.parent / "index.html").write_text(make_level_index(), encoding="utf-8")
    print("✓ 3ro-medio/index.html")
    print("Done. 5 especialidades x 12 clases = 60 clases U1.")

if __name__ == "__main__":
    main()
