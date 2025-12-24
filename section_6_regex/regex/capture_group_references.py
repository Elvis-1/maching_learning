import re

def main():
    # referencing capture groups ensures both opening a closing tags are thesame
    tag = '<div id="123">Hello</div>'
    result = re.match(
        r"""
            <(div)\s+ # match opening tag
            id="(\w+)" # match id attributes
            >       # end of opening tag
            ([^<>]+)   # match content of the tag
            </\1>  # closign div tag

        """,tag,re.VERBOSE)
    tag, id,content = result.groups()

    print(tag,id,content)



main()