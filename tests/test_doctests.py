from tools.doctests import doctests

def test_doctests_multiple_files():
    for path in [
        'tools/ls.py',
        'tools/cat.py',
        'tools/grep.py',
        'tools/rm.py',
        'tools/write_file.py',
        'tools/write_files.py'
    ]:
        output = doctests(path)
        assert isinstance(output, str)
        assert "Trying:" in output