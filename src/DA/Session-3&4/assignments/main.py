from config import config
from preprocessing import (
    Read_data_file,
    Drop_unnecessary_features,
    Check_data_type,
)


def main():
    df = Read_data_file(config.DATA_PATH)

    if df is not None:
        print("=== Data Loaded Successfully ===")
        print(df.head())

        print("\n=== Available columns to drop (from config) ===")
        print(config.COLS_TO_DROP)

        user_input = input(
            "\nEnter columns to drop (comma-separated), or press Enter to use config defaults: "
        ).strip()

        if user_input:
            cols_to_drop = [col.strip() for col in user_input.split(",")]
        else:
            cols_to_drop = config.COLS_TO_DROP

        df = Drop_unnecessary_features(df, cols_to_drop)
        print("\n=== Data After Dropping Columns ===")
        print(df.head())

        print("\n=== Data Type & Uniqueness Report ===")
        print(Check_data_type(df))


if __name__ == "__main__":
    main()