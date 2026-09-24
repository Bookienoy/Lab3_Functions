import telemetry_generator as tg
import pipeline_analytics as pa

LAST_NAME = "ANONUEVO"
SEED_NUM = 9
FAVORITE_ARTIST = "NIK MAKINO"

if __name__ == "__main__":
    print("=" * 50)
    print("3. INTELLIGENT EQUIPMENT MONITORING PIPELINE")
    print("=" * 50)
    
    stream = tg.stream_telemetry(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    
    valid_readings, invalid_count = pa.process_stream(stream)
    
    abnormal_count = 0
    print("\n--- ABNORMALITY ANALYSIS ---")
    for r in valid_readings:
        if r > 100:
            abnormal_count += 1
            pa.recursive_abnormal_trace(r)
            
    print("\n--- FINAL DIAGNOSTIC REPORT ---")
    print(f"Student: {LAST_NAME} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}")
    print(f"Total Processed Readings: {len(valid_readings) + invalid_count}")
    print(f"Valid Readings: {len(valid_readings)} | Invalid Readings: {invalid_count}")
    print(f"Detected Abnormal Conditions: {abnormal_count}")
    print(f"Overall Status: {'ATTENTION REQUIRED' if abnormal_count > 0 else 'SYSTEM NORMAL'}")
    print("=" * 50)