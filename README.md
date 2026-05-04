# EEE120_Final_Project_Group3
A small practical system using the concepts studied in EEE120 Digital Design Fundamentals. It is a digital lock that opens only when the correct binary password is entered.
# Project Title: Digital Password Lock System

## Group Members
| Name | Role |
| Odinaxon Maripova | Python Software Prototype |
| Mashhurbek Abdullayev | Lead Designer & CircuitVerse Simulation |
| Shahzoda Komiljonova | Presentation |
| Hasan Aruslanov | Lead Designer |
| Temur Doniyorov | GitHub Repository & Submission |

## Course
**Course Code:** EEE120  
**Course Name:** Digital Design Fundamentals

## Instructor
Dr. Rajan Tirpathi

## Problem Statement
In modern security systems, physical keys are easily lost or duplicated. We need a robust, low-cost digital authentication mechanism that grants access only when a specific binary sequence (password) is entered. This project designs a digital lock that compares a user-entered 4-bit binary code against a pre-stored secure password. If the codes match, the system unlocks; otherwise, access is denied.

## Inputs
The system accepts the following logical inputs:
1. **Password Input (4-bit):** A binary value entered by the user (e.g., `1011`).
2. **Stored Password (4-bit):** The hardcoded secure value within the system (e.g., `1100`).
3. **Reset Signal:** A logic `1` pulse to clear the current state and reset the lock.
4. **Lock/Unlock Button:** A trigger signal to initiate the comparison process.

## Outputs
The system provides two distinct status outputs:
1. **Access Granted:** Logic `1` (LED ON) indicating the correct password was entered.
2. **Access Denied:** Logic `1` (Red LED ON) indicating a mismatch or incorrect attempt.

## Digital Logic Explanation
The core of the hardware design relies on **combinational logic** using XOR and XNOR gates:
- **Bitwise Comparison:** Each bit of the user input is compared to the corresponding bit of the stored password using **XNOR gates**. An XNOR gate outputs `1` only if both inputs are identical.
- **Final Verification:** The outputs of the four XNOR gates are fed into a single **4-input AND gate**.
  - If all bits match, all XNOR outputs are `1`, causing the AND gate to output `1` (Access Granted).
  - If any bit mismatches, at least one XNOR output is `0`, causing the AND gate to output `0` (Access Denied).
- **Sequential Logic (Optional):** A simple D-Flip-Flop based counter tracks the number of failed attempts. If the counter reaches a threshold (e.g., 3 attempts), it triggers a permanent lockout state until a master reset is applied.


## Python Program Explanation
The Python software version simulates the exact logic of the digital circuit in a high-level environment:
- The program defines a `stored_password` variable.
- It prompts the user to input a 4-bit binary string.
- It performs a bitwise comparison (mimicking the XNOR/AND logic) to check for equality.
- It prints "Access Granted" or "Access Denied" based on the result.
- The code includes error handling for invalid inputs (non-binary characters or wrong length).

## How AI/LLM was used
During the development of this project, AI tools were utilized for:
1. **Logic Optimization:** Generating Karnaugh map simplifications to verify our XOR/XNOR gate selection was minimal.
2. **Test Case Generation:** Creating a list of edge cases (e.g., all zeros, all ones, single-bit errors) to ensure the Python code handles all scenarios.
3. **Code Refinement:** Assisting in writing the input validation logic in Python to prevent crashes on user error.

## How to Run the Python Code
1. Clone this repository or download the `main.py` file.
2. Ensure you have Python 3.x installed.
3. Open your terminal or command prompt in the project directory.
4. Run the following command:
   ```bash
   python main.py
  
## 📄 Presentation
View our interactive pitch deck:
[👉 View Presentation on Canva] (https://canva.link/0nnmlk7wrf4lvto)
