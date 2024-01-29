def non_dominated_sort(values1, values2):


    """
    this code is visualize in the research section that I wrote (Figure 1). 
    This code snippet is an implementation of the non-dominated sorting algorithm. It takes in two lists of values and assigns ranks to each value based on dominance relationships. 
    The output is a list of fronts, where each front contains the indices of non-dominated values.
    """

    S = [[] for _ in range(len(values1))]
    front = [[]]
    n = [0 for _ in range(len(values1))]
    rank = [0 for _ in range(len(values1))]

    for p in range(len(values1)):
        S[p] = []
        n[p] = 0
        for q in range(len(values1)):
            if (values1[p] > values1[q] and values2[p] > values2[q]) or (values1[p] >= values1[q] and values2[p] > values2[q]) or (values1[p] > values1[q] and values2[p] >= values2[q]):
                if q not in S[p]:
                    S[p].append(q)


            elif (values1[q] > values1[p] and values2[q] > values2[p]) or (values1[q] >= values1[p] and values2[q] > values2[p]) or (values1[q] > values1[p] and values2[q] >= values2[p]):
                n[p] += 1



        if n[p] == 0:
            rank[p] = 0

            if p not in front[0]:
                front[0].append(p)

 
 
 
    i = 0
    while front[i]:
        Q = []

        for p in front[i]:

            for q in S[p]:

                n[q] -= 1


                if n[q] == 0:

                    rank[q] = i + 1


                    if q not in Q:

                        Q.append(q)
        i += 1

        front.append(Q)

    del front[-1]


    return front