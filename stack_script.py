class ParkingLot:
    def __init__(self):
        self.license_plate_stack = []

    def add_plate(self, plate):
        self.license_plate_stack.append(plate)
        print(f"Plate {plate} added to the parking lot.")

    def remove_plate(self):
        if self.is_empty():
            print("Parking lot is empty. No plates to remove.")
        else:
            plate = self.license_plate_stack.pop()
            print(f"Plate {plate} removed from the parking lot.")
            return plate

    def find_plate(self, plate):
        if plate in self.license_plate_stack:
            position = self.license_plate_stack.index(plate)
            print(f"Plate {plate} found at position {position}.")
            return position
        else:
            print(f"Plate {plate} not found in the parking lot.")
            return -1

    def is_empty(self):
        return len(self.license_plate_stack) == 0

    def plate_count(self):
        return len(self.license_plate_stack)

    def display_plates(self):
        if self.is_empty():
            print("Parking lot is empty.")
        else:
            print("Plates in the parking lot:")
            for plate in self.license_plate_stack:
                print(plate)

# Example usage
parking_lot = ParkingLot()
parking_lot.add_plate("XYZ-6789")
parking_lot.add_plate("AAA-0101")
parking_lot.display_plates()
parking_lot.find_plate("AAA-0101")
parking_lot.remove_plate()
parking_lot.display_plates()
parking_lot.plate_count()
parking_lot.is_empty()
