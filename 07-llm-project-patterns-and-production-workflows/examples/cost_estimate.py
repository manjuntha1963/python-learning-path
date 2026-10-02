# Purpose: Calculate the cost of using an LLM API.
# Token pricing is the primary cost model for most LLM providers.

# This function calculates the total API cost using:
# - input token count
# - output token count
# - input token rate
# - output token rate
#
# Why divide by 1,000,000?
# Because LLM providers usually quote prices per 1 million tokens.
# If the call uses 1000 tokens, then 1000 / 1,000,000 is the fraction of a million tokens used.
# Then we multiply by the rate to get the actual cost.


def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    input_rate: float,
    output_rate: float
) -> float:
    """
    Calculate the cost of an LLM API call.

    Args:
        input_tokens: Number of tokens in the user's question or prompt.
        output_tokens: Number of tokens in the model's response.
        input_rate: Cost per 1 million input tokens, in dollars.
        output_rate: Cost per 1 million output tokens, in dollars.

    Returns:
        Total cost in dollars for the request.

    Example:
        If input_tokens = 1000 and output_tokens = 500,
        with rates input_rate = 0.03 and output_rate = 0.06,
        then cost = (1000 / 1_000_000) * 0.03 + (500 / 1_000_000) * 0.06
    """
    # Calculate the cost of the input portion of the request
    # For example, a prompt of 1000 tokens uses 0.001 of 1 million tokens
    input_cost = (input_tokens / 1_000_000) * input_rate

    # Calculate the cost of the model's generated response
    # This follows the same token-based pricing model
    output_cost = (output_tokens / 1_000_000) * output_rate

    # Add both parts together to get the total request cost
    total_cost = input_cost + output_cost

    # Return the final cost as a float (decimal value)
    return total_cost


# Example 1: Small API call
print("Cost Example 1: Small question")
input_tokens = 1000
output_tokens = 500
input_rate = 1.0
output_rate = 2.0

# Compute the final cost for this example
cost = estimate_cost(input_tokens, output_tokens, input_rate, output_rate)
print(f"Input tokens: {input_tokens}")
print(f"Output tokens: {output_tokens}")
print(f"Cost: ${cost:.6f}")
print()

# Example 2: Larger request
print("Cost Example 2: Larger request")
input_tokens = 5000
output_tokens = 2000
input_rate = 0.5
output_rate = 1.5

cost = estimate_cost(input_tokens, output_tokens, input_rate, output_rate)
print(f"Input tokens: {input_tokens}")
print(f"Output tokens: {output_tokens}")
print(f"Cost: ${cost:.6f}")
print()

# Production note:
# In real systems, people track total cost for each request and add:
# - caching
# - rate limiting
# - request size limits
# - better prompts
# - smaller model choices for simple tasks
print("Production tip: Use caching and cheaper models for low-risk tasks.")
