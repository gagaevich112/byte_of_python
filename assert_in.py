
full_string = 'fulltext'
substring =  'some_value'

def test_substring(full_string, substring):
    assert substring in full_sting, \
        f"expected {substring}, to be substring of {full_string}"

