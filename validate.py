import pandas as pd

expected_schema = {
    "project_number": float,
    "sample_number": int,
    "client": str,
    "location": str,
    "analyzed": bool,
    "results": {}
}

def validate_csv(file_path, schema):
    try:
        df = pd.read_csv(file_path)

        missing_columns = [col for col in schema.keys() if col not in df.columns]
        extra_columns = [col for col in df.columns if col not in schema.keys()]

        if missing_columns:
            raise ValueError(f"Missing columns in CSV: {missing_columns}")
        if extra_columns:
            raise ValueError(f"Unexpected columns in CSV: {extra_columns}")

        for column, dtype in schema.items():
            if not df[column].map(lambda x: isinstance(x, dtype)).all():
                raise ValueError(f"Column '{column}' does not match expected type '{dtype.__name__}'.")

        print("CSV matches the expected schema!")
        return df

    except Exception as e:
        print(f"Schema validation error: {e}")
        return None

csv_file_path = "exasample_data.csv"  # Replace with your CSV file path
validated_data = validate_csv(csv_file_path, expected_schema)

if validated_data is not None:
    print("DataFrame is ready for further processing.")
else:
    print("Validation failed.")
