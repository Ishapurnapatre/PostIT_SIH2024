# main.py
from ocr_reader import OCRReader
from address_validator import AddressValidator
from database import DatabaseManager
from distribution_optimizer import DistributionOptimizer

def main():
    # Step 1: Extract text from the image using OCR
    ocr = OCRReader("letter_image.jpg")
    letter_text = ocr.extract_text()
    if not letter_text:
        print("No text found, exiting...")
        return

    # Step 2: Validate and correct address and pin code
    validator = AddressValidator()
    address, pin = validator.extract_address_pin(letter_text)
    
    if not address or not pin:
        print("Could not extract address or PIN, exiting...")
        return
    
    correct_pin = validator.validate_pin(address, pin)

    # For demonstration purposes, assume sender and receiver data are static or extracted similarly
    sender = "John Doe"
    receiver = "Jane Smith"
    
    # Step 3: Insert the data into the database
    db_manager = DatabaseManager()
    db_manager.insert_letter(sender, receiver, address, correct_pin)
    
    # Step 4: Retrieve all letters from the database for distribution
    all_letters = db_manager.get_all_letters()
    
    # Step 5: Optimize distribution
    optimizer = DistributionOptimizer(all_letters)
    optimized_distribution = optimizer.optimize_distribution()
    
    # Output the optimized distribution
    for letter, cluster in optimized_distribution:
        print(f"Letter {letter} is assigned to cluster {cluster}")
    
    # Close the database connection
    db_manager.close()

if __name__ == "__main__":
    main()
