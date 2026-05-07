How to Run Clone the github repository

Backend:

Open Terminal in Visual Studio
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Frontend:

Open another terminal in Visual Studio
cd frontend
npm install
npm start
Open localhost:3000 to run the application in the browser.
Dependencies Python: FastAPI, SQLAlchemy, Pydantic Node js needs to be installed on the local machine JS: React DB: SQLite

Future Improvements

LLM Integration: Swap the keyword logic in agent.py for an OpenAI/Anthropic call to decide tool usage.
Complex Reasoning: Implement a ReAct (Reason + Act) loop where the agent can use a tool, observe the output, and decide if another tool is needed.
Assumptions and Design Decisions:

Keyword scoring — the agent scores every tool against the input and picks the highest match. Deterministic and testable, unlike LLM routing.
Execution trace — every step (receive → analyse → select → execute → return) is recorded and rendered as a timeline in the frontend.
Persistence: SQLite was chosen to demonstrate clean data modeling and easier querying for history.
