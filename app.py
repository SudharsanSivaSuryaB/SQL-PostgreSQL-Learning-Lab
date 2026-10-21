import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="SQL & PostgreSQL Interactive Course",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

home_icon_data = base64.b64encode(
    (Path(__file__).parent / "assets" / "home-icon.png").read_bytes()
).decode("ascii")

st.markdown("""
<style>
.block-container {padding-top: 1.7rem; padding-bottom: 3rem; max-width: 1200px;}
.hero {padding: 1.5rem 1.7rem; border-radius: 18px; background: linear-gradient(120deg,#102a43,#243b53); color: white; margin-bottom: 1rem;}
.hero h1 {color:white; margin-bottom:.35rem;}
.hero p {color:#e6f0fa; font-size:1.05rem;}
.lesson-card {padding: 1rem 1.1rem; border: 1px solid rgba(128,128,128,.28); border-radius: 14px; margin: .4rem 0;}
.small-muted {opacity:.8; font-size:.9rem;}
.stProgress > div > div > div > div {background-color: #2e8b78;}
.st-key-course_home_nav {
  position: relative;
  top: 48px;
  left: clamp(-108px, -6vw, -64px);
  z-index: 5;
}
.st-key-session_cover_0,
.st-key-session_cover_1,
.st-key-session_cover_2,
.st-key-session_cover_3,
.st-key-session_cover_4,
.st-key-session_cover_5,
.st-key-session_cover_6,
.st-key-session_cover_7 {
  scroll-margin-top: 76px;
}
.st-key-session_cover_0 [data-testid="stImage"] img,
.st-key-session_cover_1 [data-testid="stImage"] img,
.st-key-session_cover_2 [data-testid="stImage"] img,
.st-key-session_cover_3 [data-testid="stImage"] img,
.st-key-session_cover_4 [data-testid="stImage"] img,
.st-key-session_cover_5 [data-testid="stImage"] img,
.st-key-session_cover_6 [data-testid="stImage"] img,
.st-key-session_cover_7 [data-testid="stImage"] img {
  width: 100% !important;
  max-width: 100%;
  height: max(200px, min(675px, calc(100vh - 160px)));
  max-height: none;
  object-fit: contain;
  background-color: #0B1220;
}
.st-key-course_home_nav button {
  width: 30px;
  height: 30px;
  padding: 0;
  font-size: 0;
  color: transparent;
  background-color: transparent;
  background-image: url("data:image/png;base64,__HOME_ICON__");
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  border: 0;
  box-shadow: none;
}
</style>
""".replace("__HOME_ICON__", home_icon_data), unsafe_allow_html=True)

