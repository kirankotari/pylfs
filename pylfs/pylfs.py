import re
import sys
import subprocess
import logging


class PyLFS:
    command = ["pylfs"]
    name = "pylfs"

    def __init__(self, log_level=logging.INFO, log_format=None):
        self.format = log_format
        self.logger = self.set_logger_level(log_level)

    def set_logger_level(self, log_level):
        if self.format is None:
            self.format = "[ %(levelname)s ] :: [ %(name)s ] :: %(message)s"
        logging.basicConfig(
            stream=sys.stdout, level=log_level, format=self.format, datefmt=None
        )
        logger = logging.getLogger(self.name)
        logger.setLevel(log_level)
        return logger

    def __help(self):
        text = """
        PyLFS: Linux From Sratch Automation in Python
        """
        return text

    def __version(self):
        pass

    def __get_tar_files(self):
        pass

    def __get_lfs(self):
        pass

    def pylfs(self):
        command = self.command
        # if command:
        #     p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     out, err = p.communicate()
        #     # print(out.decode())
        #     out = out.decode().split('\n')
        #     return out
        # else:
        #     logging.error("invalid entry '{}'".format(' '.join(command)))
        return self.__help()


def run():
    obj = PyLFS()
    if len(sys.argv) >= 2:
        print(obj.pylfs(sys.argv[1]))
    else:
        print("Expecting an argument.")
        print("e.g.: pylfs <arg>")


if __name__ == "__main__":
    obj = PyLFS()
    print(obj.pylfs())
