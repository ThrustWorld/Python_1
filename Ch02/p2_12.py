disk_letter = input("Disco in cui è presente il file: ")
file_path = input("Percorso in cui è presente il file: ")
file_name = input("Nome del file: ")
file_extension = input("Estensione del file: ")

complete_file_path = disk_letter + ":\\" + file_path + "\\" + file_name + "." + file_extension # Concatenazione stringhe

print(complete_file_path)