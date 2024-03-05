import subprocess

class ChildRunner():

    def run_shell(self, filename):
        # Run the file using Popen with capture enabled
        process = subprocess.Popen(
            ["python", filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True  # Adjust shell argument if needed (e.g., set to False)
        )

        # Capture standard output and standard error
        stdout, stderr = process.communicate()

        # Decode bytes to strings (if necessary, depending on encoding)
        if stdout:
            stdout = stdout.decode('utf-8')
        if stderr:
            stderr = stderr.decode('utf-8')

        return stdout, stderr

    def run_child(self, filename):
        stdout, stderr = self.run_shell(filename=filename)

        if stdout:
            print("Standard output:")
            print(stdout)

        if stderr:
            print("Standard error:")
            print(stderr)


if __name__ == '__main__':
    filename = "Cody\out.py"
    Run = ChildRunner()
    Run.run_child(filename=filename)

    
