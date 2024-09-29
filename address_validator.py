# address_validator.py
import re

class AddressValidator:
    def __init__(self):
        # A simple dictionary for address to pin mapping
        self.address_pin_map = {
            "New York": "10001",
            "Los Angeles": "90001",
            "Chicago": "60601"
            # Add more city-pin mappings as required
        }
    
    def extract_address_pin(self, text):
        # Extract address and pin using regex
        address_pattern = r"Address: ([\w\s]+)"
        pin_pattern = r"PIN: (\d+)"
        
        address_match = re.search(address_pattern, text)
        pin_match = re.search(pin_pattern, text)

        address = address_match.group(1) if address_match else None
        pin = pin_match.group(1) if pin_match else None

        return address, pin

    def validate_pin(self, address, pin):
        # Check if the pin matches the address in the map
        correct_pin = self.address_pin_map.get(address)
        if correct_pin and correct_pin != pin:
            print(f"Correcting PIN for {address}: {pin} -> {correct_pin}")
            return correct_pin
        return pin
