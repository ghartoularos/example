import numpy as np
from example import algs
# from tqdm import tqdm
# from matplotlib import pyplot as plt

# from matplotlib import pyplot as plt
# def test_pointless_sort():
#     # generate random vector of length 10
#     x = np.random.rand(10)

#     # check that pointless_sort always returns [1,2,3]
#     assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

#     # generate a new random vector of length 10
#     x = np.random.rand(10)

#     # check that pointless_sort still returns [1,2,3]
#     assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    print('\n############Bubblesort############')


    # # multi test for inputs
    x = [np.array([]),
    np.array([2]),
    np.array(['a']),
    np.array([2,2,2,2]),
    np.array([2,2,'a',2]),
    np.array([2,2,6,4,5]),
    np.array([2.4,2.1,6.7,4.7,5.0,10.1])]

    # # # single large test
    # x = [np.random.randint(0,10000,10000)]

    # multi large test
    # x = [np.random.rand(100,i) for i in [(i + 1) * 100 for i in list(range(10))]]

    # multi smallish test
    # x = [np.random.rand(i) for i in [(i + 1) * 10 for i in list(range(50))]]
    #test
    accounts = []
    for i in x:
        if i.ndim == 1:
            ans = algs.bubblesort(i)
            accounts.append((len(i),ans))
        elif i.ndim == 2:
            for j in i:
                ans = algs.bubblesort(j)
                accounts.append((len(j),ans))
        else:
            None

    # speed testing
    # for i in [(i + 1) * 100 for i in list(range(10))]:
    #     a = np.random.rand(100,i)
    #     algs.bubblesort(a)

    return accounts

def test_quicksort():
    print('\n############Quicksort############')
# # multi test for inputs
    x = [np.array([]),
    np.array([2]),
    np.array(['a']),
    np.array([2,2,2,2]),
    np.array([2,2,'a',2]),
    np.array([2,2,6,4,5]),
    np.array([2.4,2.1,6.7,4.7,5.0,10.1])]

    # # # single large test
    # x = [np.random.randint(0,10000,10000)]

    # multi large test
    # x = [np.random.rand(100,i) for i in [(i + 1) * 100 for i in list(range(10))]]

    # multi smallish test
    # x = [np.random.rand(i) for i in [(i + 1) * 10 for i in list(range(50))]]
    #test
    accounts = []
    for i in x:
        if i.ndim == 1:
            ans = algs.quicksort(i)
            accounts.append((len(i),ans))
        elif i.ndim == 2:
            for j in i:
                ans = algs.quicksort(j)
                accounts.append((len(j),ans))
        else:
            None

    # speed testing
    # for i in [(i + 1) * 100 for i in list(range(10))]:
    #     a = np.random.rand(100,i)
    #     algs.bubblesort(a)

    return accounts

# bub = test_bubblesort()
# qui = test_quicksort()

# plt.plot(
#     # [i[0] for i in bub],
#     # [i[1][0] for i in bub],
#     # 'b',
#     # [i[0] for i in bub],
#     # [i[1][1] for i in bub],
#     # 'b--')
#     [i[0] for i in qui],
#     [i[1][0] for i in qui],
#     'g',
#     [i[0] for i in qui],
#     [i[1][1] for i in qui],
#     'g--')
# plt.xlabel('Length of sequence')
# plt.ylabel('Number of conditionals/assignments')
# plt.title('Assignments and Conditionals Scale with Input Size')
# plt.grid(True)
# plt.legend((#'Bubble: Assignments',
#             #'Bubble: Conditionals'
#             'Quick: Assignments',
#             'Quick: Conditionals'))
# plt.show()



