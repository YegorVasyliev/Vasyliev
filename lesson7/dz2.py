if __name__ == '__main__':
    text = input().split()
    reserved = input().split()

    out = ''

    for word in text:
        if word in reserved:
            out += word.upper()
        else:
            out += word
        out += ' '

    print(out)













