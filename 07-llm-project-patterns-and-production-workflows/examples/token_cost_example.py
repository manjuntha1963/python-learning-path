# Module 07 example: compute LLM token-based pricing
# This shows how cost is estimated based on token counts


def estimate_price(input_tokens, output_tokens, input_rate, output_rate):
    input_cost = (input_tokens / 1_000_000) * input_rate
    output_cost = (output_tokens / 1_000_000) * output_rate
    total = input_cost + output_cost
    return total


print(estimate_price(1000, 500, 0.03, 0.06))
