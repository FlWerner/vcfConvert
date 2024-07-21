import csv

def csv_to_vcf(csv_filename, vcf_filename):
    with open(csv_filename, 'r') as csvfile:
        csv_reader_object = csv.reader(csvfile, delimiter=",")
        
        with open(vcf_filename, 'w', encoding='utf-8') as vcf_file:
            for row in csv_reader_object:
                bday = row[5].split(".")
                dmp = bday[2]+bday[1]+bday[0]
                vcf_file.write("BEGIN:VCARD\n")
                vcf_file.write("VERSION:3.0\n")
                vcf_file.write(f"N:{row[1]};{row[0]};;;\n")
                vcf_file.write(f"FN:{row[0]} {row[1]}\n")
                vcf_file.write(f"TEL;TYPE=CELL:{row[2]}\n")
                if row[3] is not "":
                    vcf_file.write(f"TEL;TYPE=HOME:{row[3]}\n")
                vcf_file.write(f"EMAIL:{row[4]}\n")
                if row[5] is not "":
                    vcf_file.write(f"BDAY:{dmp}\n")
                if row[6] is not "":
                    vcf_file.write(f"ADR;TYPE=HOME:;;{row[6]};{row[7]};;{row[8]};;\n")
                vcf_file.write("END:VCARD\n")


if __name__ == "__main__":
    csv_filename = 'MP-EXCEL.csv'  # Name der CSV-Datei mit Adresse
    vcf_filename = 'contacts_with_address.vcf'  # Name der zu erstellenden VCF-Datei
    csv_to_vcf(csv_filename, vcf_filename)
    print(f"Kontakte wurden von {csv_filename} nach {vcf_filename} konvertiert.")