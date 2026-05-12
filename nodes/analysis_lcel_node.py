from state.state                        import AlphagraphState
from tools.run_analysis_llm             import run_analysis_llm
import json
from langchain_core.output_parsers      import PydanticOutputParser
from schemas.analysis_schema            import analysis_schema
from langchain_core.prompts             import ChatPromptTemplate
from langchain_openai                   import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

def analysis_node(state: AlphagraphState) -> AlphagraphState:
    llm = ChatOpenAI(
        model="gpt-4.1-mini",   # deterministic model
        temperature=0.2
    )


    analysis_parser     = PydanticOutputParser(pydantic_object=analysis_schema)
    format_instructions = analysis_parser.get_format_instructions()

    SYSTEM_PROMPT       = "You are a financial analyst. Your job is to analyze the market data and news. "
    HUMAN_PROMPT        = """
                        TICKER:
                        {ticker}

                        MARKET DATA:
                        {market_data}

                        NEWS DATA:
                        {news_data}

                        {format_instructions}
                        """
    
    #print(SYSTEM_PROMPT)    
    #print(HUMAN_PROMPT)    
    analysis_prompt = ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT),("human", HUMAN_PROMPT)])
    analysis_prompt = analysis_prompt.partial(format_instructions=format_instructions)
    analysis_chain  = analysis_prompt | llm | analysis_parser

    analysis = analysis_chain.invoke({
            "ticker": state.get("ticker"),
            "market_data": state.get("market_data"),
            "news_data": state.get("news_data"),
            "format_instructions": analysis_parser.get_format_instructions()
        })    

    try:
        analysis_json = json.loads(analysis)
    except:
        analysis_json = {"raw_output": analysis}

    return {"llm_output": analysis_json}
