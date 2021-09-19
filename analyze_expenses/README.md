# 楽天カード明細分析用スクリプト

## CSV集計 

CSVを一括で読み込んで、グループ化したものをCSV出力する

### usage

```
pipenv run ./analyze_expenses.py -d <dirname>
```

- dirname: CSVの格納パス

### output

- ExpensesReport_YYMMDD.csv
