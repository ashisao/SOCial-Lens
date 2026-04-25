# SOCialLens

SOCialLens is a log analysis and threat detection tool that simulates SOC (Security Operations Center) workflows by identifying suspicious activity such as failed logins, abnormal IP behavior, and potential brute-force attacks.

## Features

- Log parsing and analysis  
- Detection of failed login attempts  
- Suspicious IP identification  
- Risk scoring system (0–100)  
- Severity classification (Low, Medium, High)  
- Alert generation for anomalous activity  
- Downloadable incident report  
- Clean SOC-style dashboard using Streamlit  

## Tech Stack

- Python  
- Streamlit  
- Regex (log parsing)  

## How it Works

1. User pastes system logs  
2. Logs are parsed for failed attempts and IP activity  
3. Suspicious patterns are detected  
4. Risk score and severity are calculated  
5. Alerts are generated and displayed  
6. User can download an incident report  

## Live Demo

https://your-sociallens-link.streamlit.app

## Use Case

SOCialLens simulates a SOC Level 1 analyst workflow by analyzing logs, identifying anomalies, and prioritizing potential security threats.
