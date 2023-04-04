html = ['</h1>', 'My content', '</h1>']
other_content_to_clean = ['', 'My content', 'Something else', '/']


# we use _ when we are not going to use what is store inside this variable
def remove_first_and_last(list_to_clean):
    _, *content, _ = list_to_clean
    return content


print(remove_first_and_last(other_content_to_clean))


# checking if list has 3 elements al least
def remove_first_and_last(list_to_clean):
    if len(list_to_clean) >= 3:
        _, *content, _ = list_to_clean
        return content
    else:
        return f'the list has only {len(list_to_clean)} elements'


print(remove_first_and_last(html))


# My bizarre solution
def remove_first_and_last(list_to_clean):
    del(list_to_clean[0])
    del(list_to_clean[-1])
    return list_to_clean


print(remove_first_and_last(other_content_to_clean))
