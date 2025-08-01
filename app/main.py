from graph import graph
import uuid

def run_cli():
    print("👋 Welcome to AI Interviewer (CLI Edition)")
    topic = input("Enter interview topic: ").strip()

    session_id = str(uuid.uuid4())
    interviewer = graph()

    # Start the interview
    state = interviewer.invoke(
        {"messages": [{"role": "user", "content": topic}]},
        config={"thread_id": session_id}
    )

    question_number = 1

    while True:
        messages = state["messages"]
        last_msg = messages[-1]
        last_msg_content = getattr(last_msg, "content", str(last_msg))

        # Stop loop if final summary appears
        if "final score" in last_msg_content.lower() or "performance summary" in last_msg_content.lower():
            print("\n🎓 Final Evaluation:")
            print(last_msg_content)
            break

        # Show only the question
        print(f"\n🔹 Question {question_number}: {last_msg_content}")
        user_answer = input("Your answer: ").strip()

        # Pass user's answer into the graph
        state = interviewer.invoke(
            {"messages": [{"role": "user", "content": user_answer}]},
            config={"thread_id": session_id}
        )

        question_number += 1

if __name__ == "__main__":
    run_cli()
