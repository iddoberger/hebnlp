from hebnlp.lemmatizer import Lemmatizer


def test_lemmatizer():
    lemmatizer = Lemmatizer()
    assert lemmatizer.get_lemma("כלבים") == "כלב"
    assert lemmatizer.get_lemma("נבחו") == "נבח"
    assert lemmatizer.get_lemma("מילהלאקיימת") == None