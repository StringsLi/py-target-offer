
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip("/").split("/")
        stack = []
        for i in path:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == '':
                pass
            else:
                stack.append(i)
        return "/" + "/".join(stack)


if __name__ == '__main__':
    obj = Solution()
    path = "/home/"
    print(obj.simplifyPath(path))
