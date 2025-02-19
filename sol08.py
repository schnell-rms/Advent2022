
import time


def sol():
    start = time.perf_counter()

    file = open('inputs/input08.txt', 'r')
    forest = file.readlines()
    file.close()

    n = len(forest)
    m = len(forest[0].strip())
    is_visible = [[False] * m for i in range(n)]

    init_max = chr(ord('0')-1)

    visibility_score = [[1] * m for i in range(n)]

    for i in range(n):
        max_row = init_max
        row_visibility = [0] * m
        for j in range(m):
            if forest[i][j] > max_row:
                max_row = forest[i][j]
                is_visible[i][j] = True

            if j > 0:
                k = j - 1
                while k>0:
                    if (forest[i][j] > forest[i][k]):
                        k -= row_visibility[k]
                    else:
                        break

                row_visibility[j] = j - k

            visibility_score[i][j] *= row_visibility[j]

    for j in range(m):
        max_col = init_max
        col_visibility = [0] * n
        for i in range(n):
            if forest[i][j] > max_col:
                max_col = forest[i][j]
                is_visible[i][j] = True

            if i > 0:
                l = i - 1
                while l>0:
                    if (forest[i][j] > forest[l][j]):
                        l -= col_visibility[l]
                    else:
                        break
                
                col_visibility[i] = i - l

            visibility_score[i][j] *= col_visibility[i]

    for i in range(n-1, -1, -1):
        max_row = init_max
        row_visibility = [0] * m
        for j in range(m-1, -1, -1):
            if forest[i][j] > max_row:
                max_row = forest[i][j]
                is_visible[i][j] = True

            if j < m-1:
                k = j + 1
                while k<m-1:
                    if (forest[i][j] > forest[i][k]):
                        k += row_visibility[k]
                    else:
                        break
                
                row_visibility[j] = k - j

            visibility_score[i][j] *= row_visibility[j]

    for j in range(m-1, -1, -1):
        max_col = init_max
        col_visibility = [0] * n
        for i in range(n-1, -1, -1):
            if forest[i][j] > max_col:
                max_col = forest[i][j]
                is_visible[i][j] = True

            if i < n-1:
                l = i + 1
                while l < n-1:
                    if (forest[i][j] > forest[l][j]):
                        l += col_visibility[l]
                    else:
                        break
                
                col_visibility[i] = l - i

            visibility_score[i][j] *= col_visibility[i]

    score1 = sum([sum(x) for x in is_visible])
    score2 = max([max(v) for v in visibility_score])

    end = time.perf_counter()

    # print(visibility_score)

    print(f"Running time {end-start:.3f} seconds")

    print("First star: ", score1)
    print("Second star: ", score2)
    return


if __name__ == "__main__":
    sol()
