try:
    with open("text.txt", encoding="utf8") as r:
        mails = dict()
        for mail in r.read().split():
            name = mail[mail.index("@"):mail.index(":")]
            if name not in mails:
                mails[name] = []
            mails[name].append(mail)

        with open("answer.txt", "w", encoding="utf8") as w:
            for answer in mails.values():
                for i in answer:
                    w.write(i)
                    w.write("\n")
except FileNotFoundError as ex:
    raise FileNotFoundError("Не найден файл text.txt")
