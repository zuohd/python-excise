import requests
from contextlib import closing


def download_img(url):
    response = requests.get(url, stream=True)
    print(response.status_code, response.reason)

    with open('test.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def downloadimg_improved(url):
    with closing(requests.get(url, stream=True)) as response:
        with open('test2.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__ == '__main__':
    url = 'https://pandao.github.io/editor.md/examples/images/8.jpg'
    # download_img(url)
    downloadimg_improved(url)