SESSIONS = [
{
"title":"1. SQL and Database Fundamentals",
"subtitle":"Understand databases, DBMS, SQL, PostgreSQL, and SQL command categories.",
"objectives":["Explain database, DBMS, SQL, and PostgreSQL in simple words.","Classify DDL, DML, DQL, DCL, and transaction-control commands.","Recognize SQL as a declarative language."],
"sections":[
("Core concepts", """A **database** is an organized collection of electronic information. A **DBMS** is software that defines structures, stores and retrieves records, controls access, and coordinates concurrent activity. **SQL** is the common language used to communicate with relational database systems. SQL is declarative: you describe the result or change you want, and the database chooses how to execute it."""),
("SQL command categories", """- **DDL** — Data Definition Language: `CREATE`, `ALTER`, `DROP`; changes structures.
- **DML** — Data Manipulation Language: `INSERT`, `UPDATE`, `DELETE`; changes rows.
- **DQL** — Data Query Language: `SELECT`; reads data.
- **DCL** — Data Control Language: `GRANT`, `REVOKE`; manages permissions.
- **TCL / transaction control** — `COMMIT`, `ROLLBACK`; saves or undoes a transaction."""),
("PostgreSQL note", """PostgreSQL (Postgres) is an open-source object-relational DBMS with transactions, foreign keys, subqueries, triggers, user-defined types and functions, and advanced query features. SQL dialects can differ; syntax such as `LIMIT`, `COPY`, and some `ALTER COLUMN` forms may not be universal."""),
],
"example":"-- Read all rows from a table\nSELECT * FROM customer;",
"challenge":"Classify each command: CREATE TABLE, INSERT, SELECT, GRANT, ROLLBACK.",
"answer":"CREATE TABLE → DDL; INSERT → DML; SELECT → DQL; GRANT → DCL; ROLLBACK → transaction control.",
"quiz":[
("Which command category is mainly used to read data?",["DDL","DML","DQL","DCL"],2,"DQL groups read queries such as SELECT."),
("Which statement is true about SQL?",["It is only for creating tables","It is declarative","It only works with PostgreSQL","It cannot update records"],1,"SQL describes the desired result or change; the DBMS determines an execution plan."),
("Which command undoes uncommitted transaction work?",["DROP","REVOKE","ROLLBACK","ALTER"],2,"ROLLBACK undoes the transaction's uncommitted work.")
]},
{
"title":"2. Tables, Data Types and Relationships",
"subtitle":"Design tables and protect data with constraints and keys.",
"objectives":["Choose appropriate PostgreSQL data types.","Use NOT NULL, DEFAULT, UNIQUE, CHECK, PRIMARY KEY, and FOREIGN KEY.","Explain simple and composite keys."],
"sections":[
("Data types", """Common PostgreSQL types in the guide: `INTEGER` / `INT` for whole numbers; `NUMERIC(precision, scale)` for exact decimals such as prices; `VARCHAR(n)` or `TEXT` for strings; `DATE`, `TIME`, and `TIMESTAMP` for date/time values; and `BOOLEAN` for true/false. Choose a type that matches the meaning of the data."""),
("Constraints", """- `NOT NULL`: a value must be supplied.
- `DEFAULT`: supplies a value when one is omitted.
- `UNIQUE`: prevents duplicate constrained values or combinations.
- `CHECK`: requires a condition such as `age >= 0`.
- `PRIMARY KEY`: uniquely identifies each row and cannot be NULL.
- `FOREIGN KEY`: requires a value to refer to a valid key in another table, subject to nullability and configured rules."""),
("Keys and relationships", """A primary key can be one column or a combination of columns. A composite key uses multiple columns together. A foreign key links a row to a key in another table and protects referential integrity—for example, an order should not point to a customer that does not exist."""),
],
"example":"CREATE TABLE customer (\n    cust_id INTEGER PRIMARY KEY,\n    first_name VARCHAR(60) NOT NULL,\n    age INTEGER CHECK (age >= 0),\n    email_id VARCHAR(255) UNIQUE,\n    status VARCHAR(20) DEFAULT 'active'\n);",
"challenge":"A customer must have a unique ID and a first name. Age cannot be negative. Which constraints would you choose?",
"answer":"Use cust_id INTEGER PRIMARY KEY, first_name ... NOT NULL, and age INTEGER CHECK (age >= 0).",
"quiz":[
("Which constraint prevents negative ages when written as CHECK (age >= 0)?",["UNIQUE","CHECK","DEFAULT","FOREIGN KEY"],1,"CHECK enforces a Boolean condition on values."),
("What does a primary key guarantee?",["Every row has a unique, non-NULL key","All columns are text","Rows are automatically sorted","The table cannot be changed"],0,"Primary-key values uniquely identify rows and cannot be NULL."),
("What is a composite primary key?",["A key in a separate database","A key made from multiple columns","A nullable key","A key that allows duplicates"],1,"The combination of columns uniquely identifies the row.")
]},
{
"title":"3. INSERT and SELECT",
"subtitle":"Add records and retrieve the data you need.",
"objectives":["Insert one or more rows with explicit column lists.","Use SELECT to return chosen columns or all columns.","Understand DISTINCT and aliases."],
"sections":[
("INSERT safely", """`INSERT` adds rows. Prefer an explicit column list because it documents what each value means and avoids depending on the table's physical column order. Values must match the listed columns in order and have compatible types. Omitted columns receive their default, NULL if permitted, or an error if required with no default."""),
("Multiple rows and COPY", """You can add multiple rows in one `INSERT ... VALUES` statement. Primary-key values must remain unique. PostgreSQL `COPY` can load files efficiently; server-side `COPY` reads a file accessible to the database server, while psql's `\\copy` reads from the client computer."""),
("SELECT, DISTINCT, aliases", """`SELECT first_name, email_id FROM customer;` returns chosen columns. `SELECT * FROM customer;` returns every column. `DISTINCT` removes duplicate result rows; when multiple columns are selected, it removes duplicate combinations. `AS` gives an output column or table a temporary readable alias; it does not rename the underlying column."""),
],
"example":"INSERT INTO customer (cust_id, first_name, age, email_id)\nVALUES (2, 'Dee', 22, 'd@example.com');\n\nSELECT first_name, email_id\nFROM customer;",
"challenge":"Write an INSERT for customer ID 5, first name 'Mia', age 28. Then select only the first name and age.",
"answer":"INSERT INTO customer (cust_id, first_name, age) VALUES (5, 'Mia', 28); SELECT first_name, age FROM customer;",
"quiz":[
("Why is an explicit INSERT column list recommended?",["It encrypts data","It avoids depending on table column order","It sorts the table","It makes all columns unique"],1,"A column list documents which values go into which columns."),
("What does SELECT DISTINCT city, age return?",["Unique cities only","Unique ages only","Unique city-and-age combinations","All rows in random order"],2,"DISTINCT applies to the entire selected row combination."),
("Does an alias rename the underlying database column?",["Yes, permanently","Only after COMMIT","No, it changes the query output label","Only in PostgreSQL"],2,"Aliases are temporary names in the query result.")
]},
{
"title":"4. Filtering, Sorting and Limiting",
"subtitle":"Find the exact records you want.",
"objectives":["Filter rows with WHERE and logical operators.","Use IN, BETWEEN, LIKE, and PostgreSQL ILIKE.","Sort results and limit returned rows."],
"sections":[
("WHERE and logic", """`WHERE` keeps rows that satisfy a condition. Comparisons include `=`, `<>`, `<`, `>`, `<=`, and `>=`. `AND` requires both conditions; `OR` requires at least one; `NOT` reverses a condition. Use parentheses to make complex logic clear. Text literals use single quotes."""),
("IN, BETWEEN, LIKE", """`IN` matches one of several values. `BETWEEN` checks an inclusive range, so both endpoints count. With `LIKE`, `%` matches zero or more characters and `_` matches exactly one character. PostgreSQL also offers `ILIKE` for case-insensitive pattern matching."""),
("ORDER BY and LIMIT", """`ORDER BY` controls presentation order; without it, row order is not guaranteed. `ASC` is ascending and is the default; `DESC` is descending. PostgreSQL `LIMIT` caps the number of returned rows. When selecting top rows, sort first; stable pagination should use a unique tie-breaker where appropriate."""),
],
"example":"SELECT first_name, age\nFROM customer\nWHERE age BETWEEN 20 AND 30\n  AND first_name ILIKE 'a%'\nORDER BY age DESC\nLIMIT 10;",
"challenge":"Find customers in either 'Chennai' or 'Coimbatore', age 18 or older, sorted from oldest to youngest.",
"answer":"SELECT * FROM customer WHERE city IN ('Chennai', 'Coimbatore') AND age >= 18 ORDER BY age DESC;",
"quiz":[
("What does BETWEEN 20 AND 30 include?",["Only 20 and 30","Values greater than 20 and less than 30","Both endpoints and values between them","Only values below 30"],2,"BETWEEN is inclusive at both endpoints."),
("In LIKE 'Jo%', what does % mean?",["Exactly one character","Zero or more characters","A number only","A space"],1,"% matches zero or more characters."),
("What should you add when result order matters?",["DEFAULT","ORDER BY","CHECK","ROLLBACK"],1,"Without ORDER BY, row order is not guaranteed.")
]},
{
"title":"5. UPDATE, DELETE and ALTER TABLE",
"subtitle":"Change data and schemas without accidental damage.",
"objectives":["Update and delete matching rows safely.","Explain what happens when WHERE is omitted.","Use ALTER TABLE to evolve a schema."],
"sections":[
("UPDATE and DELETE", """`UPDATE` modifies values in rows matching a condition; `DELETE` removes matching rows. If `WHERE` is omitted from UPDATE, every row is updated. If `WHERE` is omitted from DELETE, all rows are deleted while the table structure remains. `DROP TABLE` is different: it removes the table itself."""),
("A safety checklist", """1. Run a `SELECT` with the exact `WHERE` condition first.
2. Confirm the matching rows and expected count.
3. Use a transaction for important multi-step edits when appropriate.
4. Check backups and permissions.
5. Execute UPDATE or DELETE only after checking."""),
("ALTER TABLE", """PostgreSQL `ALTER TABLE` can add or drop columns, change a column's type, rename a column, or add constraints such as CHECK, PRIMARY KEY, and FOREIGN KEY. Existing rows must satisfy a newly added constraint or the command may fail. Dropping columns or changing types can affect applications and data."""),
],
"example":"-- Preview first\nSELECT * FROM customer WHERE cust_id = 2;\n\n-- Then update the intended row\nUPDATE customer\nSET age = 23\nWHERE cust_id = 2;\n\nALTER TABLE customer ADD COLUMN phone VARCHAR(30);",
"challenge":"Before deleting customers older than 90, what query should you run first and why?",
"answer":"Run SELECT * FROM customer WHERE age > 90; inspect the rows and count before running DELETE with the same WHERE condition.",
"quiz":[
("What happens if UPDATE has no WHERE clause?",["It updates no rows","It updates every row","It drops the table","It creates a backup"],1,"Without WHERE, every row in the table is updated."),
("What does DELETE FROM customer without WHERE do?",["Removes all rows but keeps the table","Removes only duplicate rows","Removes the table structure","Changes every age to NULL"],0,"DELETE removes rows; DROP TABLE removes the table itself."),
("What is a good first step before a destructive DELETE?",["Run a SELECT with the same condition","Run DROP TABLE","Remove all constraints","Use LIMIT without checking"],0,"Preview the exact rows that will be affected.")
]},
{
"title":"6. Aggregate Functions and GROUP BY",
"subtitle":"Turn individual rows into useful summaries.",
"objectives":["Use COUNT, SUM, AVG, MIN, and MAX.","Group rows by category.","Explain WHERE versus HAVING."],
"sections":[
("Aggregate functions", """`COUNT(*)` counts rows, including rows where some columns are NULL. `COUNT(column)` counts non-NULL values in that column. `COUNT(DISTINCT column)` counts distinct non-NULL values. `SUM` totals numeric values, `AVG` calculates an average, and `MIN` / `MAX` find the smallest / largest value."""),
("GROUP BY", """`GROUP BY` forms groups that share values in specified columns, allowing an aggregate for each group. For example, group sales by product to calculate quantity sold per product. A selected non-aggregated column generally must appear in GROUP BY, subject to database rules."""),
("WHERE versus HAVING", """`WHERE` filters individual rows before grouping. `HAVING` filters groups after aggregate values are calculated. Example flow: filter active customers with WHERE, group by region, then keep regions with at least ten customers using HAVING."""),
],
"example":"SELECT region, COUNT(*) AS customer_count\nFROM customer\nWHERE status = 'active'\nGROUP BY region\nHAVING COUNT(*) >= 10\nORDER BY customer_count DESC;",
"challenge":"The sales table has product_id and quantity. Calculate total quantity sold per product, highest total first.",
"answer":"SELECT product_id, SUM(quantity) AS qty_sold FROM sales GROUP BY product_id ORDER BY qty_sold DESC;",
"quiz":[
("What does COUNT(column) ignore?",["All numeric values","NULL values in that column","Duplicate table names","Rows with zero"],1,"COUNT(column) counts non-NULL values only."),
("When is HAVING applied in the logical query model?",["Before WHERE","After groups and aggregates are calculated","Before FROM","Only after LIMIT"],1,"HAVING filters groups after grouping."),
("Which clause summarizes rows per category?",["GROUP BY","ORDER BY","ALTER TABLE","DEFAULT"],0,"GROUP BY forms groups based on selected column values.")
]},
{
"title":"7. SQL Functions and Transactions",
"subtitle":"Transform values and make related changes safely.",
"objectives":["Recognize common string, date/time, and numeric functions.","Explain transaction commands.","Describe the four ACID properties."],
"sections":[
("String, date/time, and numeric functions", """String functions include `UPPER`, `LOWER`, `TRIM`, `LTRIM`, `RTRIM`, `REPLACE`, `SUBSTRING`, `CONCAT`, and `STRING_AGG`. PostgreSQL date/time values include `CURRENT_DATE`, `CURRENT_TIME`, and `CURRENT_TIMESTAMP`. Numeric helpers include `CEIL` / `CEILING`, `FLOOR`, and PostgreSQL's `RANDOM()` and `SETSEED()`."""),
("Transactions", """A transaction groups changes so they can be committed as a unit or rolled back. `BEGIN` starts a transaction; `COMMIT` saves the transaction; `ROLLBACK` undoes uncommitted work. This is useful for operations such as transferring money, where both account updates should succeed together."""),
("ACID", """- **Atomicity**: all steps happen, or none do.
- **Consistency**: rules and constraints remain satisfied.
- **Isolation**: concurrent transactions are managed so they do not interfere incorrectly.
- **Durability**: committed changes persist according to DBMS guarantees."""),
],
"example":"BEGIN;\nUPDATE account SET balance = balance - 100 WHERE account_id = 1;\nUPDATE account SET balance = balance + 100 WHERE account_id = 2;\nCOMMIT;",
"challenge":"A transfer subtracts money from one account, but the second update fails before COMMIT. What command can undo the uncommitted work?",
"answer":"ROLLBACK. It undoes the transaction's uncommitted changes.",
"quiz":[
("Which function removes leading and trailing spaces?",["TRIM","SUM","FLOOR","COUNT"],0,"TRIM removes leading and trailing spaces or specified characters."),
("What does Atomicity mean?",["Changes are sorted","All transaction steps happen or none do","Rows are always isolated forever","Data is stored as text"],1,"Atomicity treats the transaction as one unit."),
("Which command saves a transaction?",["ROLLBACK","DROP","COMMIT","REVOKE"],2,"COMMIT completes and saves the transaction.")
]},
{
"title":"8. Integrated SQL Project and Final Assessment",
"subtitle":"Combine the course skills in a small customer and sales analysis project.",
"objectives":["Read and reason about a query in logical order.","Combine customer and orders tables using JOIN.","Aggregate spending and filter groups with HAVING.","Review common SQL mistakes and safe habits."],
"sections":[
("Logical reading order", """A useful logical model for SELECT is: FROM and joins identify source rows → WHERE filters individual rows → GROUP BY forms groups → HAVING filters groups → SELECT produces output expressions → DISTINCT removes duplicate output rows → ORDER BY sorts output → LIMIT restricts the returned result. A DBMS may physically optimize execution differently while preserving the logical result."""),
("Integrated example", """The guide's example uses `customer(cust_id, first_name, city, age)` and `orders(order_id, customer_id, order_date, total)`. A join connects orders to customers through `orders.customer_id = customer.cust_id`. Group by customer to calculate spending, then use HAVING to retain customers whose total exceeds 500."""),
("Common mistakes to avoid", """- Forgetting WHERE in UPDATE or DELETE.
- Omitting an explicit column list in INSERT.
- Reusing a primary-key value.
- Expecting natural row order without ORDER BY.
- Comparing NULL with `=` instead of using `IS NULL` or `IS NOT NULL`.
- Confusing WHERE with HAVING.
- Joining on the wrong columns.
- Assuming all SQL database products use identical syntax."""),
],
"example":"SELECT c.cust_id, c.first_name, SUM(o.total) AS total_spent\nFROM customer AS c\nJOIN orders AS o ON o.customer_id = c.cust_id\nGROUP BY c.cust_id, c.first_name\nHAVING SUM(o.total) > 500\nORDER BY total_spent DESC;",
"challenge":"Explain the integrated query in your own words: what connects the tables, what is calculated, and which customers remain?",
"answer":"The JOIN connects each order to its customer using customer IDs. SUM(o.total) calculates spending per customer. GROUP BY creates one group per customer. HAVING keeps customers whose total spending is greater than 500. ORDER BY shows the highest spenders first.",
"quiz":[
("Which condition correctly checks for missing city values?",["city = NULL","city == NULL","city IS NULL","city IN NULL"],2,"Use IS NULL or IS NOT NULL to test NULL values."),
("Which clause filters groups based on total spending?",["WHERE SUM(o.total) > 500","HAVING SUM(o.total) > 500","ORDER BY SUM(o.total)","LIMIT SUM(o.total)"],1,"HAVING filters grouped results using an aggregate condition."),
("What is the purpose of JOIN ... ON in the project query?",["Rename columns","Connect related rows from customer and orders","Delete duplicate customers","Start a transaction"],1,"The ON condition specifies how records from the tables relate.")
]}
]

