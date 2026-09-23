import io
from contextlib import redirect_stdout

import streamlit as st

from apputil import *


def run_and_capture(func):
    """Run func and return its result along with anything it printed."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        result = func()
    return result, buffer.getvalue()


st.write(
'''
# Week 3: Basic Pandas

''')


# Exercise 1: Fibonacci
st.header("Exercise 1: Fibonacci")

# the plain recursive version gets very slow for large n, so cap the input
fib_n = st.number_input("n (0-30): ",
                        min_value=0,
                        max_value=30,
                        value=None,
                        step=1,
                        format="%d",
                        key="fib_n")

if fib_n is not None:
    st.write(f"fibonacci({fib_n}) = {fibonacci(int(fib_n))}")


# Exercise 2: Binary conversion
st.header("Exercise 2: Binary")

binary_n = st.number_input("Integer to convert: ",
                           value=None,
                           step=1,
                           format="%d",
                           key="binary_n")

if binary_n is not None:
    binary_n = int(binary_n)
    st.write(f"to_binary({binary_n}) = {to_binary(binary_n)}")
    # compare with Python's built-in bin() as a check
    st.caption(f"bin({binary_n}) = {bin(binary_n)}")


# Exercise 3: Bellevue Almshouse tasks
st.header("Exercise 3: Bellevue Almshouse Dataset")

tasks = {
    "Task 1: columns sorted by missing values": task_1,
    "Task 2: total admissions per year": task_2,
    "Task 3: average age by gender": task_3,
    "Task 4: 5 most common professions": task_4,
}

choice = st.selectbox("Choose a task: ", list(tasks))

if st.button("Run task"):
    result, printed = run_and_capture(tasks[choice])

    # show any notes the task printed about messy data
    if printed:
        st.info(printed)

    st.write(result)
