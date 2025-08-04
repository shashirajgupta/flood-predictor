# agents/field_support_agent.py

def report_status(location, status_message):
    """
    Logs and formats a status report from field support.
    
    Args:
        location (str): The area or village name
        status_message (str): Message like "10 people evacuated", "road blocked"
    Returns:
        str: Confirmation response
    """
    # For now, just print/log (you can later save to a file or database)
    report = f"[📍 {location}] STATUS UPDATE: {status_message}"
    print(report)
    
    # You can also send this to an alert email or chatbot log
    return f"✅ Report received for {location}: {status_message}"
