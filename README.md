# Rime 输入法词库制作工具 Rime Dict Maker

## TODOs

- [-] iCloud vcard
- [ ] Epub books
- [ ] txt and html files
- [ ] sogou scel files

## HowTo

Install `rye`

```
$ cargo install --git https://github.com/mitsuhiko/rye rye
```

Update the project virtualenv

```
$ rye sync
```

## 生成词库

- 从 iCloud 下载通讯录到 contact 目录
- 执行 `python rime_dict_maker.py` 或着 `rye run make` 生成 `contact.dict.yaml`
