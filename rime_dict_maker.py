from pypinyin import pinyin_dict, lazy_pinyin
from datetime import datetime
import os


def check_chinese_char(phrase):
    if len(phrase) == 0:
        return False
    for c in phrase:
        if ord(c) not in pinyin_dict.pinyin_dict:
            return False
    return True


def to_pinyin(name):
    name_pinyin = lazy_pinyin(name, errors='ignore')
    return ' '.join(name_pinyin)


def to_contact_dict(line_prefix="N:", weight=100000):
    result = f"""---
name: contact
version: "{datetime.now().strftime('%Y-%m-%d')}"
sort: by_weight
...

"""
    vcard_files = list(filter(lambda x: x.endswith(".vcf"), [
        i for i in os.listdir("./contact")]))

    for vcard_file in vcard_files:
        with open(os.path.join("./contact", vcard_file), 'r') as f:
            lines = f.readlines()

            for line in lines:
                if line.startswith(line_prefix):
                    name = line[2:-1].replace(';', '')
                    if not check_chinese_char(name):
                        continue
                    name_pinyin = to_pinyin(name)
                    result += f"{name}\t{name_pinyin}\t{weight}\n"
    return result


if __name__ == "__main__":
    result = to_contact_dict()

    with open(os.path.join("./out", "contact.dict.yaml"), 'w') as f:
        f.write(result)
