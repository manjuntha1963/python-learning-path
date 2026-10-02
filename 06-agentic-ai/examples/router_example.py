# Module 06 example: router logic for agentic AI
# This demonstrates how one system can route tasks to different specialized agents


def route_task(task):
    task_lower = task.lower()

    if "search" in task_lower:
        return "research-agent"
    if "write" in task_lower:
        return "writing-agent"
    return "general-agent"


print(route_task("search the web"))
print(route_task("write a summary"))
print(route_task("answer a question"))
