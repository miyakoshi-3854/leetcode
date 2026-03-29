# LeetCode 練習リポジトリ

## 環境
- Python 3.10
- パッケージ管理: uv
- タスクランナー: mise

## よく使うコマンド
| やること | コマンド |
|---------|---------|
| 解答実行 | `mise run p` |
| 解答保存 & commit | `mise run sv` |
| フォーマット | `mise run f` |
| lint | `mise run l` |

## ディレクトリ構成
- `main.py` — 今解いている問題（作業ファイル）
- `_result/{problem}/main.py` — 保存済み解答
  - 同じ問題を再提出すると `main_2.py` のように保存される
- `_template/main.py` — テンプレート

## 言語
- 常に日本語で会話すること