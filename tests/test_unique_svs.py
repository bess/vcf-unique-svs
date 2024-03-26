import pytest
import os
from src.unique_svs import UniqueSvs
import pdb
import shutil


def test_create_dataframe():
    fixture_file = "tests/fixtures/GDN.set1.fixture.tsv"
    vcf_unique_svs = UniqueSvs(fixture_file)
    dataframe = vcf_unique_svs.dataframe
    assert (dataframe.size) == 11160


def test_get_sample_column_names():
    fixture_file = "tests/fixtures/GDN.set1.fixture.tsv"
    vcf_unique_svs = UniqueSvs(fixture_file)
    assert (vcf_unique_svs.sample_ids()) == {
        "GDN41BL",
        "GDN131BL",
        "GDN71BL",
        "GDN111BL",
        "GDN101BL",
        "GDN51BL",
        "GDN91BL",
    }

def test_output_dir_name():
    fixture_file = "tests/fixtures/GDN.set1.fixture.tsv"
    vcf_unique_svs = UniqueSvs(fixture_file)
    assert (vcf_unique_svs.output_dir_name()) == "GDN.set1.fixture_unique_svs"

def test_make_a_directory_for_output():
    fixture_file = "tests/fixtures/GDN.set1.fixture.tsv"
    vcf_unique_svs = UniqueSvs(fixture_file)
    output_dir = vcf_unique_svs.output_dir_name()
    shutil.rmtree(output_dir, ignore_errors = True)
    assert (os.path.isdir(output_dir)) == False
    vcf_unique_svs.create_output_dir()
    assert (os.path.isdir(output_dir)) == True
    shutil.rmtree(output_dir) 

def test_output_files():
    fixture_file = "tests/fixtures/GDN.set1.fixture.tsv"
    vcf_unique_svs = UniqueSvs(fixture_file)
    vcf_unique_svs.export()
    output_dir = vcf_unique_svs.output_dir_name()
    assert (os.path.isdir(output_dir)) == True
    lst = os.listdir(output_dir)
    assert (len(lst)) == 4 # There should be 4 output files for this sample
    shutil.rmtree(output_dir, ignore_errors = True)