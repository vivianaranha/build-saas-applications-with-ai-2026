def run_bounded_agent(tool_name, allowed_tools, requires_approval=False, approved=False):
    if tool_name not in allowed_tools:
        return {"status":"blocked","reason":"tool_not_allowed"}
    if requires_approval and not approved:
        return {"status":"approval_required"}
    return {"status":"executed","tool":tool_name}
