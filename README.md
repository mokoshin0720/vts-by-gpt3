# What
- GPT3を使った絵画の感想生成
    - 画像→感想生成AIのモデルを構築をするための調査
- `logs`内にこれまでの生成記録（作品 & 感想）を保存

# How to use
`src/sample.py`の`prompt`をいじることで作品にあった感想を生成させる
1. dockerの起動
```
$ make init
```

2. 感想を生成させたい作品・展示場所を入力
```
generate.py

work = '作品名'
museum = '展示場所'
```

3. 生成
```
$ make run
```