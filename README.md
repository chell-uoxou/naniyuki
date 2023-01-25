# naniyuki
Generate your original hiroyuki
<img width="1680" alt="8ddf6af6-e22e-40ff-954d-2cc1edfb25ca" src="https://user-images.githubusercontent.com/12378384/214694271-b559de5a-0ddd-4288-be61-60a070e8c684.png">


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install naniyuki.

```bash
pip install -r requirements.txt
```

If you encountered some errors while installing `mecab-python3`, please read document: https://qiita.com/yukinoi/items/990b6933d9f21ba0fb43

## Usage

```bash
main.py [-h] [-v]
```

## Example
```
keyword?: 感想
ひろゆき 「それってあなたの感想ですよね」

keyword?: ハンバーグ
ハンバーグひろゆき 「それってあなたのハンバーグですよね」

keyword?: プリクラ
プリクラ博之 「それってあなたのプリクラですよね」

keyword?: 道草
道草博之 「それってあなたの道草ですよね」

keyword?: 餅
餅ゆき 「それってあなたの餅ですよね」

keyword?: 色
ひ色ゆき 「それってあなたの色ですよね」

keyword?:  南
南村博之 「それってあなたの南ですよね」

keyword?: はまぐり
はまぐり 「それってあなたのはまぐりですよね」

keyword?:  グミ
ひろグミ 「それってあなたのグミですよね」

keyword?: 雪
ひろ雪 「それってあなたの雪ですよね」

keyword?: 粉
粉雪 「それってあなたの粉ですよね」

keyword?: 恋
僕の彼女というか妻というか細君というか奥さんというか 「それってあなたの恋ですよね」

keyword?: メルティーキッス
降る雪 「それってあなたのメルティーキッスですよね」
```


## Options
```
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
```

<!---
## Usage

```python
import naniyuki

# generate new naniyuki
keyword = "感想"
naniyuki = Naniyuki(keyword)
name = naniyuki.getNaniyuki()
print(f"{name} 「それってあなたの{keyword}ですよね」")
```
-->

## Contributing

Pull requests are welcome.
