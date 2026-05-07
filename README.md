How to Run:

Backend:
1. Open Terminal in Visual Studio
2. cd backend
3. pip install -r requirements.txt
4. uvicorn main:app --reload

Frontend:
1. Open another terminal in Visual Studio
2. cd frontend
3. npm install
4. npm start
5. Open localhost:3000 to run the application in the browser.

Dependencies: 
Python: FastAPI, SQLAlchemy, Pydantic 
Node js needs to be installed on the local machine 
JS: React 
DB: SQLite

Future Improvements:
1. LLM Integration: Swap the keyword logic in agent.py for an OpenAI/Anthropic call to decide tool usage.
2. Complex Reasoning: Implement a ReAct (Reason + Act) loop where the agent can use a tool, observe the output, and decide if another tool is needed.

Assumptions and Design Decisions:
1. Keyword scoring — the agent scores every tool against the input and picks the highest match. Deterministic and testable, unlike LLM routing.
2. Execution trace — every step (receive → analyse → select → execute → return) is recorded and rendered as a timeline in the frontend.
3. Persistence: SQLite was chosen to demonstrate clean data modeling and easier querying for history.
