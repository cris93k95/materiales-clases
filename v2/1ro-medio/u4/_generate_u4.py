# -*- coding: utf-8 -*-
"""Generador 1ro Medio · Unidad 4 — My Plans Ahead."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "u1"))
from _generate_u1 import TEMPLATE, esc  # noqa

OUT_DIR = Path(__file__).parent

COMMON_MATCHING = [
    ("Goal", "Something you want to achieve in the future."),
    ("Plan", "A set of actions for reaching a goal."),
    ("Skill", "An ability developed through practice."),
    ("Training", "Practice and instruction for a job or task."),
    ("Opportunity", "A chance to do something useful or important."),
    ("Challenge", "A difficult task that requires effort."),
    ("Decision", "A choice made after thinking."),
    ("Internship", "Short work experience for learning."),
    ("Portfolio", "Collection of evidence of one's work."),
    ("Teamwork", "Working with others to reach a shared objective."),
]

CLASES = [
    {
        "num": 1,
        "title": "Dreams, Goals & Plans",
        "subtitle": "Starting the future unit",
        "grammar": "Future with WILL — predictions and spontaneous decisions",
        "oa": "OA10 — Comprender y producir enunciados sobre planes y predicciones futuras.",
        "objective": "Distinguir dreams, goals y plans usando will para predicciones vocacionales.",
        "text_title": "The Future Starts in 1st Medio",
        "text": [
            "In 1st Medio, many students feel that the future is far away. But every decision made today will influence tomorrow. If a student learns English, practices responsibility, and explores technical areas, they will have more options after graduation.",
            "A dream is something you imagine. A goal is something you decide to achieve. A plan is the path you will follow to reach it. For example, 'I will become an automotive technician' is a goal; 'I will practice with tools every week' is part of the plan.",
            "No one knows the future perfectly. Some students will choose a specialty and later change their minds. Others will discover a talent they did not expect. The important thing is to keep learning and to make decisions with information, not fear."
        ],
        "vocab": [("dream", "sueño", "/driːm/"), ("goal", "meta", "/ɡoʊl/"), ("plan", "plan", "/plæn/"), ("future", "futuro", "/ˈfjuːtʃər/"), ("decision", "decisión", "/dɪˈsɪʒən/"), ("graduation", "graduación", "/ˌɡrædʒuˈeɪʃən/"), ("option", "opción", "/ˈɒpʃən/"), ("path", "camino", "/pæθ/"), ("talent", "talento", "/ˈtælənt/"), ("fear", "miedo", "/fɪər/")],
        "fill_gap": [("I ___ become a responsible student.", "will"), ("My choices ___ influence my future.", "will"), ("Some students ___ change their minds.", "will"), ("We ___ have more options if we study.", "will"), ("She ___ discover a new talent.", "will"), ("They ___ make decisions with information.", "will"), ("I think English ___ help me in TP.", "will"), ("My class ___ explore five specialties.", "will"), ("He ___ practice every week.", "will"), ("The future ___ start today.", "will")],
        "reading": {
            "explicit": ["What is the difference between a dream and a goal?", "What will influence tomorrow, according to the text?", "What is one example of a plan?"],
            "implicit": ["Why should decisions be made with information, not fear?"],
            "analysis": ["Explain how learning English today can affect a student's future options."],
            "critical": ["Do you think 1st Medio is too early to think about a career? Justify."],
        },
        "closure": "Exit ticket: Write one dream, one goal, and one plan using will.",
    },
    {
        "num": 2,
        "title": "Be Going To — Real Plans",
        "subtitle": "Intentions and evidence",
        "grammar": "BE GOING TO — future intentions and planned actions",
        "oa": "OA10 — Expresar intenciones futuras usando be going to.",
        "objective": "Usar be going to para comunicar planes vocacionales concretos.",
        "text_title": "Valentina's Technical Plan",
        "text": [
            "Valentina is going to choose Electronics because she likes small devices and problem-solving. She is not going to choose a specialty only because her friends choose it. She wants to make an informed decision.",
            "Next semester, she is going to visit the electronics workshop twice. She is going to ask older students about circuits, soldering, and safety. She is also going to keep a notebook with new vocabulary in English.",
            "Her plan is simple but serious. If she practices consistently, she will feel more confident. If she asks questions, she will understand the specialty better. Valentina knows that a future career is built one step at a time."
        ],
        "vocab": [("intention", "intención", "/ɪnˈtenʃən/"), ("evidence", "evidencia", "/ˈevɪdəns/"), ("informed", "informado/a", "/ɪnˈfɔːrmd/"), ("semester", "semestre", "/sɪˈmestər/"), ("soldering", "soldadura electrónica", "/ˈsɒldərɪŋ/"), ("notebook", "cuaderno", "/ˈnoʊtbʊk/"), ("consistently", "constantemente", "/kənˈsɪstəntli/"), ("confident", "seguro/a", "/ˈkɒnfɪdənt/"), ("step", "paso", "/step/"), ("career", "carrera", "/kəˈrɪər/")],
        "fill_gap": [("Valentina ___ going to choose Electronics.", "is"), ("She ___ going to ask older students.", "is"), ("They ___ going to visit the workshop.", "are"), ("I ___ going to keep a vocabulary notebook.", "am"), ("We ___ not going to decide without information.", "are"), ("___ you going to choose Electricity?", "Are"), ("He ___ going to practice soldering.", "is"), ("My classmates ___ going to compare specialties.", "are"), ("She ___ not going to follow only her friends.", "is"), ("What ___ you going to do next semester?", "are")],
        "reading": {
            "explicit": ["What specialty is Valentina going to choose?", "How many times is she going to visit the workshop?", "What is she going to keep in English?"],
            "implicit": ["Why is Valentina not going to choose only because her friends choose it?"],
            "analysis": ["Compare 'will' and 'be going to' using examples from the text."],
            "critical": ["Should friends influence your specialty choice? Explain."],
        },
        "closure": "Exit ticket: Write 4 concrete plans using be going to.",
    },
    {
        "num": 3,
        "title": "First Conditional — If I Study, I Will…",
        "subtitle": "Consequences and choices",
        "grammar": "First Conditional — If + present simple, will + verb",
        "oa": "OA10 — Formular consecuencias futuras probables usando primer condicional.",
        "objective": "Usar primer condicional para relacionar acciones presentes con resultados futuros.",
        "text_title": "Small Actions, Big Results",
        "text": [
            "If you study technical vocabulary every week, you will understand manuals more easily. If you practice pronunciation, you will speak with more confidence in oral presentations. Small actions today can create big results tomorrow.",
            "In TP education, consequences matter. If an electrician ignores safety rules, they will put people in danger. If a mechanic checks measurements carefully, they will avoid mistakes. If a graphic designer listens to feedback, the final product will improve.",
            "The first conditional helps us talk about realistic future results. It is not fantasy; it is cause and effect. Your future will not appear by magic. If you act with discipline, your opportunities will grow."
        ],
        "vocab": [("condition", "condición", "/kənˈdɪʃən/"), ("consequence", "consecuencia", "/ˈkɒnsɪkwəns/"), ("manual", "manual", "/ˈmænjuəl/"), ("pronunciation", "pronunciación", "/prəˌnʌnsiˈeɪʃən/"), ("confidence", "confianza", "/ˈkɒnfɪdəns/"), ("safety rule", "norma de seguridad", "/ˈseɪfti ruːl/"), ("measurement", "medida", "/ˈmeʒərmənt/"), ("feedback", "retroalimentación", "/ˈfiːdbæk/"), ("discipline", "disciplina", "/ˈdɪsəplɪn/"), ("opportunity", "oportunidad", "/ˌɒpərˈtuːnəti/")],
        "fill_gap": [("If you study, you ___ understand more.", "will"), ("If she practices, she ___ improve.", "will"), ("If they ignore safety, they ___ create danger.", "will"), ("If I ask questions, I ___ learn faster.", "will"), ("If we work together, we ___ finish on time.", "will"), ("If he checks the oil, he ___ avoid problems.", "will"), ("If you listen to feedback, your product ___ improve.", "will"), ("If students read manuals, they ___ know procedures.", "will"), ("If I choose carefully, I ___ feel confident.", "will"), ("If technology changes, technicians ___ keep learning.", "will")],
        "reading": {
            "explicit": ["What will happen if you study vocabulary every week?", "What will happen if a mechanic checks measurements carefully?", "What does the first conditional help us talk about?"],
            "implicit": ["Why does the text say the future will not appear by magic?"],
            "analysis": ["Choose two conditional sentences from the text and identify the condition and the result."],
            "critical": ["Do you agree that discipline creates opportunities? Justify."],
        },
        "closure": "Exit ticket: Write 5 first conditional sentences about school and your future.",
    },
    {
        "num": 4,
        "title": "Industrial Future — Machines and Automation",
        "subtitle": "Future in Industrial Mechanics",
        "grammar": "WILL + BE GOING TO + First Conditional review",
        "oa": "OA9/OA10 — Comprender textos sobre tendencias futuras en contextos TP.",
        "objective": "Describir cambios futuros en mecánica industrial usando futuro y condicional.",
        "text_title": "Automation in the Industrial Workshop",
        "text": [
            "Industrial workshops are going to change quickly in the next decade. Many repetitive tasks will be performed by automated machines, but technicians will not disappear. They will operate, program, maintain, and repair those machines.",
            "If students learn basic robotics and English manuals, they will have better opportunities. New machines will require new skills: programming, precision, teamwork, and problem-solving. Safety will also become more important because machines will move faster and with more force.",
            "Future industrial mechanics are not going to work only with hammers and wrenches. They are going to work with sensors, CNC machines, and digital controls. The best technician will be the one who combines manual skill with technological curiosity."
        ],
        "vocab": [("automation", "automatización", "/ˌɔːtəˈmeɪʃən/"), ("robotics", "robótica", "/roʊˈbɒtɪks/"), ("repetitive", "repetitivo/a", "/rɪˈpetətɪv/"), ("to operate", "operar", "/tu ˈɒpəreɪt/"), ("to maintain", "mantener", "/tu meɪnˈteɪn/"), ("CNC machine", "máquina CNC", "/siː en siː məˈʃiːn/"), ("sensor", "sensor", "/ˈsensər/"), ("digital control", "control digital", "/ˈdɪdʒɪtəl kənˈtroʊl/"), ("manual skill", "habilidad manual", "/ˈmænjuəl skɪl/"), ("curiosity", "curiosidad", "/ˌkjʊəriˈɒsəti/")],
        "fill_gap": [("Workshops ___ going to change quickly.", "are"), ("Machines ___ perform repetitive tasks.", "will"), ("Technicians ___ not disappear.", "will"), ("If students learn robotics, they ___ have opportunities.", "will"), ("Safety ___ become more important.", "will"), ("Future mechanics ___ going to use sensors.", "are"), ("The best technician ___ combine skills.", "will"), ("If machines move faster, workers ___ need more training.", "will"), ("I ___ going to learn about automation.", "am"), ("CNC machines ___ require precision.", "will")],
        "reading": {
            "explicit": ["What tasks will automated machines perform?", "What will technicians do with those machines?", "Name two new skills mentioned in the text."],
            "implicit": ["Why will safety become more important in automated workshops?"],
            "analysis": ["Explain the phrase 'manual skill with technological curiosity'."],
            "critical": ["Will automation create more opportunities or more problems for workers? Justify."],
        },
        "closure": "Exit ticket: Write 3 predictions about future workshops using will.",
    },
    {
        "num": 5,
        "title": "Automotive Future — Electric Vehicles",
        "subtitle": "Future in Automotive Mechanics",
        "grammar": "Future forms in technical predictions",
        "oa": "OA9/OA10 — Comprender predicciones sobre tecnología automotriz futura.",
        "objective": "Expresar predicciones y planes sobre vehículos eléctricos.",
        "text_title": "The Mechanic of the Electric Car Era",
        "text": [
            "Cars are changing. In the future, many vehicles will be electric, and automotive mechanics are going to need new knowledge. They will not only repair engines; they will also diagnose batteries, motors, sensors, and software systems.",
            "If a mechanic understands electricity, they will work more safely with high-voltage components. If they learn English, they will understand international diagnostic tools and manuals. Electric vehicles are quieter and cleaner, but they are not simpler.",
            "Some students think electric cars will eliminate traditional mechanics. That is not true. The profession will evolve. Mechanics are going to combine mechanical knowledge with electronics and computer diagnostics."
        ],
        "vocab": [("electric vehicle", "vehículo eléctrico", "/ɪˈlektrɪk ˈviːəkəl/"), ("battery", "batería", "/ˈbætəri/"), ("motor", "motor eléctrico", "/ˈmoʊtər/"), ("sensor", "sensor", "/ˈsensər/"), ("software system", "sistema de software", "/ˈsɒftweər ˈsɪstəm/"), ("to diagnose", "diagnosticar", "/tu ˌdaɪəɡˈnoʊs/"), ("high-voltage", "alto voltaje", "/haɪ ˈvoʊltɪdʒ/"), ("component", "componente", "/kəmˈpoʊnənt/"), ("diagnostic tool", "herramienta de diagnóstico", "/ˌdaɪəɡˈnɒstɪk tuːl/"), ("to evolve", "evolucionar", "/tu ɪˈvɒlv/")],
        "fill_gap": [("Many vehicles ___ be electric.", "will"), ("Mechanics ___ going to need new knowledge.", "are"), ("They ___ diagnose batteries and sensors.", "will"), ("If a mechanic understands electricity, they ___ work safely.", "will"), ("Electric cars ___ not eliminate mechanics.", "will"), ("The profession ___ evolve.", "will"), ("Students ___ going to study diagnostics.", "are"), ("If they learn English, they ___ understand manuals.", "will"), ("I ___ going to compare gasoline and electric cars.", "am"), ("Mechanics ___ combine different areas.", "will")],
        "reading": {
            "explicit": ["What new parts will mechanics diagnose?", "What will happen if a mechanic understands electricity?", "What will mechanics combine in the future?"],
            "implicit": ["Why are electric vehicles 'not simpler'?"],
            "analysis": ["How does the text correct the idea that electric cars will eliminate mechanics?"],
            "critical": ["Should Chilean TP schools teach electric vehicle maintenance now? Justify."],
        },
        "closure": "Exit ticket: Write 2 predictions and 2 plans about electric vehicles.",
    },
    {
        "num": 6,
        "title": "Electricity Future — Renewable Energy",
        "subtitle": "Future in Electricity",
        "grammar": "First conditional in environmental contexts",
        "oa": "OA9/OA10 — Comprender textos sobre energía renovable y expresar consecuencias futuras.",
        "objective": "Usar futuro y primer condicional para hablar de energía renovable.",
        "text_title": "If We Invest in Renewable Energy…",
        "text": [
            "Chile has excellent conditions for renewable energy. The north has strong sunlight, and the south has strong winds. If the country invests wisely, renewable energy will create many technical jobs in the next decades.",
            "Electricians are going to install and maintain solar panels, wind turbines, and smart electrical grids. If technicians are trained well, communities will receive cleaner and safer energy. If systems are poorly installed, accidents and energy losses will increase.",
            "Renewable energy is not only about nature; it is also about technical responsibility. Future electricians will need English, safety training, and digital skills. They will help build a cleaner Chile."
        ],
        "vocab": [("renewable energy", "energía renovable", "/rɪˈnjuːəbəl ˈenərdʒi/"), ("sunlight", "luz solar", "/ˈsʌnlaɪt/"), ("wind", "viento", "/wɪnd/"), ("to invest", "invertir", "/tu ɪnˈvest/"), ("solar panel", "panel solar", "/ˈsoʊlər ˈpænəl/"), ("wind turbine", "turbina eólica", "/wɪnd ˈtɜːrbaɪn/"), ("smart grid", "red inteligente", "/smɑːrt ɡrɪd/"), ("energy loss", "pérdida de energía", "/ˈenərdʒi lɒs/"), ("community", "comunidad", "/kəˈmjuːnəti/"), ("responsibility", "responsabilidad", "/rɪˌspɒnsəˈbɪləti/")],
        "fill_gap": [("If Chile invests wisely, it ___ create jobs.", "will"), ("Electricians ___ going to install solar panels.", "are"), ("If technicians are trained well, communities ___ receive cleaner energy.", "will"), ("If systems are poorly installed, accidents ___ increase.", "will"), ("Future electricians ___ need English.", "will"), ("The north ___ continue producing solar energy.", "will"), ("I ___ going to learn about smart grids.", "am"), ("If we save energy, bills ___ go down.", "will"), ("Wind turbines ___ be important in the south.", "will"), ("Safety training ___ protect workers.", "will")],
        "reading": {
            "explicit": ["What natural conditions does Chile have for renewable energy?", "What will electricians install and maintain?", "What skills will future electricians need?"],
            "implicit": ["Why can poor installation increase accidents?"],
            "analysis": ["Explain how renewable energy is connected with technical responsibility."],
            "critical": ["Should renewable energy be a priority for Chile? Justify."],
        },
        "closure": "Exit ticket: Write 3 first conditional sentences about renewable energy.",
    },
    {
        "num": 7,
        "title": "Electronics Future — Smart Homes",
        "subtitle": "Future in Electronics",
        "grammar": "Will / be going to in smart technology contexts",
        "oa": "OA9/OA10 — Comprender textos sobre tecnología inteligente y describir planes futuros.",
        "objective": "Describir funciones de casas inteligentes usando futuro y vocabulario electrónico.",
        "text_title": "Smart Homes and the Technician of Tomorrow",
        "text": [
            "Smart homes are becoming common around the world. In the future, lights, locks, cameras, and appliances will be connected to the internet. People are going to control many devices from their phones.",
            "Electronics technicians will install sensors, configure networks, and repair smart devices. If a sensor fails, the system will send an alert. If the internet connection is weak, devices will not respond correctly.",
            "This future will create new jobs, but it will also require ethical responsibility. Technicians will have access to private information, cameras, and security systems. If they respect privacy, customers will trust them."
        ],
        "vocab": [("smart home", "casa inteligente", "/smɑːrt hoʊm/"), ("lock", "cerradura", "/lɒk/"), ("appliance", "electrodoméstico", "/əˈplaɪəns/"), ("network", "red", "/ˈnetwɜːrk/"), ("sensor", "sensor", "/ˈsensər/"), ("alert", "alerta", "/əˈlɜːrt/"), ("connection", "conexión", "/kəˈnekʃən/"), ("privacy", "privacidad", "/ˈpraɪvəsi/"), ("customer", "cliente", "/ˈkʌstəmər/"), ("trust", "confianza", "/trʌst/")],
        "fill_gap": [("Lights and locks ___ be connected.", "will"), ("People ___ going to control devices from phones.", "are"), ("Technicians ___ install sensors.", "will"), ("If a sensor fails, the system ___ send an alert.", "will"), ("If the connection is weak, devices ___ not respond.", "will"), ("Smart homes ___ create new jobs.", "will"), ("Technicians ___ have access to private information.", "will"), ("If they respect privacy, customers ___ trust them.", "will"), ("I ___ going to learn networking basics.", "am"), ("Cameras ___ require ethical responsibility.", "will")],
        "reading": {
            "explicit": ["What devices will be connected to the internet?", "What will electronics technicians install?", "What will happen if a sensor fails?"],
            "implicit": ["Why is privacy important in smart homes?"],
            "analysis": ["How does the text connect technology with ethics?"],
            "critical": ["Would you like to live in a smart home? Give one benefit and one risk."],
        },
        "closure": "Exit ticket: Write one smart-home prediction and one privacy rule.",
    },
    {
        "num": 8,
        "title": "Graphic Design Future — AI and Creativity",
        "subtitle": "Future in Graphic Design",
        "grammar": "Future predictions + opinions",
        "oa": "OA9/OA10 — Comprender textos sobre cambios tecnológicos en diseño y expresar opiniones futuras.",
        "objective": "Predecir cómo la IA afectará el diseño gráfico y justificar opiniones.",
        "text_title": "Will AI Replace Graphic Designers?",
        "text": [
            "Artificial intelligence is changing graphic design. Today, AI tools can generate images, logos, color palettes, and layouts in seconds. Some people think designers will disappear, but many professionals disagree.",
            "Graphic designers are not going to stop being important. They will guide ideas, understand clients, choose visual strategies, and correct mistakes. If designers learn to use AI ethically, they will work faster and produce more creative options.",
            "The future designer will combine creativity, communication, and technology. AI will be a tool, not a complete replacement. Human taste, cultural context, and empathy will continue to matter."
        ],
        "vocab": [("artificial intelligence", "inteligencia artificial", "/ˌɑːrtɪˈfɪʃəl ɪnˈtelɪdʒəns/"), ("layout", "diagramación", "/ˈleɪaʊt/"), ("palette", "paleta", "/ˈpælət/"), ("to replace", "reemplazar", "/tu rɪˈpleɪs/"), ("strategy", "estrategia", "/ˈstrætədʒi/"), ("ethically", "éticamente", "/ˈeθɪkəli/"), ("option", "opción", "/ˈɒpʃən/"), ("taste", "gusto", "/teɪst/"), ("context", "contexto", "/ˈkɒntekst/"), ("empathy", "empatía", "/ˈempəθi/")],
        "fill_gap": [("AI ___ change graphic design.", "will"), ("Designers ___ not disappear.", "will"), ("They ___ guide ideas and understand clients.", "will"), ("If designers use AI ethically, they ___ work faster.", "will"), ("The future designer ___ combine creativity and technology.", "will"), ("AI ___ be a tool.", "will"), ("Human taste ___ continue to matter.", "will"), ("I ___ going to learn digital design tools.", "am"), ("Clients ___ need human communication.", "will"), ("Designers ___ going to correct AI mistakes.", "are")],
        "reading": {
            "explicit": ["What can AI tools generate today?", "What will designers continue to do?", "What three human elements will continue to matter?"],
            "implicit": ["Why do many professionals disagree that designers will disappear?"],
            "analysis": ["Explain the phrase 'AI will be a tool, not a complete replacement'."],
            "critical": ["Should students learn AI design tools at school? Justify."],
        },
        "closure": "Exit ticket: Write your opinion: 'AI will / will not replace designers because…'.",
    },
    {
        "num": 9,
        "title": "Writing My Future Plan",
        "subtitle": "Paragraph workshop",
        "grammar": "Future paragraph structure — will + be going to + first conditional",
        "oa": "OA14 — Producir un texto escrito breve sobre planes vocacionales futuros.",
        "objective": "Redactar un párrafo vocacional integrando will, be going to y primer condicional.",
        "text_title": "Model Paragraph — My Future Plan",
        "text": [
            "In the future, I think I will work in a technical area connected to electricity and renewable energy. I am going to visit the electricity workshop next month because I want to understand circuits and safety rules better.",
            "If I choose Electricity, I will need discipline and patience. I will also need English because many manuals and diagrams are written in English. I am going to make a vocabulary notebook and practice pronunciation every week.",
            "My plan is not perfect yet, but it is realistic. I will compare different specialties before making my final decision. If I keep learning, I will have more opportunities and more confidence."
        ],
        "vocab": [("paragraph", "párrafo", "/ˈpærəɡrɑːf/"), ("workshop", "taller", "/ˈwɜːrkʃɒp/"), ("discipline", "disciplina", "/ˈdɪsəplɪn/"), ("patience", "paciencia", "/ˈpeɪʃəns/"), ("diagram", "diagrama", "/ˈdaɪəɡræm/"), ("realistic", "realista", "/ˌriːəˈlɪstɪk/"), ("to compare", "comparar", "/tu kəmˈpeər/"), ("final", "final", "/ˈfaɪnəl/"), ("confidence", "confianza", "/ˈkɒnfɪdəns/"), ("pronunciation", "pronunciación", "/prəˌnʌnsiˈeɪʃən/")],
        "fill_gap": [("I think I ___ work in a technical area.", "will"), ("I ___ going to visit the workshop.", "am"), ("If I choose Electricity, I ___ need discipline.", "will"), ("I ___ also need English.", "will"), ("Manuals ___ be written in English.", "will"), ("I ___ going to make a notebook.", "am"), ("I ___ compare specialties.", "will"), ("If I keep learning, I ___ have more opportunities.", "will"), ("My plan ___ realistic.", "is"), ("We ___ going to write a future paragraph.", "are")],
        "reading": {
            "explicit": ["What area is the student interested in?", "What is the student going to visit next month?", "What notebook is the student going to make?"],
            "implicit": ["Why is the student's plan described as 'not perfect yet, but realistic'?"],
            "analysis": ["Find one example of will, one of be going to, and one first conditional in the text."],
            "critical": ["Is it better to have a flexible plan or a fixed plan at 1st Medio? Justify."],
        },
        "closure": "Exit ticket: Write the first draft of your future plan paragraph (80-100 words).",
    },
    {
        "num": 10,
        "title": "Dialogue Prep — My Future Plans",
        "subtitle": "Oral interaction planning",
        "grammar": "Future questions: What will you…? / Are you going to…? / What if…?",
        "oa": "OA13 — Interactuar oralmente sobre planes y metas usando preguntas y respuestas futuras.",
        "objective": "Preparar un diálogo grupal sobre planes vocacionales futuros.",
        "text_title": "Model Dialogue — Choosing a Specialty",
        "text": [
            "A: What specialty are you going to choose? B: I am going to choose Automotive Mechanics because I like engines and electric vehicles. A: Will you work with gasoline cars or electric cars? B: I think I will work with both.",
            "C: What will you do if the specialty is difficult? B: If it is difficult, I will ask for help and practice more. D: Are you going to study English for manuals? B: Yes, I am. If I learn technical English, I will understand diagnostic tools better.",
            "A: That sounds like a good plan. B: Thanks. My plan may change, but I am going to keep exploring. I want to make a decision with information and confidence."
        ],
        "vocab": [("dialogue", "diálogo", "/ˈdaɪəlɒɡ/"), ("interaction", "interacción", "/ˌɪntərˈækʃən/"), ("question", "pregunta", "/ˈkwestʃən/"), ("answer", "respuesta", "/ˈænsər/"), ("gasoline", "gasolina", "/ˈɡæsəliːn/"), ("diagnostic", "diagnóstico", "/ˌdaɪəɡˈnɒstɪk/"), ("to explore", "explorar", "/tu ɪkˈsplɔːr/"), ("confidence", "confianza", "/ˈkɒnfɪdəns/"), ("to ask for help", "pedir ayuda", "/tu æsk fər help/"), ("to sound", "sonar / parecer", "/tu saʊnd/")],
        "fill_gap": [("What specialty ___ you going to choose?", "are"), ("I ___ going to choose Automotive Mechanics.", "am"), ("___ you work with electric cars?", "Will"), ("If it is difficult, I ___ ask for help.", "will"), ("___ you going to study English?", "Are"), ("If I learn English, I ___ understand tools better.", "will"), ("My plan ___ change.", "may"), ("We ___ going to keep exploring.", "are"), ("What ___ you do if you fail?", "will"), ("That ___ like a good plan.", "sounds")],
        "reading": {
            "explicit": ["What specialty is B going to choose?", "What will B do if the specialty is difficult?", "Why is B going to study English?"],
            "implicit": ["Why does B say 'my plan may change'?"],
            "analysis": ["Identify three different future question forms in the dialogue."],
            "critical": ["Is asking for help a sign of weakness or responsibility? Justify."],
        },
        "closure": "Exit ticket: Write 5 questions for your group dialogue.",
    },
    {
        "num": 11,
        "title": "Rehearsal — Fluency and Feedback",
        "subtitle": "Practice before final dialogue",
        "grammar": "Integrated future review + pronunciation",
        "oa": "OA13 — Ensayar producción oral y aplicar retroalimentación para mejorar fluidez.",
        "objective": "Ensayar el diálogo final y aplicar retroalimentación de pares.",
        "text_title": "How to Rehearse a Dialogue",
        "text": [
            "A good dialogue is not memorized like a robot. It is practiced until the speakers feel natural. First, each student reads their lines slowly. Then, the group checks pronunciation, especially words like career, opportunity, electricity, and technician.",
            "Next, the group rehearses without reading every word. If someone forgets a line, another classmate will help with a question. If the conversation stops, the group will use a follow-up question: 'Why?' 'What will you do next?' or 'Are you going to practice more?'",
            "Finally, the group records one rehearsal and watches it. They are going to identify one strength and one improvement. Good feedback is specific, respectful, and useful."
        ],
        "vocab": [("rehearsal", "ensayo", "/rɪˈhɜːrsəl/"), ("fluency", "fluidez", "/ˈfluːənsi/"), ("feedback", "retroalimentación", "/ˈfiːdbæk/"), ("line", "línea de diálogo", "/laɪn/"), ("natural", "natural", "/ˈnætʃərəl/"), ("to forget", "olvidar", "/tu fərˈɡet/"), ("follow-up", "seguimiento", "/ˈfɒloʊ ʌp/"), ("strength", "fortaleza", "/streŋθ/"), ("improvement", "mejora", "/ɪmˈpruːvmənt/"), ("respectful", "respetuoso/a", "/rɪˈspektfəl/")],
        "fill_gap": [("Each student ___ going to read slowly.", "is"), ("If someone forgets, a classmate ___ help.", "will"), ("The group ___ use follow-up questions.", "will"), ("They ___ going to record one rehearsal.", "are"), ("Good feedback ___ specific and respectful.", "is"), ("If the conversation stops, we ___ ask 'Why?'.", "will"), ("We ___ going to check pronunciation.", "are"), ("I ___ improve my fluency.", "will"), ("My partner ___ going to help me.", "is"), ("If we practice, we ___ feel natural.", "will")],
        "reading": {
            "explicit": ["What does each student do first?", "What should the group check after reading lines?", "What is good feedback like?"],
            "implicit": ["Why should a group record one rehearsal?"],
            "analysis": ["How do follow-up questions help a dialogue continue?"],
            "critical": ["Is memorizing every line better than speaking naturally? Justify."],
        },
        "closure": "Exit ticket: Record one rehearsal or perform it for another group. Write one strength and one improvement.",
    },
    {
        "num": 12,
        "title": "🎤 Final Dialogue — My Future Plans",
        "subtitle": "Closing evaluation for 1ro medio U4",
        "grammar": "Integrated future forms — performance",
        "oa": "OA13 — Presentar oralmente un diálogo grupal coherente sobre planes futuros.",
        "objective": "Presentar el diálogo final usando will, be going to y primer condicional en contexto vocacional.",
        "text_title": "Evaluation Day — Future Plans Dialogue",
        "text": [
            "Today, each group presents its dialogue about future plans. The conversation must include at least four questions, four answers, two examples of will, two examples of be going to, and two first conditional sentences.",
            "The teacher will evaluate four criteria: grammar accuracy, vocabulary, pronunciation/fluency, and teamwork. Each criterion has 5 points, for a total of 20 points. Students are going to listen respectfully to every group.",
            "This final dialogue closes the 1st Medio year plan. You explored specialties, described processes, learned from innovators, and now you are speaking about your own future. If you keep learning, you will build more than a grade — you will build a path."
        ],
        "vocab": [("evaluation day", "día de evaluación", "/ɪˌvæljuˈeɪʃən deɪ/"), ("criterion", "criterio", "/kraɪˈtɪəriən/"), ("accuracy", "precisión", "/ˈækjərəsi/"), ("vocabulary", "vocabulario", "/vəˈkæbjəleri/"), ("pronunciation", "pronunciación", "/prəˌnʌnsiˈeɪʃən/"), ("fluency", "fluidez", "/ˈfluːənsi/"), ("teamwork", "trabajo en equipo", "/ˈtiːmwɜːrk/"), ("respectfully", "respetuosamente", "/rɪˈspektfəli/"), ("grade", "nota", "/ɡreɪd/"), ("path", "camino", "/pæθ/")],
        "fill_gap": [("Each group ___ present its dialogue.", "will"), ("The dialogue ___ include four questions.", "must"), ("The teacher ___ evaluate four criteria.", "will"), ("Students ___ going to listen respectfully.", "are"), ("If you keep learning, you ___ build a path.", "will"), ("We ___ going to speak about our future.", "are"), ("Grammar accuracy ___ important.", "is"), ("Each criterion ___ 5 points.", "has"), ("The total score ___ 20 points.", "is"), ("This dialogue ___ close the year plan.", "will")],
        "reading": {
            "explicit": ["How many questions must the dialogue include?", "What four criteria will the teacher evaluate?", "What is the total score?"],
            "implicit": ["Why does the text say students will build 'more than a grade'?"],
            "analysis": ["How does U4 connect with the previous three units?"],
            "critical": ["After completing the year, which unit was most useful for your future? Justify."],
        },
        "closure": "Exit ticket: Self-evaluate your dialogue on a 1-20 scale and write one goal for next year.",
    },
]

# fill common fields and matching where not specified
for c in CLASES:
    c.setdefault("duration", "90 min")
    c.setdefault("matching", COMMON_MATCHING)
    if "matching" not in c or len(c["matching"]) != 10:
        c["matching"] = COMMON_MATCHING

def build_class(c, prev_num, next_num):
    text_html = "\n      ".join(f"<p>{esc(p)}</p>" for p in c["text"])
    vocab_rows = "\n      ".join(f"<tr><td>{i+1}</td><td><strong>{esc(en)}</strong></td><td class='ipa'>{esc(ipa)}</td><td>{esc(es)}</td></tr>" for i,(en,es,ipa) in enumerate(c["vocab"]))
    fill_items = "\n      ".join(f"<li>{esc(q).replace('___','<span class=\"gap\">&nbsp;___&nbsp;</span>')}</li>" for q,a in c["fill_gap"])
    fill_answers = "".join(f"<li>{esc(a)}</li>" for q,a in c["fill_gap"])
    match_rows = "\n      ".join(f"<tr><td>{i+1}</td><td><strong>{esc(concept)}</strong></td><td>{esc(defn)}</td></tr>" for i,(concept,defn) in enumerate(c["matching"]))
    rq = []
    for q in c["reading"]["explicit"]:
        rq.append(f'<div class="reading-q explicit"><div class="qtype">Explicit</div>{esc(q)}</div>')
    for q in c["reading"]["implicit"]:
        rq.append(f'<div class="reading-q implicit"><div class="qtype">Implicit (inference)</div>{esc(q)}</div>')
    for q in c["reading"]["analysis"]:
        rq.append(f'<div class="reading-q analysis"><div class="qtype">Analysis</div>{esc(q)}</div>')
    for q in c["reading"]["critical"]:
        rq.append(f'<div class="reading-q critical"><div class="qtype">Critical thinking</div>{esc(q)}</div>')
    html_out = TEMPLATE.format(
        num=c["num"], title=esc(c["title"]), subtitle=esc(c["subtitle"]), duration=esc(c["duration"]), grammar=esc(c["grammar"]),
        oa=esc(c["oa"]), objective=esc(c["objective"]), text_title=esc(c["text_title"]), text_html=text_html,
        vocab_rows=vocab_rows, fill_items=fill_items, fill_answers=fill_answers, match_rows=match_rows,
        reading_html="\n    ".join(rq), closure=esc(c["closure"]),
        prev_link=f"Clase_{prev_num:02d}_U4_1ro.html" if prev_num else "#",
        next_link=f"Clase_{next_num:02d}_U4_1ro.html" if next_num else "#",
        prev_class="" if prev_num else "disabled", next_class="" if next_num else "disabled",
    )
    html_out = html_out.replace("linear-gradient(135deg,#1e3a8a,#3730a3,#6366f1)", "linear-gradient(135deg,#0f172a,#2563eb,#14b8a6)")
    html_out = html_out.replace("#3730a3", "#2563eb").replace("#6366f1", "#14b8a6").replace("#e0e7ff", "#dbeafe")
    html_out = html_out.replace(f"Unidad 1 · Clase {c['num']}/12", f"Unidad 4 · Clase {c['num']}/12")
    html_out = html_out.replace(f"Clase {c['num']} — U1 — 1ro Medio", f"Clase {c['num']} — U4 — 1ro Medio")
    html_out = html_out.replace("1ro Medio · Unidad 1 — Discovering My Future Career", "1ro Medio · Unidad 4 — My Plans Ahead")
    html_out = html_out.replace('href="../index.html">📚 Índice U1', 'href="index.html">📚 Índice U4')
    return html_out

def build_index():
    rows = "\n      ".join(f'<tr><td>{c["num"]}</td><td><a href="Clase_{c["num"]:02d}_U4_1ro.html"><strong>{esc(c["title"])}</strong></a></td><td>{esc(c["grammar"])}</td></tr>' for c in CLASES)
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unidad 4 — 1ro Medio | My Plans Ahead</title>
<style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');*{{margin:0;padding:0;box-sizing:border-box;}}body{{font-family:'Inter',sans-serif;background:#f1f5f9;color:#0f172a;line-height:1.6;}}.hero{{background:linear-gradient(135deg,#0f172a,#2563eb,#14b8a6);color:#fff;padding:46px 24px;text-align:center;}}.hero h1{{font-size:2.2rem;font-weight:800;margin-bottom:8px;}}.hero p{{opacity:.9;}}.container{{max-width:980px;margin:30px auto;padding:0 16px;}}table{{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(15,23,42,.06);}}th{{background:#2563eb;color:#fff;padding:12px;text-align:left;}}td{{padding:12px;border-bottom:1px solid #e2e8f0;}}tr:nth-child(even) td{{background:#f8fafc;}}a{{color:#2563eb;text-decoration:none;font-weight:600;}}a:hover{{text-decoration:underline;}}.footer{{text-align:center;color:#64748b;font-size:.85rem;padding:30px 0;}}</style></head><body>
<div class="hero"><h1>Unidad 4 — My Plans Ahead</h1><p>1ro Medio · Inglés · 12 clases · will / be going to / first conditional · Producto: diálogo grupal "My Future Plans"</p></div>
<div class="container"><table><tr><th>#</th><th>Clase</th><th>Gramática</th></tr>{rows}</table></div>
<div class="footer">1ro Medio · Unidad 4 · 12 clases · 2026</div></body></html>"""

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i,c in enumerate(CLASES):
        prev_num = CLASES[i-1]["num"] if i else None
        next_num = CLASES[i+1]["num"] if i < len(CLASES)-1 else None
        (OUT_DIR / f"Clase_{c['num']:02d}_U4_1ro.html").write_text(build_class(c, prev_num, next_num), encoding="utf-8")
        print(f"✓ Clase_{c['num']:02d}_U4_1ro.html")
    (OUT_DIR / "index.html").write_text(build_index(), encoding="utf-8")
    print(f"✓ index.html\n\nDone. {len(CLASES)} clases + index → {OUT_DIR}")

if __name__ == "__main__":
    main()
