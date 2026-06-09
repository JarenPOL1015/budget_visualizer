# BudgetVisualizer 📊
## By: Jaren Pazmino

An innovative and interactive monthly budget optimizer and visualizer built in Python. This software was developed as a Final Project for the **Stanford University Code in Place** course.

The application allows users to securely input their monthly financial records via the command line and instantly generates a clean, scaled bar chart using desktop graphics (`tkinter`). Its core feature is the **30% Alert Rule**: if any expense category meets or exceeds 30% of the total income, the bar dynamically switches from friendly green to warning red, providing immediate financial feedback.

---

## 🌟 Key Features

* **Multi-language Support (Internationalization):** Features full bilingual support (English & Español). Users can select their preferred interface language before starting the program.
* **Strict Modular Architecture:** Designed using Stanford's *Top-Down Desing* methodology. The logic layer and the data layer are completely decoupled.
* **Advanced Data Separation:** Localization and translation strings are isolated in an independent `translations.py` module for clean maintenance and scalability.
* **Robust Input Validation:** Fully immune to accidental user crashes (e.g., entering negative values, zeros, or textual data instead of currency floats).
* **Responsive Geometric Scaling:** Bar heights, widths, and structural margins are dynamically calculated relative to the user's desktop canvas dimensions.

---

## 📁 Project Structure

The repository is structured neatly into decoupled modules:
* `budget_visualizer.py`: The heart of the program. Handles data execution, math processing, and canvas rendering pipelines.
* `translations.py`: Holds the dictionary structures for seamless multi-language string swapping.
* `graphics.py`: A native wrapper adapted from Stanford's graphics library optimized for standalone local desktop execution.

---

## 🛠️ Installation & Execution

1. Make sure you have **Python 3** installed on your system.
2. Clone this repository or download the source files into a local folder:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/BudgetVisualizer.git](https://github.com/JarenPOL1015/budget_visualizer.git)
   cd BudgetVisualizer