def init_state():
    st.session_state.setdefault("completed", [])
    st.session_state.setdefault("quiz_answers", {})
    st.session_state.setdefault("revealed_challenges", [])
    st.session_state.setdefault("flash_index", 0)

init_state()

PAGES = ["Course Home"] + [s["title"] for s in SESSIONS] + ["Flashcards", "Final Assessment", "Resources"]

st.sidebar.title("🧠 SQL Learning Lab")
st.sidebar.caption("SQL & PostgreSQL • 8-session course")

def navigate_to(destination, tab_label="Learn"):
    """Update navigation from a widget callback, before its widget is created."""
    st.session_state["navigation"] = destination
    destination_idx = next(
        (i for i, session in enumerate(SESSIONS) if session["title"] == destination),
        None,
    )
    if destination_idx is not None:
        st.session_state[f"session_tabs_{destination_idx}"] = tab_label
        st.session_state["scroll_target"] = "session_cover"
        st.session_state["collapse_sidebar"] = True

def select_session_tab(tab_key, tab_label):
    """Switch lesson tabs from a callback before the tab widget is instantiated."""
    st.session_state[tab_key] = tab_label
    st.session_state["scroll_target"] = "session_tabs"

page = st.sidebar.selectbox(
    "Go to",
    PAGES,
    key="navigation",
    label_visibility="collapsed",
    help="Choose a course section or lesson.",
)
completed = set(st.session_state.completed)
progress = len(completed) / len(SESSIONS)
st.sidebar.progress(progress)
st.sidebar.write(f"**Progress:** {len(completed)} / {len(SESSIONS)} sessions")
st.sidebar.caption("Progress lasts for this browser session.")
if page != "Course Home":
    st.button(
        "⌂",
        key="course_home_nav",
        on_click=navigate_to,
        args=("Course Home",),
        help="Course Home",
    )

