import words

class TestWords:

    def test_concat_no_space(self):
        assert "TestWords" == words.concat_no_space("Test","Words")
    
    def test_concat_with_space(self):
        assert "Happy Birthday" == words.concat_with_space("Happy", "Birthday")
    
    def test_concat_fail(self):
        assert "Will Fail" == words.concat_no_space("Will", "Fail")