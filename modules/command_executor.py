import subprocess


class CommandExecutor:
    def __init__(self):
        pass

    def execute(self, command):
        # Execute the given command
        # Implement logic to perform actions based on the processed command
        # Return a response or result

        if command.startswith("open_app "):
            app_name = command.split("open_app ")[1]
            response = self.open_app(app_name)
        else:
            response = {"error": "Unknown command"}

        return response

    def open_app(self, app_name):
        try:
            # Open the app using subprocess
            subprocess.Popen([app_name], shell=True)
            return {"success": f"Opened {app_name}"}
        except Exception as e:
            return {"error": f"Error opening {app_name}: {str(e)}"}
