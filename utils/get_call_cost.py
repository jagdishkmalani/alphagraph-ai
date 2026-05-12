def get_call_cost(response, model="gpt-5.4"):
    # Current Pricing per 1M tokens
    pricing = {
        "gpt-5.4": {"input": 2.50, "output": 15.00, "cache": 0.25},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60, "cache": 0.015}
    }
    
    usage = response.usage
    rates = pricing.get(model)
    
    # Check for cached tokens (which are 90% cheaper on GPT-5.4)
    cached_tokens = getattr(usage.prompt_tokens_details, 'cached_tokens', 0)
    standard_prompt_tokens = usage.prompt_tokens - cached_tokens
    
    input_cost = (standard_prompt_tokens / 1_000_000) * rates['input']
    cache_cost = (cached_tokens / 1_000_000) * rates['cache']
    output_cost = (usage.completion_tokens / 1_000_000) * rates['output']
    
    total_cost = input_cost + cache_cost + output_cost
    print(f"Total Cost: {total_cost}")
    #return f"${total_cost:.6f}"

# Example usage:
# print(f"This call cost: {get_call_cost(response)}")