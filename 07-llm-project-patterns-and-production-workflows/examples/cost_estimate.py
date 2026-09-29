def estimate_cost(input_tokens: int, output_tokens: int, input_rate: float, output_rate: float) -> float:
    return (input_tokens / 1_000_000) * input_rate + (output_tokens / 1_000_000) * output_rate


print(estimate_cost(1000, 500, 1.0, 2.0))
