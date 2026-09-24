def monitor_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[MONITOR]: Processing pipeline operation '{func.__name__}'...")
        return func(*args, **kwargs)
    return wrapper

@monitor_decorator
def process_stream(stream_generator):
    valid_data = []
    invalid_count = 0
    
    scale_op = lambda x: round(x * 1.05, 2)
    
    for item in stream_generator:
        try:
            val = float(item)
            scaled = scale_op(val)
            valid_data.append(scaled)
        except (ValueError, TypeError):
            invalid_count += 1
            
    return valid_data, invalid_count

def recursive_abnormal_trace(value, depth=1):
    if value <= 50:
        print(f"  [RECURSIVE TRACE Depth {depth}]: Value stabilized at {value}")
        return depth
    print(f"  [RECURSIVE TRACE Depth {depth}]: High abnormal value detected ({value}), damping...")
    return recursive_abnormal_trace(value - 30, depth + 1)