import os
from datetime import datetime

# Path to your README file
readme_path = "README.md"

# Data to be added to the README (e.g., latest commit or project update)
new_data = f"\n\n## Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Open the README file and append the new data
with open(readme_path, 'a') as f:
    f.write(new_data)

print("README has been updated!")

