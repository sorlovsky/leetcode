def findLongestChain(pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        chain = []
        # count = 1

        def build(chain):
            print('BUILD!!!')
            print(chain)
            for pair in pairs:
                print('Current chain', chain)
                print('Current pair', pair)
                if len(chain) == 0:
                    chain.append(pair)
                else:
                    # add to the end
                    if chain[-1][1] < pair[0]:
                        chain.append(pair)
                    # potentially re-adjust the chain
                    else:
                        for i in range(len(chain)):
                            # print(pair)
                            # a
                            print(pair[1], chain[i][0])
                            if pair[1] < chain[i][0]:
                                if pair[1] < chain[i][0]:
                                    chain.insert(i, pair)
                                    chain = build(chain)
                                else:
                                    chain.pop(i)
                                    chain.insert(i, pair)
                                break 
                # print(count, chain)
                # count += 1
                print('---')

            return chain

        chain = build(chain)
        return chain


# pairs = [[3,4],[2,3],[1,2],[5,6]]
pairs = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
print(findLongestChain(pairs))