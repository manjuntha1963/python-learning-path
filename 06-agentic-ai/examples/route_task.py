# Purpose: Show how to route tasks to different agents.
# In multi-agent systems, a router decides which agent handles each task.

def route_task(task: str) -> str:
    """
    Analyze a task and decide which agent should handle it.
    
    Returns:
        The name of the best agent for this task
    """
    # Convert to lowercase to ignore capitalization
    task_lower = task.lower()
    
    # Route tasks containing "search" to the research agent
    if "search" in task_lower:
        return "research-agent"
    
    # Route tasks containing "write" to the writing agent
    if "write" in task_lower:
        return "writing-agent"
    
    # All other tasks go to the general agent
    return "general-agent"


# Test the router with different tasks
test_tasks = [
    "search the documents",
    "write an email",
    "find information about Python",
    "create a summary",
    "answer my question",
]

print("Task Routing Examples:")
print()

for task in test_tasks:
    # Determine which agent should handle this task
    assigned_agent = route_task(task)
    print(f"Task: '{task}'")
    print(f"  → Assigned to: {assigned_agent}")
    print()

print("In production, each agent has specialized skills and tools.")
print("The router ensures tasks reach the most capable agent.")
