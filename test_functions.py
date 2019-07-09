import pytest
import functions as fn

def test_clean_text():
    pre1 = "aBc D3fgh1j.k"
    post1 = "ABCDFGHJK"
    
    pre2 = "-234./!"
    post2 = ""
    
    assert fn.clean_text(pre1) == post1,"test failed"
    assert fn.clean_text(pre2) == post2,"test failed"

def test_caesar_text():
    pre1 = "aBc D3fgh1j.k"
    post1 = "ABC DFGHJK"
    
    pre2 = "-234./!"
    post2 = ""

    assert fn.caesar_text(pre1) == post1,"test failed"
    assert fn.caesar_text(pre2) == post2,"test failed"
    
    
def test_caesar():
    word1 = "apple"
    word2 = "APPLE"
    word3 = "A PP LE"
    word4 = "App13"
    
    assert fn.caesar(word1,2) == "CRRNG"
    assert fn.caesar(word2,2) == "CRRNG"
    assert fn.caesar(word3,2) == "C RR NG"
    assert fn.caesar(word4,2) == "CRR"