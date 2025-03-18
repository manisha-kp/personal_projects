#import streamlit as st

# def count_cash():
#     denominations = {
#         "100-dollar bills": 100,
#         "50-dollar bills": 50,
#         "20-dollar bills": 20,
#         "10-dollar bills": 10,
#         "5-dollar bills": 5,
#         "2-dollar coins": 2,
#         "1-dollar coins": 1,
#         "25-cent coins": 0.25,
#         "10-cent coins": 0.10,
#         "5-cent coins": 0.05
#     }
    
#     total = 0
#     st.title("CAD Cash Counter")
#     for denomination, value in denominations.items():
#         count = st.number_input(f"{denomination}:", min_value=0, value=0, step=1)
#         total += count * value
    
#     st.write(f"### Total Cash: CAD {total:.2f}")

# count_cash()
import streamlit as st

def count_cash():
    st.title("CAD Cash Counter")

    denominations = {
        "100-dollar bills": 100,
        "50-dollar bills": 50,
        "20-dollar bills": 20,
        "10-dollar bills": 10,
        "5-dollar bills": 5,
        "2-dollar coins": 2,
        "1-dollar coins": 1,
        "25-cent coins": 0.25,
        "10-cent coins": 0.10,
        "5-cent coins": 0.05
    }

    total = 0
    cash_count = {}

    st.subheader("Enter the number of each denomination:")
    for denomination, value in denominations.items():
        count = st.number_input(f"{denomination}", min_value=0, value=0, step=1)
        cash_count[denomination] = count
        total += count * value

    st.write(f"### Total Cash: CAD {total:.2f}")

    # Calculate deposit amount
    if total > 300:
        deposit_amount = total - 300
        st.write(f"### Amount to Deposit: CAD {deposit_amount:.2f}")
        deposit_breakdown = {}

        for denomination, value in sorted(denominations.items(), key=lambda x: -x[1]):
            if deposit_amount >= value:
                num_to_deposit = min(cash_count[denomination], int(deposit_amount // value))
                deposit_breakdown[denomination] = num_to_deposit
                deposit_amount -= num_to_deposit * value

        st.subheader("Deposit Breakdown:")
        for denom, count in deposit_breakdown.items():
            st.write(f"**{count} x {denom}**")
    else:
        st.write("No deposit needed.")

count_cash()
