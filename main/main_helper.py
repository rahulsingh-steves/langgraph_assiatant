from main.main_llm import llm_intake


def Planner(state):
    question=state['question']
    prompt=f"""
    You are an expert assistant.Given the question below or query , provide a detailed plan to help the  with the task of research .
    Here is the user question or query:{question}.
    Provide a step by step guide to help with te reaserch task.
    """
    plan_intake=llm_intake(prompt)
    
    state['plan']=plan_intake
    return state


def Researcher(state):
    plan_details=state['plan']
    prompt=f"""
    You are the research expert assistant.Given the details of the plan below,Provide the necessary research 
    Here is the plan details:{plan_details}.
    """
    research_notes=llm_intake(prompt)
    state['research_notes']=research_notes
    return state


def Verifier(state):
    research_notes=state['research_notes']
    prompt=f""" 
    You are the verification expert assistant.Given the research notes below. verify the accuracy and reliablity of the 
    information.if you found any discrepencies, correct the inform,ation and update the notes.
    Her is the researc notes:{rses}
    """