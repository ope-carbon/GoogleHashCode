from .output import Output

class Processor:

    def process(self, input_):
        for step in range(input_.steps):
            print(step)
        return Output()