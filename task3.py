from pathlib import Path

def get_combined_text(*args):
    lines_list = []
    for arg in args:
        with open(arg, 'r', encoding='utf-8') as f:
            path = Path(arg)
            # В случае если нужно сохранить отступы в тексте, достаточно заменить метод strip на rstrip в анонимной функции
            lines = list(map(lambda x: x.strip(), f.readlines()))
            lines_list.append([path.name, len(lines), *lines])

    lines_list.sort(key=lambda x: x[1])

    for i in range(len(lines_list)):
        for j in range(len(lines_list[i])):
            with open('FilesTXT/Task3Result.txt', 'a', encoding='utf-8') as f:
                f.write(f'{str(lines_list[i][j])}\n')

get_combined_text('FilesTXT/1.txt', 'FilesTXT/2.txt', 'FilesTXT/3.txt')
