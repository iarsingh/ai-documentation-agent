TOOLS = ["outline", "draft"]
WRITES = ("publish", "overwrite",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    result = payload.get("headings") or []
    return {"refused": False, "tools": TOOLS, "outline": result, "wrote": False, "applied": False}
