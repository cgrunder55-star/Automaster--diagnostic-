
"""
AutoDiagPro - OBD Fault Code Database
Version 1.0
"""

OBD_CODES = {
    "P0100": {
        "description": "Mass Air Flow Sensor Circuit Malfunction",
        "possible_causes": [
            "Faulty MAF sensor",
            "Damaged wiring",
            "Loose electrical connector",
            "Air intake leak"
        ],
        "tests": [
            "Inspect MAF wiring and connector",
            "Check sensor power and ground",
            "Check live MAF readings",
            "Inspect air intake system"
        ]
    },

    "P0101": {
        "description": "Mass Air Flow Sensor Range/Performance",
        "possible_causes": [
            "Dirty MAF sensor",
            "Air leak",
            "Blocked air filter",
            "Faulty MAF sensor"
        ],
        "tests": [
            "Inspect air filter",
            "Check intake pipes for leaks",
            "Compare live MAF readings with specifications"
        ]
    },

    "P0110": {
        "description": "Intake Air Temperature Sensor Circuit",
        "possible_causes": [
            "Faulty IAT sensor",
            "Open circuit",
            "Short circuit",
            "Damaged connector"
        ],
        "tests": [
            "Check sensor wiring",
            "Check reference voltage where applicable",
            "Check sensor resistance against specifications",
            "Compare live temperature readings"
        ]
    },

    "P0120": {
        "description": "Throttle Position Sensor Circuit",
        "possible_causes": [
            "Faulty throttle position sensor",
            "Wiring damage",
            "Poor ground",
            "Connector corrosion"
        ],
        "tests": [
            "Inspect throttle wiring",
            "Check power and ground",
            "Monitor throttle position live data",
            "Check signal voltage"
        ]
    },

    "P0171": {
        "description": "System Too Lean Bank 1",
        "possible_causes": [
            "Vacuum leak",
            "Low fuel pressure",
            "Dirty fuel injectors",
            "MAF sensor fault"
        ],
        "tests": [
            "Check fuel pressure",
            "Perform intake smoke test",
            "Inspect fuel trims",
            "Check MAF readings"
        ]
    },

    "P0201": {
        "description": "Injector Circuit Cylinder 1",
        "possible_causes": [
            "Faulty injector",
            "Damaged injector wiring",
            "ECU driver fault",
            "Poor electrical connection"
        ],
        "tests": [
            "Check injector resistance",
            "Inspect injector connector",
            "Check injector control pulse",
            "Test wiring continuity"
        ]
    },

    "P0300": {
        "description": "Random Multiple Cylinder Misfire",
        "possible_causes": [
            "Ignition system fault",
            "Fuel delivery problem",
            "Low compression",
            "Air leak"
        ],
        "tests": [
            "Check misfire counters",
            "Inspect spark plugs and coils",
            "Check fuel pressure",
            "Perform compression test"
        ]
    },

    "P0335": {
        "description": "Crankshaft Position Sensor Circuit",
        "possible_causes": [
            "Faulty crankshaft sensor",
            "Damaged wiring",
            "Incorrect sensor air gap",
            "Trigger wheel damage"
        ],
        "tests": [
            "Inspect sensor wiring",
            "Check sensor supply where applicable",
            "Check crankshaft signal with oscilloscope",
            "Inspect trigger wheel"
        ]
    },

    "P0340": {
        "description": "Camshaft Position Sensor Circuit",
        "possible_causes": [
            "Faulty camshaft sensor",
            "Damaged wiring",
            "Poor connector contact",
            "Timing system problem"
        ],
        "tests": [
            "Check sensor wiring",
            "Check power and ground",
            "Inspect camshaft signal",
            "Compare camshaft and crankshaft signals"
        ]
    },

    "P0420": {
        "description": "Catalyst System Efficiency Below Threshold Bank 1",
        "possible_causes": [
            "Worn catalytic converter",
            "Exhaust leak",
            "Faulty oxygen sensor",
            "Engine running incorrectly"
        ],
        "tests": [
            "Check exhaust for leaks",
            "Inspect oxygen sensor readings",
            "Check fuel trims",
            "Evaluate catalyst efficiency"
        ]
    },

    "P0500": {
        "description": "Vehicle Speed Sensor Malfunction",
        "possible_causes": [
            "Faulty speed sensor",
            "Damaged wiring",
            "ABS signal problem",
            "Connector damage"
        ],
        "tests": [
            "Inspect sensor wiring",
            "Check live vehicle speed data",
            "Inspect ABS wheel speed signals",
            "Check sensor supply and signal"
        ]
    },

    "P0562": {
        "description": "System Voltage Low",
        "possible_causes": [
            "Weak battery",
            "Alternator fault",
            "Poor battery connections",
            "Charging circuit fault"
        ],
        "tests": [
            "Test battery voltage",
            "Test charging voltage",
            "Check alternator output",
            "Inspect battery cables and grounds"
        ]
    }
}


def lookup_code(code):
    code = code.strip().upper()

    result = OBD_CODES.get(code)

    if result is None:
        return {
            "code": code,
            "description": "Code not yet in database",
            "possible_causes": [],
            "tests": ["Consult vehicle-specific service information"]
        }

    return {
        "code": code,
        **result
    }


if __name__ == "__main__":
    print("AutoDiagPro Fault Code Database")
    print("Enter EXIT to close.")

    while True:
        code = input("\nEnter fault code: ").strip()

        if code.upper() == "EXIT":
            break

        result = lookup_code(code)

        print("\nDescription:", result["description"])

        print("\nPossible causes:")
        for cause in result["possible_causes"]:
            print("-", cause)

        print("\nRecommended tests:")
        for test in result["tests"]:
            print("-", test)
