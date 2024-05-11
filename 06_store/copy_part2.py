import psycopg2
from io import StringIO
import time

def establish_db_connection():
    """ Establish a connection to the PostgreSQL database with autocommit enabled. """
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Chavasgrand@113",
    )
    connection.autocommit = True
    return connection

def reset_table(conn):
    """ Drop the existing table if it exists and create a new one. """
    with conn.cursor() as cursor:
        cursor.execute("""
            DROP TABLE IF EXISTS censusdata;
            CREATE TABLE censusdata (
                CensusTract         NUMERIC,
                State               TEXT,
                County              TEXT,
                TotalPop            INTEGER,
                Men                 INTEGER,
                Women               INTEGER,
                Hispanic            DECIMAL,
                White               DECIMAL,
                Black               DECIMAL,
                Native              DECIMAL,
                Asian               DECIMAL,
                Pacific             DECIMAL,
                Citizen             DECIMAL,
                Income              DECIMAL,
                IncomeErr           DECIMAL,
                IncomePerCap        DECIMAL,
                IncomePerCapErr     DECIMAL,
                Poverty             DECIMAL,
                ChildPoverty        DECIMAL,
                Professional        DECIMAL,
                Service             DECIMAL,
                Office              DECIMAL,
                Construction        DECIMAL,
                Production          DECIMAL,
                Drive               DECIMAL,
                Carpool             DECIMAL,
                Transit             DECIMAL,
                Walk               DECIMAL,
                OtherTransp         DECIMAL,
                WorkAtHome          DECIMAL,
                MeanCommute         DECIMAL,
                Employed            INTEGER,
                PrivateWork         DECIMAL,
                PublicWork         DECIMAL,
                SelfEmployed        DECIMAL,
                FamilyWork         DECIMAL,
                Unemployment        DECIMAL
            );
        """)
        print("Table 'censusdata' has been dropped and recreated.")

def data_preprocessing(file_path):
    """Read and preprocess data, ensuring proper type formats for numeric fields."""
    processed_data = StringIO()
    with open(file_path, 'r') as file:
        headers = next(file).strip().split(',')
        numeric_columns = {
            index: header for index, header in enumerate(headers) 
            if header.endswith('Pop') or header.endswith('Work') or 'Dec' in header or 'Income' in header or 'Employed' in header
        }
        
        for line in file:
            parts = line.strip().split(',')
            for index, header in numeric_columns.items():
                if parts[index] == "":
                    parts[index] = None  # Convert empty strings to None
                else:
                    try:
                        # Determine if the column should be float or integer based on its header
                        if 'Pop' in header or 'Employed' in header:
                            parts[index] = int(float(parts[index]))  # Force float to int conversion
                        else:
                            parts[index] = float(parts[index])
                    except ValueError:
                        parts[index] = None
            
            # Use a generator to handle None values and convert them to an empty string for CSV output
            processed_data.write(','.join("" if part is None else str(part) for part in parts) + '\n')
    processed_data.seek(0)
    return processed_data

def bulk_load_data(conn, fpath, table):
    """ Load preprocessed data into the database using the COPY command. """
    data_stream = data_preprocessing(fpath)
    cursor = conn.cursor()
    start_time = time.time()
    cursor.copy_from(data_stream, table, sep=',', null='')
    conn.commit()
    elapsed_time = time.time() - start_time
    print(f"Data loaded successfully in {elapsed_time:.2f} seconds")
    cursor.close()

def main():
    conn = establish_db_connection()
    reset_table(conn)  # Reset the table for fresh data loading
    data_file_path = 'acs2015_census_tract_data_part2.csv'
    bulk_load_data(conn, data_file_path, 'censusdata')
    conn.close()

if __name__ == "__main__":
    main()
