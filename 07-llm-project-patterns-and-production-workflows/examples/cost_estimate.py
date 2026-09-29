# Purpose: Calculate the cost of using an LLM API.
# Token pricing is the primary cost model for most LLM providers.

def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    input_rate: float,
    output_rate: float
) -> float:
    """
    Calculate the cost of an LLM API call.
    
    Args:
        input_tokens: Number of tokens in the user's question
        output_tokens: Number of tokens in the model's response
        input_rate: Price per 1 million input tokens (in dollars)
        output_rate: Price per 1 million output tokens (in dollars)
    
    Returns:
        Total cost in dollars for this API call
    
    Example:
        OpenAI GPT-4 input: $0.03/1M tokens
        OpenAI GPT-4 output: $0.06/1M tokens
        For 1000 input tokens and 500 output tokens:
        Cost = (1000/1,000,000)*0.03 + (500/1,000,000)*0.06
             = 0.000003 + 0.00003 = $0.000033
    """
    # Calculate input cost
    # Divide by 1,000,000 because prices are per million tokens
    input_cost = (input_tokens / 1_000_000) * input_rate
    
    # Calculate output cost
    output_cost = (output_tokens / 1_000_000) * output_rate
    
    # Return the total cost
    total_cost = input_cost + output_cost
    return total_cost


# Example 1: Small API call
print("Cost Example 1: Small question")
input_tokens = 1000
output_tokens = 500
input_rate = 1.0  # $1.00 per 1M tokens
output_rate = 2.0  # $2.00 per 1M tokens

cost = estimate_cost(input_tokens, output_tokens, input_rate, output_rate)
print(f"  Input tokens: {input_tokens}")
print(f"  Output tokens: {output_tokens}")
print(f"  Cost: ${cost:.6f} (about 0.003 cents)")
print()

# Example 2: Larger API call
print("Cost Example 2: Larger question with longer response")
input_tokens = 5000
output_tokens = 2000
input_rate = 0.5  # $0.50 per 1M tokens
output_rate = 1.5  # $1.50 per 1M tokens

cost = estimate_cost(input_tokens, output_tokens, input_rate, output_rate)
print(f"  Input tokens: {input_tokens}")
print(f"  Output tokens: {output_tokens}")
print(f"  Cost: ${cost:.6f}")
print()

print("Production tip: Cache common questions to reduce costs.")
print("Use cheaper models for simple tasks, expensive models only when needed.")
