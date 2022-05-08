from fileinput import FileInput
from glob import glob
import os

# ATTENTION: there must not be 2 equal key or value
dict = {
    # potorpy only#--- "Ignore this. translate only: One"
    """\n  """: """#--- \"Ignore this. translate only: One\"\n\n  """,
    """ """: """#p--- \"Ignore this. translate only: One\"\n """,
    """:\n\n    # """: """:\n    # """,
    # not traslate
    """\n# game""": """    new \"\"\n\n# game""",
    # accapo
    """""": """\"
\"""",
    """""": """\"\n\"""",
    """""": """\"\n\"""",
    # ch #
    """# n \"""": """# [n] """,
    """# q \"""": """# [q] """,
    """# pc \"""": """# [pc] """,
    """# m \"""": """# [m] """,
    """# j \"""": """# [j] """,
    """# e \"""": """# [e] """,
    """# t \"""": """# [t] """,
    """# w \"""": """# [w] """,
    """# h \"""": """# [h] """,
    """# r \"""": """# [r] """,
    """# st \"""": """# [st] """,
    """# oc \"""": """# [oc] """,
    """# oc_ \"""": """# [oc_] """,
    """# ma \"""": """# [ma] """,
    """# t1 \"""": """# [t1] """,
    """# boss \"""": """# [boss] """,
    """# pcthink \"""": """# [pcthink] """,
    """# em \"""": """# [em] """,
    """# jess \"""": """# [jess] """,
    """# extend \"""": """# [extend] """,
    # search_text : replace_text
    """
translate crowdin""": """ ## translate crowdin""",
    """    # game""": """# XX## game""",
    """:
    # """: """:
msgid \"""",
    """\" nointeract""": """ [nointeract]\"""",
    """\" with fade""": """ [withfade]\"""",
    """\" with dissolve""": """ [withdissolve]\"""",
    """\" with slowdissolve""": """ [withslowdissolve]\"""",
    """\" with hpunch""": """ [withhpunch]\"""",
    """\" with flash""": """ [withflash]\"""",
    """\" with vpunch""": """ [withvpunch]\"""",
    """\" with Dissolve(2.0)""": """ [withDissolve(2.0)]\"""",
    # ch
    """   n \"""": """   \"[n] """,
    """   q \"""": """   \"[q] """,
    """   pc \"""": """   \"[pc] """,
    """   m \"""": """   \"[m] """,
    """   j \"""": """   \"[j] """,
    """   e \"""": """   \"[e] """,
    """   t \"""": """   \"[t] """,
    """   w \"""": """   \"[w] """,
    """   h \"""": """   \"[h] """,
    """   r \"""": """   \"[r] """,
    """   st \"""": """   \"[st] """,
    """   oc \"""": """   \"[oc] """,
    """   oc_ \"""": """   \"[oc_] """,
    """   ma \"""": """   \"[ma] """,
    """   t1 \"""": """   \"[t1] """,
    """   boss \"""": """   \"[boss] """,
    """   pcthink \"""": """   \"[pcthink] """,
    """   em \"""": """   \"[em] """,
    """   jess \"""": """   \"[jess] """,
    """   extend \"""": """   \"[extend] """,
    # Fix
    """\n    \"""": """\nmsgstr \"""",
    """msgstr \"\"[""": """msgstr \"[@""",
    """msgid \"\"[""": """msgid \"[@""",
    #Final
    """\n ## translate crowdin strings:\n\n""": """\n\n# XXtranslate crowdin strings:XX\n""",
    """:XX\n# XX## game""": """:XX# XX## game""",
    # date
    """HH:HH\n\n# game""": """HH:HH# game""",
    """HH:HH\n\n# XXtranslate""": """HH:HH# XXtranslate""",
    # potorpy only
    """msgstr \"[""": """msgstr \"\"[""",
    """    old \"""": """msgid \"[mschoice] """,
    """    new \"""": """msgstr \"[mschoice] """,
    """#p---""": """msgid_plural""",
    """#---""": """msgstr[1]""",
    """\" \"""": """ || """,
    """ || """: """' '""",
    """' '""": """\" \"""",
    """\" \"""": """ - """,
}


# Creating a function to replace the text
def replacetext(search_text, replace_text, pathFile):

    # Read in the file
    with open(pathFile, "r+", encoding="utf8") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(search_text, replace_text)

    # Write the file out again
    with open(pathFile, 'w', encoding="utf8") as file:
        file.write(filedata)
    return True


def replaceDictionary(pathFile, dict={}, reverse=False):
    print(pathFile)
    if(reverse):
        for item in reversed(list(dict.items())):
            replacetext(pathFile=pathFile,
                        search_text=item[1], replace_text=item[0])
    else:
        for search_text in dict.keys():
            replacetext(pathFile=pathFile, search_text=search_text,
                        replace_text=dict[search_text])


def getListFiles():
    # Get the list of all files and directories
    path = "game/tl/"
    dir_list = glob(path + "/**/*.rpy", recursive=True)
    return dir_list


def rpytopo():
    for path in getListFiles():
        replaceDictionary(path, dict=dict)


def potorpy():
    for path in getListFiles():
        replaceDictionary(path, dict=dict, reverse=True)


potorpy()
