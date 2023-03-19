from main import *


class TestApi:
    def test_status_code(self):
        url = 'https://jsonplaceholder.typicode.com/photos'
        res = send_http_request(url)

        assert check_status_code(res.status_code) == True

    def test_image_count_p(self):
        url = 'https://jsonplaceholder.typicode.com/photos'
        res = send_http_request(url)
        actual = len(res.json())
        expected = 5000
        assert actual == expected

    def test_image_count_n(self):
        url = 'https://jsonplaceholder.typicode.com/photos'
        res = send_http_request(url)
        actual = len(res.json())
        expected = 4000

        assert expected != actual

    def test_title(self):
        url = 'https://jsonplaceholder.typicode.com/photos'
        res = send_http_request(url)

        photos = res.json()
        contains_title_1 = False
        for photo in photos:
            if photo['title'] == 'reprehenderit est deserunt velit ipsam':
                contains_title_1 = True

        assert contains_title_1 == True

    def test_unique(self):
        url = 'https://jsonplaceholder.typicode.com/photos'
        res = send_http_request(url)
        photos = res.json()
        ids_list = []
        for photo in photos:
            ids_list.append(photo['id'])
        ids_set = set(ids_list)

        assert len(ids_set) == len(ids_list)

