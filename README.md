Django AI Agent
An advanced AI Agent implementation using Django, LangGraph, and Permit.io. This project demonstrates how to build a production-ready AI assistant that can interact with a Django database, execute custom Python tools, and follow strict Role-Based Access Control (RBAC) guardrails.

🚀 Features
Django Integration: Uses the Django ORM to chat directly with your application data without needing complex vector embeddings.

LangGraph Orchestration: Manages complex agentic workflows, including multi-agent setups and supervisor loops.

Permit.io Guardrails: Implements granular permissions (RBAC) to ensure the AI agent can only perform actions (Read, Create, Update, Delete) authorized for the specific user.

Custom Tools: Turn any Python function into a tool the agent can use (e.g., fetching documents, checking movie listings, or querying internal APIs).

Jupyter Integration: Includes notebooks for rapid prototyping of agents and tools within the Django environment.

🛠️ Tech Stack
Framework: Django

AI Orchestration: LangChain / LangGraph

Permissions & Security: Permit.io

Environment: Python 3.10+

📋 Prerequisites
Before you begin, ensure you have:

A Permit.io account and API key.

An OpenAI (or Anthropic/Google) API key.

Python installed on your local machine.

⚙️ Installation
Clone the repository:

Bash
git clone https://github.com/varunsadanand/django-ai-agent.git
cd django-ai-agent
Create and activate a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Environment Setup: Create a .env file in the root directory and add your credentials:

Code snippet
OPENAI_API_KEY=your_openai_key
PERMIT_API_KEY=your_permit_key
DEBUG=True
SECRET_KEY=your_django_secret_key
Run Migrations:

Bash
python manage.py migrate
Start the Development Server:

Bash
python manage.py runserver
📖 Usage
Running the AI Agent
You can interact with the agent via the Django shell or through the provided Jupyter notebooks:

Bash
python manage.py shell_plus --notebook
Agent Capabilities
The agent is designed to:

Query User Data: "Who are the recently joined users?"

Action Execution: "Create a new document for user X" (Checked against Permit.io policy).

Tool Usage: "Search for the latest news regarding [Topic]."

🔒 Security & Permissions
This project uses Permit.io to enforce security. If the AI agent attempts to run a tool that modifies data, the Permit middleware checks the current user's role. If the user lacks the editor or admin role, the agent will receive a "Permission Denied" response and explain this to the user.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
