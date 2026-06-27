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
    if not os.path.exists(folder):
        os.makedirs(folder)
    print(folder)

print("\nEstructura de BCELP creada correctamente.")