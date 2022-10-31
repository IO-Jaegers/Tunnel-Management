from os \
    import walk, path

pathToWireguardConfig = '/etc/wireguard'


def listConfiguration():
    global pathToWireguardConfig
    retVal = []
    
    for (dirpath, dirnames, files) in walk(pathToWireguardConfig):
        for fname in files:
            pathTo = path.join(dirpath, fname)
            name, ext = path.splitext(fname)

            if ext == '.conf':
                print(pathTo)
                retVal.append(pathTo)

    return retVal


def main():
    print(listConfiguration())



if __name__ == '__main__':
    main()