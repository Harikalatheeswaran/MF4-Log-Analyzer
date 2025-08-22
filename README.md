# MF4-Log-Analyzer

## Overview
The **MF4-Log-Analyzer** is a Python-based tool designed to analyze `.mf4` log files, specifically for Data Acquisition Systems (DAS) <br>It evaluates failure behavior, detects system failures, & provides visual insights into the log data.

---

```
 8888888b.        d8888  .d8888b.              d8888                   888                                    888
 888  "Y88b      d88888 d88P  Y88b            d88888                   888                                    888
 888    888     d88P888 Y88b.                d88P888                   888                                    888
 888    888    d88P 888  "Y888b.            d88P 888 88888b.   8888b.  888 888  888 88888888  .d88b.  888d888 888
 888    888   d88P  888     "Y88b.         d88P  888 888 "88b     "88b 888 888  888    d88P  d8P  Y8b 888P"   888
 888    888  d88P   888       "888        d88P   888 888  888 .d888888 888 888  888   d88P   88888888 888     Y8P
 888  .d88P d8888888888 Y88b  d88P       d8888888888 888  888 888  888 888 Y88b 888  d88P    Y8b.     888      "
 8888888P" d88P     888  "Y8888P"       d88P     888 888  888 "Y888888 888  "Y88888 88888888  "Y8888  888     888
                                                                                888
                                                                           Y8b d88P
                                                                            "Y88P"
```
---
## Features
- **Failure Detection**:
  - Detects and displays failures set in the log.
  - Identifies transitions and constant values in signal data.
- **System State Analysis**:
  - Monitors IGN switch toggling and timestamps.
  - Checks changes in system states (`SR_StateCurrent`) and provides indices for each state.
- **Visualization**:
  - Plots failures and system signals with customizable cursors for degradation analysis.
- **Interactive User Interface**:
  - Allows users to select DAS log files and additional channels for analysis.
- **Progress Tracking**:
  - Displays progress and results using the `rich` library for enhanced console output.

---

## Requirements
- Python 3.8 or later
- Libraries:
  - `asammdf` (for reading `.mf4` files)
  - `rich` (for formatted console output)
  - `matplotlib` (for plotting graphs)
  - `tkinter` (for file selection dialogs)
- Install dependencies using the following command :
```bash
   pip install -r requirements.txt
   
```
---

### Example Workflow
1. **Log Initialization**:
   - Reads the DAS log file and extracts signal data for failures, control functions, and warning lamps.
   - Detects transitions and constant values in signal samples.

2. **Failure Analysis**:
   - Identifies current and final failures set in the system.
   - Displays results in a well-formatted console output.

3. **System State Analysis**:
   - Checks if the IGN switch was toggled and identifies timestamps of transitions.
   - Monitors changes in system states (`SR_StateCurrent`) and provides indices for each state.

4. **Visualization**:
   - Plots selected failures or signals with timestamps and degradation cursors for detailed analysis.

---

## Contributions
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

```

                                                ⠀⠀⠀⠀⠀⠀⢀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠘⣦⡀⠘⣆⠈⠛⠻⣗⠶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠈⠳⠄⠀⠈⠙⠶⣍⡻⢿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⣰⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠻⣮⡹⣿⣿⣷⣦⣄⣀⠀⠀⢀⣸⠃⠀⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⢠⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣮⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢰⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⢀⣾⣿⠀⠀⠀⠀⠀⠀⠀⣷⠀⢷⠀⠀⠀⠙⢷⣿⣿⣿⣿⣟⣋⣀⣤⣴⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⢀⣼⢿⣿⡀⠀⠀⢀⣀⣴⣾⡟⠀⠈⣇⠀⠀⠀⠈⢻⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⣼⡏⠸⣿⣿⣶⣾⣿⡿⠟⠋⠀⠀⠀⢹⡆⠀⠀⠀⠀⠹⡽⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⣰⣿⠀⠀⠀⣀⡿⠛⠉⠀⠀⢿⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠑⢹⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⣿⣿⣷⣶⣾⠏⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⡿⠃⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠈⠙⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⢀⠀⠹⣿⣿⣿⣿⣷⣶⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⢸⣿⠀⠀⠀⠀⢀⡞⠀⠀⠈⠛⠻⠿⠿⠯⠥⠤⢄⣀⣀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⢸⡇⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠈⠙⠂⠙⠳⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⡾⠁⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⡸⠃⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠇⠀⠀⠀⠃⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠏⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠙⠻⣿⣿⣿⣿⣿⣿⣦⡀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⢀⡖⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⢸⣿⠀⠀⠈⢿⣿⣿⣿⣿⣿⡿
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⣼⠁⠼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⣼⡇⠀⠀⣠⣾⣿⣿⣿⣿⠟⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠘⣇⠀⠀⢻⡄⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⢀⣼⠏⠀⣠⣾⣿⣿⡿⣿⡿⠁⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠘⠂⠀⠀⢳⠀⢳⡀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⠃⠀⠀⠀⠀⣠⣾⠃⣠⣾⣿⣿⠿⠋⢰⡟⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⢀⣀⡴⠞⠙⠲⣷⡄⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⢀⣀⣠⣤⣶⠿⠟⠋⠀⡾⠀⠀⠀⢀⣴⠟⠁⢠⡟⢱⡿⠃⠀⠀⠸⣇⡀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⢀⡴⠟⠁⠀⣀⡤⠖⠋⠁⠀⠀⠀⠀⣸⠇⠀⠀⠀⣤⠟⠑⠋⠉⣿⠋⠉⠉⠉⠁⣠⠞⠀⠀⠀⡇⠀⠀⢠⡿⠋⠀⠀⠈⠁⡿⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
                                                ⠀⠀⠀⢀⣾⣏⣤⣶⡾⠛⠉⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⣠⠞⠁⠀⠀⠀⠀⣿⠀⠀⠀⢀⡼⠃⠀⠀⠀⢸⠇⠀⣰⠟⠀⠀⠀⠀⠀⠐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⢀⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⣿⠀⠀⢀⡾⠃⠀⠀⠀⢀⡞⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⣼⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣶⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣾⠇⠀⠀⠀⢀⣾⣣⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⢠⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⢠⡟⠀⠀⠀⢀⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⢀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡄⢀⣀⡀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣾⠇⠀⠀⣰⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⣾⠀⣰⠟⠀⢀⣼⣿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⢸⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⠿⠿⠿⠿⠃⠀⠀⠀⢸⣿⣶⠏⢀⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⢸⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠃⢠⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⢿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⢃⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠈⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣧⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡟⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠁⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

```

### `Stay Curious !`


   


                      
