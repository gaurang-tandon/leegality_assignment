import local_settings as settings

class ParkingLot:
    def __init__(self):
        self.levels = {
            'A': [None] * settings.PARKING_LEVEL_LIMITS,
            'B': [None] * settings.PARKING_LEVEL_LIMITS,
        }
        self.vehicle_map = {}

    def assign_parking_space(self, vehicle_number):
        for level in ['A', 'B']:
            for spot_number in range(settings.PARKING_LEVEL_LIMITS):
                if not self.levels[level][spot_number]:
                    self.levels[level][spot_number] = vehicle_number
                    self.vehicle_map[vehicle_number] = (level, spot_number + 1)
                    return {
                        "level": level,
                        "spot": spot_number + 1
                    }
        return "Parking lot is full."

    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.vehicle_map:
            level, spot = self.vehicle_map[vehicle_number]
            return {
                "level": level,
                "spot": spot
            }
        else:
            return "Vehicle not found in the parking lot."
    

def main():
    parking_lot = ParkingLot()
    while True:
        print("\n1. Assign a parking space to a new vehicle")
        print("2. Retrieve parking spot of a particular vehicle")
        print("3. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            vehicle_number = input("Enter the vehicle number: ")
            result = parking_lot.assign_parking_space(vehicle_number)
            print(result)
        elif choice == '2':
            vehicle_number = input("Enter the vehicle number: ")
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            print(result)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()