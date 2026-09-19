
import streamlit as st
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="InstaReporter Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .status-box {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #ddd;
        background: #fafafa;
        margin-top: 15px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        background: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    '<div class="main-title">📊 InstaReporter Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Instagram reporting workflow dashboard</div>',
    unsafe_allow_html=True
)


# -----------------------------
# SESSION STATE
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []


# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    mode = st.selectbox(
        "Content Type",
        [
            "Instagram Profile",
            "Instagram Video"
        ]
    )

    st.divider()

    st.info(
        "This dashboard manages the reporting workflow. "
        "Automated mass-reporting actions are not executed from this UI."
    )


# -----------------------------
# MAIN FORM
# -----------------------------
st.subheader("🎯 Target Information")

col1, col2 = st.columns(2)

with col1:
    target = st.text_input(
        "Target Username / URL",
        placeholder="@username or Instagram URL"
    )

with col2:
    reason = st.selectbox(
        "Reason",
        [
            "Spam",
            "Scam or fraud",
            "Harassment",
            "Impersonation",
            "Inappropriate content",
            "Other"
        ]
    )


description = st.text_area(
    "Additional Notes",
    placeholder="Enter additional information..."
)


# -----------------------------
# WORKFLOW BUTTON
# -----------------------------
if st.button(
    "📋 Create Report Record",
    use_container_width=True
):

    if not target.strip():
        st.error("Please enter a target username or URL.")
    else:

        record = {
            "target": target,
            "type": mode,
            "reason": reason,
            "notes": description,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Created"
        }

        st.session_state.history.insert(0, record)

        st.success("Report workflow record created successfully.")


# -----------------------------
# STATUS
# -----------------------------
st.divider()

st.subheader("📈 Dashboard")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Total Records",
        len(st.session_state.history)
    )

with c2:
    st.metric(
        "Profile Records",
        sum(
            1
            for x in st.session_state.history
            if x["type"] == "Instagram Profile"
        )
    )

with c3:
    st.metric(
        "Video Records",
        sum(
            1
            for x in st.session_state.history
            if x["type"] == "Instagram Video"
        )
    )


# -----------------------------
# HISTORY
# -----------------------------
st.divider()

st.subheader("📝 Recent Activity")

if not st.session_state.history:

    st.info("No records created yet.")

else:

    for item in st.session_state.history:

        with st.container(border=True):

            col1, col2 = st.columns([3, 1])

            with col1:

                st.markdown(
                    f"**Target:** {item['target']}"
                )

                st.write(
                    f"**Type:** {item['type']}"
                )

                st.write(
                    f"**Reason:** {item['reason']}"
                )

                if item["notes"]:
                    st.write(
                        f"**Notes:** {item['notes']}"
                    )

            with col2:

                st.write(
                    f"🕒 {item['time']}"
                )

                st.success(
                    item["status"]
                )
