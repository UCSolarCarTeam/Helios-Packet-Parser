# PacketParser General Information

This guide explains how to set up and run the Packet Parser program, which uses **PyQt6** for the user interface and **Pandas** for data manipulation.

---

## Prerequisites

1. **Install an Integrated Development Environment (IDE):**
   - Choose an IDE that supports Python, such as:
     - [PyCharm](https://www.jetbrains.com/pycharm/)
     - [Visual Studio Code](https://code.visualstudio.com/)
     - [Jupyter Notebook](https://jupyter.org/)
     - [Spyder](https://www.spyder-ide.org/)

2. **Install Python Interpreter:**
   - Download and install Python from [python.org](https://www.python.org/downloads/).
   - During installation, ensure you check **"Add Python to PATH"**.

3. **Install `pip`:**
   - Verify that `pip` is installed by running:
     ```bash
     pip --version
     ```
   - If `pip` is not available, refer to the [pip installation guide](https://pip.pypa.io/en/stable/installation/).

---

## Steps to Set Up the Application

1. **Download the Script:**
   - Obtain the application file (e.g., `packet_parser.py`) and `requirements.txt` from the source or repository.

2. **Install Required Libraries:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the downloaded files.
   - Install all required libraries by running:
     ```bash
     pip install -r requirements.txt
     ```
   - This ensures that all dependencies, such as **PyQt6** and **Pandas**, are installed automatically.

---

## Steps to Run the Application

1. **Open the Script in Your IDE:**
   - Launch your chosen IDE and open the `Main.py` file.
   - Ensure the Python interpreter in the IDE is correctly set to the installed version.

2. **Run the Script:**
   - Use your IDE's "Run" button or execute the script via the terminal:
     ```bash
     python Main.py
     ```

3. **Interact with the Application:**
   - A PyQt6-based user interface will open, allowing you to interact with the program.
   - Use the features provided by the application, such as browsing files or parsing packet data.

---

## Troubleshooting

1. **Dependency Installation Error:**
   - Ensure the `requirements.txt` file is in the same directory and re-run:
     ```bash
     pip install -r requirements.txt
     ```

2. **PyQt6 Import Error:**
   - Ensure PyQt6 is installed by running:
     ```bash
     pip install PyQt6
     ```

3. **IDE Errors:**
   - Verify that your IDE's Python interpreter matches the Python version where the required libraries are installed.

4. **General Issues:**
   - Check for typos or incomplete code in the script.
   - Run the script in debug mode for detailed error messages.

---

You are now ready to run the Packet Parser application!
