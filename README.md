# reconciliation-analysis
Automated reconciliation between General Ledger and Trial Balance using Python

# General Ledger vs Trial Balance Reconciliation

## Project Overview
This project focuses on automating the reconciliation between the General Ledger (GL) and the Trial Balance (TB), a core control process in accounting, audit, and financial reporting.

The objective is to validate that transaction-level records in the General Ledger accurately roll up to the summarized balances presented in the Trial Balance. Using Python and Pandas, the project identifies discrepancies, quantifies differences, and classifies reconciliation outcomes in a structured and interpretable manner.

---

## Business Context
Organizations rely on reconciliations between the General Ledger and Trial Balance to ensure the completeness and accuracy of financial records. Discrepancies between these datasets can arise due to missing transactions, incorrect postings, aggregation errors, or timing differences.

If unresolved, such issues may lead to inaccurate financial statements, audit findings, and compliance risks. Automating this reconciliation process improves reliability, efficiency, and audit readiness.

---

## Methodology
The reconciliation process follows these key steps:

1. Load and validate General Ledger and Trial Balance datasets
2. Aggregate General Ledger transactions by account
3. Align summarized GL balances with Trial Balance balances
4. Calculate differences between GL and TB amounts
5. Classify accounts as matched or mismatched based on reconciliation results
6. Present clear reconciliation outputs for analysis and review

---

## Tools and Technologies
- Python  
- Pandas  
- NumPy  
- Jupyter Notebook  

---

## Key Outcomes
- Automated identification of mismatches between GL and TB balances  
- Quantification of discrepancies at the account level  
- Scalable reconciliation logic applicable to real-world financial systems  

---

## Skills Demonstrated
- Financial data analysis and reconciliation
- Data validation and completeness testing
- Data aggregation and comparison using Pandas
- Translating technical results into business-relevant insights
- Applying programming concepts to finance and audit use cases

---

## Repository Structure
gl-tb-reconciliation-analysis/
│
├── GL_TB_Reconciliation.ipynb
├── general_ledger.csv
├── trial_balance.csv
├── README.md
└── requirements.txt


---

## Notes
The datasets used in this project are simulated for learning purposes but are designed to closely resemble real-world financial data structures commonly used in corporate accounting systems.
