.PHONY: data train test api lint clean help

help: ## Bu yardım mesajını gösterir
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

data: ## Kaggle'dan veri indir
	kaggle datasets download blastchar/telco-customer-churn -p data/raw/ --unzip

train: ## Modeli eğit
	python src/models/train.py

test: ## Testleri çalıştır
	pytest tests/ -v --tb=short

api: ## API'yi başlat
	uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

lint: ## Kod kalitesini kontrol et
	ruff check src/ api/ tests/
	ruff format --check src/ api/ tests/

format: ## Kodu otomatik formatla
	ruff check --fix src/ api/ tests/
	ruff format src/ api/ tests/

clean: ## Geçici dosyaları temizle
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

