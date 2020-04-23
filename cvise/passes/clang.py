import logging
import os
import subprocess
import shutil
import tempfile

from cvise.passes.abstract import AbstractPass, PassResult

class ClangPass(AbstractPass):
    def check_prerequisites(self):
        return shutil.which(self.external_programs["clang_delta"]) is not None

    def new(self, test_case):
        return 1

    def advance(self, test_case, state):
        return state + 1

    def advance_on_success(self, test_case, state):
        return state

    def transform(self, test_case, state, process_event_notifier):
        tmp = os.path.dirname(test_case)
        with tempfile.NamedTemporaryFile(mode="w", delete=False, dir=tmp) as tmp_file:
            args = [self.external_programs["clang_delta"], "--transformation={}".format(self.arg), "--counter={}".format(state)]
            if self.clang_delta_std:
                args.apend('--std={}'.format(self.clang_delta_std))
            cmd = args + [test_case]

            logging.debug(" ".join(cmd))

            stdout, stderr, returncode = process_event_notifier.run_process(cmd)
            if returncode == 0:
                tmp_file.write(stdout)
                shutil.move(tmp_file.name, test_case)
                return (PassResult.OK, state)
            else:
                os.unlink(tmp_file.name)
                if returncode == 255 or returncode == 1:
                    return (PassResult.STOP, state)
                else:
                    return (PassResult.ERROR, state)
