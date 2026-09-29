def route_task(task: str) -> str:
    if "search" in task.lower():
        return "research-agent"
    if "write" in task.lower():
        return "writing-agent"
    return "general-agent"


print(route_task("search the documents"))
