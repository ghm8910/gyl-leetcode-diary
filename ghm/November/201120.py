def replaceSpace(s: str) -> str:
    result = []
    for c in s:
        if c == ' ':
            result.append("%20")
        else:
            result.append(c)
    return ''.join(result)


class Solution:
    pass


if __name__ == '__main__':
    print(replaceSpace("We are happy."))
