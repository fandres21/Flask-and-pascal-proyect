import requests as r

dd = {'img': ['a.jpg', 'b.jpg','c.jpg', 'd.jpg' , 'e.jpg']}

url = 'http://127.0.0.1:4000/im_data'

for i in dd['img']:
    files = {'img': open(f'figuras/{i}', 'rb')}
    res = r.post(url, files=files)
    print('Status: ',res.status_code)