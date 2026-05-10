"""
run_resume_match_rewrite.py

Entry point for the Resume–JD Matching and Grounded Resume Refinement Engine.
This script initializes the LangGraph workflow, loads the required nodes,
and runs the full pipeline including:

- JD parsing
- ATS scoring
- Critique generation
- Grounded resume rewriting
- Reflexion-based iterative improvement
- Final structured output

Usage:
    python run_resume_match_rewrite.py
"""

from graph.main_graph            import build_resume_graph
from utils.print_keywords        import pretty_print
from utils.safe_read_text_file   import safe_read_text_file

graph = build_resume_graph()

resume      = safe_read_text_file("C:\LangChain\Resumes\JMResume.txt")
sample_jd   = safe_read_text_file("C:\LangChain\JobDescriptions\JD1.txt")

initial_state = {
    "resume":           resume,
    "job_description":  sample_jd
}

#print("STATE KEYS:", initial_state.keys()) # For debugging

result = graph.invoke(initial_state)

print("=================== Reflexion method ==============================================")

print("=================== Print the final state ===============================")
# ANSI color codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
Magenta	= "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

#print(f"{BOLD}{RED}  parsed_jd {RESET}")
#pretty_print(result['parsed_jd'])

print(f"{BOLD}{RED} ================ parsed_resume ================ {RESET}")
#pretty_print(result['parsed_resume'])

print(f"{BOLD}{RED} ================ ats_score ================ {RESET}")
pretty_print(result['ats_score'])

print(f"{BOLD}{RED} ================ rewritten_resume ================ {RESET}")
#pretty_print(result['rewritten_resume'])

"""
print("=================== With Structured Ouptput for testing ==============================")
resume = extract_keywords(resume)
print_parsed_jd(resume)
print("************************************************************************************")
"""
