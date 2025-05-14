from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableConfig

from tools.static_scanner import static_rule_check
from tools.gpt_explainer import GPTExplainerTool
from tools.report_formatter import ReportFormatterTool

def static_scan_node(state: dict) -> dict:
    code = state.get("code", "")
    state["static_results"] = static_rule_check(code)
    return state

def gpt_explainer_node(state: dict) -> dict:
    code = state.get("code", "")
    state["gpt_response"] = GPTExplainerTool()._run(code)
    return state

def report_formatter_node(state: dict) -> dict:
    state["report"] = ReportFormatterTool()._run(state)
    return state

graph = StateGraph()
graph.add_node("StaticScan", static_scan_node)
graph.add_node("GPTExplainer", gpt_explainer_node)
graph.add_node("ReportFormatter", report_formatter_node)

graph.set_entry_point("StaticScan")
graph.set_edges("StaticScan", "GPTExplainer")
graph.set_edges("GPTExplainer", "ReportFormatter")

graph_executor = graph.compile()

def run_langgraph_agent(code_input: str) -> dict:
    return graph_executor.invoke({"code": code_input}, config=RunnableConfig())