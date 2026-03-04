import subprocess

# Fixed 'Text' to 'text'
result = subprocess.run("dir", shell=True, capture_output=True, text=True)
print(result)

result = subprocess.run("ipconfig", shell=True, capture_output=True, text=True)
print(result)

result = subprocess.run("python --version", shell=True, capture_output=True, text=True)
print(result.stdout)
print(result.stderr)