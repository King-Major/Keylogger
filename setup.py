from cx_Freeze import setup, Executable

# Replace 'your_script.py' with the name of your Python script
executables = [Executable("keylogger.py", base=None,target_name="keylogger.exe")]

# Add any additional options you might need for your setup
setup(
    name="YourApp",
    version="1.0",
    description="Your description",
    executables=executables,
    options={
        "build_exe": {
            "packages": ["time","os","pynput","queue"],
            "includes": [],  # Add any other libraries you need
            "include_files": []  # If you need to include non-Python files (e.g., images, configs), specify them here
        }
    }
)