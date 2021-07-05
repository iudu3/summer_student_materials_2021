#open the fasta input file and read it
input_file = open('\\Users\\19802\\Downloads\\SCOPE_sequences.txt', 'r')
#record what was read by writing it to another file
output_file = open('SCOPE_final_file.tsv','a')
#format the header! \t = tab
output_file.write('Gene\tA\tC\tT\tG\tGC\n')
#need Biopython sequence input/output library
from Bio import SeqIO
#for records created by Bio.SeqIO, 
for cur_rec in SeqIO.parse(input_file, "fasta"):
    #record the id and name
    gene_name = cur_rec.name
#count each nucleotide; sequence objects have a 'count' method which can be used to find number of times nucleotide is present
    A_count = cur_rec.seq.count('A')
    C_count = cur_rec.seq.count('C')
    T_count = cur_rec.seq.count('T')
    G_count = cur_rec.seq.count('G')
#find the gc value; first find length of the sequence
    length = len(cur_rec.seq)
#find the gc%
    gc_value = float(G_count + C_count) / length

#CNP ratios; first define the formula
#def genome_formula (A,T,Cy,G):
	#C = float((A*5*2) + (Cy*4*2) + (T*5*2) + (G*5*2))
	#N = float((A*5) + (Cy*3) + (T*2) + (G*5))
	#P = float(A + Cy + T + G)
	#output = (C/P,':',N/P,':',P/P)
	#return output

#def z_formula (Z,T,Cy,G):
	#C = float((Z*5*2) + (Cy*4*2) + (T*5*2) + (G*5*2))
	#N = float((Z*6) + (Cy*3) + (T*2) + (G*5))
	#P = float(Z + Cy + T + G)
	#output = (C/P,':',N/P,':',P/P)
	#return output    
#ratio_1= genome_formula(A_count,T_count,C_count,G_count)
#ratio_2= z_formula(A_count,T_count,C_count,G_count)

#Calculating C:N content of capsid

#def content_formula (x,y):
        #r = 28
        #Carbon = float((4*3.143*x))*((3*(r**2)*2.5)-(3*(2.5**2)*r)+(2.5**3))
        #Nitrogen = float((4*3.143*y))*((3*(r**2)*2.5)-(3*(2.5**2)*r)+(2.5**3))
        #output = Carbon,':',Nitrogen
        #return output
#Carbon
#Ca = 31
#Nitrogen
#Ni = 8.7
#print(content_formula(Ca,Ni))

#Calculating C:N content of tail

#def tail_formula (length,radius):
        #Car = float((Ca*length*3.143)*((radius**2)-(radius - 2.5)**2))
        #Nit = float((Ni*length*3.143)*((radius**2)-(radius - 2.5)**2))
        #output = Car,':',Nit
        #return output
#l = 120
#ra = 3
#print(tail_formula(1,ra))

#formatting stuff! 
    output_line = '%s\t%i\t%i\t%i\t%i\t%f\n' % \
    (gene_name, A_count, C_count, T_count, G_count, gc_value)

#save the line of text to an output file
    output_file.write(output_line)
#close the output file
output_file.close()
#close the input file
input_file.close()

