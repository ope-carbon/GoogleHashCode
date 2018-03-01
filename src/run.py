from problem1.input import Input
from problem1.processor import Processor

# assume problems
problems = ['a', 'b', 'c', 'd', 'e']

for problem in problems:
    _input = Input.from_file('input_{}.txt'.format(problem))
    output = Processor().process(input=_input)
    output.write_to_file('output_{}.txt'.format(problem))
