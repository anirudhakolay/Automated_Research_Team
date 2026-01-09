import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from crewai import LLM
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()



# Initialize the Groq LLM (Free & Fast)
llm = LLM(
    model="groq/llama-3.3-70b-versatile",  # Using the powerful Llama 3 70B model
    temperature=0.7
)

# 2. DEFINE TOOLS
# Initialize DuckDuckGo (Free Search)
ddg = DuckDuckGoSearchRun()
@tool("DuckDuckGo Search")
def duckduckgo_search(query: str) -> str:
    """Search the web using DuckDuckGo"""
    return ddg.run(query)

search_tool = duckduckgo_search

# 3. DEFINE AGENTS
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in {topic}',
    backstory="""You are a veteran analyst with a nose for news. 
    You excel at sifting through noise to find key trends.""",
    verbose=True,
    memory=True,
    llm=llm,              # <--- We explicitly tell it to use Groq
    tools=[search_tool]   # <--- We give it the free search tool
)

writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on {topic}',
    backstory="""You are a renowned content strategist. 
    You take raw data and turn it into engaging, professional narratives.""",
    verbose=True,
    memory=True,
    llm=llm,              # <--- Both agents use the free Groq model
    allow_delegation=False
)

# 4. DEFINE     

research_task = Task(
    description="""Search the web for the latest news and trends regarding {topic}.
    Focus on the last 12 months. Identify top 3 key trends.""",
    expected_output="A bullet-point summary of the top 3 trends with brief explanations.",
    agent=researcher
)

write_task = Task(
    # description="""Based on the researcher's summary, write a professional blog post about {topic}.
    # The post should have a catchy title, an introduction, and a section for each trend."""
    description="""Use the DuckDuckGo Search tool to find articles, reports, and blogs
                from the last 12 months about {topic}. Identify exactly 3 major trends with evidence.""",
    expected_output="A 3-section blog post formatted in Markdown.",
    agent=writer
)

# 5. EXECUTE THE CREW
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

# Run the project
topic = "Agentic AI trends 2025"
print(f"Searching for: {topic}...")
result = crew.kickoff(inputs={'topic': topic})

print("\n######################")
print("## FINAL REPORT ##")
print("######################\n")
print(result)