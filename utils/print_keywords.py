def print_parsed_jd(parsed):
    def safe_list(value):
        return value if isinstance(value, list) else []

    print("\n=== JD PARSED OUTPUT ===")
    print("Role Title:", getattr(parsed, "role_title", None))
    print("Summary:", getattr(parsed, "summary", None))

    sections = {
        "Hard Skills": safe_list(getattr(parsed, "hard_skills", [])),
        "Soft Skills": safe_list(getattr(parsed, "soft_skills", [])),
        "Tools / Technologies": safe_list(getattr(parsed, "tools", [])),
        "Responsibilities": safe_list(getattr(parsed, "responsibilities", [])),
        "Domain Keywords": safe_list(getattr(parsed, "domain_keywords", [])),
        "Nice to Have": safe_list(getattr(parsed, "nice_to_have", [])),
    }

    for title, items in sections.items():
        print(f"\n{title}:")
        for item in items:
            print("-", item)

    print("\nExperience Level:", getattr(parsed, "experience_level", None))


# ANSI color codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def pretty_print(obj, indent=0):
    """Recursively pretty-print dicts, Pydantic models, and lists with colors."""
    prefix = " " * indent

    # 1. If it's a Pydantic model → convert to dict
    if hasattr(obj, "model_dump"):
        obj = obj.model_dump()

    # 2. If it's a dict → print keys and recurse
    if isinstance(obj, dict):
        for key, value in obj.items():
            print(f"{prefix}{CYAN}{key}:{RESET}")
            pretty_print(value, indent + 4)
        return

    # 3. If it's a list → print each item
    if isinstance(obj, list):
        if not obj:
            print(f"{prefix}{YELLOW}- []{RESET}")
        else:
            for item in obj:
                print(f"{prefix}{YELLOW}- {RESET}", end="")
                # If item is simple, print inline
                if isinstance(item, (str, int, float)):
                    print(f"{GREEN}{item}{RESET}")
                else:
                    print()
                    pretty_print(item, indent + 4)
        return

    # 4. Base case → simple value
    print(f"{prefix}{GREEN}{obj}{RESET}")
