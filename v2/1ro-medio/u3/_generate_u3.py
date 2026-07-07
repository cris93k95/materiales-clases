# -*- coding: utf-8 -*-
"""
Generador 1ro Medio · Unidad 3 — "Innovators & Stories"
Eje: Past Simple + Past Continuous, biografías de innovadores TP.
Producto: Mini-biografía escrita + presentación grupal.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "u1"))
from _generate_u1 import TEMPLATE, esc  # noqa

OUT_DIR = Path(__file__).parent

CLASES = [
    {
        "num": 1,
        "title": "Was & Were — Talking About the Past",
        "subtitle": "Introduction to Past Simple",
        "oa": "OA10 — Reconocer y usar el verbo To Be en pasado para describir situaciones pasadas.",
        "objective": "Usar was / were para describir personas, lugares y situaciones del pasado.",
        "duration": "90 min",
        "grammar": "Past Simple of TO BE — was / were (affirmative, negative, questions)",
        "text_title": "My Grandfather Was a Mechanic",
        "text": [
            "My grandfather was a mechanic in the 1970s. He was a quiet man, but he was very proud of his job. He and his colleagues were specialists in old Ford and Chevrolet engines, which were very common in Chile at that time.",
            "His workshop was small but clean. The tools were old but reliable. My grandmother sometimes says: 'Cars were simpler back then. There were no computers, no sensors, no chips. A good mechanic only needed his hands, his eyes, and his experience.'",
            "Today, modern cars are different. They are full of electronics. But my grandfather was a real master of his craft, and his stories were always full of grease, hard work, and pride."
        ],
        "vocab": [
            ("grandfather", "abuelo", "/ˈɡrænˌfɑːðər/"),
            ("colleague", "colega", "/ˈkɒliːɡ/"),
            ("specialist", "especialista", "/ˈspeʃəlɪst/"),
            ("proud", "orgulloso/a", "/praʊd/"),
            ("reliable", "confiable", "/rɪˈlaɪəbəl/"),
            ("master", "maestro/a (experto)", "/ˈmɑːstər/"),
            ("craft", "oficio", "/krɑːft/"),
            ("grease", "grasa", "/ɡriːs/"),
            ("sensor", "sensor", "/ˈsensər/"),
            ("experience", "experiencia", "/ɪkˈspɪəriəns/"),
        ],
        "fill_gap": [
            ("My grandfather ___ a mechanic in the 1970s.", "was"),
            ("He and his colleagues ___ specialists in old engines.", "were"),
            ("The workshop ___ small but clean.", "was"),
            ("The tools ___ old but reliable.", "were"),
            ("There ___ no computers in those cars.", "were"),
            ("Cars ___ simpler back then.", "were"),
            ("My grandfather ___ proud of his job.", "was"),
            ("His stories ___ full of grease and pride.", "were"),
            ("___ your grandfather a technician too?", "Was"),
            ("They ___ not mechanics — they ___ electricians.", "were / were"),
        ],
        "matching": [
            ("Was", "Past form of 'is' (singular)."),
            ("Were", "Past form of 'are' (plural / you)."),
            ("Grandfather", "Father of one's father or mother."),
            ("Colleague", "Person who works with you."),
            ("Specialist", "Expert in a specific field."),
            ("Proud", "Feeling satisfied of an achievement."),
            ("Reliable", "Trustworthy, dependable."),
            ("Master", "A person with great skill in an art or craft."),
            ("Craft", "An activity that requires manual skill."),
            ("Experience", "Knowledge gained over time."),
        ],
        "reading": {
            "explicit": [
                "When did the grandfather work as a mechanic?",
                "What car brands did he specialize in?",
                "How was his workshop?",
            ],
            "implicit": [
                "Why does the text say modern cars 'are full of electronics'?",
            ],
            "analysis": [
                "Compare cars 'back then' with cars today, according to the text.",
            ],
            "critical": [
                "Is it easier to be a mechanic today or in the 1970s? Justify.",
            ],
        },
        "closure": "Exit ticket: Write 3 sentences about your family using 'was' / 'were'.",
    },
    {
        "num": 2,
        "title": "Past Simple — Regular Verbs",
        "subtitle": "Adding -ed",
        "oa": "OA10 — Aplicar correctamente la terminación -ed para formar el pasado de verbos regulares.",
        "objective": "Conjugar verbos regulares en pasado y aplicarlos en narraciones técnicas.",
        "duration": "90 min",
        "grammar": "Past Simple regular verbs (-ed / -d / -ied)",
        "text_title": "How Camila Discovered Her Passion",
        "text": [
            "Last year, Camila visited the school's graphic design workshop for the first time. She watched a student designing a poster, and she immediately wanted to learn. The teacher noticed her interest and invited her to try.",
            "She opened the software, clicked on a tool, and started to play. She experimented for hours. She moved colors, changed fonts, and copied templates. At the end of the class, she created her first small design.",
            "She arrived home very excited. She showed the design to her mother and explained every detail. That night, Camila decided that graphic design was her future."
        ],
        "vocab": [
            ("to discover", "descubrir", "/tu dɪˈskʌvər/"),
            ("to visit", "visitar", "/tu ˈvɪzɪt/"),
            ("to watch", "observar", "/tu wɒtʃ/"),
            ("to notice", "notar / darse cuenta", "/tu ˈnoʊtɪs/"),
            ("to invite", "invitar", "/tu ɪnˈvaɪt/"),
            ("to click", "hacer clic", "/tu klɪk/"),
            ("to experiment", "experimentar", "/tu ɪkˈsperɪment/"),
            ("to copy", "copiar", "/tu ˈkɒpi/"),
            ("to explain", "explicar", "/tu ɪkˈspleɪn/"),
            ("to decide", "decidir", "/tu dɪˈsaɪd/"),
        ],
        "fill_gap": [
            ("Camila ___ (visit) the workshop.", "visited"),
            ("She ___ (watch) a student designing.", "watched"),
            ("The teacher ___ (notice) her interest.", "noticed"),
            ("She ___ (open) the software.", "opened"),
            ("She ___ (click) on a tool.", "clicked"),
            ("She ___ (experiment) for hours.", "experimented"),
            ("She ___ (copy) some templates.", "copied"),
            ("She ___ (create) her first design.", "created"),
            ("She ___ (arrive) home excited.", "arrived"),
            ("She ___ (decide) that design was her future.", "decided"),
        ],
        "matching": [
            ("Visited", "Past of 'visit'."),
            ("Watched", "Past of 'watch'."),
            ("Noticed", "Past of 'notice'."),
            ("Opened", "Past of 'open'."),
            ("Clicked", "Past of 'click'."),
            ("Experimented", "Past of 'experiment'."),
            ("Copied", "Past of 'copy' (y → ied)."),
            ("Created", "Past of 'create' (ends in e → +d)."),
            ("Explained", "Past of 'explain'."),
            ("Decided", "Past of 'decide' (ends in e → +d)."),
        ],
        "reading": {
            "explicit": [
                "Where did Camila go for the first time?",
                "What did she do with the software?",
                "Who did she show her design to?",
            ],
            "implicit": [
                "Why did the teacher invite Camila to try?",
            ],
            "analysis": [
                "Identify 5 regular verbs from the text and write their past form.",
            ],
            "critical": [
                "Is it important to 'try things' before choosing a specialty? Justify.",
            ],
        },
        "closure": "Exit ticket: Write 4 things you did yesterday using regular past verbs.",
    },
    {
        "num": 3,
        "title": "Past Simple — Irregular Verbs",
        "subtitle": "The verbs that don't follow rules",
        "oa": "OA10 — Identificar y usar correctamente verbos irregulares en pasado simple.",
        "objective": "Memorizar y aplicar al menos 15 verbos irregulares de uso frecuente en pasado.",
        "duration": "90 min",
        "grammar": "Past Simple irregular verbs",
        "text_title": "Mateo's First Day at the Workshop",
        "text": [
            "Mateo got up at 6 a.m. He had breakfast, took his backpack, and went to the workshop with his father. They drove for 30 minutes. When they arrived, the workshop was already open.",
            "His father gave him an apron and said: 'Today, you are my apprentice.' Mateo felt nervous but excited. He saw the tools on the wall and read the safety rules. Then he heard the sound of a drill — work had begun.",
            "During the day, Mateo learned many things. He held a multimeter for the first time, wrote down measurements, and even made a small connection by himself. At 5 p.m., he came home tired but happy. He thought to himself: 'This is what I want to do.'"
        ],
        "vocab": [
            ("got up", "se levantó (get up)", "/ɡɒt ʌp/"),
            ("had", "tuvo / desayunó (have)", "/hæd/"),
            ("took", "tomó (take)", "/tʊk/"),
            ("went", "fue (go)", "/went/"),
            ("drove", "condujo (drive)", "/droʊv/"),
            ("gave", "dio (give)", "/ɡeɪv/"),
            ("felt", "sintió (feel)", "/felt/"),
            ("saw", "vio (see)", "/sɔː/"),
            ("read", "leyó (read — pron. /red/)", "/red/"),
            ("thought", "pensó (think)", "/θɔːt/"),
        ],
        "fill_gap": [
            ("Mateo ___ (get) up at 6 a.m.", "got"),
            ("He ___ (have) breakfast.", "had"),
            ("He ___ (take) his backpack.", "took"),
            ("They ___ (drive) for 30 minutes.", "drove"),
            ("His father ___ (give) him an apron.", "gave"),
            ("Mateo ___ (feel) nervous.", "felt"),
            ("He ___ (see) the tools.", "saw"),
            ("He ___ (read) the safety rules.", "read"),
            ("He ___ (hold) a multimeter for the first time.", "held"),
            ("He ___ (come) home tired but happy.", "came"),
        ],
        "matching": [
            ("Get → got", "Irregular past of 'get'."),
            ("Have → had", "Irregular past of 'have'."),
            ("Take → took", "Irregular past of 'take'."),
            ("Go → went", "Irregular past of 'go'."),
            ("Drive → drove", "Irregular past of 'drive'."),
            ("Give → gave", "Irregular past of 'give'."),
            ("See → saw", "Irregular past of 'see'."),
            ("Read → read", "Same spelling, different sound /red/."),
            ("Make → made", "Irregular past of 'make'."),
            ("Think → thought", "Irregular past of 'think'."),
        ],
        "reading": {
            "explicit": [
                "What time did Mateo get up?",
                "How long did they drive?",
                "What did Mateo do for the first time?",
            ],
            "implicit": [
                "Why did Mateo feel 'nervous but excited'?",
            ],
            "analysis": [
                "Identify 6 irregular verbs from the text and give the infinitive of each one.",
            ],
            "critical": [
                "Is it useful for a 1st Medio student to visit a workshop with their family? Why?",
            ],
        },
        "closure": "Exit ticket: Write 4 sentences using 4 different irregular past verbs about your weekend.",
    },
    {
        "num": 4,
        "title": "Past Simple — Negatives & Questions",
        "subtitle": "Did / Didn't",
        "oa": "OA10 — Producir oraciones negativas e interrogativas en pasado usando did/didn't.",
        "objective": "Formular preguntas y negaciones en pasado correctamente con did/didn't.",
        "duration": "90 min",
        "grammar": "Past Simple — questions (Did + base verb) + negatives (didn't + base verb)",
        "text_title": "An Interview With Sofía",
        "text": [
            "Reporter: Sofía, did you always want to be a mechanic? Sofía: No, I didn't! When I was a child, I wanted to be an astronaut. I didn't think about cars at all.",
            "Reporter: So, what changed? Sofía: My uncle gave me a small toy car when I was 8. I didn't play with it — I opened it and broke it! I wanted to see how it worked. My mother didn't like the mess, but my uncle laughed and said: 'She is a future mechanic!'",
            "Reporter: Did you study mechanics in basic school? Sofía: No, I didn't. There weren't classes about it. But I read books, I watched videos, and I asked many questions. Then, in 8th grade, I decided to apply to a TP high school."
        ],
        "vocab": [
            ("reporter", "reportero/a", "/rɪˈpɔːrtər/"),
            ("interview", "entrevista", "/ˈɪntərvjuː/"),
            ("astronaut", "astronauta", "/ˈæstrənɔːt/"),
            ("toy", "juguete", "/tɔɪ/"),
            ("uncle", "tío", "/ˈʌŋkəl/"),
            ("mess", "desorden", "/mes/"),
            ("future", "futuro", "/ˈfjuːtʃər/"),
            ("to laugh", "reír", "/tu lɑːf/"),
            ("to apply", "postular", "/tu əˈplaɪ/"),
            ("childhood", "infancia", "/ˈtʃaɪldhʊd/"),
        ],
        "fill_gap": [
            ("___ you always want to be a mechanic? No, I ___.", "Did / didn't"),
            ("I ___ think about cars when I was a child.", "didn't"),
            ("My uncle ___ (give) me a toy car.", "gave"),
            ("I ___ play with it — I broke it!", "didn't"),
            ("My mother ___ like the mess.", "didn't"),
            ("___ you study mechanics in basic school? No, I ___.", "Did / didn't"),
            ("There ___ classes about it.", "weren't"),
            ("I ___ many questions to my teachers.", "asked"),
            ("___ she apply to a TP high school? Yes, she ___.", "Did / did"),
            ("We ___ choose our specialty in 1st grade.", "didn't"),
        ],
        "matching": [
            ("Did", "Past auxiliary for questions."),
            ("Didn't", "Negative form of 'did' (did not)."),
            ("Reporter", "Person who interviews and reports news."),
            ("Interview", "Conversation with specific questions."),
            ("Astronaut", "Person trained to travel in space."),
            ("Toy", "Object for play, usually for children."),
            ("Mess", "State of disorder or dirt."),
            ("Future", "Time that has not yet come."),
            ("To laugh", "To express joy with sound."),
            ("To apply", "To formally request admission."),
        ],
        "reading": {
            "explicit": [
                "What did Sofía want to be when she was a child?",
                "What did her uncle give her?",
                "When did she decide to apply to TP school?",
            ],
            "implicit": [
                "Why did her uncle say 'she is a future mechanic'?",
            ],
            "analysis": [
                "Identify 3 negative past sentences and 2 questions in past from the text.",
            ],
            "critical": [
                "Should children be free to break their toys to understand them? Justify.",
            ],
        },
        "closure": "Exit ticket: Write 3 questions and 3 negative sentences in past about your last weekend.",
    },
    {
        "num": 5,
        "title": "Nikola Tesla — The Electrical Genius",
        "subtitle": "Mini-biography #1 (Electricity)",
        "oa": "OA10 — Comprender biografías técnicas breves identificando hechos relevantes en pasado.",
        "objective": "Identificar la cronología y aportes de Nikola Tesla en una biografía técnica.",
        "duration": "90 min",
        "grammar": "Past Simple — applied to biographies",
        "text_title": "Nikola Tesla (1856–1943)",
        "text": [
            "Nikola Tesla was born in 1856 in a small village in Croatia. As a child, he was very curious and intelligent. He studied physics, mathematics, and engineering at the Polytechnic in Graz, Austria.",
            "In 1884, Tesla moved to New York and worked with Thomas Edison for a short time. They didn't agree about electricity: Edison defended direct current (DC), but Tesla believed in alternating current (AC). Tesla left Edison's company and created his own designs.",
            "In 1888, Tesla invented the AC induction motor — a discovery that changed the world. Power stations, factories, and homes were soon connected with AC systems. He also worked with wireless transmission and radio. Tesla died in 1943, alone and poor. Today, electric cars and renewable energy carry his legacy."
        ],
        "vocab": [
            ("genius", "genio", "/ˈdʒiːniəs/"),
            ("village", "aldea", "/ˈvɪlɪdʒ/"),
            ("physics", "física", "/ˈfɪzɪks/"),
            ("engineering", "ingeniería", "/ˌendʒɪˈnɪərɪŋ/"),
            ("direct current (DC)", "corriente continua", "/dəˈrekt ˈkɜːrənt/"),
            ("alternating current (AC)", "corriente alterna", "/ˈɔːltərneɪtɪŋ ˈkɜːrənt/"),
            ("induction motor", "motor de inducción", "/ɪnˈdʌkʃən ˈmoʊtər/"),
            ("power station", "central eléctrica", "/ˈpaʊər ˈsteɪʃən/"),
            ("wireless", "inalámbrico/a", "/ˈwaɪərləs/"),
            ("legacy", "legado", "/ˈleɡəsi/"),
        ],
        "fill_gap": [
            ("Tesla ___ (be) born in 1856.", "was"),
            ("He ___ (study) physics and engineering.", "studied"),
            ("In 1884, he ___ (move) to New York.", "moved"),
            ("He ___ (work) with Edison for a short time.", "worked"),
            ("They ___ (not / agree) about electricity.", "didn't agree"),
            ("Tesla ___ (leave) Edison's company.", "left"),
            ("In 1888, he ___ (invent) the AC induction motor.", "invented"),
            ("Power stations ___ (be) connected with AC systems.", "were"),
            ("Tesla ___ (die) in 1943.", "died"),
            ("His legacy ___ (live) on today.", "lives"),
        ],
        "matching": [
            ("Genius", "Person with extraordinary intelligence."),
            ("Physics", "Science of matter and energy."),
            ("Engineering", "Application of science to design machines."),
            ("Direct current", "Electricity that flows in one direction."),
            ("Alternating current", "Electricity that changes direction periodically."),
            ("Induction motor", "Motor based on electromagnetic induction."),
            ("Power station", "Facility that generates electrical energy."),
            ("Wireless", "Without physical cables."),
            ("Legacy", "What someone leaves to future generations."),
            ("Discovery", "Finding something for the first time."),
        ],
        "reading": {
            "explicit": [
                "When and where was Tesla born?",
                "Who did Tesla work with in New York?",
                "What did Tesla invent in 1888?",
            ],
            "implicit": [
                "Why did Tesla and Edison disagree?",
            ],
            "analysis": [
                "How does the text contrast Tesla's contributions with his personal fate ('alone and poor')?",
            ],
            "critical": [
                "Is it fair that great inventors sometimes die poor? Justify with reference to today's world.",
            ],
        },
        "closure": "Exit ticket: Write 4 facts about Tesla using past simple.",
    },
    {
        "num": 6,
        "title": "Henry Ford — The Father of Mass Production",
        "subtitle": "Mini-biography #2 (Automotive)",
        "oa": "OA10 — Comprender una biografía técnica e identificar el impacto histórico de un innovador automotriz.",
        "objective": "Reconocer el aporte de Henry Ford a la mecánica automotriz y al trabajo industrial.",
        "duration": "90 min",
        "grammar": "Past Simple — narration + dates",
        "text_title": "Henry Ford (1863–1947)",
        "text": [
            "Henry Ford was born in 1863 on a farm in Michigan, USA. As a teenager, he loved machines and watches. He did not want to be a farmer like his father. At 16, he left home and worked as a mechanic in Detroit.",
            "In 1903, Ford founded the Ford Motor Company. In 1908, he launched the Model T — the first car that ordinary families could afford. Until then, cars were expensive and slow to build.",
            "Ford's biggest innovation was the moving assembly line, introduced in 1913. With this system, a worker did only one task many times. The production time of a Model T was reduced from 12 hours to 90 minutes! Ford also paid his workers good salaries — $5 a day, double the average at the time. He believed that workers should be able to buy the cars they built."
        ],
        "vocab": [
            ("mass production", "producción en masa", "/mæs prəˈdʌkʃən/"),
            ("farm", "granja", "/fɑːrm/"),
            ("teenager", "adolescente", "/ˈtiːnˌeɪdʒər/"),
            ("to found", "fundar", "/tu faʊnd/"),
            ("to launch", "lanzar (al mercado)", "/tu lɔːntʃ/"),
            ("ordinary", "común / corriente", "/ˈɔːrdənəri/"),
            ("assembly line", "línea de ensamblaje", "/əˈsembli laɪn/"),
            ("worker", "trabajador/a", "/ˈwɜːrkər/"),
            ("salary", "salario", "/ˈsæləri/"),
            ("average", "promedio", "/ˈævərɪdʒ/"),
        ],
        "fill_gap": [
            ("Ford ___ (be) born in 1863.", "was"),
            ("He ___ (love) machines.", "loved"),
            ("He ___ (not / want) to be a farmer.", "didn't want"),
            ("At 16, he ___ (leave) home.", "left"),
            ("In 1903, he ___ (found) the Ford Motor Company.", "founded"),
            ("In 1908, he ___ (launch) the Model T.", "launched"),
            ("Cars ___ (be) expensive before that.", "were"),
            ("He ___ (introduce) the assembly line in 1913.", "introduced"),
            ("Production time ___ (be) reduced to 90 minutes.", "was"),
            ("He ___ (pay) good salaries to his workers.", "paid"),
        ],
        "matching": [
            ("Mass production", "Manufacturing many identical products."),
            ("Farm", "Land used for crops and animals."),
            ("Teenager", "Person between 13 and 19 years old."),
            ("To found", "To establish (a company, school, etc.)."),
            ("To launch", "To start selling something new."),
            ("Ordinary", "Common, not special."),
            ("Assembly line", "Production system with sequential tasks."),
            ("Worker", "Employee, especially in manual labor."),
            ("Salary", "Money paid regularly for work."),
            ("Average", "The typical or middle value."),
        ],
        "reading": {
            "explicit": [
                "Where and when was Ford born?",
                "When did Ford launch the Model T?",
                "How much time did the assembly line save per car?",
            ],
            "implicit": [
                "Why was the Model T revolutionary?",
            ],
            "analysis": [
                "Explain Ford's belief: 'workers should be able to buy the cars they built'.",
            ],
            "critical": [
                "Was the assembly line good or bad for workers? Justify with at least 2 ideas.",
            ],
        },
        "closure": "Exit ticket: Write 4 important facts about Ford in chronological order.",
    },
    {
        "num": 7,
        "title": "Alan Turing — The Father of Computing",
        "subtitle": "Mini-biography #3 (Electronics)",
        "oa": "OA10 — Identificar hechos clave en una biografía técnica de un pionero de la electrónica.",
        "objective": "Reconocer la importancia de Alan Turing en la electrónica moderna.",
        "duration": "90 min",
        "grammar": "Past Simple — narration + cause/effect",
        "text_title": "Alan Turing (1912–1954)",
        "text": [
            "Alan Turing was born in London in 1912. As a young student, he loved mathematics and science. He studied at Cambridge University, where he wrote a paper that imagined a machine able to perform any calculation — today we call it a 'computer'.",
            "During World War II, Turing worked at Bletchley Park, a secret base in England. There, he and his team built a machine that broke the Enigma code used by Nazi Germany. Many historians believe that Turing's work shortened the war by two years and saved millions of lives.",
            "After the war, Turing helped to design the first electronic computers. He also explored artificial intelligence and asked the question: 'Can machines think?' Sadly, Turing was persecuted because of his sexuality and he died in 1954. In 2009, the British government finally apologized. Today, the 'Turing Award' is the most important prize in computer science."
        ],
        "vocab": [
            ("computing", "informática", "/kəmˈpjuːtɪŋ/"),
            ("calculation", "cálculo", "/ˌkælkjəˈleɪʃən/"),
            ("paper", "artículo académico", "/ˈpeɪpər/"),
            ("code", "código", "/koʊd/"),
            ("to break", "descifrar / romper", "/tu breɪk/"),
            ("historian", "historiador/a", "/hɪˈstɔːriən/"),
            ("artificial intelligence", "inteligencia artificial", "/ˌɑːrtɪˈfɪʃəl ɪnˈtelɪdʒəns/"),
            ("to persecute", "perseguir / discriminar", "/tu ˈpɜːrsɪkjuːt/"),
            ("to apologize", "disculparse", "/tu əˈpɒlədʒaɪz/"),
            ("award", "premio", "/əˈwɔːrd/"),
        ],
        "fill_gap": [
            ("Turing ___ (be) born in London in 1912.", "was"),
            ("He ___ (love) mathematics and science.", "loved"),
            ("He ___ (study) at Cambridge University.", "studied"),
            ("He ___ (write) a paper about a future machine.", "wrote"),
            ("During WWII, he ___ (work) at Bletchley Park.", "worked"),
            ("His team ___ (break) the Enigma code.", "broke"),
            ("Many historians ___ (believe) he saved millions of lives.", "believe"),
            ("He ___ (help) to design the first computers.", "helped"),
            ("He ___ (die) in 1954.", "died"),
            ("In 2009, the government ___ (apologize).", "apologized"),
        ],
        "matching": [
            ("Computing", "Activity of using or developing computers."),
            ("Calculation", "Mathematical process of computing numbers."),
            ("Paper", "Written academic work."),
            ("Code", "System of symbols to encode information."),
            ("To break", "To decipher or solve a code."),
            ("Historian", "Expert who studies the past."),
            ("Artificial intelligence", "Machine ability to simulate thinking."),
            ("To persecute", "To treat someone cruelly because of beliefs or identity."),
            ("To apologize", "To say sorry."),
            ("Award", "Prize given for achievement."),
        ],
        "reading": {
            "explicit": [
                "Where did Turing study?",
                "What code did Turing and his team break?",
                "What is the most important prize in computer science today?",
            ],
            "implicit": [
                "Why did Turing's work 'shorten the war by two years'?",
            ],
            "analysis": [
                "How does the text describe both Turing's success and his tragedy?",
            ],
            "critical": [
                "Should governments apologize for historical injustices? Justify.",
            ],
        },
        "closure": "Exit ticket: Write 4 sentences about Turing's contributions to electronics and computing.",
    },
    {
        "num": 8,
        "title": "Paul Rand — The Master of Logos",
        "subtitle": "Mini-biography #4 (Graphic Design)",
        "oa": "OA10 — Comprender una biografía de un innovador del diseño gráfico.",
        "objective": "Identificar la importancia de Paul Rand en la historia del diseño gráfico moderno.",
        "duration": "90 min",
        "grammar": "Past Simple — narration + descriptive details",
        "text_title": "Paul Rand (1914–1996)",
        "text": [
            "Paul Rand was born in Brooklyn, New York, in 1914. As a child, he drew constantly. He studied at the Pratt Institute and later worked as an art director in advertising agencies. In the 1940s, he became famous for his bold, minimalist designs.",
            "Rand designed logos for some of the most important companies in the world: IBM, ABC, UPS, Westinghouse, and Steve Jobs's company NeXT. His IBM logo, created in 1956, was a simple combination of three letters with horizontal stripes. It became one of the most recognized logos ever made.",
            "Rand wrote several books about design philosophy. He defended one main idea: 'A logo doesn't sell — it identifies.' He died in 1996, but his designs are still everywhere. Every TP graphic design student learns from his work, because Rand proved that simple ideas can have enormous power."
        ],
        "vocab": [
            ("logo", "logotipo", "/ˈloʊɡoʊ/"),
            ("art director", "director/a de arte", "/ɑːrt dəˈrektər/"),
            ("advertising", "publicidad", "/ˈædvərtaɪzɪŋ/"),
            ("agency", "agencia", "/ˈeɪdʒənsi/"),
            ("bold", "audaz / atrevido", "/boʊld/"),
            ("minimalist", "minimalista", "/ˈmɪnɪməlɪst/"),
            ("stripe", "raya / franja", "/straɪp/"),
            ("philosophy", "filosofía", "/fəˈlɒsəfi/"),
            ("to identify", "identificar", "/tu aɪˈdentɪfaɪ/"),
            ("recognized", "reconocido/a", "/ˈrekəɡnaɪzd/"),
        ],
        "fill_gap": [
            ("Paul Rand ___ (be) born in 1914.", "was"),
            ("As a child, he ___ (draw) constantly.", "drew"),
            ("He ___ (study) at the Pratt Institute.", "studied"),
            ("He ___ (become) famous in the 1940s.", "became"),
            ("He ___ (design) logos for IBM, ABC, and UPS.", "designed"),
            ("The IBM logo ___ (be) created in 1956.", "was"),
            ("It ___ (become) one of the most recognized logos.", "became"),
            ("He ___ (write) several books.", "wrote"),
            ("He ___ (defend) one main idea.", "defended"),
            ("Rand ___ (prove) that simple ideas have power.", "proved"),
        ],
        "matching": [
            ("Logo", "Symbol that identifies a brand."),
            ("Art director", "Person who supervises visual content."),
            ("Advertising", "Activity of promoting products or services."),
            ("Agency", "Business that provides a specific service."),
            ("Bold", "Strong, confident, eye-catching."),
            ("Minimalist", "Using only essential elements."),
            ("Stripe", "Long narrow band of color."),
            ("Philosophy", "Set of beliefs and ideas."),
            ("To identify", "To recognize or distinguish."),
            ("Recognized", "Known and accepted."),
        ],
        "reading": {
            "explicit": [
                "Where was Paul Rand born?",
                "Name three companies whose logos he designed.",
                "When did he create the IBM logo?",
            ],
            "implicit": [
                "Why does the text say his designs 'are still everywhere'?",
            ],
            "analysis": [
                "Explain Rand's idea: 'A logo doesn't sell — it identifies.'",
            ],
            "critical": [
                "Do you agree that 'simple ideas can have enormous power'? Give one example from your own life.",
            ],
        },
        "closure": "Exit ticket: Sketch a simple logo for an imaginary brand and explain it in 2 past-tense sentences (e.g., 'I drew a circle because…').",
    },
    {
        "num": 9,
        "title": "Henry Bessemer — Steel for the Modern World",
        "subtitle": "Mini-biography #5 (Industrial)",
        "oa": "OA10 — Comprender una biografía de un innovador industrial e identificar el impacto de su invención.",
        "objective": "Reconocer la importancia de Henry Bessemer en la mecánica industrial moderna.",
        "duration": "90 min",
        "grammar": "Past Simple — narration + dates + cause/effect",
        "text_title": "Henry Bessemer (1813–1898)",
        "text": [
            "Henry Bessemer was born in 1813 in a small English town called Charlton. He was the son of a type foundry worker, so he grew up around metal and machines. He didn't go to a fancy university, but he was a brilliant self-taught engineer.",
            "During the Crimean War (1853–1856), Bessemer tried to make better artillery. He realized that steel was much stronger than iron, but at that time, steel was very expensive and slow to produce. He started to experiment with a new method.",
            "In 1856, he presented the Bessemer Process: hot air was blown through liquid iron to remove impurities and create high-quality steel quickly and cheaply. The result was revolutionary! Railroads, bridges, ships, and skyscrapers became possible thanks to cheap steel. Bessemer became rich and famous. His process changed industrial mechanics forever."
        ],
        "vocab": [
            ("steel", "acero", "/stiːl/"),
            ("iron", "hierro", "/ˈaɪərn/"),
            ("foundry", "fundición", "/ˈfaʊndri/"),
            ("self-taught", "autodidacta", "/self tɔːt/"),
            ("artillery", "artillería", "/ɑːrˈtɪləri/"),
            ("to blow", "soplar", "/tu bloʊ/"),
            ("impurity", "impureza", "/ɪmˈpjʊərəti/"),
            ("railroad", "ferrocarril", "/ˈreɪlroʊd/"),
            ("bridge", "puente", "/brɪdʒ/"),
            ("skyscraper", "rascacielos", "/ˈskaɪskreɪpər/"),
        ],
        "fill_gap": [
            ("Bessemer ___ (be) born in 1813.", "was"),
            ("He ___ (grow) up around metal.", "grew"),
            ("He ___ (not / go) to a fancy university.", "didn't go"),
            ("He ___ (try) to make better artillery.", "tried"),
            ("He ___ (realize) that steel was stronger than iron.", "realized"),
            ("He ___ (start) to experiment with a new method.", "started"),
            ("In 1856, he ___ (present) his process.", "presented"),
            ("Hot air ___ (be) blown through liquid iron.", "was"),
            ("Railroads and bridges ___ (become) possible.", "became"),
            ("His process ___ (change) industry forever.", "changed"),
        ],
        "matching": [
            ("Steel", "Strong alloy of iron and carbon."),
            ("Iron", "Basic metal extracted from ore."),
            ("Foundry", "Factory where metal is melted and cast."),
            ("Self-taught", "Educated by oneself, without formal teachers."),
            ("Artillery", "Heavy weapons such as cannons."),
            ("To blow", "To produce a current of air."),
            ("Impurity", "Unwanted substance in a material."),
            ("Railroad", "Track system for trains."),
            ("Bridge", "Structure built over an obstacle."),
            ("Skyscraper", "Very tall building."),
        ],
        "reading": {
            "explicit": [
                "Where and when was Bessemer born?",
                "What did he try to improve during the Crimean War?",
                "What method did he present in 1856?",
            ],
            "implicit": [
                "Why was the Bessemer Process revolutionary?",
            ],
            "analysis": [
                "List three structures that became possible thanks to cheap steel.",
            ],
            "critical": [
                "Is being 'self-taught' still possible in modern engineering? Justify.",
            ],
        },
        "closure": "Exit ticket: Write 4 sentences in past simple about a person who inspires you (real or imaginary).",
    },
    {
        "num": 10,
        "title": "Past Continuous — While It Happened",
        "subtitle": "was/were + -ing",
        "oa": "OA10 — Usar el Past Continuous para describir acciones en progreso en el pasado.",
        "objective": "Aplicar Past Continuous para contextualizar acciones en una narración técnica.",
        "duration": "90 min",
        "grammar": "Past Continuous — was/were + verb-ing",
        "text_title": "While Mateo Was Working…",
        "text": [
            "Yesterday at 10 a.m., Mateo was working in the electrical workshop. He was testing a circuit with the multimeter. His teacher was explaining a new diagram on the whiteboard. Everything was going well — until the light suddenly turned off.",
            "Mateo's classmates were laughing because they thought it was a joke. But it was not a joke! Camila was using a 3D printer in the next room. Sofía was charging her phone. While they were doing all these activities at the same time, the breaker tripped.",
            "The teacher smiled and said: 'This is a perfect lesson. While you were learning theory, the school was teaching you something more important: never overload a circuit!' Everyone laughed and the lesson continued."
        ],
        "vocab": [
            ("to test", "probar", "/tu test/"),
            ("circuit", "circuito", "/ˈsɜːrkɪt/"),
            ("whiteboard", "pizarra", "/ˈwaɪtbɔːrd/"),
            ("suddenly", "de repente", "/ˈsʌdənli/"),
            ("joke", "broma", "/dʒoʊk/"),
            ("3D printer", "impresora 3D", "/θriː diː ˈprɪntər/"),
            ("to charge", "cargar (batería)", "/tu tʃɑːrdʒ/"),
            ("breaker tripped", "saltó el disyuntor", "/ˈbreɪkər trɪpt/"),
            ("to overload", "sobrecargar", "/tu ˌoʊvərˈloʊd/"),
            ("theory", "teoría", "/ˈθɪəri/"),
        ],
        "fill_gap": [
            ("Mateo ___ (work) in the workshop.", "was working"),
            ("He ___ (test) a circuit.", "was testing"),
            ("His teacher ___ (explain) a diagram.", "was explaining"),
            ("Mateo's classmates ___ (laugh).", "were laughing"),
            ("Camila ___ (use) a 3D printer.", "was using"),
            ("Sofía ___ (charge) her phone.", "was charging"),
            ("They ___ (do) all these activities at the same time.", "were doing"),
            ("While they ___ (learn) theory, the school taught them a lesson.", "were learning"),
            ("Everything ___ (go) well at first.", "was going"),
            ("___ you ___ (study) at 10 a.m. yesterday?", "Were / studying"),
        ],
        "matching": [
            ("To test", "To check if something works."),
            ("Circuit", "Closed path for electrical current."),
            ("Whiteboard", "White surface used for teaching."),
            ("Suddenly", "Quickly and unexpectedly."),
            ("Joke", "Something said or done to make people laugh."),
            ("3D printer", "Device that creates 3D objects."),
            ("To charge", "To supply energy to a battery."),
            ("Breaker tripped", "Circuit breaker activated by overload."),
            ("To overload", "To put too much demand on a system."),
            ("Theory", "Set of ideas that explains something."),
        ],
        "reading": {
            "explicit": [
                "What was Mateo doing at 10 a.m.?",
                "What was the teacher doing on the whiteboard?",
                "What was Sofía doing?",
            ],
            "implicit": [
                "Why did the breaker trip?",
            ],
            "analysis": [
                "What did the teacher mean by 'the school was teaching you something more important'?",
            ],
            "critical": [
                "Is it useful to learn through real-life accidents in a workshop? Justify.",
            ],
        },
        "closure": "Exit ticket: Write 3 sentences in past continuous about what you were doing yesterday at 8 p.m., 12 p.m., and 6 p.m.",
    },
    {
        "num": 11,
        "title": "Writing Your Own Mini-Biography",
        "subtitle": "Past Simple + Past Continuous combined",
        "oa": "OA14 — Producir un texto biográfico breve combinando estructuras gramaticales del pasado.",
        "objective": "Redactar una mini-biografía (150 palabras) de un/a innovador/a TP elegido/a usando pasado simple y continuo.",
        "duration": "90 min",
        "grammar": "Past Simple + Past Continuous combined — 'When X happened, Y was happening.'",
        "text_title": "Model Bio — María Skłodowska Curie",
        "text": [
            "María Skłodowska was born in Warsaw, Poland, in 1867. Her family was very poor, but her parents were teachers and they valued education. While she was studying at home with her father, she was developing a passion for science.",
            "In 1891, she moved to Paris and studied at the Sorbonne. There, she met Pierre Curie. They got married in 1895 and worked together in a small laboratory. While they were experimenting with uranium, they discovered two new elements: polonium and radium.",
            "Marie Curie won two Nobel Prizes — one in Physics (1903) and one in Chemistry (1911). She was the first woman to win, and the first person to win in two different sciences. She died in 1934, but her research opened the door to modern medicine and electronics."
        ],
        "vocab": [
            ("biography", "biografía", "/baɪˈɒɡrəfi/"),
            ("paragraph", "párrafo", "/ˈpærəɡrɑːf/"),
            ("draft", "borrador", "/drɑːft/"),
            ("element", "elemento", "/ˈelɪmənt/"),
            ("laboratory", "laboratorio", "/ləˈbɒrətəri/"),
            ("Nobel Prize", "Premio Nobel", "/noʊˈbel praɪz/"),
            ("research", "investigación", "/rɪˈsɜːrtʃ/"),
            ("medicine", "medicina", "/ˈmedɪsɪn/"),
            ("to value", "valorar", "/tu ˈvæljuː/"),
            ("passion", "pasión", "/ˈpæʃən/"),
        ],
        "fill_gap": [
            ("Marie ___ (be) born in 1867.", "was"),
            ("Her parents ___ (be) teachers.", "were"),
            ("While she ___ (study) at home, she ___ (develop) a passion.", "was studying / was developing"),
            ("In 1891, she ___ (move) to Paris.", "moved"),
            ("She ___ (meet) Pierre Curie.", "met"),
            ("They ___ (get) married in 1895.", "got"),
            ("While they ___ (experiment) with uranium, they ___ (discover) two elements.", "were experimenting / discovered"),
            ("She ___ (win) two Nobel Prizes.", "won"),
            ("She ___ (die) in 1934.", "died"),
            ("Her research ___ (open) the door to modern science.", "opened"),
        ],
        "matching": [
            ("Biography", "Story of a person's life."),
            ("Paragraph", "Group of sentences on a single idea."),
            ("Draft", "Preliminary version of a text."),
            ("Element", "Pure chemical substance."),
            ("Laboratory", "Place for scientific experiments."),
            ("Nobel Prize", "International award for outstanding achievement."),
            ("Research", "Systematic investigation."),
            ("Medicine", "Science of preventing and treating disease."),
            ("To value", "To consider important."),
            ("Passion", "Strong personal interest."),
        ],
        "reading": {
            "explicit": [
                "Where was Marie Curie born?",
                "What did she discover with Pierre?",
                "How many Nobel Prizes did she win?",
            ],
            "implicit": [
                "Why does the text say her family 'valued education'?",
            ],
            "analysis": [
                "Identify ONE sentence that combines Past Simple AND Past Continuous in the text.",
            ],
            "critical": [
                "Is Marie Curie a good role model for TP students today? Justify.",
            ],
        },
        "closure": "Exit ticket: Write the FIRST paragraph of YOUR mini-bio (innovator of your choice, 3-4 sentences).",
    },
    {
        "num": 12,
        "title": "🎤 Final Presentation — Mini-Bio Showcase",
        "subtitle": "Group presentation + written delivery",
        "oa": "OA13/OA14 — Producir oral y escritamente una biografía técnica coherente.",
        "objective": "Presentar oralmente en grupo la mini-biografía redactada y entregarla escrita al docente.",
        "duration": "90 min",
        "grammar": "INTEGRATED — Past Simple + Past Continuous + connectors",
        "text_title": "Today's Plan & Evaluation Criteria",
        "text": [
            "Today is the showcase day. Each group of 3-4 students presents the mini-biography they wrote. The order is decided by a draw. Each presentation lasts about 3 minutes, and every student speaks at least once.",
            "The evaluation has two parts. Part 1 (10 points): WRITTEN BIOGRAPHY — correct use of past simple, past continuous, connectors, and technical vocabulary. The text must be 100-150 words. Part 2 (10 points): ORAL PRESENTATION — clarity, pronunciation, eye contact, and teamwork.",
            "Remember: a biography is not a long list of dates. It is a story about a real person who changed the world. Choose carefully, speak clearly, and feel proud of your work. After all the presentations, the class will vote for the best 'INNOVATOR OF THE UNIT'. Good luck — and enjoy the showcase!"
        ],
        "vocab": [
            ("showcase", "muestra / exhibición", "/ˈʃoʊkeɪs/"),
            ("group", "grupo", "/ɡruːp/"),
            ("draw (lottery)", "sorteo", "/drɔː/"),
            ("delivery", "entrega", "/dɪˈlɪvəri/"),
            ("clarity", "claridad", "/ˈklærəti/"),
            ("teamwork", "trabajo en equipo", "/ˈtiːmwɜːrk/"),
            ("vote", "voto", "/voʊt/"),
            ("innovator", "innovador/a", "/ˈɪnəveɪtər/"),
            ("criterion", "criterio", "/kraɪˈtɪəriən/"),
            ("to enjoy", "disfrutar", "/tu ɪnˈdʒɔɪ/"),
        ],
        "fill_gap": [
            ("Today ___ (be) the showcase day.", "is"),
            ("Each group ___ (present) their biography.", "presents"),
            ("Yesterday we ___ (practice) our presentation.", "practiced"),
            ("While I ___ (write) my paragraph, my partner ___ (search) for facts.", "was writing / was searching"),
            ("Marie Curie ___ (be) a great innovator.", "was"),
            ("She ___ (win) two Nobel Prizes.", "won"),
            ("Each presentation ___ (last) 3 minutes.", "lasts"),
            ("Tesla ___ (live) in a difficult time.", "lived"),
            ("Last class, we ___ (choose) our innovator together.", "chose"),
            ("Now we ___ (be) ready to present!", "are"),
        ],
        "matching": [
            ("Showcase", "Public display of skills or work."),
            ("Group", "Set of people working together."),
            ("Draw", "Random selection method."),
            ("Delivery", "The act of submitting work."),
            ("Clarity", "Quality of being easy to understand."),
            ("Teamwork", "Cooperation in a group."),
            ("Vote", "Formal expression of choice."),
            ("Innovator", "Person who introduces new ideas."),
            ("Criterion", "Standard for judging."),
            ("To enjoy", "To take pleasure in something."),
        ],
        "reading": {
            "explicit": [
                "How long does each presentation last?",
                "How many points does the written biography have?",
                "What does the class do after all the presentations?",
            ],
            "implicit": [
                "Why does the text say 'a biography is not a long list of dates'?",
            ],
            "analysis": [
                "Why are written and oral parts evaluated separately?",
            ],
            "critical": [
                "Is group voting a fair way to choose the best innovator? Justify.",
            ],
        },
        "closure": "Exit ticket: Submit your written biography to the teacher. Self-evaluate your presentation on a 1-10 scale.",
    },
]

MATCH_LABELS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shuffled_matching_rows(pairs, class_number):
    definitions = [definition for concept, definition in pairs]
    if len(definitions) > 1:
        shift = (class_number % (len(definitions) - 1)) + 1
        definitions = definitions[shift:] + definitions[:shift]
    rows = []
    for index, ((concept, _), definition) in enumerate(zip(pairs, definitions)):
        rows.append((index + 1, concept, f"{MATCH_LABELS[index]}. {definition}"))
    return rows


def normalize_term(term):
    return "".join(ch for ch in term.upper() if ch.isalpha())


def make_blank_cells(length):
    return " ".join("___" for _ in range(max(length, 1)))


def rotate_text(text, step):
    if len(text) < 2:
        return text
    shift = step % len(text)
    if shift == 0:
        shift = 1
    return text[shift:] + text[:shift]


def render_crossword(vocab):
    clues = []
    for index, (word, meaning, _) in enumerate(vocab[:6], start=1):
        normalized = normalize_term(word)
        direction = "Across" if index <= 3 else "Down"
        clues.append(
            f"<li><strong>{direction} {index}.</strong> {esc(meaning)} "
            f"<small>({len(normalized)} letters)</small><br>{make_blank_cells(len(normalized))}</li>"
        )
    return (
        "<section class=\"card\">"
        "<h2>🧩 Vocabulary Challenge — Mini Crossword</h2>"
        "<p style=\"margin-bottom:12px;color:#64748b;\">Read each clue and write the technical word in English. Ignore spaces when counting letters.</p>"
        f"<ol class=\"activity\">{''.join(clues)}</ol>"
        "</section>"
    )


def render_word_search(vocab):
    words = [normalize_term(word) for word, _, _ in vocab[:6]]
    width = max(11, max(len(word) for word in words))
    alphabet = "TECHNICALWORDS"
    rows = []
    for row_index, word in enumerate(words):
        offset = (row_index * 2) % max(1, width - len(word) + 1)
        filler = []
        for col_index in range(width - len(word)):
            filler.append(alphabet[(row_index + col_index) % len(alphabet)])
        row = "".join(filler[:offset]) + word + "".join(filler[offset:])
        rows.append(row[:width])
    while len(rows) < width:
        row_index = len(rows)
        rows.append("".join(alphabet[(row_index + col_index) % len(alphabet)] for col_index in range(width)))
    word_bank = ", ".join(esc(word) for word, _, _ in vocab[:6])
    grid = "<br>".join(" ".join(row) for row in rows)
    return (
        "<section class=\"card\">"
        "<h2>🔎 Vocabulary Challenge — Word Search</h2>"
        f"<p style=\"margin-bottom:12px;color:#64748b;\">Find these words in the grid: {word_bank}.</p>"
        f"<div style=\"font-family:monospace;line-height:1.7;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:14px;letter-spacing:0.12em;\">{grid}</div>"
        "</section>"
    )


def render_unscramble(vocab, class_number):
    rows = []
    for index, (word, meaning, _) in enumerate(vocab[:6], start=1):
        normalized = normalize_term(word)
        scrambled = rotate_text(normalized, class_number + index)
        if scrambled == normalized:
            scrambled = normalized[::-1]
        rows.append(
            f"<li><strong>{esc(scrambled)}</strong> — {esc(meaning)}<br>{make_blank_cells(len(normalized))}</li>"
        )
    return (
        "<section class=\"card\">"
        "<h2>🔤 Vocabulary Challenge — Unscramble the Terms</h2>"
        "<p style=\"margin-bottom:12px;color:#64748b;\">Unscramble each technical word and write the correct version in English.</p>"
        f"<ol class=\"activity\">{''.join(rows)}</ol>"
        "</section>"
    )


def render_clue_bank(vocab):
    clues = []
    for index, (word, meaning, _) in enumerate(vocab[:6], start=1):
        normalized = normalize_term(word)
        clues.append(
            f"<li><strong>Clue {index}.</strong> {esc(meaning)} "
            f"<small>({len(normalized)} letters)</small><br>{make_blank_cells(len(normalized))}</li>"
        )
    return (
        "<section class=\"card\">"
        "<h2>🕵️ Vocabulary Challenge — Definition Detective</h2>"
        "<p style=\"margin-bottom:12px;color:#64748b;\">Match each definition with the correct English term from today's vocabulary.</p>"
        f"<ol class=\"activity\">{''.join(clues)}</ol>"
        "</section>"
    )


def build_vocab_activity(vocab, class_number, class_title):
    lowered = class_title.lower()
    if "showcase" in lowered or "presentation" in lowered:
        return ""
    selector = (class_number - 1) % 4
    if selector == 0:
        return render_crossword(vocab)
    if selector == 1:
        return render_word_search(vocab)
    if selector == 2:
        return render_unscramble(vocab, class_number)
    return render_clue_bank(vocab)

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
        f"<tr><td>{row_num}</td><td><strong>{esc(concept)}</strong></td><td>{esc(defn)}</td></tr>"
        for row_num, concept, defn in shuffled_matching_rows(c["matching"], c["num"])
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

    prev_link = f"Clase_{prev_num:02d}_U3_1ro.html" if prev_num else "#"
    next_link = f"Clase_{next_num:02d}_U3_1ro.html" if next_num else "#"
    prev_class = "" if prev_num else "disabled"
    next_class = "" if next_num else "disabled"

    html_out = TEMPLATE.format(
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
    vocab_activity_html = build_vocab_activity(c["vocab"], c["num"], c["title"])
    if vocab_activity_html:
        html_out = html_out.replace(
            "  </section>\n\n  <section class=\"card\">\n    <h2>📝 Fill in the Gap (10 items)</h2>",
            f"  </section>\n\n  {vocab_activity_html}\n\n  <section class=\"card\">\n    <h2>📝 Fill in the Gap (10 items)</h2>",
            1,
        )
    # U3 color: warm amber/rose (innovators & stories)
    html_out = html_out.replace(
        "linear-gradient(135deg,#1e3a8a,#3730a3,#6366f1)",
        "linear-gradient(135deg,#9a3412,#c2410c,#ea580c)"
    ).replace("#3730a3", "#9a3412").replace("#6366f1", "#ea580c").replace("#e0e7ff", "#ffedd5")
    html_out = html_out.replace(
        f"Unidad 1 · Clase {c['num']}/12",
        f"Unidad 3 · Clase {c['num']}/12"
    )
    html_out = html_out.replace(
        f"Clase {c['num']} — U1 — 1ro Medio",
        f"Clase {c['num']} — U3 — 1ro Medio"
    )
    html_out = html_out.replace(
        "1ro Medio · Unidad 1 — Discovering My Future Career",
        "1ro Medio · Unidad 3 — Innovators & Stories"
    )
    html_out = html_out.replace('href="../index.html">📚 Índice U1', 'href="index.html">📚 Índice U3')
    return html_out

def build_index():
    rows = "\n      ".join(
        f'<tr><td>{c["num"]}</td><td><a href="Clase_{c["num"]:02d}_U3_1ro.html"><strong>{esc(c["title"])}</strong></a></td><td>{esc(c["grammar"])}</td></tr>'
        for c in CLASES
    )
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unidad 3 — 1ro Medio | Innovators & Stories</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Inter',sans-serif;background:#f1f5f9;color:#0f172a;line-height:1.6;}}
.hero{{background:linear-gradient(135deg,#9a3412,#c2410c,#ea580c);color:#fff;padding:46px 24px;text-align:center;}}
.hero h1{{font-size:2.2rem;font-weight:800;margin-bottom:8px;}}
.hero p{{opacity:0.9;}}
.container{{max-width:980px;margin:30px auto;padding:0 16px;}}
table{{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(15,23,42,0.06);}}
th{{background:#9a3412;color:#fff;padding:12px;text-align:left;}}
td{{padding:12px;border-bottom:1px solid #e2e8f0;}}
tr:nth-child(even) td{{background:#f8fafc;}}
a{{color:#9a3412;text-decoration:none;font-weight:600;}}
a:hover{{text-decoration:underline;}}
.footer{{text-align:center;color:#64748b;font-size:0.85rem;padding:30px 0;}}
</style></head><body>
<div class="hero">
  <h1>Unidad 3 — Innovators & Stories</h1>
  <p>1ro Medio · Inglés · 12 clases · Past Simple + Past Continuous · Producto: mini-biografía + presentación grupal</p>
</div>
<div class="container">
  <table>
    <tr><th>#</th><th>Clase</th><th>Gramática</th></tr>
    {rows}
  </table>
</div>
<div class="footer">1ro Medio · Unidad 3 · 12 clases · 2026</div>
</body></html>"""

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i,c in enumerate(CLASES):
        prev_num = CLASES[i-1]["num"] if i>0 else None
        next_num = CLASES[i+1]["num"] if i<len(CLASES)-1 else None
        out = build_class(c, prev_num, next_num)
        (OUT_DIR / f"Clase_{c['num']:02d}_U3_1ro.html").write_text(out, encoding="utf-8")
        print(f"✓ Clase_{c['num']:02d}_U3_1ro.html")
    (OUT_DIR / "index.html").write_text(build_index(), encoding="utf-8")
    print(f"✓ index.html\n\nDone. {len(CLASES)} clases + index → {OUT_DIR}")

if __name__ == "__main__":
    main()
