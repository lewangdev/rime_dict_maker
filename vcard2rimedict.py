def get_names(vcardfilepath, line_prefix="N:"):

    with open(vcardfilepath, 'r') as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith(line_prefix):
                name = line[2:].replace(';', '')
                print(name)


if __name__ == "__main__":
    vcardfilepath = "./vcard/iCloud vCard.vcf"
    get_names(vcardfilepath)

