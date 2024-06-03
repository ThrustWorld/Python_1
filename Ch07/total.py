input_file_name = input("Input file name: ")
output_file_name = input("Output file name: ")

infile = open(input_file_name,"r") # file aperto in lettura, percorso relativo che parte dalla root directory
outfile = open(output_file_name, "w") # file aperto in scrittura

total = 0.0
counter = 0

line = infile.readline() # legge e restituisce riga di testo
while line != "":
    value = float(line)
    outfile.write("%15.2f \n" % value)
    total += value
    counter += 1
    line = infile.readline()

outfile.write("%15s \n" % "---------") # Scrive sul file designato per la scrittura
outfile.write("Total: %8.2f \n" % total)

average = total / counter
outfile.write("Average: %6.2f \n" % average)

infile.close() # termina di lavorare sul file
outfile.close()