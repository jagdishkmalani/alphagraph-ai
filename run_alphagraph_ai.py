from utils.pretty_print import pretty_print
from dotenv import load_dotenv
load_dotenv()

from graph.graph import build_graph

def main():
    ticker = "NVDA" #input("Enter ticker: ").strip()

    initial_state = {
        "ticker": ticker,
        "errors": []
    }

    graph = build_graph()
    result = graph.invoke(initial_state)
    #result = build_graph.invoke(initial_state)
    #pretty_print(result)
    pretty_print(result["llm_output"])
    #print(result)

if __name__ == "__main__":
    main()

