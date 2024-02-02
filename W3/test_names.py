from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Beniamina", "Tangatakino") == ("Tangatakino; Beniamina")
    assert make_full_name("Peka Tuteru Avake", "Takai") == ("Takai; Peka Tuteru Avake")
    assert make_full_name("Jean-Claude", "Van-Damne") == ("Van-Damne; Jean-Claude")
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Tangatakino; Beniamina") == ("Tangatakino")
    assert extract_family_name("Takai; Peka Tuteru Avake") == ("Takai")
    assert extract_family_name("Van-Damne; Jean-Claude") == ("Van-Damne")
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name("Tangatakino; Beniamina") == ("Beniamina")
    assert extract_given_name("Takai; Peka Tuteru Avake") == ("Peka Tuteru Avake")
    assert extract_given_name("Van-Damne; Jean-Claude") == ("Jean-Claude")
    assert extract_given_name("; ") == ""

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN",__file__])