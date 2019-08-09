from subprocess import Popen, PIPE


class Process:
    def __init__(self, command, **kwargs):
        self.proc = Popen(command, stdout=PIPE, stderr=PIPE, **kwargs)

    def pipe(self, command, **kwargs):
        proc = Process(command, stdin=self.proc.stdout, **kwargs)
        self.proc.stdout.close()
        return proc

    def communicate(self):
        stdout, stderr = self.proc.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')
