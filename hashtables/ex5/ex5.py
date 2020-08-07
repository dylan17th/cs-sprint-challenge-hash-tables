
def finder(files, queries):

    query_cache = {}
    result = []

    for ele in queries:
        query_cache[ele] = ele

    for ele in files:
        new = ele.split("/")
        if new[-1] in query_cache:
            result.append(ele)

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
