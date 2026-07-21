import io
import sys
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Python: Learn to Speak", page_icon="🐍", layout="centered"
)

# Custom Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: #00ff66;
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
if "module_index" not in st.session_state:
  st.session_state.module_index = 0

# Track answer states per module
if "m1_status" not in st.session_state:
  st.session_state.m1_status = None
if "m2_status" not in st.session_state:
  st.session_state.m2_status = None
if "m3_status" not in st.session_state:
  st.session_state.m3_status = None

modules_list = [
    "Module 1: The Voice Box (print)",
    "Module 2: The Backpack (Variables)",
    "Module 3: The Fork in the Road (If/Else)",
]

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(
    ["🚀 Interactive Lessons", "💻 Live Sandbox", "📖 Terminology Glossary"]
)

# --- TAB 1: INTERACTIVE LESSONS ---
with tab1:
  # Callback function to sync selectbox selection back to session state index
  def update_module_index():
    selected_val = st.session_state.my_selectbox_key
    st.session_state.module_index = modules_list.index(selected_val)

  # Selectbox tied to session state via index and callback
  selected_module = st.selectbox(
      "Choose Your Learning Module",
      modules_list,
      index=st.session_state.module_index,
      key="my_selectbox_key",
      on_change=update_module_index,
  )

  st.divider()

  # Render content based on current module_index (source of truth)
  current_module = modules_list[st.session_state.module_index]

  if "Module 1" in current_module:
    st.subheader("Module 1: `print` (The Computer's Voice Box)")
    st.write(
        "In human language, you use your voice to speak. In Python, you use"
        " `print` to make the computer speak text onto the screen."
    )

    st.markdown("### Challenge 1: Make the computer say hello!")
    col1, col2, col3 = st.columns(3)

    with col1:
      if st.button("speak('Hello!')"):
        st.session_state.m1_status = "wrong1"
        st.rerun()

    with col2:
      if st.button("print('Hello!')"):
        if st.session_state.m1_status != "correct":
          st.session_state.score += 10
        st.session_state.m1_status = "correct"
        st.rerun()

    with col3:
      if st.button("display('Hello!')"):
        st.session_state.m1_status = "wrong3"
        st.rerun()

    if st.session_state.m1_status == "correct":
      st.success(
          "🎉 Correct! You spoke your first line of Python! (+10 XP)"
      )
    elif st.session_state.m1_status in ["wrong1", "wrong3"]:
      st.error("❌ Incorrect! Try the correct syntax.")

  elif "Module 2" in current_module:
    st.subheader("Module 2: Variables (The Computer's Backpack)")
    st.write(
        "Think of a variable as a labeled box where the computer can store data"
        " to use later. Example: `score = 100`"
    )

    st.markdown("### Challenge 2: Store a value!")
    if st.button("100 = score"):
      st.session_state.m2_status = "wrong1"
      st.rerun()
    if st.button("score == 100"):
      st.session_state.m2_status = "wrong2"
      st.rerun()
    if st.button("score = 100"):
      if st.session_state.m2_status != "correct":
        st.session_state.score += 10
      st.session_state.m2_status = "correct"
      st.rerun()

    if st.session_state.m2_status == "correct":
      st.success(
          "🎉 Nailed it! Data successfully saved into memory. (+10 XP)"
      )
    elif st.session_state.m2_status:
      st.error("❌ Not quite right. Variable name goes on the left!")

  elif "Module 3" in current_module:
    st.subheader("Module 3: If/Else (The Computer's Choices)")
    st.write(
        "Computers aren't smart on their own; they just follow rules. `if` lets"
        " them make decisions based on conditions."
    )

    st.markdown("### Challenge 3: Write a basic choice condition")
    if st.button("if score > 50: win()"):
      if st.session_state.m3_status != "correct":
        st.session_state.score += 15
      st.session_state.m3_status = "correct"
      st.rerun()
    if st.button("when score > 50 do win()"):
      st.session_state.m3_status = "wrong"
      st.rerun()

    if st.session_state.m3_status == "correct":
      st.success(
          "🎉 Spot on! Python uses the `if` keyword followed by a colon."
          " (+15 XP)"
      )
    elif st.session_state.m3_status == "wrong":
      st.error("❌ Python doesn't use 'when' or 'do' like plain English here.")

  st.divider()

  # --- NEXT / PREVIOUS CHAPTER CONTROLS ---
  col_prev, col_next = st.columns(2)

  with col_prev:
    if st.session_state.module_index > 0:
      if st.button("⬅ Previous Chapter"):
        st.session_state.module_index -= 1
        st.session_state.my_selectbox_key = modules_list[
            st.session_state.module_index
        ]
        st.rerun()

  with col_next:
    if st.session_state.module_index < len(modules_list) - 1:
      if st.button("Next Chapter ➡"):
        st.session_state.module_index += 1
        st.session_state.my_selectbox_key = modules_list[
            st.session_state.module_index
        ]
        st.rerun()

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
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
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
    f"Active Chapter: {st.session_state.module_index + 1} of"
    f" {len(modules_list)}"
)
