from html2image import Html2Image
hti = Html2Image()
hti.output_path = 'images/'

with open('barcodes.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        url = f'http://3.136.112.72:8010/product/{line}/'
        save_as = f'{line}.png'
        print(url, ' --- ', end='')
        hti.screenshot(url=url, save_as=save_as)
        print('done')
        
    
    