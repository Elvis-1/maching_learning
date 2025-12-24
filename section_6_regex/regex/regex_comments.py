import re

def main():
    tag = '<div id="123">Hello</div>'
    result = re.match(
        r"""
            <div\s+ # match opening tag
            id="(\w+)" # match id attributes
            >       # end of opening tag
            ([^<>]+)   # match content of the tag
            </div>  # closign div tag

        """,tag,re.VERBOSE)
    id,content = result.groups()

    print(id,content)



main()