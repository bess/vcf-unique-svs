import pandas as pd
from pathlib import Path
import numpy as np
import os
import pdb
import csv


# Given a VCF file (https://en.wikipedia.org/wiki/Variant_Call_Format):
# 1. Determine the sample ids referenced in this file (these can vary in name and number)
# 2. Create a separate output VCF file for each sample id
# 3. Into each output file, place only the variants for which this sample id is a 1/0
# (i.e., exclude anything that is commonly found in the population, because that won't
# be a likely culprit for clinical significance.)
class UniqueSvs:
    # Pass in a VCF file, and read it in as a tab delimited CSV.
    def __init__(self, file: str) -> None:
        self.filename = file
        self.dataframe = pd.read_csv(file, sep="\t")
        pass

    # From the full VCF dataframe, remove all columns that are not sample ids.
    # This will leave us with only the names of the sample ids in this VCF.
    def sample_ids(self):
        columns = np.array(self.dataframe.columns)
        sampleIDs = set(columns) - set(UniqueSvs.columns2exclude)
        return sampleIDs
    
    def output_dir_name(self):
        return Path(self.filename).stem + "_unique_svs"

    # Create a directory where the output will be written
    def create_output_dir(self):
        output_dir = self.output_dir_name()
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    columns2exclude = [
        "AnnotSV_ID",
        "SV_chrom",
        "SV_start",
        "SV_end",
        "SV_length",
        "SV_type",
        "Samples_ID",
        "ID",
        "REF",
        "ALT",
        "QUAL",
        "FILTER",
        "INFO",
        "FORMAT",
        "Annotation_mode",
        "CytoBand",
        "Gene_name",
        "Gene_count",
        "Tx",
        "Tx_start",
        "Tx_end",
        "Overlapped_tx_length",
        "Overlapped_CDS_length",
        "Overlapped_CDS_percent",
        "Frameshift",
        "Exon_count",
        "Location",
        "Location2",
        "Dist_nearest_SS",
        "Nearest_SS_type",
        "Intersect_start",
        "Intersect_end",
        "RE_gene",
        "P_gain_phen",
        "P_gain_hpo",
        "P_gain_source",
        "P_gain_coord",
        "P_loss_phen",
        "P_loss_hpo",
        "P_loss_source",
        "P_loss_coord",
        "P_ins_phen",
        "P_ins_hpo",
        "P_ins_source",
        "P_ins_coord",
        "po_P_gain_phen",
        "po_P_gain_hpo",
        "po_P_gain_source",
        "po_P_gain_coord",
        "po_P_gain_percent",
        "po_P_loss_phen",
        "po_P_loss_hpo",
        "po_P_loss_source",
        "po_P_loss_coord",
        "po_P_loss_percent",
        "P_snvindel_nb",
        "P_snvindel_phen",
        "B_gain_source",
        "B_gain_coord",
        "B_gain_AFmax",
        "B_loss_source",
        "B_loss_coord",
        "B_loss_AFmax",
        "B_ins_source",
        "B_ins_coord",
        "B_ins_AFmax",
        "B_inv_source",
        "B_inv_coord",
        "B_inv_AFmax",
        "po_B_gain_allG_source",
        "po_B_gain_allG_coord",
        "po_B_gain_someG_source",
        "po_B_gain_someG_coord",
        "po_B_loss_allG_source",
        "po_B_loss_allG_coord",
        "po_B_loss_someG_source",
        "po_B_loss_someG_coord",
        "TAD_coordinate",
        "ENCODE_experiment",
        "GC_content_left",
        "GC_content_right",
        "Repeat_coord_left",
        "Repeat_type_left",
        "Repeat_coord_right",
        "Repeat_type_right",
        "Gap_left",
        "Gap_right",
        "SegDup_left",
        "SegDup_right",
        "ENCODE_blacklist_left",
        "ENCODE_blacklist_characteristics_left",
        "ENCODE_blacklist_right",
        "ENCODE_blacklist_characteristics_right",
        "ACMG",
        "HI",
        "TS",
        "DDD_HI_percent",
        "ExAC_delZ",
        "ExAC_dupZ",
        "ExAC_cnvZ",
        "ExAC_synZ",
        "ExAC_misZ",
        "GenCC_disease",
        "GenCC_moi",
        "GenCC_classification",
        "GenCC_pmid",
        "OMIM_ID",
        "OMIM_phenotype",
        "OMIM_inheritance",
        "OMIM_morbid",
        "OMIM_morbid_candidate",
        "LOEUF_bin",
        "GnomAD_pLI",
        "ExAC_pLI",
        "AnnotSV_ranking_score",
        "AnnotSV_ranking_criteria",
        "ACMG_class",
    ]