def show_quiz(session, prefix):
    st.subheader("🧩 Quick knowledge check")
    score = 0
    answered = 0
    for i, (question, options, correct, explanation) in enumerate(session["quiz"]):
        key = f"{prefix}_q{i}"
        choice = st.radio(question, options, key=key, index=None)
        if choice is not None:
            answered += 1
            is_correct = options.index(choice) == correct
            if is_correct:
                score += 1
                st.success("Correct! " + explanation)
            else:
                st.error("Not quite. " + explanation)
    if answered:
        st.info(f"Current score: {score}/{answered}. Try again after reviewing the explanations.")
    return score, answered

def show_session(session, idx):
    cover_images = {
        0: "session-1-fundamentals.png",
        1: "session-2-tables-data-types.png",
        2: "session-3-insert-select.png",
        3: "session-4-filtering-sorting-limiting.png",
        4: "session-5-update-delete-alter.png",
        5: "session-6-aggregates-group-by.png",
        6: "session-7-functions-transactions.png",
        7: "session-8-integrated-assessment.png",
    }
    with st.container(key=f"session_cover_{idx}"):
        if idx in cover_images:
            cover_path = Path(__file__).parent / "assets" / cover_images[idx]
            st.image(cover_path, use_container_width=True)
        st.title(session["title"])
        st.write(session["subtitle"])
        st.caption(f"Session {idx+1} of {len(SESSIONS)} • Suggested time: 30–45 minutes")
        st.subheader("🎯 Learning objectives")
        for obj in session["objectives"]:
            st.markdown(f"- {obj}")
    tab_key = f"session_tabs_{idx}"
    tabs = st.tabs(
        ["Learn", "Code example", "Challenge", "Quiz"],
        key=tab_key,
        default="Learn",
        on_change="rerun",
    )
    scroll_target = st.session_state.pop("scroll_target", None)
    collapse_sidebar = st.session_state.pop("collapse_sidebar", False)
    if scroll_target or collapse_sidebar:
        target_class = f"session_cover_{idx}" if scroll_target == "session_cover" else tab_key
        st.html(
            f"""<script>
            setTimeout(() => {{
                const sidebar = document.querySelector('[data-testid="stSidebar"]');
                const collapseButton = document.querySelector('[data-testid="stSidebarCollapseButton"] button');
                if ({str(collapse_sidebar).lower()} && sidebar?.getAttribute('aria-expanded') === 'true' && collapseButton) {{
                    collapseButton.click();
                }}
                const target = document.querySelector('.st-key-{target_class}');
                if (target) target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}, 150);
            </script>""",
            unsafe_allow_javascript=True,
        )
    with tabs[0]:
        for heading, body in session["sections"]:
            with st.expander(heading, expanded=True):
                st.markdown(body)
        _, next_col = st.columns([5, 1])
        next_col.button(
            "Next →",
            key=f"tab_next_code_{idx}",
            on_click=select_session_tab,
            args=(tab_key, "Code example"),
            type="primary",
            use_container_width=True,
        )
    with tabs[1]:
        st.markdown("Review the example and explain each clause before moving on.")
        st.code(session["example"], language="sql")
        st.button("Copying tip: select the code and use Ctrl+C", key=f"copytip{idx}", disabled=True)
        _, next_col = st.columns([5, 1])
        next_col.button(
            "Next →",
            key=f"tab_next_challenge_{idx}",
            on_click=select_session_tab,
            args=(tab_key, "Challenge"),
            type="primary",
            use_container_width=True,
        )
    with tabs[2]:
        st.markdown(f"**Your task:** {session['challenge']}")
        response = st.text_area("Write your answer or SQL here", key=f"challenge_{idx}", height=120, placeholder="Try it yourself before revealing the solution...")
        if st.button("Reveal suggested answer", key=f"reveal_{idx}"):
            if idx not in st.session_state.revealed_challenges:
                st.session_state.revealed_challenges.append(idx)
        if idx in st.session_state.revealed_challenges:
            st.success("Suggested answer")
            st.code(session["answer"], language="sql" if "SELECT" in session["answer"] or "INSERT" in session["answer"] or "ROLLBACK" in session["answer"] else "text")
        st.caption("The suggested answer is one valid approach; wording or SQL may vary.")
        _, next_col = st.columns([5, 1])
        next_col.button(
            "Next →",
            key=f"tab_next_quiz_{idx}",
            on_click=select_session_tab,
            args=(tab_key, "Quiz"),
            type="primary",
            use_container_width=True,
        )
    with tabs[3]:
        score, answered = show_quiz(session, f"session{idx}")
        if answered == len(session["quiz"]) and score == len(session["quiz"]):
            if idx not in st.session_state.completed:
                st.session_state.completed.append(idx)
                st.rerun()
        is_done = idx in st.session_state.completed
        previous_col, next_col = st.columns(2)
        if idx > 0:
            previous_col.button(
                "← Previous session",
                on_click=navigate_to,
                args=(SESSIONS[idx-1]["title"],),
                key=f"prev{idx}",
                use_container_width=True,
            )
        if idx < len(SESSIONS)-1:
            next_col.button(
                "Next session →",
                on_click=navigate_to,
                args=(SESSIONS[idx+1]["title"],),
                key=f"next{idx}",
                disabled=not is_done,
                type="primary" if is_done else "secondary",
                help="Answer every quiz question correctly to unlock the next session." if not is_done else None,
                use_container_width=True,
            )
    st.divider()

