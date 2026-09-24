LAST_NAME = "ANONUEVO"
SEED_NUM = 9
FAVORITE_ARTIST = "NIK MAKINO" 

def generate_fault_code():
    code = (len(LAST_NAME) * SEED_NUM) + len(FAVORITE_ARTIST)
    return code

def trace_fault_recursive(fault_level, call_count=0):
    call_count += 1
    print(f"[TRACE Step {call_count}]: Analyzing Fault Level Code -> {fault_level}")
    
    if fault_level <= 5:
        print("[BASE CONDITION MET]: Fault localized and isolated successfully.")
        return call_count, fault_level
    
    return trace_fault_recursive(fault_level // 2, call_count)

if __name__ == "__main__":
    print("=" * 50)
    print("2. RECURSIVE FAULT TRACE")
    print("=" * 50)
    initial_fault = generate_fault_code()
    print(f"Generated Initial Fault Code ({LAST_NAME}/{FAVORITE_ARTIST}): {initial_fault}\n")
    
    total_calls, final_code = trace_fault_recursive(initial_fault)
    
    print("\n--- FAULT TRACE SUMMARY ---")
    print(f"Total Recursive Calls Performed: {total_calls}")
    print(f"Final Resolved Code: {final_code}")
    print("=" * 50)