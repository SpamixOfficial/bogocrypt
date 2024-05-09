from sys import exit

import argparse, time, random, os, json

def bogocrypt(file, output="a"):
    tempindex = 0
    chardict = {}
    tempdict = {}
    decryption = {}
    tempstr = ""
    finalstr = ""
    print(f"Encrypting file \"{file}\"")
    with open(file, 'r') as f:
        data = f.read()#.replace('\n', '')
        chars = len(data)
    for i in range(0, chars):
        if not data[i] in chardict:
            while True:
                ustr = random.randint(32,255)
                randomchar = chr(ustr)
                if not str(ustr) in list(decryption.values()):
                    break
            chardict[data[i]] = f"$[temp{tempindex}]"
            tempdict[f"$[temp{tempindex}]"] = randomchar
            decryption[str(ord(data[i]))] = str(ustr)
            tempindex += 1
        tempstr += chardict[data[i]]

    finalstr = tempstr
    for value in tempdict:
        finalstr = finalstr.replace(value, tempdict[value])
    print(f"Writing output to \"{output}\"")
    with open(output, 'w') as f:
        if os.path.exists(output):
            f.truncate()
            f.write(finalstr)
        else:
            f.write(finalstr)
        f.close()
    if os.path.exists(f"{output}.decryption.json"):
        index = 0
        while True:
            if os.path.exists(f"{output}.decryption.{index}.json"):
                index += 1
            else:
                break

        with open(f"{output}.decryption.{index}.json", 'w') as f:
            f.truncate()
            json.dump(decryption, f, indent=4)
            f.close()
        
    else:
        with open(f"{output}.decryption.json", 'w') as f:
            f.truncate()
            json.dump(decryption, f, indent=4)
            f.close()

def bogodecrypt(file, output, table):
    with open(table) as f:
        decryption = json.load(f)
    finalstr = ""
    keys = list(decryption.keys())
    values = list(decryption.values())

    print(f"Decrypting file \"{file}\"")
    with open(file, 'r') as g:
        data = g.read()
        chars = len(data)
    for i in range(0, chars):
        if str(ord(data[i])) in values:
            position = values.index(str(ord(data[i])))
            finalstr += chr(int(keys[position]))
    print(f"Writing output to \"{output}\"")
    with open(output, 'w') as h:
        h.truncate()
        h.write(finalstr)
        h.close()
    

parser = argparse.ArgumentParser(description='Encode your files so good you won\'t even find out how to decode them!')
parser.add_argument('file', metavar='file', type=str, nargs=1,
                   help='The file to encrypt')
parser.add_argument('-o', '--output', metavar="Y", type=str, nargs=1,
                   help="The output file")
parser.add_argument('-d', '--decrypt', action='store_true', help="Decrypt a file")
parser.add_argument('-s', '--skip', action='store_true', help="Skip countdown")
parser.add_argument('-t', '--table', metavar="T", type=str, nargs=1,
                   help="The decryption table. NOTE: Should ONLY be used if argument -d is specified!")
args = parser.parse_args()

if args.decrypt:
    if not args.table:
        print("To decrypt a file a decryption table is needed.\nUse -t {some json file} to specify a table.")
        exit(1)
    if not args.skip:
        print("Welcome to BogoCrypt, your file will be painfully decrypted in:")
        for i in range(0, 5):
            print(f"{(5-i)}", end="", flush=True)
            for point in range(0, 9):
                print(".", end="", flush=True)
                time.sleep(0.1)
            print(".")
    bogodecrypt(file=args.file[0], output=args.output[0], table=args.table[0])
elif args.file:
    if not args.output:
        while True:
            confirm = input("Since no output file was specified using \"-o\", the input file will be overwritten with the new encrypted file.\nARE YOU SURE YOU WANT TO DO THIS? (y/N)\n")
            if confirm.lower() == "y" or confirm.lower() == "n":
                break
            elif not confirm.lower():
                print("No option was specified, using default option \"N (No)\".")
                exit(0)
            elif confirm.lower() != "y" and confirm.lower() != "n":
                print("Answer must be \"y\" or \"n\"!\nPlease try again...\n")
        if confirm.lower() == "y":
            print("Action confirmed, now there's no going back!")
            if not args.skip:
                print("Starting in...")
                for i in range(0, 5):
                    print(f"{(5-i)}", end="", flush=True)
                    for point in range(0, 9):
                        print(".", end="", flush=True)
                        time.sleep(0.1)
                    print(".")
            bogocrypt(file=args.file, output=args.file)
    else:
        if not args.skip:
            print("Welcome to BogoCrypt, your file will be painfully encrypted in:")
            for i in range(0, 5):
                print(f"{(5-i)}", end="", flush=True)
                for point in range(0, 9):
                    print(".", end="", flush=True)
                    time.sleep(0.1)
                print(".")
        bogocrypt(file=args.file[0], output=args.output[0])
