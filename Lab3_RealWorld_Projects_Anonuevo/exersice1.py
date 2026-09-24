LAST_NAME = "ANONUEVO"
SEED_NUM = 9
FAVORITE_ARTIST = "NIK MAKINO"

def process_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG]: Executing diagnostic process '{func.__name__}'...")
        return func(*args, **kwargs)
    return wrapper

def generate_equipment_data():
    base_val = len(LAST_NAME) * SEED_NUM
    readings = [
        base_val * 1.5,
        base_val * 2.2,
        "INVALID_ENTRY",
        base_val * 0.8,
        len(FAVORITE_ARTIST) * 10
    ]
    return readings

def validate_readings(readings):
    valid = []
    for r in readings:
        try:
            val = float(r)
            valid.append(val)
        except (ValueError, TypeError):
            print(f"[WARNING]: Dropped invalid reading entry -> '{r}'")
    return valid

@process_logger
def calculate_metrics(valid_readings):
    avg_reading = sum(valid_readings) / len(valid_readings)
    return round(avg_reading, 2)

def classify_condition(avg_reading):
    if avg_reading > 80:
        return "CRITICAL OVERLOAD"
    elif avg_reading > 50:
        return "OPTIMAL OPERATIONAL STATUS"
    else:
        return "LOW POWER STAGE"

if __name__ == "__main__":
    print("=" * 50)
    print("1. EQUIPMENT DIAGNOSTIC SYSTEM")
    print("=" * 50)
    raw_data = generate_equipment_data()
    print("Generated Equipment Data:", raw_data)
    
    valid_data = validate_readings(raw_data)
    print("Validation Results (Valid Entries):", valid_data)
    
    avg_metric = calculate_metrics(valid_data)
    status = classify_condition(avg_metric)
    
    print("\n--- FINAL DIAGNOSTIC SUMMARY ---")
    print(f"Student Operator: {LAST_NAME} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}")
    print(f"Processed Average Metric: {avg_metric}")
    print(f"Equipment Status: {status}")
    print("=" * 50)