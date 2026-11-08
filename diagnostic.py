"""
Universal Vehicle Diagnostic System
Version 0.1

Initial software foundation.
"""

class VehicleDiagnosticSystem:

    def __init__(self):
        self.vehicle = None
        self.connected = False

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


if __name__ == "__main__":
    diagnostic = VehicleDiagnosticSystem()
    print("Universal Vehicle Diagnostic System")
    print("Software foundation ready.")
