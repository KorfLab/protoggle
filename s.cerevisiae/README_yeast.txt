This is a note for the process used to find phenotype data and refine it on yeast

1. Download the full phenotype data from yeastmine

2. Observe and cross reference against their phenotype_readme.txt file to label the columns

3. Merge downloaded dataset with column names generated by previous step (manually done)

Ex: cat header_pheno.tab >> full_phenodata.tab | cat phenotype_yeast.tab >> full_phenodata.tab

{SKIP TO STEP 5 (LEFT IN AS REFERENCE TO MANIPULATE FULL_PHENO DATASET USING CUT COMMAND)}
{SKIP}4. Refine the columns down to what we are interested in:

Gene_name(col1), feature_type(col2), SGD_Gene_ID(col4), reference(col5), mutant_info(col7), Allele_name/Description(col8), phenotype(col10)

{SKIP}cut -f1,2,4,5,7,8,10 full_phenodata.tab > refined_phenotype_data.tab

5. Start narrowing the dataset down to what we care about (Currently the basics, that it is temperature sensitive mutation and a SNP)

	A. We are interested in conditional mutants so let's use awk to find '/conditional/'

	awk -F'\t' 'BEGIN {OFS = FS} /conditional/ {print $1,$2,$4,$5,$7,$8,$10}' full_phenodata.tab > conditional_phenodata.tab

	This complex command takes our full_phenodata.tab and finds the 'conditional' mutants, it then prints the columns we selected in step 4
	allowing us to skip step 4 and complete it in one line. OFS means Output Field Seperator which we set to '\t' using the -F command
	then setting it equivalent to the -F (Field Seperator).

#### Files #####

-full_phenodata.tab : Contains the contents of the yeast mine phenotype data along with newly added column names

-procedure_yeast.py : Python file to search the full_phenodata.tab for our specified features

-heat_sens_cond.txt : downloaded Gene-Ontology netword of genes with "heat_sensitivity"

-conditional_phenodata.tab : All mutants that result in conditional mutations. Currently over 4000 as per wc -l
