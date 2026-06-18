from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel

# Step 1: Create the app
app = QApplication([])

# Step 2: Create main window
window = QWidget()
window.setWindowTitle("Task 4 - Add Two Numbers")
window.setGeometry(100, 100, 400, 300)

# Step 3: First input box
input1 = QLineEdit(window)
input1.setPlaceholderText("Enter first number")
input1.move(100, 40)
input1.setText("6")

# Step 4: Second input box
input2 = QLineEdit(window)
input2.setPlaceholderText("Enter second number")
input2.move(100, 80)
input2.setText("7")

# Step 5: Label to show result
result_label = QLabel("", window)
result_label.setFixedWidth(200)
result_label.move(100, 170)

# Step 6: Button
calc_button = QPushButton("Calculate Sum", window)
calc_button.move(100, 120)

# Step 7: Function to calculate sum
def calculate_sum():
    try:
        num1 = float(input1.text())
        num2 = float(input2.text())
        total =  num1 + num2
        result_label.setText("Result: " + str(total))
    except ValueError:
        result_label.setText("Please enter valid numbers")

# Step 8: Connect button to function
calc_button.clicked.connect(calculate_sum)

# Step 9: Show window
window.show()
app.exec_()
