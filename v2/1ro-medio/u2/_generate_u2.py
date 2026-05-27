# -*- coding: utf-8 -*-
"""
Generador 1ro Medio · Unidad 2 — "How It Works"
Eje: Passive Voice + descripción de procesos técnicos de las 5 especialidades.
Producto: Prueba comprensión lectora TP (clase 10) + Interrogación oral
"Describe a process" (clase 12) — exigida por la Articulación 2026.
"""
from pathlib import Path
import html, sys

# Reutilizar template y funciones del generador U1
sys.path.insert(0, str(Path(__file__).parent.parent / "u1"))
from _generate_u1 import TEMPLATE, build_class as _build_class_u1, esc  # noqa

OUT_DIR = Path(__file__).parent
UNIT_NUM = 2
UNIT_TITLE = "How It Works"
UNIT_PRODUCT = "Interrogación oral 'Describe a process' (junio)"

CLASES = [
    {
        "num": 1,
        "title": "What Is Passive Voice?",
        "subtitle": "Introduction — when and why",
        "oa": "OA10 — Identificar la voz pasiva en textos técnicos y comprender su función comunicativa.",
        "objective": "Reconocer la estructura de la voz pasiva en presente y diferenciarla de la voz activa.",
        "duration": "90 min",
        "grammar": "Passive Voice (Simple Present) — is/are + past participle",
        "text_title": "Why Do Technicians Use Passive Voice?",
        "text": [
            "In technical English, the passive voice is used very often. Why? Because in a workshop or factory, the most important thing is NOT who does the action — it is what is done. For example, technicians say 'The engine is repaired' instead of 'A mechanic repairs the engine'. The focus is on the engine, not on the mechanic.",
            "The structure is simple: subject + is/are + past participle. 'Cars are produced in factories.' 'Energy is transformed by solar panels.' 'A logo is designed by Camila.' The agent (the person who does the action) is introduced with the word 'by', but very often it is not mentioned at all.",
            "Passive voice is found in manuals, instructions, scientific texts, and process descriptions. Every TP student should master it, because manuals in English are written with passive structures on almost every page."
        ],
        "vocab": [
            ("passive voice", "voz pasiva", "/ˈpæsɪv vɔɪs/"),
            ("active voice", "voz activa", "/ˈæktɪv vɔɪs/"),
            ("subject", "sujeto", "/ˈsʌbdʒɪkt/"),
            ("agent", "agente (quien ejecuta la acción)", "/ˈeɪdʒənt/"),
            ("past participle", "participio pasado", "/pɑːst ˈpɑːrtɪsɪpəl/"),
            ("focus", "foco / énfasis", "/ˈfoʊkəs/"),
            ("structure", "estructura", "/ˈstrʌktʃər/"),
            ("manual", "manual", "/ˈmænjuəl/"),
            ("instruction", "instrucción", "/ɪnˈstrʌkʃən/"),
            ("process", "proceso", "/ˈprɒses/"),
        ],
        "fill_gap": [
            ("The engine ___ repaired by a mechanic.", "is"),
            ("Cars ___ produced in factories.", "are"),
            ("Energy ___ transformed by solar panels.", "is"),
            ("Logos ___ designed by graphic designers.", "are"),
            ("English ___ spoken in many factories.", "is"),
            ("The tools ___ cleaned every day.", "are"),
            ("A circuit ___ tested with a multimeter.", "is"),
            ("Manuals ___ written in English.", "are"),
            ("The lathe ___ operated by Daniel.", "is"),
            ("Mistakes ___ corrected during rehearsal.", "are"),
        ],
        "matching": [
            ("Passive voice", "Structure where the subject receives the action."),
            ("Active voice", "Structure where the subject does the action."),
            ("Subject", "The main noun of the sentence."),
            ("Agent", "The person or thing that performs the action."),
            ("Past participle", "Third form of a verb (worked, made, done)."),
            ("By", "Preposition that introduces the agent."),
            ("Focus", "The element of the sentence we want to highlight."),
            ("Manual", "Technical book with instructions."),
            ("Process", "A series of actions to achieve a result."),
            ("Structure", "The way grammar elements are arranged."),
        ],
        "reading": {
            "explicit": [
                "What is the structure of the passive voice in present?",
                "Which word introduces the agent in a passive sentence?",
                "Where can passive voice be found, according to the text?",
            ],
            "implicit": [
                "Why is the focus on the engine and not on the mechanic in technical English?",
            ],
            "analysis": [
                "Compare 'A mechanic repairs the engine' with 'The engine is repaired'. What changes?",
            ],
            "critical": [
                "Why should TP students 'master' passive voice for international manuals?",
            ],
        },
        "closure": "Exit ticket: Transform 3 active sentences into passive voice.",
    },
    {
        "num": 2,
        "title": "Active → Passive Transformation",
        "subtitle": "Step-by-step practice",
        "oa": "OA10 — Transformar oraciones de voz activa a pasiva manteniendo el significado.",
        "objective": "Aplicar correctamente la transformación activa→pasiva con verbos regulares e irregulares.",
        "duration": "90 min",
        "grammar": "Active vs Passive — transformation rules + irregular past participles",
        "text_title": "How to Transform a Sentence in Three Steps",
        "text": [
            "Transforming a sentence from active to passive is like a small puzzle. Step 1: identify the object of the active sentence — it will become the new subject. Step 2: choose the correct form of the verb 'to be' (is or are) according to that new subject. Step 3: add the past participle of the main verb.",
            "Example: 'Daniel uses a wrench.' → 'A wrench IS USED (by Daniel).' Another one: 'Technicians install solar panels.' → 'Solar panels ARE INSTALLED (by technicians).'",
            "Irregular verbs are challenging at first. The past participle of 'make' is 'made'. 'Buy' becomes 'bought'. 'Write' becomes 'written'. A good technician memorizes the most common irregular forms because they appear in every manual."
        ],
        "vocab": [
            ("to transform", "transformar", "/tu trænsˈfɔːrm/"),
            ("object", "objeto (complemento)", "/ˈɒbdʒɪkt/"),
            ("irregular", "irregular", "/ɪˈreɡjələr/"),
            ("regular", "regular", "/ˈreɡjələr/"),
            ("verb form", "forma verbal", "/vɜːrb fɔːrm/"),
            ("rule", "regla", "/ruːl/"),
            ("example", "ejemplo", "/ɪɡˈzɑːmpəl/"),
            ("puzzle", "rompecabezas", "/ˈpʌzəl/"),
            ("to memorize", "memorizar", "/tu ˈmeməraɪz/"),
            ("step", "paso", "/step/"),
        ],
        "fill_gap": [
            ("Active: They use computers. → Passive: Computers ___ used.", "are"),
            ("Active: The teacher explains the lesson. → Passive: The lesson ___ ___.", "is / explained"),
            ("Active: We make videos. → Passive: Videos ___ made.", "are"),
            ("Active: Sofía repairs cars. → Passive: Cars ___ ___ by Sofía.", "are / repaired"),
            ("Active: Mateo installs panels. → Passive: Panels ___ installed.", "are"),
            ("Active: Camila designs logos. → Passive: Logos ___ designed.", "are"),
            ("Active: The factory produces parts. → Passive: Parts ___ produced.", "are"),
            ("Active: People write manuals. → Passive: Manuals ___ ___.", "are / written"),
            ("Active: Students read books. → Passive: Books ___ read.", "are"),
            ("Active: He drives the truck. → Passive: The truck ___ ___.", "is / driven"),
        ],
        "matching": [
            ("Make → made", "Irregular past participle of 'make'."),
            ("Buy → bought", "Irregular past participle of 'buy'."),
            ("Write → written", "Irregular past participle of 'write'."),
            ("Drive → driven", "Irregular past participle of 'drive'."),
            ("Read → read", "Past participle that keeps the same spelling."),
            ("Use → used", "Regular past participle of 'use'."),
            ("Install → installed", "Regular past participle of 'install'."),
            ("Repair → repaired", "Regular past participle of 'repair'."),
            ("Design → designed", "Regular past participle of 'design'."),
            ("Produce → produced", "Regular past participle of 'produce'."),
        ],
        "reading": {
            "explicit": [
                "What is Step 1 of the transformation?",
                "Give the past participle of 'make', 'buy' and 'write'.",
                "How many steps does the text describe?",
            ],
            "implicit": [
                "Why is the transformation compared to 'a small puzzle'?",
            ],
            "analysis": [
                "Why do irregular past participles require memorization?",
            ],
            "critical": [
                "Do you think it is harder to learn passive voice in English or in Spanish? Why?",
            ],
        },
        "closure": "Exit ticket: Transform these 3 sentences into passive: (1) They make cars. (2) She writes reports. (3) We buy tools.",
    },
    {
        "num": 3,
        "title": "Industrial Mechanics — How a Lathe Works",
        "subtitle": "Process description #1",
        "oa": "OA10 — Comprender procesos técnicos descritos en voz pasiva.",
        "objective": "Identificar la secuencia de un proceso industrial y describirlo con voz pasiva.",
        "duration": "90 min",
        "grammar": "Passive Voice + sequence connectors (first, then, next, after, finally)",
        "text_title": "How a Metal Piece Is Shaped on a Lathe",
        "text": [
            "First, a cylindrical metal bar is selected and the technical drawing is read carefully. The required diameter and length are checked against the order. Safety glasses are worn before any operation.",
            "Then, the bar is fixed on the lathe with a chuck. The cutting tool is positioned, and the machine is turned on. The bar is rotated at high speed while the tool removes material gradually.",
            "Next, measurements are taken with a caliper. If the piece is too large, more material is removed. After that, the surface is polished. Finally, the piece is inspected, labeled, and stored for delivery."
        ],
        "vocab": [
            ("lathe", "torno", "/leɪð/"),
            ("metal bar", "barra de metal", "/ˈmetəl bɑːr/"),
            ("diameter", "diámetro", "/daɪˈæmɪtər/"),
            ("chuck", "mandril (del torno)", "/tʃʌk/"),
            ("cutting tool", "herramienta de corte", "/ˈkʌtɪŋ tuːl/"),
            ("caliper", "calibrador / pie de metro", "/ˈkælɪpər/"),
            ("to polish", "pulir", "/tu ˈpɒlɪʃ/"),
            ("to inspect", "inspeccionar", "/tu ɪnˈspekt/"),
            ("to label", "etiquetar", "/tu ˈleɪbəl/"),
            ("delivery", "entrega / despacho", "/dɪˈlɪvəri/"),
        ],
        "fill_gap": [
            ("First, the metal bar ___ selected.", "is"),
            ("Safety glasses ___ worn before any operation.", "are"),
            ("The bar ___ fixed with a chuck.", "is"),
            ("The machine ___ turned on.", "is"),
            ("Measurements ___ taken with a caliper.", "are"),
            ("The surface ___ polished.", "is"),
            ("The pieces ___ inspected and labeled.", "are"),
            ("Finally, the piece ___ stored for delivery.", "is"),
            ("The diameter ___ checked against the order.", "is"),
            ("The cutting tool ___ positioned carefully.", "is"),
        ],
        "matching": [
            ("Lathe", "Machine that rotates a piece to shape it."),
            ("Chuck", "Clamp that holds the piece on the lathe."),
            ("Cutting tool", "Sharp tool that removes material."),
            ("Caliper", "Instrument used to measure diameter."),
            ("Diameter", "Distance across a circle through the center."),
            ("To polish", "To make a surface smooth and shiny."),
            ("To inspect", "To examine carefully for defects."),
            ("To label", "To attach an identification tag."),
            ("Delivery", "The act of taking a product to its destination."),
            ("Safety glasses", "Eye protection used in workshops."),
        ],
        "reading": {
            "explicit": [
                "What is the first thing that is done?",
                "How is the bar fixed to the lathe?",
                "What is taken with a caliper?",
            ],
            "implicit": [
                "Why are safety glasses worn before any operation?",
            ],
            "analysis": [
                "Why is the process organized with sequence connectors (first, then, next, finally)?",
            ],
            "critical": [
                "If one step is skipped, what could go wrong? Choose one step and explain.",
            ],
        },
        "closure": "Exit ticket: Write 3 sequence sentences describing your morning routine using passive voice (e.g., 'Breakfast is prepared').",
    },
    {
        "num": 4,
        "title": "Automotive Mechanics — How an Oil Change Is Done",
        "subtitle": "Process description #2",
        "oa": "OA10 — Describir un proceso de mantención automotriz aplicando voz pasiva.",
        "objective": "Comprender y describir el procedimiento de cambio de aceite con conectores secuenciales.",
        "duration": "90 min",
        "grammar": "Passive Voice — sequence + agentless constructions",
        "text_title": "How an Oil Change Is Performed",
        "text": [
            "First, the car is parked on a flat surface and the engine is turned off. The car is lifted with a hydraulic jack, and the oil pan is located underneath the engine. A drain pan is placed below it.",
            "Then, the drain plug is unscrewed and the old oil is collected. While the oil is drained, the old oil filter is removed with a special wrench. A new filter is installed in its place.",
            "After that, the drain plug is tightened again. Finally, new oil is poured through the engine cap until the correct level is reached. The dipstick is checked, the cap is closed, and the car is started for a final test."
        ],
        "vocab": [
            ("oil change", "cambio de aceite", "/ɔɪl tʃeɪndʒ/"),
            ("hydraulic jack", "gato hidráulico", "/haɪˈdrɔːlɪk dʒæk/"),
            ("oil pan", "cárter de aceite", "/ɔɪl pæn/"),
            ("drain plug", "tapón de drenaje", "/dreɪn plʌɡ/"),
            ("oil filter", "filtro de aceite", "/ɔɪl ˈfɪltər/"),
            ("dipstick", "varilla medidora", "/ˈdɪpstɪk/"),
            ("to drain", "drenar", "/tu dreɪn/"),
            ("to tighten", "apretar (un perno)", "/tu ˈtaɪtən/"),
            ("to pour", "verter", "/tu pɔːr/"),
            ("engine cap", "tapa del motor", "/ˈendʒɪn kæp/"),
        ],
        "fill_gap": [
            ("The car ___ parked on a flat surface.", "is"),
            ("The engine ___ turned off.", "is"),
            ("The car ___ lifted with a jack.", "is"),
            ("The drain plug ___ unscrewed.", "is"),
            ("The old oil ___ collected.", "is"),
            ("The old filter ___ removed.", "is"),
            ("A new filter ___ installed.", "is"),
            ("The drain plug ___ tightened again.", "is"),
            ("New oil ___ poured through the cap.", "is"),
            ("The dipstick ___ checked at the end.", "is"),
        ],
        "matching": [
            ("Oil change", "Routine maintenance that replaces engine oil."),
            ("Hydraulic jack", "Device that lifts a heavy vehicle."),
            ("Oil pan", "Container under the engine that holds oil."),
            ("Drain plug", "Bolt that closes the oil pan."),
            ("Oil filter", "Component that removes impurities from oil."),
            ("Dipstick", "Stick used to measure the oil level."),
            ("To drain", "To remove a liquid from a container."),
            ("To tighten", "To make something firm by turning."),
            ("To pour", "To make a liquid flow from one place to another."),
            ("Engine cap", "Removable cover for the oil entry."),
        ],
        "reading": {
            "explicit": [
                "What is used to lift the car?",
                "What is removed with a special wrench?",
                "What is checked at the end?",
            ],
            "implicit": [
                "Why is the engine turned off before lifting the car?",
            ],
            "analysis": [
                "Why is a 'final test' done after closing the cap?",
            ],
            "critical": [
                "Should every driver know how an oil change works, even without being a mechanic? Why?",
            ],
        },
        "closure": "Exit ticket: List the 4 main steps of an oil change in passive voice.",
    },
    {
        "num": 5,
        "title": "Electricity — How a Light Switch Is Installed",
        "subtitle": "Process description #3",
        "oa": "OA10 — Aplicar voz pasiva en la descripción de instalaciones eléctricas básicas.",
        "objective": "Comprender y describir la instalación de un interruptor con voz pasiva y conectores.",
        "duration": "90 min",
        "grammar": "Passive Voice + modal passive (must be / should be)",
        "text_title": "How a Light Switch Is Installed",
        "text": [
            "First, the main breaker is turned off. Safety must always be respected; the circuit must be tested with a voltage tester before any wire is touched. Only when no current is detected, the work can begin.",
            "Then, the old switch is unscrewed from the wall box. The wires are disconnected carefully and labeled. The new switch is wired according to the diagram: the black wire is connected to the brass terminal, and the white wire to the silver one.",
            "After that, the switch is screwed back into the box. The faceplate is mounted, and the breaker is turned on again. Finally, the switch is tested several times. If the light works, the job is completed. If not, the breaker must be turned off and the connections must be reviewed."
        ],
        "vocab": [
            ("light switch", "interruptor de luz", "/laɪt swɪtʃ/"),
            ("breaker", "disyuntor / interruptor general", "/ˈbreɪkər/"),
            ("voltage tester", "probador de voltaje", "/ˈvoʊltɪdʒ ˈtestər/"),
            ("wire", "cable", "/ˈwaɪər/"),
            ("terminal", "terminal (de conexión)", "/ˈtɜːrmɪnəl/"),
            ("brass", "latón", "/bræs/"),
            ("faceplate", "placa frontal", "/ˈfeɪspleɪt/"),
            ("to screw", "atornillar", "/tu skruː/"),
            ("to connect", "conectar", "/tu kəˈnekt/"),
            ("circuit", "circuito", "/ˈsɜːrkɪt/"),
        ],
        "fill_gap": [
            ("The main breaker ___ turned off first.", "is"),
            ("Safety ___ always be respected.", "must"),
            ("The circuit ___ be tested with a voltage tester.", "must"),
            ("The old switch ___ unscrewed.", "is"),
            ("The wires ___ disconnected carefully.", "are"),
            ("The black wire ___ connected to the brass terminal.", "is"),
            ("The faceplate ___ mounted.", "is"),
            ("The breaker ___ turned on again.", "is"),
            ("The switch ___ tested several times.", "is"),
            ("If not, the connections ___ be reviewed.", "must"),
        ],
        "matching": [
            ("Light switch", "Device that opens or closes a lighting circuit."),
            ("Breaker", "Safety device that interrupts current automatically."),
            ("Voltage tester", "Tool used to detect electrical voltage."),
            ("Wire", "Insulated conductor that carries electricity."),
            ("Terminal", "Metallic point where a wire is fixed."),
            ("Brass", "Yellow metallic alloy used in terminals."),
            ("Faceplate", "Cover that hides the switch mechanism."),
            ("To screw", "To fix with a threaded fastener."),
            ("To connect", "To join two electrical parts."),
            ("Circuit", "Closed path through which current flows."),
        ],
        "reading": {
            "explicit": [
                "What is turned off first?",
                "What is the black wire connected to?",
                "What is tested several times at the end?",
            ],
            "implicit": [
                "Why is the circuit tested with a voltage tester before touching any wire?",
            ],
            "analysis": [
                "Explain the use of 'must' and 'must be' in the text. What kind of obligation does it express?",
            ],
            "critical": [
                "Would you trust yourself to install a light switch at home after reading this text? Justify.",
            ],
        },
        "closure": "Exit ticket: Write 2 safety rules using 'must be + past participle'.",
    },
    {
        "num": 6,
        "title": "Electronics — How a Smartphone Is Assembled",
        "subtitle": "Process description #4",
        "oa": "OA10 — Comprender descripciones de procesos industriales electrónicos en voz pasiva.",
        "objective": "Identificar etapas del ensamblaje electrónico y describirlas usando voz pasiva.",
        "duration": "90 min",
        "grammar": "Passive Voice — long process descriptions + while/during",
        "text_title": "How a Smartphone Is Assembled in a Factory",
        "text": [
            "First, the main board (PCB) is manufactured in a clean room. Components such as resistors, capacitors, and microchips are placed on the board by automated machines. Then, the components are soldered using a precise heating process.",
            "After that, the board is tested electronically. While the board is tested, the screen is prepared in another section of the factory. The battery is also assembled separately. During this stage, every component is verified for quality.",
            "Next, the main board, screen, battery, and case are joined together. The phone is closed and the software is installed. Finally, the device is packaged with its charger, cable, and manual. The product is now ready to be shipped."
        ],
        "vocab": [
            ("PCB (printed circuit board)", "placa de circuito impreso", "/piː siː biː/"),
            ("clean room", "sala blanca", "/kliːn ruːm/"),
            ("to manufacture", "fabricar", "/tu ˌmænjəˈfæktʃər/"),
            ("to assemble", "ensamblar", "/tu əˈsembəl/"),
            ("automated", "automatizado/a", "/ˈɔːtəmeɪtɪd/"),
            ("to ship", "enviar / despachar", "/tu ʃɪp/"),
            ("quality control", "control de calidad", "/ˈkwɒləti kənˈtroʊl/"),
            ("case", "carcasa", "/keɪs/"),
            ("battery", "batería", "/ˈbætəri/"),
            ("charger", "cargador", "/ˈtʃɑːrdʒər/"),
        ],
        "fill_gap": [
            ("The main board ___ manufactured in a clean room.", "is"),
            ("Components ___ placed by automated machines.", "are"),
            ("The components ___ soldered with a heating process.", "are"),
            ("The board ___ tested electronically.", "is"),
            ("The screen ___ prepared in another section.", "is"),
            ("The battery ___ assembled separately.", "is"),
            ("Every component ___ verified for quality.", "is"),
            ("The phone ___ closed and the software ___ installed.", "is / is"),
            ("The device ___ packaged with its accessories.", "is"),
            ("The product ___ ready to be shipped.", "is"),
        ],
        "matching": [
            ("PCB", "Flat board with electronic circuits printed on it."),
            ("Clean room", "Sterile environment for sensitive manufacturing."),
            ("To manufacture", "To produce items on a large scale."),
            ("To assemble", "To put parts together to make a product."),
            ("Automated", "Operated by machines without human action."),
            ("To ship", "To send products from a factory to customers."),
            ("Quality control", "Process of checking products for defects."),
            ("Case", "Outer shell that protects the device."),
            ("Battery", "Energy storage component."),
            ("Charger", "Device that supplies energy to a battery."),
        ],
        "reading": {
            "explicit": [
                "Where is the PCB manufactured?",
                "What is done while the board is tested?",
                "What is included in the final package?",
            ],
            "implicit": [
                "Why does the factory use a 'clean room' to manufacture the PCB?",
            ],
            "analysis": [
                "Why are batteries and screens assembled in separate sections?",
            ],
            "critical": [
                "Should consumers know how their smartphones are assembled? Justify.",
            ],
        },
        "closure": "Exit ticket: Write 3 passive sentences using 'while' or 'during'.",
    },
    {
        "num": 7,
        "title": "Graphic Design — How a Poster Is Produced",
        "subtitle": "Process description #5",
        "oa": "OA10 — Describir el proceso de producción gráfica en voz pasiva.",
        "objective": "Identificar etapas de producción de un afiche y describirlas con voz pasiva.",
        "duration": "90 min",
        "grammar": "Passive Voice — applied to creative/design processes",
        "text_title": "How a Promotional Poster Is Produced",
        "text": [
            "First, a brief is received from the client. The objective, target audience, and key message are analyzed carefully. Then, several sketches are drawn by hand or on a tablet to explore creative ideas.",
            "After the best sketch is selected, the digital design is started in Photoshop or Illustrator. Colors are chosen based on color theory, and typography is selected to match the brand. The image is composed with attention to balance and hierarchy.",
            "Next, the draft is sent to the client for feedback. Adjustments are made if necessary. Finally, the file is exported in high resolution, and the poster is printed on quality paper. The job is delivered, and the client is invoiced."
        ],
        "vocab": [
            ("brief", "encargo / requerimiento", "/briːf/"),
            ("client", "cliente", "/ˈklaɪənt/"),
            ("target audience", "público objetivo", "/ˈtɑːrɡɪt ˈɔːdiəns/"),
            ("sketch", "boceto", "/sketʃ/"),
            ("hierarchy", "jerarquía", "/ˈhaɪərɑːrki/"),
            ("balance", "equilibrio", "/ˈbæləns/"),
            ("draft", "borrador", "/drɑːft/"),
            ("feedback", "retroalimentación", "/ˈfiːdbæk/"),
            ("resolution", "resolución", "/ˌrezəˈluːʃən/"),
            ("to invoice", "facturar", "/tu ˈɪnvɔɪs/"),
        ],
        "fill_gap": [
            ("A brief ___ received from the client.", "is"),
            ("The target audience ___ analyzed carefully.", "is"),
            ("Several sketches ___ drawn.", "are"),
            ("The best sketch ___ selected.", "is"),
            ("Colors ___ chosen based on color theory.", "are"),
            ("Typography ___ selected to match the brand.", "is"),
            ("The draft ___ sent to the client.", "is"),
            ("Adjustments ___ made if necessary.", "are"),
            ("The file ___ exported in high resolution.", "is"),
            ("The client ___ invoiced at the end.", "is"),
        ],
        "matching": [
            ("Brief", "Initial document explaining the design request."),
            ("Client", "The person who orders the design."),
            ("Target audience", "Group of people the design is made for."),
            ("Sketch", "Quick rough drawing of an idea."),
            ("Hierarchy", "Order of importance of visual elements."),
            ("Balance", "Even distribution of visual weight."),
            ("Draft", "First non-final version of a design."),
            ("Feedback", "Comments to improve the work."),
            ("Resolution", "Number of pixels in an image."),
            ("To invoice", "To send a bill for payment."),
        ],
        "reading": {
            "explicit": [
                "What is received first?",
                "Where is the digital design started?",
                "What is exported at the end?",
            ],
            "implicit": [
                "Why is the draft sent to the client before final printing?",
            ],
            "analysis": [
                "How is the creative process organized to balance creativity and client needs?",
            ],
            "critical": [
                "Can artificial intelligence replace this creative process? Justify.",
            ],
        },
        "closure": "Exit ticket: Describe the production of one school product (like a poster) in 3 passive sentences.",
    },
    {
        "num": 8,
        "title": "Sequence Connectors — Mastering the Flow",
        "subtitle": "First · Then · Next · After · Finally",
        "oa": "OA14 — Producir descripciones secuenciales coherentes usando conectores temporales.",
        "objective": "Aplicar conectores secuenciales para organizar la descripción de un proceso técnico.",
        "duration": "90 min",
        "grammar": "Sequence connectors + passive voice (review)",
        "text_title": "How to Describe Any Process Like a Pro",
        "text": [
            "Every good process description follows a clear order. The most useful connectors are: 'First' (to start), 'Then' or 'Next' (to continue), 'After that' (to indicate the result of a previous step), 'While' or 'During' (to show simultaneous actions), and 'Finally' (to close the description).",
            "For example: 'First, the bread is sliced. Then, butter is spread on each slice. Next, ham and cheese are added. After that, the sandwich is closed. While the sandwich is prepared, juice is poured into a glass. Finally, breakfast is served.'",
            "Using these connectors transforms a list of steps into a smooth, professional description. They help your audience follow your explanation easily, in any technical or daily context."
        ],
        "vocab": [
            ("connector", "conector", "/kəˈnektər/"),
            ("sequence", "secuencia", "/ˈsiːkwəns/"),
            ("order", "orden", "/ˈɔːrdər/"),
            ("simultaneous", "simultáneo/a", "/ˌsɪməlˈteɪniəs/"),
            ("step", "paso / etapa", "/step/"),
            ("flow", "fluidez / flujo", "/floʊ/"),
            ("description", "descripción", "/dɪˈskrɪpʃən/"),
            ("smooth", "fluido/a", "/smuːð/"),
            ("clearly", "claramente", "/ˈklɪərli/"),
            ("audience", "audiencia", "/ˈɔːdiəns/"),
        ],
        "fill_gap": [
            ("___, the bread is sliced.", "First"),
            ("___, butter is spread on each slice.", "Then"),
            ("___, ham and cheese are added.", "Next"),
            ("___ that, the sandwich is closed.", "After"),
            ("___ the sandwich is prepared, juice is poured.", "While"),
            ("___, breakfast is served.", "Finally"),
            ("___, the customer is greeted.", "First"),
            ("___ the order is taken, the food is cooked.", "After"),
            ("___ the food is served, the bill is prepared.", "While"),
            ("___, the customer pays and leaves.", "Finally"),
        ],
        "matching": [
            ("First", "Used to mark the beginning of a sequence."),
            ("Then", "Used to indicate the next step."),
            ("Next", "Synonym of 'then' for continuation."),
            ("After that", "Used after completing a previous step."),
            ("While", "Used for simultaneous actions."),
            ("During", "Synonym of 'while' followed by a noun."),
            ("Finally", "Used to close the sequence."),
            ("Step", "A single stage in a process."),
            ("Sequence", "Ordered series of steps."),
            ("Smooth", "Flowing without interruption."),
        ],
        "reading": {
            "explicit": [
                "What connector is used to start a description?",
                "What connectors show simultaneous actions?",
                "What connector closes the description?",
            ],
            "implicit": [
                "Why do connectors transform 'a list of steps' into 'a smooth description'?",
            ],
            "analysis": [
                "Why is the order of connectors so important in technical writing?",
            ],
            "critical": [
                "Is it possible to describe a process without sequence connectors? What is lost?",
            ],
        },
        "closure": "Exit ticket: Write the process of brushing your teeth using all 5 connectors and passive voice.",
    },
    {
        "num": 9,
        "title": "Reading Practice — Pre-Test",
        "subtitle": "Get ready for the comprehension test",
        "oa": "OA9 — Demostrar comprensión de textos técnicos breves identificando información explícita e implícita.",
        "objective": "Practicar estrategias de comprensión lectora antes de la prueba formativa.",
        "duration": "90 min",
        "grammar": "Integrated review: passive voice + connectors",
        "text_title": "Recycling Aluminum — A Circular Process",
        "text": [
            "Aluminum is one of the most recycled materials in the world. First, used cans are collected from homes, schools, and factories. They are sorted by color and material, and any non-aluminum object is removed.",
            "Then, the cans are crushed into small blocks. The blocks are transported to a recycling plant. There, the aluminum is melted in a large furnace at 660°C. During this stage, paint and impurities are burned off.",
            "After the metal is purified, it is poured into molds. New aluminum sheets are produced and sold to factories. Finally, these sheets are used to make new cans, car parts, or even airplane components. The cycle is closed: a recycled can may return to the supermarket in only sixty days."
        ],
        "vocab": [
            ("aluminum", "aluminio", "/əˈluːmɪnəm/"),
            ("can", "lata", "/kæn/"),
            ("to sort", "clasificar", "/tu sɔːrt/"),
            ("to crush", "aplastar / triturar", "/tu krʌʃ/"),
            ("furnace", "horno (industrial)", "/ˈfɜːrnɪs/"),
            ("to melt", "fundir", "/tu melt/"),
            ("impurity", "impureza", "/ɪmˈpjʊərəti/"),
            ("mold", "molde", "/moʊld/"),
            ("sheet", "lámina", "/ʃiːt/"),
            ("cycle", "ciclo", "/ˈsaɪkəl/"),
        ],
        "fill_gap": [
            ("Used cans ___ collected from homes.", "are"),
            ("They ___ sorted by color and material.", "are"),
            ("The cans ___ crushed into blocks.", "are"),
            ("The blocks ___ transported to a recycling plant.", "are"),
            ("The aluminum ___ melted at 660°C.", "is"),
            ("Impurities ___ burned off.", "are"),
            ("The metal ___ poured into molds.", "is"),
            ("New sheets ___ produced and sold.", "are"),
            ("These sheets ___ used for new cans.", "are"),
            ("The cycle ___ closed in only 60 days.", "is"),
        ],
        "matching": [
            ("Aluminum", "Lightweight metal widely used and recycled."),
            ("Can", "Metallic container for drinks or food."),
            ("To sort", "To separate items into categories."),
            ("To crush", "To press something into a smaller form."),
            ("Furnace", "Industrial oven that melts metals."),
            ("To melt", "To turn a solid into a liquid by heat."),
            ("Impurity", "Substance that does not belong in a material."),
            ("Mold", "Container that shapes a liquid into a solid."),
            ("Sheet", "Thin, flat piece of metal."),
            ("Cycle", "Series of events that repeat in order."),
        ],
        "reading": {
            "explicit": [
                "Where are the cans collected from?",
                "At what temperature is the aluminum melted?",
                "How long can it take for a recycled can to return to the supermarket?",
            ],
            "implicit": [
                "Why is sorting cans by color and material important before crushing them?",
            ],
            "analysis": [
                "Explain why the text calls the process a 'closed cycle'.",
            ],
            "critical": [
                "Should aluminum recycling be mandatory in every Chilean school? Justify.",
            ],
        },
        "closure": "Exit ticket: Identify one explicit detail, one inference, and one critical reflection from any text of this unit.",
    },
    {
        "num": 10,
        "title": "🧪 READING COMPREHENSION TEST",
        "subtitle": "Evaluación formativa de comprensión lectora TP",
        "oa": "OA9 — Comprensión lectora de textos técnicos: información explícita, implícita, análisis y juicio crítico.",
        "objective": "Aplicar estrategias de comprensión lectora a un texto TP inédito (sin haberlo trabajado antes).",
        "duration": "90 min",
        "grammar": "Integrated — passive voice + connectors + technical vocabulary",
        "text_title": "TEST: How a Wind Turbine Generates Electricity",
        "text": [
            "[INSTRUCCIONES — Lee el texto en silencio durante 10 minutos. Luego responde las 6 preguntas en inglés. Tienes 60 minutos para responder. El uso de diccionario está permitido los últimos 20 minutos.]",
            "Wind energy is one of the cleanest sources of electricity in the world. A wind turbine is a large machine that transforms the kinetic energy of the wind into electrical energy. Modern turbines are installed on hills, plains, or even at sea, where the wind blows strongly and constantly.",
            "First, the wind pushes three large blades. The blades are connected to a central rotor. When the wind speed is at least 4 meters per second, the rotor is activated and it starts to spin. The blades are designed with a special aerodynamic shape, similar to an airplane wing, so even a moderate wind can move them.",
            "Then, the rotor is connected to a gearbox inside the nacelle (the box at the top of the tower). The gearbox is used to increase the rotation speed. Next, this faster rotation is transferred to a generator, where electricity is finally produced.",
            "After that, the electricity is sent through internal cables down the tower. It is then transformed by a step-up transformer to a higher voltage. Finally, the high-voltage electricity is connected to the national grid, and it is distributed to thousands of homes.",
            "Wind energy is renewable and does not emit CO₂. However, it has limitations: turbines are only effective in windy locations, they can affect birds, and they are expensive to install. Despite these challenges, wind power is considered a key technology for the future of energy in Chile and the world."
        ],
        "vocab": [
            ("wind turbine", "turbina eólica", "/wɪnd ˈtɜːrbaɪn/"),
            ("blade", "aspa / paleta", "/bleɪd/"),
            ("rotor", "rotor", "/ˈroʊtər/"),
            ("nacelle", "góndola (de turbina)", "/nəˈsel/"),
            ("gearbox", "caja de engranajes", "/ˈɡɪərbɒks/"),
            ("generator", "generador", "/ˈdʒenəreɪtər/"),
            ("kinetic energy", "energía cinética", "/kɪˈnetɪk ˈenərdʒi/"),
            ("transformer", "transformador", "/trænsˈfɔːrmər/"),
            ("grid", "red eléctrica", "/ɡrɪd/"),
            ("renewable", "renovable", "/rɪˈnjuːəbəl/"),
        ],
        "fill_gap": [
            ("A wind turbine ___ a large machine.", "is"),
            ("Modern turbines ___ installed on hills or at sea.", "are"),
            ("The blades ___ connected to a central rotor.", "are"),
            ("The blades ___ designed with an aerodynamic shape.", "are"),
            ("The gearbox ___ used to increase rotation speed.", "is"),
            ("Electricity ___ finally produced in the generator.", "is"),
            ("The electricity ___ sent through internal cables.", "is"),
            ("It ___ transformed to a higher voltage.", "is"),
            ("The high-voltage electricity ___ distributed to homes.", "is"),
            ("Wind energy ___ considered a key technology.", "is"),
        ],
        "matching": [
            ("Wind turbine", "Machine that produces electricity from wind."),
            ("Blade", "Long flat part that catches the wind."),
            ("Rotor", "Central rotating axis of a turbine."),
            ("Nacelle", "Box at the top of the tower with the gearbox."),
            ("Gearbox", "Mechanism that changes rotation speed."),
            ("Generator", "Device that produces electricity."),
            ("Kinetic energy", "Energy of motion."),
            ("Transformer", "Device that changes voltage level."),
            ("Grid", "Network that distributes electricity."),
            ("Renewable", "Naturally replenished energy source."),
        ],
        "reading": {
            "explicit": [
                "What is the minimum wind speed required to activate the rotor?",
                "Where is the gearbox located?",
                "Why is the step-up transformer used?",
            ],
            "implicit": [
                "Why are turbines often installed at sea or on hills?",
            ],
            "analysis": [
                "Trace the path of energy from the wind to the homes. List at least 4 steps in order.",
            ],
            "critical": [
                "Considering the limitations mentioned (cost, birds, location), do you think Chile should continue investing in wind energy? Justify with at least 2 reasons.",
            ],
        },
        "closure": "Cierre: revisión grupal de respuestas y autoevaluación con rúbrica adjunta.",
    },
    {
        "num": 11,
        "title": "Preparing the Oral Test — Describe a Process",
        "subtitle": "Final rehearsal before the interrogación",
        "oa": "OA13 — Producir oralmente la descripción de un proceso técnico aplicando voz pasiva y conectores.",
        "objective": "Estructurar y ensayar una descripción oral de 1-2 minutos sobre un proceso técnico elegido.",
        "duration": "90 min",
        "grammar": "Passive Voice + connectors + technical vocabulary — INTEGRATED",
        "text_title": "Model Speech — How My Coffee Is Made Every Morning",
        "text": [
            "Hello, today I am going to describe how my morning coffee is made. The process has four main steps and only takes five minutes.",
            "First, water is poured into the kettle and the kettle is turned on. While the water is heated, two spoons of ground coffee are placed in a French press. Then, when the water is boiling, it is poured slowly over the coffee.",
            "Next, the mixture is stirred and the lid is closed. The coffee is left to infuse for four minutes. After that, the plunger is pressed down slowly. Finally, the fresh coffee is served in my favorite cup, and a little milk is added. Thank you for listening — and enjoy your day!"
        ],
        "vocab": [
            ("to describe", "describir", "/tu dɪˈskraɪb/"),
            ("speech", "discurso", "/spiːtʃ/"),
            ("kettle", "hervidor", "/ˈketəl/"),
            ("ground coffee", "café molido", "/ɡraʊnd ˈkɒfi/"),
            ("French press", "prensa francesa (cafetera)", "/frentʃ pres/"),
            ("to stir", "revolver", "/tu stɜːr/"),
            ("lid", "tapa", "/lɪd/"),
            ("to infuse", "infundir / dejar reposar", "/tu ɪnˈfjuːz/"),
            ("plunger", "émbolo", "/ˈplʌndʒər/"),
            ("to serve", "servir", "/tu sɜːrv/"),
        ],
        "fill_gap": [
            ("Today I ___ going to describe a process.", "am"),
            ("Water ___ poured into the kettle.", "is"),
            ("The kettle ___ turned on.", "is"),
            ("Two spoons of coffee ___ placed in the press.", "are"),
            ("The water ___ poured over the coffee.", "is"),
            ("The mixture ___ stirred.", "is"),
            ("The lid ___ closed.", "is"),
            ("The coffee ___ left to infuse for four minutes.", "is"),
            ("The plunger ___ pressed down slowly.", "is"),
            ("Finally, the coffee ___ served.", "is"),
        ],
        "matching": [
            ("Speech", "Oral presentation in front of an audience."),
            ("Kettle", "Container used to boil water."),
            ("Ground coffee", "Coffee beans that have been milled."),
            ("French press", "Manual coffee maker with a plunger."),
            ("To stir", "To move a liquid with a spoon."),
            ("Lid", "Top cover of a container."),
            ("To infuse", "To extract flavor in a liquid by waiting."),
            ("Plunger", "Vertical rod that pushes downward."),
            ("To serve", "To present food or drink to someone."),
            ("To describe", "To explain with details."),
        ],
        "reading": {
            "explicit": [
                "How many main steps does the process have?",
                "Where is the ground coffee placed?",
                "How long is the coffee left to infuse?",
            ],
            "implicit": [
                "Why does the speaker mention that the process 'only takes five minutes'?",
            ],
            "analysis": [
                "How does the speaker open and close the speech politely?",
            ],
            "critical": [
                "Is choosing a 'daily' topic (like coffee) a good strategy for this oral test? Why?",
            ],
        },
        "closure": "Exit ticket: Choose YOUR process for next class and write the first 2 sentences of your speech.",
    },
    {
        "num": 12,
        "title": "🎤 ORAL TEST — Describe a Process",
        "subtitle": "Interrogación oral final de U2 (junio)",
        "oa": "OA13 — Producir oralmente una descripción técnica coherente aplicando voz pasiva y conectores.",
        "objective": "Presentar oralmente la descripción de un proceso técnico (1-2 minutos) ante el/la docente.",
        "duration": "90 min",
        "grammar": "ALL U2 grammar — applied in real performance.",
        "text_title": "Evaluation Criteria — How You Will Be Graded",
        "text": [
            "Today is the day of the oral interrogation. Each student is evaluated individually for 1 to 2 minutes. The teacher listens, asks one or two follow-up questions, and grades using a 5-criteria rubric.",
            "The 5 criteria are: (1) USE OF PASSIVE VOICE — at least 4 correct passive sentences are required. (2) SEQUENCE CONNECTORS — first, then, next, after, finally are used to organize the description. (3) TECHNICAL VOCABULARY — at least 5 technical words are pronounced correctly. (4) FLUENCY — speech flows without long pauses. (5) CONTENT — the process is clear and complete.",
            "Each criterion is graded from 1 to 4 points (maximum total = 20 points). Remember: confidence is rewarded. Even if you make a small mistake, keep going. Self-correction is also valued. Good luck — you are ready!"
        ],
        "vocab": [
            ("oral test", "prueba oral", "/ˈɔːrəl test/"),
            ("interrogation", "interrogación", "/ɪnˌterəˈɡeɪʃən/"),
            ("criterion", "criterio", "/kraɪˈtɪəriən/"),
            ("rubric", "rúbrica", "/ˈruːbrɪk/"),
            ("fluency", "fluidez", "/ˈfluːənsi/"),
            ("pause", "pausa", "/pɔːz/"),
            ("follow-up question", "pregunta de seguimiento", "/ˈfɒloʊ ʌp ˈkwestʃən/"),
            ("self-correction", "autocorrección", "/self kəˈrekʃən/"),
            ("performance", "desempeño", "/pərˈfɔːrməns/"),
            ("confidence", "confianza", "/ˈkɒnfɪdəns/"),
        ],
        "fill_gap": [
            ("Each student ___ evaluated individually.", "is"),
            ("The teacher ___ listens and asks questions.", "(remains active)"),
            ("At least 4 passive sentences ___ required.", "are"),
            ("Connectors ___ used to organize the description.", "are"),
            ("Technical words ___ pronounced correctly.", "are"),
            ("The maximum total ___ 20 points.", "is"),
            ("Mistakes ___ corrected by the student when possible.", "are"),
            ("The process ___ described in 1-2 minutes.", "is"),
            ("Confidence ___ rewarded.", "is"),
            ("Each criterion ___ graded from 1 to 4.", "is"),
        ],
        "matching": [
            ("Oral test", "Evaluation done by speaking, not writing."),
            ("Interrogation", "One-on-one oral assessment."),
            ("Criterion", "A standard used to judge performance."),
            ("Rubric", "Document containing all criteria."),
            ("Fluency", "Smooth, continuous speech."),
            ("Pause", "Short break in speech."),
            ("Follow-up question", "Extra question after the main answer."),
            ("Self-correction", "Fixing your own mistake immediately."),
            ("Performance", "How well a task is executed."),
            ("Confidence", "Belief in one's own ability."),
        ],
        "reading": {
            "explicit": [
                "How long should each student speak?",
                "How many criteria are in the rubric?",
                "What is the maximum total score?",
            ],
            "implicit": [
                "Why is self-correction valued?",
            ],
            "analysis": [
                "Why is 'CONFIDENCE' explicitly rewarded?",
            ],
            "critical": [
                "After your performance, do you think the rubric is fair? Justify.",
            ],
        },
        "closure": "Exit ticket: Self-evaluate your oral test on the 20-point scale. Which criterion was your strongest? Which one will you improve for next year?",
    },
]

