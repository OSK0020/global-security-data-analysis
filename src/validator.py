def validate_record(record):
    # Ensure record has required security fields
    return "id" in record and "threat_level" in record