if page == "Course Home":
    st.markdown("""
    <div class="hero">
      <h1>SQL & PostgreSQL Interactive Course</h1>
      <p>Learn in eight sessions through concise lessons, code examples, challenges, flashcards, and quizzes.</p>
    </div>
    """, unsafe_allow_html=True)
    a,b,c = st.columns(3)
    a.metric("Sessions", "8")
    b.metric("Completed", f"{len(completed)}/8")
    c.metric("Course progress", f"{int(progress*100)}%")
    st.progress(progress)
    st.markdown("### Your learning path")
    st.write("Follow the sessions in order. Each session includes learning objectives, source-based explanations, a SQL example, a challenge, and a short quiz.")
    for i, s in enumerate(SESSIONS):
        with st.container(border=True):
            left, right = st.columns([5,1])
            left.markdown(f"**{s['title']}**")
            left.caption(s["subtitle"])
            right.markdown("✅ Complete" if i in completed else "⬜ Not started")
            st.button(
                "Continue learning →" if i not in completed else "Review session →",
                key=f"open_home_{i}",
                on_click=navigate_to,
                args=(s["title"],),
                type="primary" if i == len(completed) else "secondary",
            )
    st.markdown("### Suggested study routine")
    st.markdown("1. Read the explanation.\n2. Trace the SQL example line by line.\n3. Attempt the challenge without revealing the answer.\n4. Take the quiz and revisit any missed concept.\n5. Once every quiz answer is correct, continue to the next session.")
    st.info("This version focuses on learning interactions. It does not execute arbitrary SQL inside the app; use the PostgreSQL playground in Resources for real query execution.")

