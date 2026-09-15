import os
import requests

def rule_based_explanation(metrics):

    loops = metrics.get("loops", 0)
    functions = metrics.get("functions", 0)

    feedback = []

    # Complexity rules
    if loops == 0:
        feedback.append("No loops detected. Code is likely O(1). Good efficiency.")

    elif loops == 1:
        feedback.append("Single loop detected. Complexity likely O(n). Acceptable.")

    elif loops == 2:
        feedback.append("Nested loops detected. Complexity may be O(n²). Consider optimization.")

    else:
        feedback.append("High nesting detected. Code may be inefficient (O(n³) or worse).")

    # Structure rules
    if functions == 0:
        feedback.append("No functions used. Code is not modular.")
    elif functions == 1:
        feedback.append("Single function detected. Consider breaking logic into modules.")
    else:
        feedback.append("Good modular structure with multiple functions.")

    # Best practice rule
    if loops > 2 and functions < 2:
        feedback.append(" High complexity & low modularity detected. Refactor strongly recommended.")

    return "\n\n".join(feedback)

def ai_explanation(code):

    api_key = os.getenv("OPENAI_KEY")

    # If no API key → skip AI
    if not api_key:
        return None

    prompt = f"""
You are a senior software engineer.
Review this code:

{code}

Give:
- issues
- improvements
- optimized version
"""

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

    except:
        pass

    return None


def explain(code, metrics):

    ai_result = ai_explanation(code)

    if ai_result:
        return ai_result, "AI"

    return rule_based_explanation(metrics), "RULE"