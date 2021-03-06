from problem1.input import Input
from problem1.output import Output
from problem1.processor import Processor

# assume problems
problems = ['a', 'b', 'c', 'd', 'e']

for problem in problems:
    print(problem)
    input_ = Input.from_file('input_{}.txt'.format(problem))
    output = Processor().process(input_=input_)
    output.write_to_file(outputFile='output_{}.txt'.format(problem))
