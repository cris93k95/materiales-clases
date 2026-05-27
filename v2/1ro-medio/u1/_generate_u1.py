# -*- coding: utf-8 -*-
"""
Generador de las 12 clases de Unidad 1 — 1ro Medio
"Discovering My Future Career"
Estructura mandatoria por clase:
- Texto auténtico TP
- 10 vocabulary (English + Spanish + IPA)
- 10 fill in the gap (grammar focus)
- 10 matching (concept ↔ definition)
- 6 reading comprehension (3 explicit + 1 implicit + 1 analysis + 1 critical) en inglés
"""
from pathlib import Path
import json, html, sys

OUT_DIR = Path(__file__).parent

# ============================================================
# DATA — 12 clases
# ============================================================
CLASES = [
    # ----------------------- CLASE 1 -----------------------
    {
        "num": 1,
        "title": "Who Am I as a Future Technician?",
        "subtitle": "Self-introduction & diagnostic",
        "oa": "OA9 — Demostrar comprensión de ideas generales e información explícita en textos orales y escritos breves sobre temas conocidos (intereses personales, formación TP).",
        "objective": "Identificar y usar el verbo To Be para describirse a sí mismo en contexto vocacional.",
        "duration": "90 min",
        "grammar": "To Be (am / is / are) — affirmative, negative, questions",
        "text_title": "Meet Camila — A 1st Year TP Student",
        "text": [
            "Hi! My name is Camila and I am fifteen years old. I am a student at a technical-professional high school in Chile. This year I am in 1st Medio, and I am excited because I am going to explore five different specialties: Industrial Mechanics, Automotive Mechanics, Electricity, Electronics, and Graphic Design.",
            "My classmates are very diverse. Some are interested in machines, others are good with computers, and a few are talented at drawing. We are all curious about our future careers. Our English teacher says that English is important for every technician because manuals, tools, and software are often in English.",
            "I am not sure yet which specialty I want to choose. My favorite subjects are Math and Art, so maybe Graphic Design is a good option. But I am also interested in how engines work. The choice is not easy, but it is exciting. Today, I am ready to start my journey!"
        ],
        "vocab": [
            ("specialty", "especialidad", "/ˈspeʃəlti/"),
            ("technician", "técnico/a", "/tekˈnɪʃən/"),
            ("classmate", "compañero/a de clase", "/ˈklæsˌmeɪt/"),
            ("diverse", "diverso/a", "/daɪˈvɜːrs/"),
            ("curious", "curioso/a", "/ˈkjʊəriəs/"),
            ("manual", "manual (instructivo)", "/ˈmænjuəl/"),
            ("tool", "herramienta", "/tuːl/"),
            ("software", "programa informático", "/ˈsɒftweər/"),
            ("choice", "elección", "/tʃɔɪs/"),
            ("journey", "trayecto, recorrido", "/ˈdʒɜːrni/"),
        ],
        "fill_gap": [
            ("Camila ___ fifteen years old.", "is"),
            ("My classmates ___ very diverse.", "are"),
            ("I ___ not sure about my specialty yet.", "am"),
            ("English ___ important for every technician.", "is"),
            ("___ you a 1st Medio student?", "Are"),
            ("We ___ ready to start.", "are"),
            ("My teacher ___ from Santiago.", "is"),
            ("___ Camila interested in Graphic Design?", "Is"),
            ("They ___ not in the workshop today.", "are"),
            ("I ___ excited about English class.", "am"),
        ],
        "matching": [
            ("Specialty", "A technical area of study, like Electricity or Electronics."),
            ("Technician", "A person trained to do practical technical work."),
            ("Classmate", "Another student in the same class as you."),
            ("Manual", "A book with instructions on how to use something."),
            ("Tool", "An object used to do work, like a screwdriver."),
            ("Workshop", "A room with tools where students practice."),
            ("Software", "Computer programs and applications."),
            ("Curious", "Wanting to know or learn something new."),
            ("Choice", "The act of deciding between two or more options."),
            ("Journey", "A long process or experience of change."),
        ],
        "reading": {
            "explicit": [
                "How old is Camila?",
                "How many specialties will Camila explore this year?",
                "What are Camila's favorite subjects?",
            ],
            "implicit": [
                "Why does the English teacher think English is useful for technicians?",
            ],
            "analysis": [
                "Why is the author's choice of specialty 'not easy but exciting'? Explain in your own words.",
            ],
            "critical": [
                "Do you agree that English is important for every technician? Justify your answer with at least one example.",
            ],
        },
        "closure": "Exit ticket: Write 3 sentences about yourself using 'To Be'. Example: 'I am 15. I am a 1st Medio student. I am interested in…'.",
    },
    # ----------------------- CLASE 2 -----------------------
    {
        "num": 2,
        "title": "Industrial Mechanics — Tools & Tasks",
        "subtitle": "Specialty 1 of 5",
        "oa": "OA10 — Identificar vocabulario técnico básico y aplicar Presente Simple en descripciones de rutinas laborales.",
        "objective": "Usar Presente Simple afirmativo para describir tareas de un técnico industrial.",
        "duration": "90 min",
        "grammar": "Simple Present — affirmative (3rd person -s/-es)",
        "text_title": "A Day in an Industrial Workshop",
        "text": [
            "Daniel works in an industrial mechanics workshop. Every morning he arrives at 8:00 a.m. and puts on his safety boots, gloves, and helmet. Safety comes first in any workshop.",
            "He uses many tools: a wrench, a hammer, a drill, and a lathe. The lathe is a large machine that shapes pieces of metal. Daniel also reads technical drawings and checks measurements very carefully. Precision is essential in industrial work.",
            "After lunch, his team operates the milling machine and produces small metal parts for a local factory. They clean the machines at the end of the shift. Daniel loves his job because he creates real, useful things with his hands."
        ],
        "vocab": [
            ("workshop", "taller", "/ˈwɜːrkˌʃɒp/"),
            ("safety boots", "botas de seguridad", "/ˈseɪfti buːts/"),
            ("wrench", "llave inglesa", "/rentʃ/"),
            ("hammer", "martillo", "/ˈhæmər/"),
            ("drill", "taladro", "/drɪl/"),
            ("lathe", "torno", "/leɪð/"),
            ("milling machine", "fresadora", "/ˈmɪlɪŋ məˈʃiːn/"),
            ("measurement", "medida", "/ˈmeʒərmənt/"),
            ("precision", "precisión", "/prɪˈsɪʒən/"),
            ("shift", "turno", "/ʃɪft/"),
        ],
        "fill_gap": [
            ("Daniel ___ (work) in a workshop.", "works"),
            ("He ___ (put) on safety boots.", "puts"),
            ("The lathe ___ (shape) metal pieces.", "shapes"),
            ("Daniel ___ (read) technical drawings.", "reads"),
            ("His team ___ (operate) the milling machine.", "operates"),
            ("They ___ (clean) the machines after the shift.", "clean"),
            ("Safety ___ (come) first in any workshop.", "comes"),
            ("He ___ (check) measurements carefully.", "checks"),
            ("Daniel ___ (love) his job.", "loves"),
            ("The workshop ___ (open) at 8 a.m.", "opens"),
        ],
        "matching": [
            ("Wrench", "Tool used to turn nuts and bolts."),
            ("Hammer", "Tool used to drive nails into surfaces."),
            ("Drill", "Tool that makes holes in materials."),
            ("Lathe", "Machine that rotates and shapes metal."),
            ("Milling machine", "Machine that cuts solid materials with rotating blades."),
            ("Safety boots", "Footwear that protects the feet in a workshop."),
            ("Helmet", "Hard cover that protects the head."),
            ("Gloves", "Hand protection worn during manual work."),
            ("Shift", "A scheduled period of work."),
            ("Precision", "Exactness and accuracy in measurement."),
        ],
        "reading": {
            "explicit": [
                "What time does Daniel arrive at the workshop?",
                "Name three tools Daniel uses.",
                "What does the lathe do?",
            ],
            "implicit": [
                "Why does the text say 'safety comes first'?",
            ],
            "analysis": [
                "Explain why precision is essential in industrial mechanics.",
            ],
            "critical": [
                "Would you enjoy working in an industrial workshop? Give one reason in favor and one against.",
            ],
        },
        "closure": "Exit ticket: Write 3 sentences in Simple Present about a technician's routine. Use 3rd person -s.",
    },
    # ----------------------- CLASE 3 -----------------------
    {
        "num": 3,
        "title": "Automotive Mechanics — Under the Hood",
        "subtitle": "Specialty 2 of 5",
        "oa": "OA10 — Formular preguntas y respuestas simples sobre rutinas técnicas en Presente Simple.",
        "objective": "Producir oraciones negativas e interrogativas en Presente Simple usando do/does.",
        "duration": "90 min",
        "grammar": "Simple Present — negative & questions (do/does)",
        "text_title": "Sofía, the Future Mechanic",
        "text": [
            "Sofía wants to be an automotive mechanic. She is sixteen years old and she is fascinated by cars. But Sofía does not study only because she likes cars — she studies because she wants to understand how every part of an engine works.",
            "Does she enjoy getting dirty with engine oil? Yes, she does! In the workshop, she opens the hood and checks the battery, the spark plugs, and the engine belts. She also replaces the brake pads and rotates the tires.",
            "Sofía's father does not believe that girls can be good mechanics. But Sofía proves him wrong every day. Do her classmates respect her work? Yes, they do — because she is one of the best in her class."
        ],
        "vocab": [
            ("hood", "capó", "/hʊd/"),
            ("engine", "motor", "/ˈendʒɪn/"),
            ("battery", "batería", "/ˈbætəri/"),
            ("spark plug", "bujía", "/spɑːrk plʌɡ/"),
            ("engine belt", "correa del motor", "/ˈendʒɪn belt/"),
            ("brake pad", "pastilla de freno", "/breɪk pæd/"),
            ("tire", "neumático", "/ˈtaɪər/"),
            ("oil", "aceite", "/ɔɪl/"),
            ("mechanic", "mecánico/a", "/məˈkænɪk/"),
            ("to replace", "reemplazar", "/tu rɪˈpleɪs/"),
        ],
        "fill_gap": [
            ("Sofía ___ not study only because she likes cars.", "does"),
            ("___ she enjoy her work? Yes, she ___.", "Does / does"),
            ("Her father ___ not believe in her.", "does"),
            ("___ you change engine oil at home?", "Do"),
            ("They ___ not replace tires every month.", "do"),
            ("___ the mechanic check the battery every day?", "Does"),
            ("I ___ not understand this engine part.", "do"),
            ("___ Sofía's classmates respect her? Yes, they ___.", "Do / do"),
            ("We ___ not work on Sundays.", "do"),
            ("___ the engine make a strange noise?", "Does"),
        ],
        "matching": [
            ("Hood", "Metal cover over the engine of a car."),
            ("Battery", "Device that stores electrical energy for the car."),
            ("Spark plug", "Part that ignites the fuel in an engine."),
            ("Engine belt", "Rubber band that connects engine parts."),
            ("Brake pad", "Part that creates friction to stop the car."),
            ("Tire", "Rubber ring fitted around a wheel."),
            ("Oil", "Liquid that lubricates engine parts."),
            ("Mechanic", "A person who repairs vehicles."),
            ("To replace", "To put something new in place of something old."),
            ("To rotate", "To change the position of tires for even wear."),
        ],
        "reading": {
            "explicit": [
                "How old is Sofía?",
                "What does Sofía check under the hood?",
                "What does she replace and rotate?",
            ],
            "implicit": [
                "Why does Sofía's father probably think girls cannot be mechanics?",
            ],
            "analysis": [
                "How does Sofía respond to her father's opinion? What does her behavior show?",
            ],
            "critical": [
                "Should gender influence the choice of a technical specialty? Justify your answer.",
            ],
        },
        "closure": "Exit ticket: Write 2 questions and 2 negative sentences in Simple Present about a mechanic.",
    },
    # ----------------------- CLASE 4 -----------------------
    {
        "num": 4,
        "title": "Electricity — Powering the World",
        "subtitle": "Specialty 3 of 5",
        "oa": "OA12 — Expresar habilidades y capacidades técnicas usando el modal Can/Can't.",
        "objective": "Usar Can / Can't para describir habilidades de un/a técnico/a eléctrico/a.",
        "duration": "90 min",
        "grammar": "Modal verb CAN / CAN'T — affirmative & negative",
        "text_title": "Mateo, the Apprentice Electrician",
        "text": [
            "Mateo is an electrician apprentice. He can read electrical diagrams, he can use a multimeter, and he can install simple lighting systems. But he cannot work on high-voltage lines yet — that requires more years of training and a special license.",
            "In his second year, Mateo can identify the difference between alternating current (AC) and direct current (DC). He can also connect switches, plugs, and circuit breakers safely. Safety is critical: electricity cannot be seen, but it can be deadly.",
            "Mateo's dream is to work for a renewable energy company. He believes that everyone can contribute to a cleaner planet. With solar panels and wind turbines, technicians like him can change the world."
        ],
        "vocab": [
            ("electrician", "electricista", "/ɪˌlekˈtrɪʃən/"),
            ("diagram", "diagrama", "/ˈdaɪəɡræm/"),
            ("multimeter", "multímetro", "/ˈmʌltiˌmiːtər/"),
            ("voltage", "voltaje", "/ˈvoʊltɪdʒ/"),
            ("current", "corriente", "/ˈkɜːrənt/"),
            ("switch", "interruptor", "/swɪtʃ/"),
            ("plug", "enchufe", "/plʌɡ/"),
            ("circuit breaker", "disyuntor", "/ˈsɜːrkɪt ˌbreɪkər/"),
            ("solar panel", "panel solar", "/ˈsoʊlər ˈpænəl/"),
            ("wind turbine", "turbina eólica", "/wɪnd ˈtɜːrbaɪn/"),
        ],
        "fill_gap": [
            ("Mateo ___ read electrical diagrams.", "can"),
            ("He ___ work on high-voltage lines yet.", "cannot"),
            ("She ___ use a multimeter very well.", "can"),
            ("They ___ install solar panels without training.", "cannot"),
            ("I ___ identify AC and DC current.", "can"),
            ("We ___ ignore safety procedures.", "cannot"),
            ("Electricity ___ be deadly.", "can"),
            ("You ___ see electricity, but you ___ feel it.", "cannot / can"),
            ("My classmate ___ connect a switch safely.", "can"),
            ("A good electrician ___ work without a multimeter.", "cannot"),
        ],
        "matching": [
            ("Electrician", "A person who installs and repairs electrical systems."),
            ("Diagram", "A drawing that shows how something is connected."),
            ("Multimeter", "Device that measures voltage, current, and resistance."),
            ("Voltage", "Electrical pressure measured in volts."),
            ("Current", "The flow of electricity in a circuit."),
            ("Switch", "Device that opens or closes an electrical circuit."),
            ("Plug", "Device connected to an appliance to receive power."),
            ("Circuit breaker", "Safety device that stops the current automatically."),
            ("Solar panel", "Device that converts sunlight into electricity."),
            ("Wind turbine", "Machine that converts wind into electrical energy."),
        ],
        "reading": {
            "explicit": [
                "Name three things Mateo can do.",
                "What can Mateo NOT do yet?",
                "What is Mateo's dream job?",
            ],
            "implicit": [
                "Why is a special license needed to work on high-voltage lines?",
            ],
            "analysis": [
                "Explain why the text says 'electricity cannot be seen, but it can be deadly'.",
            ],
            "critical": [
                "Do you think every school should teach about renewable energy? Why?",
            ],
        },
        "closure": "Exit ticket: Write 3 sentences with CAN and 2 with CAN'T about your own technical skills.",
    },
    # ----------------------- CLASE 5 -----------------------
    {
        "num": 5,
        "title": "Electronics — Circuits Around Us",
        "subtitle": "Specialty 4 of 5",
        "oa": "OA12 — Formular preguntas con Can para indagar sobre habilidades técnicas.",
        "objective": "Formular preguntas con Can y dar respuestas cortas para indagar habilidades técnicas en electrónica.",
        "duration": "90 min",
        "grammar": "Can — questions & short answers (Yes, I can. / No, I can't.)",
        "text_title": "Inside a Smartphone",
        "text": [
            "Can you imagine your life without a smartphone? Inside that small device, hundreds of electronic components work together: resistors, capacitors, transistors, and a microchip that processes everything in milliseconds.",
            "An electronics technician can identify, test, and replace these components. Can they fix a broken phone screen? Yes, they can — with the right tools and steady hands. Can they solder microchips at home? Usually no, they can't, because this requires specialized equipment.",
            "The world of electronics is constantly changing. Can students learn it quickly? Yes, they can, if they are curious and patient. Every robot, drone, and electric vehicle depends on electronic technicians who understand how circuits behave."
        ],
        "vocab": [
            ("smartphone", "teléfono inteligente", "/ˈsmɑːrtfoʊn/"),
            ("resistor", "resistencia", "/rɪˈzɪstər/"),
            ("capacitor", "condensador", "/kəˈpæsɪtər/"),
            ("transistor", "transistor", "/trænˈzɪstər/"),
            ("microchip", "microchip", "/ˈmaɪkroʊtʃɪp/"),
            ("circuit", "circuito", "/ˈsɜːrkɪt/"),
            ("to solder", "soldar (electrónica)", "/tu ˈsɒldər/"),
            ("component", "componente", "/kəmˈpoʊnənt/"),
            ("device", "dispositivo", "/dɪˈvaɪs/"),
            ("drone", "dron", "/droʊn/"),
        ],
        "fill_gap": [
            ("___ you fix a smartphone? Yes, I ___.", "Can / can"),
            ("___ a technician solder a microchip at home? No, usually they ___.", "Can / can't"),
            ("___ students learn electronics quickly?", "Can"),
            ("___ this drone fly in the rain? No, it ___.", "Can / can't"),
            ("___ resistors store energy? No, they ___.", "Can / can't"),
            ("___ you identify a capacitor in this board?", "Can"),
            ("___ they replace this broken screen? Yes, they ___.", "Can / can"),
            ("___ a microchip work without electricity? No, it ___.", "Can / can't"),
            ("___ we test the circuit now?", "Can"),
            ("___ the technician read the diagram? Yes, she ___.", "Can / can"),
        ],
        "matching": [
            ("Resistor", "Component that limits the flow of electric current."),
            ("Capacitor", "Component that stores electrical energy temporarily."),
            ("Transistor", "Component that amplifies or switches signals."),
            ("Microchip", "Very small electronic device that processes data."),
            ("Circuit", "Closed loop where electricity flows."),
            ("To solder", "To join metal parts using melted material."),
            ("Component", "Each individual part of an electronic system."),
            ("Device", "A machine or piece of equipment with a function."),
            ("Drone", "Unmanned aerial vehicle controlled remotely."),
            ("Smartphone", "Portable device that combines phone and computer."),
        ],
        "reading": {
            "explicit": [
                "Name four components inside a smartphone.",
                "What can an electronics technician do?",
                "Can a technician solder microchips at home? Why or why not?",
            ],
            "implicit": [
                "Why does soldering microchips require specialized equipment?",
            ],
            "analysis": [
                "Why does the text say 'the world of electronics is constantly changing'? Give an example.",
            ],
            "critical": [
                "Which is more important for an electronics technician: speed or precision? Explain.",
            ],
        },
        "closure": "Exit ticket: Write 5 Yes/No questions with CAN about a classmate's technical abilities.",
    },
    # ----------------------- CLASE 6 -----------------------
    {
        "num": 6,
        "title": "Graphic Design — Visual Communication",
        "subtitle": "Specialty 5 of 5",
        "oa": "OA10 — Usar adjetivos descriptivos en orden correcto para describir productos gráficos.",
        "objective": "Aplicar el orden de adjetivos en inglés para describir productos de diseño gráfico.",
        "duration": "90 min",
        "grammar": "Adjective word order (opinion-size-age-color-origin-material-purpose + noun)",
        "text_title": "Camila's Graphic Design Portfolio",
        "text": [
            "Camila is a graphic design student. Her portfolio is full of beautiful, modern designs. Last week she created a large red Chilean tourism poster, a small black-and-white digital logo for a coffee shop, and a colorful printed flyer for a school event.",
            "Graphic designers use professional software like Photoshop, Illustrator, and InDesign. They combine typography, color theory, and composition to send clear visual messages. A good designer is creative, patient, and detail-oriented.",
            "Today, Camila is finishing a beautiful old vintage poster for her grandfather's bakery. She chose warm yellow tones, a classic serif font, and high-quality printing paper. Her grandfather is very proud — and so is she."
        ],
        "vocab": [
            ("portfolio", "portafolio", "/pɔːrtˈfoʊlioʊ/"),
            ("poster", "afiche / cartel", "/ˈpoʊstər/"),
            ("logo", "logo", "/ˈloʊɡoʊ/"),
            ("flyer", "volante", "/ˈflaɪər/"),
            ("typography", "tipografía", "/taɪˈpɒɡrəfi/"),
            ("composition", "composición", "/ˌkɒmpəˈzɪʃən/"),
            ("font", "fuente / tipografía", "/fɒnt/"),
            ("design", "diseño", "/dɪˈzaɪn/"),
            ("color theory", "teoría del color", "/ˈkʌlər ˈθɪəri/"),
            ("printing", "impresión", "/ˈprɪntɪŋ/"),
        ],
        "fill_gap": [
            ("Camila created a ___ poster. (large / red / Chilean)", "large red Chilean"),
            ("She designed a ___ logo. (small / black-and-white / digital)", "small black-and-white digital"),
            ("It is a ___ flyer. (colorful / printed)", "colorful printed"),
            ("He likes ___ fonts. (classic / serif)", "classic serif"),
            ("This is a ___ poster. (beautiful / old / vintage)", "beautiful old vintage"),
            ("She chose ___ tones. (warm / yellow)", "warm yellow"),
            ("They use ___ software. (professional / design)", "professional design"),
            ("It is a ___ logo. (modern / minimalist)", "modern minimalist"),
            ("That is a ___ portfolio. (huge / digital)", "huge digital"),
            ("We need ___ paper. (high-quality / printing)", "high-quality printing"),
        ],
        "matching": [
            ("Portfolio", "Collection of design works that shows skills."),
            ("Poster", "Large printed picture used to advertise."),
            ("Logo", "Symbol that represents a brand."),
            ("Flyer", "Small printed paper distributed to inform people."),
            ("Typography", "Style and appearance of printed text."),
            ("Composition", "Arrangement of visual elements in a design."),
            ("Font", "Set of letters with the same design style."),
            ("Color theory", "Study of how colors interact with each other."),
            ("Layout", "How elements are arranged on a page."),
            ("Printing", "Process of producing text or images on paper."),
        ],
        "reading": {
            "explicit": [
                "What three products did Camila create last week?",
                "Name three software programs designers use.",
                "What is Camila finishing today?",
            ],
            "implicit": [
                "Why is Camila's grandfather proud of her?",
            ],
            "analysis": [
                "Why is color theory important in graphic design?",
            ],
            "critical": [
                "In the age of AI image generators, is human graphic design still important? Why?",
            ],
        },
        "closure": "Exit ticket: Describe one product in your bag using 3 adjectives in correct order.",
    },
    # ----------------------- CLASE 7 -----------------------
    {
        "num": 7,
        "title": "Skills & Qualities of a Technician",
        "subtitle": "Cross-specialty profile",
        "oa": "OA12 — Expresar necesidad y obligación usando have to / need to.",
        "objective": "Usar have to / need to para describir requisitos profesionales en las cinco especialidades TP.",
        "duration": "90 min",
        "grammar": "Have to / Need to (obligation & necessity)",
        "text_title": "What Every Technician Needs",
        "text": [
            "Every technician needs to develop both technical and personal skills. To work in a specialty, students have to study hard, but they also need to learn how to communicate, collaborate, and solve problems.",
            "An industrial mechanic has to follow safety rules strictly. An automotive mechanic needs to read English manuals to understand new car systems. An electrician has to respect voltage regulations. An electronics technician needs to be precise with tiny components. A graphic designer has to be creative and patient.",
            "All five specialties share something important: technicians have to keep learning every year because technology never stops evolving. They also need to be honest, responsible, and respectful with their team. Real success is not only about tools — it is about character."
        ],
        "vocab": [
            ("skill", "habilidad", "/skɪl/"),
            ("quality", "cualidad", "/ˈkwɒləti/"),
            ("requirement", "requisito", "/rɪˈkwaɪərmənt/"),
            ("teamwork", "trabajo en equipo", "/ˈtiːmwɜːrk/"),
            ("responsibility", "responsabilidad", "/rɪˌspɒnsəˈbɪləti/"),
            ("honesty", "honestidad", "/ˈɒnəsti/"),
            ("communication", "comunicación", "/kəˌmjuːnɪˈkeɪʃən/"),
            ("problem-solving", "resolución de problemas", "/ˈprɒbləm ˌsɒlvɪŋ/"),
            ("respect", "respeto", "/rɪˈspekt/"),
            ("regulation", "norma / reglamento", "/ˌreɡjəˈleɪʃən/"),
        ],
        "fill_gap": [
            ("Every technician ___ develop technical skills.", "has to / needs to"),
            ("Students ___ study hard.", "have to / need to"),
            ("An electrician ___ respect voltage regulations.", "has to / needs to"),
            ("We ___ communicate clearly with our team.", "have to / need to"),
            ("You ___ learn new software every year.", "have to / need to"),
            ("She ___ follow safety rules in the workshop.", "has to / needs to"),
            ("Technicians ___ keep learning.", "have to / need to"),
            ("I ___ be patient with electronic components.", "have to / need to"),
            ("A designer ___ be creative.", "has to / needs to"),
            ("They ___ respect their teammates.", "have to / need to"),
        ],
        "matching": [
            ("Skill", "An ability acquired through practice."),
            ("Quality", "A personal characteristic, like honesty."),
            ("Requirement", "Something necessary or compulsory."),
            ("Teamwork", "Working together with others to reach a goal."),
            ("Responsibility", "The duty to take care of something."),
            ("Honesty", "The quality of being truthful."),
            ("Communication", "The act of sharing information."),
            ("Problem-solving", "The process of finding solutions."),
            ("Respect", "Treating others with consideration."),
            ("Regulation", "An official rule or law."),
        ],
        "reading": {
            "explicit": [
                "What does an automotive mechanic need to do with manuals?",
                "What does an electronics technician need to be?",
                "Name three personal qualities mentioned in the text.",
            ],
            "implicit": [
                "Why does the text say 'technology never stops evolving'?",
            ],
            "analysis": [
                "Explain the sentence: 'Real success is not only about tools — it is about character'.",
            ],
            "critical": [
                "Which is more important in a technician: technical skills or personal qualities? Justify.",
            ],
        },
        "closure": "Exit ticket: Write 3 sentences about what YOU have to do this year to be a good student.",
    },
    # ----------------------- CLASE 8 -----------------------
    {
        "num": 8,
        "title": "Why I Would Choose… — Written Draft",
        "subtitle": "Connecting ideas",
        "oa": "OA14 — Producir textos escritos breves con conectores básicos para justificar opiniones.",
        "objective": "Usar conectores (because, also, so, however) para justificar la elección de una especialidad TP.",
        "duration": "90 min",
        "grammar": "Connectors: because, also, so, however, and",
        "text_title": "Mateo's Choice",
        "text": [
            "I would choose Electricity because it combines science and practical work. Electricity is everywhere — in our homes, hospitals, and factories — so good electricians are always needed. I also enjoy mathematics, and electricity requires calculations.",
            "However, electricity is not easy. You have to be careful and follow safety rules, because mistakes can be dangerous. Also, you need to read technical English to understand modern equipment.",
            "I believe Electricity is a smart choice for me because it gives me a real profession and many job opportunities. My family supports my decision, so I feel confident. And finally, I am curious — I always want to know how things work."
        ],
        "vocab": [
            ("to choose", "elegir", "/tu tʃuːz/"),
            ("decision", "decisión", "/dɪˈsɪʒən/"),
            ("opportunity", "oportunidad", "/ˌɒpərˈtuːnəti/"),
            ("opinion", "opinión", "/əˈpɪnjən/"),
            ("reason", "razón", "/ˈriːzən/"),
            ("to support", "apoyar", "/tu səˈpɔːrt/"),
            ("confident", "seguro/a (de uno mismo)", "/ˈkɒnfɪdənt/"),
            ("career", "carrera profesional", "/kəˈrɪər/"),
            ("future", "futuro", "/ˈfjuːtʃər/"),
            ("draft", "borrador", "/drɑːft/"),
        ],
        "fill_gap": [
            ("I would choose Electricity ___ I enjoy math.", "because"),
            ("Electricity is everywhere, ___ technicians are needed.", "so"),
            ("I like the work; I ___ enjoy the technology.", "also"),
            ("Electricity is interesting, ___ it can be dangerous.", "however"),
            ("My family supports me, ___ I feel confident.", "so"),
            ("I want to study Graphic Design ___ I love art.", "because"),
            ("___, I need to practice software every day.", "However"),
            ("She is creative ___ patient.", "and"),
            ("Electronics requires precision; you ___ need patience.", "also"),
            ("Cars are complex, ___ mechanics need many skills.", "so"),
        ],
        "matching": [
            ("Because", "Conjunction used to express a reason."),
            ("So", "Conjunction used to express a result."),
            ("Also", "Adverb used to add information."),
            ("However", "Adverb used to express contrast."),
            ("And", "Conjunction used to join similar ideas."),
            ("Reason", "An explanation for an action or opinion."),
            ("Opinion", "A personal point of view."),
            ("Career", "A long-term professional path."),
            ("To support", "To help or back someone."),
            ("Confident", "Sure of oneself and one's abilities."),
        ],
        "reading": {
            "explicit": [
                "Why does Mateo choose Electricity?",
                "What does Mateo enjoy besides electrical work?",
                "Who supports Mateo's decision?",
            ],
            "implicit": [
                "Why does Mateo say electricians are 'always needed'?",
            ],
            "analysis": [
                "How does Mateo balance the positive and negative aspects of Electricity in his text?",
            ],
            "critical": [
                "Is family support important when choosing a career? Justify your answer.",
            ],
        },
        "closure": "Exit ticket: Write 4 sentences justifying YOUR specialty choice using because, also, so, and however.",
    },
    # ----------------------- CLASE 9 -----------------------
    {
        "num": 9,
        "title": "Script Writing for the Video",
        "subtitle": "Building 'My Future Career'",
        "oa": "OA14 — Organizar un guion oral breve aplicando estructuras gramaticales aprendidas.",
        "objective": "Redactar un guion (script) de 2-3 minutos para el video 'My Future Career' integrando contenidos de la unidad.",
        "duration": "90 min",
        "grammar": "Integrated review: To Be + Simple Present + Can + Have to + connectors",
        "text_title": "Model Script — My Future Career",
        "text": [
            "Hello! My name is Valentina. I am 15 years old and I am a 1st Medio student. I would choose Electronics as my future specialty because I love understanding how small devices work, like smartphones and drones.",
            "An electronics technician can identify components, can test circuits, and can solder small connections. However, you have to be very patient, because mistakes are easy to make with tiny parts. You also need to read technical English to learn from international manuals.",
            "In ten years, I want to design educational drones for Chilean schools. I am excited about my future career because it combines my passion for technology with my desire to help my community. Thank you for watching my video!"
        ],
        "vocab": [
            ("script", "guion", "/skrɪpt/"),
            ("introduction", "introducción", "/ˌɪntrəˈdʌkʃən/"),
            ("body", "desarrollo (de un texto)", "/ˈbɒdi/"),
            ("conclusion", "conclusión", "/kənˈkluːʒən/"),
            ("audience", "audiencia", "/ˈɔːdiəns/"),
            ("message", "mensaje", "/ˈmesɪdʒ/"),
            ("structure", "estructura", "/ˈstrʌktʃər/"),
            ("clarity", "claridad", "/ˈklærəti/"),
            ("passion", "pasión", "/ˈpæʃən/"),
            ("community", "comunidad", "/kəˈmjuːnəti/"),
        ],
        "fill_gap": [
            ("My name ___ Valentina.", "is"),
            ("I ___ a 1st Medio student.", "am"),
            ("I ___ choose Electronics ___ I love technology.", "would / because"),
            ("A technician ___ identify components.", "can"),
            ("You ___ be very patient.", "have to / need to"),
            ("I ___ excited about my future.", "am"),
            ("She ___ test circuits with a multimeter.", "can"),
            ("We ___ read manuals in English.", "have to / need to"),
            ("Drones ___ designed by skilled technicians.", "are"),
            ("Thank you ___ watching my video!", "for"),
        ],
        "matching": [
            ("Script", "Written text of what someone will say."),
            ("Introduction", "First part of a presentation."),
            ("Body", "Main part of a text or presentation."),
            ("Conclusion", "Final part of a presentation."),
            ("Audience", "People who watch or listen."),
            ("Message", "The main idea being communicated."),
            ("Structure", "The way parts are organized."),
            ("Clarity", "The quality of being easy to understand."),
            ("Passion", "Strong interest or enthusiasm."),
            ("Community", "A group of people living in the same area."),
        ],
        "reading": {
            "explicit": [
                "What specialty does Valentina choose?",
                "What can an electronics technician do?",
                "What does Valentina want to design in 10 years?",
            ],
            "implicit": [
                "Why does Valentina mention 'Chilean schools' in her conclusion?",
            ],
            "analysis": [
                "Identify the three parts of Valentina's script (introduction, body, conclusion). Where does each begin?",
            ],
            "critical": [
                "Why is having a clear conclusion important in a video script?",
            ],
        },
        "closure": "Exit ticket: Write the FIRST paragraph of your own 'My Future Career' script (3-4 sentences).",
    },
    # ----------------------- CLASE 10 -----------------------
    {
        "num": 10,
        "title": "Rehearsal & Peer Feedback",
        "subtitle": "Oral practice + pronunciation",
        "oa": "OA13 — Pronunciar con claridad palabras clave usando referencias fonéticas (IPA).",
        "objective": "Ensayar el guion en voz alta y dar retroalimentación a un par utilizando vocabulario fonético básico.",
        "duration": "90 min",
        "grammar": "Pronunciation focus: word stress + IPA review",
        "text_title": "How to Rehearse Like a Pro",
        "text": [
            "Rehearsing is not just reading. A good rehearsal involves three things: pronunciation, intonation, and confidence. Practice in front of a mirror, record yourself with your phone, and listen carefully to identify difficult words.",
            "Word stress is very important in English. For example, the word 'technician' is pronounced /tekˈnɪʃən/ — the stress falls on the second syllable. If you stress the wrong syllable, native speakers may not understand you.",
            "Peer feedback is also valuable. Listen to your classmate, repeat what you hear, and give kind, specific suggestions. Say 'Your introduction was clear' or 'Try to pronounce <career> as /kəˈrɪər/, not /ˈkærɪər/'. Good feedback helps everyone improve."
        ],
        "vocab": [
            ("rehearsal", "ensayo", "/rɪˈhɜːrsəl/"),
            ("pronunciation", "pronunciación", "/prəˌnʌnsiˈeɪʃən/"),
            ("intonation", "entonación", "/ˌɪntəˈneɪʃən/"),
            ("stress", "acento (énfasis)", "/stres/"),
            ("syllable", "sílaba", "/ˈsɪləbəl/"),
            ("feedback", "retroalimentación", "/ˈfiːdbæk/"),
            ("suggestion", "sugerencia", "/səˈdʒestʃən/"),
            ("mirror", "espejo", "/ˈmɪrər/"),
            ("to record", "grabar", "/tu rɪˈkɔːrd/"),
            ("clear", "claro/a", "/klɪər/"),
        ],
        "fill_gap": [
            ("A good rehearsal ___ three things.", "involves"),
            ("Word stress ___ very important.", "is"),
            ("___ you record yourself? It helps a lot.", "Can"),
            ("Native speakers ___ not understand wrong stress.", "may"),
            ("You ___ listen carefully to your classmate.", "have to / need to"),
            ("Good feedback ___ everyone improve.", "helps"),
            ("She ___ practice in front of a mirror.", "needs to / has to"),
            ("'Technician' is stressed on the ___ syllable.", "second"),
            ("Peer feedback ___ valuable.", "is"),
            ("We ___ repeat what we hear.", "can / have to"),
        ],
        "matching": [
            ("Rehearsal", "Practice before a real performance."),
            ("Pronunciation", "The way a word is said."),
            ("Intonation", "The rise and fall of the voice."),
            ("Stress", "The emphasis on a syllable."),
            ("Syllable", "A unit of pronunciation in a word."),
            ("Feedback", "Information given to improve performance."),
            ("Suggestion", "An idea or proposal for improvement."),
            ("Mirror", "Reflective surface used to see yourself."),
            ("To record", "To capture sound or video."),
            ("Clear", "Easy to see, hear, or understand."),
        ],
        "reading": {
            "explicit": [
                "Name the three elements of a good rehearsal.",
                "Where does the stress fall in 'technician'?",
                "Give one example of polite feedback from the text.",
            ],
            "implicit": [
                "Why does the text recommend recording yourself with your phone?",
            ],
            "analysis": [
                "How can wrong word stress cause misunderstanding? Explain with an example.",
            ],
            "critical": [
                "Is peer feedback more effective than teacher feedback? Justify.",
            ],
        },
        "closure": "Exit ticket: Choose 3 words from your script and write them with IPA stress marks.",
    },
    # ----------------------- CLASE 11 -----------------------
    {
        "num": 11,
        "title": "Recording Session (Work-in-Progress)",
        "subtitle": "Self-correction & final adjustments",
        "oa": "OA13 — Autoevaluar la propia producción oral y aplicar mejoras.",
        "objective": "Grabar una primera versión del video y aplicar autocorrecciones identificadas en la grabación.",
        "duration": "90 min",
        "grammar": "Self-correction language: 'I should change…', 'I need to improve…'",
        "text_title": "Five Tips for a Great Video",
        "text": [
            "First, look at the camera, not at the script. Eye contact is essential for a strong connection with your audience. If you need notes, keep them small and use them only as a reference.",
            "Second, speak slowly and clearly. Many students rush because they are nervous, but a slow rhythm helps the audience understand. Third, smile naturally — your face shows your confidence.",
            "Fourth, check your light and sound before recording. A dark video or a noisy room ruins your work. Finally, watch your recording before submitting it. Ask yourself: 'Should I change this sentence? Do I need to improve this word?' Self-correction is the secret of every good communicator."
        ],
        "vocab": [
            ("recording", "grabación", "/rɪˈkɔːrdɪŋ/"),
            ("eye contact", "contacto visual", "/aɪ ˈkɒntækt/"),
            ("rhythm", "ritmo", "/ˈrɪðəm/"),
            ("nervous", "nervioso/a", "/ˈnɜːrvəs/"),
            ("confidence", "confianza", "/ˈkɒnfɪdəns/"),
            ("light", "luz", "/laɪt/"),
            ("sound", "sonido", "/saʊnd/"),
            ("to submit", "entregar / enviar", "/tu səbˈmɪt/"),
            ("self-correction", "autocorrección", "/self kəˈrekʃən/"),
            ("communicator", "comunicador/a", "/kəˈmjuːnɪkeɪtər/"),
        ],
        "fill_gap": [
            ("___ I look at the camera or at my notes?", "Should"),
            ("I ___ to speak more slowly.", "need"),
            ("Eye contact ___ essential.", "is"),
            ("You ___ check the light before recording.", "should / have to"),
            ("Many students ___ because they are nervous.", "rush"),
            ("___ I change this sentence?", "Should"),
            ("Self-correction ___ the secret of every communicator.", "is"),
            ("I ___ improve my pronunciation of 'electrician'.", "need to / have to"),
            ("A dark video ___ your work.", "ruins"),
            ("___ we use notes? Yes, but small ones.", "Can"),
        ],
        "matching": [
            ("Recording", "An audio or video file captured electronically."),
            ("Eye contact", "Looking directly at someone's eyes."),
            ("Rhythm", "A regular pattern of sounds or movements."),
            ("Nervous", "Worried or anxious."),
            ("Confidence", "Belief in one's abilities."),
            ("Light", "Brightness needed to see something."),
            ("Sound", "Audio that we can hear."),
            ("To submit", "To deliver or hand in work."),
            ("Self-correction", "Identifying and fixing one's own mistakes."),
            ("Communicator", "A person who shares ideas effectively."),
        ],
        "reading": {
            "explicit": [
                "Where should you look while recording?",
                "Why should you speak slowly?",
                "What two technical things should you check before recording?",
            ],
            "implicit": [
                "Why does the text say 'eye contact creates a strong connection'?",
            ],
            "analysis": [
                "Why is self-correction called 'the secret of every good communicator'?",
            ],
            "critical": [
                "Which tip is the most difficult to apply for you? Why?",
            ],
        },
        "closure": "Exit ticket: After recording, write 2 sentences using 'I should…' and 'I need to…' to plan improvements.",
    },
    # ----------------------- CLASE 12 -----------------------
    {
        "num": 12,
        "title": "Final Evaluation — My Future Career Video",
        "subtitle": "Submission day (rubric: 18 points)",
        "oa": "OA13 — Producir una presentación oral coherente que integre vocabulario técnico y estructuras gramaticales de la unidad.",
        "objective": "Entregar el video final aplicando los criterios de la rúbrica 'My Future Career' (18 puntos).",
        "duration": "90 min",
        "grammar": "Integrated evaluation — all U1 grammar applied in the video.",
        "text_title": "Rubric Criteria — What I Am Evaluated On",
        "text": [
            "Today is submission day. Your video 'My Future Career' will be evaluated with the official rubric. There are six criteria, each scored from 1 to 3 points, for a maximum of 18 points.",
            "The criteria are: 1) Content & Justification — does your video clearly explain WHY you choose the specialty? 2) Vocabulary — do you use technical terms correctly? 3) Grammar — do you apply To Be, Simple Present, Can, Have to, and connectors well? 4) Pronunciation — are your key words clear and well-stressed? 5) Fluency & Pace — do you speak with natural rhythm? 6) Video Quality — is the sound, light, and visual composition acceptable?",
            "Remember: this is not just an English assignment, it is a personal reflection. Be honest, be proud, and show the world the future technician you want to become. Good luck — you can do this!"
        ],
        "vocab": [
            ("evaluation", "evaluación", "/ɪˌvæljuˈeɪʃən/"),
            ("rubric", "rúbrica", "/ˈruːbrɪk/"),
            ("criterion", "criterio", "/kraɪˈtɪəriən/"),
            ("score", "puntaje", "/skɔːr/"),
            ("submission", "entrega", "/səbˈmɪʃən/"),
            ("fluency", "fluidez", "/ˈfluːənsi/"),
            ("pace", "ritmo (velocidad)", "/peɪs/"),
            ("content", "contenido", "/ˈkɒntent/"),
            ("justification", "justificación", "/ˌdʒʌstɪfɪˈkeɪʃən/"),
            ("reflection", "reflexión", "/rɪˈflekʃən/"),
        ],
        "fill_gap": [
            ("The video ___ evaluated with a rubric.", "is"),
            ("There ___ six criteria.", "are"),
            ("You ___ use technical vocabulary.", "have to / need to"),
            ("___ you speak with natural rhythm?", "Do"),
            ("I ___ improve my pronunciation before submitting.", "should / need to"),
            ("Good luck — you ___ do this!", "can"),
            ("The maximum score ___ 18 points.", "is"),
            ("Students ___ to be honest in their reflection.", "have"),
            ("___ your video clearly explain WHY?", "Does"),
            ("Today ___ submission day.", "is"),
        ],
        "matching": [
            ("Evaluation", "Process of judging quality or value."),
            ("Rubric", "Document with criteria for grading."),
            ("Criterion", "A single standard used to judge."),
            ("Score", "The number of points received."),
            ("Submission", "The act of handing in work."),
            ("Fluency", "Ability to speak smoothly."),
            ("Pace", "The speed at which you speak."),
            ("Content", "The information or ideas in a text."),
            ("Justification", "A reason that explains a decision."),
            ("Reflection", "Serious thought about something personal."),
        ],
        "reading": {
            "explicit": [
                "How many criteria are in the rubric?",
                "What is the maximum total score?",
                "Name two of the six rubric criteria.",
            ],
            "implicit": [
                "Why does the teacher call this assignment a 'personal reflection'?",
            ],
            "analysis": [
                "Why are 'Content & Justification' and 'Grammar' both important and yet different?",
            ],
            "critical": [
                "After watching your own video, do you think the rubric is fair? Justify.",
            ],
        },
        "closure": "Exit ticket: Self-evaluate your video on a 1-18 scale. Which criterion do you think is your strongest?",
    },
]

