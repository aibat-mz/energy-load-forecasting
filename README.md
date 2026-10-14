# energy-load-forecasting

## PJM Energy Load Forecasting

Проект прогнозирует нагрузку PJM на 24 часа вперёд. В ноутбуке сравниваются baseline-модели, XGBoost и CatBoost; для приложения выбран XGBoost. CatBoost нужен только для эксперимента и не входит в зависимости деплоя.

## Структура

- `notebook.ipynb` — анализ данных, формирование семи признаков и сравнение моделей.
- `PJME_hourly.csv` — исходные почасовые данные PJM, используемые в ноутбуке.
- `pjm-deployment/app.py` — Streamlit-приложение, загружающее XGBoost-модель.
- `pjm-deployment/xgboost_model.bin` — сохранённая модель XGBoost для приложения.
- `pjm-deployment/` — Dockerfile и зависимости приложения.

В приложении нужно вручную указать календарные признаки и значения нагрузки за 24, 48, 144 и 168 часов до прогнозируемого момента. Порядок и названия этих признаков совпадают с `FEATURES` в ноутбуке.

## Запуск приложения в Docker

Из каталога `pjm-deployment`:

```bash
docker build -t pjm-load-forecast .
docker run --rm -p 8501:8501 pjm-load-forecast
```

Затем откройте `http://localhost:8501`.

Ноутбук сохраняет обученную модель по пути `pjm-deployment/xgboost_model.bin` при запуске из корня проекта. Логи CatBoost и локальные виртуальные окружения в Git не добавляются.
