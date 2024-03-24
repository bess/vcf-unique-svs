
import pytest
import os
from src.unique_svs import UniqueSvs

def test_action():
    testfile = os.path.relpath("fixtures/GDN.set1.fixture.tsv", start=os.curdir)
    vcf_unique_svs = UniqueSvs()
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"

# @pytest.fixture
# def test_action():
#     print(testfile)
#     assert(testfile == "foo")
#     # vcf_unique_svs = UniqueSvs(file: )
#     # assert vcf_unique_svs.action(1) == 1
