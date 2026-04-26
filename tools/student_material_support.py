import re


TERM_DEFINITIONS = {
    "hammer": "a hand tool used to hit nails or shape material",
    "screwdriver": "a tool used to tighten or loosen screws",
    "wrench": "a tool used to turn bolts or nuts",
    "wire": "a metal conductor that carries electricity",
    "circuit": "a complete path that lets electricity move",
    "printer": "a machine that produces text or images on paper",
    "engine": "the machine that produces power in a vehicle",
    "brake": "the system that slows or stops movement",
    "panel": "a board where controls, circuits, or indicators are grouped",
    "switch": "a control that opens or closes an electrical connection",
    "battery": "a device that stores electrical energy",
    "tool": "an object used to do a practical or technical job",
    "lathe": "a machine that turns material so it can be shaped",
    "mill": "a machine used to cut material with rotating tools",
    "drill press": "a fixed machine used to drill accurate holes",
    "welder": "equipment used to join metal parts with heat",
    "caliper": "a tool used to measure thickness or distance accurately",
    "micrometer": "a precision tool for very small measurements",
    "file": "a hand tool used to smooth or shape a surface",
    "grinding wheel": "a rotating abrasive wheel used for shaping or finishing",
    "vise": "a tool that holds material firmly in place during work",
    "clamp": "a device that keeps parts together or fixed during a task",
    "blueprint": "a technical drawing that shows how something must be built",
    "tolerance": "the allowed small difference in a measurement",
    "steel": "a strong metal used in structures, machines, and tools",
    "aluminum": "a light metal used in many industrial and transport products",
    "brake pad": "the part of a brake system that presses to stop the wheel",
    "transmission": "the system that transfers power from the engine to movement",
    "coolant": "liquid that controls the temperature of an engine or system",
    "jack": "a device used to lift a vehicle safely",
    "spark plug": "a component that creates the spark needed in many engines",
    "oil filter": "the part that removes impurities from engine oil",
    "radiator": "the system that helps cool the engine",
    "exhaust": "the system that carries gases away from the engine",
    "tire": "the rubber part that covers the wheel and contacts the road",
    "alternator": "the part that generates electrical power in a vehicle",
    "diagnostic scanner": "a tool that reads digital fault information from a vehicle",
    "breaker": "a protective switch that stops current during a fault",
    "outlet": "the connection point where electrical devices receive power",
    "voltage": "the electrical force that pushes current through a circuit",
    "current": "the flow of electricity through a circuit",
    "resistance": "the opposition to electrical flow in a material or circuit",
    "multimeter": "an instrument that measures voltage, current, and resistance",
    "pliers": "a hand tool used to grip, bend, or cut wire and parts",
    "conduit": "protective tubing used to route electrical wiring",
    "transformer": "equipment that changes electrical voltage levels",
    "grounding": "a safety connection that sends electricity safely to the earth",
    "ink": "colored liquid used in printing",
    "paper": "the material used as a surface for printed work",
    "plate": "the prepared surface that carries the printable image",
    "press": "the machine that transfers ink onto paper or another surface",
    "offset": "a printing method where the image is transferred indirectly",
    "digital printing": "printing produced directly from digital files without plates",
    "binding": "the process of joining printed pages together",
    "color profile": "the settings that control how colors are represented",
    "cmyk": "the four-color model used in printing: cyan, magenta, yellow, and black",
    "resolution": "the level of detail or image sharpness in a file or print",
    "prepress": "the stage where files are prepared before printing",
    "cutter": "a machine or tool used to trim material precisely",
    "laminator": "equipment that adds a protective film to a printed surface",
    "densitometer": "an instrument used to measure ink density or color consistency",
    "resistor": "a component that limits electrical current",
    "capacitor": "a component that stores and releases electrical energy",
    "transistor": "a semiconductor component used to switch or amplify signals",
    "led": "a component that emits light when current passes through it",
    "pcb": "a board that holds and connects electronic components",
    "soldering iron": "a heated tool used to join electronic parts with solder",
    "oscilloscope": "an instrument that displays electrical signals as waves",
    "diode": "a component that allows current mainly in one direction",
    "integrated circuit": "a small chip that contains many electronic functions",
    "sensor": "a device that detects change and sends information",
    "amplifier": "a circuit or device that increases signal strength",
    "frequency": "the number of repetitions of a signal in one second",
    "signal": "electrical information that carries data",
    "cnc machine": "computer-controlled equipment used for precise machining",
    "milling": "the machining process of cutting material with rotating tools",
    "hydraulic press": "a machine that uses fluid pressure to apply force",
    "welding (mig/tig)": "controlled metal joining processes used for different materials and finishes",
    "quality control": "the process of verifying that a result meets the required standard",
    "technical drawing": "a precise visual plan that communicates measurements and design details",
    "engine diagnostics": "the analysis used to identify vehicle faults and performance issues",
    "obd scanner": "a tool that reads digital fault codes from vehicle systems",
    "fuel injection": "the system that delivers fuel to the engine in a controlled way",
    "turbocharger": "a device that increases engine power by compressing air",
    "hybrid system": "a vehicle system that combines electric and fuel power",
    "torque": "the turning force that makes a part rotate",
    "horsepower": "a measure of engine power output",
    "alignment": "the correct position of wheels or parts so the system works properly",
    "three-phase power": "an electrical system that uses three alternating currents",
    "circuit breaker": "a protective device that stops current during overload or fault",
    "voltage regulator": "a device that keeps voltage stable",
    "switchgear": "equipment that controls, protects, and isolates electrical systems",
    "load calculation": "the process of determining the electrical demand required",
    "microcontroller": "a small programmable chip used to control a device",
    "pcb design": "the planning and organization of tracks and components on a circuit board",
    "firmware": "software stored inside a device to control its functions",
    "soldering station": "a work unit used for safe and controlled soldering",
    "iot sensor": "a connected device that collects physical data for digital systems",
    "embedded system": "a hardware-software system built into a device",
    "signal processing": "the analysis and modification of electronic signals",
}


