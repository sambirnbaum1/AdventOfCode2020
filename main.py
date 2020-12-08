import argparse
import cProfile
import importlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--problems', type=str, dest='problems', nargs='+')

    args = parser.parse_args()

    for problem in args.problems:
        print(problem)
        pkg = importlib.import_module(f'adventOfCode.{problem}')
        cProfile.run('solution = pkg.solve()')
        print(solution)
