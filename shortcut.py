import subprocess
input_string = "This is amazing, it works"
input_bytes = input_string.encode("utf-8")
print(input_bytes)

result = subprocess.run(
    ["shortcuts", "run", "Make Jarvis say anything!"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, input=input_string)
print(result)
