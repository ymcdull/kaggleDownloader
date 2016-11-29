## Need to prepare "cookies.txt" file exported from google plugin "cookietxt-export"

## "pattern" package needed
## challenge_name hard-coded

from pattern import web
import subprocess
import requests

website = "https://www.kaggle.com"
challenge_name = "house-prices-advanced-regression-techniques"
url = "{}/c/{}/data".format(website, challenge_name)

page = requests.get(url).text.encode('ascii', 'ignore')
dom = web.Element(page)
table = dom.by_id("data-files")
a_elements = table.by_tag("a")


def download_check():
    files = []
    for i in range(len(a_elements)):
        this_el = a_elements[i]
        this_content = this_el.content
        file_with_size = this_el.href.split('/')[-1] + '\t' + this_content.split(' ', 1)[-1]

        files.append(file_with_size)

    print "Download Review:"
    for f in files:
        print f

def download(small_file_only = False):
    command_str = "wget --load-cookies=cookies.txt {}"
    for i in range(len(a_elements)):
        this_el = a_elements[i]
        file_url = website + this_el.href
        file_name = this_el.href.split('/')[-1]
        
        if small_file_only:
            this_content = this_el.content
            if this_content.strip().endswith(("kb)", "GB)")):
                print "Ignore large file: {}".format(file_name)
                print
                continue

        print("{} downloading...".format(file_name))
        command = command_str.format(file_url)
        subprocess.call(command, shell = True)
        print("{} finished...".format(file_name))
        print


if __name__ == "__main__":
#     download_check()
    download()