A2_QUESTION_ITEMS = [
    "What is the main task or routine described in the text?",
    "Which tool, system, or material appears first in the reading?",
    "What actions help the reader understand the sequence of the job?",
    "Which technical words are essential for understanding the text?",
    "Why is English useful in this professional situation?",
    "What idea from the text can you use in your own future workshop context?",
]


B1_QUESTION_ITEMS = [
    "What professional challenge, responsibility, or goal is described in the text?",
    "Which tools, systems, or documents shape the routine or decision-making process?",
    "How does the sequence of actions support quality, safety, or efficiency?",
    "Which evidence from the text shows the importance of technical vocabulary in context?",
    "Why does English become necessary beyond simple translation in this professional setting?",
    "What transferable career skill can you infer from the reading and why does it matter?",
]


def clean_text(text):
    return re.sub(r"\s+", " ", text or "").strip()


def course_level(course_key):
    return "A2" if course_key.startswith("1ro") else "B1"


def reading_note(course_key):
    if course_level(course_key) == "A2":
        return "Texto graduado A2: cinco parrafos, secuencia clara y apoyo de vocabulario para comprender la rutina tecnica."
    return "Texto B1: cinco parrafos con contexto profesional, evidencia tecnica y razonamiento aplicado."


def definition_for_term(word):
    normalized = clean_text(word).lower()
    return TERM_DEFINITIONS.get(normalized, f"technical term linked to {normalized}")


def build_question_list_markup(course_key):
    questions = A2_QUESTION_ITEMS if course_level(course_key) == "A2" else B1_QUESTION_ITEMS
    return "<ol>" + "".join(f"<li>{question}</li>" for question in questions) + "</ol>"


def expand_reading(base_paragraphs, course_key, course_label, vocab_words, objective):
    paragraphs = [clean_text(p) for p in base_paragraphs if clean_text(p)]
    if len(paragraphs) >= 5:
        return paragraphs

    word_one = vocab_words[0] if vocab_words else "tool"
    word_two = vocab_words[1] if len(vocab_words) > 1 else word_one
    normalized_objective = clean_text(objective).rstrip(".")

    if course_level(course_key) == "A2":
        expanded = [
            f"{paragraphs[0]} The reading introduces the workplace, the people involved, and the main task in simple language.",
            f"Before the routine continues, the student notices words such as {word_one} and {word_two}. These words are important because they explain what is used, what is checked, and what should happen next.",
            f"{paragraphs[1]} The actions appear in a clear order so the reader can follow the procedure without losing the main idea.",
            "While reading, the student identifies the purpose of each action, the safety detail, and the result of the task. This helps the class connect vocabulary with real workshop decisions.",
            f"{paragraphs[2]} By the end of the text, the reader can explain the routine, justify one decision, and connect the lesson objective with {normalized_objective.lower()}.",
        ]
    else:
        expanded = [
            f"{paragraphs[0]} The text frames the situation as part of a real professional pathway or technical routine in {course_label}.",
            f"Before the central action is completed, the reader must interpret terms such as {word_one} and {word_two} in context. These references matter because they signal tools, systems, or evidence that support later decisions.",
            f"{paragraphs[1]} Rather than listing actions only, the passage shows how procedure, evidence, and responsibility are connected in professional work.",
            "A key part of the reading is the way the professional explains results, reports a difficulty, or justifies a choice. This is where technical English moves from isolated vocabulary to professional communication.",
            f"{paragraphs[2]} The closing idea links the routine to {normalized_objective.lower()}, showing why English supports accuracy, safety, and career development.",
        ]

    return expanded[:5]