
import csv
import os


def write_row(line, outf):
    line = line.strip('\n')
    line = line.split(',')
    letter = line[0]
    x_box = line[1]
    y_box = line[2]
    width = line[3]
    height = line[4]
    onpix = line[5]
    x_bar = line[6]
    y_bar = line[7]
    x_twobar = line[8]
    y_twobar = line[9]
    xy_bar = line[10]
    x_two_ybr = line[11]
    xy_two_br = line[12]
    x_edge = line[13]
    x_edge_vs_y = line[14]
    y_edge = line[15]
    y_edge_vs_x = line[16]

    outf.writerow([letter, x_box, y_box, width,
                  height, onpix, x_bar, y_bar,
                  x_twobar, y_twobar, xy_bar, x_two_ybr,
                  xy_two_br, x_edge, x_edge_vs_y, y_edge,
                  y_edge_vs_x])


def write_header(output_file):
    output_file.writerow(['letter', 'x_box', 'y_box', 'width', 'height',
                          'onpix', 'x_bar', 'y_bar', 'x2bar', 'y2bar',
                          'xybar', 'x2ybar', 'xy2bar', 'x_edge', 'xegvy',
                          'y_edge', 'yegvx'])


with open('letter-recognition.data') as f:
    lines = f.readlines()

    train = csv.writer(open('data/train_letters.csv', 'w'))

    write_header(train)

    for i, line in enumerate(lines):
        write_row(line, train)
        if i == 14000:
            print('training data complete')
            print('writing to test data')
            break
    f.close()

with open('letter-recognition.data') as f:
    test = csv.writer(open('data/test_letters.csv', 'w'))
    write_header(test)

    for i, line in enumerate(f.readlines()):
        if i > 14000:
            write_row(line, test)

    print('processing done')

    f.close()

