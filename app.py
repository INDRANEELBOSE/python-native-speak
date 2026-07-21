import io
import json
import random
import sys
import urllib.request
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

# Track answer states for all 12 modules
for i in range(1, 13):
  key = f"m{i}_status"
  if key not in st.session_state:
    st.session_state[key] = None

modules_list = [
    "Module 1: The Voice Box (print)",
    "Module 2: The Backpack (Variables)",
    "Module 3: The Fork in the Road (If/Else)",
    "Module 4: The Endless Loop (While/For)",
    "Module 5: The Mini-Machine (Functions)",
    "Module 6: The Filing Cabinet (Lists & Dicts)",
    "Module 7: The Toolbelt (Imports & Modules)",
    "Module 8: The Safety Net (Try/Except)",
    "Module 9: The Diary (File Handling)",
    "Module 10: The Blueprint (Classes & OOP)",
    "Module 11: The Ninja Shortcut (Lambdas)",
    "Module 12: The Internet Wire (APIs & JSON)",
]

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(
    ["🚀 Interactive Lessons", "💻 Live Sandbox", "📖 Terminology Glossary"]
)

# --- TAB 1: INTERACTIVE LESSONS ---
with tab1:
  # Clean Selectbox Bound directly to index
  selected_module = st.selectbox(
      "Choose Your Learning Module",
      modules_list,
      index=st.session_state.module_index,
      key="module_selectbox_key",
  )

  # Update module index based on user selection
  st.session_state.module_index = modules_list.index(selected_module)
  st.divider()

  idx = st.session_state.module_index

  # --- MODULE 1 ---
  if idx == 0:
    st.subheader("Module 1: `print` (The Computer's Voice Box)")
    st.write(
        "In human language, you use your voice to speak. In Python, you use"
        " `print` to make the computer speak text onto the screen."
    )

    st.markdown("### Challenge 1: Make the computer say hello!")
    col1, col2, col3 = st.columns(3)

    with col1:
      if st.button("speak('Hello!')", key="m1_b1"):
        st.session_state.m1_status = "wrong"
        st.rerun()
    with col2:
      if st.button("print('Hello!')", key="m1_b2"):
        if st.session_state.m1_status != "correct":
          st.session_state.score += 10
        st.session_state.m1_status = "correct"
        st.rerun()
    with col3:
      if st.button("display('Hello!')", key="m1_b3"):
        st.session_state.m1_status = "wrong"
        st.rerun()

    if st.session_state.m1_status == "correct":
      st.success(
          "🎉 Correct! You spoke your first line of Python! (+10 XP)"
      )
    elif st.session_state.m1_status == "wrong":
      st.error("❌ Incorrect! Try the correct syntax.")

  # --- MODULE 2 ---
  elif idx == 1:
    st.subheader("Module 2: Variables (The Computer's Backpack)")
    st.write(
        "Think of a variable as a labeled box where the computer can store data"
        " to use later. Example: `score = 100`"
    )

    st.markdown("### Challenge 2: Store a value!")
    if st.button("100 = score", key="m2_b1"):
      st.session_state.m2_status = "wrong"
      st.rerun()
    if st.button("score == 100", key="m2_b2"):
      st.session_state.m2_status = "wrong"
      st.rerun()
    if st.button("score = 100", key="m2_b3"):
      if st.session_state.m2_status != "correct":
        st.session_state.score += 10
      st.session_state.m2_status = "correct"
      st.rerun()

    if st.session_state.m2_status == "correct":
      st.success(
          "🎉 Nailed it! Data successfully saved into memory. (+10 XP)"
      )
    elif st.session_state.m2_status == "wrong":
      st.error("❌ Not quite right. Variable name goes on the left!")

  # --- MODULE 3 ---
  elif idx == 2:
    st.subheader("Module 3: If/Else (The Computer's Choices)")
    st.write(
        "Computers aren't smart on their own; they just follow rules. `if` lets"
        " them make decisions based on conditions."
    )

    st.markdown("### Challenge 3: Write a basic choice condition")
    if st.button("if score > 50: win()", key="m3_b1"):
      if st.session_state.m3_status != "correct":
        st.session_state.score += 15
      st.session_state.m3_status = "correct"
      st.rerun()
    if st.button("when score > 50 do win()", key="m3_b2"):
      st.session_state.m3_status = "wrong"
      st.rerun()

    if st.session_state.m3_status == "correct":
      st.success(
          "🎉 Spot on! Python uses the `if` keyword followed by a colon."
          " (+15 XP)"
      )
    elif st.session_state.m3_status == "wrong":
      st.error("❌ Python doesn't use 'when' or 'do' like plain English here.")

  # --- MODULE 4 ---
  elif idx == 3:
    st.subheader("Module 4: Loops (The Robot's Treadmill)")
    st.write(
        "Instead of writing the same instruction 100 times, a loop tells the"
        " computer to repeat an action automatically."
    )

    st.markdown("### Challenge 4: Which command runs a task across a range?")
    if st.button("repeat 5 times:", key="m4_b1"):
      st.session_state.m4_status = "wrong"
      st.rerun()
    if st.button("for i in range(5):", key="m4_b2"):
      if st.session_state.m4_status != "correct":
        st.session_state.score += 15
      st.session_state.m4_status = "correct"
      st.rerun()

    if st.session_state.m4_status == "correct":
      st.success(
          "🎉 Perfect! `for i in range()` is Python's loop counter. (+15 XP)"
      )
    elif st.session_state.m4_status == "wrong":
      st.error("❌ Not quite! Python relies on `for` loops with ranges.")

  # --- MODULE 5 ---
  elif idx == 4:
    st.subheader("Module 5: Functions (The Mini-Machine Recipe)")
    st.write(
        "A function is a custom mini-machine you build once and reuse whenever"
        " you want. You define it using `def`."
    )

    st.markdown("### Challenge 5: How do you start building a custom function?")
    if st.button("create my_func():", key="m5_b1"):
      st.session_state.m5_status = "wrong"
      st.rerun()
    if st.button("def make_coffee():", key="m5_b2"):
      if st.session_state.m5_status != "correct":
        st.session_state.score += 20
      st.session_state.m5_status = "correct"
      st.rerun()

    if st.session_state.m5_status == "correct":
      st.success(
          "🎉 Outstanding! `def` defines a function in Python. (+20 XP)"
      )
    elif st.session_state.m5_status == "wrong":
      st.error("❌ Incorrect! Python uses shorthand `def`.")

  # --- MODULE 6 ---
  elif idx == 5:
    st.subheader("Module 6: Lists & Dictionaries (The Filing Cabinet)")
    st.write(
        "Instead of storing just one value in a backpack, a **List** holds a"
        " whole row of items inside brackets `[]`."
    )

    st.markdown("### Challenge 6: How do you write a list of fruits?")
    if st.button("fruits = (apple, banana)", key="m6_b1"):
      st.session_state.m6_status = "wrong"
      st.rerun()
    if st.button("fruits = ['apple', 'banana']", key="m6_b2"):
      if st.session_state.m6_status != "correct":
        st.session_state.score += 20
      st.session_state.m6_status = "correct"
      st.rerun()

    if st.session_state.m6_status == "correct":
      st.success(
          "🎉 Spot on! Lists use square brackets `[]` in Python. (+20 XP)"
      )
    elif st.session_state.m6_status == "wrong":
      st.error("❌ Close, but parentheses `()` are tuples. Lists use `[]`.")

  # --- MODULE 7 ---
  elif idx == 6:
    st.subheader("Module 7: Imports & Modules (The Toolbelt)")
    st.write(
        "Python comes with thousands of pre-made toolkits. To use a toolkit like"
        " random math tools, you have to `import` it first."
    )

    st.markdown("### Challenge 7: How do you bring in the random toolkit?")
    if st.button("get random", key="m7_b1"):
      st.session_state.m7_status = "wrong"
      st.rerun()
    if st.button("import random", key="m7_b2"):
      if st.session_state.m7_status != "correct":
        st.session_state.score += 20
      st.session_state.m7_status = "correct"
      st.rerun()

    if st.session_state.m7_status == "correct":
      st.success(
          "🎉 You got it! `import` unlocks external modules. (+20 XP)"
      )
    elif st.session_state.m7_status == "wrong":
      st.error("❌ Incorrect! Python uses the keyword `import`.")

  # --- MODULE 8 ---
  elif idx == 7:
    st.subheader("Module 8: Try/Except (The Safety Net)")
    st.write(
        "Sometimes code crashes (like dividing by zero). A `try/except` block"
        " catches errors gracefully instead of letting the app explode."
    )

    st.markdown(
        "### Challenge 8: What keyword catches errors when a crash happens?"
    )
    if st.button("catch error:", key="m8_b1"):
      st.session_state.m8_status = "wrong"
      st.rerun()
    if st.button("except:", key="m8_b2"):
      if st.session_state.m8_status != "correct":
        st.session_state.score += 25
      st.session_state.m8_status = "correct"
      st.rerun()

    if st.session_state.m8_status == "correct":
      st.success("🎉 Awesome! `except` handles the crash safely. (+25 XP)")
    elif st.session_state.m8_status == "wrong":
      st.error("❌ Not quite! Python uses `except` to catch problems.")

  # --- MODULE 9 ---
  elif idx == 8:
    st.subheader("Module 9: File Handling (The Computer's Diary)")
    st.write(
        "To read or write files on your disk, Python uses the built-in `open()`"
        " function combined with a mode like `'r'` (read) or `'w'` (write)."
    )

    st.markdown("### Challenge 9: How do you open a file to write data into it?")
    if st.button("open('notes.txt', 'w')", key="m9_b1"):
      if st.session_state.m9_status != "correct":
        st.session_state.score += 25
      st.session_state.m9_status = "correct"
      st.rerun()
    if st.button("open_file('notes.txt')", key="m9_b2"):
      st.session_state.m9_status = "wrong"
      st.rerun()

    if st.session_state.m9_status == "correct":
      st.success(
          "🎉 Perfect! `open(filename, 'w')` opens a file for writing. (+25 XP)"
      )
    elif st.session_state.m9_status == "wrong":
      st.error("❌ Incorrect! Python's built-in command is `open()`.")

  # --- MODULE 10 ---
  elif idx == 9:
    st.subheader("Module 10: Object-Oriented Programming (The Blueprint)")
    st.write(
        "A **class** is an architectural blueprint used to create custom"
        " objects. You set up initial properties using `__init__`."
    )

    st.markdown(
        "### Challenge 10: What keyword creates a new class blueprint?"
    )
    if st.button("object Car:", key="m10_b1"):
      st.session_state.m10_status = "wrong"
      st.rerun()
    if st.button("class Car:", key="m10_b2"):
      if st.session_state.m10_status != "correct":
        st.session_state.score += 30
      st.session_state.m10_status = "correct"
      st.rerun()

    if st.session_state.m10_status == "correct":
      st.success("🎉 Spot on! `class` defines blueprints in Python. (+30 XP)")
    elif st.session_state.m10_status == "wrong":
      st.error("❌ Not quite! Python uses the `class` keyword.")

  # --- MODULE 11 ---
  elif idx == 10:
    st.subheader("Module 11: Lambdas (The Ninja Shortcut)")
    st.write(
        "A **lambda** is a tiny, anonymous one-line function used when you"
        " don't want to write a full `def` block."
    )

    st.markdown(
        "### Challenge 11: Which keyword creates a quick one-line anonymous"
        " function?"
    )
    if st.button("lambda x: x * 2", key="m11_b1"):
      if st.session_state.m11_status != "correct":
        st.session_state.score += 30
      st.session_state.m11_status = "correct"
      st.rerun()
    if st.button("shortcut x: x * 2", key="m11_b2"):
      st.session_state.m11_status = "wrong"
      st.rerun()

    if st.session_state.m11_status == "correct":
      st.success("🎉 Incredible! `lambda` is your quick one-liner. (+30 XP)")
    elif st.session_state.m11_status == "wrong":
      st.error("❌ Incorrect! Python uses the keyword `lambda`.")

  # --- MODULE 12 ---
  elif idx == 11:
    st.subheader("Module 12: APIs & JSON (The Internet Wire)")
    st.write(
        "To talk to other servers on the internet, Python sends web requests and"
        " parses data packs called **JSON** (JavaScript Object Notation)."
    )

    st.markdown(
        "### Challenge 12: Which standard module helps parse JSON data packets"
        " into Python dictionaries?"
    )
    if st.button("import json", key="m12_b1"):
      if st.session_state.m12_status != "correct":
        st.session_state.score += 35
      st.session_state.m12_status = "correct"
      st.rerun()
    if st.button("import internet", key="m12_b2"):
      st.session_state.m12_status = "wrong"
      st.rerun()

    if st.session_state.m12_status == "correct":
      st.success(
          "🎉 Magnificent! `json` converts web responses into usable data."
          " (+35 XP)"
      )
    elif st.session_state.m12_status == "wrong":
      st.error("❌ Incorrect! Python uses the `json` module.")

  st.divider()

  # --- NEXT / PREVIOUS CHAPTER CONTROLS ---
  col_prev, col_next = st.columns(2)

  with col_prev:
    if st.session_state.module_index > 0:
      if st.button("⬅ Previous Chapter"):
        st.session_state.module_index -= 1
        st.rerun()

  with col_next:
    if st.session_state.module_index < len(modules_list) - 1:
      if st.button("Next Chapter ➡"):
        st.session_state.module_index += 1
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
    * **`print()`** $\rightarrow$ **The Voice Box:** Screams text onto the screen.
    * **Variable** $\rightarrow$ **The Backpack:** A labeled pocket storing data.
    * **`if / else`** $\rightarrow$ **The Fork in the Road:** Decision maker.
    * **`for / while`** $\rightarrow$ **The Treadmill:** Automatic loop repetition.
    * **`def`** $\rightarrow$ **The Mini-Machine:** Reusable custom functions.
    * **List `[]`** $\rightarrow$ **The Filing Cabinet:** Ordered rows of items.
    * **`import`** $\rightarrow$ **The Toolbelt:** Bringing in pre-made external toolkits.
    * **`try / except`** $\rightarrow$ **The Safety Net:** Catching errors gracefully.
    * **`open()`** $\rightarrow$ **The Diary:** Reading and writing hard-drive files.
    * **`class`** $\rightarrow$ **The Blueprint:** Object-oriented design patterns.
    * **`lambda`** $\rightarrow$ **The Ninja Shortcut:** One-line anonymous functions.
    * **`json`** $\rightarrow$ **The Internet Wire:** Parsing web application data packets.
    """
  )

# Sidebar Stats Tracker
st.sidebar.markdown("### 📊 Player Status")
st.sidebar.metric("Total XP Score", f"{st.session_state.score} XP")
st.sidebar.success(
    f"Active Chapter: {st.session_state.module_index + 1} of"
    f" {len(modules_list)}"
)
