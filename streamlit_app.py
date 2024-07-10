import streamlit as st
import psycopg2

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
#df = conn.query('SELECT * FROM transactions;', ttl="10m")
st.dataframe('transactions')
# Print results.
#for row in df.itertuples():
  #  st.write(f"{row.name} has a :{row.pet}:")
