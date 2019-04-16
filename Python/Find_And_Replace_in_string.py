class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        S_c = S
        shift = 0
        indexs = [i[0] for i in sorted(enumerate(indexes), key=lambda x:x[1])]
        for i in range(len(indexes)):
            index = indexes[indexs[i]]
            source = sources[indexs[i]]
            target = targets[indexs[i]]
            length = len(source)
            if S[index:index+length] == source:
                S_c = S_c[:index+shift] + target + S_c[index+length+shift:]
                shift += len(target) - length
        return S_c
        
