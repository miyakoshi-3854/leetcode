# leetcode

<a href="https://leetcode.com/u/miyakoshi-3854/">
    <img src="https://leetcard.jacoblin.cool/miyakoshi-3854" />
</a>

## 📝概要

leetcode用 python環境

## 🛠️環境構築

### 1. [`mise`](https://mise.jdx.dev/getting-started.html)をインストールする

### 2. 下記コマンドを実行

```bash
mise run setup
```

## 🚀使い方

### 1. 問題を解く

./main.pyを編集して問題を解く。

```bash
mise run p
```

### 2. 回答を保存

```bash
mise run sv
```

問題 (例: `1.aaa-bbb`) を入力すると:
- `_result/{problem}/main.py` に保存
- 同じ `problem` を解いた場合に、`problem_2` のように保存される
- 自動で `git commit`
- `main.py`がテンプレートにリセット

## 📂ディレクトリ構成

```bash
.
├── main.py                # 作業用メインファイル
├── .mise.toml             # 開発ツール管理 (mise)
├── .pre-commit-config.yaml # コードチェック自動化設定
├── shell/
│   └── solve.sh           # 解答保存用スクリプト
├── _template/             # テンプレートファイル格納
└── _result/               # 解答保存先
    └── {problem}/
        └── main.py
```
