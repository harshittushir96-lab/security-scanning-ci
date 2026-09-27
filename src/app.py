import subprocess

result = subprocess.run(
    ["echo", "Hello"],
    capture_output=True,
    text=True,
    check=True
)

print(result.stdout)
