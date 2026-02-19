from langgraph.graph import StateGraph, START,END
from typing import TypedDict,List,Optional
from main.main_graph import *




class AssistantState(TypedDict):
    question:str
    plan:str
    research_notes:str
    verified_output:str
    summary:str
    final_answer:str
    

new_graph=StateGraph(AssistantState)


new_graph.add_node("planner",Planner)
new_graph.add_node("researcher",Researcher)
new_graph.add_node("verifier",Verifier)
new_graph.add_node("summarizer",Summarizer)
new_graph.add_node("finalizer",Finalizer)




new_graph.set_entry_point("planner")
new_graph.add_edge("planner","researcher")
new_graph.add_edge("researcher","verifier")
new_graph.add_edge("verifier","summarizer")
new_graph.add_edge("summarizer","finalizer")
new_graph.add_edge("finalizer",END)






    