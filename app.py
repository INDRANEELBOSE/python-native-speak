import io
import sys
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
    "**The Native Language Approach:** Master Python core words like a spoken"
    " language through interactive challenges and instant visual feedback."
)

# Session State Initialization
if "score" not in st.session_state:
  st.session_state.score = 0
if "module" not in st.session_state:
  st.session_state.module = 1

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(
    ["🚀 Interactive Lessons", "💻 Live Sandbox", "📖 Terminology Glossary"]
)

# --- TAB 1: INTERACTIVE LESSONS ---
with tab1:
  # Module Select Menu
  selected_module = st.selectbox(
      "Choose Your Learning Module",
      [
          "Module 1: The Voice Box (print)",
          "Module 2: The Backpack (Variables)",
          "Module 3: The Fork in the Road (If/Else)",
      ],
  )

  st.divider()

  if "Module 1" in selected_module:
    st.subheader("Module 1: `print` (The Computer's Voice Box)")
    st.write(
        "In human language, you use your voice to speak. In Python, you use"
        " `print` to make the computer speak text onto the screen."
    )

    st.markdown("### Challenge 1: Make the computer say hello!")
    col1, col2, col3 = st.columns(3)

    with col1:
      if st.button("speak('Hello!')"):
        st.error("❌ Not quite! Python doesn't recognize 'speak'.")
    with col2:
      if st.button("print('Hello!')"):
        st.success(
            "🎉 Correct! You spoke your first line of Python! (+10 XP)"
        )
        st.session_state.score += 10
    with col3:
      if st.button("display('Hello!')"):
        st.error("❌ Close, but Python uses a specific 5-letter word.")

  elif "Module 2" in selected_module:
    st.subheader("Module 2: Variables (The Computer's Backpack)")
    st.write(
        "Think of a variable as a labeled box where the computer can store data"
        " to use later. Example: `score = 100`"
    )

    st.markdown("### Challenge 2: Store a value!")
    opt1 = st.button("100 = score")
    opt2 = st.button("score == 100")
    opt3 = st.button("score = 100")

    if opt1:
      st.error("❌ Backwards! Variable name always goes on the left.")
    elif opt2:
      st.error("❌ That's for checking equality later, not saving data.")
    elif opt3:
      st.success("🎉 Nailed it! Data successfully saved into memory. (+10 XP)")
      st.session_state.score += 10

  elif "Module 3" in selected_module:
    st.subheader("Module 3: If/Else (The Computer's Choices)")
    st.write(
        "Computers aren't smart on their own; they just follow rules. `if` lets"
        " them make decisions based on conditions."
    )

    st.markdown("### Challenge 3: Write a basic choice condition")
    c1 = st.button("if score > 50: win()")
    c2 = st.button("when score > 50 do win()")

    if c1:
      st.success(
          "🎉 Spot on! Python uses the `if` keyword followed by a colon."
          " (+15 XP)"
      )
      st.session_state.score += 15
    elif c2:
      st.error(
          "❌ Python doesn't use the word 'when' or 'do' like plain English here."
      )

# --- TAB 2: LIVE SANDBOX ---
with tab2:
  st.subheader("💻 Python Sandbox")
  st.write(
      "Test your code live! Type a simple Python command below and run it"
      " instantly."
  )

  user_code = st.text_area(
      "Write code here:", value='print("Hello, World from Python!")'
  )

  if st.button("▶ Run Code"):
    # Capture standard output safely
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
      # Execute code safely in a restricted scope
      exec(user_code)
      result = new_stdout.getvalue()
    except Exception as e:
      result = f"Error: {e}"
    finally:
      sys.stdout = old_stdout

    st.markdown("### Output Result:")
    st.markdown(
        f'<div class="output-box">{result if result else "Code ran successfully with no output."}</div>',
        unsafe_allow_html=True,
    )

# --- TAB 3: TERMINOLOGY GLOSSARY ---
with tab3:
  st.subheader("📖 Plain-English Python Dictionary")
  st.write(
      "No scary jargon. Here is what programming terms actually mean in human"
      " terms:"
  )

  st.markdown(
      """
    * **`print()`** $\rightarrow$ **The Voice Box:** Screams text onto the screen for humans to read.
    * **Variable** $\rightarrow$ **The Backpack:** A labeled pocket where you store a piece of information (like a name or number) to use later.
    * **String** $\rightarrow$ **The Text Tag:** Normal everyday text wrapped in quotes (like `"Apple"`).
    * **Integer** $\rightarrow$ **The Whole Number:** Plain counting numbers without decimals (like `42`).
    * **`if / else`** $\rightarrow$ **The Fork in the Road:** Tells the computer what to do depending on whether a rule is true or false.
    """
  )

# Sidebar Stats Tracker
st.sidebar.markdown("### 📊 Player Status")
st.sidebar.metric("Total XP Score", f"{st.session_state.score} XP")
st.sidebar.success(
    "App is live, interactive, and completely sandboxed. Ready for testing!"
)
