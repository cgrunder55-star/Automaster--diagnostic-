
"""
AutoDiagPro
Universal Vehicle Diagnostic System
Version 0.2
"""

from obd_codes import lookup_code


class VehicleDiagnosticSystem:

    def __init__(self):
        self.vehicle = None
        self.connected = False
        self.fault_codes = []

    def identify_vehicle(self, make, model, year):
        self.vehicle = {
            "make": make,
            "model": model,
            "year": year
        }
        return self.vehicle

    def connection_status(self):
        return self.connected

    def get_vehicle(self):
        return self.vehicle

    def set_connection(self, status):
        self.connected = bool(status)
        return self.connected

    def diagnose_fault(self, code):
        result = lookup_code(code)
        self.fault_codes.append(result)
        return result

    def get_fault_history(self):
        return self.fault_codes

    def clear_fault_history(self):
        self.fault_codes.clear()
        return True


if __name__ == "__main__":

    diagnostic = VehicleDiagnosticSystem()

    print("================================")
    print("       AutoDiagPro")
    print(" Universal Vehicle Diagnostics")
    print("================================")

    diagnostic.identify_vehicle(
        "Toyota", "Hilux", 2018
    )

    print("\nVehicle:", diagnostic.get_vehicle())

    code = input("\nEnter fault code: ")

    result = diagnostic.diagnose_fault(code)

    print("\nFault:", result["code"])
    print("Description:", result["description"])

    print("\nPossible causes:")
    for cause in result["possible_causes"]:
        print("-", cause)

    print("\nRecommended tests:")
    for test in result["tests"]:
        print("-", test)
