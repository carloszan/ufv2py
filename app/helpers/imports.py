# if it is on Travis env, the tests will pass!
import os
import matplotlib
travis = os.environ.get('TRAVIS')
if travis:
    matplotlib.use('Agg')
