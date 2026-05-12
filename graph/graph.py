from langgraph.graph             import StateGraph, END
from state.state                 import AlphagraphState
from nodes.input_validation_node import input_validation_node
from nodes.market_data_node      import market_data_node
from nodes.news_retrieval_node   import news_retrieval_node
#from nodes.analysis_node         import analysis_node
from nodes.analysis_lcel_node    import analysis_node

def build_graph():
    builder = StateGraph(AlphagraphState)

    # Nodes
    builder.add_node("input_validation"                     , input_validation_node)
    builder.add_node("market_data"                          , market_data_node)
    builder.add_node("news_retrieval"                       , news_retrieval_node)
    builder.add_node("analysis"                             , analysis_node)

    builder.set_entry_point("input_validation")

    # Flow: input_validation → market_data
    builder.add_edge("input_validation"     , "market_data")
    builder.add_edge("market_data"          , "news_retrieval")
    builder.add_edge("news_retrieval"       , "analysis")

    return builder.compile()
