import numpy as np
from example import algs
def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # input testing
    x = [np.array([]),
    np.array([2]),
    np.array(['a']),
    np.array([2,2,2,2]),
    np.array([2,2,'a',2]),
    np.array([2,2,6,4,5]),
    np.array([2.4,2.1,6.7,4.7,5.0,10.1])]
    for i in x:
        ans = algs.bubblesort(i)
        if 'None' in str(ans):
            None
        else:
            print(ans)
    # speed testing
    # for i in [(i + 1) * 100 for i in list(range(10))]:
    #     a = np.random.rand(100,i)
    #     algs.bubblesort(a)
    return 

def test_quicksort():

    x = [np.array([]),
    np.array([2]),
    np.array(['a']),
    np.array([2,2,2,2]),
    np.array([2,2,'a',2]),
    np.array([2,2,6,4,5]),
    np.array([2.4,2.1,6.7,4.7,5.0,10.1])]
    for i in x:
        ans = algs.bubblesort(i)
        if 'None' in str(ans):
            None
        else:
            print(ans)
    return 

test_bubblesort()
test_quicksort()