elif page in [s["title"] for s in SESSIONS]:
    idx = next(i for i,s in enumerate(SESSIONS) if s["title"] == page)
    show_session(SESSIONS[idx], idx)

elif page == "Flashcards":
    st.title("🃏 Flashcards")
    cards = [
        ("What is SQL?", "Structured Query Language; used to communicate with relational database systems."),
        ("What is DDL?", "Data Definition Language. Examples: CREATE, ALTER, DROP."),
        ("What is a primary key?", "A unique, non-NULL identifier for each row."),
        ("What is a foreign key?", "A column or set of columns that references a key in another table."),
        ("What does DISTINCT do?", "Removes duplicate result rows."),
        ("What does BETWEEN do?", "Checks an inclusive range; both endpoints count."),
        ("What does GROUP BY do?", "Forms groups that share values so aggregates can be calculated per group."),
        ("WHERE vs HAVING?", "WHERE filters rows before grouping; HAVING filters groups after aggregation."),
        ("What does ROLLBACK do?", "Undoes uncommitted transaction work."),
        ("What does ACID stand for?", "Atomicity, Consistency, Isolation, Durability."),
        ("How do you test for NULL?", "Use IS NULL or IS NOT NULL, not = NULL."),
        ("Why use ORDER BY?", "To request a defined result order.")
    ]
    i = st.session_state.flash_index % len(cards)
    q,a = cards[i]
    st.caption(f"Card {i+1} of {len(cards)}")
    with st.container(border=True):
        st.subheader(q)
        if st.button("Show answer", key="flash_show"):
            st.session_state["flash_show_answer"] = True
        if st.session_state.get("flash_show_answer"):
            st.success(a)
    x,y = st.columns(2)
    if x.button("← Previous card"):
        st.session_state.flash_index = (i-1) % len(cards)
        st.session_state["flash_show_answer"] = False
        st.rerun()
    if y.button("Next card →"):
        st.session_state.flash_index = (i+1) % len(cards)
        st.session_state["flash_show_answer"] = False
        st.rerun()

