
    # Pass in a VCF file
    # def __init__(self, file: str) -> None:
    #     self.file = file


#module load python
#script to create individual vcf files from multisample vcfs with unique variants.
#[TBD - script runs with 2 arguements which is the file name to be processed and 'trio' or 'proband']

# import sys
# import pandas as pd
# import numpy as np
# import csv

# probands = []

# def main():
    
#     arg = sys.argv[1]
#     #argv is the name of file to be processed
    
#     df = pd.read_csv(arg, sep='\t')
#     #read tsv file into pandas data framework
    
#     columns = np.array(df.columns)
#     #df.columns returns column names
#     #print(columns)
#     #np.array creates new instance of an array out of the column names
#     #pandas dataframe (df) remains intact
    
#     columns2exclude = ['AnnotSV_ID', 'SV_chrom', 'SV_start', 'SV_end', 'SV_length', 'SV_type', 'Samples_ID', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'Annotation_mode', 'CytoBand', 'Gene_name', 'Gene_count', 'Tx', 'Tx_start', 'Tx_end', 'Overlapped_tx_length', 'Overlapped_CDS_length', 'Overlapped_CDS_percent', 'Frameshift', 'Exon_count', 'Location', 'Location2', 'Dist_nearest_SS', 'Nearest_SS_type', 'Intersect_start', 'Intersect_end', 'RE_gene', 'P_gain_phen', 'P_gain_hpo', 'P_gain_source', 'P_gain_coord', 'P_loss_phen', 'P_loss_hpo', 'P_loss_source', 'P_loss_coord', 'P_ins_phen', 'P_ins_hpo', 'P_ins_source', 'P_ins_coord', 'po_P_gain_phen', 'po_P_gain_hpo', 'po_P_gain_source', 'po_P_gain_coord', 'po_P_gain_percent', 'po_P_loss_phen', 'po_P_loss_hpo', 'po_P_loss_source', 'po_P_loss_coord', 'po_P_loss_percent', 'P_snvindel_nb', 'P_snvindel_phen', 'B_gain_source', 'B_gain_coord', 'B_gain_AFmax', 'B_loss_source', 'B_loss_coord', 'B_loss_AFmax', 'B_ins_source', 'B_ins_coord', 'B_ins_AFmax', 'B_inv_source', 'B_inv_coord', 'B_inv_AFmax', 'po_B_gain_allG_source', 'po_B_gain_allG_coord', 'po_B_gain_someG_source', 'po_B_gain_someG_coord', 'po_B_loss_allG_source', 'po_B_loss_allG_coord', 'po_B_loss_someG_source', 'po_B_loss_someG_coord', 'TAD_coordinate', 'ENCODE_experiment', 'GC_content_left', 'GC_content_right', 'Repeat_coord_left', 'Repeat_type_left', 'Repeat_coord_right', 'Repeat_type_right', 'Gap_left', 'Gap_right', 'SegDup_left', 'SegDup_right', 'ENCODE_blacklist_left', 'ENCODE_blacklist_characteristics_left', 'ENCODE_blacklist_right', 'ENCODE_blacklist_characteristics_right', 'ACMG', 'HI', 'TS', 'DDD_HI_percent', 'ExAC_delZ', 'ExAC_dupZ', 'ExAC_cnvZ', 'ExAC_synZ', 'ExAC_misZ', 'GenCC_disease', 'GenCC_moi', 'GenCC_classification', 'GenCC_pmid', 'OMIM_ID', 'OMIM_phenotype', 'OMIM_inheritance', 'OMIM_morbid', 'OMIM_morbid_candidate', 'LOEUF_bin', 'GnomAD_pLI', 'ExAC_pLI', 'AnnotSV_ranking_score', 'AnnotSV_ranking_criteria', 'ACMG_class'
# ]
#     #removes all columns names except sampleID column names
    
#     sampleIDs = set(columns) - set(columns2exclude)
    
#     #print(sampleIDs)
    
#     for sample in sampleIDs:
#         matching_lines = df[df.Samples_ID == sample] 
#         #only returns lines from the pandas dataframe where the SampleID field matches the sample ID exactly
#         #print(matching_lines)
#         if matching_lines.index.empty:
#             continue
    
#         file = open(sample + '_unique.tsv', 'w')
#         #create file per sampleID
#         tsv_writer = csv.writer(file, delimiter='\t')
#         #print values with tab delimiters
#        # tsv_writer.writerow(columns2exclude)
#         #print column headers
#         matching_lines.to_csv(file, sep='\t', index=False)
        
#         file.close()
    
   
# main()
