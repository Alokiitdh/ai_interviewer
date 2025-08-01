from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from llm import llm
from tools import tavily_tool
from prompts import question_agent_prompt, evaluation_agent_prompt, performance_agent_prompt, supervisor_prompt
from schema import QuestionResponse,EvaluationResponse,PerformanceResponse
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

checkpointer = InMemorySaver()
store = InMemoryStore()

#Question Agent
question_agent = create_react_agent(
        model=llm,
        name="question_framing_agent",
        tools = [tavily_tool],
        prompt=question_agent_prompt,
        response_format=QuestionResponse
)
#Evaluation Agent
evaluation_agent = create_react_agent(
        model=llm,
        name="evaluation_agent",
        tools = [],
        prompt=evaluation_agent_prompt,
        response_format=EvaluationResponse
)

# performance_agent
performance_agent = create_react_agent(
        model=llm,
        name="performance_agent",
        tools = [],
        prompt=performance_agent_prompt,
        response_format=PerformanceResponse
)

# Supervisor
ai_interviewer = create_supervisor(
    model=llm,
    agents=[question_agent,evaluation_agent, performance_agent],
    prompt=supervisor_prompt,
    add_handoff_back_messages=True,
    supervisor_name="AI_Interviewer",
    output_mode="last_message"
)

interviewer_graph = ai_interviewer.compile(name="AI_Interviewer",
                                               checkpointer=checkpointer,
                                             store=store)

# interviewer_graph.get_graph().draw_mermaid_png(output_file_path="ai_graph_2.png")

def graph():
    return interviewer_graph


