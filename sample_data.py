import pandas as pd

def build_messy_data():
    # Return a dictionary of messy sample data.
    data = {
        "Name ": [
            "  Ahmed Khan", "fatima ali", "AHMED KHAN", "Bilal Hussain", "fatima ali",
            "Bilal Hussain", "  Ayesha Malik  ", "usman tariq", "Sana Javed", "USMAN TARIQ",
            "Hassan Raza", "Zainab Shah", "hassan raza", "Imran Qureshi", "Sana Javed",
            "Maria Butt", "  Asad Ali", "asad ali", "Hira Siddiqui", "Kamran Akmal",
            "Nadia Yousaf", "kamran akmal", "Omar Farooq", "Rabia Nasir", "  Omar Farooq  ",
            "Tariq Mehmood", "Sadia Imran", "Yasir Shah", "sadia imran", "Mahnoor Aslam",
        ],
        " City": [
            "karachi", "Lahore ", "Karachi", "islamabad", "Lahore",
            "Islamabad", "faisalabad", "multan", "Peshawar", "Multan",
            "quetta", "Rawalpindi", "Quetta", None, "Peshawar",
            "sialkot", "karachi", "Karachi", "Hyderabad", "gujranwala",
            None, "Gujranwala", "bahawalpur", "Sargodha", "Bahawalpur",
            "abbottabad", "sukkur", "larkana", "Sukkur", None,
        ],
        "Age": [
            28, 34, 28, None, 34,
            45, 29, 31, 26, 31,
            38, None, 38, 40, 26,
            33, 27, 27, None, 50,
            24, 50, 36, 29, 36,
            None, 32, 41, 32, 23,
        ],
        "Salary": [
            50000, 62000, 50000, 48000, 62000,
            None, 55000, 47000, 53000, 47000,
            61000, 58000, 61000, None, 53000,
            45000, 50500, 50500, 49000, 72000,
            None, 72000, 65000, 46000, 65000,
            39000, None, 68000, 68000, 42000,
        ],
    }
    return data

def main():
    data = build_messy_data()
    df = pd.DataFrame(data)
    output_file = "messy_data.xlsx"
    df.to_excel(output_file, index=False)
    print(f"Created '{output_file}' with {len(df)} rows and {len(df.columns)} columns.")
    print("You can now run excel_cleaner.py on this file to see it get cleaned up.")
if __name__ == "__main__":
    main()