import streamlit as st

questions = [
    {
        "question": "What is Python?",
        "options": [
            "A. Programming Language",
            "B. Database",
            "C. Operating System",
            "D. Browser"
        ],
        "Answer": "A"
    },
    {
        "question": "What is a tuple?",
        "options": [
            "A. Changeable",
            "B. Immutable",
            "C. Function",
            "D. Loop"
        ],
        "Answer": "B"
    }
]


# Page configuration
st.set_page_config(
    page_title="IOE Model Question",
    page_icon="📝",
    layout="centered"
)

st.title("📝 IOE Model Question")
st.write("Select one answer for each question.")

# Form
with st.form("quiz_form"):

    answers = {}

    for i, q in enumerate(questions):

        st.subheader(f"{i + 1}. {q['question']}")

        # Radio button
        answers[i] = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"question_{i}"
        )

        st.divider()

    # Submit button
    submitted = st.form_submit_button("Submit Quiz")

# Calculate result
if submitted:

    score = 0

    for i, q in enumerate(questions):

        # Get A/B/C/D from selected option
        user_answer = answers[i][0]

        print("Question:", q["question"])
        print("User Answer:", user_answer)
        print("Correct Answer:", q["Answer"])

        if user_answer == q["Answer"]:
            score += 1
        else:
            score -= 0.25

    st.success("Quiz submitted successfully!")

    st.subheader("Result")

    st.write(f"**Your Score: {score} / {len(questions)}**")

    if score == len(questions):
        st.balloons()
        st.success("Excellent! 🎉")

    elif score > 0:
        st.info("Good job! Keep practicing.")

    else:
        st.warning("Keep practicing and try again.")
