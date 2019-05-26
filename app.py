import argparse

import autopy
from PIL import Image


def screenshot(top_left, right_bottom, next_page, total_page):
    rect_size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
    images = []
    for i in range(total_page):
        page_num = "{}".format(i).zfill(len(str(total_page)))
        file_name = 'tmp/page-{}.png'.format(page_num)
        images.append(file_name)

        autopy.bitmap.capture_screen((top_left, rect_size)).save(file_name)
        autopy.mouse.move(*next_page)
        autopy.mouse.click(delay=1)

    return images


def image2pdf(images):
    pil_images = [Image.open(i) for i in images]
    pil_images[0].save('book.pdf', save_all=True, append_images=pil_images[1:])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take book screenshots.')
    parser.add_argument('top_left', type=str)
    parser.add_argument('right_bottom', type=str)
    parser.add_argument('next_button', type=str)
    parser.add_argument('total_page', type=int)

    args = parser.parse_args()

    top_left = tuple(map(lambda x: int(x), args.top_left.split(',')))
    right_bottom = tuple(map(lambda x: int(x), args.right_bottom.split(',')))
    next_button = tuple(map(lambda x: int(x), args.next_button.split(',')))
    total_page = args.total_page

    print("Take book screenshot at {} {} and next at {} with {} pages".format(
        top_left, right_bottom, next_button, total_page
    ))

    images = screenshot(top_left, right_bottom, next_button, total_page)
    image2pdf(images)