# ============================================================
# BUILD (overrides U1 unit data via decorator)
# ============================================================
def build_index():
    rows = "\n      ".join(
        f'<tr><td>{c["num"]}</td><td><a href="Clase_{c["num"]:02d}_U2_1ro.html"><strong>{esc(c["title"])}</strong></a></td><td>{esc(c["grammar"])}</td></tr>'
        for c in CLASES
    )
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unidad 2 — 1ro Medio | How It Works</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Inter',sans-serif;background:#f1f5f9;color:#0f172a;line-height:1.6;}}
.hero{{background:linear-gradient(135deg,#0f766e,#0ea5a4,#10b981);color:#fff;padding:46px 24px;text-align:center;}}
.hero h1{{font-size:2.2rem;font-weight:800;margin-bottom:8px;}}
.hero p{{opacity:0.9;}}
.container{{max-width:980px;margin:30px auto;padding:0 16px;}}
table{{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(15,23,42,0.06);}}
th{{background:#0f766e;color:#fff;padding:12px;text-align:left;}}
td{{padding:12px;border-bottom:1px solid #e2e8f0;}}
tr:nth-child(even) td{{background:#f8fafc;}}
a{{color:#0f766e;text-decoration:none;font-weight:600;}}
a:hover{{text-decoration:underline;}}
.footer{{text-align:center;color:#64748b;font-size:0.85rem;padding:30px 0;}}
</style></head><body>
<div class="hero">
  <h1>Unidad 2 — How It Works</h1>
  <p>1ro Medio · Inglés · 12 clases · Passive Voice + descripción de procesos TP · {UNIT_PRODUCT}</p>
</div>
<div class="container">
  <table>
    <tr><th>#</th><th>Clase</th><th>Gramática</th></tr>
    {rows}
  </table>
</div>
<div class="footer">1ro Medio · Unidad 2 · 12 clases · 2026</div>
</body></html>"""

def build_class(c, prev_num, next_num):
    """Same as U1 but writes Clase_NN_U2_1ro.html with green accent."""
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

    prev_link = f"Clase_{prev_num:02d}_U2_1ro.html" if prev_num else "#"
    next_link = f"Clase_{next_num:02d}_U2_1ro.html" if next_num else "#"
    prev_class = "" if prev_num else "disabled"
    next_class = "" if next_num else "disabled"

    # Recolor: passive voice unit uses teal/emerald gradient
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
    # Swap U1 indigo gradient for U2 teal/emerald + update breadcrumb tag
    html_out = html_out.replace(
        "linear-gradient(135deg,#1e3a8a,#3730a3,#6366f1)",
        "linear-gradient(135deg,#0f766e,#0ea5a4,#10b981)"
    ).replace("#3730a3", "#0f766e").replace("#6366f1", "#10b981").replace("#e0e7ff", "#d1fae5")
    html_out = html_out.replace(
        f"Unidad 1 · Clase {c['num']}/12",
        f"Unidad 2 · Clase {c['num']}/12"
    )
    html_out = html_out.replace(
        "1ro Medio · Unidad 1 — Discovering My Future Career",
        "1ro Medio · Unidad 2 — How It Works"
    )
    return html_out

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i,c in enumerate(CLASES):
        prev_num = CLASES[i-1]["num"] if i>0 else None
        next_num = CLASES[i+1]["num"] if i<len(CLASES)-1 else None
        html_out = build_class(c, prev_num, next_num)
        out_path = OUT_DIR / f"Clase_{c['num']:02d}_U2_1ro.html"
        out_path.write_text(html_out, encoding="utf-8")
        print(f"✓ {out_path.name}")
    idx = OUT_DIR / "index.html"
    idx.write_text(build_index(), encoding="utf-8")
    print(f"✓ {idx.name}")
    print(f"\nDone. {len(CLASES)} clases + index → {OUT_DIR}")

if __name__ == "__main__":
    main()
