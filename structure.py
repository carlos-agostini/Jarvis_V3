import os

# Carpetas principales del proyecto
folders = [
    "config", 
    "core", 
    "agents", 
    "models/whisper", 
    "models/custom", 
    "utils", 
    "tests"
]

# Archivos vacíos que queremos crear
files = [
    "config/settings.py",
    "core/__init__.py", 
    "core/decision_engine.py", 
    "core/task_manager.py", 
    "core/voice_assistant.py",
    "agents/__init__.py",
    "agents/email_agent.py", 
    "agents/todo_agent.py", 
    "agents/slack_agent.py",
    "models/__init__.py", 
    "utils/__init__.py",
    "utils/audio_utils.py",
    "utils/file_utils.py",
    "utils/slack_utils.py",
    "tests/test_voice_assistant.py",
    "tests/test_agents.py",
    "tests/test_task_manager.py",
    "Dockerfile",
    "requirements.txt",
    "main.py",
    "README.md"
]

# Crear carpetas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Crear archivos
for file in files:
    with open(file, 'w') as f:
        pass  # Crear el archivo vacío

print("Estructura del proyecto creada.")
