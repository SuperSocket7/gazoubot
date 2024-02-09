# gazoubot
Misskeyで動くランダムな画像をノートするボット
## これは何ですか<br>詳細を説明します
元はTwitter APIの有料化に巻き込まれたまちカドまぞく画像botをMisskeyで復活させるために作ったプログラムです<br>
仕組みとしてはドライブにあるファイルをランダムで選んでノートするだけなので、まぞく以外のアニメの画像とかでも使えます。<br>
ドライブに投稿したい画像をアップロードして、.envに次のように書いて`$ python3 main.py`で実行してください、毎時00分00秒に実行されるようにできてます。
```
Token="YourToken" //設定から作れるアクセストークンも可
instance="msky.nekokawa.net" //インスタンスのアドレス。
icon="Edfcv6Cn_400x400.jpg" //アイコンのファイル名、アイコンが間違えてノートされるのを防ぎます
```
このボットはこのプログラムが使われています。
- [まちカドまぞく画像bot](https://msky.nekokawa.net/@syamisyamibot)
- [狐画像bot](https://msky.nekokawa.net/@FoxBot)