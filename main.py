from src.validation import (
    load_csv,
    standardize_columns,
    validate_schema,
    validate_missing_values,
    validate_duplicates
)


def print_validation_report(
        file_name,
        missing_columns,
        missing_values,
        duplicate_count,
        changes
):
    print("\n" + "=" * 50)
    print(f"{file_name:^50}")
    print("=" * 50)

    print(f"Missing Columns : {missing_columns if missing_columns else 'None'}")
    print(f"Missing Values  : {missing_values if missing_values else 'None'}")
    print(f"Duplicate Rows  : {duplicate_count}")

    if changes:
        print("Columns Renamed :")
        for old, new in changes.items():
            print(f"  {old}  -->  {new}")
    else:
        print("Columns Renamed : None")


def main():

    tb_path = input("Enter Trial Balance file path : ").strip()
    gl_path = input("Enter General Ledger file path : ").strip()

    tb_df = load_csv(tb_path)
    gl_df = load_csv(gl_path)

    if tb_df is None or gl_df is None:
        print("\nOne or more files could not be loaded.")
        return

    # -------------------------
    # Standardize Columns
    # -------------------------

    tb_df, tb_changes = standardize_columns(tb_df)
    gl_df, gl_changes = standardize_columns(gl_df)

    # -------------------------
    # Validation
    # -------------------------

    tb_missing_columns = validate_schema(tb_df)
    gl_missing_columns = validate_schema(gl_df)

    tb_missing_values = validate_missing_values(tb_df)
    gl_missing_values = validate_missing_values(gl_df)

    tb_duplicates = validate_duplicates(tb_df)
    gl_duplicates = validate_duplicates(gl_df)

    # -------------------------
    # Report
    # -------------------------

    print("\n")
    print("=" * 50)
    print("VALIDATION REPORT".center(50))
    print("=" * 50)

    print_validation_report(
        "TRIAL BALANCE",
        tb_missing_columns,
        tb_missing_values,
        tb_duplicates,
        tb_changes
    )

    print_validation_report(
        "GENERAL LEDGER",
        gl_missing_columns,
        gl_missing_values,
        gl_duplicates,
        gl_changes
    )


if __name__ == "__main__":
    main()