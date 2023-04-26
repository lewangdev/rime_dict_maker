import pypinyin
from datetime import datetime
initials_set = set(pypinyin.style._constants._INITIALS)


def check_zhchar(phrase):
    for c in phrase:
        if ord(c) not in pypinyin.pinyin_dict.pinyin_dict:
            return False
    return True


def convert2pinyin(name):
    name_pinyin = []
    for v in name.split():
        if len(v) == 2:
            if not check_zhchar(v[0]):
                continue

            pinyin = pypinyin.lazy_pinyin(v[0])
            for p in pinyin:
                if p in initials_set:
                    break
            else:
                name_pinyin.append(''.join(pinyin)) 

    return ''.join(name_pinyin)


def get_names(vcardfilepath, line_prefix="N:"):
    result = f"""---
name: contact
version: "{datetime.now().strftime('%Y-%m-%d')}"
sort: by_weight
...

    """

    with open(vcardfilepath, 'r') as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith(line_prefix):
                name = line[2:-1].replace(';', '')
                name_pinyin = convert2pinyin(name)
                result += name + '\t' + ' '.join(name_pinyin) + '\t' + '10000' + '\n'
    return result


if __name__ == "__main__":
    vcardfilepath = "./vcard/iCloud vCard.vcf"
    result = get_names(vcardfilepath)

    with open('contact.dict.yaml', 'w') as f:
        f.write(result)