elif page == "Final Assessment":
    st.title("🏁 Final Assessment")
    st.write("Test the core ideas from all eight sessions. Answer all questions, then submit for your score.")
    final_questions = [
        ("Which category includes ALTER TABLE?",["DDL","DML","DQL","DCL"],0),
        ("Which constraint prevents negative values with age >= 0?",["UNIQUE","CHECK","DEFAULT","FOREIGN KEY"],1),
        ("What does SELECT DISTINCT city, age make unique?",["City only","Age only","City-age combinations","Customer IDs"],2),
        ("Which operator can match one of several values?",["IN","TRIM","COMMIT","ALTER"],0),
        ("What is the safest first step before DELETE?",["DROP TABLE","SELECT using the same WHERE","COMMIT immediately","Remove the WHERE clause"],1),
        ("Which clause filters aggregated groups?",["WHERE","HAVING","LIMIT","INSERT"],1),
        ("Which function counts all rows, including rows with NULL columns?",["COUNT(*)","COUNT(column)","SUM(*)","AVG(*)"],0),
        ("Which command undoes uncommitted changes?",["COMMIT","ROLLBACK","GRANT","CREATE"],1),
        ("Which is a correct NULL test?",["city = NULL","city IS NULL","city == NULL","city LIKE NULL"],1),
        ("What does JOIN ... ON do?",["Connects related rows","Deletes rows","Changes a data type","Starts a transaction"],0),
        ("What does ORDER BY control?",["Access permissions","Result order","Table constraints","Transaction durability"],1),
        ("Which ACID property means committed changes persist?",["Atomicity","Consistency","Isolation","Durability"],3),
    ]
    answers = []
    for i,(q,opts,correct) in enumerate(final_questions):
        choice = st.radio(f"{i+1}. {q}",opts,key=f"final_{i}",index=None)
        answers.append(None if choice is None else opts.index(choice))
    if st.button("Submit final assessment", type="primary"):
        answered = sum(x is not None for x in answers)
        score = sum(1 for i,x in enumerate(answers) if x == final_questions[i][2])
        st.session_state["final_score"] = (score, answered, len(final_questions))
        if answered < len(final_questions):
            st.warning(f"You answered {answered} of {len(final_questions)} questions. Unanswered questions count as incorrect.")
        st.metric("Your score", f"{score}/{len(final_questions)}", f"{round(score/len(final_questions)*100)}%")
        st.subheader("Answer review")
        for i, (question, options, correct) in enumerate(final_questions):
            selected = answers[i]
            selected_text = options[selected] if selected is not None else "No answer selected"
            correct_text = options[correct]
            st.markdown(f"**{i+1}. {question}**")
            st.write(f"Your answer: {selected_text}")
            if selected == correct:
                st.success(f"Correct answer: {correct_text}")
            else:
                st.error(f"Correct answer: {correct_text}")
        if score >= 10:
            st.success("Excellent work! Review the sessions where you were unsure.")
        elif score >= 7:
            st.info("Good progress. Revisit the topics you found difficult and try again.")
        else:
            st.warning("Keep practising. Review the lessons and flashcards, then retake the assessment.")
        st.caption("This is a practice score, not a formal certification.")

elif page == "Resources":
    st.title("🔗 Practice and course resources")
    st.markdown("""
    ### Run PostgreSQL queries online
    - [DB Fiddle](https://www.db-fiddle.com/) — choose PostgreSQL when available, create sample tables, and run SQL.
    - [SQL Fiddle](http://sqlfiddle.com/) — another browser-based SQL practice option; availability may vary.

    ### Suggested practice dataset
    Start with the `customer` and `orders` tables used in the course guide. Try creating them, inserting sample rows, filtering customers, joining orders, and calculating total spending.

    ### Source document
    This course structure is based on the uploaded **SQL & PostgreSQL Detailed Study Guide**. The lessons preserve its main concepts and examples while reorganizing them into eight sessions. Additional interactive activities are practice scaffolding for learning.
    """)
    pdf_path = Path(__file__).parent / "SQL_PostgreSQL_Detailed_Study_Guide.pdf"
    if pdf_path.exists():
        st.download_button("Download original study guide PDF", data=pdf_path.read_bytes(), file_name=pdf_path.name, mime="application/pdf")
    st.markdown("### Deployment")
    st.markdown("The project includes `requirements.txt` and `README.md`. You can deploy it to Streamlit Community Cloud by connecting a GitHub repository containing these files.")


