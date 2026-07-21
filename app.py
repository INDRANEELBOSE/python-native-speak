import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Python: Learn to Speak", page_icon="🐍", layout="centered"
)

# Custom Styling for Retro Arcade Vibe
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: #00ff66;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f2937;
        color: #00ff66;
        border: 1px solid #00ff66;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00ff66;
        color: #0e1117;
    }
    .output-box {
        background-color: #111827;
        border-left: 4px solid #00ff66;
        padding: 15px;
        font-family: monospace;
        border-radius: 4px;
        color: #38bdf8;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# App Header
st.title("🐍 Python: Learn to Speak")
st.markdown(
    "**The Native Language Approach:** Master Python core words like a spoken language through instant visual actions."
)
st.divider()

# Session State Initialization for Progress
if "score" not in st.session_state:
    st.session_state.score = 0
if "step" not in st.session_state:
    st.session_state.step = 1

# --- LEVEL 1: THE VOICE BOX (print) ---
if st.session_state.step == 1:
  st.subheader("Word #1: `print` (The Computer's Voice Box)")
  st.write(
      "In human language, you use your voice to speak. In Python, you use"
      " `print` to make the computer speak onto the screen."
  )

  st.markdown("### Challenge 1: Make the computer say hello!")
  st.write("Which command tells the computer to output text to the screen?")

  # Interactive Choice Buttons (Zero-typing frustration)
  col1, col2, col3 = st.columns(3)

  with col1:
    if st.button("speak('Hello!')"):
      st.error("❌ Not quite! Python doesn't recognize 'speak'. Try again!")

  with col2:
    if st.button("print('Hello!')"):
      st.success("🎉 Correct! You spoke your first line of Python!")
      st.session_state.score += 10
      st.session_state.step = 2
      st.rerun()

  with col3:
    if st.button("display('Hello!')"):
      st.error("❌ Close, but Python uses a specific 5-letter word for this.")

# --- LEVEL 2: THE MEMORY BOX (Variables) ---
elif st.session_state.step == 2:
  st.subheader("Word #2: Variables (The Computer's Backpack)")
  st.write(
      "Think of a variable as a labeled box where the computer can store data"
      " to use later. For example: `name = 'Alex'`"
  )

  st.markdown("### Challenge 2: Store a score!")
  st.write(
      "How do you correctly store the number `100` inside a variable named"
      " `score`?"
  )

  opt1 = st.button("100 = score")
  opt2 = st.button("score == 100")
  opt3 = st.button("score = 100")

  if opt1:
    st.error(
        "❌ Backwards! The variable name always goes on the left, and the value"
        " goes on the right."
    )
  elif opt2:
    st.error(
        "❌ That's for checking if things are equal later. To store data, use a"
        " single equals sign."
    )
  elif opt3:
    st.success("🎉 Nailed it! Data successfully saved into memory.")
    st.session_state.score += 10
    st.session_state.step = 3
    st.rerun()

# --- LEVEL 3: COMPLETION ---
elif st.session_state.step == 3:
  st.balloons()
  st.subheader("🏆 Module 1 Complete!")
  st.markdown(
      '<div class="output-box">CONGRATULATIONS! You have successfully learned'
      " your first core Python words ('print' and variables). You are officially"
      " speaking the language.</div>",
      unsafe_allow_html=True,
  )

  if st.button("🔄 Restart Training"):
    st.session_state.step = 1
    st.session_state.score = 0
    st.rerun()

# Sidebar Stats Tracker
st.sidebar.markdown("### 📊 Player Stats")
st.sidebar.metric("XP Score", f"{st.session_state.score} XP")
st.sidebar.metric("Current Stage", f"Level {st.session_state.step} of 3")
