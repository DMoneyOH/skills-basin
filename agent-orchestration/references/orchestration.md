# Orquestracao (Se Matched >= 2)
## Overview
The orchestration process coordinates the execution of multiple skills to achieve a complex task.
## How It Works
1. The `orchestrate.py` script is executed with the matched skills and the user's request as input.
2. The script generates a plan of execution with the standard, order of steps, and data flow between skills.
3. The script returns the plan of execution as a JSON response.