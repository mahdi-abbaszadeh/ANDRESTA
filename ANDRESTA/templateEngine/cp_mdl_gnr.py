import dzn_generator
import mapping_result

def gen():
    dzn_generator.gen()
    mapping_result.run_minizinc()
    mapping_result.run()
