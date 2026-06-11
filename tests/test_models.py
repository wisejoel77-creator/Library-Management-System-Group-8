from models.member import Member

def test_member():
    m = Member("John", "john@email.com")
    assert m.name == "John"