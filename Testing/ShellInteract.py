import subprocess, os, sys

class ShellInteract:
    def shell_interact(self, inp):
        if inp[0:2] == "cd":
            os.chdir(inp[3:])
            return os.path.abspath(os.curdir)
        if inp == "cd../":
            os.chdir(os.path.dirname(os.getcwd()))
            return os.path.abspath(os.curdir)
        if inp[0:4] == "open":
            path = str(os.path.abspath(os.curdir)+"\\%s" % (inp[5:]))
            out = []
            with open(path, "r") as inFile:
                for i in inFile:
                    out.append(i)
            inFile.close()
            return ''.join(out)
        if inp == "exit":
            sys.exit()
        command = subprocess.Popen(inp, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        out = command.stdout.read().decode()
        return out

    def main(self):
        while True:
            x = input(str("Enter command: "))
            print(self.shell_interact(x))


if __name__ == "__main__":
    NemesisShellConnect = ShellInteract()
    NemesisShellConnect.main()
