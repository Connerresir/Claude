def check_consequences(action, params):
    risky_keywords = ["delete", "remove", "destroy", "shutdown", "reboot"]
    for keyword in risky_keywords:
        if keyword in action.lower():
            return f"Warning: The action '{action}' with parameters '{params}' may have unintended consequences. Are you sure you want to proceed?"
    return None
