from problem1.input import Input
from problem1.processor import Processor

# assume problems
problems = ['a', 'b', 'c', 'd', 'e']

for problem in problems:
    _input = Input.fromFile('input_{}.txt'.format(problem))
    output = Processor().process(input=_input)
    outputFilename = 'output_{}.txt'.format(problem)
    # Create output file
