from analyzer import analyze
from scorer import score
from ai_engine import explain

def run_review(code):

    metrics = analyze(code)

    if "error" in metrics:
        return {
            "score": 0,
            "metrics": metrics,
            "feedback": metrics["error"],
            "mode": "RULE"
        }

    final_score = score(metrics)

    feedback, mode = explain(code, metrics)

    return {
        "score": final_score,
        "metrics": metrics,
        "feedback": feedback,
        "mode": mode
    }