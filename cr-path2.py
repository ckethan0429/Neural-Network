from urllib.parse import urljoin

base="http://example.com/html/a.html"

print(urljoin(base, "/hoge.html"))
print(urljoin(base, "http://www.naver.com"))
print(urljoin(base, "../index.html"))
print(urljoin(base, "../img/hoge.png"))
print(urljoin(base, "../css/hoge.css"))