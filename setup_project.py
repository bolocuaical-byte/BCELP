import os

folders = [
    "backend",
    "frontend",
    "database",
    "docs",
    "modules",
    "templates",
    "datasets",
    "laboratory",
    "tests",
    "scripts",
    "tools",
    "resources"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(folder)

print("\nEstructura de BCELP creada correctamente.")