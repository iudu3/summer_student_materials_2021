#Imports needed to complete below
import os
from Bio import SeqIO
from Bio import Entrez

#Always leet Entrez know who you are via providing email
Entrez.email = "iudu@spelman.edu"

#Open the file (Accension_numbers.txt) to read each accession number
with open("Accension_numbers.txt", "r") as reader:
#for every accession number (aka line) in the the file being read
     for line in reader:
#Come up with a filename (this actually didn;t turn out how I wanted it to, but it's fine. I can rework it another day).
          filename = line
#Straight from Biopython, except outhandle is "a" instead of "r", I provide the path for outhandle to go to to record the sequences. id is equal to the line name
          if not os.path.isfile(filename):
               # Downloading...
              
               net_handle = Entrez.efetch(
                    db="nucleotide", id= line, rettype="fasta", retmode="text"
               )
               out_handle = open("/Users/19802/Downloads/line", "a")
               out_handle.write(net_handle.read())
               out_handle.close()
               net_handle.close()
               print("Saved")
#Instead of Seq.IO read, use SeqIO.parse to go through the data separately, if not command line will not be able to read all the records
          record = SeqIO.parse("/Users/19802/Downloads/line", "fasta")
          print(record)
#It is good practice to close the reader
reader.close()    
