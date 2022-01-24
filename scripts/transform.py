import pandas as pd

# Saving text files to a variable
clinical_df = 'data/TCGA_OV_CLINICAL_DF.txt';
counts_df = 'data/TCGA_OV_COUNTS_DF.txt';
gene_annot_df = 'data/TCGA_OV_GENE_ANNOT.txt';
sample_df_info = 'data/TCGA_OV_SAMPLE_INFO.txt';
tmm_cpm_df = 'data/TCGA_OV_TMM_CPM_DF.txt';

# Reading each text file into a pandas dataframe for easy manipulation
clinical_pd = pd.read_table(clinical_df, sep = '\s+');
count_pd = pd.read_table(counts_df, sep='\s+');
gene_annot_pd = pd.read_table(gene_annot_df, sep = '\s+');
sample_info_pd = pd.read_table(sample_df_info, sep = '\s+');
tmm_cpm_pd = pd.read_csv(tmm_cpm_df, sep = '\s+');


# Missing data in clinical datacounframe: Columns containing missing data are
# days to birth, days to death, year of death, age at diagnosis,
# days to last follow up, figo stage, age at diagnosis,
# os time.


# Rename columns  to be consistent with clinical_df
sample_info_pd.rename(columns={'File.ID': 'file_id', 'File.Name': 'filename', 'Data.Category': 'data_category', 'Data.Type': 'data_type',
                               'Project.ID': 'project_id', 'Case.ID': 'case_submitter_id', 'Sample.ID': 'sample_id', 'Sample.Type': 'sample_type'},
                      inplace = True)
gene_annot_pd.rename(columns={'SYMBOL': 'symbol', 'GENEID': 'gene_id'}, inplace= True);
count_pd.rename(columns={'ENSEMBL_ID': 'gene_id'}, inplace = True);

# Reshaping dataframe
count_pd_melted = pd.melt(count_pd, ['gene_id'])
