import streamlit as st
from calculator import *

# Initialize session state
if "restart" not in st.session_state:
	st.session_state["restart"] = True

if "num1" not in st.session_state:
	st.session_state["num1"] = 0.0

if "num2" not in st.session_state:
	st.session_state["num2"] = 0.0

if "angle" not in st.session_state:
	st.session_state["angle"] = 0.0

if "history" not in st.session_state:
	st.session_state["history"] = []  # Initialize history if not already present


def restart_app():
	"""Restarts the application with initial values."""
	st.session_state["restart"] = True
	st.session_state["num1"] = 0.0
	st.session_state["num2"] = 0.0
	st.session_state["angle"] = 0.0
	st.rerun()  # Use the correct method to rerun the app


def terminate_app():
	"""Terminates the application."""
	st.session_state["restart"] = False
	st.rerun()  # Use the correct method to rerun the app


def save_to_history(entry):
	"""Appends a new entry to the history."""
	st.session_state["history"].append(entry)


if st.session_state["restart"]:
	st.title("Advanced Calculator")

	# Sidebar for operation selection
	operation = st.sidebar.selectbox(
		"Choose an operation:",
		[
			"Addition",
			"Subtraction",
			"Multiplication",
			"Division",
			"Modular Division",
			"Floor Division",
			"Sine",
			"Cosine",
			"Tangent",
			"Cotangent",
			"Secant",
			"Cosecant",
			"History",
		]
	)

	# Input fields for operations
	if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Modular Division", "Floor Division"]:
		st.session_state["num1"] = st.number_input("Enter the first number:", value=st.session_state["num1"], step=1.0,
		                                           format="%.2f")
		st.session_state["num2"] = st.number_input("Enter the second number:", value=st.session_state["num2"], step=1.0,
		                                           format="%.2f")

		if st.button("Calculate"):
			if operation == "Addition":
				result = add(st.session_state["num1"], st.session_state["num2"])
			elif operation == "Subtraction":
				result = sub(st.session_state["num1"], st.session_state["num2"])
			elif operation == "Multiplication":
				result = mul(st.session_state["num1"], st.session_state["num2"])
			elif operation == "Division":
				result = div(st.session_state["num1"], st.session_state["num2"])
			elif operation == "Modular Division":
				result = mod(st.session_state["num1"], st.session_state["num2"])
			elif operation == "Floor Division":
				result = floor(st.session_state["num1"], st.session_state["num2"])
			save_to_history(f"{operation} of {st.session_state['num1']} and {st.session_state['num2']} = {result}")
			st.success(f"Result: {result}")

	elif operation in ["Sine", "Cosine", "Tangent", "Cotangent", "Secant", "Cosecant"]:
		st.session_state["angle"] = st.number_input("Enter the angle in degrees:", value=st.session_state["angle"],
		                                            step=1.0, format="%.2f")

		if st.button("Calculate"):
			if operation == "Sine":
				result = sin(st.session_state["angle"])
			elif operation == "Cosine":
				result = cos(st.session_state["angle"])
			elif operation == "Tangent":
				result = tan(st.session_state["angle"])
			elif operation == "Cotangent":
				result = cot(st.session_state["angle"])
			elif operation == "Secant":
				result = sec(st.session_state["angle"])
			elif operation == "Cosecant":
				result = cosec(st.session_state["angle"])
			save_to_history(f"{operation} of {st.session_state['angle']}° = {result}")
			st.success(f"Result: {result}")

	elif operation == "History":
		st.subheader("Calculation History")
		if st.session_state["history"]:
			for entry in st.session_state["history"]:
				st.write(entry)
		else:
			st.info("No calculations in history.")

	# Prompt the user whether to continue or exit
	st.write("Do you want to continue?")
	col1, col2 = st.columns(2)
	with col1:
		if st.button("Yes"):
			restart_app()
	with col2:
		if st.button("No"):
			terminate_app()

else:
	st.title("Goodbye!")
	st.write("Thank you for using the calculator!")
	st.stop()
