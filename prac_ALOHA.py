import os
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "iudu@spelman.edu"  # Always tell NCBI who you are

file = open('Accension_numbers.txt','w')
file.writelines

if not os.path.isfile(filename):
    # Downloading...
    net_handle = Entrez.efetch(
        db="nucleotide", id="VTLG01000087.1", rettype="fasta", retmode="text"
    )
    out_handle = open(filename, "w")
    out_handle.write(net_handle.read())
    out_handle.close()
    net_handle.close()
    print("Saved")

print("Parsing...")
record = SeqIO.read(filename, "fasta")
print(record)

#whatchu wanna do - do this for every single accension number in accension_numbers.txt
#first you have to open the file
#then you have to read each line in the file
#for each line in that file
#do the entrez search
    #the id will be each line from the text file
#I want to have separate files for each of the line names
