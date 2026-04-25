import streamlit as st
import re

st.set_page_config(page_title="SOCial Lens", layout="wide")

# ------------------ SIDEBAR ------------------
st.sidebar.title("SOCial Lens")
page = st.sidebar.radio("Navigation", ["Dashboard", "Analyze Logs"])

# ------------------ CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #00ff9f;
}

.stApp {
    background-color: #0e1117;
}

h1, h2, h3 {
    color: #00ff9f;
}

.stTextArea textarea {
    background-color: #1c1f26;
    color: white;
    border: 1px solid #00ff9f;
}

.stButton>button {
    background-color: #00ff9f;
    color: black;
    border-radius: 6px;
    font-weight: bold;
}

.card {
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #00ff9f;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ DASHBOARD ------------------
if page == "Dashboard":
    st.title("SOC Dashboard")

    st.markdown("""
    <div class="card">
    This tool simulates SOC log analysis by detecting suspicious patterns like brute-force attempts and abnormal IP activity.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    Use the "Analyze Logs" section to paste logs and detect threats.
    </div>
    """, unsafe_allow_html=True)

# ------------------ ANALYSIS ------------------
if page == "Analyze Logs":

    st.title("Log Analysis")

    col1, col2 = st.columns([1, 1])

    # -------- LEFT: INPUT --------
    with col1:
        st.subheader("Input Logs")

        log_input = st.text_area(
            "Paste logs here",
            height=300,
            placeholder="Example:\nFailed login from 192.168.1.10"
        )

        analyze = st.button("Analyze")

    # -------- RIGHT: OUTPUT --------
    with col2:
        st.subheader("Results")

        if analyze and log_input:

            with st.spinner("Analyzing logs... detecting anomalies..."):

                logs = log_input.split("\n")

                failed_logins = 0
                ip_count = {}

                for line in logs:

                    if "failed" in line.lower() or "invalid" in line.lower():
                        failed_logins += 1

                    ip_match = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", line)
                    if ip_match:
                        ip = ip_match.group()
                        ip_count[ip] = ip_count.get(ip, 0) + 1

                suspicious_ips = [ip for ip, count in ip_count.items() if count > 3]

                # Risk scoring
                risk_score = failed_logins * 5 + len(suspicious_ips) * 20
                risk_score = min(risk_score, 100)

                # Severity
                if risk_score >= 80:
                    severity = "HIGH"
                    color = "red"
                elif risk_score >= 40:
                    severity = "MEDIUM"
                    color = "orange"
                else:
                    severity = "LOW"
                    color = "green"

                # Metrics
                colA, colB, colC = st.columns(3)
                colA.metric("Failed Logins", failed_logins)
                colB.metric("Unique IPs", len(ip_count))
                colC.metric("Risk Score", f"{risk_score}/100")

                # Severity Card
                st.markdown(f"""
                <div style="
                    padding:20px;
                    border-radius:10px;
                    border:2px solid {color};
                    text-align:center;
                    margin-top:20px;
                ">
                    <h2 style="color:{color};">Severity: {severity}</h2>
                </div>
                """, unsafe_allow_html=True)

                # Alerts
                if suspicious_ips:
                    st.markdown("### Alerts")
                    for ip in suspicious_ips:
                        st.error(f"Suspicious activity from IP: {ip}")
                else:
                    st.success("No major suspicious activity detected")

                # ---------------- REPORT EXPORT ----------------
                report = f"""
SOCial Lens Incident Report

----------------------------------
Failed Logins: {failed_logins}
Unique IPs: {len(ip_count)}
Risk Score: {risk_score}/100
Severity: {severity}

Suspicious IPs:
"""

                if suspicious_ips:
                    for ip in suspicious_ips:
                        report += f"- {ip}\n"
                else:
                    report += "None\n"

                st.download_button(
                    label="Download Report",
                    data=report,
                    file_name="incident_report.txt",
                    mime="text/plain"
                )

        elif analyze:
            st.warning("Please paste logs first")