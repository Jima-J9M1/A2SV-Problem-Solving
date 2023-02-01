class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0
        merge = "" 



        while ptr1 < len(word1) and ptr2 < len(word2):

            if word1[ptr1] > word2[ptr2]:
                merge += word1[ptr1]
                ptr1 += 1

            elif word1[ptr1] < word2[ptr2]:
                merge += word2[ptr2]
                ptr2 += 1


            else:

                val_1 = word1[ptr1: ]
                val_2 = word2[ptr2: ]

                if  val_1 > val_2:

                    while ptr1 < len(word1) and word1[ptr1] >= word2[ptr2] and  word1[ptr1: ] > word2[ptr2:]:
                        merge += word1[ptr1]
                        ptr1 += 1

                elif val_1 < val_2:

                    while ptr2 < len(word2) and word1[ptr1] <= word2[ptr2] and  word1[ptr1: ] < word2[ptr2:]:
                        merge += word2[ptr2]
                        ptr2 += 1
                else:
                    while ptr2 < len(word2) and word1[ptr1: ] == word2[ptr2: ]:
                        merge += word2[ptr2]
                        ptr2 += 1
                    
                                     
                                     
        if ptr1 < len(word1):
            merge += word1[ptr1:]

        elif ptr2 < len(word2):
            merge += word2[ptr2:]

        return merge
  