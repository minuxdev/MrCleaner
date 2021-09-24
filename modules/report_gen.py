def report_generator(path, dub_files, sizes, base_converter):
    with open(f'{path}/Report.txt', 'w') as rep:
        rep.write('{:=^79}\n\n'.format(' DUPLICATED FILES '))
        for l in range(len(dub_files)):
            rep.write(f'{l+1} - {dub_files[l]}  -  {base_converter(sizes[l])}\n')

