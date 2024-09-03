def levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    distance_matrix = [[0 for _ in range(len(s2) + 1)]
                       for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        distance_matrix[i][0] = i
    for j in range(len(s2) + 1):
        distance_matrix[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                distance_matrix[i][j] = distance_matrix[i - 1][j - 1]
            else:
                distance_matrix[i][j] = 1 + min(
                    distance_matrix[i - 1][j - 1],
                    distance_matrix[i - 1][j],
                    distance_matrix[i][j - 1]
                )

    return distance_matrix[-1][-1]
