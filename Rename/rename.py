import os

path = str(input("Url: "))
index = str(input("Index: ")).upper()

def main():
    for count, file in enumerate(os.listdir(path)):

        filename, extension = os.path.splitext(f'{file}')

        dst = f"{index}-{(count+1):04}{extension}"
        src = f"{path}/{file}"
        dst = f"{path}/{dst}"

        os.rename(src, dst)

if __name__ == '__main__':
    main()