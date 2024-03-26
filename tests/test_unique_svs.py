import pytest
import os
from src.unique_svs import UniqueSvs
import pdb


def test_create_dataframe():
    fixture_file = "tests/fixtures/GDN.set1.fixture.tsv"
    vcf_unique_svs = UniqueSvs(fixture_file)
    dataframe = vcf_unique_svs.dataframe
    assert (dataframe.size) == 11160


#
# def test_action():
#     print(testfile)
#     assert(testfile == "foo")
#     #
#     # assert vcf_unique_svs.action(1) == 1
