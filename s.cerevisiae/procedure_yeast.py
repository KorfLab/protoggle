import gzip
import json_object_list_handler


class yeast_mutant(object):
    species = "Saccharomyces cerevisiae"
    molecular_mutation = "N/A"

    def __init__(self, id):
        self.id = id
    pass

def first_use():

    infile = gzip.open("conditional_phenodata.tab.gz", "rt")

    temp_alleles = ["ts allele", "temperature sensitive", "temperature-sensitive", "temperature-inducible degron", "-ts"]

    allels = []

    # If there is an allele_name we use it
    #We have already narrowed down with awk to produce these

    for line in infile:
        line_splits = line.split("\t")
        #print(line)
        # line_splits[5] is the allele name
        if (line_splits[5]) == " ":
            continue
        if any(word in line_splits[5] for word in temp_alleles):
            allels.append(line)

    # Let's create an object that can hold these
    # Let's make the id "Yeast"+allele

    '''One = yeast_mutant("spam")
    
    print(One.species)'''


    # [0] = Gene name, [1] = feature type. [2] = gene ID [3] = Reference [4] = Not Important [5] = allele [6] = description

    # Use a dictionary
    object_list = []
    for entry in allels:
        entry_splits = entry.split("\t")
        entry_id = "Yeast_"+entry_splits[0]+"_"+entry_splits[5]
        entry_id = entry_id.replace(" ", "")
        #print(entry_id)
        curr_mutant = yeast_mutant(entry_id)
        curr_mutant.Gene = entry_splits[0]
        curr_mutant.Feature_type = entry_splits[1]
        curr_mutant.SGD_ID = entry_splits[2]
        curr_mutant.Ref = entry_splits[3]
        curr_mutant.allele = entry_splits[5]
        curr_mutant.description = entry_splits[6]
        # Add this at the end
        object_list.append(curr_mutant)


    json_object_list_handler.JSONs_outfmt(object_list)

    mutants = json_object_list_handler.JSONs_open()

    return mutants

# Returns a list of all the mutant objects
def subsequent_use():
    return json_object_list_handler.JSONs_open()

mutants = subsequent_use()