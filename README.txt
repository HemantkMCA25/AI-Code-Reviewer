🤖 AI Code Reviewer (Hybrid AI System)

An intelligent code review system that analyzes Python code using AST-based static analysis and provides structured feedback using rule-based logic with optional AI enhancement. It also generates a custom quality score based on code complexity, modularity, and optimization potential.

🚀 Features

AST-based static code analysis (loops, functions, structure detection)
Custom scoring engine (0–100) based on complexity and code quality
Hybrid feedback system (AI-powered + rule-based fallback)
Code complexity estimation and modularity checks
Interactive Streamlit UI for real-time code review
Transparent analysis mode display (AI or Rule-based)

🏗️ Project Structure

ai-code-reviewer/
│
├── app.py → Streamlit UI
├── analyzer.py → AST-based analysis
├── scorer.py → Score calculation logic
├── ai_engine.py → AI + rule-based hybrid feedback
├── review.py → Main pipeline controller
├── requirements.txt → Dependencies
└── README.txt

⚙️ How It Works

User inputs Python code via Streamlit UI
AST parser extracts structural metrics (loops, functions, nesting)
Scoring engine evaluates code quality (0–100 scale)
AI model generates feedback (if API key is available)
Rule-based system acts as fallback if AI is unavailable
Final result is displayed with score, metrics, and feedback

▶️ Installation & Setup

Clone Repository
git clone https://github.com/your-username/ai-code-reviewer

cd ai-code-reviewer
Install Dependencies
pip install -r requirements.txt
Run Application
python -m streamlit run app.py

🔑 Optional AI Setup

Windows (PowerShell):
setx OPENAI_KEY "your_api_key_here"

Mac/Linux:
export OPENAI_KEY "your_api_key_here"

If no API key is provided, the system automatically switches to rule-based analysis.

📊 Scoring System

Score is calculated based on:

1. Loop complexity
2. Function modularity
3. Code structure quality
4. Optimization potential

Final Score Range: 0–100

🧠 Example Output

Score: 78/100
Mode: AI-Enhanced / Rule-Based

Feedback:

Nested loops detected → high complexity (O(n²))
Improve modularity using functions
Consider optimized data structures

🛠️ Tech Stack

Python
Streamlit
AST (Abstract Syntax Tree)
OpenAI API (optional)

🚀 Future Improvements

GitHub repository code review support
Multi-language support (Java, C++)
PDF report generation
Advanced ML-based bug detection
Code similarity detection