# ============================================================
# HTML TEMPLATE
# ============================================================
TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Clase {num} — U1 — 1ro Medio | {title}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'Inter',sans-serif; background:#f1f5f9; color:#0f172a; line-height:1.65; }}
.hero {{ background:linear-gradient(135deg,#1e3a8a,#3730a3,#6366f1); color:#fff; padding:38px 24px; text-align:center; }}
.hero .tag {{ display:inline-block; background:rgba(255,255,255,0.18); padding:4px 14px; border-radius:999px; font-size:0.78rem; font-weight:600; letter-spacing:1px; margin-bottom:10px; }}
.hero h1 {{ font-size:2rem; font-weight:800; margin-bottom:6px; }}
.hero .sub {{ opacity:0.9; font-size:1rem; font-weight:400; }}
.meta-bar {{ background:#fff; border-bottom:1px solid #e2e8f0; padding:14px 24px; display:flex; flex-wrap:wrap; gap:18px; justify-content:center; font-size:0.88rem; }}
.meta-bar div {{ color:#475569; }}
.meta-bar strong {{ color:#1e293b; }}
.container {{ max-width:980px; margin:24px auto; padding:0 16px; }}
section.card {{ background:#fff; border-radius:14px; padding:24px; margin-bottom:18px; box-shadow:0 4px 14px rgba(15,23,42,0.06); }}
.card h2 {{ font-size:1.25rem; color:#3730a3; margin-bottom:14px; display:flex; align-items:center; gap:10px; padding-bottom:8px; border-bottom:2px solid #e0e7ff; }}
.card h3 {{ font-size:1rem; color:#1e293b; margin:14px 0 8px; }}
.text-block p {{ margin-bottom:10px; text-align:justify; color:#1e293b; }}
.text-block {{ background:#f8fafc; border-left:4px solid #6366f1; padding:16px 18px; border-radius:8px; }}
table {{ width:100%; border-collapse:collapse; margin-top:8px; font-size:0.92rem; }}
th {{ background:#3730a3; color:#fff; padding:10px; text-align:left; }}
td {{ padding:9px 10px; border-bottom:1px solid #e2e8f0; vertical-align:top; }}
tr:nth-child(even) td {{ background:#f8fafc; }}
.ipa {{ font-family:'Doulos SIL','Charis SIL',Georgia,serif; color:#7c3aed; font-weight:600; }}
ol.activity {{ counter-reset:item; list-style:none; padding-left:0; }}
ol.activity li {{ counter-increment:item; margin-bottom:10px; padding-left:34px; position:relative; }}
ol.activity li::before {{ content:counter(item); position:absolute; left:0; top:0; background:#3730a3; color:#fff; width:24px; height:24px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:0.78rem; font-weight:700; }}
.gap {{ display:inline-block; min-width:90px; border-bottom:2px solid #6366f1; padding:0 4px; color:#3730a3; font-weight:600; }}
.answer-key {{ display:none; background:#fef3c7; padding:12px 14px; border-radius:8px; margin-top:10px; border-left:4px solid #f59e0b; }}
.answer-key.show {{ display:block; }}
button.toggle {{ background:#3730a3; color:#fff; border:none; padding:8px 14px; border-radius:8px; cursor:pointer; font-weight:600; font-size:0.85rem; margin-top:10px; }}
button.toggle:hover {{ background:#1e1b4b; }}
.reading-q {{ background:#eef2ff; padding:12px 14px; border-radius:8px; margin-bottom:8px; }}
.reading-q.explicit {{ border-left:4px solid #10b981; }}
.reading-q.implicit {{ border-left:4px solid #3b82f6; }}
.reading-q.analysis {{ border-left:4px solid #f59e0b; }}
.reading-q.critical {{ border-left:4px solid #ef4444; }}
.reading-q .qtype {{ font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#64748b; margin-bottom:4px; }}
.grammar-box {{ background:#fffbeb; border:1px dashed #fbbf24; border-radius:10px; padding:14px 16px; margin-bottom:14px; }}
.grammar-box strong {{ color:#92400e; }}
.closure-box {{ background:#ecfdf5; border-left:4px solid #10b981; padding:14px 16px; border-radius:8px; }}
.nav {{ display:flex; justify-content:space-between; gap:10px; margin-top:24px; }}
.nav a {{ flex:1; text-align:center; background:#3730a3; color:#fff; padding:12px; border-radius:10px; text-decoration:none; font-weight:600; font-size:0.9rem; }}
.nav a.disabled {{ background:#cbd5e1; pointer-events:none; }}
.footer {{ text-align:center; color:#64748b; font-size:0.82rem; padding:20px 0 30px; }}
@media (max-width:720px) {{ .hero h1 {{ font-size:1.5rem; }} .card {{ padding:18px; }} th,td {{ padding:7px; font-size:0.85rem; }} }}
@media print {{ button.toggle,.nav {{ display:none; }} .answer-key {{ display:block; }} }}
</style>
</head>
<body>
<div class="hero">
  <span class="tag">Unidad 1 · Clase {num}/12</span>
  <h1>{title}</h1>
  <p class="sub">{subtitle}</p>
</div>
<div class="meta-bar">
  <div><strong>Nivel:</strong> 1ro Medio</div>
  <div><strong>Asignatura:</strong> Inglés</div>
  <div><strong>Duración:</strong> {duration}</div>
  <div><strong>Gramática:</strong> {grammar}</div>
</div>

<div class="container">

  <section class="card">
    <h2>🎯 Objetivo de Aprendizaje</h2>
    <p><strong>OA:</strong> {oa}</p>
    <p style="margin-top:8px;"><strong>Objetivo de la clase:</strong> {objective}</p>
  </section>

  <section class="card">
    <h2>📖 Reading Text — {text_title}</h2>
    <div class="text-block">
      {text_html}
    </div>
  </section>

  <section class="card">
    <h2>🔤 Vocabulary (10 words with IPA)</h2>
    <table>
      <tr><th>#</th><th>English</th><th>Pronunciation (IPA)</th><th>Español</th></tr>
      {vocab_rows}
    </table>
  </section>

  <section class="card">
    <h2>📝 Fill in the Gap (10 items)</h2>
    <div class="grammar-box"><strong>Grammar focus:</strong> {grammar}</div>
    <ol class="activity">
      {fill_items}
    </ol>
    <button class="toggle" onclick="document.getElementById('ans-fill-{num}').classList.toggle('show')">Mostrar/Ocultar respuestas</button>
    <div class="answer-key" id="ans-fill-{num}">
      <strong>Answer key:</strong>
      <ol>{fill_answers}</ol>
    </div>
  </section>

  <section class="card">
    <h2>🔗 Matching (10 pairs)</h2>
    <table>
      <tr><th>#</th><th>Concept</th><th>Definition</th></tr>
      {match_rows}
    </table>
  </section>

  <section class="card">
    <h2>📚 Reading Comprehension (6 questions — English only)</h2>
    <p style="margin-bottom:12px; color:#64748b; font-size:0.88rem;">3 explicit · 1 implicit · 1 analysis · 1 critical</p>
    {reading_html}
  </section>

  <section class="card">
    <h2>🚪 Cierre / Exit Ticket</h2>
    <div class="closure-box">{closure}</div>
  </section>

  <div class="nav">
    <a href="{prev_link}" class="{prev_class}">← Clase anterior</a>
    <a href="../index.html">📚 Índice U1</a>
    <a href="{next_link}" class="{next_class}">Próxima clase →</a>
  </div>
</div>

<div class="footer">1ro Medio · Unidad 1 — Discovering My Future Career · Clase {num}/12 · 2026</div>
</body>
</html>
"""

# ============================================================
# BUILD
# ============================================================
def esc(s): return html.escape(str(s))

def build_class(c, prev_num, next_num):
    text_html = "\n      ".join(f"<p>{esc(p)}</p>" for p in c["text"])
    vocab_rows = "\n      ".join(
        f"<tr><td>{i+1}</td><td><strong>{esc(en)}</strong></td><td class='ipa'>{esc(ipa)}</td><td>{esc(es)}</td></tr>"
        for i,(en,es,ipa) in enumerate(c["vocab"])
    )
    fill_items = "\n      ".join(
        f"<li>{esc(q).replace('___','<span class=\"gap\">&nbsp;___&nbsp;</span>')}</li>"
        for q,a in c["fill_gap"]
    )
    fill_answers = "".join(f"<li>{esc(a)}</li>" for q,a in c["fill_gap"])
    match_rows = "\n      ".join(
        f"<tr><td>{i+1}</td><td><strong>{esc(concept)}</strong></td><td>{esc(defn)}</td></tr>"
        for i,(concept,defn) in enumerate(c["matching"])
    )
    rq = []
    for q in c["reading"]["explicit"]:
        rq.append(f'<div class="reading-q explicit"><div class="qtype">Explicit</div>{esc(q)}</div>')
    for q in c["reading"]["implicit"]:
        rq.append(f'<div class="reading-q implicit"><div class="qtype">Implicit (inference)</div>{esc(q)}</div>')
    for q in c["reading"]["analysis"]:
        rq.append(f'<div class="reading-q analysis"><div class="qtype">Analysis</div>{esc(q)}</div>')
    for q in c["reading"]["critical"]:
        rq.append(f'<div class="reading-q critical"><div class="qtype">Critical thinking</div>{esc(q)}</div>')
    reading_html = "\n    ".join(rq)

    prev_link = f"Clase_{prev_num:02d}_U1_1ro.html" if prev_num else "#"
    next_link = f"Clase_{next_num:02d}_U1_1ro.html" if next_num else "#"
    prev_class = "" if prev_num else "disabled"
    next_class = "" if next_num else "disabled"

    return TEMPLATE.format(
        num=c["num"],
        title=esc(c["title"]),
        subtitle=esc(c["subtitle"]),
        duration=esc(c["duration"]),
        grammar=esc(c["grammar"]),
        oa=esc(c["oa"]),
        objective=esc(c["objective"]),
        text_title=esc(c["text_title"]),
        text_html=text_html,
        vocab_rows=vocab_rows,
        fill_items=fill_items,
        fill_answers=fill_answers,
        match_rows=match_rows,
        reading_html=reading_html,
        closure=esc(c["closure"]),
        prev_link=prev_link,
        next_link=next_link,
        prev_class=prev_class,
        next_class=next_class,
    )

def build_index():
    rows = "\n      ".join(
        f'<tr><td>{c["num"]}</td><td><a href="Clase_{c["num"]:02d}_U1_1ro.html"><strong>{esc(c["title"])}</strong></a></td><td>{esc(c["grammar"])}</td></tr>'
        for c in CLASES
    )
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unidad 1 — 1ro Medio</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Inter',sans-serif;background:#f1f5f9;color:#0f172a;line-height:1.6;}}
.hero{{background:linear-gradient(135deg,#1e3a8a,#3730a3,#6366f1);color:#fff;padding:46px 24px;text-align:center;}}
.hero h1{{font-size:2.2rem;font-weight:800;margin-bottom:8px;}}
.hero p{{opacity:0.9;}}
.container{{max-width:980px;margin:30px auto;padding:0 16px;}}
table{{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(15,23,42,0.06);}}
th{{background:#3730a3;color:#fff;padding:12px;text-align:left;}}
td{{padding:12px;border-bottom:1px solid #e2e8f0;}}
tr:nth-child(even) td{{background:#f8fafc;}}
a{{color:#3730a3;text-decoration:none;}}
a:hover{{text-decoration:underline;}}
.footer{{text-align:center;color:#64748b;font-size:0.85rem;padding:30px 0;}}
</style></head><body>
<div class="hero">
  <h1>Unidad 1 — Discovering My Future Career</h1>
  <p>1ro Medio · Inglés · 12 clases · Producto final: Video "My Future Career" (18 pts)</p>
</div>
<div class="container">
  <table>
    <tr><th>#</th><th>Clase</th><th>Gramática</th></tr>
    {rows}
  </table>
</div>
<div class="footer">1ro Medio · Unidad 1 · 12 clases · 2026</div>
</body></html>"""

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i,c in enumerate(CLASES):
        prev_num = CLASES[i-1]["num"] if i>0 else None
        next_num = CLASES[i+1]["num"] if i<len(CLASES)-1 else None
        html_out = build_class(c, prev_num, next_num)
        out_path = OUT_DIR / f"Clase_{c['num']:02d}_U1_1ro.html"
        out_path.write_text(html_out, encoding="utf-8")
        print(f"✓ {out_path.name}")
    idx = OUT_DIR / "index.html"
    idx.write_text(build_index(), encoding="utf-8")
    print(f"✓ {idx.name}")
    print(f"\nDone. {len(CLASES)} clases + index → {OUT_DIR}")

if __name__ == "__main__":
    main()
