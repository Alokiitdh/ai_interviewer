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
        last_msg = state["messages"][-1]

        # FIX: Use dot notation
        if isinstance(last_msg, str):
            last_msg_content = last_msg
        else:
            last_msg_content = last_msg.content

        if "final_score" in last_msg_content.lower():  # or any other end marker you use
            break

        print(f"\n🔹 Question {question_number}: {last_msg_content}")
        user_answer = input("Your answer: ").strip()

        state = interviewer.invoke(
            {"messages": [{"role": "user", "content": user_answer}]},
            config={"thread_id": session_id}
        )

        eval_msg = state["messages"][-1]

        if hasattr(eval_msg, "content"):
            print(f"✅ Evaluation: {eval_msg.content}")
        else:
            print("✅ Evaluation:", eval_msg)

        question_number += 1

    print("\n🎯 Final Report:")
    print(state["messages"][-1].content)

if __name__ == "__main__":
    run_cli()
