COLUMN_ALIASES= {
    "Account": [
        "GL",
        "General Ledger",
        "Account Name",
        "Ledger",
        "account_code"
    ],

    "Amount": [
        "Amt",
        "Balance",
        "Net Amount",
        "Trial Balance",
        "amount"
    ]
}
REQUIRED_COLUMNS = [
    "Account",
    "Amount"
]
ACCOUNT_ALIASES = {
    # Assets
    "Accounts Receivable": "Receivables",
    "Accounts Payable": "Payables",
    "Prepaid Expense": "Prepaid Expenses",
    "Prepaid Expenses": "Prepaid Expenses",

    # Revenue
    "Sales Revenue": "Sales",
    "Revenue": "Sales",
    "Service Revenue": "Service Revenue",

    # Expenses
    "Rent Expense": "Rent",
    "Salaries Expense": "Salaries",
    "Salary Expense": "Salaries",
    "Utilities Expense": "Utilities",
    "Insurance Expense": "Insurance",
    "Marketing Expense": "Marketing",
    "Depreciation Expense": "Depreciation",
    "Supplies Expense": "Supplies",
    "Interest Expense": "Interest",

    # Inventory
    "Cost Of Goods Sold": "COGS",
    "Cost Of Sales": "COGS",
}