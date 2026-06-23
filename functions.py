import argparse

def validate_port(value: str) -> int:
    try:
        port = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"argument -p: invalid value: {value} (Provide an integer value from 0 to 65535.)")
    
    if port < 0 or port > 65535:
        raise argparse.ArgumentTypeError(f"argument -p: invalid value: {value} (Provide an integer value from 0 to 65535.)")
    
    return port

def validate_count(value: str) -> int | float:
    try:
        count = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"argument -c: invalid value: {value} (Provide an integer value greater than or equal to 0.)")
    
    if count < 0:
        raise argparse.ArgumentTypeError(f"argument -c: invalid value: {value} (Provide an integer value greater than or equal to 0.)")
    if count == 0:
        return float('inf')
        
    return count

def validate_size(value: str) -> int:
    try:
        size = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"argument -s: invalid value: {value} (Provide an integer value from 1 to 65535.)")
    
    if size < 1 or size > 65535:
        raise argparse.ArgumentTypeError(f"argument -s: invalid value: {value} (Provide an integer value from 1 to 65535.)")
    
    return size

def validate_interval(value: str) -> float:
    try:
        interval = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"argument -i: invalid value: {value} (Provide a float value greater than or equal to 0.)")
    
    if interval < 0:
        raise argparse.ArgumentTypeError(f"argument -i: invalid value: {value} (Provide a float value greater than or equal to 0.)")
        
    return interval